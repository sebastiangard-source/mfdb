import csv, re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from meta_b4 import M, COMMON, D
from build_b4 import agg, styles_out, BR

HDR = next(csv.reader(open(os.path.join(HERE, 'return_template.csv'))))
ORDER = [r[0] for r in csv.reader(open(os.path.join(HERE, 'return_template.csv')))][31:41]

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

from meta_b4 import TECH
MADEIN = {
    'Gap': '0/244 own styles name a country; "Imported" stated on 244/244 (full catalogue, PDP fabric bullets)',
    'Goldwin': ('MI', 'a country of origin on the PDP (Vietnam 68, China 49, Indonesia 16, Japan 6)'),
    'Kiel James Patrick': ('MI', '"Made in USA" (the rest say "Imported")'),
}
FULL = {  # large houses: full-catalogue counts over the sample
    'Gap': dict(styles_total=244, styles_with_composition=244, colourway_ratio='816/244', swim_styles='NC', swim_share_of_range='NC', mens_styles_excl_swim='NC',
                style_method='style_id (full own catalogue counted from the product-search API: 244 styles / 816 colours; fibre shares from a 152-row category-stratified sample)'),
    'Jos. A. Bank': dict(styles_total=653, styles_with_composition=555, colourway_ratio='NC', swim_styles='NC', swim_share_of_range='NC', mens_styles_excl_swim='NC',
                         style_method='part_number (full own clothing catalogue counted from the search service: 653 products; fibre shares from a 123-row category-stratified sample)'),
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
    st = m.get('styles') or {k: v for k, v in agg.get(b, {}).items() if not k.startswith('_')}
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
