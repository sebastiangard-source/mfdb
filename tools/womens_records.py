#!/usr/bin/env python3
"""Write the women's brand records in the men's record shape.

    python3 tools/womens_records.py        writes data/brands_womens/<slug>.json, one per women's-only brand

The record is the men's one (data/brands/*.json) with the men's keys that have a women's reading: name, band,
band_note, why, origin, chan, say, onething, prices (eight slots), garments, price_evidence, price_read, doors,
site, ownership, season, opview, quote, resale, certs. No dials. A crossover (a men's-map brand in the women's
universe) has no record here; the women's build reads its men's record. Every value traces to a return in
jobs/returns: doors_womens_*, prices_womens_*, prices_womens_2_*, outerwear_high_womens_*, facts_womens_*.
"""
import csv, json, os, re, glob, collections, unicodedata, datetime


def num(v):
    try:
        return int(float(v))
    except Exception:
        return None


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data/brands_womens')
BAND_KEY = {'Basic': 'basic', 'Premium': 'premium', 'Accessible': 'accessible', 'True Luxury': 'trueLux', 'Pending': 'pending'}
G = ['tee', 'blouse', 'sweater', 'jeans', 'trousers', 'dress', 'outerwear', 'shoes']
GARMENTS = ['T-shirt', 'Blouse', 'Sweater', 'Jeans', 'Trousers', 'Dress', 'Outerwear', 'Shoes']


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
NONLEATHER_HIGH['Lucky Brand'] = 199  # everyday price ruling, 13 Oct: Comp. Value is a reference; Utility Jacket $199 is the dearest undiscounted piece




def k(s):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()).strip('-')


def v(x):
    return '' if x in ('NC', 'NONE', 'np', '', None) else x


def price_slot(p, g):
    lo, hi = num(p[g + '_low']), num(p[g + '_high'])
    if lo is None:
        return None if p[g + '_low'] == 'NONE' else ('np' if p[g + '_low'] == 'np' else '?')
    return [lo, hi if hi is not None else lo]


