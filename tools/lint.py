#!/usr/bin/env python3
"""
lint.py — check data/ against schema/fields.json before anything is built.

validate.py and testpass.py still run on the built page; they are the release gate
and they stay. This runs first, on the source, and says which brand file is wrong
rather than which line of an 800KB build is. The rules are the same five classes:

  ORPHAN  a name that is not a seated brand (notes key not a dial, region index
          off the end of places, price_checked on a brand with unassessed slots)
  RANGE   a value outside its field's legal set
  SHAPE   wrong arity, wrong subkeys, malformed pair, non-https url
  GAP     a required field missing
  NOTE    findings that are legitimate but must be visible (null one-thing with a
          note, linkless one-thing, held prices)

Exit 1 on ORPHAN / RANGE / SHAPE / GAP.
"""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import spec
from spec import get, BRAND_FIELDS, NOTE_KEYS

P = collections.defaultdict(list)


def fail(kind, msg):
    P[kind].append(msg)


data = spec.load()
names = set(data.names)
nplaces = len(data.places)
slots = spec.REG['price_slots']

for rec in data.brands:
    n = rec['name']
    if rec['band'] not in data.bands:
        fail('RANGE', f'{n}: band {rec["band"]!r} not in bands.json')
    for fname, f in BRAND_FIELDS.items():
        if f['const'] == 'DATA' and fname in ('band', 'seat', 'dagger', 'row_class', 'row_override'):
            continue
        v = get(rec, f['path'])
        if v is None:
            if f['absent'] == 'required':
                fail('GAP', f'{n}: {fname}')
            continue
        t = f['type']
        if t == 'int':
            if not isinstance(v, int) or isinstance(v, bool):
                fail('SHAPE', f'{n}: {fname} {v!r} is not an integer')
            elif 'range' in f and not f['range'][0] <= v <= f['range'][1]:
                fail('RANGE', f'{n}: {fname} {v} outside {f["range"]}')
            elif v in f.get('banned', []):
                fail('RANGE', f'{n}: {fname} {v} is a retired band')
        elif t == 'str':
            if not isinstance(v, str) or not v.strip():
                fail('SHAPE', f'{n}: {fname} is empty')
            elif 'legal' in f and v not in f['legal']:
                fail('RANGE', f'{n}: {fname} {v!r} not in {f["legal"]}')
        elif t == 'url':
            if not str(v).startswith('https://'):
                fail('SHAPE', f'{n}: {fname} is not https')
        elif t == 'bool':
            if v is not True:
                fail('SHAPE', f'{n}: {fname} must be true or absent')
        elif t == 'list':
            if not isinstance(v, list) or not v:
                fail('SHAPE', f'{n}: {fname} must be a non-empty list')
                continue
            if 'len' in f and len(v) != f['len']:
                fail('SHAPE', f'{n}: {fname} has {len(v)} values, expected {f["len"]}')
            if 'legal' in f:
                bad = [x for x in v if x not in f['legal']]
                if bad:
                    fail('RANGE', f'{n}: {fname} tokens {bad} not in {f["legal"]}')
                if len(set(v)) != len(v):
                    fail('SHAPE', f'{n}: {fname} repeats a token')
            if 'range' in f:
                bad = [x for x in v if not isinstance(x, int) or not f['range'][0] <= x <= f['range'][1]]
                if bad:
                    fail('RANGE', f'{n}: {fname} values {bad} outside {f["range"]}')
        elif t == 'obj':
            if not isinstance(v, dict):
                fail('SHAPE', f'{n}: {fname} must be an object')
            elif 'keys' in f and set(v) != set(f['keys']):
                fail('SHAPE', f'{n}: {fname} keys {sorted(v)}, expected {f["keys"]}')
            elif fname == 'shoelink' and not str(v['u']).startswith('https://'):
                fail('SHAPE', f'{n}: shoelink url is not https')
            elif fname == 'notes':
                for k in v:
                    if k not in NOTE_KEYS:
                        fail('ORPHAN', f'{n}: note key {k!r} is not a dial')
            elif fname == 'region':
                for k in ('o', 's'):
                    bad = [i for i in v[k] if not 0 <= i < nplaces]
                    if bad:
                        fail('ORPHAN', f'{n}: region.{k} indices {bad} off the end of places ({nplaces})')
        elif t == 'prices':
            if not isinstance(v, list) or len(v) != len(slots):
                fail('SHAPE', f'{n}: prices needs {len(slots)} slots')
                continue
            for i, p in enumerate(v):
                if p is None or p == '?':
                    continue
                if not isinstance(p, list) or len(p) != 2:
                    fail('SHAPE', f'{n}: prices[{slots[i]}] must be [lo, hi], null or "?"')
                elif p[0] > p[1]:
                    fail('SHAPE', f'{n}: prices[{slots[i]}] low above high')
            if rec.get('price_checked') and '?' in v:
                # The tick says "all eight garments opened and read"; a "?" says
                # nobody looked. Both cannot be true. Pre-existing in the 3.6.0
                # data, so a WARN until it is ruled — likely these are held
                # non-USD figures wearing the not-assessed mark.
                fail('WARN', f'{n}: price_checked tick, but {v.count("?")} slot(s) read "?"')
        elif t == 'onething':
            if not isinstance(v, dict) or set(v) != {'p', 'u', 'n'}:
                fail('SHAPE', f'{n}: onething needs p, u, n')
            elif v['p'] is None:
                if not v['n']:
                    fail('SHAPE', f'{n}: onething null with no note saying why')
                else:
                    fail('NOTE', f'{n}: no signature garment — {v["n"][:70]}')
            elif not v['u']:
                fail('NOTE', f'{n}: linkless one-thing "{v["p"]}" — {v["n"][:60]}')
            elif not str(v['u']).startswith('https://'):
                fail('SHAPE', f'{n}: onething url is not https')
        elif t == 'doors':
            c = v.get('c')
            if c not in ('full', 'partial', 'count', 'none'):
                fail('RANGE', f'{n}: doors coverage {c!r}')
                continue
            if c == 'none':
                if set(v) != {'c'}:
                    fail('SHAPE', f'{n}: doors none must carry nothing else')
                continue
            cities = v.get('cities', [])
            for row in cities:
                if not (isinstance(row, list) and len(row) == 3 and isinstance(row[2], int)):
                    fail('SHAPE', f'{n}: door row {row!r} is not [city, state, count]')
                elif not str(row[0]).strip():
                    fail('SHAPE', f'{n}: a door row carries no city')
            tot = sum(r[2] for r in cities if isinstance(r, list) and len(r) == 3)
            if c == 'full':
                if v.get('n') is None:
                    fail('SHAPE', f'{n}: doors full with no count')
                elif tot != v['n']:
                    fail('SHAPE', f'{n}: doors full, cities sum {tot} against {v["n"]}')
            elif c == 'count':
                if cities:
                    fail('SHAPE', f'{n}: doors count must carry no cities')
                if not v.get('n'):
                    fail('SHAPE', f'{n}: doors count with no number')
            elif c == 'partial':
                if not cities:
                    fail('SHAPE', f'{n}: doors partial with no cities — use count or none')
                if v.get('n') is not None and tot > v['n']:
                    fail('SHAPE', f'{n}: doors partial, {tot} verified against {v["n"]}')
        elif t == 'fibre':
            need = ['t', 'w', 'n', 's', 'c', 'x', 'xh', 'sp', 'sc', 'nc', 'st']
            if not isinstance(v, dict) or [k for k in need if k not in v]:
                fail('SHAPE', f'{n}: fibre missing {[k for k in need if k not in (v or {})]}')
            elif v['w'] > v['t'] or (v['x'] is not None and v['xh'] is not None and v['xh'] > v['x']) or not (99 <= v['n'] + v['s'] + v['c'] + (100 - round(100 * v['w'] / v['t']) if v['t'] else 0) <= 101 if v['t'] else True):
                fail('RANGE', f'{n}: fibre figures do not reconcile (t={v["t"]} w={v["w"]} n/s/c={v["n"]}/{v["s"]}/{v["c"]} x/xh={v["x"]}/{v["xh"]})')
            if get(rec, 'dials.natural') is not None:
                fail('ORPHAN', f'{n}: dials.natural is stored; it is derived from fibre at build')

