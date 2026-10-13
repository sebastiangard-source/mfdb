import csv, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(HERE, 'raw'); OUT = os.path.join(HERE, 'out')
D = '2026-10-11'
OD = ['brand','store_name','banner_stated','format','status','street','city','state','zip','country','phone','venue','source_url','captured_on','note']
ST = ['brand','locator_url','locator_kind','shop_name','street','city','state','zip','country','shop_kind','source','note']
US = {'Alabama':'AL','Arizona':'AZ','California':'CA','Colorado':'CO','District of Columbia':'DC','Florida':'FL','Georgia':'GA','Illinois':'IL','Louisiana':'LA','Maryland':'MD','Michigan':'MI',
      'Minnesota':'MN','Missouri':'MO','Nevada':'NV','New Jersey':'NJ','New York':'NY','North Carolina':'NC','Ohio':'OH','Pennsylvania':'PA','South Carolina':'SC','Tennessee':'TN','Texas':'TX',
      'Virginia':'VA','Wisconsin':'WI'}
d = []
def A(**k):
    r = {c: 'NC' for c in OD}; r.update(status='open', captured_on=D, venue='-', note='-'); r.update(k); d.append(r)

# Edward Green
A(brand='Edward Green', store_name='Edward Green Jermyn Street', banner_stated='Edward Green', format='own-door', street='75 Jermyn Street', city='London', state='-', zip='SW1Y 6NP', country='GB', phone='020 7839 0202',
  source_url='https://www.edwardgreen.com/store/jermyn-st')
A(brand='Edward Green', store_name='Edward Green Paris', banner_stated='Edward Green', format='own-door', street='199 bis Boulevard St. Germain', city='Paris', state='-', zip='NC', country='FR', phone='+33 (0)1 53 63 47 50',
  source_url='https://www.edwardgreen.com/store/boulevard-st-germain')
# Evan Kinori
A(brand='Evan Kinori', store_name='Evan Kinori San Francisco', banner_stated='evan kinori', format='own-door', street='1367 Valencia Street', city='San Francisco', state='CA', zip='94110', country='US', phone='(628) 867-6535',
  source_url='https://evankinori.com/pages/visit', note='opened December 2021; joined to the studio in the back half of the building')
# Express
EXS = 'https://stores.express.com'
for l in open(os.path.join(RAW, 'exp_stores.txt'), encoding='utf8'):
    f = l.rstrip('\n').split('|')
    if len(f) < 4: continue
    name, street, csz, ph = f
    m = re.match(r'(.*), ([A-Z]{2}) (\d{5})', csz)
    city, stt, z = (m.group(1), m.group(2), m.group(3)) if m else (csz, 'NC', 'NC')
    ph = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', ph) if ph else 'NC'
    note, venue, sname = '-', name, 'Express ' + name
    if 'Express Women' in name:
        venue = re.sub(r'^Visit Express Women at ', '', name); sname = 'Express Women ' + venue
        note = 'womens-only: counted as a brand door, flagged (11 Oct ruling)'
    A(brand='Express', store_name=sname, banner_stated='EXPRESS', format='own-door', street=street, city=city, state=stt, zip=z, country='US', phone=ph, venue=venue,
      source_url=EXS + ' (store pages)', note=note)
# Freenote
A(brand='Freenote Cloth', store_name='Freenote Cloth Los Angeles', banner_stated='Freenote', format='own-door', street='5509 N. Figueroa Street', city='Los Angeles', state='CA', zip='90042', country='US', phone='323-381-5123',
  source_url='https://freenotecloth.com/pages/locations', note='open daily 11-7; chain-stitch hemming; also carries "Friends of Freenote" third-party brands')
A(brand='Freenote Cloth', store_name='Freenote Cloth San Juan Capistrano', banner_stated='Freenote', format='own-door', street='32122 Camino Capistrano Suite 100', city='San Juan Capistrano', state='CA', zip='92675', country='US',
  phone='949-481-5460', source_url='https://freenotecloth.com/pages/locations', note='Mon-Fri 9-5, Sat-Sun 9-4 (office-style hours; may sit with the head office): counted, flagged for ruling')
