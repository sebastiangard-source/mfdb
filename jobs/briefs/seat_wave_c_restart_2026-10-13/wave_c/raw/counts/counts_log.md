# working log — door counts (not for return)
## Dickies — 2026-10-10
- /en-us/pages/stores: iframe https://hosted.where2getit.com/dickies/index.1116.html -> 404 "Sorry, page not found"; /dickies/, /dickies/index.html also 404
- stores.dickies.com NXDOMAIN
- sitemap pages: only /pages/stores, /pages/emea-store-locator-dev (EMEA, dev), /pages/select-your-location; no store detail pages
- => NC, block in note
## Birdwell — 2026-10-10
- nav/footer links: shop-all, about-us, contact-birdwell only; pages sitemap has no store/visit page; /pages/authorized-dealers lists ~95 third-party US dealers + 2 AU + Huckberry online, no Birdwell-banner shop; contact page: email/chat only, no address; about-us: no store mention
- => 0 own doors (brand's own site names no store; locator = authorized-dealers page)
## Danner — 2026-10-10
- danner.com/store-finder embeds Locally (danner.locally.com, company_id 2266). Fetched /stores/conversion_data centred 39.8,-98.6 diag 8000 => 6212 markers (n_markers 6212, uncapped); also 11-point sweep total 6206 consistent.
- Danner-named markers: 6 US + 1 JP (DANNER LUCUA Shop, Osaka, company 301140 = Danner Japan licensee, Locally lists only this JP one)
- US: Factory Store 12021 NE Airport Way Suite B Portland OR 97220 (503) 251-1111; Landing 829 N 10th St Suite 200-A Renton WA 98057 (425) 226-6338; Tanasbourne 11010 NE Evergreen Parkway Hillsboro OR 97006 (503) 262-0332; Box Factory 555 NW Arizona Ave Suite 20 Bend OR 97701 (541) 388-1798; Denver 1435 16th Street Denver CO 80202 (303) 623-2628; Woodinville 13620 NE 175th St Suite 110 Woodinville WA 98072 (425) 818-2166
- 12 other company_id 2266 markers are unclaimed third-party retailers (is_claimed 0) — company_id not a brand filter
- no Danner store-list page (/stores, /our-stores etc 404)
- Portland W Burnside flagship not in locator (not asserted closed — not listed)
## Frye — 2026-10-10
- /pages/store-locator now redirects to /pages/contact (phone/email form, no address list); pages sitemap (32 pages) has no store/visit/boutique page; /pages/heritage and /pages/shipping mention no store
- => 0, basis: brand site publishes no store and its locator URL redirects to contact
## Jos. A. Bank — 2026-10-10
- https://www.josbank.com/store-directory lists 186 store pages (/store-locator/<city>-<st>-<id>), 38 states + DC; none named outlet/factory; saved raw/josbank_dir.txt
- cross-check: locator search 02035 returned Mansfield Crossing, Dedham, Framingham — all in directory, no outlet surfaced
- format: all "Retail Apparel and Tuxedo rental" in search results => own-door
## Outdoor Voices — 2026-10-10
- no locator; footer: Returns/Exchanges, My Account, Returns, Help Center, About Us, Accessibility, privacy, Terms — no store link
- 18 /pages/visit-us-* pages in pages sitemap (boston, nashville, dc, dallas, chicago, nyc-flatiron, houston-heights, houston, austin-south-congress, stanford-pop-up, denver, ov-charlotte, ov-philadelphia, ov-minneapolis, ov-atlanta-buckhead, ov-miami, ov-scottsdale, ov-san-diego): 7 render empty (length 1), the rest descriptive copy only; none carries address, hours or phone; "once we're open" wording on Atlanta/Miami
- help-center-other, returns-exchanges, faq: no store/in-person wording
- => 0, low-confidence basis: site publishes no store; flag for ruling
## Rancourt & Co. — 2026-10-10
- pages: only /pages/about, /pages/contact; footer no store link; about = factory history (Lewiston 1967, bought back 2008) no shop; faqs no store/visit wording
- contact: 9 Bridge Street Lewiston ME 04240, 9-5 EST (factory/customer service; not stated as a shop)
- => 0, flag the factory address with hours for ruling
## UGG — 2026-10-10
- ugg.com/stores.html = Locally (company 41445); conversion_data US-centred diag 8000: 8776 markers, 128 UGG-named, 47 US; saved raw/ugg_us.txt
- https://www.ugg.com/our-stores/ "Our Brand Stores": Newbury St Boston (857) 400-8270; South Coast Plaza (714) 551-0750; Powell St SF (415) 329-6077; American Dream East Rutherford (201) 500-2577; Garden State Plaza Paramus (201) 254-8419; Lenox Square Atlanta (404) 537-3660; Michigan Ave Chicago (773) 295-0904; SoHo 79 Mercer (212) 226-0602; 5th Ave 530 5th Ave (347) 696-7900; Mall of America (952) 373-4012 = 10; plus "COMING SOON! Williamsburg, NYC 129 N 6th Street Brooklyn NY 11249 (347) 986-2160"
- Locally adds 36 outlets (all in outlet centres incl. Simon Mills value malls Ontario Mills, Concord Mills, Great Mall, Mill at Jersey Gardens; Dawsonville = North Georgia Premium Outlets) + Macy's Herald Square (concession)
- => US own-door 10, outlet 36, concession 1, coming soon 1
## Universal Works — 2026-10-10
- https://universalworks.com/en-us/pages/stores (store list renders after country prompt; /pages/all-of-our-stores is a two-card hub): London King's Cross, Unit 30 Coal Drops Yard N1C 4DQ +44 (0)20 8036 3352; London Soho, 26 Berwick Street W1F 8RG +44 (0)20 3581 1501; Nottingham, 120-122 Derby Road NG1 5FB +44 (0)115 666 7266; Tokyo, 6th Floor Hankyu Men's Tokyo, 2-5-1 Yurakucho Chiyoda 100-8488 (dept store => concession)
- https://universalworks.com/en-us/pages/partnership-stores: Lyon 10 Rue d'Algérie 69001 (run by Shoez Gallery); Toulouse 6 Rue Temponières 31000 (run by Mr Sunbell Store); Berlin Rosa-Luxemburg-Strasse 28 10178 +49(0) 30 984306063 (run by Trüffelschwein) — operator-run under UW banner => own-door, operator flagged
- => US 0; world own-door 6 (3 own + 3 partnership), concession 1
## Y-3 — not retried per RULINGS_wave_c_facts_2026-10-10 ("do not retry adidas.com"); y-3.com NXDOMAIN on 2026-10-10 per facts-first => NC
## Zara — 2026-10-10
- endpoint: https://www.zara.com/us/en/stores-locator/search?lat=..&lng=..&isGlobalSearch=true&showOnlyPickup=false&isDonationOnly=false&ajax=true — returns physical stores within ~30 km (radius field 30; observed max ~27 km); no radius param honoured (tried radius, searchRadius, distance, maxResults); no store directory in sitemaps (sitemap-pages/help/marketing us-en checked)
- pass 1: grid lat 24.5–49.2 step 0.5, lng -124.8..-66.8 step 0.65, flood-fill 0.25/0.3 around every hit, plus AK (3), HI (5), PR (3) points: 5595 queries, 0 errors, 101 records
- spot check 72 metro centres: +2 (Cherry Creek Denver 12517; Westfield Galleria Roseville 1140) — grid gaps confirmed
- pass 2: offset grid (lat +0.25, lng +0.325): 4361 queries, 0 errors, 0 new; combined lattice max gap ≈28 km
- 103 records, all countryCode US, kind Zara; 1 isOnlyForEmployees (18957 "E_ZA_ESTA EEUU", 500 5th Ave Suite 400, PROVISIONAL) excluded => 102 customer stores; 90 Mall, 12 Street; 101 list a Man section (Greenwich CT 221-225 Greenwich Ave: Woman/Kids only)
- PR queries returned nothing on the US locator (PR stores, if any, sit on another locale) — not counted
