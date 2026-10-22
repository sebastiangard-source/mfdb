#!/usr/bin/env python3
"""Add (or refresh) a "WS centers" set on the overlaps page (app/sub/overlaps.html), from the WS center directories.

Uses the same retail filter and name folding as tools/build_ws_venn.py. Existing rows get the WS bit where the folded
name matches; WS brands on no other list are added as new rows, with a category from the directory's own category
(Fashion & Style -> Apparel & accessories, Beauty -> Beauty & fragrance, Home -> Home, otherwise Unclear).
Rerunnable: the WS bit is always the ninth character of m.
"""
import csv, glob, json, os, re, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_ws_venn import fold, NOT_RETAIL, ROOT

P = os.path.join(ROOT, 'app/sub/overlaps.html')


def main():
    s = open(P, encoding='utf8').read()
    lines = s.split('\n'); i = [k for k, l in enumerate(lines) if l.lstrip().startswith('var ALL=')][0]
    A = json.loads(re.match(r'\s*var ALL=(\[.*\]);\s*$', lines[i]).group(1))
    A = [r for r in A if not (r.get('ws_only'))]                     # rerun: drop rows this script added
    ws, cat = collections.defaultdict(set), {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'jobs/returns/ws_centers_2026-10-22/return_tenants*.csv'))):
        for t in csv.DictReader(open(f, encoding='utf8')):
            c = t['category_on_site'].lower(); n = t['tenant_name'].strip()
            if not (any(k in c for k in ('fashion', 'specialty', 'beauty', 'home', 'shopping')) or c == 'nd'): continue
            if NOT_RETAIL.search(n): continue
            k = fold(n); ws[k].add(t['center']); cat.setdefault(k, (n, c))
    seen = set(); hit = 0
    for r in A:
        m = r['m'][:8]; k = fold(r['n'])
        r['m'] = m + ('1' if k in ws else '0'); hit += k in ws; seen.add(k)
        if k in ws: r['wc'] = sorted(ws[k])
    added = 0
    for k, (n, c) in cat.items():
        if k in seen: continue
        ci = 0 if 'fashion' in c else 2 if 'beauty' in c else 4 if 'home' in c else 6
        A.append({'n': n, 'm': '00000000' + '1', 't': 0, 'f': '', 'c': ci, 's': None, 'g': '', 'o': '', 'wc': sorted(ws[k]), 'ws_only': 1}); added += 1
    A.sort(key=lambda r: r['n'].lower())
    lines[i] = 'var ALL=' + json.dumps(A, ensure_ascii=False) + ';'
    s = '\n'.join(lines)
    if "k:'WS'" not in s:
        s = s.replace("{k:'NM',name:'Neiman Marcus',color:'#475569'}];", "{k:'NM',name:'Neiman Marcus',color:'#475569'},{k:'WS',name:'WS centers',color:'#0E7490'}];", 1)
        s = s.replace("'six','seven','eight'][NS]", "'six','seven','eight','nine'][NS]", 1)
        s = s.replace('<title>How the eight brand lists overlap</title>', '<title>How the nine brand lists overlap</title>', 1)
        s = s.replace('<h1>How the eight brand lists overlap</h1>', '<h1>How the nine brand lists overlap</h1>', 1)
        s = s.replace('Saks, and Neiman Marcus.', 'Saks, Neiman Marcus, and the retail tenants of 18 WS Development centers (read from each center\'s own directory, 22 October 2026; restaurants, services and offices left out).', 1)
        # show the WS centers a brand is at, in the chip and the table
        s = s.replace("if(r.f) extra+='<small class=\"star\"", "if(r.wc) extra+='<small title=\"'+esc(r.wc.join(', '))+'\">WS: '+r.wc.length+'</small>';\n    if(r.f) extra+='<small class=\"star\"", 1)
        s = s.replace("if(s.k==='NAP'&&r.f) extra=", "if(s.k==='WS'&&r.wc) extra=' <span style=\"color:#5A6672;font-size:12px\" title=\"'+esc(r.wc.join(', '))+'\">'+r.wc.length+'</span>';\n      if(s.k==='NAP'&&r.f) extra=", 1)
    open(P, 'w', encoding='utf8').write(s)
    print(f'WS brands {len(ws)}: {hit} matched existing rows, {added} added')


if __name__ == '__main__':
    main()
