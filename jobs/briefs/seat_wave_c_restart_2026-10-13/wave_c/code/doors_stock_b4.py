import csv, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(HERE, 'raw'); OUT = os.path.join(HERE, 'out')
D = '2026-10-12'
OD = ['brand','store_name','banner_stated','format','status','street','city','state','zip','country','phone','venue','source_url','captured_on','note']
ST = ['brand','locator_url','locator_kind','shop_name','street','city','state','zip','country','shop_kind','source','note']
d = []
def A(**k):
    r = {c: 'NC' for c in OD}; r.update(status='open', captured_on=D, venue='-', note='-'); r.update(k); d.append(r)

# ---------------------------------------------------------------- Gap (393 store pages, 12 Oct)
for l in open(os.path.join(RAW, 'gap_stores.txt'), encoding='utf8'):
    f = l.rstrip('\n').split('|')
    if len(f) < 6: continue
    sid, street, city, stt, z, t = f
    src = f'https://www.gap.com/stores/{stt.lower()}/{city.lower().replace(" ", "").replace(".", "")}/gap-{sid}.html'
    if t == 'R':
        A(brand='Gap', store_name=f'Gap {city} (store {sid})', banner_stated='Gap', format='own-door', street=street, city=city, state=stt, zip=z, country='US', source_url=src,
          note='Puerto Rico: counted as US (ruling)' if stt == 'PR' else 'store_type lists Gap full-price banners')
    elif t == 'M':
        A(brand='Gap', store_name=f'Gap {city} (store {sid})', banner_stated='Gap', format='own-door', street=street, city=city, state=stt, zip=z, country='US', source_url=src,
          note='store_type lists Gap, babyGap, GapKids and Gap Factory Store on one record; not in an outlet centre; counted as an own door, flagged')
    elif t == 'F':
        A(brand='Gap', store_name=f'Gap Factory {city} (store {sid})', banner_stated='Gap Factory Store', format='outlet', street=street, city=city, state=stt, zip=z, country='US', source_url=src,
          note='Gap Factory Store: outlet, not counted' + ('; Puerto Rico' if stt == 'PR' else ''))
    else:
        A(brand='Gap', store_name=f'Gap {city} (store {sid})', banner_stated='Gap', format='NC', status='closed (every day "closed" on the page)', street=street, city=city, state=stt, zip=z, country='US', source_url=src,
          note='no store_type and no open hours: excluded from the count')

# ---------------------------------------------------------------- G-Star re-read (batch 3 ruling request: addresses for the US mono-brand doors)
for l in open(os.path.join(RAW, 'gs_doors.txt'), encoding='utf8'):
    f = l.rstrip('\n').split('|')
    if len(f) < 10: continue
    n, street, city, stt, z, ph, fmt, venue, path, cat = f
    note = {'own-door': 'G-Star-named full-price door', 'outlet': 'store in an outlet centre: outlet, not counted', 'NC': 'name carries no format word (Belmont Park Village); not counted'}[fmt]
    if 'Soho' in n: note += '; record carried a temporary closure 27 Jul-17 Aug 2026 (past)'
    A(brand='G-Star', store_name=n, banner_stated='G-Star RAW' if 'RAW' in n else 'G-Star', format=fmt, street=street, city=city, state=stt, zip=z, country='US', phone=ph, venue=venue,
      source_url='https://www.g-star.com' + path, note=note + f'; finder category "{cat}"; re-read 12 Oct for batch 3')

