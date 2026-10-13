"""Batch 2 style layer and roll-ups. Inputs are the raw captures in raw/ (Chrome, 11 Oct 2026)."""
import csv, json, re, sys, os
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fibre import style_row

RAW = os.path.join(HERE, 'raw')

def load(name, fields):
    rows = []
    for l in open(os.path.join(RAW, name), encoding='utf8'):
        l = l.rstrip('\n')
        if not l.strip(): continue
        f = l.split('~'); f += [''] * (len(fields) - len(f))
        rows.append(dict(zip(fields, f)))
    return rows

# ------------------------------------------------------------------ composition clean-up (main line only)
def prep(comp):
    c = (comp or '').strip()
    if not c or c.upper().startswith('ND'): return c
    c = c.replace('|', ';')
    c = re.sub(r'\s+(Fully lined|bonded to)\b.*$', '', c, flags=re.I)
    c = re.sub(r',?\s+Trim\s+\d.*$', '', c)
    c = re.sub(r'(\d)%/(?=[A-Za-z])', r'\1% ', c)
    c = re.sub(r'\s+(Futter|Lining|Liner|Filling|Fill|Padding|Back|Hood|Overlays|Trim|Collar|Pocketing|Piping)\s*:', '; Lining:', c, flags=re.I)
    c = re.sub(r'\(Body\).*$', '', c)                       # Danner liner jacket: body named after its blend
    c = re.sub(r'\s(Shell),\s*Suede,.*$', '', c)               # Danner "100% Cotton Shell, Suede, 100% Polyester Lining"
    c = re.sub(r'\s+/\s+(?=\d)', ', ', c)                       # "61% Polyester / 37% Cotton / 2% Elastane"
    c = re.sub(r'(?<=[A-Za-z])/\s?(?=\d{1,3}\s?%)', ', ', c)    # "65% Polyester/35% Cotton"
    c = re.sub(r'\b(\d+(?:\.\d)?)\s?oz\.?\s*', '', c)            # fabric weights
    c = re.sub(r'(\d+)\s?gsm\.?', '', c, flags=re.I)
    # Castaway slash format: "98/2 Cotton/Stretch", "60/40% Cotton/Polyester", "91/9 Poly/Spandex"
    m = re.search(r'(\d{1,3})/(\d{1,3})%?\s+([A-Za-z]+)/([A-Za-z]+)', c)
    if m:
        a, b, f1, f2 = m.groups()
        f2 = 'Elastane' if f2.lower() == 'stretch' else f2
        c = c[:m.start()] + f'{a}% {f1}, {b}% {f2}' + c[m.end():]
    c = re.sub(r'(\d{1,3})\s?%\s?Cotton/Suede', r'\1% Cotton', c)
    c = re.sub(r'^Produced in (100% \w+).*$', r'\1', c, flags=re.I)
    return c

# ------------------------------------------------------------------ category functions
def cat_bd(r):
    t, ty = r['title'].lower(), r['type']
    if ty == 'pant': return ('denim' if re.search(r'denim|selvedge|type 0', t) else 'trousers'), 'pant'
    if ty == 'shirt' and 'polo' in t: return 'tees-polos', 'shirt'
    m = {'t-shirt': 'tees-polos', 'shirt': 'shirts', 'jacket': 'outerwear', 'sweater': 'knitwear', 'hoodie': 'sweats',
         'sweatshirt': 'sweats', 'shorts': 'shorts', 'pullover': 'outerwear'}
    c = m[ty]
    if ty == 'sweater' and 'sweatshirt' in t: c = 'sweats'
    return c, ty

def cat_budd(r):
    ty = r['type']
    m = {'Knitwear': 'knitwear', 'Pyjamas': 'other', 'Nightshirts': 'other', 'Dressing Gowns': 'other', 'Underwear': 'underwear-swim',
         'Dress Waistcoats': 'tailoring', 'Shirts': 'shirts', 'Day Shirts': 'shirts', 'Dress Shirts': 'shirts', 'Casual Shirts': 'shirts'}
    return m[ty], ty

