#!/usr/bin/env python3
"""Build the women's Spectrum — a locations-first map with price bands and no dials.

    python3 tools/womens_records.py      first: writes data/brands_womens/*.json (the men's record shape)
    python3 tools/build_womens.py        writes dist/womens_spectrum.html

One record shape, two folders: data/brands_womens/ (women's-only brands) and data/brands/ (the men's map, read for
the crossovers — men's-map brands in the women's universe). Stores: registers/own_doors_womens_2026-10-10.csv for
the women's records, data/places.json for the men's.
"""
import csv, json, os, re, sys, glob, collections, unicodedata, datetime

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


CF = {}
_cff = os.path.join(ROOT, 'registers/clean_fibre.csv')
if os.path.exists(_cff):
    CF = {r['brand']: r for r in csv.DictReader(open(_cff, encoding='utf8'))}


def clean_of(b):
    """Natural-or-lyocell band on the share of judged styles whose every fibre is natural or lyocell (elastane ≤ 5%); men's cuts."""
    if not b.get('fabric'):
        return None
    f = b.get('fibre') or {}
    share, n = f.get('clean_pct'), f.get('clean_n')
    if share is None:
        r = CF.get(b['name'])
        if r and num(r['styles_judged']) and num(r['styles_judged']) >= 20:
            share, n = num(r['clean_pct']), num(r['styles_judged'])
    if share is None:
        return None
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



# ---- reader-facing wording (copy review, 16 Oct 2026): the panel shows evidence, not how we worked ----
FIB = {'cotton': 'cotton', 'cashmere': 'cashmere', 'linen': 'linen', 'silk': 'silk', 'a synthetic': 'synthetic',
       'wool (alpaca, mohair and camel counted with it)': 'wool (alpaca, mohair and camel included)', 'wool': 'wool'}


def tidy_note(v):
    v = (v or '').strip()
    if not v or 'NC; share of range NC' in v or re.match(r'(?i)^(NC\b|seeded|authored|\[authored|rescored|no fabric dials|shoe house;|sells a tee as a basic|a named tee in the range)', v):
        return ''
    v = re.sub(r'\s*—\s*seeded .*$', '', v)
    m = re.match(r'^(\d+)% of (?:\d+ )?(?:the )?sampled styles with a composition are (?:led by (.+?)|in denim \(the jeans category or denim cloth\));', v)
    if m:
        pct, f = m.group(1), m.group(2)
        what = 'denim' if f is None else 'mostly ' + FIB.get(f, f)
        return f'None of the styles checked are {what}.' if pct == '0' else f'{pct}% of styles checked are {what}.'
    v = re.sub(r'^Thread proposed \d \([^)]*\):\s*', '', v)
    v = re.sub(r'\s*Seated as proposed, pending ruling\.?\s*$', '', v)
    if re.match(r'^(\[\]\s*)?—\s*NONE; share of range 0%?\.?$', v.strip()) or v.strip().startswith('— NONE'):
        return 'No named performance fabric.'
    v = re.sub(r'^no named technical fabric on the site\.?$', 'No named performance fabric.', v)
    v = re.sub(r'^named fabrics NONE\b\s*', 'No named performance fabric ', v)
    v = re.sub(r'^named fabrics\s+', 'Named fabrics: ', v)
    v = re.sub(r'^\[(.*?)\]\s*—\s*owned; share of range (\d+)%\.?$', lambda m: 'Its own fabrics (' + ', '.join(x.strip().strip('"') for x in m.group(1).split(',')) + f') on {m.group(2)}% of the range.', v)
    v = v.replace(' — ', ': ').replace('—', ', ')
    v = re.sub(r'\bfibre', 'fiber', v)
    # Scoring talk is ours, not the reader's. Drop the clauses and sentences that argue the number.
    v = re.sub(r'\s*\[[^\]]*\]', '', v)
    v = re.sub(r",? so (?:it(?:'|’)s|this is|it sits at) (?:a )?\d\b", '', v)
    SCORE = re.compile(r"(?i)\bis a \d\b|\b(?:a|an) \d\b|^\d\b|\b\d (?:on|if|until)\b|pending|\bruled\b|held at|proposed|rubric|\brule\b|not read|read rendered|\bscor|lifts it|would need")
    sents = [x for x in re.split(r'(?<=[.!?])\s+', v) if x and not SCORE.search(x)]
    return ' '.join(sents).strip()