# ---------------------------------------------------------------- Goldwin (/pages/shoplist, 12 Oct)
GWS = 'https://us.goldwin.global/pages/shoplist'
for n, s_, c, stt, z, cc, ph, fmt, venue, nt in [
    ('Goldwin NewYork', '300 Lafayette Street', 'New York', 'NY', '10012', 'US', '+1-332-278-6930', 'own-door', '-', 'Mon-Sat 11-7, Sun 12-6'),
    ('Goldwin Marunouchi', '1F, Brick Square, 2-6-1 Marunouchi, Chiyoda-ku', 'Tokyo', 'Tokyo', 'NC', 'JP', '+81 3-6268-0037', 'own-door', 'Brick Square', '-'),
    ('Goldwin Harajuku', 'Citta Jingumae 1F, 6-10-12 Jingumae, Shibuya-ku', 'Tokyo', 'Tokyo', 'NC', 'JP', '+81 3-6419-7920', 'own-door', '-', '-'),
    ('Goldwin Kyoto', '460 Sakai-cho, Nakagyo-ku', 'Kyoto', 'Kyoto', 'NC', 'JP', '+81 75-222-2228', 'own-door', '-', '-'),
    ('Goldwin Sapporo', '2nd Floor 4PLA, 4-1-1 Minami Ichijo Nishi, Chuo-ku', 'Sapporo', 'Hokkaido', '060-0061', 'JP', '+81 11-211-8611', 'own-door', '4PLA', '-'),
    ('Goldwin London', '35 Broadwick St', 'London', '-', 'W1F 0DH', 'GB', '+44 20-4630-9070', 'own-door', '-', '-'),
    ('Goldwin Munich', 'Schaefflerstrasse 4, Schaefflerhof', 'Munich', '-', '80333', 'DE', '+49 89-4625-9810', 'own-door', '-', '-'),
    ('Goldwin Seoul', '33, Eonju-ro 164-gil, Gangnam-gu', 'Seoul', '-', 'NC', 'KR', '+82 2-6203-1571', 'own-door', '-', '-'),
    ('Goldwin Beijing', 'S8-14, 1F, Building S8, No.19 Sanlitun Road, Chaoyang District', 'Beijing', '-', 'NC', 'CN', '+86 10-5365-1101', 'own-door', 'Sanlitun', '-'),
    ('Goldwin Chengdu', 'Shop 2223, 2F, Block 16, No.8 Zhongsa Cap Street, Jinjiang District', 'Chengdu', 'Sichuan', 'NC', 'CN', '+86 28-8678-5220', 'own-door', 'Chengdu Taikoo Li', 'shop in a shopping centre'),
    ('Goldwin Shanghai', "N3-12, Jing'an Kerry Centre, 1515 Nanjing Xi Lu", 'Shanghai', '-', 'NC', 'CN', 'NC', 'own-door', "Jing'an Kerry Centre", 'shop in a shopping centre'),
    ('Goldwin Hangzhou', 'L2123, L2, Hangzhou Wuxiang City, No.701 Fuchun Road, Shangcheng District', 'Hangzhou', 'Zhejiang', 'NC', 'CN', 'NC', 'own-door', 'Hangzhou Wuxiang City', 'shop in a shopping centre'),
    ('Goldwin Nanjing', 'L608, L6 Floor, Phase I, Deji Plaza, No. 18 Zhongshan Road, Xuanwu District', 'Nanjing', 'Jiangsu', 'NC', 'CN', 'NC', 'own-door', 'Deji Plaza', 'shop in a shopping centre (flag: Deji Plaza also trades as a department store)'),
    ('Goldwin Shenyang', 'Shop L570, MixC Shenyang, No. 288 Qingnian Street, Heping District', 'Shenyang', 'Liaoning', 'NC', 'CN', 'NC', 'own-door', 'MixC Shenyang', 'shop in a shopping centre'),
    ('Goldwin Shenzhen', 'Shop T117, MixC Shenzhen (Phase 3), No. 1 Shucheng Road, Luohu District', 'Shenzhen', 'Guangdong', 'NC', 'CN', 'NC', 'own-door', 'MixC Shenzhen', 'shop in a shopping centre'),
    ("Goldwin XI'AN", 'Shop 2AG0011, 2/F, SEG International Shopping Center', "Xi'an", 'Shaanxi', 'NC', 'CN', 'NC', 'own-door', 'SEG International Shopping Center', 'shop in a shopping centre'),
    ('Goldwin Shinsegae Gangnam', '8F, 176 Shinbanpo-ro, Seocho-gu', 'Seoul', '-', 'NC', 'KR', '+82 2-3479-6243', 'concession', 'Shinsegae Gangnam department store', 'department-store shop: concession, not counted'),
    ('Goldwin Hyundai Pangyo', '7F, 20 Pangyoyeok-ro 146beon-gil, Bundang-gu', 'Seongnam-si', 'Gyeonggi-do', 'NC', 'KR', '+82-31-5170-1722', 'concession', 'Hyundai Department Store Pangyo', 'department-store shop: concession, not counted'),
    ('Goldwin Shinsegae Centum City', '1F, 15 Centum 4-ro, Haeundae-gu', 'Busan', '-', 'NC', 'KR', '+82 51-745-2003', 'concession', 'Shinsegae Centum City department store', 'department-store shop: concession, not counted'),
    ('Goldwin Hyundai Trade Center Store', '6F, Hyundai Department Store Trade Center, 517 Teheran-ro, Gangnam-gu', 'Seoul', '-', 'NC', 'KR', '+82 2-3467-8711', 'concession', 'Hyundai Department Store Trade Center', 'department-store shop: concession, not counted'),
    ('GRAVITY KANDA', 'Daieido bldg. 1F 2F, 3-6 Ogawamachi, Chiyoda-ku', 'Tokyo', 'Tokyo', 'NC', 'JP', '+81 3-3291-0770', 'other brand own door', '-', 'listed among Goldwin stores but the door reads GRAVITY: not counted (for ruling)'),
    ('GRAVITY NISEKO', 'MUSE, 1-5-3 Niseko Hirafu 2-jo, Kutchan-cho, Abuta-gun', 'Kutchan', 'Hokkaido', 'NC', 'JP', '+81 136-55-8086', 'other brand own door', '-', 'door reads GRAVITY: not counted (for ruling)'),
    ('GRAVITY YUZAWA', '2F Ski Center COWABUNGA, GALA Yuzawa Ski Resort, 1039-2 Kayadaira, Yuzawa-machi, Minamiuonuma-gun', 'Yuzawa', 'Niigata', 'NC', 'JP', 'NC', 'other brand own door', 'GALA Yuzawa Ski Resort', 'door reads GRAVITY: not counted (for ruling)')]:
    A(brand='Goldwin', store_name=n, banner_stated='GRAVITY' if n.startswith('GRAVITY') else 'GOLDWIN', format=fmt, street=s_, city=c, state=stt, zip=z, country=cc, phone=ph, venue=venue, source_url=GWS, note=nt)

