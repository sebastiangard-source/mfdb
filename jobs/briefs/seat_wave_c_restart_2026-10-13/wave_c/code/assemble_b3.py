import csv, re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from meta_b3 import M, COMMON, D
from build_b3 import agg, styles_out, BR

HDR = next(csv.reader(open(os.path.join(HERE, 'return_template.csv'))))
ORDER = [r[0] for r in csv.reader(open(os.path.join(HERE, 'return_template.csv')))][21:31]

def rows_of(b): return [r for r in styles_out if r['brand'] == b]

def madein(b, label):
    rs = BR[b]['rows']
    n = sum(1 for r in rs if (r.get('mi') or '').strip() not in ('', '-'))
    return f'{n}/{len(rs)} styles state {label}'

def tech(b, pat):
    rs = rows_of(b)
    hits = [r for r in rs if re.search(pat, r['title'] + ' ' + r['composition'], re.I)]
    seen = {}
    for r in hits:
        for mm in re.finditer(pat, r['title'] + ' ' + r['composition'], re.I): seen.setdefault(mm.group(0).lower(), mm.group(0))
    return hits, sorted(seen.values(), key=str.lower)

TECH = {'Eastside Golf': r'TENCEL', 'G-Star': r'LYCRA|Sorona'}
MADEIN = {
    'Eastside Golf': 'no country stated: product pages give no "Made in" or "Imported" (checked on three; none of 118 style records carries a country)',
    'Evan Kinori': ('MI', 'a making place in the description (Japan, California, UK, Italy cottage knitting, Kathmandu)'),
    'Flint and Tinder': ('MI', 'a country of origin (Huckberry country_of_origin field: China, Indonesia, Vietnam, USA, India, Turkey, Peru, Cambodia, Morocco)'),
    'Freenote Cloth': ('MI', '"Sewn in USA" in the description'),
    'Fusalp': ('MI', 'a country, via a COO_ product tag only (China); product pages not read for origin'),
    'Gallery Dept.': ('MI', 'a country in the description (most Made in USA; Portugal, Italy)'),
}
FULL = {  # large houses: full-catalogue counts over the sample
    'Express': dict(styles_total=425, styles_with_composition=344, colourway_ratio='1971/426', swim_styles=0, swim_share_of_range=0, mens_styles_excl_swim=425,
                    style_method='product (full catalogue counted: 426 products read; fibre shares from a 139-row category-stratified sample)'),
    'G-Star': dict(styles_total=1835, styles_with_composition=1798, colourway_ratio='4744/1835', swim_styles='NC', swim_share_of_range='NC', mens_styles_excl_swim='NC',
                   style_method='style_code (full catalogue counted from the Algolia index; fibre shares from a 176-row category-stratified sample)'),
}

out = []
for b in ORDER:
    m = M[b]
    row = {h: 'NC' for h in HDR}
    row['brand'] = b
    for k, v in m.items():
        if k in ('g', 'styles'): continue
        if k in row: row[k] = v
    for k, v in COMMON.items(): row[k] = v
    notes = [m.get('note', '')]
    for g, cells in m['g'].items():
        for k, v in cells.items():
            if k == '_note':
                if v: notes.append(f'{g}: {v}')
                continue
            row[f'{g}_{k}'] = v
    st = m.get('styles') or {k: v for k, v in agg[b].items() if not k.startswith('_')}
    for k, v in st.items(): row[k] = v
    if b in FULL:
        row.update(FULL[b])
    for k in list(row):
        v = row[k]
        if isinstance(v, str) and v.startswith('MADEIN_'):
            spec = MADEIN[b]
            row[k] = spec if isinstance(spec, str) else madein(b, spec[1])
        elif isinstance(v, str) and v.startswith('TECHSHARE_'):
            hits, names = tech(b, TECH[b]); row[k] = f'{len(hits)}/{len(rows_of(b))} styles name one of these in title or composition' + (' (sample rows)' if b in FULL else '')
        elif isinstance(v, str) and v.startswith('TECH_'):
            hits, names = tech(b, TECH[b]); row[k] = '; '.join(names) if names else 'NONE'
    notes.append('B Corp / GOTS: NC — not reached this batch')
    notes.append('Pronunciation: NC — no brand states one')
    row['note'] = ' | '.join(x for x in notes if x)
    out.append(row)

if __name__ == '__main__':
    bad = [(r['brand'], k) for r in out for k in HDR if str(r[k]).strip() == '']
    print('empty cells:', bad[:10])
    with open(os.path.join(HERE, 'out', 'return.csv'), 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, HDR); w.writeheader(); w.writerows(out)
    print(len(out), 'rows', len(HDR), 'cols')
    for r in out:
        print(r['brand'], '|', r['styles_total'], r['styles_with_composition'], r['colourway_ratio'], '|', r['tech_named_fabrics'], '|', r['tech_share_of_range'], '|', r['made_in_stated_share'][:80])