# Fusalp
FUS = 'https://fusalpen.storeloc.unique.paris (store locator category 1 "Fusalp store")'
for l in open(os.path.join(RAW, 'fus_stores.txt'), encoding='utf8'):
    f = l.rstrip('\n').split('|')
    if len(f) < 9: continue
    n, s, c, stt, z, cc, ph, fmt, nt = f
    venue = '-'
    if fmt == 'outlet': venue = nt.replace(' (outlet centre)', ''); nt = 'store in an outlet centre: outlet, not counted'
    elif fmt == 'concession':
        venue = re.search(r'\((.*?)\)', nt).group(1); nt = 'department-store counter: concession, not counted' + ('; womens-only' if 'womens-only' in nt else '')
    elif fmt == 'pop-up':
        venue = re.search(r'in (.*?) department store', nt).group(1) + ' department store'
        nt = 'store e-mail names it a pop-up; dates not given on the locator; not counted (for ruling)'
    elif 'shopping centre' in nt: venue = nt.replace(' shopping centre', ''); nt = 'shop in a shopping centre'
    A(brand='Fusalp', store_name=n, banner_stated='FUSALP', format=fmt, status='open (dates not stated)' if fmt == 'pop-up' else 'open', street=s, city=c, state=stt, zip=z, country=cc,
      phone=ph if ph else 'NC', venue=venue, source_url=FUS, note=nt)
# G-Star (facts-first 8 Oct: names only)
GSS = 'https://www.g-star.com/en_us (store finder getstores?country_iso=US; facts-first 8 Oct)'
for n, c, stt, v, fmt in [('G-Star Atlanta Lenox Square', 'Atlanta', 'GA', 'Lenox Square', 'own-door'), ('G-Star Houston Galleria', 'Houston', 'TX', 'Galleria', 'own-door'),
                           ('G-Star Pentagon City', 'NC', 'NC', 'Pentagon City', 'own-door'), ('G-Star Aventura Mall', 'NC', 'NC', 'Aventura Mall', 'own-door'),
                           ('G-Star King of Prussia', 'NC', 'NC', 'King of Prussia', 'own-door'), ('G-Star Melrose Ave', 'Los Angeles', 'CA', '-', 'own-door'),
                           ('G-Star Soho', 'New York', 'NY', '-', 'own-door'), ('G-Star Chicago Shops at Northbridge', 'Chicago', 'IL', 'Shops at Northbridge', 'own-door'),
                           ('G-Star Garden State Plaza', 'NC', 'NC', 'Garden State Plaza', 'own-door'),
                           ('G-Star Sawgrass Mills', 'NC', 'NC', 'Sawgrass Mills', 'outlet'), ('G-Star Jersey Gardens', 'NC', 'NC', 'Jersey Gardens', 'outlet'),
                           ('G-Star Woodbury Common', 'NC', 'NC', 'Woodbury Common', 'outlet'), ('G-Star Belmont Park Village', 'NC', 'NC', 'Belmont Park Village', 'NC')]:
    st_ = '237 Lafayette St' if 'Soho' in n else 'NC'
    note = '-' if fmt == 'own-door' else ('store in an outlet centre: outlet, not counted' if fmt == 'outlet' else 'format not stated in the finder record; not counted')
    A(brand='G-Star', store_name=n, banner_stated='G-Star', format=fmt, street=st_, city=c, state=stt, zip='NC', country='US', phone='NC', venue=v, source_url=GSS, note=(note if note != '-' else 'G-Star-named full-price door') + ('; address detail not captured (names only in the 8 Oct record)' if st_ == 'NC' else ''))
# Gallery Dept.
A(brand='Gallery Dept.', store_name='GALLERY DEPT. Los Angeles', banner_stated='GALLERY DEPT.', format='own-door', street='7956 Beverly Blvd', city='Los Angeles', state='CA', zip='90048', country='US', phone='(310) 899-2313',
  source_url='https://gallerydept.com/pages/stores', note='Mon-Sat 11-7, Sun 12-6')
