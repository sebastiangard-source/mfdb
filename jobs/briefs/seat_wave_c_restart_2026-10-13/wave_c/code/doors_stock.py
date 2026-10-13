import csv, re
D='2026-10-10'
OD=['brand','store_name','banner_stated','format','status','street','city','state','zip','country','phone','venue','source_url','captured_on','note']
ST=['brand','locator_url','locator_kind','shop_name','street','city','state','zip','country','shop_kind','source','note']
d=[]
def A(**k):
    r={c:'NC' for c in OD}; r.update(status='open',captured_on=D,venue='-',note='-'); r.update(k); d.append(r)
A(brand='Alan Flusser',store_name='Alan Flusser Custom',banner_stated='Alan Flusser Custom',format='own-door',street='3 East 48th Street, Floor 3',city='New York',state='NY',zip='10017',country='US',phone='+1-212-888-4500',source_url='https://alanflusser.com/',note='by appointment; showroom')
A(brand='Anglo-Italian',store_name='Anglo-Italian Company',banner_stated='Anglo-Italian',format='own-door',street='57 Weymouth Street',city='London',state='-',zip='W1G 8NP',country='GB',phone='+44 20 7183 4492',source_url='https://www.angloitalian.com/pages/our-store',note='Tue–Sat 11am–7pm; New York trunk shows only, not a door')
for n,s,c,z,co,f,nt in [('Asket','72-74 Brewer Street','London','-','GB','own-door','full assortment, free repairs'),('Asket','Norrmalmstorg 1','Stockholm','-','SE','own-door','full assortment, free repairs'),
    ('Asket Archive','Stockholm Quality Outlet, Barkarby','Stockholm','-','SE','outlet','previous editions; in an outlet centre'),('Asket Pop-Up','Amiraplatz 1','Munich','-','DE','pop-up','opening soon; open 5/11–28/11 2026')]:
    A(brand='Asket',store_name=n,banner_stated='Asket',format=f,status='coming soon' if f=='pop-up' else 'open',street=s,city=c,state='-',zip=z,country=co,source_url='https://www.asket.com/en-us/stores',note=nt)
A(brand='Awake NY',store_name='Awake NY Flagship',banner_stated='Awake NY',format='own-door',street='62 Orchard St',city='New York',state='NY',zip='NC',country='US',source_url='https://awakenyclothing.com/pages/flagship',note='page gives street and city only')
A(brand='Aztech Mountain',store_name='42 Hudson Street',banner_stated='Aztech Mountain',format='own-door',street='42 Hudson Street',city='New York',state='NY',zip='10013',country='US',phone='(646) 449-8558',source_url='https://aztechmountain.com/pages/locations',note='also sells Amundsen, I Pezzi Dipinti, Performance Ski Aspen, Montura, Salomon, Sweet Protection')
A(brand='Aztech Mountain',store_name='Aztech Mountain at Arlberg Club House',banner_stated='Aztech Mountain',format='concession',street='Dorf 2',city='Lech',state='-',zip='6764',country='AT',phone='+43 5583 2134500',venue='Arlberg Club House',source_url='https://aztechmountain.com/pages/locations',note='"first European concession"; not counted')
for n,s,c,st,z,p in [('BAD BIRDIE SCOTTSDALE - FASHION SQUARE','7014 E Camelback Rd Suite #2232','Scottsdale','AZ','85251','(520) 619-7328'),('BAD BIRDIE UTC WESTFIELD - SAN DIEGO','4525 La Jolla Village Drive Suite D18','San Diego','CA','92122','(858) 253-6675'),('BAD BIRDIE SCOTTSDALE - KIERLAND COMMONS','15034 N Scottsdale Rd Suite 105G1B','Scottsdale','AZ','85254','(623) 526-5565')]:
    A(brand='Bad Birdie',store_name=n,banner_stated='Bad Birdie',format='own-door',street=s,city=c,state=st,zip=z,country='US',phone=p,venue={'Scottsdale':'Scottsdale Fashion Square' if 'FASHION' in n else 'Kierland Commons','San Diego':'Westfield UTC'}[c],source_url='https://badbirdiegolf.com/pages/stores')
for n,s,c,st,z,p in [('Williamsburg','69 N 7th St','Brooklyn','NY','11249','(718) 576-3299'),('SoHo','426 Broome St','New York','NY','10013','(646) 455-0844'),('Boston','73 Newbury St','Boston','MA','02116','(857) 991-1498'),('Seattle','5342 Ballard Ave NW','Seattle','WA','98107','(206) 906-9096'),('Silver Lake','3212 Sunset Blvd','Los Angeles','CA','90026','(323) 407-6447'),('Portland','524 NW 23rd Ave','Portland','OR','97210','(503) 384-2669'),('Chicago','1563 N Milwaukee Ave','Chicago','IL','60622','(773) 360-1448')]:
    A(brand='Blundstone',store_name='Blundstone '+n,banner_stated='Blundstone',format='own-door',street=s,city=c,state=st,zip=z,country='US',phone=p,source_url='https://www.blundstone.com/pages/blundstone-shops')
