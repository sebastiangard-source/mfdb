#!/usr/bin/env python3
"""
menswear_spectrum validator.

Supersedes audit.py, which answered one question: is a required field present.
This checks five classes of failure, all of which a bulk merge can introduce
silently:

  ORPHAN    a key that is not a brand in BANDS (typo, or a rendering variance
            like "J. McLaughlin" for "J.McLaughlin")
  DUPE      a repeated key in a dict literal. JS and json.loads both keep the
            last one with no error, so the earlier value vanishes
  RANGE     a value outside its dial's legal set
  SHAPE     wrong arity, wrong subkeys, malformed pair
  GAP       a required field missing for a brand

Usage:  python3 validate.py [path]        default ./menswear_spectrum.html
Exit 1 if anything fails.
"""
import sys, re, json, collections

PATH = sys.argv[1] if len(sys.argv) > 1 else 'menswear_spectrum.html'
S = open(PATH, encoding='utf8').read()

problems = collections.defaultdict(list)


def fail(kind, msg):
    problems[kind].append(msg)


# ---------------------------------------------------------------- extraction

def dupe_hook(pairs):
    """json object hook that surfaces duplicate keys instead of eating them."""
    seen, out = set(), {}
    for k, v in pairs:
        if k in seen:
            dupe_hook.hits.append(k)
        seen.add(k)
        out[k] = v
    return out


def grab(const):
    """Extract a const's object literal by brace matching, then JSON-parse it."""
    i = S.find('const %s ' % const)
    if i < 0:
        i = S.find('const %s=' % const)
    if i < 0:
        return None
    seg = S[i:i + 400000]
    st = seg.find('{')
    d = 0
    for j, c in enumerate(seg[st:], st):
        if c == '{':
            d += 1
        elif c == '}':
            d -= 1
            if d == 0:
                raw = seg[st:j + 1]
                dupe_hook.hits = []
                try:
                    obj = json.loads(raw, object_pairs_hook=dupe_hook)
                except json.JSONDecodeError as e:
                    fail('SHAPE', f'{const}: will not parse — {e}')
                    return None
                for k in dupe_hook.hits:
                    fail('DUPE', f'{const}: key "{k}" appears more than once; '
                                 f'only the last value survives')
                return obj
    return None


# ---------------------------------------------------------------- BANDS

rows = re.findall(r'\["([^"]+)",([01]),\[([\d,\s]+)\]', S)
BRANDS = [r[0] for r in rows]
BRANDSET = set(BRANDS)

for b, c in collections.Counter(BRANDS).items():
    if c > 1:
        fail('DUPE', f'BANDS: brand row "{b}" appears {c} times')

for name, _flag, attrs in rows:
    vals = [int(x) for x in attrs.split(',')]
    if len(vals) != 4:
        fail('SHAPE', f'BANDS "{name}": {len(vals)} focus attrs, expected 4 '
                      f'(tech, comfort, craft, style)')
    for v in vals:
        if not 1 <= v <= 5:
            fail('RANGE', f'BANDS "{name}": focus attr {v} outside 1–5')

# ---------------------------------------------------------------- rules

REGISTERS = ['GOLF', 'STATUS', 'FINBRO', 'IVY', 'MURICA', 'ITAL', 'FREN',
             'STREET', 'AVANT', 'PREP', 'WEIRD', 'BOAT', 'RACQUET', 'SKI', 'SCANDI', 'BRIISH']

NOTE_KEYS = {'tech', 'comfort', 'craft', 'style', 'denim', 'cashmere', 'linen',
             'cotton', 'wool', 'synth', 'golf', 'status', 'finbro', 'ivy',
             'murica', 'ital', 'fren', 'street', 'avant', 'prep', 'weird',
             'boat', 'racquet', 'ski', 'scandi', 'briish', 'fuss', 'dur', 'forg', 'reach', 'shoes',
             'golffice'}

CHAN_TOKENS = {'O', 'D', 'I', 'W', 'X'}
CONF_VALUES = {'L', 'S', 'M', 'H', 'G'}

# Required for every brand. A merge that lands partial coverage shows up here.
REQUIRED = ['FAB', 'WHY', 'ORIGIN', 'CITIES', 'REACH', 'CHAN', 'DUR', 'FORG',
            'PRICES', 'ONETHING']

ALL_CONSTS = (REQUIRED + REGISTERS +
              ['OPVIEW', 'SHOP', 'NOTES', 'SHOELINK', 'CONF', 'FORGC',
               'SHOES', 'GOLFFICE', 'FUSS', 'BRUV', 'SAIL'])

D = {}
for c in dict.fromkeys(ALL_CONSTS):
    o = grab(c)
    if o is None:
        fail('SHAPE', f'{c}: const not found')
        o = {}
    D[c] = o
    for k in o:
        if k not in BRANDSET:
            fail('ORPHAN', f'{c}: "{k}" is not a brand in BANDS')