# ---------------------------------------------------------------- Golf Wang
GWG = 'https://golfwang.com/pages/'
A(brand='Golf Wang', store_name='GOLF WANG LA', banner_stated='GOLF WANG', format='own-door', street='350 N. Fairfax Ave', city='Los Angeles', state='CA', zip='90036', country='US', source_url=GWG + 'golf-wang-la', note='Mon-Sat 11-7, Sun 12-6')
A(brand='Golf Wang', store_name='GOLF WANG NYC', banner_stated='GOLF WANG', format='own-door', street='35 Howard St', city='New York', state='NY', zip='10013', country='US', source_url=GWG + 'golf-wang-new-york')
A(brand='Golf Wang', store_name='GOLF WANG LONDON', banner_stated='GOLF WANG', format='own-door', street='57-59 Beak Street', city='London', state='-', zip='W1F 9SJ', country='GB', source_url=GWG + 'golf-wang-london')
A(brand='Golf Wang', store_name='GOLF WANG SYDNEY', banner_stated='GOLF WANG', format='own-door', street='58 Oxford Street, Darlinghurst', city='Sydney', state='NSW', zip='2010', country='AU', source_url=GWG + 'golf-wang-sydney')

# ---------------------------------------------------------------- Hender Scheme (sukima)
HSS = 'https://henderscheme.com (shop pages)'
for n, s_, c, stt, z, ph, v in [
    ('sukima Ebisu', '1F 2-17-20 Ebisu, Shibuya-ku', 'Tokyo', 'Tokyo', '150-0013', '+81 3 6447 7448', '-'),
    ('sukima Kappabashi', '1F 4-2-10 Motoasakusa, Taito-ku', 'Tokyo', 'Tokyo', '111-0041', '+81 3 6231 7579', '-'),
    ('sukima Miyashita Park', 'MIYASHITA PARK North 2F, 6-20-10 Jingumae, Shibuya-ku', 'Tokyo', 'Tokyo', '150-0001', '+81 3 6434 1197', 'MIYASHITA PARK'),
    ('sukima Osaka', '3-8-17 Toyosaki, Kita-ku', 'Osaka', 'Osaka', '531-0072', '+81 6 6131 8484', '-'),
    ('sukima Fukuoka', '1-4-19 Minoshima, Hakata-ku', 'Fukuoka', 'Fukuoka', '812-0017', '+81 92 402 0233', '-'),
    ('sukima Nagoya', 'HAERA 1F, 3-25-1 Nishiki, Naka-ku', 'Nagoya', 'Aichi', '460-0003', '+81 52 212 6566', 'HAERA')]:
    A(brand='Hender Scheme', store_name=n, banner_stated='sukima (Hender Scheme directly operated store)', format='own-door', street=s_, city=c, state=stt, zip=z, country='JP', phone=ph, venue=v,
      source_url=HSS, note='house calls it エンダースキーマ直営店「スキマ」; counted, flagged for ruling on the sukima name')

