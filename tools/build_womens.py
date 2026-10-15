#!/usr/bin/env python3
"""Build the women's Spectrum — a locations-first map with price bands and no dials.

    python3 tools/womens_records.py      first: writes data/brands_womens/*.json (the men's record shape)
    python3 tools/build_womens.py        writes dist/womens_spectrum.html

One record shape, two folders: data/brands_womens/ (women's-only brands) and data/brands/ (the men's map, read for
the crossovers — men's-map brands in the women's universe). Stores: registers/own_doors_womens_2026-10-10.csv for
the women's records, data/places.json for the men's.
"""
import csv, json, os, re, glob, collections, unicodedata, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NE = ['MA', 'CT', 'ME', 'NH', 'NJ', 'NY', 'PA', 'RI', 'VT', 'DE']
BAND = {'basic': 'Basic', 'premium': 'Premium', 'accessible': 'Accessible', 'trueLux': 'True Luxury', 'pending': 'Pending'}
MENS_GARMENTS = ['T-shirt', 'Polo', 'Dress shirt', 'Jeans', 'Dress pants', 'Sweater', 'Outerwear', 'Shoes']
CH = {'O': 'its own stores', 'D': 'department stores', 'I': 'independent shops', 'W': 'its own site'}


def num(v):
    try:
        return int(float(v))
    except Exception:
        return None


def k(s):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())


def tier(n):
    if n is None: return 'NC'
    if n == 0: return 'none'
    if n <= 3: return 'flagship'
    if n <= 12: return 'circuit'
    if n <= 50: return 'network'
    if n <= 250: return 'chain'
    return 'mass'


def clean(x, extra=()):
    return '' if (x or '').lower() in ('nc', 'none', '', 'street', 'not stated', 'street / unknown') + tuple(extra) else x


def about_of(b):
    """The About block from a record in the men's shape (either folder)."""
    o = b.get('ownership') or {}; s = b.get('season') or {}; q = b.get('quote'); r = b.get('resale') or {}; c = b.get('certs') or {}; one = b.get('onething') or {}
    origin = b.get('origin', '')
    if origin.startswith('Founding date') or origin == 'Not yet read.':
        origin = ''
    quote = q['q'] if q else ''
    who = ', '.join(x for x in ((q or {}).get('who', ''), (q or {}).get('src', '')) if x)
    if not quote and b.get('opview'):
        m = re.match(r'^[“"](.+?)[”"]\s*[—–-]\s*(.*)$', b['opview'].strip(), re.S)
        if m: quote, who = m.group(1), m.group(2)
    a = {'sells': b.get('why', ''), 'chan': [CH[x] for x in b.get('chan', []) if x in CH], 'founded': origin,
         'owner': o.get('owner', ''), 'ownerurl': o.get('u', ''), 'sig': one.get('p', ''), 'sigurl': one.get('u', ''), 'pron': b.get('say', ''),
         'quote': quote, 'who': who, 'qurl': (q or {}).get('u', ''),
         'look': s.get('l', '') if s.get('u') else '', 'lookurl': s.get('u', ''),
         'vinted': (r.get('vinted') or {}).get('u', ''), 'trr': (r.get('therealreal') or {}).get('u', ''), 'grailed': (r.get('grailed') or {}).get('u', ''),
         'bcorp': (c.get('bcorp') or {}).get('e', ''), 'gots': (c.get('gots') or {}).get('e', ''),
         'status': (b.get('facts_read') or {}).get('status', 'read')}
    return a if any(a[x] for x in ('sells', 'founded', 'owner', 'sig', 'quote')) else None


def natural_of(b):
    """Natural-fibre band, the men's cuts (99.95 / 95 / 85 / 70) on the share of styles led by a natural fibre; None where unread or held."""
    f = b.get('fibre')
    if not f or not f.get('t') or not b.get('fabric'):
        return None
    if 'n_pct' in f:
        if not f.get('w') or f['w'] < 20: return None
        share = f['n_pct']
    else:
        disc = f.get('n', 0) + f.get('s', 0) + f.get('c', 0)
        if not disc or f.get('w') is None or f['w'] / f['t'] < 0.5: return None
        share = 100 * f['n'] / disc
    return 5 if share >= 99.95 else 4 if share >= 95 else 3 if share >= 85 else 2 if share >= 70 else 1


def fibre_line(b):
    f = b.get('fibre')
    if not f or not f.get('t'):
        return ''
    if 'n_pct' in f:  # women's record: percentages of a sample
        cel = f"{f['c_pct']}% cellulosic" + (f" (lyocell {f['ly_pct']}%, viscose and other {f['cv_pct']}%)" if f.get('ly_pct') is not None and f['c_pct'] else '')
        return f"{f['t']} styles on the site; of {f['w']} read with a composition, {f['n_pct']}% natural-led, {f['s_pct']}% synthetic, {cel}; {f['spandex']} with elastane; {'one cloth story' if f['sp']=='one' else 'two cloth stories' if f['sp']=='split' else f['sp']}."
    disc = f.get('n', 0) + f.get('s', 0) + f.get('c', 0)
    if not disc:
        return ''
    return f"{f['t']} men's styles counted; of {f['w']} stating a composition, {round(100*f['n']/disc)}% natural-led, {round(100*f['s']/disc)}% synthetic, {round(100*f.get('c',0)/disc)}% cellulosic."