def tidy_basis(v):
    v = (v or '').strip(); hand = 'hand-' in v
    v = re.sub(r'\s*\((?:women.s price pass|the men.s map)[^)]*\)', '', v)
    m = re.match(r'^men.s dress-shirt and sweater entry, mean \$(\d+)', v)
    if m: return f'Men’s shirt and sweater start at ${m.group(1)} on average.'
    m = re.match(r'^mean of blouse and sweater entry \$(\d+)', v)
    if m: return f'Blouse and sweater start at ${m.group(1)} on average.' + (' Placed by hand.' if hand else '')
    m = re.match(r'^mean of blouse entry \$(\d+)', v)
    if m: return f'Blouse starts at ${m.group(1)}.' + (' Placed by hand.' if hand else '')
    m = re.match(r'^mean of sweater entry \$(\d+)', v)
    if m: return f'Sweater starts at ${m.group(1)}.' + (' Placed by hand.' if hand else '')
    m = re.match(r'^core tee \$(\d+) and core blouse \$(\d+)', v)
    if m: return f'Basic tee ${m.group(1)}, blouse ${m.group(2)}.'
    m = re.match(r'^core tee \$(\d+) with no woven blouse', v)
    if m: return f'Basic tee ${m.group(1)}; no blouse sold.'
    m = re.match(r'^shoe house, banded on shoe entry \$(\d+)', v)
    if m: return f'Shoes start at ${m.group(1)}.'
    if v.startswith('banded on its men'): return 'Placed on its men’s prices.'
    v = re.sub(r'(?i)\s*\((?:thread proposal|thread re-read)\)', '', v)
    v = re.sub(r'(?i)^(?:provisional, )?for ruling(?:, \d+ Oct)?:\s*|^ruled \d+ Oct:\s*|^core-garment rule, \d+ Oct:\s*|^everyday selling price is the price, \d+ Oct:\s*', '', v)
    v = re.sub(r'(?i)^price read blocked \(complete\);\s*', '', v)
    v = re.sub(r'(?i)^no priced staple;\s*', 'No staple garment priced. ', v)
    v = re.sub(r'(?i);?\s*hand-band\w*', '. Placed by hand', v)
    v = re.sub(r'(?i)Exact figures are whole dollars\.\s*', '', v)
    v = re.sub(r'\bseated on\b', 'placed on', v)
    v = v.replace(' — ', ': ').strip()
    return (v[:1].upper() + v[1:]).rstrip('.') + '.' if v else v


def tidy_fi(v):
    m = re.search(r'of (\d+) (?:read with a composition|stating a composition), (\d+)% natural-led, (\d+)% synthetic, (\d+)% cellulosic(?: \(lyocell (\d+)%)?', v or '')
    if not m: return (v or '').replace('fibre', 'fiber')
    n, nat, syn, cel, ly = m.groups()
    out = f'Of {n} styles checked, {nat}% are mostly natural fibers, {syn}% synthetic and {cel}% rayon-type fibers'
    return out + (f' ({ly}% lyocell).' if ly and ly != '0' else '.')

