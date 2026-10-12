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

FIBW = ['cotton', 'linen', 'wool', 'cashmere', 'yak', 'hemp', 'silk', 'nylon', 'polyester', 'leather', 'suede', 'mohair', 'alpaca']
def title_fibres(t):
    t = t.lower().replace('-', ' ')
    t = re.sub(r'\bcot\b', 'cotton', t); t = re.sub(r'\blin\b', 'linen', t); t = re.sub(r'\bcash\b', 'cashmere', t)
    out = []
    for w in re.findall(r'[a-z]+', t):
        if w in FIBW and w not in out: out.append(w)
    return ' '.join(out)

def prep(c):
    c = (c or '').strip()
    if not c or c.upper().startswith('ND'): return 'ND'
    if c.startswith('KW:'): return ' '.join(c[3:].split('+'))
    c = re.sub(r'\s*-\s*(BODY LINING|LINING|YOKE|PADDING|POCKETING|HOOD LINING|SLEEVES|INSERTS|PIECES).*$', '', c, flags=re.I)
    c = re.sub(r'\s+(LINING|YOKE|PADDING|POCKETING|INSERTS|PIECES|BODY LINING)\s?:.*$', '', c, flags=re.I)
    c = re.sub(r'\s*/\s*(?=\d)', ', ', c)
    c = re.sub(r'(?<=[A-Za-z)])/\s?(?=\d{1,3}\s?%)', ', ', c)
    c = re.sub(r'\s+(Close|Wash|Do not|Turn|Delicate|Protect).*$', '', c)
    return c.strip()

# ------------------------------------------------------------------ categories (canonical, house label)
def cat_esg(r):
    t, ty = r['title'].lower(), r['type']
    if re.search(r'\bshirt\b', t) and 'tee' not in t: return 'shirts', ty
    if ty in ('Polo', 'Polos', 'T-Shirts', 'T-Shirt', 'Jersey'): return 'tees-polos', ty
    if ty == 'Sweaters':
        if re.search(r'sweater|cardigan', t) and 'hood' not in t: return 'knitwear', ty
        return 'sweats', ty
    if ty in ('Sweatshirts', 'Hoodies'): return 'sweats', ty
    if ty == 'Vests': return ('knitwear' if 'club vest' in t else 'outerwear'), ty
    if ty in ('Pants', 'Bottoms'): return ('shorts' if 'short' in t else 'trousers'), ty
    if ty == 'Shorts': return 'shorts', ty
    if ty == 'Tops': return ('sweats' if 'quarter zip' in t else 'outerwear'), ty
    return 'outerwear', ty

def cat_ek(r):
    t, ty = r['title'].lower(), r['type'].lower()
    if 'three button jacket' in t: return 'tailoring', r['type'] or 'jacket (title)'
    if 'tee' in t: return 'tees-polos', r['type'] or 'tee (title)'
    if 'sweatshirt' in t or 'sweatpant' in t: return 'sweats', r['type'] or 'sweats (title)'
    if 'knit' in ty or re.search(r'sweater|cardigan|knit polo', t): return 'knitwear', r['type']
    if re.search(r'short\b|shorts', t) and 'shirt' not in t: return 'shorts', r['type']
    if 'pant' in t: return 'trousers', r['type'] or 'pant (title)'
    if re.search(r'shirt', t): return 'shirts', r['type'] or 'shirt (title)'
    return 'outerwear', r['type'] or 'jacket/coat (title)'

def cat_exp(r):
    lab, t = r['type'], r['title'].lower()
    if lab in ('tees', 'graphic-tees', 'polos', 'sweater-polos'): return 'tees-polos', lab
    if lab in ('dress-shirts', '1mx', 'button-down', 'casual-shirts'): return ('outerwear' if re.search(r'barn jacket|chore jacket', t) else 'shirts'), lab
    if lab == 'hoodies': return ('outerwear' if 'bomber' in t else 'shirts' if 'shirt jacket' in t else 'sweats'), lab
    if lab == 'shirts-all': return ('knitwear' if re.search(r'sweater|cardigan', t) else 'outerwear'), lab
    if lab == 'jeans': return 'denim', lab
    if lab in ('dress-pants', 'casual-pants'):
        if 'sweatshort' in t or 'short' in t: return 'shorts', lab
        if 'sweatpant' in t: return 'sweats', lab
        return 'trousers', lab
    if lab == 'shorts': return 'shorts', lab
    if lab == 'blazers-vests': return ('outerwear' if 'zip jacket' in t else 'tailoring'), lab
    if lab in ('suiting-all', 'coats'): return 'outerwear', lab
    if lab == 'sweaters': return 'knitwear', lab
    return 'other', lab

