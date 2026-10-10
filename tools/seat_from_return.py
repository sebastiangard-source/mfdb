#!/usr/bin/env python3
"""Seat brands from a seating-evidence return (the seat_resort / seat_wave record).

    python3 tools/seat_from_return.py <return_dir> <authored.py> <job_id> [--brands a,b,c]

<return_dir> holds return.csv (132 columns), return_styles.csv, own_doors.csv and either
return_counts.csv or held_door_counts.csv. <authored.py> defines a dict A keyed by brand name
with the Spectrum thread's authored dials (band override, comfort, style, fabric, dur, forg,
forgc, fuss, golffice, reg, whitet, logo, western, rock, workwear, outdoor, surf, why, chan,
say, shoes). Tech and craft are seated at the thread's proposals, pending ruling.

Writes data/brands/<slug>.json for each brand in A that has a return row, appends own-door
rows to data/places.json (src = job_id) and remaps region.o for every brand. Bands follow
the price rule unless A overrides: tee at or under $35 and dress shirt under $80 (tee alone
where there is no dress shirt, provided another clothing slot is priced) = basic; else the mean of dress-shirt and sweater entry:
under $150 premium, $150–400 accessible, over $400 trueLux; a shoe-only house by its shoe
entry on the same cuts. Run lint after.
"""
import csv, json, sys, os, re, glob, collections, importlib.util, unicodedata
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from spec import slug  # noqa: E402

NE = {'MA', 'CT', 'ME', 'NH', 'NJ', 'NY', 'PA', 'RI', 'VT', 'DE'}
G = ['tee', 'polo', 'dress_shirt', 'jeans', 'dress_pants', 'sweater', 'outerwear', 'shoes']
GN = ['T-shirt', 'Polo', 'Dress shirt', 'Jeans', 'Dress pants', 'Sweater', 'Outerwear', 'Shoes']
NAT = {'cotton', 'wool', 'leather', 'linen', 'cashmere', 'silk', 'alpaca', 'mohair', 'other-natural',
       'hemp', 'suede', 'down', 'yak', 'camel', 'shearling'}
SYN = {'polyester', 'polyamide', 'polyurethane', 'acrylic', 'elastane', 'polypropylene', 'nylon',
       'other-synthetic', 'modacrylic', 'aramid'}
CEL = {'viscose', 'lyocell', 'modal', 'triacetate', 'other-cellulosic', 'rayon', 'cupro', 'acetate'}
CHAN = {'O': None, 'D': 'department stores', 'I': 'independent shops', 'W': 'its own site', 'X': None}


def nc(v):
    return v is None or str(v).strip() in ('', 'NC', 'NONE', 'none', '-')


def num(v):
    try:
        return int(round(float(str(v).replace(',', '').replace('$', ''))))
    except Exception:
        return None


def jl(v):
    try:
        x = json.loads(v)
        return x if isinstance(x, list) else []
    except Exception:
        return [s.strip() for s in re.split(r'[;|]', v) if s.strip()] if not nc(v) else []


def join_and(xs):
    xs = [x for x in xs if x]
    if not xs:
        return ''
    if len(xs) == 1:
        return xs[0]
    return ', '.join(xs[:-1]) + ', and ' + xs[-1]


def band_by_rule(prices):
    def lo(i):
        p = prices[i]
        return p[0] if isinstance(p, list) else None
    tee, shirt, sw, shoes = lo(0), lo(2), lo(5), lo(7)
    clothing = any(lo(i) is not None for i in (1, 3, 4, 5, 6))  # a tee alone beside shoes is a shoe house
    if tee is not None and tee <= 35 and (shirt is None or shirt < 80) and (shirt is not None or clothing):
        return 'basic', f'tee ${tee}, dress shirt {"$"+str(shirt) if shirt else "no slot"}'
    pts = [x for x in (shirt, sw) if x is not None]
    if not pts and shoes is not None:
        pts = [shoes]
        why = f'shoe house: shoe entry ${shoes}'
    else:
        why = f'dress shirt {"$"+str(shirt) if shirt else "none"}, sweater {"$"+str(sw) if sw else "none"}'
    if not pts:
        return 'premium', 'no priced staple; premium by default, flagged'
    m = sum(pts) / len(pts)
    return ('premium' if m < 150 else 'accessible' if m <= 400 else 'trueLux'), why


