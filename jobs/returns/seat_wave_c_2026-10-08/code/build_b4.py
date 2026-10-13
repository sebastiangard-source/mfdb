"""Batch 3 style layer and roll-ups. Inputs: raw captures in raw/ (Chrome, 11 Oct 2026)."""
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


def prep(c):
    c = (c or '').strip()
    if not c or c.upper().startswith('ND'): return 'ND'
    if c.startswith('KW:'): return ' '.join(c[3:].split('+'))
    c = re.sub(r'\s*/\s*(?=\d)', ', ', c)
    c = re.sub(r'(?<=[A-Za-z)])\s?/\s?(?=\d{1,3}\s?%)', ', ', c)
    c = re.sub(r';', ',', c)
    return c.strip()

def T(r): return r['title'].lower()

def cat_gap(r):
    ty, t = r['type'], T(r)
    if ty in ('boxers', 'underwear'): return 'underwear-swim', ty
    if ty in ('sleepwear', 'sleepwear tops'): return 'other', ty
    if ty == 'polos' or 'tees' in ty: return ('other' if 'tank' in t and False else 'tees-polos'), ty
    if ty == 'shirts': return 'shirts', ty
    if ty == 'sweatshirts': return ('shorts' if 'short' in t else 'sweats'), ty
    if ty == 'sweaters': return 'knitwear', ty
    if ty == 'jeans': return ('trousers' if 'corduroy' in t else 'denim'), ty
    if ty == 'pants':
        if 'swim' in t: return 'underwear-swim', ty
        if 'pj' in t: return 'other', ty
        if 'short' in t: return 'shorts', ty
        return 'trousers', ty
    if ty == 'shorts': return 'shorts', ty
    if ty == 'jackets': return ('shirts' if 'shirt jacket' in t else 'outerwear'), ty
    return 'other', ty

def cat_gold(r):
    ty, t = r['type'], T(r)
    if ty == 't-shirts': return ('knitwear' if re.search(r'cardigan|crew$|vest', t) else 'tees-polos'), ty
    if ty == 'shirts-poloshirts': return 'shirts', ty
    if ty in ('sweaters-cardigans',): return 'knitwear', ty
    if ty in ('sweatshirts-hoodies', 'fleece'): return ('outerwear' if 'jacket' in t else 'sweats'), ty
    if ty == 'full-length': return ('denim' if 'jeans' in t else 'trousers'), ty
    if ty == 'shorts': return 'shorts', ty
    return 'outerwear', ty

def cat_gw(r):
    ty, t = r['type'], T(r)
    if re.search(r'boxer|brief', t): return 'underwear-swim', ty
    if re.search(r'tee\b|t-shirt', t): return 'tees-polos', ty
    if 'polo' in t: return 'tees-polos', ty
    if re.search(r'button up|shirt', t) and 'over' not in t: return 'shirts', ty
    if 'sweater' in t: return 'knitwear', ty
    if re.search(r'hoodie|crewneck|sweatpant', t): return 'sweats', ty
    if 'short' in t: return 'shorts', ty
    if re.search(r'denim pant', t): return 'denim', ty
    if 'pant' in t: return 'trousers', ty
    return 'outerwear', ty

def cat_hs(r): return 'outerwear', r['type']

def cat_hb(r):
    ty, t = r['type'], T(r)
    if ty in ('Shirts Polos', 'Shirts T-Shirts'): return 'tees-polos', ty
    if ty == 'Shirts Button Downs': return 'shirts', ty
    if ty == 'Layering Sweaters': return 'knitwear', ty
    if ty == 'Layering Pullovers': return ('knitwear' if re.search(r'sweater|merino', t) else 'sweats'), ty
    if ty.startswith('Outerwear'): return 'outerwear', ty
    if ty == 'Bottoms Pants': return ('denim' if '5 pocket' in t and 'corduroy' not in t and False else 'trousers'), ty
    if ty == 'Bottoms Shorts': return 'shorts', ty
    return 'other', ty