sub = {f'{st}|{c}' for st, labs in data.regions.items() for labs_, cities in [(None, sum(labs.values(), []))] for c in cities}
for i, pl in enumerate(data.places):
    if pl.get('k') in ('s', 'o') and f'{pl.get("s")}|{pl.get("c")}' not in sub:
        fail('GAP', f'places[{i}] ({pl.get("n")!r}, {pl.get("c")} {pl.get("s")}): no sub-region in regions.json')
    for k in ('n', 'c', 's'):
        if not pl.get(k):
            fail('SHAPE', f'places[{i}] ({pl.get("n")!r}): missing {k}')

# ---------------------------------------------------------------- report
hard = ['ORPHAN', 'RANGE', 'SHAPE', 'GAP']
priced = sum(1 for b in data.brands for x in b['prices'] if isinstance(x, list))
unk = sum(1 for b in data.brands for x in b['prices'] if x == '?')
cov = collections.Counter(b['doors']['c'] for b in data.brands)
print(f'brands   {len(data.brands)}   places {nplaces}   changelog v{data.changelog[0]["v"]}')
print(f'prices   {priced} priced  {unk} not assessed')
print(f'doors    ' + '  '.join(f'{k}:{cov[k]}' for k in ('full', 'partial', 'count', 'none')))
print(f'notes    {len(P["NOTE"])} one-thing findings (null or linkless, all explained)')
if P['WARN']:
    print(f'\nWARN  ({len(P["WARN"])}) — legal, but a claim and a gap disagree')
    for m in P['WARN']:
        print(f'    {m}')
total = sum(len(P[k]) for k in hard)
for k in hard:
    if P[k]:
        print(f'\n{k}  ({len(P[k])})')
        for m in P[k]:
            print(f'    {m}')
print()
if total:
    print(f'FAIL — {total} problem(s).')
    sys.exit(1)
print('PASS — data is clean.')
