import csv, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(HERE, 'raw'); OUT = os.path.join(HERE, 'out')
D = '2026-10-11'
OD = ['brand','store_name','banner_stated','format','status','street','city','state','zip','country','phone','venue','source_url','captured_on','note']
ST = ['brand','locator_url','locator_kind','shop_name','street','city','state','zip','country','shop_kind','source','note']
d = []
def A(**k):
    r = {c: 'NC' for c in OD}; r.update(status='open', captured_on=D, venue='-', note='-'); r.update(k); d.append(r)

# Brain Dead
BDS = 'https://wearebraindead.com/pages/stores'
for n, s, c, st, z, co, p, v, nt in [
    ('BRAIN DEAD STUDIOS', '611 N Fairfax Ave', 'Los Angeles', 'CA', '90036', 'US', '323-917-5053', '-', 'cinema with shop and cafe'),
    ('BRAIN DEAD FABRICATIONS', '3819 W Sunset Blvd', 'Los Angeles', 'CA', '90026', 'US', '323-522-3166', '-', '-'),
    ('BRAIN DEAD NEW YORK', '202 Elizabeth St', 'New York', 'NY', '10012', 'US', '646-448-4624', '-', '-'),
    ('BRAIN DEAD PORTLAND', '1022 W Burnside St, #E', 'Portland', 'OR', '97209', 'US', '971-383-2715', '-', '-'),
    ('BRAIN DEAD @ LONG BEACH RISING', '205 E Anaheim St', 'Long Beach', 'CA', '90813', 'US', 'NC', 'Long Beach Rising', 'own door, flagged (11 Oct ruling): the brand lists it under its own name; weekday hours 6am-10pm suggest a host site, but nothing names another operator'),
    ('BRAIN DEAD STUDIOS HARAJUKU', '4 Chome-29-8 Jingumae', 'Shibuya City, Tokyo', '-', '150-000', 'JP', 'NC', '-', '-'),
    ('BRAIN DEAD SHIBUYA', 'Shibuya PARCO 5F, 15-1 Udagawacho', 'Shibuya City, Tokyo', '-', '150-8377', 'JP', 'NC', 'Shibuya PARCO', 'shop in a shopping centre')]:
    A(brand='Brain Dead', store_name=n, banner_stated='BRAIN DEAD', format='own-door', street=s, city=c, state=st, zip=z, country=co, phone=p, venue=v, source_url=BDS, note=nt)
# Budd
A(brand='Budd Shirtmakers', store_name='Budd', banner_stated='Budd', format='own-door', street='3 Piccadilly Arcade', city='London', state='-', zip='SW1Y 6NH', country='GB', venue='Piccadilly Arcade',
  source_url='https://www.buddshirts.co.uk/pages/our-store', note='shop and cutting room since 1910; US trunk shows only')
# C.P. Company
CPS = 'https://www.cpcompany.com/en-us/stores/ (Stores-FindStores endpoint)'
for l in open(os.path.join(RAW, 'cp_stores.txt'), encoding='utf8'):
    f = l.rstrip('\n').split('|')
    if len(f) < 9: continue
    sid, name, a1, a2, city, z, stc, cc, ph = f[:9]
    fmt, nt, venue = 'own-door', '-', '-'
    if 'Outlet' in name: fmt, nt = 'outlet', 'in Gotemba Premium Outlets (outlet centre)'; venue = 'Gotemba Premium Outlets'
    elif re.search(r'Réel Department Store|Hankyu|Takashimaya', name + a1): fmt, nt = 'concession', 'store inside a department store; not counted as an own door'
    elif re.search(r'Mall|Parco|Forus|MixC|Kerry Centre|Taikoo Li', a1 + name, re.I): nt = 'shop in a shopping centre'
    m = re.search(r'(Réel Department Store|Hankyu Mens Osaka|Osaka Takashimaya|Shibuya Parco|Kanazawa Forus|Ouya Shopping Mall|MixC World|Kerry Centre|Taikoo Li|Hangzhou Tower Shopping Mall|JPR Harajuku Bldg)', a1 + ' ' + name)
    if m and venue == '-': venue = m.group(1)
    A(brand='C.P. Company', store_name=name, banner_stated='C.P. Company', format=fmt, street=a1, city=city, state=stc or '-', zip=z or 'NC', country=cc, phone=ph or 'NC', venue=venue, source_url=CPS, note=nt)
