#!/usr/bin/env python3
"""WS centers x CAKE x Croissant: a three-way comparison page (app/sub/ws-cake-croissant.html).

WS tenants come from the ws_centers_2026-10-22 returns (each center's own directory). Retail brands only:
restaurants, services, fitness, banks, offices and the like are left out by category and by name. CAKE and
Croissant lists come from the CAKE-and-Croissant companion page. Names are matched folded (case, accents,
punctuation, "&"/"and", a leading "The"), with the aliases below.
"""
import csv, glob, json, os, re, unicodedata, collections, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUB = os.path.join(ROOT, 'app/sub')

NOT_RETAIL = re.compile(r"\b(bank|chase|capital one|salon|spa|nail|tan|fitness|yoga|pilates|barre|stretch ?lab|solidcore|barry|cycle|physical therapy|"
                        r"dentist|dental|healthcare|medical|med spa|aesthetic|realty|sotheby|elliman|brown harris|post office|postal|management office|"
                        r"playground|library|industrious|t-mobile|cvs|shoprite|supermarket|wine|spirits|tobacco|great clips|massage|blow dry|"
                        r"hair|club pilates|residences|ritz-carlton|palihouse|tuxedo|tailoring|kitchen|cafe|café|bar\b|coffee|juice|pizza|bakery|"
                        r"grill|flatbread|shake shack|sweetgreen|chipotle|panera|ramen|mendocino|cupcake|ben and jerry|counter|superfoods|"
                        r"olives|wonder\b|hippo|mandarin|mercato|jacob|oliva|acquavella|galleries|toys|kids|tots|dogs|woof|grooming|optical|opticians|"
                        r"site for sore eyes|tempur|shade store|apple barrel|ross dress|kohl|dick|old navy|apple\b|golf lounge|top shelf|"
                        r"atria|alley, maass|design studio|public studio|made local|marketplace|floral|candle pour|pottery place|color me mine|"
                        r"paul labrecque|francis conroy|visage|élan|sweat spot|justfoodfordogs|angel tips|face foundri|"
                        r"hospital|swim school|vet\\b|fifth third|schwab|boot camp|club studio|escape|at&t|verizon|walgreens|whole foods|"
                        r"trader joe|star market|greenacres|office depot|rivian|urban air|sport clips|smile doctors|laser|skin laundry|skinmd|"
                        r"skinkind|skinlab|skin & body|wax|drybar|miniluxe|glowbar|heyday|the tox|restore hyper|next health|madison reed|"
                        r"lucid studio|seaport brand|one seaport|summer market|snowport|the green|the point|summer street steps|sirocco|showcase|"
                        r"restaurant|apizza|chocolates|it.sugar|lahey|ob-gyn|clevens|pure glow|wellness|levitate|nourish|glow & grow|mane & mani|"
                        r"sachetta|pet supplies|natural pet|sample sale|hallmark|lenscrafters|sunglass hut|trudy)", re.I)
ALIAS = {'aliceandoliviabystaceybendet': 'aliceandolivia', 'beachbyeverythingbutwater': 'beach', 'theloft': 'loft', 'jjill': 'jjill',
         'josabankclothiers': 'josabank', 'williamssonoma': 'williamssonoma', 'seany': 'sea', 'katespade': 'katespadenewyork',
         'greysonclothiers': 'greyson', 'lushhandmadecosmetics': 'lushcosmetics', 'sleepnumberbyselectcomfort': 'sleepnumber', 'somaintimates': 'soma', 'crewcutsbyjcrew': 'crewcuts', 'stretchlab': 'stretchlab'}


def fold(x):
    x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode().lower().replace('&', 'and').replace('+', 'and')
    x = re.sub(r'^the ', '', x.strip())
    x = re.sub(r'[^a-z0-9]', '', x)
    return ALIAS.get(x, x)


def main():
    s = open(os.path.join(SUB, 'cake-croissant.html'), encoding='utf8').read()
    grab = lambda v: json.loads(re.search(r'var %s=(\[.*?\]);' % v, s).group(1))
    both, cake, croi, retail = grab('both'), grab('cake'), grab('croi'), set(grab('retail'))
    links = json.loads(re.search(r'var LINKS=(\{.*?\});\n', s).group(1))
    names, sets, centers = {}, collections.defaultdict(set), collections.defaultdict(set)
    def add(n, k):
        f = fold(n); names.setdefault(f, n); sets[f].add(k); return f
    for n in cake + both: add(n, 'C')
    for n in croi + both: add(n, 'R')
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'jobs/returns/ws_centers_2026-10-22/return_tenants*.csv'))):
        rows += list(csv.DictReader(open(f, encoding='utf8')))
    drops = {fold(r['tenant']) for r in csv.DictReader(open(os.path.join(ROOT, 'registers/ws_tenant_drops_2026-10-22.csv'), encoding='utf8'))}
    cats = collections.Counter()
    for t in rows:
        c = t['category_on_site'].lower(); n = t['tenant_name'].strip()
        if not (any(k in c for k in ('fashion', 'specialty', 'beauty', 'home', 'shopping')) or c == 'nd'): continue
        if NOT_RETAIL.search(n) or fold(n) in drops: continue  # drops: stores, local boutiques, non-brands (ruled 22 Oct)
        f = add(n, 'W'); centers[f].add(t['center'] + (' (coming soon)' if t['status'] == 'coming_soon' else ''))
    ctrs = sorted({t['center'] for t in rows})
    data = [{'n': names[f], 'w': 'W' in v, 'c': 'C' in v, 'r': 'R' in v, 'x': sorted(centers.get(f, [])), 'rt': names[f] in retail,
             'ig': (links.get(names[f]) or {}).get('ig', ''), 'tt': (links.get(names[f]) or {}).get('tt', '')} for f, v in sets.items()]
    data.sort(key=lambda d: d['n'].lower())
    tpl = open(os.path.join(SUB, 'ws-cake-croissant.tpl.html'), encoding='utf8').read()
    html = tpl.replace('/*DATA*/', 'var D=' + json.dumps(data, ensure_ascii=False) + ';var CENTERS=' + json.dumps(ctrs) + ';')
    open(os.path.join(SUB, 'ws-cake-croissant.html'), 'w', encoding='utf8').write(html)
    reg = collections.Counter(('W' if d['w'] else '') + ('C' if d['c'] else '') + ('R' if d['r'] else '') for d in data)
    print(len(data), 'brands;', dict(reg), ';', len(ctrs), 'centers:', ', '.join(ctrs))


if __name__ == '__main__':
    main()