def scalars(const, lo, hi, banned=()):
    for b, v in D[const].items():
        if not isinstance(v, int):
            fail('SHAPE', f'{const} "{b}": {v!r} is not an integer')
        elif not lo <= v <= hi:
            fail('RANGE', f'{const} "{b}": {v} outside {lo}–{hi}')
        elif v in banned:
            fail('RANGE', f'{const} "{b}": {v} is a retired band')


for c in REGISTERS:
    # 0 means not represented, not unassessed. See the 1,491-cell migration.
    scalars(c, 0, 5)

scalars('REACH', 1, 5)
scalars('DUR', 1, 5)
scalars('FORG', 1, 5)
scalars('FUSS', -3, 3)       # bipolar, centre = off
scalars('GOLFFICE', -3, 3)   # bipolar
scalars('BRUV', -3, 3)       # bipolar: bruv at the negative pole, bruh at the positive
scalars('SAIL', -3, 3)       # bipolar: under sail at the negative pole, under power at the positive
# Shoes is tri-state: a score, a verified 0, or absent = not assessed.
# 1 and 2 were the assumed bands and were removed; their return means a
# merge reintroduced guesses.
scalars('SHOES', 0, 5, banned=(1, 2))

for b, v in D['FAB'].items():
    if not isinstance(v, list) or len(v) != 6:
        fail('SHAPE', f'FAB "{b}": expected 6 values '
                      f'(denim, cashmere, linen, cotton, wool, synth)')
    else:
        for x in v:
            if not isinstance(x, int) or not 1 <= x <= 5:
                fail('RANGE', f'FAB "{b}": {x!r} outside 1–5')

for b, v in D['FORGC'].items():
    if not isinstance(v, list) or len(v) != 3:
        fail('SHAPE', f'FORGC "{b}": expected 3 components')
    else:
        for x in v:
            if not isinstance(x, int) or not 1 <= x <= 5:
                fail('RANGE', f'FORGC "{b}": {x!r} outside 1–5')

for b, v in D['CHAN'].items():
    if not isinstance(v, list) or not v:
        fail('SHAPE', f'CHAN "{b}": expected a non-empty list')
    else:
        for t in v:
            if t not in CHAN_TOKENS:
                fail('RANGE', f'CHAN "{b}": token {t!r} not in '
                              f'{sorted(CHAN_TOKENS)}')
        if len(set(v)) != len(v):
            fail('SHAPE', f'CHAN "{b}": repeated channel token')

for b, v in D['CONF'].items():
    if v not in CONF_VALUES:
        fail('RANGE', f'CONF "{b}": {v!r} not in {sorted(CONF_VALUES)}')

for b, v in D['PRICES'].items():
    if not isinstance(v, list) or len(v) != 8:
        fail('SHAPE', f'PRICES "{b}": expected 5 garment slots '
                      f'(T-shirt, Polo, Dress shirt, Jeans, Dress pants)')
        continue
    for i, p in enumerate(v):
        if p is None:
            continue  # null = verified: brand does not make the garment
        if p in ('?', 'np'):
            continue  # "?" = not assessed; "np" = checked, none published. Both distinct from null
        if not isinstance(p, list) or len(p) not in (2, 3):
            fail('SHAPE', f'PRICES "{b}" slot {i}: expected [low, high], [low, high, CUR], null, "?" or "np"')
        elif p[0] > p[1]:
            fail('SHAPE', f'PRICES "{b}" slot {i}: low {p[0]} above high {p[1]}')

for b, v in D['ONETHING'].items():
    if set(v) != {'p', 'u', 'n'}:
        fail('SHAPE', f'ONETHING "{b}": subkeys {sorted(v)}, expected p, u, n')
    elif v['p'] is None:
        # Checked and found to have no signature garment. A finding, not a hole —
        # but only if the reasoning is written down, otherwise it is a hole.
        if not v['n']:
            fail('SHAPE', f'ONETHING "{b}": null product with no note explaining why')
        else:
            fail('NOENTRY', f'{b}: {v["n"][:80]}')
    elif not v['u']:
        # An empty url is legitimate: a red-pen call exists but no stable link
        # could be verified. The note must say so, or it is an oversight.
        fail('LINKLESS', f'{b}: "{v["p"]}" — {v["n"][:70]}')
    elif not str(v['u']).startswith('https://'):
        fail('SHAPE', f'ONETHING "{b}": url is not https')

for b, v in D['SHOELINK'].items():
    if set(v) != {'t', 'u'}:
        fail('SHAPE', f'SHOELINK "{b}": subkeys {sorted(v)}, expected t, u')
    elif not str(v['u']).startswith('https://'):
        fail('SHAPE', f'SHOELINK "{b}": url is not https')

