import csv, json, re, sys
from collections import Counter, defaultdict
sys.path.insert(0, '/home/claude/wc/b1')
from fibre import style_row

D = '2026-10-10'
HDR = next(csv.reader(open('/home/claude/wc/return_template.csv')))

def money(x):
    """whole dollars, half-up"""
    return int(float(x) + 0.5)

# ---------------------------------------------------------------- style loaders
def load(path, fields):
    rows = []
    for l in open(path, encoding='utf8'):
        l = l.rstrip('\n')
        if not l: continue
        f = l.split('~'); f += [''] * (len(fields) - len(f))
        rows.append(dict(zip(fields, f)))
    return rows

def cat_ai(r):
    t, ty = r['title'].lower(), r['type']
    if ty == 'Polo': return ('knitwear' if 'knitted' in t else 'tees-polos'), 'Polo'
    if ty == 'Shirting': return ('tees-polos' if 'rugby' in t else 'shirts'), 'Shirting'
    if ty == 'Outerwear':
        if 'chore' in t: return 'outerwear', 'Outerwear'
        return 'outerwear', 'Outerwear'
    return {'Knitwear': 'knitwear', 'Denim': 'denim', 'Tailoring': 'tailoring', 'Trousers': 'trousers'}[ty], ty

def cat_awake(r):
    t, ty = r['title'].lower(), r['type']
    if 'denim' in t: return 'denim', ty or 'derived'
    if ty in ('Tees',) or 'tee' in t or 'jersey' in t: return 'tees-polos', ty or 'derived'
    if 'polo' in t: return 'tees-polos', ty
    if ty == 'Shirt': return 'shirts', ty
    if 'sweatpant' in t or 'hoodie' in t or ty in ('Hoodie', 'Sweatpants'): return 'sweats', ty or 'derived'
    if ty in ('Shorts', 'Bottoms') or 'short' in t or 'jorts' in t: return 'shorts', ty
    if ty == 'Jacket': return 'outerwear', ty
    if ty == 'Knitwear': return 'knitwear', ty
    if ty == 'Pants': return 'trousers', ty
    return 'other', ty or 'derived'

def cat_az(r):
    ty = r['type']
    m = {'skijacket': 'outerwear', 'skipant': 'trousers', 'vest': 'outerwear', 'sweater': 'knitwear', 'fleece': 'other',
         'baselayer': 'other', 'shirt': 'shirts', 'shirt(tee)': 'tees-polos', 'shirt(insulator)': 'outerwear'}
    lab = {'skijacket': 'mens-ski-jackets', 'skipant': 'mens-ski-pants', 'vest': 'vest (tag fa26-m-vest)', 'sweater': 'mens-sweaters', 'fleece': 'mens-technical-fleece',
           'baselayer': 'mens-technical-fleece (next to skin)', 'shirt': 'mens-shirts-and-flannels', 'shirt(tee)': 'mens-shirts-and-flannels', 'shirt(insulator)': 'mens-shirts-and-flannels'}
    return m[ty], lab[ty]

def cat_bb(r):
    ty = r['type']
    m = {"Men's Polo": 'tees-polos', "Men's T-Shirt": 'tees-polos', "Men's Quarterzip": 'sweats', 'Hoodie': 'sweats', "Men's Sweatshirt": 'sweats',
         "Men's Jacket": 'outerwear', "Men's Shorts": 'shorts', "Men's Pants": 'trousers'}
    return m[ty], ty

def cat_berg(r):
    ty = r['type']
    m = {'Outerwear': 'outerwear', 'Tailoring': 'tailoring', 'Knitwear': 'knitwear', 'Trousers': 'trousers', 'Jeans': 'denim', 'Shirts': 'shirts', 'Sweatshirts': 'sweats', 'Jersey': 'tees-polos'}
    return m[ty], ty

def cat_bw(r):
    ty = r['type']
    m = {'Boardshorts': 'underwear-swim', 'T-Shirts': 'tees-polos', 'UV Shirts': 'tees-polos', 'Fleece': 'sweats', 'Jackets': 'outerwear', 'Walk Shorts': 'shorts', 'Pants': 'trousers', 'Sweaters': 'knitwear'}
    return m[ty], ty

def cat_asket(r):
    t, c = r['title'].lower(), r['type']
    if 'jeans' in t: return 'denim', 'Denim'
    if 'short' in t and 'sweat' not in t and 'boxer' not in t: return 'shorts', 'Trousers'
    if 'chino' in t or 'trouser' in t: return 'trousers', 'Trousers'
    if 'merino wool polo' in t: return 'knitwear', 'Knitwear'
    if c == 'knitwear': return 'knitwear', 'Knitwear'
    if c == 't-shirts': return 'tees-polos', 'T-Shirts'
    if c == 'shirts': return 'shirts', 'Shirts'
    if c == 'outerwear': return 'outerwear', 'Outerwear'
    if c == 'sweats': return 'sweats', 'Sweats'
    if c == 'underwear': return 'underwear-swim', 'Underwear'
    return 'other', c