def prices_of(b):
    pr = b.get('prices')
    if not pr: return None
    out = {}
    for g, p in zip(b.get('garments') or MENS_GARMENTS, pr):
        out[g.lower()] = p if isinstance(p, list) else ('NONE' if p is None else p)
    return out


def main():
    womens = [json.load(open(f, encoding='utf8')) for f in sorted(glob.glob(os.path.join(ROOT, 'data/brands_womens/*.json')))]
    men = {k(b['name']): b for b in (json.load(open(f, encoding='utf8')) for f in glob.glob(os.path.join(ROOT, 'data/brands/*.json')))}
    universe = {k(r['brand']) for r in csv.DictReader(open(os.path.join(ROOT, 'registers/womens_universe_counted_2026-10-10.csv'), encoding='utf8'))}
    doors = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(ROOT, 'registers/own_doors_womens_2026-10-10.csv'), encoding='utf8')):
        if r['format'] == 'own-door' and r['status'] == 'open':
            doors[r['brand']].append({'sn': r['store_name'], 'a': r['street'], 'c': r['city'], 's': r['state'], 'z': clean(r['zip']), 'v': clean(r['venue']), 'op': clean(r['operator'])})
    places = json.load(open(os.path.join(ROOT, 'data/places.json')))
    mstores = collections.defaultdict(list)
    for p in places:
        if p['k'] == 'o':
            mstores[p['n']].append({'sn': p.get('bn', '') or '', 'a': p.get('a', ''), 'c': p['c'], 's': p['s'], 'z': p.get('z', ''), 'v': p.get('v2', ''), 'op': p.get('op', '')})

    brands = []
    for b in womens:
        d = b['doors']; stores = doors.get(b['name'], [])
        brands.append({'n': b['name'], 'band': BAND[b['band']], 'basis': b.get('band_note', ''), 'own': d['n'], 'out': d.get('out', 0), 'con': d.get('con', 0),
                       'tier': tier(d['n']), 'stores': stores, 'ne': sum(1 for s in stores if s['s'] in NE), 'locator': d.get('locator', ''),
                       'read': (d.get('basis') or '').replace('doors_womens ', ''), 'note': d.get('note', ''), 'src': b.get('src', 'womens'),
                       'prices': prices_of(b), 'lh': bool(b.get('leather_high_held')), 'depts': b.get('depts', 0), 'about': about_of(b), 'm': b.get('band_mean'),
                       'f': b.get('focus') or None, 'fa': b.get('fabric') or None, 'gl': {k.lower(): u for k, u in (b.get('garment_links') or {}).items()} or None,
                       'fi': fibre_line(b), 'nt': b.get('notes') or {}, 'nat': natural_of(b)})
    for kk, b in men.items():
        if kk not in universe: continue
        d = b.get('doors', {}); n = d.get('n') if d.get('c') in ('full', 'count', 'partial') else None
        if not n: continue
        stores = mstores.get(b['name'], [])
        pr = b.get('prices') or []
        st = [x[0] for x in (pr[2] if len(pr) > 2 else None, pr[5] if len(pr) > 5 else None) if isinstance(x, list) and len(x) < 3]
        m = round(sum(st) / len(st)) if st and b['band'] in ('premium', 'accessible', 'trueLux') else None
        basis = (f"men’s dress-shirt and sweater entry, mean ${m}, at the women’s cuts" if m is not None else 'banded on its men’s range (the men’s map)' + ((': ' + b['band_note']) if b.get('band_note') else ''))
        brands.append({'n': b['name'], 'band': BAND[b['band']], 'm': m, 'basis': basis, 'own': n,
                       'out': d.get('out', 0) or 0, 'con': d.get('con', 0) or 0, 'tier': tier(n), 'stores': stores, 'ne': sum(1 for s in stores if s['s'] in NE),
                       'locator': '', 'read': (d.get('basis') or '').split(';')[0].strip(), 'note': 'Also on the men’s map; its stores sell both. Prices and facts are the men’s record.',
                       'src': 'men', 'prices': prices_of(b), 'lh': False, 'depts': 0, 'about': about_of(b),
                       'f': b.get('focus') or None, 'fa': b.get('fabric') or None, 'gl': {k.lower(): u for k, u in (b.get('garment_links') or {}).items()} or None,
                       'fi': fibre_line(b), 'nt': {k: b['notes'][k] for k in ('tech', 'craft', 'comfort', 'style') if k in (b.get('notes') or {})}, 'nat': natural_of(b)})
    brands.sort(key=lambda b: unicodedata.normalize('NFKD', b['n']).encode('ascii', 'ignore').decode().lower().lstrip('.'))  # alphabetical within each band
    nb = collections.Counter(b['band'] for b in brands)
    data = {'built': datetime.date.today().isoformat(), 'brands': brands, 'ne': NE}
    tpl = open(os.path.join(ROOT, 'app/womens_template.html'), encoding='utf8').read()
    html = tpl.replace('/*__DATA__*/', 'const W = ' + json.dumps(data, ensure_ascii=False) + ';')
    os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
    out = os.path.join(ROOT, 'dist/womens_spectrum.html')
    open(out, 'w', encoding='utf8').write(html)
    print(f'{len(brands)} brands ({sum(1 for b in brands if b["src"]=="men")} crossovers), {sum(len(b["stores"]) for b in brands)} stores, bands {dict(nb)} -> {out} {os.path.getsize(out):,} bytes')


if __name__ == '__main__':
    main()
