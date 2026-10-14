#!/usr/bin/env python3
"""Build the women's Spectrum v0 — a locations-first map with price bands and no dials.

    python3 tools/build_womens.py        writes dist/womens_spectrum.html

Brands: every women's-universe brand with at least one counted full-price US store that is not on the
men's map, plus the men's-map crossovers (banded on their men's range, flagged). Bands from the women's
price pass as it lands (jobs/returns/prices_womens_2026-10-13/batch*/return.csv), else "pending".
Doors from registers/own_doors_womens_2026-10-10.csv (own-door, open) and, for crossovers, data/places.json.
"""
import csv, json, os, re, glob, collections, unicodedata, datetime


def num(v):
    try:
        return int(float(v))
    except Exception:
        return None


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NE = ['MA', 'CT', 'ME', 'NH', 'NJ', 'NY', 'PA', 'RI', 'VT', 'DE']
BAND = {'basic': 'Basic', 'premium': 'Premium', 'accessible': 'Accessible', 'trueLux': 'True Luxury'}
def cut(m):
    return 'Premium' if m < 150 else ('Accessible' if m <= 400 else 'True Luxury')


def band_of(p):
    """The men's price rule on the women's staples; a provisional read where the staples are missing."""
    tee, bl, sw = num(p['tee_low']), num(p['blouse_low']), num(p['sweater_low'])
    rd = p['read_date']
    if p['tee_low'] == 'NC' and p['blouse_low'] == 'NC' and p['sweater_low'] == 'NC':
        return 'Pending', 'price read blocked (' + p['status'] + '); ' + p['note'][:140]
    if tee is not None and bl is not None and tee <= 35 and bl < 80:
        return 'Basic', f"core tee ${tee} and core blouse ${bl} (women's price pass, {rd})"
    if tee is not None and tee <= 35 and p['blouse_low'] == 'NONE' and any(num(p[g + '_low']) is not None for g in ('sweater', 'jeans', 'trousers', 'dress', 'outerwear')):
        return 'Basic', f"core tee ${tee} with no woven blouse sold, another clothing slot priced (the Salomon reading; women's price pass, {rd})"
    staples = [x for x in (bl, sw) if x is not None]
    if staples:
        m = sum(staples) / len(staples)
        what = 'blouse and sweater' if len(staples) == 2 else ('blouse' if bl is not None else 'sweater')
        flag = '; ' + p['band_proposed'] if 'hand' in p['band_proposed'].lower() else ''
        return cut(m), f"mean of {what} entry ${m:.0f} (women's price pass, {rd}){flag}"
    others = [num(p[g + '_low']) for g in ('dress', 'trousers', 'outerwear')]
    others = [x for x in others if x is not None]
    if others:
        m = sum(others) / len(others)
        return cut(m), f"provisional, for ruling: no blouse or sweater, mean of dress/trousers/outerwear entries ${m:.0f} (women's price pass, {rd}); {p['band_proposed']}"
    if num(p['shoes_low']) is not None:
        return cut(num(p['shoes_low'])), f"shoe house, banded on shoe entry ${num(p['shoes_low'])} (women's price pass, {rd})"
    return 'Pending', 'no priced staple; ' + p['note'][:140]


HAND = {'Aritzia': ('Premium', 'core-garment rule, 13 Oct: the $28 ribbed baby tee and $58 smocked top are not its core tee and shirt'),
        'Lucky Brand': ('Basic', 'everyday selling price is the price, 13 Oct: the struck "Comp. Value" is a reference, not a former price'),
        'Suzie Kondi': ('Accessible', 'for ruling, 14 Oct: its only sweater is a $2,295 made-to-order hand-knit, not a staple; seated on the $325 shirt entry beside $295 track pants (thread proposal)'),
        'Miguelina': ('Accessible', 'ruled 14 Oct: resort house with no sweater; tops from $215 and dresses from $495, not the $423 blouse alone (thread proposal)'),
        'GUESS': ('Premium', 'core-garment rule, 13 Oct: the $69 cropped shirt is not its core shirt; the plain Cotton Shirt is $89 (thread re-read)')}