def cat_cp(r):
    c, t = r['type'], r['title'].lower()
    base = c.split('/')[-1]
    m = {'jackets-coats': 'outerwear', 'overshirts': 'shirts', 'blazers': 'tailoring', 'shirts': 'shirts', 'sweatshirts': 'sweats',
         'knitwear': 'knitwear', 't-shirts-polos': 'tees-polos', 'trousers': 'trousers', 'tracksuits-shorts': 'sweats'}
    if base == 'tennis-kit': return ('shorts' if 'short' in t else 'tees-polos'), 'tennis-kit'
    return m[base], ('Metropolis ' if c.startswith('X/') else '') + base

def cat_cast(r):
    t = r['title'].lower()
    if 'boxer' in t: return 'underwear-swim', r['type']
    if 'sleeper' in t: return 'other', r['type']
    if re.search(r'blazer|sportcoat|tweedbank', t): return 'tailoring', r['type']
    if re.search(r'sweater|cricket vest|crew neck', t): return 'knitwear', r['type']
    if re.search(r'quarterzip|sweatshirt', t): return 'sweats', r['type']
    if re.search(r'polo|tee', t): return 'tees-polos', r['type']
    if re.search(r'jacket|vest', t): return 'outerwear', r['type']
    if re.search(r'short', t) and 'shirt' not in t: return 'shorts', r['type']
    if re.search(r'pant', t): return 'trousers', r['type']
    return 'shirts', r['type']

def cat_closed(r):
    c, t = r['type'], r['title'].lower()
    if c == 'men-hosen': return ('sweats' if 'track' in t else 'trousers'), 'Hosen'
    if c == 'men-jeans': return ('trousers' if 'linen' in t else 'denim'), 'Jeans'
    if c == 'men-jacken': return ('tailoring' if 'blazer' in t else 'outerwear'), 'Jacken & Mäntel'
    if c == 'men-hemden': return 'shirts', 'Hemden'
    if c == 'men-strick': return 'knitwear', 'Strick'
    if c == 'men-t': return ('sweats' if re.search(r'sweat|hoodie|track', t) else 'tees-polos'), 'T-Shirts & Sweatshirts'
    return 'other', c

def cat_danner(r):
    c = r['type']
    if 'overlook thermal' in r['title'].lower(): c = 'shirts'
    return c, 'derived: ' + c

def cat_dt(r):
    ty = r['type']
    m = {'SS Tee': 'tees-polos', 'Tee': 'tees-polos', 'LS Tee': 'tees-polos', 'Thermal': 'tees-polos', 'Polo': 'tees-polos', 'Rugby': 'tees-polos',
         'Sports Jersey': 'tees-polos', 'Basic Light Jacket': 'outerwear', 'Puffer Jacket': 'outerwear', 'Varsity Jacket': 'outerwear',
         'Track Jacket': 'sweats', 'Trench Coat': 'outerwear', 'Vest': 'outerwear', 'Denim Jacket': 'outerwear', 'Quarter Zip': 'sweats',
         'Zip Hoodie': 'sweats', 'Hoodie': 'sweats', 'Crewneck': 'sweats', 'Half Zip': 'sweats', 'Sweatpant': 'sweats', 'Track Pant': 'sweats',
         'Sweat Short': 'shorts', 'Denim Short': 'shorts', 'Leather Pant': 'trousers', 'Pant': 'trousers', 'Jean': 'denim',
         'Denim Pant - STRAIGHT': 'denim', 'Denim Pant - Baggy': 'denim', 'Sweater': 'knitwear', 'LS Shirt': 'shirts', 'Button Up': 'shirts',
         'Boxers': 'underwear-swim'}
    c = m[ty]
    if ty == 'Leather Pant' and 'short' in r['title'].lower(): c = 'shorts'
    return c, ty