# Carmina
CAS = 'https://www.carminashoemaker.com/us/en/carmina-stores'
for n, s, c, st, z, co, p, fmt, nt in [
    ('Carmina New York', '45 E 45th St', 'New York', 'NY', '10017', 'US', '+1 212-687-0222', 'own-door', '-'),
    ('Carmina San Francisco', '54 Geary Street', 'San Francisco', 'CA', '94108', 'US', '+1 415-757-7526', 'own-door', '-'),
    ('Carmina Madrid', 'Claudio Coello, 73', 'Madrid', '-', 'NC', 'ES', 'NC', 'own-door', '-'),
    ('Carmina Barcelona', 'Passeig de Gràcia, 110', 'Barcelona', '-', 'NC', 'ES', 'NC', 'own-door', '-'),
    ('Carmina Palma de Mallorca', 'Unió, 4', 'Palma de Mallorca', '-', 'NC', 'ES', 'NC', 'own-door', '-'),
    ('Carmina Paris', "4 Avenue de l'Opera", 'Paris', '-', 'NC', 'FR', 'NC', 'own-door', '-'),
    ('Carmina London', '3 Clifford St (Mayfair)', 'London', '-', 'W1S 2LF', 'GB', 'NC', 'own-door', '-'),
    ('Carmina Luxembourg', '11C Avenue Porte-Neuve', 'Luxembourg', '-', 'NC', 'LU', 'NC', 'own-door', '-'),
    ('Carmina Tokyo', 'Marunouchi Naka-Dori Ave, 1-9-4 Yurakucho', 'Tokyo', '-', 'NC', 'JP', 'NC', 'own-door', '-'),
    ('Carmina Outlet Inca', "Berenguer D'Anoia, 60", 'Inca', '-', 'NC', 'ES', 'NC', 'outlet', 'the brand calls it the Carmina Outlet ("where it all began")')]:
    A(brand='Carmina', store_name=n, banner_stated='Carmina', format=fmt, street=s, city=c, state=st, zip=z, country=co, phone=p, source_url=CAS, note=nt)
# Closed
for l in open(os.path.join(RAW, 'closed_stores.txt'), encoding='utf8'):
    f = l.rstrip('\n').split('|')
    if len(f) < 7: continue
    n, s, c, z, co, p, nt = f[:7]
    if nt == "women's only": nt = "womens-only: counted as a brand door, flagged (11 Oct ruling)"
    venue = 'Alstertal-Einkaufszentrum' if 'AEZ' in n else '-'
    A(brand='Closed', store_name=n, banner_stated='CLOSED', format='own-door', street=s, city=c, state='-', zip=z, country=co, phone=p, venue=venue, source_url='https://www.closed.com/stores', note=nt or '-')
# Danner (from counts return, 10 Oct)
for row in csv.DictReader(open(os.path.join(RAW, 'danner_doors_counts.csv'), encoding='utf8')):
    d.append(row)
# Denim Tears
A(brand='Denim Tears', store_name='Denim Tears Flagship Store (African Diaspora Goods)', banner_stated='DENIM TEARS', format='own-door', street='176 Spring Street', city='New York', state='NY', zip='10012', country='US',
  phone='(646) 386-7637', source_url='https://denimtears.com/pages/stores', note='"Designed by Theaster Gates"')
A(brand='Denim Tears', store_name='Denim Tears Atlanta Residency (African Diaspora Goods)', banner_stated='DENIM TEARS', format='pop-up', status='open (dates not stated)', street='3393 Peachtree Road NE', city='Atlanta', state='GA',
  zip='30326', country='US', phone='(404) 736-6676', venue='Lenox Square', source_url='https://denimtears.com/pages/stores', note='residency = pop-up (ruled 10 Oct); the stores page gives no start or end date')
