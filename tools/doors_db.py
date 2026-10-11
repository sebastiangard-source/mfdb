#!/usr/bin/env python3
"""Build registers/locations_db_v1.csv: every full-price, brand-owned US store on file,
men's and women's, one row per door, with empty lat/lon columns for the geocoding job.

v1 scope (ruled 11 Oct 2026): format own-door, status open, US and Puerto Rico. No outlets,
factory or clearance stores, concessions, department-store counters, pop-ups or stockists.
Operator-run doors under the brand's banner stay (ruled 8 Oct), with the operator carried.

Sources, in order; a later source never overwrites an earlier row for the same door:
  1. data/places.json own doors (k = o) — the map's rows, already cleaned and ruled
  2. registers/own_doors_womens_2026-10-10.csv — the 36 women's chains
  3. registers/own_doors_wave_b_2026-10-08.csv — wave B rows for brands not yet seated
  4. any extra own_doors CSVs passed on the command line (wave C batches, Rue La La)
Doors de-duplicate on brand + normalized street + ZIP5.
"""
import csv, json, os, re, sys, hashlib, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'registers', 'locations_db_v1.csv')
COLS = ['door_id', 'brand', 'map', 'store_name', 'banner', 'street', 'city', 'state', 'zip', 'country',
        'phone', 'venue', 'operator', 'neighbourhood', 'source', 'captured_on', 'lat', 'lon', 'geo_source', 'geo_match']
OPEN = {'open', 'as listed', '', 'ok'}
US = {'US', 'USA', 'United States', 'PR', ''}


def nstreet(s):
    s = re.sub(r'[^a-z0-9 ]', ' ', (s or '').lower())
    s = re.sub(r'\b(suite|ste|unit|space|floor|fl|#)\b.*$', '', s)
    return re.sub(r'\s+', ' ', s).strip()


def key(brand, street, zip5):
    return hashlib.sha1(f'{brand}|{nstreet(street)}|{zip5}'.encode()).hexdigest()[:12]


def clean(v):
    v = (v or '').strip()
    return '' if v in ('NC', 'NONE', '-', 'not stated', 'not stated by locator') else v


def main(extra):
    rows, seen = [], {}

    def add(r):
        if not r['street'] or not r['city'] or not r['state']:
            return
        k = key(r['brand'], r['street'], r['zip'])
        if k in seen:
            return
        seen[k] = True
        r['door_id'] = k
        rows.append({c: r.get(c, '') for c in COLS})

    # 1. the map's own doors
    places = json.load(open(os.path.join(ROOT, 'data/places.json')))
    for x in places:
        if x.get('k') != 'o':
            continue
        add({'brand': x['n'], 'map': 'men', 'store_name': '', 'banner': x.get('bn', ''), 'street': x.get('a', ''),
             'city': x.get('c', ''), 'state': x.get('s', ''), 'zip': (x.get('z') or '')[:5], 'country': 'US',
             'phone': '', 'venue': x.get('v2', ''), 'operator': x.get('op', ''), 'neighbourhood': x.get('h', ''),
             'source': x.get('src', 'places'), 'captured_on': ''})

    # 2–4. register CSVs
    files = [('women', os.path.join(ROOT, 'registers/own_doors_womens_2026-10-10.csv')),
             ('men', os.path.join(ROOT, 'registers/own_doors_wave_b_2026-10-08.csv'))] + [('men', f) for f in extra]
    for which, f in files:
        for d in csv.DictReader(open(f, encoding='utf8')):
            if d.get('format') != 'own-door' or (d.get('status') or '').lower() not in OPEN:
                continue
            if clean(d.get('country', 'US')) not in US:
                continue
            add({'brand': d['brand'], 'map': which, 'store_name': clean(d.get('store_name')), 'banner': clean(d.get('banner_stated')),
                 'street': clean(d.get('street')), 'city': clean(d.get('city')), 'state': clean(d.get('state')),
                 'zip': clean(d.get('zip'))[:5], 'country': 'US', 'phone': clean(d.get('phone')), 'venue': clean(d.get('venue')),
                 'operator': clean(d.get('operator')), 'neighbourhood': '', 'source': os.path.basename(f),
                 'captured_on': clean(d.get('captured_on'))})

    rows.sort(key=lambda r: (r['brand'].lower(), r['state'], r['city'], r['street']))
    with open(OUT, 'w', newline='', encoding='utf8') as fh:
        w = csv.DictWriter(fh, fieldnames=COLS); w.writeheader(); w.writerows(rows)
    by = collections.Counter(r['map'] for r in rows)
    print(f'{len(rows)} doors -> {OUT}  men {by["men"]}  women {by["women"]}  brands {len({r["brand"] for r in rows})}')
    print('no ZIP:', sum(1 for r in rows if not r['zip']), ' no phone:', sum(1 for r in rows if not r['phone']))


if __name__ == '__main__':
    main(sys.argv[1:])