def cat_deus(r):
    ty, t = r['type'], r['title'].lower()
    if re.search(r'boardshort|board short|swim', t) or ty in ('Board Shorts', 'Boardshorts'): return 'underwear-swim', ty
    if ty == 'Pants': return ('denim' if 'jean' in t else 'trousers'), ty
    m = {'Jackets': 'outerwear', 'T-Shirts': 'tees-polos', 'Long Sleeve T-Shirts': 'tees-polos', 'Tees': 'tees-polos', 'Tanks': 'tees-polos',
         'Moto Jerseys': 'tees-polos', 'Jerseys': 'tees-polos', 'Shorts': 'shorts', 'Sweats': 'sweats', 'Fleece': 'sweats',
         'Hoodies & Sweaters': 'sweats', 'Shirts': 'shirts', 'Knitwear': 'knitwear', 'Sweaters': 'knitwear'}
    c = m[ty]
    if ty == 'Jackets' and 'fleece' in t: c = 'sweats'
    return c, ty

def cat_dk(r):
    ty, t = r['type'], r['title'].lower()
    if ty.startswith('pants'):
        if re.search(r'jean|denim', t): return 'denim', ty
        return 'trousers', ty
    if ty == 'jeans': return 'denim', ty
    if ty.startswith('shorts'): return 'shorts', ty
    if ty in ('bib-overalls', 'coveralls'): return 'other', ty
    if ty == 'shirts-tshirts': return 'tees-polos', ty
    if ty == 'shirts':
        if re.search(r't-shirt|tee\b|polo|henley|sun shirt', t): return 'tees-polos', ty
        return 'shirts', ty
    if ty in ('outerwear-shirt-jackets', 'shirt-jacket'): return 'shirts', ty
    if ty == 'outerwear-hoodies-sweatshirts': return ('knitwear' if 'sweater' in t else 'sweats'), ty
    if ty.startswith('outerwear'): return 'outerwear', ty
    return 'other', ty

BD = 'https://wearebraindead.com/products/'
BR = {}
BR['Brain Dead'] = dict(rows=load('bd_styles.txt', ['h', 'title', 'type', 'sku', 'price', 'compare', 'comp', 'mi']), cat=cat_bd,
                        code=lambda r: (re.match(r'BD[A-Z]\d\d[A-Z]\d{2}(\d{4,6}?)(?:[A-Z]{2}\d{2})$', r['sku']) or [None, r['sku']])[1] and ('BD-' + re.match(r'BD[A-Z]\d\d[A-Z]\d{2}(\d{4,6}?)(?:[A-Z]{2}\d{2})$', r['sku']).group(1)) if re.match(r'BD[A-Z]\d\d[A-Z]\d{2}(\d{4,6}?)(?:[A-Z]{2}\d{2})$', r['sku']) else r['sku'],
                        url=lambda r: BD + r['h'], method='product_code', group=True)
BR['Budd Shirtmakers'] = dict(rows=load('budd_styles.txt', ['code', 'h', 'title', 'type', 'comp', 'mill', 'mi', 'n', 'lo', 'hi']), cat=cat_budd,
                              code=lambda r: r['code'] if r['code'] != '-' else r['h'], url=lambda r: 'https://www.buddshirts.co.uk/products/' + r['h'], method='product_code')
BR['C.P. Company'] = dict(rows=[r for r in load('cp_styles.txt', ['code', 'path', 'title', 'type', 'price', 'comp', 'mi'])], cat=cat_cp,
                          code=lambda r: r['code'], url=lambda r: 'https://www.cpcompany.com/en-us/' + r['path'], method='product_code')
BR['Castaway Nantucket Island'] = dict(rows=load('castaway_styles.txt', ['code', 'h', 'title', 'type', 'n', 'lo', 'hi', 'comp', 'mi']), cat=cat_cast,
                                       code=lambda r: r['code'], url=lambda r: 'https://www.castawayclothing.com/products/' + r['h'], method='product_code')
BR['Closed'] = dict(rows=load('closed_styles.txt', ['code', 'h', 'title', 'type', 'lo', 'hi', 'comp', 'mi', 'n']), cat=cat_closed,
                    code=lambda r: r['code'], url=lambda r: 'https://www.closed.com/products/' + r['h'], method='product_code')
BR['Danner'] = dict(rows=load('danner_styles.txt', ['code', 'h', 'title', 'type', 'n', 'price', 'comp', 'mi']), cat=cat_danner,
                    code=lambda r: r['code'], url=lambda r: 'https://www.danner.com/' + r['h'] + '.html', method='title_dedup')
