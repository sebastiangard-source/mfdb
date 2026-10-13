import csv, re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from meta_b2 import M, COMMON, D
from build_b2 import agg, styles_out, BR

HDR = next(csv.reader(open(os.path.join(HERE, 'return_template.csv'))))
ORDER = [r[0] for r in csv.reader(open(os.path.join(HERE, 'return_template.csv')))][11:21]

def rows_of(b): return [r for r in styles_out if r['brand'] == b]

def madein(b, label):
    rs = BR[b]['rows']
    n = sum(1 for r in rs if (r.get('mi') or '').strip())
    return f'{n}/{len(rs)} styles state {label}'

def tech(b, pat):
    rs = rows_of(b)
    hits = [r for r in rs if re.search(pat, r['title'] + ' ' + r['composition'], re.I)]
    seen = {}
    for r in hits:
        for mm in re.finditer(pat, r['title'] + ' ' + r['composition'], re.I): seen.setdefault(mm.group(0).lower(), mm.group(0))
    names = sorted(seen.values(), key=str.lower)
    return hits, names

TECH = {
    'C.P. Company': r'Chrome-R|Shell-R|D\.D\. Shell|Nycra-R|Flatt|Micro Kei|Metro-Tek|Micro-Tek|MetroShield|MetroShell|PrimaLoft|Gore G-Type|Pro-Tek|Nano Titanium',
    'Danner': r'GTX|GORE-TEX|PrimaLoft|Primaloft|Cordura|CORDURA|WINDSTOPPER|Octa',
    'Deus Ex Machina': r'Windstopper',
    'Dickies': r'FLEX|Cooling|DuraTech|LYCRA',
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
    if b == 'Brain Dead':
        row['styles_total'] = int(row['styles_total']) + 69
        row['mens_styles_excl_swim'] = int(row['mens_styles_excl_swim']) + 68
    for k in list(row):
        v = row[k]
        if v == 'MADEIN_BU': row[k] = madein(b, 'a making country on the product page (England, Scotland, London)')
        elif v == 'MADEIN_CP': row[k] = madein(b, 'a confection country in the product passport (weaving and dyeing countries alongside)')
        elif v == 'MADEIN_CW': row[k] = madein(b, '"Imported" without a country; none states a country')
        elif v == 'MADEIN_CL': row[k] = madein(b, 'a country ("Made in ...") on the product page')
        elif v == 'MADEIN_DN': row[k] = madein(b, 'a country of origin (14 United States)')
        elif v == 'MADEIN_DT': row[k] = madein(b, 'a country in the description (denim: Made in USA)')
        elif v == 'MADEIN_DK': row[k] = 'no country stated: product pages say "Imported" (checked on all 247 styles)'
        elif isinstance(v, str) and v.startswith('TECH_'):
            hits, names = tech(b, TECH[b]); row[k] = '; '.join(names) if names else 'NONE'
        elif isinstance(v, str) and v.startswith('TECHSHARE_'):
            hits, names = tech(b, TECH[b]); row[k] = f'{len(hits)}/{len(rows_of(b))} styles name one of these fabrics in title or composition'
    notes.append('B Corp / GOTS: NC — not reached this batch (B Lab directory search ignored its query in batch 1; GOTS database not attempted)')
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
        print(r['brand'], '|', r['tech_named_fabrics'][:80], '|', r['tech_share_of_range'], '|', r['made_in_stated_share'][:70])