A(brand='Gallery Dept.', store_name='GALLERY DEPT. Miami', banner_stated='GALLERY DEPT.', format='own-door', street='140 NE 39th St Suite 108', city='Miami', state='FL', zip='33137', country='US', phone='NC', venue='Miami Design District',
  source_url='https://gallerydept.com/pages/stores')
# brands with no own door: one NONE row each
for b, src, nt in [('Eastside Golf', 'https://eastsidegolf.com/pages/store-locator', 'no Eastside Golf store; locator lists stockists only'),
                   ('Flint and Tinder', 'https://huckberry.com/explore/stores', 'ruled 10 Oct: 0 own doors; Huckberry stores are stockist rows'),
                   ('Frye', 'counts return 10 Oct', 'store locator redirects to contact; door count 0 (ruled)')]:
    A(brand=b, store_name='NONE', banner_stated='NONE', format='NONE', status='NONE', street='NONE', city='NONE', state='NONE', zip='NONE', country='NONE', phone='NONE', venue='NONE', source_url=src, note=nt)
with open(os.path.join(OUT, 'own_doors.csv'), 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, OD); w.writeheader(); w.writerows(d)

# ------------------------------------------------------------------ stockists
s = []
def S(**k):
    r = {c: 'NC' for c in ST}; r.update(source=f'Chrome {D}', note='-'); r.update(k); s.append(r)
NONEROW = dict(shop_name='NONE', street='NONE', city='NONE', state='NONE', zip='NONE', country='NONE', shop_kind='NONE')
ESL = 'https://eastsidegolf.com/pages/store-locator'
for l in open(os.path.join(RAW, 'esg_stockists.txt'), encoding='utf8'):
    f = l.rstrip('\n').split('|')
    if len(f) < 7: continue
    n, st_, c, stt, z, co, ph = f
    stt = US.get(stt.strip(), stt.strip()) or '-'
    if stt.startswith('District'): stt = 'DC'
    cc = {'United States': 'US', 'United Kingdom': 'GB', 'Bermuda': 'BM'}[co]
    kind = 'golf club or pro shop' if re.search(r'golf|club|country|links|course|resort', n, re.I) else 'independent'
    S(brand='Eastside Golf', locator_url=ESL, locator_kind='store locator', shop_name=n, street=st_, city=c, state=stt, zip=z or 'NC', country=cc, shop_kind=kind,
      source='stockist.co widget u22909 (locations/all)', note='duplicate rows without address dropped (214 raw rows -> 112)')
EGL = 'https://www.edwardgreen.com/stockists'
for n, st_, c, stt in [('Cuffs Clothing', 'NC', 'Chagrin Falls', 'OH'), ('Dashing', '320 S Dearborn', 'Chicago', 'IL'), ("Gentlemen's Footwear", '6114 Village Way', 'San Diego', 'CA'),
                       ('George Bass', 'NC', 'New Orleans', 'LA'), ("Khaki's of Carmel", 'NC', 'Carmel', 'CA'), ('Leffot', '10 Christopher St', 'New York', 'NY'), ('Mr Sid', 'NC', 'Newton', 'MA'),
                       ('Old House Provisions', 'NC', 'Alexandria', 'VA'), ('Sid Mashburn', '1198 Howell Mill Rd', 'Atlanta', 'GA'), ('Sid Mashburn', 'NC', 'Houston', 'TX')]:
    S(brand='Edward Green', locator_url=EGL, locator_kind='stockist page', shop_name=n, street=st_, city=c, state=stt, zip='NC', country='US', shop_kind='independent', source=EGL,
      note='US rows only; page lists North America 12 (also L\'Uomo Montreal, Silver Deer Mexico City), Europe 15, Asia 25, rest of world 2')