for b, v in D['SHOP'].items():
    if not str(v).startswith('https://'):
        fail('SHAPE', f'SHOP "{b}": url is not https')

DOORS = grab('DOORS')
if DOORS is None:
    fail('SHAPE', 'DOORS: const not found')
    DOORS = {}
for k in DOORS:
    if k not in BRANDSET:
        fail('ORPHAN', f'DOORS: "{k}" is not a brand in BANDS')
for b, v in DOORS.items():
    c = v.get('c')
    if c not in ('full', 'partial', 'count', 'none'):
        fail('RANGE', f'DOORS "{b}": coverage {c!r} not full/partial/count/none')
        continue
    if c == 'none':
        if set(v) != {'c'}:
            fail('SHAPE', f'DOORS "{b}": coverage none must carry nothing else')
        continue
    cities = v.get('cities', [])
    for row in cities:
        if not (isinstance(row, list) and len(row) == 3 and isinstance(row[2], int)):
            fail('SHAPE', f'DOORS "{b}": city row {row!r} is not [city, state, count]')
        elif not str(row[0]).strip():
            # A door with no city cannot be filtered on, which is the whole
            # reason the city list exists.
            fail('SHAPE', f'DOORS "{b}": a door row carries no city')
    tot = sum(r[2] for r in cities if isinstance(r, list) and len(r) == 3)
    if c == 'full':
        # The whole point of "full" is that it can be filtered on. If the city
        # counts do not account for every door, it cannot.
        if v.get('n') is None:
            fail('SHAPE', f'DOORS "{b}": coverage full with no door count')
        elif tot != v['n']:
            fail('SHAPE', f'DOORS "{b}": full, but cities sum to {tot} against {v["n"]} doors')
    elif c == 'count':
        if cities:
            fail('SHAPE', f'DOORS "{b}": coverage count must carry no cities')
        if not v.get('n'):
            fail('SHAPE', f'DOORS "{b}": coverage count with no number')
    elif c == 'partial':
        if not cities:
            fail('SHAPE', f'DOORS "{b}": partial with no verified cities \u2014 use count or none')
        if v.get('n') is not None and tot > v['n']:
            fail('SHAPE', f'DOORS "{b}": partial, {tot} verified against a total of {v["n"]}')

for b, v in D['NOTES'].items():
    for k in v:
        if k not in NOTE_KEYS:
            fail('ORPHAN', f'NOTES "{b}": note key {k!r} is not a dial')

# ---------------------------------------------------------------- gaps

gaps = []
for b in BRANDS:
    missing = [f for f in REQUIRED if b not in D[f]]
    if missing:
        gaps.append((b, missing))
        fail('GAP', f'{b}: {", ".join(missing)}')

# ---------------------------------------------------------------- report

print(f'file      {PATH}')
print(f'brands    {len(BRANDS)} rows, {len(BRANDSET)} unique')
print(f'coverage  ' + '  '.join(
    f'{c}:{len(D[c])}' for c in REQUIRED))
unk = sum(1 for v in D['PRICES'].values() for x in v if x == '?')
absent = sum(1 for v in D['PRICES'].values() for x in v if x is None)
print(f'prices    {1584-unk-absent} priced  {absent} not a staple  {unk} not assessed')
import collections as _c
_cov = _c.Counter(v.get('c') for v in DOORS.values())
_doors = sum(r[2] for v in DOORS.values() for r in v.get('cities', []))
print(f'doors     full:{_cov["full"]}  partial:{_cov["partial"]}  count:{_cov["count"]}  '
      f'none:{_cov["none"]}  ({_doors} addressed doors)')
print(f'partial   ' + '  '.join(
    f'{c}:{len(D[c])}' for c in ['SHOES', 'GOLFFICE', 'FUSS', 'CONF', 'SHOP',
                                 'NOTES', 'SHOELINK']))
print()

order = ['ORPHAN', 'DUPE', 'RANGE', 'SHAPE', 'GAP']
total = sum(len(problems[k]) for k in order)

if problems['NOENTRY']:
    print(f'NOTE  brands checked and found to have no signature garment '
          f'({len(problems["NOENTRY"])})')
    for m in problems['NOENTRY']:
        print(f'    {m}')
    print()

if problems['LINKLESS']:
    print(f'WARN  one-thing entries with no link ({len(problems["LINKLESS"])}) '
          f'— legitimate if the note explains why')
    for m in problems['LINKLESS']:
        print(f'    {m}')
    print()

if not total:
    print('PASS — no orphans, duplicates, range violations, shape errors or gaps.')
    sys.exit(0)

for k in order:
    if problems[k]:
        print(f'{k}  ({len(problems[k])})')
        for m in problems[k]:
            print(f'    {m}')
        print()
print(f'FAIL — {total} problem(s).')
sys.exit(1)