BR = {}
BR['Anglo-Italian'] = dict(dom='https://www.angloitalian.com', rows=load('/home/claude/wc/b1/ai_styles.txt', ['h', 'title', 'type', 'price', 'comp', 'mi', 'n']), cat=cat_ai,
                          code=lambda r: r['h'], url=lambda r: 'https://www.angloitalian.com/products/' + r['h'], method='title_dedup')
BR['Awake NY'] = dict(rows=load('/home/claude/wc/b1/awake_styles.txt', ['h', 'title', 'type', 'price', 'compare', 'comp', 'n']), cat=cat_awake,
                     code=lambda r: r['h'], url=lambda r: 'https://awakenyclothing.com/products/' + r['h'], method='title_dedup')
BR['Aztech Mountain'] = dict(rows=load('/home/claude/wc/b1/aztech_styles.txt', ['h', 'title', 'type', 'price', 'compare', 'comp', 'mi', 'tech']), cat=cat_az,
                            code=lambda r: r['h'], url=lambda r: 'https://aztechmountain.com/products/' + r['h'], method='handle')
BR['Bad Birdie'] = dict(rows=load('/home/claude/wc/b1/bb_styles.txt', ['code', 'h', 'title', 'type', 'lo', 'hi', 'live', 'n', 'comp']), cat=cat_bb,
                       code=lambda r: r['code'], url=lambda r: 'https://badbirdiegolf.com/products/' + r['h'], method='product_code')
BR['Berg & Berg'] = dict(rows=load('/home/claude/wc/b1/berg_styles.txt', ['h', 'title', 'type', 'price', 'comp', 'mi', 'n']), cat=cat_berg,
                        code=lambda r: r['h'], url=lambda r: 'https://bergbergstore.com/products/' + r['h'], method='title_dedup')
BR['Birdwell'] = dict(rows=load('/home/claude/wc/b1/bw_styles.txt', ['code', 'h', 'title', 'type', 'lo', 'hi', 'live', 'n', 'comp', 'mi']), cat=cat_bw,
                     code=lambda r: r['code'], url=lambda r: 'https://www.birdwell.com/products/' + r['h'], method='product_code')
def cat_beams(r):
    ty, t = r['type'], r['title'].lower()
    if 'polo' in t: return 'tees-polos', ty
    m = {'Coats & Jackets': 'outerwear', 'Jackets': 'outerwear', 'T-Shirts': 'tees-polos', 'Tank Tops': 'tees-polos', 'Pants': 'trousers', 'Sweaters': 'knitwear', 'Shirts': 'shirts',
         'Shorts': 'shorts', 'Jeans': 'denim', 'Hoodies': 'sweats', 'Sweatpants': 'sweats', "Men's Undergarments": 'underwear-swim'}
    c = m[ty]
    if ty == 'Shirts' and 'thermal' in t: c = 'tees-polos'
    if ty == 'Pants' and 'denim' in t: c = 'shorts' if 'shorts' in t else 'denim'
    if ty == 'Shirts' and 'long sleeve' in t and 'suvin' in t: c = 'tees-polos'
    return c, ty
BR['Beams'] = dict(rows=load('/home/claude/wc/b1/beamsus_styles.txt', ['code', 'h', 'title', 'type', 'lo', 'hi', 'live', 'n', 'T', 'comp', 'mi']), cat=cat_beams,
                  code=lambda r: r['code'], url=lambda r: 'https://beams-america.com/products/' + r['h'], method='product_code')
BR['Asket'] = dict(rows=load('/home/claude/wc/b1/asket_styles.txt', ['code', 'uri', 'title', 'type', 'price', 'comp', 'mi', 'sup', 'n']), cat=cat_asket,
                  code=lambda r: r['code'], url=lambda r: 'https://www.asket.com/en-us' + r['uri'], method='product_code')

LINES = {'Beams': lambda r: ('BEAMS T' if r.get('T') == 'T' else '"the A" by BEAMS' if r['title'].startswith('the A') else '-'),
         'Birdwell': lambda r: ('SurfNyl' if 'surfnyl' in (r['comp'] + r['title']).lower() and r['type'] in ('Boardshorts', 'Jackets') else
                                'SurfStretch' if 'surfstretch' in (r['comp'] + r['title']).lower() else 'Sunteez' if 'sunteez' in r['title'].lower() else '-'),
         'Aztech Mountain': lambda r: ('Matterhorn' if 'matterhorn' in r['title'].lower() else 'Hayden' if 'hayden' in r['title'].lower() else
                                       'Pyramid' if 'pyramid' in r['title'].lower() else 'Pfeifer' if 'pfeifer' in r['title'].lower() else '-'),
         'Bad Birdie': lambda r: ('Bad Elements' if 'bad elements' in r['h'] or 'vapor' in r['title'].lower() else 'Velocity' if 'velocity' in r['title'].lower() else '-')}