# Deus
for n, s, c, st, z, co, p, nt, url in [
    ('The Emporium of Post Modern Activities', '1001 Venice Boulevard', 'Venice (Los Angeles)', 'CA', '90291', 'US', '+1 (888) 515-3387', 'flagship with cafe and workshop', 'the-emporium-of-post-modern-activities'),
    ('The Tenement of Tenacity', '55 Avenue de la Marne', 'Biarritz', '-', '64200', 'FR', 'NC', '-', 'the-tenement-of-tenacity'),
    ('The Portal of Possibilities', 'Via Thaon Di Revel 3', 'Milan', '-', '20159', 'IT', '+39 02 83422610', 'store and workshop', 'portal-of-possibilities'),
    ('The Temple of Enthusiasm', 'NC', 'Canggu', '-', 'NC', 'ID', 'NC', 'named on the flagship page; no store page or address', 'flagship-stores'),
    ('The House of Simple Pleasures', '102-104 Parramatta Road', 'Camperdown', 'NSW', '2050', 'AU', '+61 2 8594 2800', '-', 'the-house-of-simple-pleasures'),
    ('The Mansion of Munificence', 'Av. Rebouças, 3685', 'São Paulo', '-', 'NC', 'BR', 'NC', 'store e-mail at deusbr.com: operator-run, flagged', 'the-mansion-of-munificence')]:
    A(brand='Deus Ex Machina', store_name=n, banner_stated='Deus Ex Machina', format='own-door', street=s, city=c, state=st, zip=z, country=co, phone=p, source_url='https://deuscustoms.com/pages/' + url, note=nt)
with open(os.path.join(OUT, 'own_doors.csv'), 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, OD); w.writeheader(); w.writerows(d)

# ------------------------------------------------------------------ stockists
s = []
def S(**k):
    r = {c: 'NC' for c in ST}; r.update(source=f'Chrome {D}', note='-'); r.update(k); s.append(r)
NONEROW = dict(shop_name='NONE', street='NONE', city='NONE', state='NONE', zip='NONE', country='NONE', shop_kind='NONE')
S(brand='Brain Dead', locator_url='NONE', locator_kind='none', source='https://wearebraindead.com/sitemap.xml (64 pages)', note='no stockist page among the 64 site pages', **NONEROW)
S(brand='Budd Shirtmakers', locator_url='NONE', locator_kind='none', source='https://www.buddshirts.co.uk/sitemap.xml (84 pages)', note='no stockist page; sells through its own shop, site and US trunk shows', **NONEROW)
S(brand='C.P. Company', locator_url='https://www.cpcompany.com/en-us/stores/', locator_kind='store locator', source='Stores-FindStores endpoint', note='locator returns own stores only; no stockist list published', **NONEROW)
CAL = 'https://www.carminashoemaker.com/us/en/physicalLocation/stores'
for n, st_, c, sta, z in [('CHRISTOPHER SCHAFER CLOTHIER', '37 W 26th St. Suite 306', 'New York', 'NY', '10010'), ('GENTLEMENS FOOTWEAR', '6114 Village Way', 'San Diego', 'CA', 'NC'), ('THE ARMOURY', '168 Duane St - Ground Floor', 'New York', 'NY', 'NC')]:
    S(brand='Carmina', locator_url=CAL, locator_kind='store locator', shop_name=n, street=st_, city=c, state=sta, zip=z, country='US', shop_kind='independent', source=CAL,
      note='locator mixes own stores and stockists (70 locations in 30 countries); US rows only, 63 non-US locations not rowed')
