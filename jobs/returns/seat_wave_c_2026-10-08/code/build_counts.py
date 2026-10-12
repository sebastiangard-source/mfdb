import csv
D='2026-10-10'
rows=[]
def R(**k): rows.append(k)
R(brand='Birdwell',own_doors_us=0,outlets_us=0,concessions_us=0,own_doors_world=0,
  locator_url='https://www.birdwell.com/pages/authorized-dealers',locator_kind='stockist page',
  doors_basis="brand site names no Birdwell store: nav/footer link only shop-all, about-us, contact-birdwell; pages sitemap has no store/visit page; authorized-dealers page lists ~95 third-party US dealers, 2 AU, Huckberry online, none under the Birdwell name; contact page is email/chat only",
  source=f'Chrome {D}: birdwell.com home, /sitemap.xml pages, /pages/authorized-dealers, /pages/contact-birdwell, /pages/about-us',
  note="Worklist said 'Newport Beach store'; nothing on birdwell.com names one. The two Newport Beach entries on the dealer page are 15th Street Surf Shop and Jack's Surf Shop. Zero rests on the brand's own site saying nothing; flagged in NOTE.md.")
R(brand='Danner',own_doors_us=6,outlets_us=0,concessions_us=0,own_doors_world='NC',
  locator_url='https://www.danner.com/store-finder',locator_kind='store locator',
  doors_basis="Locally widget (danner.locally.com, company_id 2266) read via its conversion_data feed from a US-centred query wide enough to return every marker (6212 of n_markers 6212); Danner-named markers: 6 US, 1 JP",
  source=f'Chrome {D}: danner.com/store-finder iframe -> danner.locally.com /stores/conversion_data',
  note="US: Factory Store Portland OR (NE Airport Way, at the factory; not an outlet centre, counted own-door, flagged), Landing Renton WA, Tanasbourne Hillsboro OR, Box Factory Bend OR, Denver CO, Woodinville WA. company_id 2266 also tags 12 unclaimed third-party retailers, so the filter is the Danner name. The W Burnside Portland flagship is not in the locator. World NC: Locally shows one Japan door (DANNER LUCUA Shop, Osaka, company 301140, a separate Danner Japan account) and is not Danner Japan's store list.")
R(brand='Dickies',own_doors_us='NC',outlets_us='NC',concessions_us='NC',own_doors_world='NC',
  locator_url='https://www.dickies.com/en-us/pages/stores',locator_kind='store locator',
  doors_basis='not counted: locator broken',
  source=f'Chrome {D}: /en-us/pages/stores, iframe src, sitemap pages',
  note="Block: /en-us/pages/stores embeds https://hosted.where2getit.com/dickies/index.1116.html, which returns HTTP 404 'Sorry, page not found' (also /dickies/ and /dickies/index.html). stores.dickies.com does not resolve. Pages sitemap holds no store pages (only /pages/stores, /pages/select-your-location and /pages/emea-store-locator-dev). Not a zero.")
R(brand='Frye',own_doors_us=0,outlets_us=0,concessions_us=0,own_doors_world=0,
  locator_url='https://www.thefryecompany.com/pages/store-locator',locator_kind='none',
  doors_basis="brand site publishes no store: /pages/store-locator now redirects to /pages/contact (phone, email, form; no addresses); pages sitemap (32 pages) has no store/visit/boutique page; heritage and shipping pages name no store",
  source=f'Chrome {D}: thefryecompany.com/pages/store-locator, /sitemap.xml pages, /pages/heritage, /pages/shipping',
  note="Zero rests on the brand's site carrying no store and its locator URL redirecting to Contact. Flagged in NOTE.md.")
R(brand='Jos. A. Bank',own_doors_us=185,outlets_us=1,concessions_us=0,own_doors_world=185,
  locator_url='https://www.josbank.com/store-directory',locator_kind='store locator',
  doors_basis="brand's own store directory: 186 stores (/store-locator/<city>-<st>-<id>) in 38 states and DC, none named outlet or factory; street, zip and phone read from each store page's schema.org microdata; 1 of the 186 (Leesburg VA) sits in Leesburg Corner Premium Outlets and is counted as an outlet",
  source=f'Chrome {D}: josbank.com/store-directory (all links read); cross-check josbank.com/store-locator search 02035',
  note="Six store pages return 404 (Walnut Creek CA, Baton Rouge LA, Northborough MA, Portsmouth NH, Appleton WI, Middleton WI); each is still returned by the locator search with an address, so they are counted, not treated as closed. Cross-checks: zip 02035 returned Mansfield, Dedham and Framingham, all in the directory. Search results label stores 'Retail Apparel and Tuxedo rental'. The directory was not reconciled against a full zip sweep. World = US (no non-US doors on the site).")
R(brand='Outdoor Voices',own_doors_us=0,outlets_us=0,concessions_us=0,own_doors_world=0,
  locator_url='NONE',locator_kind='none',
  doors_basis="brand site publishes no store: no locator; footer links Returns, Help Center, About Us, Accessibility, policies only; 18 /pages/visit-us-* pages survive in the pages sitemap, unlinked, 7 empty and 11 descriptive copy only, none with an address, hours or phone",
  source=f'Chrome {D}: outdoorvoices.com footer, /sitemap.xml pages, the 18 visit-us pages, /pages/faq, help-center-other, help-center-returns-exchanges',
  note="Low-confidence zero, flagged for ruling: the visit-us pages are legacy store pages ('drop in once we're open' on Atlanta and Miami) with no address. Nothing on the site says any store is open.")