styles_out, agg = [], {}
for b, cfg in BR.items():
    rows = []
    for r in cfg['rows']:
        cat, house = cfg['cat'](r)
        s = style_row(r['comp'])
        comp = r['comp'] if r['comp'] and not r['comp'].startswith('ND') else 'ND'
        notes = [x for x in [s['note']] if x]
        if r.get('n') and r['n'] not in ('', '1'): notes.append(f"{r['n']} colourways/listings collapsed")
        if r['comp'].startswith('ND (') : notes.append(r['comp'][3:].strip('() ') )
        if 'surfnyl' in r['comp'].lower() and s['lead_fibre'] == 'polyamide': notes.append('SurfNyl® filed as nylon (polyamide) per ruling 10 Oct 2026; the site states no fibre')
        if b == 'Beams' and 'polyurethane' in r['comp'].lower(): notes.append('polyurethane as written; Japanese labelling uses polyurethane for spandex')
        line = LINES.get(b, lambda r: '-')(r)
        rows.append(dict(brand=b, style_code=cfg['code'](r), title=r['title'], url=cfg['url'](r), category=cat, category_house=house, lines=line,
                         composition=comp.replace(' (named, no %)', ''), lead_fibre=s['lead_fibre'], lead_pct=s['lead_pct'], elastane_pct=s['elastane_pct'],
                         pure=s['pure'] if comp != 'ND' or s['pure'] != 'undisclosed' else 'undisclosed', single_fibre=s['single_fibre'], note='; '.join(notes) or '-', _s=s))
    styles_out += rows
    # roll-up
    n = len(rows); wc = sum(1 for r in rows if r['_s']['has'])
    cls = Counter(r['_s']['cls'] for r in rows if r['_s']['has'])
    pct = lambda k: int(100 * cls.get(k, 0) / n + 0.5) if n else 'NC'
    cats = defaultdict(lambda: Counter()); catn = Counter()
    for r in rows:
        catn[r['category_house']] += 1
        if r['_s']['has']: cats[r['category_house']][r['_s']['cls']] += 1
    led = {}
    for c, cc in cats.items():
        if not cc: continue
        led[c] = cc.most_common(1)[0][0]
    swimc = {r['category_house'] for r in rows if r['category'] == 'underwear-swim'}
    syn = [c for c in led if led[c] == 'synthetic' and c not in swimc]
    nat = sorted([c for c in led if led[c] == 'natural' and c not in swimc], key=lambda c: -catn[c])
    big_syn = [c for c in syn if catn[c] >= 10]; big_nat = [c for c in nat]
    shape = 'split' if big_syn and big_nat else 'one'
    swim = sum(1 for r in rows if r['category'] == 'underwear-swim' and ('swim' in r['category_house'].lower() or 'board' in r['category_house'].lower()))
    raw = sum(int(r.get('n') or 1) for r in cfg['rows'])
    agg[b] = dict(styles_total=n, styles_with_composition=wc, natural_pct=pct('natural'), synthetic_pct=pct('synthetic'), cellulosic_pct=pct('cellulosic'),
                  spandex_styles=sum(r['_s']['sp'] for r in rows), shape=shape, natural_categories=json.dumps(nat[:3]), synthetic_categories=json.dumps(syn),
                  colourway_ratio=f'{raw}/{n}', style_method=cfg['method'], swim_styles=swim, swim_share_of_range=(int(100 * swim / n + 0.5) if n else 'NC'),
                  mens_styles_excl_swim=n - swim, _cov=wc / n if n else 0)

if __name__ == '__main__':
    for b, a in agg.items():
        print(b, {k: v for k, v in a.items()})
    json.dump({b: {k: v for k, v in a.items()} for b, a in agg.items()}, open('/home/claude/wc/b1/agg.json', 'w'), indent=1)
    cols = ['brand', 'style_code', 'title', 'url', 'category', 'category_house', 'lines', 'composition', 'lead_fibre', 'lead_pct', 'elastane_pct', 'pure', 'single_fibre', 'note']
    with open('/home/claude/wc/b1/return_styles.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, cols, extrasaction='ignore'); w.writeheader(); w.writerows(styles_out)
    print(len(styles_out), 'style rows')
