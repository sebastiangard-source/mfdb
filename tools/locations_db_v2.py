#!/usr/bin/env python3
"""Practice build of the v2 locations database: every brand-owned store and every non-department-store
stockist on file for the men's brands banded Premium, Accessible or True Luxury (Basic excluded).

    python3 tools/locations_db_v2.py

Writes registers/locations_db_v2_practice.csv (one row per brand × door) and
registers/stockist_shops_v2_practice.csv (one row per shop, with the brands it carries).

Sources:
  own doors   data/places.json (k = o) — the map's rows, cleaned and ruled
  stockists   registers/stockists_wave_{a,b,c}_*.csv, shop_kind independent or golf club / pro shop,
              US or PR, with a street; and data/places.json (k = s) through brand.region.s — the
              Northeast shop register
Department stores, online-only listings, other brands' own doors and NC rows are excluded.
"""
import csv, json, os, re, glob, hashlib, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANDS = {'premium': 'Premium', 'accessible': 'Accessible', 'trueLux': 'True Luxury'}
KEEP_KIND = {'independent', 'golf club or pro shop'}
# Ruled 12 Oct: running-shoe houses' stockist lists are run-specialty shops, not the menswear circuit; their
# stockists are left out of v2 (their own stores stay). Hoka and On alone were 1,849 of 3,278 shops.
NO_STOCKISTS = {'Hoka', 'On'}
COLS = ['row_id', 'brand', 'band', 'kind', 'shop_name', 'shop_kind', 'street', 'city', 'state', 'zip', 'venue',
        'operator', 'neighbourhood', 'source']


def nstreet(s):
    s = re.sub(r'[^a-z0-9 ]', ' ', (s or '').lower())
    s = re.sub(r'\b(suite|ste|unit|space|floor|fl|#)\b.*$', '', s)
    return re.sub(r'\s+', ' ', s).strip()


def ok(v):
    v = (v or '').strip()
    return v and v not in ('NC', 'NONE', '-') and not v.startswith('NC')


def main():
    brands = {}
    for f in glob.glob(os.path.join(ROOT, 'data/brands/*.json')):
        b = json.load(open(f))
        if b['band'] in BANDS:
            brands[b['name']] = b
    places = json.load(open(os.path.join(ROOT, 'data/places.json')))
    rows, seen = [], set()

    def add(r):
        k = (r['brand'], r['kind'], nstreet(r['street']), (r['zip'] or '')[:5] or r['city'].lower())
        if k in seen:
            return
        seen.add(k)
        r['row_id'] = hashlib.sha1('|'.join(k).encode()).hexdigest()[:12]
        rows.append({c: r.get(c, '') for c in COLS})

    # own doors
    for p in places:
        if p.get('k') == 'o' and p['n'] in brands and ok(p.get('c')):
            add({'brand': p['n'], 'band': BANDS[brands[p['n']]['band']], 'kind': 'own', 'shop_name': p.get('bn', '') or p['n'],
                 'shop_kind': 'brand store', 'street': p.get('a', ''), 'city': p['c'], 'state': p['s'], 'zip': (p.get('z') or '')[:5],
                 'venue': p.get('v2', ''), 'operator': p.get('op', ''), 'neighbourhood': p.get('h', ''), 'source': p.get('src', 'places')})
    # Northeast shop register
    for name, b in brands.items():
        if name in NO_STOCKISTS:
            continue
        for i in (b.get('region') or {}).get('s', []):
            p = places[i]
            add({'brand': name, 'band': BANDS[b['band']], 'kind': 'stockist', 'shop_name': p['n'], 'shop_kind': p.get('t', 'independent'),
                 'street': p.get('a', ''), 'city': p['c'], 'state': p['s'], 'zip': (p.get('z') or '')[:5], 'venue': '', 'operator': '',
                 'neighbourhood': p.get('h', ''), 'source': 'ne_shop_register'})
    # wave stockist registers
    for f in sorted(glob.glob(os.path.join(ROOT, 'registers/stockists_wave_*.csv'))):
        for d in csv.DictReader(open(f, encoding='utf8')):
            if d['brand'] not in brands or d['brand'] in NO_STOCKISTS or d.get('shop_kind') not in KEEP_KIND:
                continue
            if d.get('country') not in ('US', 'PR') or not ok(d.get('street')) or not ok(d.get('city')):
                continue
            add({'brand': d['brand'], 'band': BANDS[brands[d['brand']]['band']], 'kind': 'stockist', 'shop_name': d['shop_name'],
                 'shop_kind': d['shop_kind'], 'street': d['street'], 'city': d['city'], 'state': d['state'], 'zip': (d.get('zip') or '')[:5],
                 'venue': '', 'operator': '', 'neighbourhood': '', 'source': os.path.basename(f)})

    rows.sort(key=lambda r: (r['brand'].lower(), r['kind'], r['state'], r['city'], r['street']))
    out = os.path.join(ROOT, 'registers/locations_db_v2_practice.csv')
    with open(out, 'w', newline='', encoding='utf8') as fh:
        w = csv.DictWriter(fh, fieldnames=COLS); w.writeheader(); w.writerows(rows)

    # shops table: one row per stockist shop, brands it carries
    shops = collections.OrderedDict()
    for r in rows:
        if r['kind'] != 'stockist':
            continue
        k = (nstreet(r['street']), r['zip'] or r['city'].lower())
        s = shops.setdefault(k, {'shop_name': r['shop_name'], 'shop_kind': r['shop_kind'], 'street': r['street'], 'city': r['city'],
                                 'state': r['state'], 'zip': r['zip'], 'brands': []})
        s['brands'].append(r['brand'])
    out2 = os.path.join(ROOT, 'registers/stockist_shops_v2_practice.csv')
    with open(out2, 'w', newline='', encoding='utf8') as fh:
        w = csv.writer(fh); w.writerow(['shop_name', 'shop_kind', 'street', 'city', 'state', 'zip', 'brands_on_file', 'brands'])
        for s in sorted(shops.values(), key=lambda s: (-len(s['brands']), s['state'], s['city'])):
            w.writerow([s['shop_name'], s['shop_kind'], s['street'], s['city'], s['state'], s['zip'], len(set(s['brands'])), '; '.join(sorted(set(s['brands'])))])

    by = collections.Counter((r['band'], r['kind']) for r in rows)
    print(f'{len(rows)} rows -> {out}; {len(shops)} distinct stockist shops -> {out2}')
    for k in sorted(by):
        print(f'  {k[0]:12} {k[1]:9} {by[k]}')
    cov = collections.Counter(r['brand'] for r in rows if r['kind'] == 'stockist')
    print('brands with any stockist row:', len(cov), 'of', len(brands))


if __name__ == '__main__':
    main()