def cat_iw(r):
    ty, t = r['type'], T(r)
    if ty in ("men's rigid", "men's rinse", "men's wash", 'Jeans'):
        return ('trousers' if re.search(r'carpenter|oscar washed brown', t) else 'denim'), ty
    if ty in ("men's pants",): return 'trousers', ty
    if 'short' in t: return 'shorts', ty
    if 'lounge pant' in t or 'chore pant' in t: return 'trousers', ty
    if ty == "men's wovens": return 'shirts', ty
    if ty in ("men's jackets",): return ('knitwear' if 'knit raglan' in t else 'outerwear'), ty
    if ty == "men's sweater": return 'knitwear', ty
    if ty == 'sweatshirt': return 'sweats', ty
    if 'cardigan' in t: return 'knitwear', ty
    return 'tees-polos', ty

def cat_jab(r):
    ty, t = r['type'], T(r)
    if ty in ('suits', 'sportcoats'): return 'tailoring', ty
    if ty == 'dress-shirts': return 'shirts', ty
    if ty == 'casual-tops':
        if re.search(r'polo|tee\b', t) and 'sweater' not in t: return 'tees-polos', ty
        if re.search(r'sweater', t): return 'knitwear', ty
        if 'pullover' in t: return 'sweats', ty
        return 'shirts', ty
    if ty == 'pants': return ('denim' if 'jean' in t else 'shorts' if 'short' in t else 'trousers'), ty
    if ty == 'sweaters': return 'knitwear', ty
    if ty == 'outerwear': return 'outerwear', ty
    return 'other', ty

def cat_kat(r):
    ty, t = r['type'], T(r)
    if ty in ('Trunks', 'Volleys'): return ('shorts' if 'rover short' in t else 'underwear-swim'), ty
    if ty in ('Graphic Tees', 'Graphic Tee', 'Polo'): return 'tees-polos', ty
    if ty == 'Knits': return ('sweats' if re.search(r'hood|pullover', t) else 'tees-polos'), ty
    if ty in ('Fleece', 'Graphic Fleece'): return 'sweats', ty
    if ty in ('Sweaters', 'Sweater'): return 'knitwear', ty
    if ty in ('Shirts', 'Shirt', 'Flannel', 'Shirt Jackets'): return 'shirts', ty
    if ty == 'Pants':
        if re.search(r'lounge', t): return 'sweats', ty
        if re.search(r'\d{2} (baggy|slim|relaxed|classic)', t): return 'denim', ty
        return 'trousers', ty
    if ty == 'Shorts': return ('sweats' if 'lounge' in t else 'shorts'), ty
    return 'outerwear', ty

KJPT = {'FL': "Men's Shirts (flannel)", 'OW': "Men's Outerwear", 'UF': 'Unisex Fleece', 'SJ': "Men's Shirts (shirt jacket)", 'US': 'Unisex Sweatshirts',
        'PC': "Men's Pants (cords)", 'PO': "Men's Shirts (polo)", 'PA': "Men's Pants (other)", 'SW': "Men's Sweaters", 'SC': "Men's Sweaters (custom)",
        'QZ': "Men's Quarterzips", 'TE': "Men's Shirts (SS tee)", 'UW': 'Unisex Sweaters', 'SH': "Men's Shorts", 'SO': "Men's Shirts (other)", 'HE': "Men's Shirts (henley)"}
def cat_kjp(r):
    k = r['tcode']
    m = {'FL': 'shirts', 'SJ': 'shirts', 'SO': 'shirts', 'OW': 'outerwear', 'UF': 'sweats', 'US': 'sweats', 'PC': 'trousers', 'PA': 'trousers',
         'PO': 'tees-polos', 'TE': 'tees-polos', 'HE': 'tees-polos', 'SW': 'knitwear', 'SC': 'knitwear', 'UW': 'knitwear', 'QZ': 'knitwear', 'SH': 'shorts'}
    return m[k], KJPT[k]

# ------------------------------------------------------------------ brand inputs
BR = {}
gap = load('gap_sample.txt', ['code', 'cc', 'type', 'title', 'n', 'lo', 'hi', 'comp', 'mi', 'cap'])
for r in gap: r['mi'] = ''
BR['Gap'] = dict(rows=gap, cat=cat_gap, code=lambda r: r['code'], url=lambda r: 'https://www.gap.com/browse/product.do?pid=' + r['cc'],
                 method='style_id (category-stratified sample)')