def main():
    womens = [json.load(open(f, encoding='utf8')) for f in sorted(glob.glob(os.path.join(ROOT, 'data/brands_womens/*.json')))]
    men = {k(b['name']): b for b in (json.load(open(f, encoding='utf8')) for f in glob.glob(os.path.join(ROOT, 'data/brands/*.json')))}
    universe = {k(r['brand']) for r in csv.DictReader(open(os.path.join(ROOT, 'registers/womens_universe_counted_2026-10-10.csv'), encoding='utf8'))}
    # Crossover Part A (15 Oct 2026): men's-map brands whose own US site sells a women's clothing range join as crossovers.
    # Only `yes` joins; `partial` and `NC` wait for a ruling.
    xa = os.path.join(ROOT, 'jobs/returns/womens_crossover_a_2026-10-15/return_a.csv')
    if os.path.exists(xa):
        universe |= {k(r['brand']) for r in csv.DictReader(open(xa, encoding='utf8')) if r['womens_clothing'].strip() == 'yes'}
    # Follow-up of 15 Oct: re-reads of brands Part A left open. Dover Street Market counts as a Comme des Garçons door
    # (ruled 15 Oct 2026), so CDG's DSM evidence makes it a crossover.
    xf = os.path.join(ROOT, 'jobs/returns/followup_2026-10-15/part1/return_a.csv')
    if os.path.exists(xf):
        universe |= {k(r['brand']) for r in csv.DictReader(open(xf, encoding='utf8')) if r['womens_clothing'].strip() == 'yes'}
    # The Cyprus Brand Set (15 Oct 2026, Sebastian): the men's-map brands read as selling no women's clothing join too,
    # marked men's only. Later answers win (the follow-up re-read Allen Edmonds).
    ans = {}
    for f in (xa, xf):
        if os.path.exists(f):
            ans.update({k(r['brand']): r['womens_clothing'].strip() for r in csv.DictReader(open(f, encoding='utf8'))})
    menonly = {kk for kk, v in ans.items() if v == 'no'}
    universe |= menonly
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
                       'fi': fibre_line(b), 'nt': b.get('notes') or {}, 'nat': natural_of(b), 'cf': clean_of(b), 'cfl': (CF.get(b['name']) or {}).get('clean_with_lyocell')})
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
                       'locator': '', 'read': (d.get('basis') or '').split(';')[0].strip(), 'mo': kk in menonly,
                       'note': 'Prices and facts are from the brand’s men’s record until its women’s prices are read.',
                       'src': 'men', 'prices': prices_of(b), 'lh': False, 'depts': 0, 'about': about_of(b),
                       'f': b.get('focus') or None, 'fa': b.get('fabric') or None, 'gl': {k.lower(): u for k, u in (b.get('garment_links') or {}).items()} or None,
                       'fi': fibre_line(b), 'nt': b.get('notes') or {}, 'nat': natural_of(b), 'cf': clean_of(b), 'cfl': (CF.get(b['name']) or {}).get('clean_with_lyocell')})
    # Segments (taxonomy ruled 15 Oct 2026: the men's fifteen plus eight new; placements provisional where not high)
    sf = os.path.join(ROOT, 'jobs/returns/brandset_segments_2026-10-15/segments.csv')
    if os.path.exists(sf):
        seg = {r['brand']: r for r in csv.DictReader(open(sf, encoding='utf8'))}
        for b in brands:
            r = seg.get(b['n'])
            if r:
                b['sg'] = r['segment']; b['sg2'] = '' if r['secondary'] == '-' else r['secondary']; b['sgc'] = r['confidence']; b['sgb'] = r['basis']
    brands.sort(key=lambda b: unicodedata.normalize('NFKD', b['n']).encode('ascii', 'ignore').decode().lower().lstrip('.'))  # alphabetical within each band
    nb = collections.Counter(b['band'] for b in brands)
    # Other brands (beauty, home, jewelry): store lists only, no tiers (Sebastian, 16 Oct 2026). Read by doors_bhj_2026-10-16.
    other = []
    for job in ('doors_bhj_2026-10-16', 'doors_tel_2026-10-16'):
      wl = os.path.join(ROOT, f'jobs/briefs/{job}/worklist_brands.csv')
      if os.path.exists(wl):
        od = collections.defaultdict(list); counted = {}
        for f in sorted(glob.glob(os.path.join(ROOT, f'jobs/returns/{job}/batch*/return_doors.csv'))):
            for r in csv.DictReader(open(f, encoding='utf8')):
                if r.get('format') == 'own-door' and r.get('status', 'open') == 'open':
                    od[r['brand']].append({'sn': r.get('store_name', ''), 'a': clean(r.get('street', '')), 'c': r.get('city', ''), 's': r.get('state', ''), 'z': clean(r.get('zip', '')), 'v': clean(r.get('venue', '')), 'op': clean(r.get('operator', '')), 'ph': re.sub(r'\D', '', r.get('phone', '') or '')})
        for f in sorted(glob.glob(os.path.join(ROOT, f'jobs/returns/{job}/batch*/return_counts.csv'))):
            for r in csv.DictReader(open(f, encoding='utf8')):
                counted[r['brand']] = r
        for r in csv.DictReader(open(wl, encoding='utf8')):
            n = r['brand']; c = counted.get(n)
            seen_addr = set(); st = []
            for x in od.get(n, []):
                if re.search(r'\bspa\b', x['sn'], re.I): continue  # a hotel spa is not a store, like a restaurant (ruled 16 Oct)
                # One door per store: the same street and ZIP (Catbird's Wedding Annex is upstairs in Williamsburg), or the
                # same ZIP and phone (Jo Malone lists stores two or three times). Rows with no street or phone are never merged.
                keys = set()
                street = re.sub(r'\s*\(.*?\)', '', (x['a'] or '').lower().split(',')[0]).strip()
                if street: keys.add(('a', street, x['z'] or x['c'].lower()))
                if len(x['ph']) >= 10 and x['z']: keys.add(('p', x['ph'][-10:], x['z'][:5]))
                if keys & seen_addr: continue
                seen_addr |= keys; x = {k: v for k, v in x.items() if k != 'ph'}; st.append(x)
            own = len(st) if c and (c.get('us_own_stores') or '').strip().upper() not in ('NC', 'HELD', '') else None   # held or unread: still counting
            other.append({'n': n, 'cat': r['category'], 'own': own, 'none': bool(c and (c.get('us_own_stores') or '').strip().upper() == 'NONE'), 'stores': st, 'tier': tier(own) if own else '',
                          'ne': sum(1 for x in st if x['s'] in NE), 'locator': (c or {}).get('locator_url', '') or '', 'read': (c or {}).get('captured_on', '') or '',
                          'note': (c or {}).get('note', '') or ''})
    for b in brands:
        b['nt'] = {k: t for k, t in ((k, tidy_note(v)) for k, v in (b.get('nt') or {}).items()) if t}
        b['basis'] = tidy_basis(b.get('basis', ''))
        b['fi'] = tidy_fi(b.get('fi', ''))
    data = {'built': datetime.date.today().isoformat(), 'brands': brands, 'other': other, 'ne': NE}
    tpl = open(os.path.join(ROOT, 'app/womens_template.html'), encoding='utf8').read()
    html = tpl.replace('/*__DATA__*/', 'const W = ' + json.dumps(data, ensure_ascii=False) + ';')
    os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
    out = os.path.join(ROOT, 'dist/womens_spectrum.html')
    open(out, 'w', encoding='utf8').write(html)
    print(f'{len(brands)} brands ({sum(1 for b in brands if b["src"]=="men" and not b.get("mo"))} crossovers, {sum(1 for b in brands if b.get("mo"))} men’s only), {sum(len(b["stores"]) for b in brands)} stores, bands {dict(nb)} -> {out} {os.path.getsize(out):,} bytes')
    if '--deploy' in sys.argv:
        # Same route as the men's map: the deploy branch, which the host copies into public_html/mfdb.
        import shutil, subprocess, tempfile
        wt = tempfile.mkdtemp()
        subprocess.run(['git', 'fetch', '-q', 'origin', 'deploy'], cwd=ROOT, check=True)
        subprocess.run(['git', 'worktree', 'add', '-q', wt, 'deploy'], cwd=ROOT, check=True)
        subprocess.run(['git', 'merge', '-q', '--ff-only', 'origin/deploy'], cwd=wt)
        shutil.copy(out, os.path.join(wt, 'womens.html'))
        shutil.copy(out, os.path.join(wt, 'brandset.html'))       # GitHub Pages address for The Cyprus Brand Set
        open(os.path.join(wt, '.nojekyll'), 'w').close()           # serve the files as they are, no Jekyll pass
        subprocess.run(['git', 'add', 'womens.html', 'brandset.html', '.nojekyll'], cwd=wt, check=True)
        ver = (re.search(r'<b>(v[\d.]+) ·', tpl) or [None, '?'])[1]
        subprocess.run(['git', '-c', 'user.name=mfdb', '-c', 'user.email=mfdb@local', 'commit', '-qm', f'deploy womens {ver}'], cwd=wt)
        subprocess.run(['git', 'push', '-q', 'origin', 'HEAD:deploy'], cwd=wt, check=True)
        subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=ROOT)
        print(f'deploy branch updated: womens {ver} -> womens.html')


if __name__ == '__main__':
    main()
