import csv
D='2026-10-10'; doors=[]
def A(**k):
    base=dict(brand='',store_name='',banner_stated='',format='own-door',status='open',street='NC',city='NC',state='NC',zip='NC',country='US',phone='NC',venue='NC',source_url='',captured_on=D,note='-')
    base.update(k); doors.append(base)
# Danner
for n,s,c,st,z,p in [("Danner - Factory Store","12021 NE Airport Way Suite B","Portland","OR","97220","(503) 251-1111"),("Danner - Landing","829 N 10th St Suite 200-A","Renton","WA","98057","(425) 226-6338"),("Danner - Tanasbourne","11010 NE Evergreen Parkway","Hillsboro","OR","97006","(503) 262-0332"),("Danner - Box Factory","555 NW Arizona Ave Suite 20","Bend","OR","97701","(541) 388-1798"),("Danner - Denver","1435 16th Street","Denver","CO","80202","(303) 623-2628"),("Danner - Woodinville","13620 NE 175th St Suite 110","Woodinville","WA","98072","(425) 818-2166")]:
    A(brand='Danner',store_name=n,banner_stated='Danner',street=s,city=c,state=st,zip=z,phone=p,venue='NC',source_url='https://danner.locally.com/stores/conversion_data (via https://www.danner.com/store-finder)',
      note='at the Danner factory site; called Factory Store; not in an outlet centre, so own-door — flagged' if 'Factory' in n else '-')
# UGG
ph={'Newbury St':'(857) 400-8270','South Coast Plaza':'(714) 551-0750','Powell Street':'(415) 329-6077','American Dream':'(201) 500-2577','Garden State':'(201) 254-8419','Lenox Square':'(404) 537-3660','Michigan Ave':'(773) 295-0904','Soho':'(212) 226-0602','5th Avenue':'(347) 696-7900','Mall of America':'(952) 373-4012'}
own=set(ph); 
for r in open('raw/ugg_us.txt').read().strip().split('|'):
    f=r.split('~'); n=f[0].replace('UGG - ','')
    fmt='own-door' if n in own else 'concession' if 'Macy' in n else 'outlet'
    A(brand='UGG',store_name=f[0].strip(),banner_stated='UGG',format=fmt,street=f[1].strip(),city=f[2],state=f[3],zip=f[4],phone=ph.get(n,'NC'),
      venue={'Mall of America':'Mall of America','Lenox Square':'Lenox Square','American Dream':'American Dream','Garden State':'Westfield Garden State Plaza','South Coast Plaza':'South Coast Plaza',"Macy's Herald Square":"Macy's Herald Square"}.get(n, n if fmt=='outlet' else '-'),
      source_url='https://www.ugg.com/our-stores/' if fmt=='own-door' else 'https://ugg.locally.com/stores/conversion_data (via https://www.ugg.com/stores.html)',
      note={'outlet':'in an outlet centre','concession':'branded shop inside a department store'}.get(fmt,'-'))
A(brand='UGG',store_name='UGG Williamsburg, NYC',banner_stated='UGG',status='coming soon',street='129 N 6th Street',city='Brooklyn',state='NY',zip='11249',phone='(347) 986-2160',venue='-',source_url='https://www.ugg.com/our-stores/',note='listed COMING SOON; not counted')
# Universal Works
for n,s,c,z,co,p,fmt,nt in [("London King's Cross","Unit 30 Coal Drops Yard","London","N1C 4DQ","GB","+44 (0)20 8036 3352","own-door","-"),("London Soho","26 Berwick Street","London","W1F 8RG","GB","+44 (0)20 3581 1501","own-door","-"),("Nottingham","120-122 Derby Road","Nottingham","NG1 5FB","GB","+44 (0)115 666 7266","own-door","-"),("Tokyo","6th Floor, Hankyu Men's Tokyo, 2-5-1 Yurakucho, Chiyoda City","Tokyo","100-8488","JP","NC","concession","inside Hankyu Men's department store; not counted")]:
    A(brand='Universal Works',store_name=n,banner_stated='Universal Works',format=fmt,street=s,city=c,state='-',zip=z,country=co,phone=p,venue="Hankyu Men's Tokyo" if fmt=='concession' else ('Coal Drops Yard' if 'Cross' in n else '-'),source_url='https://universalworks.com/en-us/pages/stores',note=nt)