def main():
    args = sys.argv[1:]
    only = None
    if '--brands' in args:
        i = args.index('--brands'); only = set(args[i + 1].split(',')); del args[i:i + 2]
    rdir, authored, job = args[0], args[1], args[2]
    spec_ = importlib.util.spec_from_file_location('authored', authored)
    mod = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(mod)
    A = mod.A
    today = date.today().isoformat()

    R = {r['brand']: r for r in csv.DictReader(open(os.path.join(rdir, 'return.csv')))}
    S = collections.defaultdict(list)
    for s in csv.DictReader(open(os.path.join(rdir, 'return_styles.csv'))):
        S[s['brand']].append(s)
    D = collections.defaultdict(list)
    for d in csv.DictReader(open(os.path.join(rdir, 'own_doors.csv'))):
        D[d['brand']].append(d)
    C = {}
    for fn in ('held_door_counts.csv', 'return_counts.csv'):
        p = os.path.join(rdir, fn)
        if os.path.exists(p):
            for c in csv.DictReader(open(p)):
                C[c['brand']] = c

    places = json.load(open(os.path.join(ROOT, 'data/places.json')))
    zips = json.load(open(os.path.join(ROOT, 'registers/nyc_neighbourhoods.json')))['zips']
    existing = {json.load(open(f))['name'] for f in glob.glob(os.path.join(ROOT, 'data/brands/*.json'))}
    seat = max(json.load(open(f))['seat'] for f in glob.glob(os.path.join(ROOT, 'data/brands/*.json')))
    report = []

    for name, a in A.items():
        if only and name not in only:
            continue
        if name not in R:
            print('no return row:', name); continue
        if name in existing:
            print('already seated:', name); continue
        r = R[name]
        seat += 1
        # ---- prices
        prices, ev, links, ronly = [], {}, {}, []
        for g, gn in zip(G, GN):
            lo, hi, b = r[g + '_low'], r[g + '_high'], r[g + '_basis']
            if lo == 'NONE' or b == 'NONE':
                prices.append(None)
            elif lo == 'np':
                prices.append('np')
            elif nc(lo) or num(lo) is None:
                prices.append('?')
            else:
                prices.append([num(lo), num(hi) if num(hi) is not None else num(lo)])
                ev[gn] = {'lp': r[g + '_low_product'], 'lu': r[g + '_low_url'], 'hp': r[g + '_high_product'],
                          'hu': r[g + '_high_url'], 'b': b}
                if b == 'range':
                    ronly.append(gn)
            if not nc(r[g + '_mens_listing_url']):
                links[gn] = r[g + '_mens_listing_url']
        band, bwhy = band_by_rule(prices)
        override = a.get('band')
        if override and override != band:
            bwhy += f'; rule said {band}, seated {override} by hand'
            band = override
        # ---- fibre
        rows = S.get(name, [])
        fibre = None
        if rows:
            def cls(s):
                p, lf = s['pure'], s['lead_fibre']
                if p == 'natural': return 'n'
                if p == 'synthetic': return 's'
                if p == 'cellulosic': return 'c'
                if p == 'blend':
                    return 'n' if lf in NAT else 's' if lf in SYN else 'c' if lf in CEL else None
                return None
            cnt = collections.Counter(cls(s) for s in rows)
            w = cnt['n'] + cnt['s'] + cnt['c']
            tot = r['styles_total']
            t = int(tot) if tot.isdigit() and int(tot) >= len(rows) else len(rows)
            el = [s for s in rows if s['elastane_pct'].isdigit()]
            fibre = {'t': t, 'w': w, 'n': round(100 * cnt['n'] / t), 's': round(100 * cnt['s'] / t),
                     'c': round(100 * cnt['c'] / t),
                     'x': round(100 * sum(1 for s in el if int(s['elastane_pct']) > 0) / t),
                     'xh': round(100 * sum(1 for s in el if int(s['elastane_pct']) >= 5) / t),
                     'sp': r['shape'] if r['shape'] in ('one', 'split') else 'one',
                     'sc': jl(r['synthetic_categories']), 'nc': jl(r['natural_categories']),
                     'st': 'complete' if (tot.isdigit() and w / t >= 0.8) else 'partial'}
            rec = fibre['n'] + fibre['s'] + fibre['c'] + (100 - round(100 * w / t))
            if not 99 <= rec <= 101:
                k = max(('n', 's', 'c'), key=lambda q: fibre[q]); fibre[k] += 100 - rec
        # ---- doors
        c = C.get(name, {})
        n_claim = num(c.get('us_own_doors', r['own_doors_us']))
        out = num(c.get('us_outlets', '0')) or 0
        con = num(c.get('us_concessions', '0')) or 0
        drows = [d for d in D.get(name, []) if d['format'] == 'own-door' and d['country'] in ('US', 'USA')
                 and d['status'].lower() not in ('closed', 'held', 'opening', 'coming-soon', 'temporarily closed')]
        new_places = []
        for d in drows:
            pl = {'n': name, 'a': '' if nc(d['street']) else d['street'], 'c': d['city'], 's': d['state'],
                  'z': d['zip'][:5] if d['zip'].strip() and d['zip'][:5].isdigit() else '', 'k': 'o', 'src': job}
            if not nc(d.get('venue')):
                pl['v2'] = d['venue']
            if pl['s'] == 'NY' and pl['c'] in ('New York', 'Brooklyn') and pl['z'] in zips:
                pl['h'] = zips[pl['z']]
            new_places.append(pl)
        cc = collections.Counter((p['c'], p['s']) for p in new_places)
        cities = [[k[0], k[1], v] for k, v in sorted(cc.items(), key=lambda kv: (-kv[1], kv[0]))]
        basis = f'{job} {r["read_date"]}'
        if new_places:
            doors = {'c': 'full', 'n': len(new_places), 'cities': cities, 'basis': basis, 'out': out, 'con': con}
            if n_claim is not None and n_claim != len(new_places):
                doors['basis'] += f' (rows {len(new_places)}; count filed {n_claim})'
        elif n_claim:
            doors = {'c': 'count', 'n': n_claim, 'basis': basis + ' (count from the return; no rows)', 'out': out, 'con': con}
        else:
            doors = {'c': 'full', 'n': 0, 'cities': [], 'basis': f'positive zero {today} ({job})', 'out': out, 'con': con}
        places.extend(new_places)
        # ---- cities line
        chan = a.get('chan', ['W'])
        tail = join_and([CHAN[x] for x in chan if CHAN.get(x)])
        if doors['c'] == 'count':
            head = f'{doors["n"]} stores across the US (count only; addresses to come)'
        elif doors['n'] == 0:
            head = 'No store of its own in the US'
        elif doors['n'] == 1:
            head = f'One store, in {cities[0][0]}'
        else:
            head = f'{doors["n"]} stores across the US, including ' + ', '.join(x[0] for x in cities[:3])
        cities_line = f'{head} · {tail}' if tail else head
        # ---- evidence blocks
        tol = r['tech_owned_or_licensed'].lower()
        origin_t = ('none' if nc(r['tech_owned_or_licensed']) else 'both' if ('owned' in tol or 'house' in tol) and 'licens' in tol
                    else 'licensed' if 'licens' in tol or 'third' in tol else 'house' if 'owned' in tol or 'house' in tol else 'unclear')
        marks = [] if nc(r['tech_named_fabrics']) else jl(r['tech_named_fabrics'])
        tech_ev = {'names': 'no' if not marks else 'yes', 'origin': origin_t, 'marks': marks, 'source': job, 'checked': r['read_date']}
        craft_ev = {'owned': r['owned_facility'], 'makers': r['named_makers'], 'mills': r['named_mills'],
                    'madein': r['made_in_stated_share'], 'heritage': r['heritage_claim'], 'process': r['process_documented'],
                    'urls': [u for u in (r['craft_url_1'], r['craft_url_2']) if not nc(u)],
                    'proposed': num(r['proposed_craft']), 'reasoning': r['craft_reasoning'], 'source': job}
        tech, craft = num(r['proposed_tech']) or 1, num(r['proposed_craft']) or 1
        founders = ' and '.join(x.strip() for x in r['founders'].split(';')) if not nc(r['founders']) else ''
        origin = f'Founded in {r["founded_year"]}' if not nc(r['founded_year']) else 'Founded'
        if not nc(r['founded_place']) and not r['founded_place'].startswith('NC'):
            origin += f' in {r["founded_place"]}'
        if founders:
            origin += f' by {founders}'
        origin += '.'
        opview = None
        if not nc(r['quote']):
            q = r['quote'].strip().strip('"“”')
            opview = f'“{q}” — {r["quote_who"]}, {r["quote_source"]}'
        if nc(r['signature_product']):
            onething = {'p': None, 'u': None, 'n': f'no signature product named in the {job} return'}
        else:
            onething = {'p': r['signature_product'], 'u': None if nc(r['signature_product_url']) else r['signature_product_url'],
                        'n': f'from the {job} return; "{r["signature_product"]}"'}
        resale = {}
        if not nc(r['vinted_mens_url']):
            resale['vinted'] = {'u': r['vinted_mens_url'], 'm': 'brand filter', 'n': ''}
        if not nc(r['grailed_url']):
            resale['grailed'] = {'u': r['grailed_url']}
        season = None
        if r['lookbook_found'].lower().startswith('yes') and not nc(r['lookbook_url']) and not r['lookbook_mens'].lower().startswith('no'):
            season = {'l': r['lookbook_season_label'], 't': 'lookbook', 'u': r['lookbook_url'],
                      'm': 'yes' if r['lookbook_mens'].lower().startswith('yes') else 'unisex'}
        certs = {}
        if r['b_corp'].lower().startswith('yes'):
            certs['bcorp'] = {'e': r['b_corp_entity']}
        if r['gots_certified'].lower().startswith('yes'):
            certs['gots'] = {'e': r['gots_entity'], 'n': ''}
        # ---- notes
        notes = {'tech': f'Thread proposed {tech} ({r["read_date"]}): {"; ".join(marks[:8])} — {r["tech_owned_or_licensed"]}; share of range {r["tech_share_of_range"][:80]}. Seated as proposed, pending ruling.',
                 'craft': f'Thread proposed {craft} ({r["read_date"]}): {r["craft_reasoning"][:400]} Seated as proposed, pending ruling.'}
        prov = f'seeded {today} from the {job} return; provisional'
        dials = {'dur': a['dur'], 'forg': a['forg'], 'fuss': a['fuss'], 'golffice': a['golffice'],
                 'whitet': a['whitet'], 'logo': a['logo'], 'western': a['western'], 'rock': a['rock'],
                 'workwear': a['workwear'], 'outdoor': a['outdoor'], 'surf': a['surf']}
        dials.update(a.get('reg', {}))
        if 'shoes' in a:
            dials['shoes'] = a['shoes']
        for k in ('comfort', 'style', 'dur', 'forg', 'fuss', 'golffice', 'whitet', 'logo', 'western', 'rock',
                  'workwear', 'outdoor', 'surf', 'denim', 'cashmere', 'linen', 'cotton', 'wool', 'synth'):
            notes[k] = prov
        for k in a.get('reg', {}):
            notes[k] = prov
        if 'shoes' in a:
            notes['shoes'] = prov
        rec = collections.OrderedDict()
        rec['name'] = name; rec['band'] = band; rec['seat'] = seat; rec['dagger'] = 0
        rec['focus'] = {'tech': tech, 'comfort': a['comfort'], 'craft': craft, 'style': a['style']}
        rec['fabric'] = a['fabric']; rec['dials'] = dials
        rec['why'] = a['why']; rec['origin'] = origin; rec['chan'] = chan; rec['conf'] = a.get('conf', 'S')
        rec['forgc'] = a['forgc']; rec['onething'] = onething; rec['prices'] = prices
        if '?' not in prices:
            rec['price_checked'] = True
        if ronly:
            rec['price_range_only'] = ronly
        rec['price_evidence'] = ev; rec['garment_links'] = links
        rec['price_read'] = {'date': r['read_date'], 'store': r['store_used'], 'currency': r['currency'],
                             'status': r['status'], 'sublines': r['sublines_included'] or '-'}
        rec['notes'] = notes; rec['doors'] = doors; rec['cities'] = cities_line
        rec['site'] = {'domain': r['site_domain'], 'platform': 'other', 'feed': 'none', 'feed_count': 0,
                       'status': 'live_store' if not nc(r['store_used']) else 'no_us_store', 'checked': r['read_date']}
        rec['tech_evidence'] = tech_ev; rec['craft_evidence'] = craft_ev
        rec['ownership'] = {'owner': r['owner_today'], 'u': None if nc(r['ownership_url']) else r['ownership_url']}
        if opview:
            rec['opview'] = opview
        if resale:
            rec['resale'] = resale
        if season:
            rec['season'] = season
        if certs:
            rec['certs'] = certs
        if a.get('say'):
            rec['say'] = a['say']
        if fibre:
            rec['fibre'] = fibre
        rec['band_note'] = f'{band} by the price rule ({bwhy})'
        fn = os.path.join(ROOT, 'data/brands', slug(name) + '.json')
        open(fn, 'w').write(json.dumps(rec, ensure_ascii=False, indent=1))
        report.append((seat, name, band, bwhy, doors['c'], doors['n'], out, con, fibre and fibre['st']))

    json.dump(places, open(os.path.join(ROOT, 'data/places.json'), 'w'), ensure_ascii=False, indent=1)
    # remap region.o for every brand
    byname = collections.defaultdict(list)
    for i, x in enumerate(places):
        if x.get('k') == 'o' and x.get('s') in NE:
            byname[x['n']].append(i)
    for f in glob.glob(os.path.join(ROOT, 'data/brands/*.json')):
        d = json.load(open(f), object_pairs_hook=collections.OrderedDict)
        want = byname.get(d['name'], []); reg = d.get('region') or {}
        if sorted(reg.get('o', [])) != want:
            if want: reg['o'] = want; reg.setdefault('s', [])
            else: reg.pop('o', None)
            if reg: d['region'] = reg
            else: d.pop('region', None)
            open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=1))
    for row in report:
        print(f'{row[0]:3} {row[1]:20} {row[2]:10} doors={row[4]}:{row[5]} out={row[6]} con={row[7]} fibre={row[8]}  [{row[3]}]')


if __name__ == '__main__':
    main()
