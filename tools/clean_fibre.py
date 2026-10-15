#!/usr/bin/env python3
"""Clean-fibre share per brand: styles whose every fibre is natural or lyocell (Tencel), elastane at 5% or under.

    python3 tools/clean_fibre.py      writes registers/clean_fibre.csv from every return_styles.csv on file

Ruled 15 Oct 2026: lead fibre does not matter; what matters is that nothing but natural fibres and lyocell is in the
cloth. Tencel Modal is modal, not lyocell, and is out. A style whose composition names a fibre the vocabulary does not
know is not counted either way (listed in registers/clean_fibre_unknown.csv so the vocabulary can grow).
"""
import csv, glob, re, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAT = {'cotton','wool','linen','silk','cashmere','hemp','alpaca','mohair','camel','vicuna','vicuña','yak','merino','ramie','jute','lambswool','lambs wool',
       'merino wool','extra fine merino','extrafine merino','extrafine merino wool','extra-fine merino wool','superfine merino','superfine merino wool','cotone','lana','seta','lino',
       'baumwolle','wolle','seide','leinen','coton','laine','soie','lin','silk noil','angora','cashmere wool','wool cashmere','kid mohair','camel hair','alpaca wool',
       'baby alpaca','linen flax','flax','cotton linen','linen cotton','wool linen','silk cotton','cotton silk','wool silk','silk wool','merino lambswool','shetland wool',
       'yak wool','egyptian cotton','sea island cotton','leather','suede','lambskin','calfskin','cowhide','down','feather','feathers','goose down','duck down',
       'cotton single jersey','cotton for lightweight comfort','co','wo','li','se','ws','cotton and','pima','supima','organic'}
LYO = {'lyocell','tencel','tencel lyocell','lyocell tencel','lenzing lyocell','refibra','lyocell (tencel)','tencel (lyocell)','tencel lyocell fibres','tencel lyocell fibers','lyocell (tencel )'}
EL = {'elastane','spandex','lycra','ecomade lycra','elasthanne','elastan','elastomultiester','elastane (lycra)','polyurethane elastane','elastane lycra','roica elastane','ea','el'}
STRIP = r'^(recycled|organic|certified|rws|gots|responsible|bci|better cotton|regenerative|mulberry|washed|brushed|mercerized|pima|supima|virgin|italian|japanese|peruvian|mongolian|scottish|french|belgian|long staple|long-staple|extra long staple|premium|heavyweight|lightweight|fine|soft|pure|100)\s+'


def parse(c):
    out = []
    for p, n in re.findall(r'(\d{1,3}(?:[.,]\d)?)\s*%\s*([A-Za-z™®()\-\s/é]+?)(?=[,;/]|\d{1,3}\s*%|$)', c):
        n = n.strip().lower().replace('™', '').replace('®', '').strip(' .-'); n = re.sub(r'\s+', ' ', n)
        for _ in range(3): n = re.sub(STRIP, '', n)
        n = re.sub(r'\s*\((?:organic|recycled|us pdp|lightweight|rws)\)$', '', n).strip()
        out.append((float(p.replace(',', '.')), n))
    return out


def main():
    seen = set(); per = collections.defaultdict(lambda: collections.Counter()); unknown = collections.Counter()
    files = glob.glob(os.path.join(ROOT, 'jobs/returns/*/batch*/return_styles.csv')) + glob.glob(os.path.join(ROOT, 'jobs/returns/*/return_styles.csv'))
    for f in files:
        for r in csv.DictReader(open(f, encoding='utf8')):
            c = r.get('composition', '')
            if not c or c.upper() in ('NC', 'ND'): continue
            key = (r['brand'], r.get('url') or r.get('title'))
            if key in seen: continue
            seen.add(key); parts = parse(c)
            if not parts: continue
            s = sum(p for p, _ in parts)
            if s < 95 or s > 105: continue
            other = [n for p, n in parts if n not in NAT and n not in LYO and n not in EL]
            syn_known = any(n in ('polyester', 'nylon', 'polyamide', 'viscose', 'rayon', 'acrylic', 'polyurethane', 'modal', 'cupro', 'acetate', 'polypropylene', 'modacrylic', 'pes (polyester)', 'poly', 'tencel modal', 'lenzing tencel modal', 'elastolefin', 'triacetate', 'pu', 'pa', 'pl', 'cv') for n in other)
            if other and not syn_known:
                for n in other: unknown[n] += 1
                continue  # unknown fibre: not counted either way
            per[r['brand']]['w'] += 1
            el = sum(p for p, n in parts if n in EL)
            if not other and el <= 5:
                per[r['brand']]['clean'] += 1
                if any(n in LYO for p, n in parts): per[r['brand']]['lyo'] += 1
    os.makedirs(os.path.join(ROOT, 'registers'), exist_ok=True)
    with open(os.path.join(ROOT, 'registers/clean_fibre.csv'), 'w', newline='', encoding='utf8') as f:
        w = csv.writer(f); w.writerow(['brand', 'styles_judged', 'clean_styles', 'clean_pct', 'clean_with_lyocell'])
        for b, c in sorted(per.items()):
            w.writerow([b, c['w'], c['clean'], round(100 * c['clean'] / c['w']) if c['w'] else '', c['lyo']])
    with open(os.path.join(ROOT, 'registers/clean_fibre_unknown.csv'), 'w', newline='', encoding='utf8') as f:
        w = csv.writer(f); w.writerow(['fibre_name_as_read', 'styles']); [w.writerow([n, k]) for n, k in unknown.most_common()]
    tot = sum(c['w'] for c in per.values()); cl = sum(c['clean'] for c in per.values())
    print(f"{len(per)} brands, {tot} styles judged, {cl} clean ({100*cl//tot}%), {sum(c['lyo'] for c in per.values())} with lyocell; {sum(unknown.values())} styles on {len(unknown)} unknown fibre names")


if __name__ == '__main__':
    main()