def main():
    men = {k(json.load(open(f))['name']) for f in glob.glob(os.path.join(ROOT, 'data/brands/*.json'))}
    counts = {r['brand']: r for r in csv.DictReader(open(os.path.join(ROOT, 'registers/door_counts_womens_2026-10-10.csv'), encoding='utf8'))}
    screen = {r['brand']: r for r in csv.DictReader(open(os.path.join(ROOT, 'registers/screen_womens_2026-10-12.csv'), encoding='utf8'))}
    doors = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(ROOT, 'registers/own_doors_womens_2026-10-10.csv'), encoding='utf8')):
        if r['format'] == 'own-door' and r['status'] == 'open':
            doors[r['brand']].append(r)
    priced = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'jobs/returns/prices_womens_2026-10-13/batch*/return.csv'))) + \
             sorted(glob.glob(os.path.join(ROOT, 'jobs/returns/prices_womens_2_2026-10-13/return.csv'))):
        for r in csv.DictReader(open(f, encoding='utf8')):
            if r['status'] == 'NC' or (r['tee_low'] == 'NC' and r['blouse_low'] == 'NC' and r['sweater_low'] == 'NC' and r['brand'] in priced):
                continue
            priced[r['brand']] = r
    facts = {}
    ff = os.path.join(ROOT, 'jobs/returns/facts_womens_2026-10-13/return.csv')
    if os.path.exists(ff):
        facts = {r['brand']: r for r in csv.DictReader(open(ff, encoding='utf8'))}
    universe = {r['brand']: r for r in csv.DictReader(open(os.path.join(ROOT, 'registers/womens_universe_counted_2026-10-10.csv'), encoding='utf8'))}
    oh = {}
    of = os.path.join(ROOT, 'jobs/returns/outerwear_high_womens_2026-10-14/return.csv')
    if os.path.exists(of):
        oh = {r['brand']: r for r in csv.DictReader(open(of, encoding='utf8'))}

    os.makedirs(OUT, exist_ok=True)
    for f in glob.glob(os.path.join(OUT, '*.json')):
        os.remove(f)
    n_out = 0; seen = set()
    for name, r in list(counts.items()) + [(n, s) for n, s in screen.items() if n not in counts]:
        n = num(r['us_own_stores'])
        if n is None or n == 0 or k(name) in men or k(name) in seen or name in NOT_WOMENS:
            continue
        seen.add(k(name))
        p = priced.get(name); fa = facts.get(name)
        if name in HAND:
            band, basis = HAND[name]
        elif p:
            band, basis = band_of(p)
        else:
            band, basis = 'Pending', 'not in the women\u2019s price pass (no own store when the worklist was cut)'
        rec = {'name': name, 'band': BAND_KEY[band], 'band_note': basis, 'women': True, 'garments': GARMENTS}
        # facts
        if fa:
            CH = {'O': 'O', 'D': 'D', 'I': 'I', 'W': 'W'}
            rec['why'] = v(fa['what_it_sells'])
            parts = [x for x in (('in ' + v(fa['founded_place'])) if v(fa['founded_place']) else '', ('in ' + v(fa['founded_year'])) if v(fa['founded_year']) else '',
                                 ('by ' + v(fa['founders'])) if v(fa['founders']) else '') if x]
            rec['origin'] = ('Founded ' + ' '.join(parts) + '.') if parts else 'Founding date and place not published by the brand.'
            rec['chan'] = [c for c in fa['channels'].split(';') if c in CH]
            if v(fa['pronunciation']): rec['say'] = fa['pronunciation']
            if v(fa['signature_product']): rec['onething'] = {'p': fa['signature_product'], 'u': v(fa['signature_product_url']), 'n': 'facts pass ' + fa['read_date']}
            if v(fa['owner_today']): rec['ownership'] = {'owner': fa['owner_today'], 'u': v(fa['ownership_url'])}
            if fa['lookbook_found'] == 'yes': rec['season'] = {'l': v(fa['lookbook_season_label']) or 'current', 't': 'lookbook', 'u': v(fa['lookbook_url']), 'm': 'yes' if fa['lookbook_womens'] == 'yes' else 'no'}
            if v(fa['quote']):
                rec['quote'] = {'q': fa['quote'], 'who': v(fa['quote_who']), 'src': v(fa['quote_source']), 'u': v(fa['quote_url']), 'd': v(fa['quote_date'])}
                rec['opview'] = '\u201c' + fa['quote'] + '\u201d \u2014 ' + ', '.join(x for x in (v(fa['quote_who']), v(fa['quote_source'])) if x)
            resale = {}
            if v(fa['vinted_womens_url']): resale['vinted'] = {'u': fa['vinted_womens_url'], 'm': 'brand filter', 'n': v(fa['vinted_brand_ids'])}
            if v(fa['therealreal_url']): resale['therealreal'] = {'u': fa['therealreal_url']}
            if resale: rec['resale'] = resale
            certs = {}
            if fa['b_corp'] == 'yes': certs['bcorp'] = {'e': v(fa['b_corp_entity']) or name}
            if fa['gots_certified'] == 'yes': certs['gots'] = {'e': v(fa['gots_entity']) or name}
            if certs: rec['certs'] = certs
            rec['facts_read'] = {'date': fa['read_date'], 'status': fa['status'], 'source': fa['source']}
        else:
            rec['why'] = ''; rec['origin'] = 'Not yet read.'; rec['chan'] = ['O']
        # prices
        if p:
            prices = [price_slot(p, g) for g in G]
            ohp = p['outerwear_high_product']
            if isinstance(prices[6], list) and LEATHER_RE.search(ohp) and not FAUX_RE.search(ohp):
                hi = NONLEATHER_HIGH.get(name)
                prices[6] = [prices[6][0], hi] if hi is not None else [prices[6][0], prices[6][0]]
                rec['leather_high_held'] = hi is None
            rec['prices'] = prices
            pe = {}
            for g, gn in zip(G, GARMENTS):
                if num(p[g + '_low']) is not None:
                    e = {'lp': p[g + '_low_product'], 'lu': p[g + '_low_url'], 'hp': p[g + '_high_product'], 'hu': p[g + '_high_url'], 'b': p[g + '_basis']}
                    if g == 'outerwear' and name in oh and num(oh[name]['outerwear_high']) is not None:
                        e.update({'hp': oh[name]['outerwear_high_product'], 'hu': oh[name]['outerwear_high_url'], 'b': oh[name]['outerwear_basis']})
                    pe[gn] = e
            rec['price_evidence'] = pe
            rec['price_read'] = {'date': p['read_date'], 'store': p['store_used'], 'currency': p['currency'], 'status': p['status'], 'sublines': v(p['sublines_included']) or '-'}
        # doors
        rows = doors.get(name, [])
        cities = collections.Counter((d['city'], d['state']) for d in rows)
        rec['doors'] = {'c': 'full' if rows else 'count', 'n': n, 'cities': sorted([[c, s, x] for (c, s), x in cities.items()]),
                        'basis': 'doors_womens ' + (r.get('captured_on') or ''), 'out': num(r.get('us_outlets')) or 0, 'con': num(r.get('us_concessions')) or 0,
                        'locator': r.get('locator_url', ''), 'note': r.get('note', '')}
        rec['cities'] = f"{n} stores across the US"
        dom = (fa['site_domain'] if fa else '') or re.sub(r'^https?://(www\.)?', '', r.get('locator_url', '')).split('/')[0]
        rec['site'] = {'domain': dom}
        rec['depts'] = num(universe.get(name, {}).get('full_price_stores') or 0) or 0
        rec['src'] = 'womens' if name in counts else 'screen'
        json.dump(rec, open(os.path.join(OUT, slug(name) + '.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
        n_out += 1
    print(f'{n_out} women\u2019s records -> data/brands_womens/')


if __name__ == '__main__':
    main()