def cat_ft(r):
    p = r['type']
    if p.startswith('shirts/'):
        if re.search(r't-shirts|henleys|polo-shirts', p): return 'tees-polos', p
        return 'shirts', p
    if p == 'jackets/shirt-jackets': return 'shirts', p
    if p == 'jackets/blazers': return 'tailoring', p
    if p.startswith('jackets/'): return 'outerwear', p
    if p.startswith('sweaters/'): return 'knitwear', p
    if p.startswith('sweatshirts'): return 'sweats', p
    if p.startswith('pants/'): return 'trousers', p
    if p.startswith('jeans'): return 'denim', p
    if p.startswith('shorts/'): return 'shorts', p
    if p.startswith('swim') or p.startswith('basics/'): return 'underwear-swim', p
    return 'other', p

def cat_fn(r):
    ty, t = r['type'], r['title'].lower()
    if ty == 'wovens': return 'shirts', ty
    if ty == 'knits': return ('sweats' if 'sweatshirt' in t else 'tees-polos'), ty
    if ty == 'Denim': return 'denim', ty
    if ty == 'Pants': return 'trousers', ty
    if ty == 'Shorts': return ('underwear-swim' if 'boardshort' in t else 'shorts'), ty
    return 'outerwear', ty

def cat_fry(r): return 'outerwear', r['type']

def cat_fus(r):
    ty = r['type']
    if ty in ('SWEATERS & CARDIGANS', 'SWEATER', 'ZIP UP JACKETS'): return 'knitwear', ty
    if ty == 'SWEATSHIRT': return 'sweats', ty
    if ty in ('THERMAL LAYER', 'BASE LAYER', 'MID LAYER TOPS', 'LEGGINGS'): return 'other', ty
    if ty in ('SKI PANTS', 'PANTS'): return 'trousers', ty
    if 'T-SHIRT' in ty: return 'tees-polos', ty
    return 'outerwear', ty

def cat_gs(r):
    pt, t = r['type'], r['title'].lower()
    if pt in ('T-Shirt', 'Polo', 'Tank top'): return 'tees-polos', pt
    if pt in ('Shirt', 'Overshirts'): return 'shirts', pt
    if pt in ('Sweater', 'Hoodie', 'Sweatpants'): return ('shorts' if 'short' in t else 'sweats'), pt
    if pt in ('Pullovers', 'Cardigan'): return 'knitwear', pt
    if pt in ('5-pocket', '3D'): return ('trousers' if 'pants' in t else 'denim'), pt
    if pt in ('Denim', 'Cargo Short', 'Trainer Short', 'Pocket Short'): return 'shorts', pt
    if pt in ('Cargo Pant', 'Chino', 'Worker pant', 'Biker pant'): return ('shorts' if 'short' in t else 'trousers'), pt
    if pt in ('Swim shorts', 'Trunk'): return 'underwear-swim', pt
    if pt in ('Sleepwear', 'Bathrobes', 'Jumpsuits', 'Dungaree'): return 'other', pt
    if pt == 'Blazers': return 'tailoring', pt
    return 'outerwear', pt

def cat_gd(r):
    ty, t = r['type'], r['title'].lower()
    if ty == 'TOPS': return ('shirts' if re.search(r'shirt|flannel|button down', t) and 'tee' not in t else 'tees-polos'), ty
    if ty == 'SWEATSHIRTS': return 'sweats', ty
    if ty == 'OUTERWEAR': return 'outerwear', ty
    if re.search(r'short|trunks', t): return 'shorts', ty
    if 'sweatpant' in t: return 'sweats', ty
    if re.search(r'denim|flare|cut|bootcut', t): return 'denim', ty
    return 'trousers', ty

# ------------------------------------------------------------------ brand inputs
BR = {}
ESG_F = ['code', 'h', 'title', 'type', 'n', 'lo', 'loH', 'hi', 'hiH', 'comp', 'mi', 'sale', 'tags']
BR['Eastside Golf'] = dict(rows=load('esg_styles.txt', ESG_F), cat=cat_esg, code=lambda r: r['code'],
                           url=lambda r: 'https://eastsidegolf.com/products/' + r['h'], method='product_code')

ek = [r for r in load('ek_styles.txt', ['code', 'h', 'type', 'n', 'lo', 'hi', 'comp', 'mi']) if not re.match(r'orSlow|MAN-TLE', r['code'])]
for r in ek:
    r['title'] = r['code']
    if r['comp'] == 'T':
        tf = title_fibres(r['code'] + ' ' + r['h'])
        r['comp'] = tf if tf else 'ND'
    r['mi'] = {'cottage industry': 'Italy (cottage industry, Lucca)'}.get(r['mi'], r['mi'])
BR['Evan Kinori'] = dict(rows=ek, cat=cat_ek, code=lambda r: re.sub(r'[^a-z0-9]+', '-', r['code'].lower()).strip('-'),
                         url=lambda r: 'https://evankinori.com/products/' + r['h'], method='title_dedup')

