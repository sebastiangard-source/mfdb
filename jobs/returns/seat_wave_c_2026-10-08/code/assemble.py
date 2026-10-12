import csv, json, sys, re
sys.path.insert(0, '/home/claude/wc/b1')
from meta_b1 import M, COMMON, D
from build_b1 import agg, styles_out, BR

HDR = next(csv.reader(open('/home/claude/wc/return_template.csv')))
ORDER = [r[0] for r in csv.reader(open('/home/claude/wc/return_template.csv'))][1:11]

def madein(b):
    rows = BR[b]['rows']
    k = 'mi'
    n = sum(1 for r in rows if r.get(k, '').strip())
    return f'{n}/{len(rows)} styles state a country on the product page or feed'

def tech_bw():
    rows = BR['Birdwell']['rows']
    n = sum(1 for r in rows if re.search(r'surf(nyl|stretch)', r['comp'] + r['title'], re.I) and r['type'] in ('Boardshorts', 'Jackets'))
    return f'{n}/{len(rows)} styles are SurfNyl® or SurfStretch® boardshorts and jackets'

out = []
for b in ORDER:
    m = M.get(b)
    row = {h: 'NC' for h in HDR}
    row['brand'] = b
    if not m:
        out.append(row); continue
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
    if b in agg and agg[b]['_cov'] < 0.6: row['status'] = 'partial'
    for k in ('made_in_stated_share', 'tech_share_of_range'):
        if row[k] == 'MADEIN_AI': row[k] = madein('Anglo-Italian')
        if row[k] == 'MADEIN_AZ': row[k] = madein('Aztech Mountain')
        if row[k] == 'MADEIN_BW': row[k] = madein('Birdwell')
        if row[k] == 'MADEIN_BE': row[k] = madein('Beams')
        if row[k] == 'TECH_BW': row[k] = tech_bw()
    notes.append('B Corp / GOTS: NC — B Lab directory search ignored its query in Chrome ("Showing all 339 B Corps"); GOTS database not reached in the time box')
    row['note'] = ' | '.join(x for x in notes if x)
    out.append(row)

if __name__ == '__main__':
    bad = [(r['brand'], k) for r in out for k in HDR if str(r[k]).strip() == '']
    print('empty cells:', bad[:10])
    with open('/home/claude/wc/b1/return.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, HDR); w.writeheader(); w.writerows(out)
    print(len(out), 'rows')