gold = [r for r in load('gold_styles.txt', ['code', 'title', 'type', 'lo', 'comp', 'tag']) if r['tag'] != 'collab']
coo = {}
for l in open(os.path.join(RAW, 'gold_coo.txt'), encoding='utf8'):
    c, _, codes = l.partition(':')
    for k in codes.split(): coo[k] = c.strip()
for r in gold:
    r['hi'] = r['lo']; r['n'] = '1'; r['mi'] = '' if coo.get(r['code'], 'Vietnam') == 'None' else coo.get(r['code'], 'Vietnam')
BR['Goldwin'] = dict(rows=gold, cat=cat_gold, code=lambda r: r['code'], url=lambda r: 'https://us.goldwin.global/products/' + r['code'].lower(), method='product_code')

gw = [r for r in load('gw_styles.txt', ['code', 'h', 'title', 'type', 'n', 'lo', 'hi', 'comp', 'line']) if r['line'] == 'own']
for r in gw: r['mi'] = ''
BR['Golf Wang'] = dict(rows=gw, cat=cat_gw, code=lambda r: r['code'], url=lambda r: 'https://golfwang.com/products/' + r['h'], method='product_code')

hs = [dict(code='zw-c-lcj', h='1_1_zw-c-lcj_1/black', title='collar jacket', type='wear', n='2', lo='204050', hi='204050', comp='leather', mi='')]
BR['Hender Scheme'] = dict(rows=hs, cat=cat_hs, code=lambda r: r['code'], url=lambda r: 'https://online.henderscheme.com/item/detail/' + r['h'], method='product_code')

hb = load('hb_styles.txt', ['title', 'h', 'type', 'n', 'nl', 'lo', 'comp', 'mi'])
for r in hb: r['hi'] = r['lo']
BR['Holderness & Bourne'] = dict(rows=hb, cat=cat_hb, code=lambda r: re.sub(r'[^a-z0-9]+', '-', r['title'].lower()).strip('-'),
                                 url=lambda r: 'https://holdernessandbourne.com/products/' + r['h'], method='model_name (collegiate logo versions folded in)')

iw0 = load('iw_styles.txt', ['code', 'h', 'title', 'type', 'n', 'lo', 'comp', 'usa'])
FITS = r'^(limited edition love fades no\.\d+ )?(barton|willie|henry|lewis|hank|hencye|russell|charlie|oscar|sturgill)\b'
IWG = {}
for r in iw0:
    r['hi'] = r['lo']; r['mi'] = ''
    m = re.match(FITS, r['title']) if r['type'] in ("men's rigid", "men's rinse", "men's wash", 'Jeans') else None
    k = ('denim-' + m.group(2)) if m and 'broken twill' not in r['title'] or (m and r['type'] != "men's rigid") else r['code']
    if m and r['code'] == '20210131': k = r['code']
    if k not in IWG: IWG[k] = dict(r, n=0, code=k, title=(m.group(2) + ' jean' if k.startswith('denim-') else r['title']), lo=r['lo'], hi=r['hi'], comps=[])
    g = IWG[k]; g['n'] += int(r['n']); g['lo'] = str(min(float(g['lo']), float(r['lo']))); g['hi'] = str(max(float(g['hi']), float(r['hi'])))
    g['comps'].append(r['comp'])
iw = []
for g in IWG.values():
    cs = [c for c in g['comps'] if c != 'ND']
    g['comp'] = Counter(cs).most_common(1)[0][0] if cs else 'ND'; g['n'] = str(g['n']); iw.append(g)
BR['Imogene + Willie'] = dict(rows=iw, cat=cat_iw, code=lambda r: r['code'], url=lambda r: 'https://imogeneandwillie.com/products/' + r['h'],
                              method='product_code; denim grouped by fit (washes = colourways)')

jab = [r for r in load('jab_sample.txt', ['code', 'type', 'title', 'lo', 'comp', 'mi']) if not r['code'].endswith('_C')]
def slug(n): return re.sub(r'[^a-z0-9]+', '-', n.lower()).strip('-')
for r in jab: r['hi'] = r['lo']; r['n'] = '1'; r['mi'] = ''
BR['Jos. A. Bank'] = dict(rows=jab, cat=cat_jab, code=lambda r: r['code'], url=lambda r: 'https://www.josbank.com/p/' + slug(r['title']),
                          method='part_number (category-stratified sample)')