BR['Denim Tears'] = dict(rows=load('dt_styles.txt', ['h', 'title', 'type', 'lo', 'hi', 'comp', 'mi', 'n']), cat=cat_dt,
                         code=lambda r: r['h'], url=lambda r: 'https://denimtears.com/products/' + r['h'], method='title_dedup')
BR['Deus Ex Machina'] = dict(rows=[r for r in load('deus_styles.txt', ['code', 'h', 'title', 'type', 'n', 'lo', 'hi', 'cmp', 'comp'])
                                    if not re.search(r'Deus x AGTZ|Attaquer', r['title'])], cat=cat_deus,
                             code=lambda r: r['code'], url=lambda r: 'https://deuscustoms.com/products/' + r['h'], method='product_code')
BR['Dickies'] = dict(rows=load('dickies_styles.txt', ['code', 'h', 'title', 'type', 'n', 'lo', 'hi', 'cmp', 'comp']), cat=cat_dk,
                     code=lambda r: r['code'], url=lambda r: 'https://www.dickies.com/en-us/products/' + r['h'], method='product_code')

# Brain Dead: collapse colourways on the 6-digit style number
def bd_group(rows):
    g = {}
    for r in rows:
        m = re.match(r'BD[A-Z]\d\d[A-Z]\d{2}(\d{4,6}?)([A-Z]{2}\d{2})$', r['sku'])
        k = m.group(1).zfill(6) if m else r['sku']
        g.setdefault(k, []).append(r)
    out = []
    for k, a in g.items():
        f = dict(a[0]); f['n'] = str(len(a)); f['code'] = 'BD' + k
        f['title'] = re.sub(r'\s+-\s+[^-]+$', '', f['title'])
        if not f['comp']:
            f['comp'] = next((x['comp'] for x in a if x['comp']), '')
        out.append(f)
    return out
BR['Brain Dead']['rows'] = bd_group(BR['Brain Dead']['rows'])
BR['Brain Dead']['code'] = lambda r: r['code']

LINES = {
    'C.P. Company': lambda r: 'Metropolis Series' if r['type'].startswith('X/') else ('Tennis kit (Hard Court/Grass/Clay editions)' if r['type'] == 'tennis-kit' else '-'),
    'Brain Dead': lambda r: 'Brain Dead Equipment' if 'equipment' in r['title'].lower() else ('Type 00/02/03 denim' if re.search(r'type 0\d', r['title'].lower()) else ('Fantasy Games' if 'fantasy' in r['title'].lower() else '-')),
    'Denim Tears': lambda r: 'Cotton Wreath' if 'wreath' in r['title'].lower() else ('André Leon Talley' if 'talley' in r['title'].lower() else ('ADG (African Diaspora Goods)' if 'adg' in r['title'].lower() else '-')),
    'Dickies': lambda r: ('874' if '874' in r['title'] else 'FLEX' if 'FLEX' in r['title'] else 'Pro Series' if 'Pro Series' in r['title'] else 'Tradebuilt' if 'Tradebuilt' in r['title']
                          else 'Dickies Skateboarding' if 'Skateboarding' in r['title'] or r['type'].endswith('skate') else 'Worn In' if 'Worn In' in r['title'] else '-'),
    'Danner': lambda r: 'Made in USA' if r['mi'] == 'United States' else '-',
    'Deus Ex Machina': lambda r: 'Address (city tees)' if 'address' in r['title'].lower() else '-',
}