# ---------------------------------------------------------------- Imogene + Willie
IWL = 'https://imogeneandwillie.com/pages/locations'
A(brand='Imogene + Willie', store_name='imogene + willie Nashville (flagship)', banner_stated='imogene + willie', format='own-door', street='2601 12th Avenue South', city='Nashville', state='TN', zip='NC', country='US',
  phone='+1 (615) 292-5005', source_url=IWL, note='Mon-Sat 10-6, Sun 11-5; the 2009 service-station shop; tailor shop (repairs, chainstitch hemming)')
A(brand='Imogene + Willie', store_name='imogene + willie Austin', banner_stated='imogene + willie', format='own-door', street='1401 S Congress Ave', city='Austin', state='TX', zip='NC', country='US',
  phone='+1 (512) 382-1002', source_url=IWL, note='Mon-Sat 11-7, Sun 11-6')

# ---------------------------------------------------------------- Kiel James Patrick
A(brand='Kiel James Patrick', store_name='KJP Flagship Store', banner_stated='Kiel James Patrick', format='own-door', street="3 Bowen's Wharf", city='Newport', state='RI', zip='NC', country='US', phone='401-619-4647',
  source_url='https://kieljamespatrick.com/pages/about-us', note='Mon-Thu 10-7, Fri-Sun 10-8 (hours vary by season); "est 2017"; the Pawtucket office/factory (925 Central Ave) is not open to the public, not rowed as a door')

# ---------------------------------------------------------------- no rows / NC
A(brand='Jos. A. Bank', store_name='NC', banner_stated='NC', format='NC', status='NC', street='NC', city='NC', state='NC', zip='NC', country='NC', phone='NC', venue='NC', source_url='counts return 10 Oct',
  note='doors already registered (185 own + 1 outlet); not re-read, per instructions')
A(brand='Katin', store_name='NC', banner_stated='NC', format='NC', status='NC', street='NC', city='NC', state='NC', zip='NC', country='NC', phone='NC', venue='NC', source_url='https://katinusa.com/pages/the-katin-story',
  note='story says the original Surfside surf shop is still run by Sato Hughes and her son Glenn; no address, hours or store page on the site (for ruling)')
for b, src, nt in [('Holderness & Bourne', 'https://holdernessandbourne.com', 'no store page and no own store found'),
                   ('Hickey Freeman', 'https://www.hickeyfreeman.com', 'landing page only; sends buyers to Dillard\'s; no store named (flagged)')]:
    A(brand=b, store_name='NONE', banner_stated='NONE', format='NONE', status='NONE', street='NONE', city='NONE', state='NONE', zip='NONE', country='NONE', phone='NONE', venue='NONE', source_url=src, note=nt)
with open(os.path.join(OUT, 'own_doors.csv'), 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, OD); w.writeheader(); w.writerows(d)

# ---------------------------------------------------------------- stockists
s = []
def S(**k):
    r = {c: 'NC' for c in ST}; r.update(source=f'Chrome {D}', note='-'); r.update(k); s.append(r)
