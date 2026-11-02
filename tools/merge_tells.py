#!/usr/bin/env python3
"""Merge the tells_2026-11-01 returns into registers/tells.csv and onto both maps.

Every return.csv under jobs/returns/tells_2026-11-01 is read in path order, so a later run overrides an
earlier one for the same brand. Sebastian's rulings in OVERRIDE win over any return. Men's records get a
`tell` field (yes rows at high or medium confidence only); the Explorer reads registers/tells.csv at build.
"""
import csv, glob, json, os, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from spec import slug  # noqa: E402

COLS = ['brand', 'has_tell', 'tell', 'description', 'kind', 'placement', 'visibility', 'since', 'source_url', 'example_product_url', 'confidence', 'read_date', 'origin', 'note']
OVERRIDE = {  # rulings on single rows where a return held back
    # Construction details count (the brief lists `construction` as a kind); the brand's own page names the facing
    # as its signature, 1 Nov 2026.
    'Edward Green': dict(has_tell='yes', confidence='medium', description="A swan's-neck shaped eyelet facing on its lace-ups, which the brand calls a signature detail."),
}


def nc(v):
    return (v or '').strip() in ('', 'NC', 'ND', 'NONE', 'none')


def main():
    rows = collections.OrderedDict()
    files = sorted(glob.glob(os.path.join(ROOT, 'jobs/returns/tells_2026-11-01/**/return.csv'), recursive=True))
    master = os.path.join(ROOT, 'jobs/returns/tells_2026-11-01/master_return.csv')
    if os.path.exists(master):
        files.append(master)  # the thread's one-row-per-brand roll-up wins over the per-run files
    for f in files:
        run = 'master' if f.endswith('master_return.csv') else os.path.basename(os.path.dirname(f))
        for r in csv.DictReader(open(f, encoding='utf8')):
            if r['has_tell'] == 'NC':
                continue
            r['origin'] = run
            rows[r['brand']] = {k: r.get(k, '') for k in COLS}
    for b, o in OVERRIDE.items():
        rows[b] = {**{k: '' for k in COLS}, **rows.get(b, {}), 'brand': b, **o}
    with open(os.path.join(ROOT, 'registers/tells.csv'), 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(sorted(rows.values(), key=lambda r: r['brand'].lower()))
    shown = {b: r for b, r in rows.items() if r['has_tell'] == 'yes' and r['confidence'] in ('high', 'medium')}
    n = 0
    for fn in glob.glob(os.path.join(ROOT, 'data/brands/*.json')):
        d = json.load(open(fn, encoding='utf8'), object_pairs_hook=collections.OrderedDict)
        r = shown.get(d['name'])
        if r:
            t = collections.OrderedDict(t=r['tell'], d=r['description'], k=r['kind'], v=r['visibility'])
            if not nc(r['since']): t['y'] = r['since']
            if not nc(r['example_product_url']): t['u'] = r['example_product_url']
            if not nc(r['source_url']): t['s'] = r['source_url']
            t['c'] = r['confidence']
            if d.get('tell') != t: d['tell'] = t; open(fn, 'w', encoding='utf8').write(json.dumps(d, ensure_ascii=False, indent=1))
            n += 1
        elif 'tell' in d:
            d.pop('tell'); open(fn, 'w', encoding='utf8').write(json.dumps(d, ensure_ascii=False, indent=1))
    c = collections.Counter(r['has_tell'] for r in rows.values())
    print(f'{len(rows)} brands read: {dict(c)}; {len(shown)} shown; {n} on the men\'s map')


if __name__ == '__main__':
    main()