A(brand='Beams',store_name='BEAMS MALIBU',banner_stated='BEAMS',format='own-door',street='23710 Malibu Rd',city='Malibu',state='CA',zip='90265',country='US',source_url='https://beams-america.com/pages/our-locations',note='Beams America store; multi-brand shop under the BEAMS name')
with open('own_doors.csv','w',newline='',encoding='utf8') as f:
    w=csv.DictWriter(f,OD); w.writeheader(); w.writerows(d)
s=[]
def S(**k):
    r={c:'NC' for c in ST}; r.update(source=f'Chrome {D}',note='-'); r.update(k); s.append(r)
S(brand='Alan Flusser',locator_url='NONE',locator_kind='none',shop_name='NONE',street='NONE',city='NONE',state='NONE',zip='NONE',country='NONE',shop_kind='NONE',note='custom house, sells only through its own showroom; no stockist page')
S(brand='Anglo-Italian',locator_url='NONE',locator_kind='none',shop_name='NONE',street='NONE',city='NONE',state='NONE',zip='NONE',country='NONE',shop_kind='NONE',source='https://www.angloitalian.com/pages/about',note='"Anglo-Italian does not wholesale"; /pages/stockists 404')
S(brand='Asket',locator_url='NC',locator_kind='NC',shop_name='NC',note='not looked for within the time box (Asket sells direct; no stockist link seen in nav)')
for n in ['A Ma Maniere','Feature','Livestock','Kith','Headquarter','Politics','Social Status','August Shop','Concepts','Homebread','Island Snow','Lapstone & Hammer','Maze','Momentum','NRML','Oneness','Packer','Sole Classics']:
    S(brand='Awake NY',locator_url='https://awakenyclothing.com/pages/stockists',locator_kind='stockist page',shop_name=n,street='NC',city='NC',state='NC',zip='NC',country='NC (listed under NORTH AMERICA)',shop_kind='independent',source='https://awakenyclothing.com/pages/stockists',note='page lists names only, no addresses; 51 more under Europe, Asia, Australia not rowed')
S(brand='Aztech Mountain',locator_url='https://aztechmountain.com/pages/locations',locator_kind='none',shop_name='NONE',street='NONE',city='NONE',state='NONE',zip='NONE',country='NONE',shop_kind='NONE',source='https://aztechmountain.com/pages/locations',note='"has products in various retail locations across the US and international. Reach out to find Aztech..." — no list published')
S(brand='Bad Birdie',locator_url='NONE',locator_kind='none',shop_name='NONE',street='NONE',city='NONE',state='NONE',zip='NONE',country='NONE',shop_kind='NONE',source='https://badbirdiegolf.com/pages/about-us',note='about page says "we were in pro shops, major retailers" but no list; /pages/stockists, /retailers, /find-a-retailer 404')
S(brand='Beams',locator_url='https://beams-america.com/pages/our-locations',locator_kind='none',shop_name='NONE',street='NONE',city='NONE',state='NONE',zip='NONE',country='NONE',shop_kind='NONE',source='https://beams-america.com/pages/our-locations',note='Beams America lists only its own Malibu store; no US stockist list')
S(brand='Berg & Berg',locator_url='NONE',locator_kind='none',shop_name='NONE',street='NONE',city='NONE',state='NONE',zip='NONE',country='NONE',shop_kind='NONE',source='https://bergbergstore.com/pages/stockists',note='/pages/stockists and /pages/retailers 404; no list on site')
raw=open('/home/claude/wc/raw/birdwell_dealers.txt').read().split('\n',1)[1]
state=None; country='US'
STATES={'Arizona':'AZ','California':'CA','Connecticut':'CT','Florida':'FL','Hawaii':'HI','Maryland':'MD','Massachusetts':'MA','Michigan':'MI','New Hampshire':'NH','New Jersey':'NJ','New York':'NY','North Carolina':'NC','South Carolina':'SC','Rhode Island':'RI','New South Wales':'NSW','Queensland':'QLD'}
for tok in [t.strip() for t in raw.split('|') if t.strip()]:
    if tok in STATES: state=STATES[tok]; continue
    if tok=='AUSTRALIA': country='AU'; continue
    if tok=='ONLINE RETAILER': state='online'; continue
    if state=='online':
        S(brand='Birdwell',locator_url='https://www.birdwell.com/pages/authorized-dealers',locator_kind='stockist page',shop_name=tok,street='NONE',city='NONE',state='NONE',zip='NONE',country='US',shop_kind='online only',source='https://www.birdwell.com/pages/authorized-dealers'); continue
    m=re.split(r'\s+[–-]\s+',tok,1); name=m[0]; city=m[1] if len(m)>1 else 'NC'
    S(brand='Birdwell',locator_url='https://www.birdwell.com/pages/authorized-dealers',locator_kind='stockist page',shop_name=name,street='NC',city=city,state=state,zip='NC',country=country,shop_kind='independent',source='https://www.birdwell.com/pages/authorized-dealers',note='dealer page lists name and town only')
S(brand='Blundstone',locator_url='https://www.blundstone.com/pages/stores',locator_kind='store locator',shop_name='NC',note='retailer locator renders client-side; not read within the time box')
with open('stockists.csv','w',newline='',encoding='utf8') as f:
    w=csv.DictWriter(f,ST); w.writeheader(); w.writerows(s)
from collections import Counter
print(Counter(r['brand'] for r in d)); print(Counter(r['brand'] for r in s))