for n,s,c,z,co,p,op in [("Partnership Store Lyon","10 Rue d'Algérie","Lyon","69001","FR","NC","Shoez Gallery"),("Partnership Store Toulouse","6 Rue Temponières","Toulouse","31000","FR","NC","Mr Sunbell Store"),("Partnership Store Berlin","Rosa-Luxemburg-Strasse 28","Berlin","10178","DE","+49(0) 30 984306063","Trüffelschwein")]:
    A(brand='Universal Works',store_name=n,banner_stated='Universal Works Partnership Store',street=s,city=c,state='-',zip=z,country=co,phone=p,venue='-',source_url='https://universalworks.com/en-us/pages/partnership-stores',note=f'operated by {op} (the page says day-to-day running is managed by the {op} team and it cannot take returns from other UW stores)')
# Jos. A. Bank
addr={}
for r in open('raw/josbank_addr.txt').read().replace('\n','|').strip('|').split('|'):
    f=r.split('~'); addr[f[0]]=f[1:]
broken={'walnut-creek-ca-109','baton-rouge-la-111','northborough-ma-58','portsmouth-nh-114','appleton-wi-115','middleton-wi-28'}
for r in open('raw/josbank_dir.txt').read().strip().split('|'):
    slug,name=r.split('~'); city_st,venue=name.split(' - ',1)
    st_,c,stt,z,p=addr[slug]
    fmt='outlet' if slug=='leesburg-va-937' else 'own-door'
    nt=[]
    if fmt=='outlet': nt.append('241 Fort Evans Rd NE is Leesburg Corner Premium Outlets (same address as UGG Leesburg Corner Premium Outlets); outlet under the outlet-centre ruling')
    if slug in broken: nt.append('store page returns 404; address and phone from the locator search on josbank.com/store-locator, 2026-10-10')
    A(brand='Jos. A. Bank',store_name=f'Jos. A. Bank {venue.title()}',banner_stated='Jos. A. Bank',format=fmt,street=st_,city=c,state=stt,zip=z,phone=p,venue=venue.title(),
      source_url='https://www.josbank.com/store-locator' if slug in broken else f'https://www.josbank.com/store-locator/{slug}',note='; '.join(nt) or '-')
# Zara — fields as the locator writes them
for r in (open('raw/zara_us_pass1.txt').read().strip().strip('|')+open('raw/zara_us_extra.txt').read().strip()).split('|'):
    f=r.split('~')
    if f[10]=='EMP': continue
    sid,nm,ad,city,st,z,typ,status,ph,man=f[:10]
    A(brand='Zara',store_name=nm if nm else f'ZARA {city} (street store)',banner_stated='Zara',street=ad,city=city,state=st[2:],zip=z,phone=ph,venue=nm if typ=='Mall' and nm else '-',
      source_url='https://www.zara.com/us/en/stores-locator',note='; '.join(x for x in [f'locator id {sid}; type {typ}; fields as written by the locator', 'no Man section listed (Woman, Kids only)' if man=='noM' else ''] if x))
cols=['brand','store_name','banner_stated','format','status','street','city','state','zip','country','phone','venue','source_url','captured_on','note']
with open('out/own_doors_counts.csv','w',newline='',encoding='utf8') as f:
    w=csv.DictWriter(f,cols); w.writeheader(); w.writerows(doors)
from collections import Counter
print(Counter((d['brand'],d['format'],d['status']) for d in doors))
