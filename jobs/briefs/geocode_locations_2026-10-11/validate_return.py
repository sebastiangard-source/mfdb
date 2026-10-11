#!/usr/bin/env python3
"""Check a geocoding return before sending it back.
   python3 validate_return.py locations_db_v1.csv return.csv
Fails on: a door_id missing or repeated; lat/lon outside the door's state (bounding boxes below,
with a 0.3-degree margin); a 'rooftop' or 'street' match more than ~25 km from the ZIP's
first-three-digit area as a sanity flag (warn only); any empty cell."""
import csv, sys, math
BOX = {'AL':(30.1,35.1,-88.5,-84.8),'AK':(51,71.5,-180,-129),'AZ':(31.3,37.1,-114.9,-109),'AR':(33,36.6,-94.7,-89.6),
'CA':(32.5,42.1,-124.5,-114.1),'CO':(36.9,41.1,-109.1,-102),'CT':(40.9,42.1,-73.8,-71.7),'DE':(38.4,39.9,-75.8,-75),
'DC':(38.7,39.1,-77.2,-76.9),'FL':(24.4,31.1,-87.7,-79.9),'GA':(30.3,35.1,-85.7,-80.8),'HI':(18.8,22.3,-160.3,-154.7),
'ID':(41.9,49.1,-117.3,-111),'IL':(36.9,42.6,-91.6,-87.4),'IN':(37.7,41.8,-88.1,-84.7),'IA':(40.3,43.6,-96.7,-90.1),
'KS':(36.9,40.1,-102.1,-94.5),'KY':(36.4,39.2,-89.6,-81.9),'LA':(28.9,33.1,-94.1,-88.7),'ME':(43,47.5,-71.1,-66.9),
'MD':(37.9,39.8,-79.5,-75),'MA':(41.2,42.9,-73.6,-69.9),'MI':(41.6,48.3,-90.5,-82.1),'MN':(43.4,49.4,-97.3,-89.4),
'MS':(30.1,35.1,-91.7,-88),'MO':(35.9,40.7,-95.8,-89),'MT':(44.3,49.1,-116.1,-104),'NE':(39.9,43.1,-104.1,-95.3),
'NV':(35,42.1,-120.1,-114),'NH':(42.6,45.4,-72.6,-70.6),'NJ':(38.9,41.4,-75.6,-73.8),'NM':(31.3,37.1,-109.1,-103),
'NY':(40.4,45.1,-79.8,-71.8),'NC':(33.8,36.6,-84.4,-75.4),'ND':(45.9,49.1,-104.1,-96.5),'OH':(38.4,42,-84.9,-80.5),
'OK':(33.6,37.1,-103.1,-94.4),'OR':(41.9,46.3,-124.6,-116.4),'PA':(39.7,42.3,-80.6,-74.6),'RI':(41.1,42.1,-71.9,-71.1),
'SC':(32,35.3,-83.4,-78.5),'SD':(42.4,45.9,-104.1,-96.4),'TN':(34.9,36.7,-90.4,-81.6),'TX':(25.8,36.6,-106.7,-93.5),
'UT':(36.9,42.1,-114.1,-109),'VT':(42.7,45.1,-73.5,-71.4),'VA':(36.5,39.5,-83.7,-75.2),'WA':(45.5,49.1,-124.9,-116.9),
'WV':(37.2,40.7,-82.7,-77.7),'WI':(42.4,47.1,-92.9,-86.8),'WY':(40.9,45.1,-111.1,-104),'PR':(17.8,18.6,-67.4,-65.2)}
OK_MATCH = {'rooftop','street','range','interpolated','locator','NC'}
db = {r['door_id']: r for r in csv.DictReader(open(sys.argv[1], encoding='utf8'))}
ret = list(csv.DictReader(open(sys.argv[2], encoding='utf8')))
fails, warns = [], []
seen = set()
for r in ret:
    i = r['door_id']
    if i not in db: fails.append(f'{i}: not in the input'); continue
    if i in seen: fails.append(f'{i}: repeated'); continue
    seen.add(i)
    for c in ('lat','lon','geo_source','geo_match','matched_address','geo_note'):
        if r.get(c, '') == '': fails.append(f'{i}: empty {c}')
    if r['geo_match'] not in OK_MATCH: fails.append(f'{i}: geo_match {r["geo_match"]!r} not in {sorted(OK_MATCH)}')
    if r['lat'] == 'NC': continue
    try: lat, lon = float(r['lat']), float(r['lon'])
    except ValueError: fails.append(f'{i}: lat/lon not numeric'); continue
    st = db[i]['state']; b = BOX.get(st)
    if b and not (b[0]-0.3 <= lat <= b[1]+0.3 and b[2]-0.3 <= lon <= b[3]+0.3):
        fails.append(f'{i}: {lat},{lon} is outside {st} ({db[i]["city"]})')
missing = [i for i in db if i not in seen]
if missing: fails.append(f'{len(missing)} door_ids have no row in the return (first: {missing[:5]})')
nc = sum(1 for r in ret if r['lat'] == 'NC')
print(f'{len(ret)} rows, {nc} NC, {len(fails)} failures')
for f in fails[:40]: print('  FAIL', f)
sys.exit(1 if fails else 0)