NONEROW = dict(shop_name='NONE', street='NONE', city='NONE', state='NONE', zip='NONE', country='NONE', shop_kind='NONE')
NCROW = dict(shop_name='NC', street='NC', city='NC', state='NC', zip='NC', country='NC', shop_kind='NC')
IWS = 'https://imogeneandwillie.com/pages/stockists'
for l in open(os.path.join(RAW, 'iw_stockists.txt'), encoding='utf8'):
    f = l.rstrip('\n').split('|')
    if len(f) < 5: continue
    n, st_, c, stt, z = f
    S(brand='Imogene + Willie', locator_url=IWS, locator_kind='stockist page', shop_name=n, street=st_ or 'NC', city=c, state=stt, zip=z or 'NC', country='US', shop_kind='independent', source=IWS)
HSL = 'https://henderscheme.com (stockists, North America)'
for n in ['& son', 'ANNMS', 'CANOE CLUB', "C'H'C'M", "CIBONE O'TE", 'Covet + Lou', 'MAC: Modern Appealing Clothing', 'Mohawk General Store', 'Nalata Nalata', 'PACKER', 'GLASSWING', 'VEN. SPACE', 'HAVEN', 'NEIGHBOUR']:
    S(brand='Hender Scheme', locator_url=HSL, locator_kind='stockist page', shop_name=n, street='NC', city='NC', state='NC', zip='NC', country='CA' if n in ('HAVEN', 'NEIGHBOUR') else 'NC', shop_kind='independent', source=HSL,
      note='page gives names and links only under North America (HAVEN and NEIGHBOUR are Canadian; the rest not placed per row); also Europe 7, Asia 13, Oceania 2')
S(brand='Hickey Freeman', locator_url='https://www.hickeyfreeman.com', locator_kind='brand site link', shop_name="Dillard's", street='NONE', city='NONE', state='NONE', zip='NONE', country='US', shop_kind='department store (online link)',
  source='hickeyfreeman.com "SHOP NOW AT DILLARD\'S" -> dillards.com/brand/Hickey+Freeman/men', note='the only retailer the brand site names; Dillard\'s stores not read')
S(brand='Gap', locator_url='https://www.gap.com/stores', locator_kind='store locator', note='locator lists Gap stores only; third-party stockists not looked for', **NCROW)
S(brand='Goldwin', locator_url='https://us.goldwin.global/pages/shoplist', locator_kind='store locator', note='shop list holds Goldwin and GRAVITY shops only (see own_doors.csv); third-party stockists not looked for', **NCROW)
S(brand='Golf Wang', locator_url='NC', locator_kind='NC', note='no stockist page found; not looked for further', **NCROW)
S(brand='Holderness & Bourne', locator_url='NC', locator_kind='none', note='sold through golf-club pro shops (2,000+ club pages in the sitemap) and named shops in blog posts (Murray\'s Toggery; "our new Scottish stockists"); no stockist list, not rowed', **NCROW)
S(brand='Jos. A. Bank', locator_url='NC', locator_kind='NC', note='own stores only; not re-read', **NCROW)
S(brand='Katin', locator_url='NONE', locator_kind='none', source='katinusa.com nav (Our Story, Journal, Rewards only)', note='no stockist page published', **NONEROW)
S(brand='Kiel James Patrick', locator_url='NONE', locator_kind='none', source='kieljamespatrick.com wholesale application page', note='wholesale application only; no stockist list published', **NONEROW)
with open(os.path.join(OUT, 'stockists.csv'), 'w', newline='', encoding='utf8') as f:
    w = csv.DictWriter(f, ST); w.writeheader(); w.writerows(s)
from collections import Counter
print(Counter((r['brand'], r['format']) for r in d)); print(Counter(r['brand'] for r in s))
bad = [(r['brand'], k) for r in d + s for k in r if str(r[k]).strip() == '']
print('empty:', bad[:10])
nostreet = [r['store_name'] for r in d if r['format'] == 'own-door' and ('NC' in (r['street'], r['city'], r['state']))]
print('own-door rows missing street/city/state:', nostreet)