NOT_WOMENS = {'Kartik Research', 'Sanderlak'}  # Kartik: women's menu empty on its own US store (price pass 2); Sanderlak: menswear-led, ruled 14 Oct → men's map
# Ruled 14 Oct: leather and suede are not an elevated material, so a leather piece is never an outerwear high.
# Where the thread named the top non-leather piece, it is used; the rest show the entry only until re-read.
LEATHER_RE = re.compile(r'\b(leather|suede|nappa|lambskin)\b', re.I)
FAUX_RE = re.compile(r'faux|effect|polyurethane|vegan', re.I)
NONLEATHER_HIGH = {'B SIDES': 1400, 'RÙADH': 3900, 'The Frankie Shop': 1150, 'Veronica de Piante': 3790}
_f = os.path.join(ROOT, 'jobs/returns/outerwear_high_womens_2026-10-14/return.csv')
if os.path.exists(_f):
    for _r in csv.DictReader(open(_f, encoding='utf8')):
        if num(_r['outerwear_high']) is not None:
            NONLEATHER_HIGH[_r['brand']] = num(_r['outerwear_high'])
NONLEATHER_HIGH['Lucky Brand'] = 199  # everyday price ruling, 13 Oct: Comp. Value is a reference; Utility Jacket $199 is the dearest undiscounted piece  # women's menu empty on its own US store, every product menswear (price pass 2, 13 Oct)


def k(s):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())


def v(x):
    return '' if x in ('NC', 'NONE', 'np', '', None) else x


def about_of(f):
    """The facts block for the brand page, from the women's facts pass; empty where unread."""
    if not f:
        return None
    CH = {'O': 'its own stores', 'D': 'department stores', 'I': 'independent shops', 'W': 'its own site'}
    founded = ' '.join(x for x in (('Founded in ' + v(f['founded_place'])) if v(f['founded_place']) else '', ('in ' + v(f['founded_year'])) if v(f['founded_year']) else '',
                                   ('by ' + v(f['founders'])) if v(f['founders']) else '') if x).strip()
    return {'sells': v(f['what_it_sells']), 'chan': [CH[c] for c in f['channels'].split(';') if c in CH],
            'founded': (founded + '.') if founded else '', 'owner': v(f['owner_today']), 'ownerurl': v(f['ownership_url']),
            'sig': v(f['signature_product']), 'sigurl': v(f['signature_product_url']), 'pron': v(f['pronunciation']),
            'quote': v(f['quote']), 'who': v(f['quote_who']), 'qsrc': v(f['quote_source']), 'qurl': v(f['quote_url']),
            'look': v(f['lookbook_season_label']) if f['lookbook_found'] == 'yes' else '', 'lookurl': v(f['lookbook_url']) if f['lookbook_found'] == 'yes' else '',
            'vinted': v(f['vinted_womens_url']), 'trr': v(f['therealreal_url']),
            'bcorp': v(f['b_corp_entity']) if f['b_corp'] == 'yes' else '', 'gots': v(f['gots_entity']) if f['gots_certified'] == 'yes' else '',
            'status': f['status'], 'read': f['read_date']}


def tier(n):
    if n is None: return 'NC'
    if n == 0: return 'none'
    if n <= 3: return 'flagship'
    if n <= 12: return 'circuit'
    if n <= 50: return 'network'
    if n <= 250: return 'chain'
    return 'mass'