CWL = 'https://www.castawayclothing.com/apps/store-locator'
seen = set()
for l in open(os.path.join(RAW, 'castaway_stockists.txt'), encoding='utf8'):
    f = l.rstrip('\n').split('|')
    if len(f) < 3: continue
    name, street, rest = f
    key = (name.lower().replace('the ', ''), street.lower()[:12])
    if key in seen: continue
    seen.add(key)
    m = re.match(r'\s*(.*?),\s*(.*?)\s*,\s*(.+)$', rest)
    city, mid, country = (m.group(1), m.group(2), m.group(3)) if m else (rest, '', 'NC')
    mz = re.match(r'(.*?)\s*(\d{5}(?:-\d{4})?)?$', mid.strip())
    state = (mz.group(1) or '-').strip() or '-'; zz = mz.group(2) or 'NC'
    cc = {'United States': 'US', 'Bermuda': 'BM', 'Bahamas': 'BS', 'Cayman Islands': 'KY'}.get(country.strip(), country.strip())
    kind, note = 'independent', '-'
    if name.startswith("Murray's Toggery"): kind, note = 'other brand own door', 'ruled 10 Oct: Murray\'s Toggery is a stockist row; Castaway own doors = 0'
    elif re.search(r'Proshop|Resort', name): note = 'resort or club shop named by the brand; register relevance for the Spectrum thread'
    S(brand='Castaway Nantucket Island', locator_url=CWL, locator_kind='store locator', shop_name=name.strip(), street=street.strip(), city=city.strip(), state=state, zip=zz, country=cc, shop_kind=kind,
      source=CWL + ' (stores/surrounding endpoint)', note=note)
S(brand='Closed', locator_url='NC', locator_kind='NC', note='stockists not looked for within the time box (the stores page lists own stores only)')
S(brand='Danner', locator_url='https://www.danner.com/store-finder', locator_kind='store locator', note='Locally widget carries about 6,200 retailer markers mixed with the 6 Danner doors; not rowed in the time box')
for n, st_, c, sta, z, co in [('Dover Street Market London', '18-22 Haymarket (entrance on Orange Street)', 'London', '-', 'SW1Y 4DG', 'GB'), ('Dover Street Market Los Angeles', '608 Imperial Street', 'Los Angeles', 'CA', '90021', 'US'),
                              ('Dover Street Market New York', '160 Lexington Avenue', 'New York', 'NY', '10016', 'US'), ('Dover Street Market Ginza', '6-8-5 Ginza, Ginza Komatsu West', 'Tokyo', '-', '104-0061', 'JP')]:
    S(brand='Denim Tears', locator_url='https://denimtears.com/pages/stores', locator_kind='stockist page', shop_name=n, street=st_, city=c, state=sta, zip=z, country=co, shop_kind='independent',
      source='https://denimtears.com/pages/stores', note='listed as authorised retail ("Guaranteed authentic Denim Tears goods can only be purchased on our website and in the below retail locations")')
DEL = 'https://deuscustoms.com/pages/store-locator'
for l in open(os.path.join(RAW, 'deus_stockists.txt'), encoding='utf8'):
    f = l.rstrip('\n').split('|')
    if len(f) < 6: continue
    n, st_, c, sta, z, co = f
    note = '-'
    if n == '12345': note = 'shop name as listed ("12345")'
    if 'Troy Lee Designs' in n: note = 'another brand\'s store'
    S(brand='Deus Ex Machina', locator_url=DEL, locator_kind='store locator', shop_name=n, street=st_, city=c, state=sta.upper(), zip=z, country=co,
      shop_kind='other brand own door' if 'Troy Lee' in n else 'independent', source='stockist.co widget u17277 (locations/all)', note=note if note != '-' else 'US and Puerto Rico rows only; 299 non-US locations not rowed (France 136, Indonesia 52, UK 51, Canada 46, others)')
S(brand='Dickies', locator_url='https://www.dickies.com/en-us/pages/stores', locator_kind='store locator', note='locator broken (where2getit iframe 404, counts return 10 Oct); no stockist list read')
with open(os.path.join(OUT, 'stockists.csv'), 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, ST); w.writeheader(); w.writerows(s)
from collections import Counter
print(Counter(r['brand'] for r in d)); print(Counter(r['brand'] for r in s))