exp = [r for r in load('exp_sample.txt', ['code', 'title', 'type', 'lo', 'n', 'comp', 'mi']) if r['code'] != '06957933']
for r in exp: r['hi'] = r['lo']
BR['Express'] = dict(rows=exp, cat=cat_exp, code=lambda r: r['code'], url=lambda r: 'https://www.express.com/exp/search?q=' + r['code'],
                     method='product_code (category-stratified sample)')

ft = load('ft_styles.txt', ['code', 'title', 'type', 'n', 'lo', 'hi', 'comp', 'mi', 'sale', 'h'])
BR['Flint and Tinder'] = dict(rows=ft, cat=cat_ft, code=lambda r: 'HB-' + r['code'],
                              url=lambda r: 'https://huckberry.com/store/flint-and-tinder/category/p/' + r['h'], method='product_group')

fn = load('fn_styles.txt', ['code', 'h', 'title', 'type', 'n', 'lo', 'hi', 'comp', 'mi', 'sale'])
for r in fn:
    if r['type'].lower() == 'leather':
        r['comp'] = 'suede' if 'suede' in r['title'].lower() else 'leather'
    elif r['comp'].startswith('KW:') and r['type'] == 'Denim':
        r['comp'] = 'ND'
BR['Freenote Cloth'] = dict(rows=fn, cat=cat_fn, code=lambda r: r['code'],
                            url=lambda r: 'https://freenotecloth.com/products/' + r['h'], method='product_code')

fry = load('fry_styles.txt', ['title', 'h', 'type', 'vendor', 'n', 'lo', 'hi', 'comp', 'sale'])
for r in fry: r['mi'] = ''
BR['Frye'] = dict(rows=fry, cat=cat_fry, code=lambda r: re.sub(r'[^a-z0-9]+', '-', r['title'].lower()).strip('-'),
                  url=lambda r: 'https://www.thefryecompany.com/products/' + r['h'], method='title_dedup')

fus = load('fus_styles.txt', ['code', 'h', 'title', 'type', 'n', 'lo', 'hi', 'comp', 'mi', 'sale'])
for r in fus: r['mi'] = '' if r['mi'] == '-' else r['mi'].title()
BR['Fusalp'] = dict(rows=fus, cat=cat_fus, code=lambda r: r['code'], url=lambda r: 'https://fusalp.com/en-us/products/' + r['h'], method='product_code')

gs = load('gs_sample.txt', ['code', 'title', 'type', 'n', 'lo', 'hi', 'comp', 'url'])
for r in gs: r['mi'] = ''
BR['G-Star'] = dict(rows=gs, cat=cat_gs, code=lambda r: r['code'], url=lambda r: 'https://www.g-star.com/en_us' + r['url'],
                    method='style_code (category-stratified sample)')

gd0 = load('gd_styles.txt', ['code', 'h', 'title', 'type', 'n', 'lo', 'hi', 'comp', 'mi'])
G = {}
for r in gd0:
    k = r['title'].replace('G-PATCH LOGO HOODIE', 'G-PATCH LOGO HOODIE')
    if k not in G: G[k] = dict(r, n=0, lo=r['lo'], hi=r['hi'])
    g = G[k]; g['n'] = int(g['n']) + int(r['n'] or 1)
    g['lo'] = str(min(float(g['lo']), float(r['lo']))); g['hi'] = str(max(float(g['hi']), float(r['hi'])))
    if (not g['mi'] or g['mi'] == '-') and r['mi'] != '-': g['mi'] = r['mi']
gd = list(G.values())
for r in gd: r['n'] = str(r['n']); r['mi'] = '' if r['mi'] == '-' else r['mi']
BR['Gallery Dept.'] = dict(rows=gd, cat=cat_gd, code=lambda r: re.sub(r'[^a-z0-9]+', '-', r['title'].lower()).strip('-'),
                           url=lambda r: 'https://gallerydept.com/products/' + r['h'], method='title_dedup')

LINES = {
    'Eastside Golf': lambda r: 'Signature' if 'signature' in r['title'].lower() else ('Core' if r['code'].startswith(('EC', 'EGMC')) else '-'),
    'Flint and Tinder': lambda r: '365 Collection' if r['title'].startswith('365') else ('All-American (Made in USA denim)' if 'All-American' in r['title'] else '-'),
    'Express': lambda r: '1MX' if '1MX' in r['title'] else ('Luxtouch' if 'Luxtouch' in r['title'] else '-'),
    'G-Star': lambda r: 'RAW Research (RR/GSRR)' if re.search(r'\bRR\b|GSRR', r['title']) else ('E (premium)' if re.match(r'E ', r['title']) else '-'),
    'Gallery Dept.': lambda r: 'DÉPT.' if 'DÉPT' in r['title'] else ('Retouche' if 'RETOUCHE' in r['title'] else '-'),
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