styles_out, agg = [], {}
for b, cfg in BR.items():
    rows = []
    for r in cfg['rows']:
        cat, house = cfg['cat'](r)
        raw = (r.get('comp') or '').strip()
        raw = re.sub(r'^N(?=\d)', '', raw)
        raw = re.sub(r'\s+(\d{2}\s?°C|Feinw|fine wash|nicht |sehr |milde|mild |schonende|Do not|im$).*$', '', raw, flags=re.I).strip()
        nd = (not raw) or raw.upper().startswith('ND')
        s = style_row(prep(raw) if not nd else 'ND')
        notes = [x for x in [s['note']] if x]
        n = r.get('n') or '1'
        if n not in ('', '1'): notes.append(f'{n} colourways/listings collapsed')
        if nd and raw.startswith('ND ('): notes.append(raw[3:].strip('() '))
        if nd and not raw.startswith('ND ('): notes.append('page read; no fibre composition stated')
        if b == 'Castaway Nantucket Island' and re.search(r'\d+/\d+', raw): notes.append('house writes slash format; "Stretch" filed as elastane')
        if b == 'Budd Shirtmakers' and r.get('mill'): notes.append('mill named on page: ' + r['mill'])
        line = LINES.get(b, lambda r: '-')(r)
        comp_out = raw if not nd else 'ND'
        rows.append(dict(brand=b, style_code=cfg['code'](r), title=r['title'].strip(), url=cfg['url'](r), category=cat, category_house=house, lines=line,
                         composition=comp_out.replace(' (named, no %)', ''), lead_fibre=s['lead_fibre'], lead_pct=s['lead_pct'], elastane_pct=s['elastane_pct'],
                         pure=s['pure'] if not nd else 'undisclosed', single_fibre=s['single_fibre'], note='; '.join(notes) or '-', _s=s if not nd else dict(s, has=False, cls=None, sp=0, sph=0)))
    styles_out += rows
    n = len(rows); wc = sum(1 for r in rows if r['_s']['has'])
    cls = Counter(r['_s']['cls'] for r in rows if r['_s']['has'])
    pct = lambda k: int(100 * cls.get(k, 0) / n + 0.5) if n else 'NC'
    cats = defaultdict(Counter); catn = Counter()
    for r in rows:
        catn[r['category_house']] += 1
        if r['_s']['has']: cats[r['category_house']][r['_s']['cls']] += 1
    led = {c: cc.most_common(1)[0][0] for c, cc in cats.items() if cc}
    swimc = {r['category_house'] for r in rows if r['category'] == 'underwear-swim'}
    syn = [c for c in led if led[c] == 'synthetic' and c not in swimc]
    nat = sorted([c for c in led if led[c] == 'natural' and c not in swimc], key=lambda c: -catn[c])
    big_syn = [c for c in syn if catn[c] >= 10]
    shape = 'split' if big_syn and nat else 'one'
    swim = sum(1 for r in rows if r['category'] == 'underwear-swim' and re.search(r'swim|board', r['category_house'] + ' ' + r['title'], re.I))
    raw_n = sum(int(r.get('n') or 1) for r in cfg['rows'])
    agg[b] = dict(styles_total=n, styles_with_composition=wc, natural_pct=pct('natural'), synthetic_pct=pct('synthetic'), cellulosic_pct=pct('cellulosic'),
                  spandex_styles=sum(r['_s']['sp'] for r in rows), shape=shape, natural_categories=json.dumps(nat[:3], ensure_ascii=False),
                  synthetic_categories=json.dumps(syn, ensure_ascii=False), colourway_ratio=f'{raw_n}/{n}', style_method=cfg['method'], swim_styles=swim,
                  swim_share_of_range=(int(100 * swim / n + 0.5) if n else 'NC'), mens_styles_excl_swim=n - swim, _cov=wc / n if n else 0,
                  _madein=sum(1 for r in cfg['rows'] if (r.get('mi') or '').strip()))

if __name__ == '__main__':
    for b, a in agg.items():
        print(b, {k: v for k, v in a.items()})
    cols = ['brand', 'style_code', 'title', 'url', 'category', 'category_house', 'lines', 'composition', 'lead_fibre', 'lead_pct', 'elastane_pct', 'pure', 'single_fibre', 'note']
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    with open(os.path.join(HERE, 'out', 'return_styles.csv'), 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, cols, extrasaction='ignore'); w.writeheader(); w.writerows(styles_out)
    print(len(styles_out), 'style rows')
    bad = [r for r in styles_out if 'sums to' in r['note'] or 'unparsed' in r['note']]
    print('parse flags:', len(bad))
    for r in bad[:60]: print('  ', r['brand'], '|', r['composition'][:70], '|', r['note'][:80])