kat = load('kat_styles.txt', ['code', 'h', 'title', 'type', 'lo', 'comp'])
for r in kat: r['hi'] = r['lo']; r['n'] = '1'; r['mi'] = ''
for r in kat:
    if r['code'] in ('KTNWSISA', 'KTNFLLOU', 'KTNPAPCS'): r['n'] = '2'
BR['Katin'] = dict(rows=kat, cat=cat_kat, code=lambda r: r['code'], url=lambda r: 'https://katinusa.com/products/' + r['h'], method='product_code')

kjp = load('kjp_styles.txt', ['title', 'h', 'tcode', 'n', 'lo', 'comp', 'mi'])
for r in kjp: r['hi'] = r['lo']; r['type'] = KJPT[r['tcode']]
BR['Kiel James Patrick'] = dict(rows=kjp, cat=cat_kjp, code=lambda r: r['h'], url=lambda r: 'https://kieljamespatrick.com/products/' + r['h'],
                                method='title_dedup (colour suffix stripped)')

LINES = {
    'Gap': lambda r: 'GapStudio' if 'GapStudio' in r['title'] else ('OuiGap (capsule)' if 'OuiGap' in r['title'] else ('Hill City' if 'Hill City' in r['title'] else '-')),
    'Goldwin': lambda r: 'Goldwin 0' if r['title'].startswith('Goldwin 0') else '-',
    'Jos. A. Bank': lambda r: ('Reserve' if 'Reserve' in r['title'] else '1905' if '1905' in r['title'] else 'Traveler' if 'Traveler' in r['title'] else '-'),
    'Katin': lambda r: 'OTG (Out There Gear)' if r['title'].startswith('OTG') else '-',
}

styles_out, agg = [], {}
for b, cfg in BR.items():
    rows = []
    for r in cfg['rows']:
        cat, house = cfg['cat'](r)
        raw = prep(r.get('comp'))
        nd = raw == 'ND'
        s = style_row(raw if not nd else 'ND')
        notes = [x for x in [s['note']] if x]
        n = str(r.get('n') or '1')
        if n not in ('', '1'): notes.append(f'{n} colourways/listings collapsed')
        if nd: notes.append('page read; no fibre composition stated')
        if b == 'Evan Kinori' and not re.search(r'\d%', r.get('comp', '')) and not nd: notes.append('fibre named in the title (no % on page)')
        if b == 'Freenote Cloth' and r['type'].lower() == 'leather': notes.append('hide named in title; body composition is the lining')
        line = LINES.get(b, lambda r: '-')(r)
        rows.append(dict(brand=b, style_code=cfg['code'](r), title=r['title'].strip(), url=cfg['url'](r), category=cat, category_house=house, lines=line,
                         composition=raw if not nd else 'ND', lead_fibre=s['lead_fibre'] if not nd else 'ND', lead_pct=s['lead_pct'] if not nd else 'ND',
                         elastane_pct=s['elastane_pct'] if not nd else 'ND', pure=s['pure'] if not nd else 'undisclosed',
                         single_fibre=s['single_fibre'] if not nd else '-', note='; '.join(notes) or '-', _s=s if not nd else dict(s, has=False, cls=None, sp=0, sph=0)))
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
    swim = sum(1 for r in rows if r['category'] == 'underwear-swim' and re.search(r'swim|board|trunk', r['category_house'] + ' ' + r['title'], re.I) and not re.search(r'boxer|brief', r['title'], re.I))
    raw_n = sum(int(r.get('n') or 1) for r in cfg['rows'])
    agg[b] = dict(styles_total=n, styles_with_composition=wc, natural_pct=pct('natural'), synthetic_pct=pct('synthetic'), cellulosic_pct=pct('cellulosic'),
                  spandex_styles=sum(r['_s']['sp'] for r in rows), shape=shape, natural_categories=json.dumps(nat[:3], ensure_ascii=False),
                  synthetic_categories=json.dumps(syn, ensure_ascii=False), colourway_ratio=f'{raw_n}/{n}', style_method=cfg['method'], swim_styles=swim,
                  swim_share_of_range=(int(100 * swim / n + 0.5) if n else 'NC'), mens_styles_excl_swim=n - swim, _cov=wc / n if n else 0,
                  _madein=sum(1 for r in cfg['rows'] if (r.get('mi') or '').strip() not in ('', '-')))

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