def main():
    men = {}
    for f in glob.glob(os.path.join(ROOT, 'data/brands/*.json')):
        b = json.load(open(f)); men[k(b['name'])] = b
    counts = {r['brand']: r for r in csv.DictReader(open(os.path.join(ROOT, 'registers/door_counts_womens_2026-10-10.csv'), encoding='utf8'))}
    screen = {r['brand']: r for r in csv.DictReader(open(os.path.join(ROOT, 'registers/screen_womens_2026-10-12.csv'), encoding='utf8'))}
    doors = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(ROOT, 'registers/own_doors_womens_2026-10-10.csv'), encoding='utf8')):
        doors[r['brand']].append(r)
    # price pass
    priced = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'jobs/returns/prices_womens_2026-10-13/batch*/return.csv'))) + \
             sorted(glob.glob(os.path.join(ROOT, 'jobs/returns/prices_womens_2_2026-10-13/return.csv'))):
        for r in csv.DictReader(open(f, encoding='utf8')):
            if r['status'] == 'NC' or (r['tee_low'] == 'NC' and r['blouse_low'] == 'NC' and r['sweater_low'] == 'NC' and r['brand'] in priced):
                continue  # a blocked retry never overwrites a read
            priced[r['brand']] = r
    facts = {}
    ff = os.path.join(ROOT, 'jobs/returns/facts_womens_2026-10-13/return.csv')
    if os.path.exists(ff):
        facts = {r['brand']: r for r in csv.DictReader(open(ff, encoding='utf8'))}
    universe = {r['brand']: r for r in csv.DictReader(open(os.path.join(ROOT, 'registers/womens_universe_counted_2026-10-10.csv'), encoding='utf8'))}

    brands = []
    seen = set()
    # women's register brands with stores
    for name, r in list(counts.items()) + [(n, s) for n, s in screen.items() if n not in counts]:
        n = num(r['us_own_stores'])
        if n is None or n == 0 or k(name) in men or k(name) in seen or name in NOT_WOMENS:
            continue
        seen.add(k(name))
        rows = [d for d in doors.get(name, []) if d['format'] == 'own-door' and d['status'] == 'open']
        p = priced.get(name)
        if name in HAND:
            band, basis = HAND[name]
        elif p:
            band, basis = band_of(p)
        else:
            band, basis = 'Pending', 'not in the women’s price pass (no own store when the worklist was cut)'
        prices = None; leather_high = False
        if p:
            G = ['tee', 'blouse', 'sweater', 'jeans', 'trousers', 'dress', 'outerwear', 'shoes']
            prices = {g: ([num(p[g + '_low']), num(p[g + '_high'])] if num(p[g + '_low']) is not None else p[g + '_low']) for g in G}
            ohp = p['outerwear_high_product']
            if isinstance(prices['outerwear'], list) and LEATHER_RE.search(ohp) and not FAUX_RE.search(ohp):
                prices['outerwear'][1] = NONLEATHER_HIGH.get(name)  # None → entry shown alone, high under re-read
                leather_high = name not in NONLEATHER_HIGH
        stores = [{'sn': d['store_name'], 'a': d['street'], 'c': d['city'], 's': d['state'], 'z': d['zip'] if d['zip'] not in ('NC', 'NONE') else '',
                   'v': d['venue'] if d['venue'].lower() not in ('nc', 'none', '', 'street', 'not stated', 'street / unknown') else '', 'op': d['operator'] if d['operator'] not in ('NC', 'NONE', '', 'none', 'not stated') else ''}
                  for d in rows]
        brands.append({'n': name, 'band': band, 'basis': basis, 'own': n, 'out': num(r.get('us_outlets')) or 0, 'con': num(r.get('us_concessions')) or 0,
                       'tier': tier(n), 'stores': stores, 'ne': sum(1 for s in stores if s['s'] in NE),
                       'locator': r.get('locator_url', ''), 'read': r.get('captured_on', ''), 'note': r.get('note', ''),
                       'src': 'womens' if name in counts else 'screen', 'prices': prices, 'lh': leather_high,
                       'depts': num(universe.get(name, {}).get('full_price_stores') or 0) or 0, 'about': about_of(facts.get(name))})
    # crossovers from the men's map
    places = json.load(open(os.path.join(ROOT, 'data/places.json')))
    wu = {k(n) for n in universe}
    for kk, b in men.items():
        if kk not in wu:
            continue
        d = b.get('doors', {}); n = d.get('n') if d.get('c') in ('full', 'count', 'partial') else None
        if not n:
            continue
        stores = [{'sn': p.get('bn', '') or '', 'a': p.get('a', ''), 'c': p['c'], 's': p['s'], 'z': p.get('z', ''), 'v': p.get('v2', ''), 'op': p.get('op', '')}
                  for p in places if p['k'] == 'o' and p['n'] == b['name']]
        brands.append({'n': b['name'], 'band': BAND[b['band']], 'basis': 'banded on its men’s range (the men’s map)', 'own': n, 'out': d.get('out', 0) or 0,
                       'con': d.get('con', 0) or 0, 'tier': tier(n), 'stores': stores, 'ne': sum(1 for s in stores if s['s'] in NE),
                       'locator': '', 'read': d.get('basis', '')[:40], 'note': 'Also on the men’s map; its stores sell both.', 'src': 'men', 'prices': None,
                       'depts': num(universe.get(b['name'], {}).get('full_price_stores') or 0) or 0})
    brands.sort(key=lambda b: (-b['own'], b['n'].lower()))
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