EKL = 'https://evankinori.com/pages/about'
for n, c, stt in [("c'h'c'm", 'New York', 'NY'), ('180 The Store', 'New York', 'NY'), ('Reliquary', 'San Francisco', 'CA'), ('Departamento', 'Los Angeles', 'CA'), ('Equipment', 'Minneapolis', 'MN'),
                  ('Glasswing', 'Seattle', 'WA'), ('Rennes', 'Philadelphia', 'PA'), ('Rocha', 'Austin', 'TX')]:
    S(brand='Evan Kinori', locator_url=EKL, locator_kind='stockist page', shop_name=n, street='NC', city=c, state=stt, zip='NC', country='US', shop_kind='independent', source=EKL,
      note='page gives names and cities only; US rows only (also Canada 2, Australia 1, Europe 15, Japan 8, Korea 1, China 1)')
S(brand='Express', locator_url='https://stores.express.com', locator_kind='store locator', note='locator lists Express stores only; third-party stockists not looked for', shop_name='NC', street='NC', city='NC', state='NC', zip='NC', country='NC', shop_kind='NC')
HBL = 'https://huckberry.com/explore/stores'
for st_, c, stt, z in [('425 Hayes St', 'San Francisco', 'CA', 'NC'), ('1239 Wisconsin Ave NW', 'Washington', 'DC', 'NC'), ('837 W Armitage Ave', 'Chicago', 'IL', 'NC')]:
    S(brand='Flint and Tinder', locator_url=HBL, locator_kind='store locator', shop_name='Huckberry', street=st_, city=c, state=stt, zip=z, country='US', shop_kind='other brand own door',
      source=HBL + ' (facts-first 8 Oct)', note='ruled 10 Oct: Huckberry store carrying its house label Flint and Tinder; not a Flint and Tinder door')
S(brand='Freenote Cloth', locator_url='NONE', locator_kind='none', source='freenotecloth.com stockist page returns 404', note='no stockist list published', **NONEROW)
S(brand='Frye', locator_url='NC', locator_kind='NC', note='store locator redirects to contact (counts return 10 Oct); no stockist list read', shop_name='NC', street='NC', city='NC', state='NC', zip='NC', country='NC', shop_kind='NC')
FUL = 'https://fusalpen.storeloc.unique.paris (category 2 "Partner store")'
for n, st_, c, stt, z in [('Miller Sports', '408 S Hunter St', 'Aspen', 'CO', 'NC'), ('Cole Sport', '1615 Park Ave', 'Park City', 'UT', 'NC'), ('Brass Ranch', 'River Run, 1 Sun Valley Rd', 'Sun Valley', 'ID', 'NC')]:
    S(brand='Fusalp', locator_url=FUL, locator_kind='store locator', shop_name=n, street=st_, city=c, state=stt, zip=z, country='US', shop_kind='independent', source=FUL,
      note='US rows only; 110 partner stores worldwide, 107 non-US not rowed')
S(brand='G-Star', locator_url='NC', locator_kind='store locator', note='facts-first 8 Oct: 101 US points of sale (52 department store, 28 multi-brand, 7 shop-in-shop and others); not rowed (store endpoint not reached in this read)',
  shop_name='NC', street='NC', city='NC', state='NC', zip='NC', country='NC', shop_kind='NC')
S(brand='Gallery Dept.', locator_url='NC', locator_kind='NC', note='stockists not looked for (the stores page lists the two own stores only)', shop_name='NC', street='NC', city='NC', state='NC', zip='NC', country='NC', shop_kind='NC')
with open(os.path.join(OUT, 'stockists.csv'), 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, ST); w.writeheader(); w.writerows(s)
from collections import Counter
print(Counter(r['brand'] for r in d)); print(Counter(r['brand'] for r in s))
print(Counter((r['brand'], r['format']) for r in d if r['brand'] in ('Fusalp', 'G-Star')))
bad = [(r['brand'], k) for r in d + s for k in r if str(r[k]).strip() == '']
print('empty:', bad[:10])