R(brand='Rancourt & Co.',own_doors_us=0,outlets_us=0,concessions_us=0,own_doors_world=0,
  locator_url='NONE',locator_kind='none',
  doors_basis="brand site names no shop: pages are only /pages/about and /pages/contact; footer has no store link; about page is factory history; FAQ has no visit or store wording",
  source=f'Chrome {D}: rancourtandcompany.com footer, /sitemap.xml pages, /pages/about, /pages/faqs, /pages/contact',
  note="Flagged for ruling: /pages/contact gives Rancourt & Co., 9 Bridge Street, Lewiston ME 04240, hours 9:00am-5:00pm EST. That is the factory; the site does not call it a shop. If you treat it as a factory store this becomes 1 (the Oxxford showroom precedent).")
R(brand='UGG',own_doors_us=10,outlets_us=36,concessions_us=1,own_doors_world='NC',
  locator_url='https://www.ugg.com/our-stores/',locator_kind='store locator',
  doors_basis="own doors from the brand's 'Our Brand Stores' page (10 US, plus Williamsburg NYC marked coming soon, not counted); outlets and concession from the Locally locator (ugg.locally.com, company_id 41445): 47 UGG-named US markers = the 10 + 36 in outlet centres + 1 Macy's Herald Square",
  source=f'Chrome {D}: ugg.com/our-stores/; ugg.com/stores.html -> ugg.locally.com /stores/conversion_data (8776 of 8776 markers)',
  note="Outlet calls on centre type, under the ruling: Ontario Mills, Concord Mills, Great Mall (Milpitas) and The Mill at Jersey Gardens are outlet/value centres; Dawsonville is North Georgia Premium Outlets. American Dream is a mall and counts as own-door. Macy's Herald Square is a branded shop inside a department store, so a concession. World NC: Locally holds 81 UGG-named non-US markers, but its non-US coverage is not the brand's list.")
R(brand='Universal Works',own_doors_us=0,outlets_us=0,concessions_us=0,own_doors_world=6,
  locator_url='https://universalworks.com/en-us/pages/stores',locator_kind='store locator',
  doors_basis="brand's stores page lists London King's Cross, London Soho, Nottingham and a Tokyo shop on the 6th floor of Hankyu Men's (department store, a concession); partnership-stores page lists Lyon, Toulouse and Berlin under the brand's name, run by local operators; none in the US",
  source=f'Chrome {D}: universalworks.com/pages/all-of-our-stores (hub), /en-us/pages/stores, /en-us/pages/partnership-stores',
  note="World 6 = 3 own UK + 3 operator-run Partnership Stores (Shoez Gallery, Lyon; Mr Sunbell Store, Toulouse; Trüffelschwein, Berlin), counted under the operator ruling and flagged. Hankyu Men's Tokyo is a concession, not counted. The page's own text did not render until the US country prompt was answered.")
R(brand='Y-3',own_doors_us='NC',outlets_us='NC',concessions_us='NC',own_doors_world='NC',
  locator_url='https://www.adidas.com/us/y_3',locator_kind='NC',
  doors_basis='not counted: not retried, per ruling',
  source='facts-first 2026-10-10 block record; RULINGS_wave_c_facts_2026-10-10',
  note="Not retried: the 10 Oct ruling says NC stands and adidas.com is not to be retried (the Spectrum thread will read it). Earlier block: adidas.com/us 403 with a robot check; www.y-3.com NXDOMAIN.")
cols=['brand','own_doors_us','outlets_us','concessions_us','own_doors_world','locator_url','locator_kind','doors_basis','captured_on','source','note']
import sys
z=[r for r in rows]
R(brand='Zara',own_doors_us=102,outlets_us=0,concessions_us=0,own_doors_world='NC',
  locator_url='https://www.zara.com/us/en/stores-locator',locator_kind='store locator',
  doors_basis="census of the brand's US locator endpoint (/us/en/stores-locator/search), which returns stores within about 30 km of a point. Two full grids over the lower 48 (0.5° x 0.65°, the second offset by half a step, so the combined gap is about 28 km), flood-filled around every hit, plus Alaska, Hawaii and Puerto Rico points and 72 metro centres: about 10,000 queries, 0 errors, 103 records. One is an employee-only office (500 5th Ave Suite 400, status PROVISIONAL), excluded, leaving 102 customer stores",
  source=f'Chrome {D}: zara.com/us/en/stores-locator search endpoint; sitemap-index checked for a store directory (none)',
  note="Replaces the facts-first floor of 69. 91 mall and 11 street stores in 26 states (no DC store); each is listed in own_doors.csv. 101 of the 102 list a Man section; Greenwich CT (221-225 Greenwich Ave) lists Woman and Kids only. The first grid alone missed 2 (Cherry Creek Denver, Westfield Galleria Roseville); the metro check caught them and the offset grid found nothing further. Residual risk: a store more than about 28 km from every query point; none is known. Puerto Rico points return nothing on the US locator. World NC.")
cols=['brand','own_doors_us','outlets_us','concessions_us','own_doors_world','locator_url','locator_kind','doors_basis','captured_on','source','note']
order=['Birdwell','Danner','Dickies','Frye','Jos. A. Bank','Outdoor Voices','Rancourt & Co.','UGG','Universal Works','Y-3','Zara']
rows.sort(key=lambda r: order.index(r['brand']))
with open('out/return_counts.csv','w',newline='',encoding='utf8') as f:
    w=csv.DictWriter(f,cols); w.writeheader()
    for r in rows: r['captured_on']=D; w.writerow(r)
print(len(rows))
