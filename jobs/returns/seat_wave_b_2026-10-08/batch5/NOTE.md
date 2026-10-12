# seat_wave_b — batch 5 (Rapha through Timberland) · 11 October 2026

## Files

- `return.csv`: 10 rows.
- `return_styles.csv`: 1,199 styles.
- `stockists.csv`: 2,271 rows.
- `return_counts.csv`: 8 brands.
- `own_doors.csv`: the running master, 1,288 rows.
- `held_door_counts.csv`: Sperry's row is replaced by the 11 Oct re-read.

All brand names match the canonical keys exactly, no cell is empty, and every store count equals its rows. `NC` (not checked) appears only where a site blocked the read.

## Sperry: re-read as ruled

- **The locator works; there was no 401.** The store list is built into the page itself and never calls the Aldo service that fails on ghbass.com.
- **Doors** are the same as on 8 Oct: 1 own door (Disney Springs) and 3 Tanger outlets, now with the locator's own lat/lon. The four 8 Oct rows were replaced with the fresh rows.
- **Sperry sells no men's clothing.** Its feed has 678 shoes, and its "clothing" is socks. That makes 7 garment slots NONE and shoes $110–200.
- **Owner** is Authentic Brands Group (SR Holdings / Sperry Top-Sider LLC), not G-III. The Aldo Group operates the site and the stores.

## Retry, 11 Oct afternoon

- **Timberland: complete on sections 1–3.** I moved between listing pages by navigating instead of in-page fetching, and nothing was blocked.
  - Prices: all 8 slots filled.
  - Fibre: 66 styles from 155 tiles, every one with a stated composition. 86% natural; shape is `one`, because outerwear is an 8-to-8 tie.
  - Stockists: the www locator lists 12,874 US dealers. 1,440 shops are written as rows; 11,165 doors in chains (Foot Locker, Hibbett, Dick's and others) are summarised.
- **Stockists now total 3,710 rows.**

## Blocked mid-read (original run)

- **Timberland:** PerimeterX challenge (HTTP 403, px-captcha) from page 2 of the men's clothing listing.
  - Prices are from page 1 only (48 of 155 tiles), so they are the lowest and highest found.
  - 18 styles are counted, with composition `NC`.

## Flags for merge

| Brand | Flag | Filed |
|---|---|---|
| Rapha | Boston and Chicago clubhouses are not on the brand's list; Bentonville is | 4 own doors; `worklist_conflict` |
| Rapha | Cycling tights and skinsuits | Category `other` (11 styles); `trousers` is the alternative |
| Rapha | Archive sits in the men's navigation | Counted, never priced |
| Rowing Blazers | 7 styles titled "Cashmere" are 5–10% cashmere | Filed as read |
| Rowing Blazers | Warm & Wonderful | Treated as own sub-line, so priced |
| Salomon | Fleece crew is the only sweater-shaped knit; no chino | Sweater and dress pants NONE |
| Salomon | Shoe low is a Forces-line tactical sandal, $70 | $70 (otherwise $100) |
| Saturdays NYC | Sonic Youth tees: band licence plus limited edition | Excluded |
| Saturdays NYC | The brand is now run by Crosby South (Australia), with no US doors | Positive zero; Crosby St row `closed` |
| Schott NYC | Leather shirts and leather pants | Excluded as overshirts and outside the trouser slot |
| Schott NYC | Outerwear low is a sale item | Regular price $130 |
| Snow Peak | PACAYA shop-in-shop inside an independent store | `concession` |
| Snow Peak | Polyurethane (Japanese label term) counted as stretch | 12 stretch styles (6 without) |
| The Kooples | Each colour has its own article number and handle | Grouped by title plus composition plus price: 260 styles |
| The Kooples | 157 styles carry an Archives markdown inside the navigation | Counted at full price |
| Thursday Boot | Each colour has its own handle | Counted by model code: 36 (177 by handle) |
| Thursday Boot | Flight Jacket has a shearling collar | Excluded from the outerwear high ($399; otherwise $425) |

## Things found

- **Rapha** is held through Carpegna Ltd by Thomas and Steuart Walton (Companies House).
- **Rowing Blazers** is majority-owned by Burch Creative Capital since 2024. Its founder, Jack Carlson, left in March 2025.
- **The Kooples** belongs to Groupe Verdoso since March 2025 (bought from MF Brands), not SMCP or LVMH. Its locator lists 44 own doors in Europe and none in the US.
- **Snow Peak** went private in a 2024 management buyout with Bain Capital. It has a third US store, in Seattle, that the worklist leaves out.
- **Schott's** Union, NJ factory is documented on the brand's own factory tour, so craft is proposed at 4.
- **Salomon** belongs to Amer Sports, with ANTA as largest shareholder. It has 5 own doors and 2 outlets; Woodbury is an outlet by venue.

---

# Per-brand notes


## Rapha: full record, read 2026-10-11 (complete)

**Mark as written:** Rapha. The key stays `Rapha`, and `note` carries `mark_as_written: Rapha`.

**What was checked.** Everything was read in Chrome tab 39485843.
- **Store:** `rapha.cc/us/en_US/` redirects to `/us/en/`. It is a Next.js front end on an Algolia index (`products_en_us`), priced in USD.
- **Clubhouses:** read from the `content.rapha.cc` clubhouse list.
- **Census:** the men's listing (`/us/en/shop/mens`, 813 colourway hits on 14 server-rendered pages) and 239 product pages, fetched one at a time. Nothing was blocked.
- **Prices:** checked on 7 rendered product pages.
- **Ownership:** read from the Companies House PSC registers.

## Own doors (section 4)
- **The list:** the footer link "Find a Store" goes to the clubhouse list. Its payload groups the clubhouses by region: North America 4, Asia Pacific 8, Europe 7.
- **US: 4 own doors, 0 outlets, 0 concessions, 0 pop-ups.**
  - New York, 159 Prince St.
  - "Los Angeles", which is at 1347 4th St, **Santa Monica**.
  - San Francisco, 2198 Filbert St.
  - **Bentonville AR**, 200 E Central Ave. Bentonville is the home town of RZC and the Waltons.
  - All four rows carry the page's own lat/lon.
- **worklist_conflict:** the worklist says "US clubhouses in NYC, Boston, Chicago, LA, SF".
  - **Boston and Chicago are not on the brand's list.** `/clubhouses/boston` returns 404 and `/clubhouses/chicago` redirects to the index.
  - Bentonville is on the list but not in the claim.
  - No closed rows were written, because the locator has no record of the two missing stores.
- **World:** `world_non_us` = 15. That is 14 clubhouses plus one entry named "Mallorca North Pop-Up", which the feed types as a Clubhouse. `own_doors_world` = 18, which is 4 US + 14 and leaves out the pop-up.

## Stockists (section 5)
- The "Find a Stockist" page (Rapha Retail Partners) lists **two US partners**: Mike's Bikes and Landry's Bicycles. Each is shown only as "Multiple retail locations".
- Both are written as rows with the address cells `NC`. See the flags below.

## Prices
- **Tee:** range, $70 (Cotton T-Shirt II) to $140 (Long Sleeve Merino Tee).
- **Dress pants:** single, $175 (Easy Tech Pants, a lifestyle nylon trouser; there is no chino or dress trouser in the main range).
- **Outerwear:** range, $190 (Core Rain Jacket) to $540 (Brevet Gore-Tex Rain Jacket).
- **Shoes:** range, $260 (Road Shoes) to $580 (Pro Team Powerweave Road Shoes). These are own-label cycling shoes; there is no loafer.
- **`NONE`:** polo, dress shirt, jeans and sweater. The only jeans are the Rapha + Hiut collaboration. The only "shirts" are two archive tech shirts.
- **How full prices were chosen:** the men's navigation includes an **Archive** section (174 marked-down colourways). The payload's `wasPrice` usually equals the sale price, so it cannot be used to spot markdowns. Prices were therefore taken only from colourways outside Archive, and each one was confirmed on the rendered page with no strikethrough.

## Fibre (section 3)
- **Coverage:** 236 styles, counted by the 7-character base SKU (colour suffix dropped), from 540 colourways. 234 of them state a composition.
  - The two without one are Pro Team Gilet II and the RCC + Yinka Ilori tee. Their payloads have no materials list, so they are filed as undisclosed.
- **Split:** 80% synthetic, 19% natural, 0% cellulosic.
- **Stretch:** 144 styles have elastane on the main line, 142 of them at 5% or more.
- **Shape: split.**
  - Natural-led: Hoodies & T-shirts (cotton tees, merino tees) and Hoodies & Sweatshirts (93% organic cotton).
  - Synthetic-led: Jerseys, Bib Shorts, Jackets, Gilets, Tights, Skinsuits and Shorts & Trousers.
- **How the kit was mapped:**
  - Jerseys and tees go to tees-polos; bib shorts and shorts to shorts; gilets to outerwear.
  - Base layers go to underwear-swim.
  - Tights and skinsuits go to other.
  - The two items titled "Shirt" go to shirts.
- **Line verdicts:**
  - **Wholly synthetic** (90% or more): Core Collection 14, Brevet 9, Brevet Element 4, Gravel 7, Majority Recycled Materials 37, Pro Team 80 (95% synthetic), Mountain Bike 24 (96%), Road & Gravel 29 (93%).
  - **Mixed:** Lifestyle 30 (60% natural), RCC 25, Special Editions 55.
  - 32 styles sit in no line.
- **Suspicious compositions** (filed as read and flagged in the style note):
  - DAG01XX reads "16 polyester" with no % sign.
  - ASE02XX names the cloth without a fibre on its first two lines.

## Sections 6–13
- **Tech: 4.** Shadow and Powerweave are house names (no mill stated). Licensed fabrics are GORE-TEX/Windstopper, Polartec, PrimaLoft and OCTA.
- **Craft: 2.**
  - No owned or named making was found. The 2025 Impact Report describes suppliers in 18 countries.
  - A country of origin sits in the payload of 235 of 236 styles: VN 111, PT 50, CN 48, ID 24, RO 2.
- **Owner, verified:** the controller is Carpegna Ltd (10898646), which holds 75% or more of Rapha Racing Ltd (04849594). Carpegna's PSCs are Thomas L. Walton and Steuart L. Walton, notified August 2017. Both registers were read on 2026-10-11.
  - Fortune (13 Feb 2026) reports that RZC paused new investments; it reports no sale of Rapha.
- **Quote:** Simon Mottram in Cycling Weekly, 30 Oct 2024. It was read through a fetch summary; recheck the wording against the page.
- **Not reached (NC):** lookbook (`/about-rapha` now redirects to the homepage, where the current campaign is "Against Better Judgement"), Vinted, and the GOTS database search.
- **B Corp:** no, from a directory search.
- **Out of scope but noticed:**
  - Two Women's jackets are tagged Unisex in the men's listing; they were excluded.
  - RCC Membership ($95) appears as a product.
  - The tier-one supplier list URL (rapha.cc/tier-one-suppliers) returns 404.

## Flags for merge
- **Worklist claim vs locator.** Boston and Chicago are absent from the brand's clubhouse list; press suggests they closed. Under the standing rules there are no rows. Bentonville is a fourth US clubhouse the worklist did not name.
- **Stockist chains.** Mike's Bikes and Landry's Bicycles are multi-door bike-shop chains. Rapha gives no door count, so it is unknown whether the 5+ chain rule applies. Both are bike shops, so the register door-one test also needs a ruling.
- **Archive in the navigation.** The census counts archive styles because Archive is a men's navigation node. The standing rule excludes archive stock only when it sits outside the navigation.
- **Cycling garment mapping.** Base layers are filed as underwear-swim, so they are out of the split verdict. Tights and skinsuits are filed as other. If Sebastian prefers tights as trousers, 11 styles move.


## Rowing Blazers: full record, wave B (read 11 Oct 2026)

**What I checked:** rowingblazers.com in Chrome. It is a Shopify store (USD, currency rate 1.0). I read:
- `/products.json`: 767 products over 4 pages; the 5th page was empty
- `/collections/shop-all-mens/products.json`: 532 products
- the 8 men's navigation collections (Sweaters, Rugby, Tees, Polo Shirts, Button Downs, Blazers, Sherpa & Outerwear, Bottoms): 140 handles. Each count matches the count the page states (for example, men-sweaters says 35 PRODUCTS).
- all 140 men's PDPs, one at a time about 1.5–2 s apart. A first pass got about 90 "Failed to fetch" network errors with no 403 or captcha, and a slower retry read all of them.
- /pages/locations, about-us, our-values, FAQ and lookbooks
- off-site: Fashion Dive and Glossy (ownership) and The Rake (quote)

**Section 4 (own doors): 1 US own door, 0 outlets, 0 concessions, 0 pop-ups, 0 non-US.**
- The footer link "Locations" opens a static page titled "New York Store" with one address: 262 Elizabeth St, New York NY 10012.
- The page has no phone, map embed or geo, so lat and lon are `NC`.
- The worklist claim "NYC store" is confirmed.

**Prices (USD, full price; no compare-at prices in the navigation):**

| Garment | Basis | Low | High |
|---|---|---|---|
| Tee | range | $68 | $68 (every own-label tee is $68) |
| Polo | range | $98 Heart Icon Piqué | $148 Cotton Silk Sweater Polo |
| Dress shirt | range (casual oxford button-downs only) | $148 | $188 Franklin garment-dyed oxford |
| Jeans | NONE | | |
| Dress pants | range | $248 Henry Pleated Flannel | $348 Tuxedo Pant (100% wool) |
| Sweater | range (no elevated fibre) | $178 | $348 Donegal Fair Isle Crew |
| Outerwear | range | $298 Madras Anorak | $998 Wool Houndstooth Julian Coat |
| Shoes | NONE | | |

- That is 6 of 8 slots priced. Jeans and shoes are `NONE`: there is no denim and no footwear anywhere in the 767-product feed.
- Excluded from prices: the Winnie-the-Pooh, Babar and Paddington character licences, the Cambridge collegiate licence, and other collabs (Tracksmith, UNO, Magic 8 Ball, Moomin, '47).
- Warm & Wonderful is counted as the brand's own sub-line.

**Fibre census:**
- 119 styles by SKU stem, from 140 colourway handles.
- Composition stated on 119/119.
- Split: 92.4% natural, 6.7% synthetic, 0.8% cellulosic.
- 7 styles have elastane, none at 5% or more.
- Shape `one`: knitwear (35), tees/polos/rugby (41) and shirts (16) are all natural-led. Synthetic shows up only in sherpa fleeces (outerwear, 4 of 8) and mesh or nylon shorts (3 of 3).

Line verdicts, for lines of 5 or more styles:
- all-natural: Winnie-the-Pooh collab (18), Babar collab (12), Harrison rugby fit family (7)
- mixed: Cambridge (7, two polyester), Paddington (6, one sherpa), Warm & Wonderful (5, one sherpa)
- 56 styles sit in no named line.

**Stockists:** none listed. The site has no stockist page (/pages/stockists 404). I filed one `none` row.

**Craft 2 / Tech 1 (proposed).**
- Craft: no maker or mill is named on any PDP, and 25 of 140 PDPs say Portugal. "Vintage looms in Portugal" is a claim, since the factory is unnamed.
- Tech: no named technical fabric.

**Owner:**
- Burch Creative Capital has held a majority since Feb 2024, with co-investors Tom Vellios and Jason Epstein. The brand's own about-us page confirms "part of the Burch family of brands".
- Jack Carlson founded the brand in 2017 with David Rosenzweig. Carlson stayed on as creative director, left in March 2025, and has since joined J.Press.

**mark_as_written:** ROWING BLAZERS (capitals in the logo; page titles write "Rowing Blazers").

## Flags for merge
- **"Cashmere" titles:** 7 styles are titled "Cashmere" (for example, "Cashmere Finance Sweater" and "Babar Cashmere Sweater") but are 90% wool / 10% cashmere, or 95% cotton / 5% cashmere. They are filed as read and flagged per style. The map should not read them as cashmere knits.
- **Western Babar Harrison Rugby:** the PDP gives 90% merino / 10% cashmere, while every other Harrison rugby is 100% organic cotton. It is filed as read and flagged.
- **Heart Icon Piqué Polo ($98 low polo):** the PDP says "FINAL SALE" but it has no compare-at price and sits in the navigation, so it is used at its listed price.
- **Is Warm & Wonderful a sub-line?** I treated it as the brand's own sub-line: separate vendor name, sold in the Rowing Blazers store and men's navigation. If the Spectrum thread treats it as a collab instead, the $298 sherpa and $348 sheep sweater drop out. The outerwear low would still be $298 (Madras Anorak), and the sweater high would stay $348 (Donegal crew).
- **Collabs in the census:** character and collegiate collab styles (43 of 119) are kept in the fibre census, following the Palace precedent, and are out of prices.

Out of scope, noticed:
- The press puts sales at about $25M a year under Carlson (Glossy).
- Sale and archive stock outside the navigation includes cashmere knits marked down 50%. It is out of the census by ruling.


## Salomon: full record, read 2026-10-11

**What was checked.** Everything was read in Chrome (tab 39485845):
- salomon.com `/en-us/` (Next.js, PerimeterX present, no block met);
- Salomon's store locator at stores.salomon.com (Locally.com hosted, company_id 71), linked as "Find a store" in the salomon.com footer;
- the Amer Sports Form 20-F / Annual Report for FY2025.

The proxy refuses direct downloads from stores.salomon.com, so the locator JSON was read in-page and copied out page by page. A SHA-256 check confirmed the copy matches the page.

**Own doors (section 4).** The locator JSON returned 5,379 markers on a US-centred query, 4,280 of them US (1 coded PR). The locator's own store-category filter has two values, OBS "Brand Store" and FO "Outlet Store". A re-sweep on 33 regional centres, including AK, HI and PR, added no US rows.
- **US: 5 own doors + 2 outlets.**
  - Own doors: SoHo (169 Spring St), Upper West Side (270 Columbus Ave), Williamsburg (127 N 6th St), Chicago Bucktown, and Hollywood Melrose.
  - Outlets: Woodbury Commons and Arc'teryx Salomon Ogden Outlet. The locator labels Woodbury Commons a Brand Store, but it sits in Woodbury Common Premium Outlets, so the outlet-centre rule makes it an outlet. The Ogden outlet is co-bannered with Arc'teryx and sits under a separate locator account.
- The worklist claim "NYC store" is confirmed: there are 3 NYC doors.
- Williamsburg has no hours and no inventory data in the feed, so it may be new. It is filed `as listed`.
- Lat/lon on all 7 rows are the locator's own coordinates.
- **World: NC.** The locator does cover the world, but each query returns the nearest ~13,000 dealers, and one European query took about 60 seconds. Partial sightings:
  - Paris-centred: 23 brand stores / 34 outlets.
  - Switzerland-centred: 25 / 35.
  - London-centred: 23 / 34.
  - Shanghai-centred: 12 / 1.
  - Sydney-centred: 9 / 1.
  - Mexico: 18 stores + 6 factory outlets.
  - Whistler: 1.
- The 20-F gives 703 owned retail stores for the whole Amer Sports group. That figure is not used.

**Stockists (section 5).** These come from the same feed, US and PR only, with the 7 own and outlet doors excluded.
- **Chains with 5 or more US doors are summarised here and not written as rows: 75 chains, 2,353 rows.** Chains were grouped by name prefix and by the locator's company_id.
  - DICK'S Sporting Goods 722 (including House of Sport, Warehouse Sale and combo stores)
  - REI 189
  - Sportsman's Warehouse 136
  - Fleet Feet 130
  - Bass Pro Shops 123
  - Tradehome Shoes 104
  - Nordstrom / Nordstrom Rack 89 (department store; company_id 9308)
  - Road Runner Sports 44
  - Christy Sports 42
  - Cabela's 37
  - SCHEELS 35
  - Going, Going, Gone! 34
  - Erik's 31
  - Sun & Ski Sports 31
  - Galls 30
  - Marathon Sports 28
  - Mountain High Outfitters 27
  - Super Shoes 27
  - Rogan's Shoes 25
  - US Patriot Tactical 22
  - Shoe Station 20
  - Gearhead Outfitters 19
  - Brown's Shoe Fit 17
  - Half-Moon Outfitters 17
  - Foot Locker 16
  - BC Surf & Sport 16
  - Sports Basement 15
  - Backcountry 15
  - Four Mountain Sports 13
  - Ski 'N See 12
  - Wheel & Sprocket 10
  - JD Sports 10
  - Big Peach Running Co. 9
  - Great Outdoor Provision Co. 9
  - Kith 9
  - Peter Glenn 8
  - Cripple Creek Bike and Backcountry 8
  - Elliott's Boots 8
  - Tyler's 8
  - Curtis Blue Line 8
  - Read's Uniforms 8
  - Bloomingdale's 8 (department store)
  - Runners Roost 7
  - Buckman's 7
  - Epic Mountain Gear 7
  - Charm City Run 7
  - High Country Outfitters 7
  - Boyne Country Sports 7
  - Shoe Fly 6
  - Walkabout Outfitter 6
  - evo 6
  - Harrison's 6
  - Columbus Running Company 6
  - Cumberland Transit 6
  - Sport Loft 6
  - 5 doors each: Whole Earth Provision Co., Al's Sporting Goods, Gorham Bike & Ski, Foot Traffic, Ski Barn, A Snail's Pace, Birkenstock Comfort Shoes, Pacers, Alabama Outdoors, Sand Dollar Lifestyles, TC Running Company, BlueZone Sports, Surefoot, Base Mountain Sports, Pro Bike + Run, Confluence Running, Sole Sports Running Zone, Pants Store, Eastern Mountain Sports, Atlantic Tactical.
- **That leaves 1,920 rows in `stockists.csv`.**
  - `shop_kind` is a reading of the name, because the locator gives no shop type.
  - The note carries the locator's raw store tags. Only WSE ("Winter Sports Equipment") and FTW ("Footwear") are shown as labels on the page. The other codes are SS / SSF (the sportstyle doors such as The Webster, Undefeated, Dover Street Market, Kith and Concepts), Forces (tactical and uniform shops), PREMIUM, ORApp, SnowApp, BP, AE, NE, SBE, RF and OF; their meanings are unlabelled.
  - Most rows are ski, run and outdoor specialists. Apply the register tests before merging: many sell skis, boots or shoes and no clothing.
  - Resort, club, institution and rental shops are flagged in the note.

**Prices and listing links.** All prices are USD on salomon.com/en-us. On every men's clothing style read, `basePrice` in the PDP payload equals `finalPrice` and the JSON-LD offer, so no markdown was met.
- **Ranges:**
  - Tee $35–$100.
  - Outerwear $150–$750: the ski jacket SCRAMBLER GORE-TEX is the top; on the general Jackets page the top is S/LAB BONATTI INFINITE at $500.
  - Shoes $70–$300.
- **NONE:** polo, dress shirt, jeans, dress pants and sweater.
- Men's shoes were read from the sorted listing only (126 products, which include unisex styles). The low is RX BREAK FORCES at $70, a Forces sandal. The high is TEPIAZ ADVANCED at $300.
- The search URL `/en-us/search?q=` works.

**Fibre (section 3). The census is complete.** It covers 53 styles by model code (LC#####), matching the listing's "53 products" and the sum of the 7 sub-categories (55, with 2 overlaps). There are 110 colourways (article codes).
- Composition comes from each PDP's server-rendered Composition block. All 53 were fetched one at a time and **all 53 state a composition**.
- **17% natural, 83% synthetic, 0% cellulosic.** 17 styles carry elastane on the main line, all at 5% or more.
- **Line verdicts:**
  - **LOGO is wholly natural**: 7 styles, organic-cotton tees and 70/30 organic cotton / recycled polyester sweats.
  - **Wholly synthetic**: SHAKEout (10), Sense Aero (9), Bonatti (4, under 5 so no verdict) and S/LAB (3).
  - The only other natural-led styles are the cotton tees BRANDPLAY and VENOM.
- **Shape: split.** Tees are 8 synthetic-led to 6 natural-led, and the LOGO sweats are natural-led.

**Owner.** Amer Sports, Inc. (NYSE: AS), Form 20-F FY2025.
- ANTA Sports is the largest shareholder; the excerpt read gives no percentage.
- Salomon revenue passed $2 billion in 2025 (+35%).
- Products are "conceived" at the Annecy Design Center.
- About 28% of sourced group product was made in the PRC.
- The filing mentions owned facilities in Austria, France and Germany without naming the brand.

**Not reached:** lookbook, Vinted, Grailed, B Corp and GOTS (all `NC`), and the world own-door count.

**`mark_as_written: SALOMON`**

## Flags for merge
- **Sweater slot is `NONE`.** The only crewneck pullover is a polyester fleece (ESSENTIAL LIGHTWARM, $60), not knitwear. Decide whether a fleece crewneck can stand in for the band rule.
- **Dress pants is `NONE`.** The only trousers are technical (hiking pant WAYFARER 2.0 $110, softshell, rain and ski pants), and there is no chino.
- **Fleece midlayers (6 styles) are filed under category `other`**, not `knitwear`, and the tights (2) also under `other`.
- **Shoes low is a Forces (tactical) sandal**, RX BREAK FORCES at $70. If the Forces line should be excluded, the low becomes RX SLIDE 3.0 ATQ at $100.
- **Woodbury Commons** is filed as an outlet against the locator's "Brand Store" label, under the outlet-centre rule.
- **Ogden outlet** is co-bannered Arc'teryx Salomon and sits under a separate locator account. It is filed as a Salomon outlet; the operator is not stated.
- **SHAKEout HEXAFLOW (LC13944)** has a suspicious composition, filed as read: the pocket-lining line sums to 300%. The main line is unaffected.
- **Owned facility claim is unverified.** The about page still cites the 2019 "Advanced Shoe Factory 4.0" in France; its current status was not verified. Craft is proposed at 2 and tech at 4.


## Saturdays NYC: full record, wave B batch 5 (read 11 Oct 2026)

**Checked:** saturdaysnyc.com (Shopify; the shop is `crosbysouth.myshopify.com`, country AUS, Global-E). I read:
- the full `/products.json`: 352 products on 2 pages;
- the men's collections, which reconcile with the feed: mens-apparel has 210, the feed has 212 clothing handles, and the difference is the 2 orSlow women's pants;
- 95 PDPs, one per article number, 1.5 s apart, for the composition in the Details accordion (it is not in `body_html`);
- the store locator and its 8 store pages, and the wholesale and shipping pages;
- web.archive.org captures of the brand's own locator and the Crosby Street page.

**Section 4 (own doors): positive zero in the US.**
- The live locator (`/blogs/stores`) lists Japan 7 and Australia 1. Of those 8, 7 are own doors and Hankyu Umeda Main Store 8F is a department-store concession. The Japan operator is not stated.
- Crosby Street (31 Crosby St, SoHo) has a `closed` row, with coordinates from the brand's own map pin. It was listed under USA in the 2025-07-12 capture, was gone by 2025-12-06, and its page now 404s.
- worklist_conflict: the worklist says "NYC and LA stores". LA was a 2023 pop-up page. The West Village page was already 404 in 2021.

**Currency:** `Shopify.currency.rate` is 0.69847 with USD active. Even so, the feed prices equal the displayed USD prices on every PDP read, so I filed them as USD. The site sets one figure for USD and AUD ("$300 (USD / AUD)").

**Prices:** all 8 slots are filled, all at full price; no compare-at prices appear in scope.
- **Dress shirt:** casual woven shirts only, filed as a range.
- **Polo:** knit polos only, filed as a range.
- **Sweater:** two crewnecks, neither in an elevated fibre, filed as a range.
- **Shoes:** one own-label sandal at $165, filed as a range with low = high. The slides are Lusso Cloud, a stocked brand.

**Fibre census: 89 men's styles, by article number (SKU stem), from 204 colourway handles. 86 state a composition.**
- Split: 76% natural, 19% synthetic, 1% cellulosic. No elastane; the 1% polyurethane on 3 styles is not counted as elastane.
- Shape: one. Every category with 10 or more styles leads natural.
- Swim: 7 styles, 4 of them synthetic.
- The 3 undisclosed styles are Japanese-denim pants that give only weight and origin.
- Excluded: 3 Sonic Youth licensed-artwork limited-edition tees and 2 orSlow women's pants.
- Kept: the Dickies, Hanes and orSlow collaborations, 9 styles.

**Line verdicts:**
- Made in Japan is all-natural: 14 of 15 disclosed styles, from 18 styles in all.
- Denim is all-natural: 7 of 7 disclosed, from 10.
- Collaborations are mixed: 9 styles, 2 of them synthetic-led (the Dickies poly/wool slacks).
- Miller Standard (3) and Suiting (2) fall under the 5-style line threshold.

**Stockists:** none listed (the wholesale page is enquiry-only).

**Tech 1 / Craft 2 (proposed):**
- No named or licensed tech fabric.
- Made in Japan or Okayama is stated on 22 of 95 PDPs.
- No maker, mill or facility is named.
- Heritage is dated and placed (Aug 2009, Crosby St).

**Ownership:** the store and wholesale are run by Crosby South (Australia), going by the brand's own site. The founders (Tunstall, Rosen, Collett) come from press only.

**Not reached:** Vinted, Grailed, B Corp/GOTS, signature product, pronunciation (all NC).

**mark_as_written:** SATURDAYS NEW YORK CITY (header logotype). Copy writes "Saturdays NYC".

## Flags for merge
- **Sonic Youth tees** were excluded as licensed artwork. The standing rule names character licences, not bands, but the tees are also limited editions.
- **Talley Swim Short** carries three article numbers across seasons (BBS66110, BBS26000, BBS16180). Under the article-number rule that is three styles; the same applies to Danjo (two). Counting by model would give 86.
- **Tee high** is the long-sleeve wool tee ($115). The dearest short-sleeve tee is Brandon Relaxed Wool Tee at $99.
- **Brand is now Australian-run.** The SoHo origin store is closed and there are no US doors. The map may want to reconsider "NYC" positioning.


## Schott NYC: full record, wave B batch 5 (read 11 Oct 2026)

**Checked:** schottnyc.com (Shopify, USD, `Shopify.currency.rate` 1.0). I read the full `/products.json` (438 products over 2 pages; page 3 was empty) and 13 collection feeds. I read the Specs block (Origin / Material / Yarn) on all 277 in-scope product pages, one at a time, 1.5 s apart. I also read the store locator (a Stockist.co widget, full feed of 251 rows), the three flagship store pages, the factory tour, the story page, the contact page and the journal. Outside the store: Grailed and the B Lab directory. No blocks on schottnyc.com.

**Section 4 (own doors): 3 US own doors, 0 outlets, 0 concessions, 0 pop-ups.**
- Stores: New York (32 Howard St), Los Angeles (101 S La Brea Ave #104A) and San Francisco (619 Sansome St). Each is a "Schott NYC" row at priority 1000 in the locator, and each matches a brand store page. Lat/lon are taken from the locator feed.
- The other 248 locator rows are third-party stockists: 224 US, 24 Canada.
- world_non_us is NC. The locator covers only the US and Canada. The story page mentions flagships in Paris and Tokyo, but the locator does not list them, so they are not counted.
- Worklist claim "NYC store": confirmed, and there are also stores in LA and SF.

**Prices (all 8 slots filled, USD; feed prices match the displayed pages):**

| Slot | Basis | Low | High |
|---|---|---|---|
| Tee | pair | $45 | $55 |
| Polo | range | $90 | $90 |
| Dress shirt (casual button-downs) | range | $80 | $100 |
| Jeans | range | $230 | $230 |
| Trousers (in place of dress pants) | range | $120 | $145 |
| Sweater (crewneck) | range | $85 | $140 |
| Outerwear | range | $130 | $1,935 |
| Boots (no loafer) | range | $330 | $330 |

- Outerwear high is P622H, a Perfecto Brand Horween horsehide trucker, as the dearest regular non-shearling jacket. Shearling (257S $1,690, B-6 $1,500), fur- or sheepskin-collar jackets (P656H $1,675 and others), JD1 (a licensed James Dean reissue) and Springsteen curated-collection pieces are excluded.
- Leather jackets carry size upcharges; I filed the base price.

**Fibre census: 277 styles** (by article number; 522 colourways; ratio 522/277).
- 274 have a composition and 3 give a cloth name only (ND).
- Natural 91%, synthetic 8%, cellulosic 0%. Spandex 1 (JN2503, 2% stretch). Shape `one`.
- Synthetic-led styles are nylon and polyester bombers, puffers and vests (17 of 44 in Men's Outerwear) and the nylon-acrylic-wool "Cloud Blend" knits (6).
- Line verdicts:
  - **Perfecto Brand** (16 styles): all-natural, all leather.
  - **Made in USA** (141 styles, half the range): all-natural (140 natural, 1 ND); it covers leather jackets, wool peacoats, tees and jeans.
  - The imported half holds all the synthetics.
- Many compositions name a fibre without a percentage. Leather jackets give the hide type only, and many tees, shirts and nylon jackets say only "Cotton" or "Nylon". Under the Belstaff precedent these count as compositions with `lead_pct` ND.

**Stockists:** 224 US rows from the brand's own locator.
- 220 independent, 3 department stores (single-store independents: Flemington Dept. Store, Hubert's, Robert's) and 1 online only (Revzilla).
- No chain has 5 or more US doors. The largest are Stag (4), Sault (3), Bob's Sport Chalet, Oak Hall, Ramsey Outdoor and Rambler (2 each).
- Two Harley-Davidson dealerships and two clubs (Happy Hollow Club, Midtown Athletic Club) are kept as listed.

**Craft 4 / Tech 1 (proposed):**
- The owned factory is evidenced. The factory tour names Union, New Jersey (2012 to today, the 7th site since 1913), shows each of 10 production steps with photos and video, and says all men's leathers and wool coats are made there. The contact page gives the HQ as 735 Rahway Ave, Union, NJ 07083. The factory page itself gives no street address. No filing was read.
- Horween is named on at least 8 leather styles; Nihon Menpu and White Oak/Cone Mills are named on the jeans.
- 130 of 277 styles say only "Imported" and name no maker, so I proposed 4, not 5.
- Tech: no named or licensed fabric anywhere.

**Not reached:**
- Vinted: the catalog page returned a "Session refresh" interstitial and the brands API ignored the query, so I stopped.
- GOTS: not checked.
- Pronunciation: the brand gives none.
- Ownership comes from the brand's own statement ("family owned and operated"), not from a filing.

**mark_as_written:** Schott N.Y.C. (JSON-LD Organization name, page-title suffix, Shopify vendor field). This matches the 10 Oct ruling.

## Flags for merge
- **Leather shirts.** 5601SH Cowhide Western Shirt ($490; spec style "Shirt-Jacket") and 3601SH Suede Western Shirt ($475) are excluded from the dress-shirt slot as overshirts. If they count, the shirt high becomes $490.
- **Leather pants.** 601P ($910) is excluded from the trousers slot in favour of cloth trousers. If it counts, the trousers high is $910.
- **Sweater basis.** I filed the crewneck range ($85 to $140). The full sweater category reaches $200 (SW2135 yak-blend cardigan) and $210 (F2144 sweater jacket).
- **Outerwear low uses a compare-at price.** 8402 is $130 regular and $70 on sale. The cheapest jacket that is not marked down is 9508 at $150.
- **Archive sale left out of the census.** 15 Schott clothing items sit only in mens-sale and in no category collection.
- **JD1 and 740B left out of the census.** JD1 is licensed and a reissue; 740B is boys' sizes.
- **Suspicious compositions, filed as read:**
  - 9626D: spec tag says Nylon, description says 100% polyester.
  - 213V: spec tag says Cowhide, description says lambskin.
  - 8261DV: spec tag says Nylon, description says cotton blend.
  - SW2372: spec tag says Cotton, description says yak blend.
  - SW2542: named acrylic first, but sibling styles lead with nylon.
  - F1522: the page reads "805 wool".
- **Brand claim vs. product data.** The factory page says all men's leathers are made in Union, but 3 leather flight jackets (A2SM, G1TG, G1S) say "Imported".


## Snow Peak: full record, wave B batch 5 (read 2026-10-11)

**What was checked.** I read www.snowpeak.com, the US store. It runs on Shopify, prices in USD, and `Shopify.currency.rate` is 1.0. The site search at `/search?q=` returns results ("jacket" gave 166).
- **Catalogue.** I read the full `/products.json` feed: 867 products over 4 pages, de-duplicated by id, and the 5th page came back empty. 248 of them are Apparel. I also read the products.json for the Apparel (192), Outerwear (46), Tops (57), Bottoms (32) and Accessories (87) collections.
- **Composition.** I opened all 111 men's product pages one at a time, 1.5 s apart. Composition sits in the page's Materials block, or in the Specs & Features block on older pages. It is not in the feed body.
- **Doors.** I read /pages/visit-our-stores (clicked through each store in its selector) and the Storemapper feed behind /pages/store-locator (user 7305).
- **Other pages.** /pages/our-history and /pages/global.
- **Ownership.** I read the 2024 tender-offer coverage on nihon-ma.co.jp (the result), jpx.co.jp (the delisting watch notice) and fashionsnap.com (the terms).
- **No blocks.**

**Section 4 (own doors): 3 US own doors, 1 concession.**

| Store | Address | Locator coordinates |
|---|---|---|
| Portland (North American flagship and HQ4, with the Takibi restaurant) | 404 NW 23rd Ave | yes |
| Brooklyn | 76 N 6th St | yes |
| Seattle (evo CornerStone campus, Fremont) | 3524 Stone Way N | none |

- **Seattle** appears in the stores-page selector but not in the Storemapper feed. Its lat/lon is NC and no operator is stated.
- **Concession:** PACAYA in Bend, OR. The locator tags it "Shop-In-Shop".
- No outlets or pop-ups are listed.
- **Worklist claim** "NYC and Portland stores": confirmed. The NYC store is in Brooklyn, and the claim misses Seattle.
- **world_non_us is NC.** snowpeak.com's locator covers the US plus 26 Canadian dealers. Japan, Korea, Taiwan and the UK run separate national sites, which I did not read.

**Stockists: 119 US rows.** All come from the brand's Storemapper feed (358 rows: 332 US, 26 Canada). Most are independent outdoor, fly-fishing and bike shops. Five rows are not independents:
- 3 are other brands' own doors: AETHER NYC and Topo Designs Denver and Fort Collins.
- 1 is online only: the Backcountry.com kiosk.
- The 2 Public Lands doors are filed as independent but are a Dick's Sporting Goods banner (flagged).

Five dealer chains have 5 or more US doors, so they are summarised here rather than written as rows (210 locator rows in all):

| Chain | US rows |
|---|---|
| REI | 177 |
| Mountain High Outfitters | 10 |
| Alabama Outdoors | 9 |
| Half Moon Outfitters | 8 |
| Moosejaw Mountaineering | 6 |

Alabama Outdoors includes two rows at the same address (3054 Independence Dr, Birmingham and Homewood). The two Snow Peak stores and PACAYA are excluded from stockists.

**Scope and census.** Snow Peak sells mostly camping gear. Only clothing in the Apparel navigation is counted:
- **Included:** Outerwear, Tops and Bottoms, plus 2 tees that appear only on the Apparel page.
- **Excluded:** 23 women's, kids', dress and skirt styles. This includes the Urake Varsity Print Pullover, which is tagged Womens Apparel. Also out: caps, socks, bags, gloves, wallets, footwear and the Merrell/KEEN collaborations.
- **Result:** **111 styles**, counted by product code (the SKU stem with the size and colour suffix removed), covering 313 colourways.
- **Sale:** the "last-chance" sale collections hold prior-season stock outside the main range and are out.
- **Prices:** no men's style has a compare-at price, so every price is full price.

**Fibre verdict.** 110 of 111 styles state a composition. The one that does not is the Solid & Delta Stake L/S Tee.

| Fibre lead | Styles | Share |
|---|---|---|
| Natural | 49 | 44% |
| Synthetic | 61 | 55% |
| Cellulosic | 0 | 0% |

- **Stretch:** 12 styles carry elastane on the main line, 10 of them at 5% or more.
- **Split range.** Outerwear is synthetic-led (30 of 41) and so are Bottoms (15 of 23). Tops are natural-led (28 of 45).
- **Lines:**

| Line | Styles | Verdict |
|---|---|---|
| Trad Label | 14 | all natural (cotton, linen/wool, cotton/linen) |
| Fly Fishing (SPF) | 18 | 16 synthetic, 2 natural; mixed, just under the all-synthetic bar |
| Epic | 12 | 10 synthetic; mixed |
| Takibi flame-resistant line | 9 | 6 synthetic-led (modacrylic) + 3 cotton/modacrylic denim; mixed |

58 styles sit in no named line.

**Prices (USD).** Exact figures are in `note`.

| Garment | Low | High | Basis |
|---|---|---|---|
| Tee | $40 | $85 | range |
| Polo | NONE | NONE | |
| Dress shirt (casual button-fronts) | $180 | $210 | range |
| Jeans | $160 | $220 | range |
| Dress pants (casual trousers) | $135 | $340 | range |
| Sweater | NONE | NONE | |
| Outerwear | $170 | $1,000 | range |
| Shoes (Mountain Trek Shoes) | $360 | $360 | single |

**Craft and tech.** I propose tech **4** and craft **2**.
- **Tech:** licensed GORE-TEX, PERTEX, PrimaLoft, Polartec and Teijin fabrics, plus the house's own Takibi flame-resistant fabric. Together they cover about 22% of styles.
- **Craft:** the dated Tsubame-Sanjo and Niigata heritage belongs to the gear. Apparel pages name no maker or mill. Only 5 of 111 state a country (3 Japan, 2 Italy), and 7 more say "Japan Fabric".

**Owner (verified).** Snow Peak, Inc. was taken private in 2024 in a management buyout with Bain Capital.
- **Tender offer:** made by BCJ-80 Inc. (whose parent is BCJ-79), at JPY 1,250 a share, from 21 Feb to 12 Apr 2024.
- **Result:** it succeeded with 59.55% tendered, settled on 19 Apr 2024.
- **After the offer:** a share consolidation and delisting from the Tokyo Stock Exchange followed. Tohru Yamai was expected to stay on and hold shares indirectly.
- **Gaps:** I did not read the exact delisting date. The tender-result article does not name Bain; the Bain link rests on the fashionsnap and Nikkei/CNBC reports.

**Mark as written.** `mark_as_written: snow peak` (lowercase logotype; the site's copy writes "Snow Peak").

**Not reached.** Vinted, the B Corp directory and GOTS. A web search of bcorporation.net showed no Snow Peak listing. No lookbook page exists on the US site; there are only seasonal campaign pages such as "The Art of Play".

## Flags for merge
1. **PACAYA (Bend, OR)** is a Snow Peak shop-in-shop inside an independent store. I filed it as a `concession`, but the concession rule speaks only of department-store counters. Should it be a concession or a stockist?
2. **Seattle** is listed on the brand's stores page but not in its locator feed. I counted it as an own door with the operator not stated. It sits on the evo CornerStone campus next to evo Seattle, which is a dealer.
3. **Polyurethane is counted as elastane** (the Japanese labelling term) on 6 main lines. If it is not counted, spandex_styles drops from 12 to 6.
4. **Sweater is NONE.** The house's "Polartec High Loft Fleece Crew Neck Sweater" ($229.95) is a polyester fleece. The alternative is a single $230.
5. **Shoes:** the $19.95 Everywhere Easy Sandals are SS26 festival merchandise. I treated them as a limited item and excluded them. Including them would make shoes a range of $20–$360.
6. **Unisex range.** There is no men's navigation. The garment listing URLs are house category pages that also carry a few women's items.
7. **Public Lands** (2 stockist rows) is a Dick's Sporting Goods banner. It is filed as `independent` because no better shop_kind exists.
8. **Out of scope, noticed:** Snow Peak also runs a US campfield in Long Beach, WA and the Takibi restaurant in Portland. Neither is a store.


## Sperry: full record, wave B batch 5 (read 11 Oct 2026)

**Checked:** sperry.com (Shopify, USD, `Shopify.currency.rate` 1.0). I read the locator at /pages/store-locator and /en-ca/pages/store-locator, plus /pages/store-information. I read the full `/products.json` (817 products over pages 1-4; page 5 was empty; no duplicate ids) and the men's navigation tree. I ran site search-suggest for 10 garment words. I read the men's loafers & oxfords collection, PDPs for Harbor Loafer, Gold Cup Woven Penny Loafer and Harpoon Crush, the Handcrafted in Maine collection, About Us, the Gold Cup page, the Fall Winter Edit, the privacy policy, the terms of service and the market selector. I also checked Grailed, the B Lab directory and Vinted.

**Section 4, own doors: re-read fresh, readable, no 401.** The locator page carries its store list as JSON in the server-rendered HTML: 4 records, each with storeNumber, address, coordinates and storeType. The 4 rendered tiles match it. A zip search (10001) re-sorts the same 4 in the browser and makes no network call. The page never calls the Aldo `store-availability` app proxy that returned 401 on ghbass.com. The count is 1 own-door (Disney Springs) and 3 outlets (Tanger Myrtle Beach, Lancaster and Charleston). The outlets are inferred from the venue, because the locator gives all four storeType "Classic". This is the same set as the 8 Oct read, but I captured it again rather than carrying the old figures. lat/lon come from the locator's own coordinates. The /en-ca locator serves the same 4 US records and no Canadian store. world_non_us is NC because the locator covers only the North America store that Aldo runs.

**Owner (the brief's G-III precedent does not apply):** the privacy policy, effective 23 Sep 2026, names **SR Holdings Inc. and Sperry Top-Sider, LLC, entities within Authentic Brands Group**, as owners of the Sperry IP. It says ABG has "partnered with The Aldo Group Inc." for day-to-day operation of the website and "In-Store Services". The terms name The Aldo Group Inc., Montreal, as site operator. The store rows carry operator Aldo.

**Clothing: none. This contradicts the prompt's "some apparel".** The feed has 678 FOOTWEAR products. Its 70 CLOTHING products are all socks, and its 58 CHILD_CLOTH products are all kids' footwear. Men's navigation has no apparel, and searches for shirt, tee, polo, jacket, sweater, hat, pants, hoodie and shorts return only shoes. That gives seven NONE garment slots, a fibre census of 0 styles, and a return_styles.csv with the header only. Fibre line verdicts: none.

**Shoes (pair) $110 to $200:**
- Low: Authentic Original Harbor Loafer at $110 full price.
- High: Gold Cup Woven Penny Loafer at $200 full price, the dearest regular men's loafer. Three other Gold Cup loafers sit at $195.
- Both prices were confirmed on the displayed PDPs.
- Gold Cup is counted as a regular-range premium line.

**Stockists:** the brand lists none. I wrote one `none` row.

**Proposed craft 2, tech 3.**
- Craft: the about page dates the founding (1935), the patent (1939) and Navy issue (1940), but names no place. Process copy covers the handsewn moccasin, rawhide laces and siped sole. No factory, maker or tannery is named. Only one style states a country: the Made in Maine 2-Eye at $395, 4 colourways, marked down. The about page's "Handcrafted in Maine" for Gold Cup is an unnamed-workshop claim and does not appear in any Gold Cup product copy.
- Tech: Wave-Siping is a house-owned outsole named on 533 of 678 footwear products. 360° Lacing is on 262 and the PLUSHWAVE footbed on 1. OrthoLite (licensed) is on 24.

**Not reached:** Vinted. /brand/sperry resolves to the unfiltered catalogue and the brands API returned 403, so I stopped. There is no lookbook: the Fall Winter Edit is a shop-the-trend page.

**mark_as_written:** SPERRY on the logotype, locator banner and store names. Copy and the vendor field write "Sperry".

**Out of scope, noticed:** the about page names collaborations with Chris Echeverria, Malbon Golf and Todd Snyder. The Sperry x BEAMS PLUS MIL CVO and Sperry x Aritzia are both in the feed, all excluded from prices. The feed product type CHILD_CLOTH holds shoes, so filtering on type alone would mislead.

## Flags for merge
- **The worklist/prompt expected apparel; none exists on sperry.com.** The map should carry Sperry as a shoe-only house, with seven NONE slots like G.H.BASS.
- **Owner differs from the Bass precedent:** Sperry is Authentic Brands Group, not G-III. Aldo operates both sites.
- **Locator now readable while Bass's 401s.** The Sperry count of 1 + 3 rests on a fresh read. Bass stays NC.


## The Kooples: full record, wave B batch 5 (read 2026-10-11)

**What was checked.** `thekooples.com/us/` redirects to **/en/en/**, a WiziShop storefront that runs Global-e for the US. Each price tile carries a merchant-fixed price per market (`data-fp`, e.g. EUR 65 / US $95 / GB £70), and the US figure is the displayed price, so the record is in USD without conversion. The site does not say whether duties are included.

I read the following in Chrome:
- the men's Ready-to-wear listing: 356 tiles via `?page=8`. Paging is cumulative (page N contains pages 1–N), and page 9 resets to page 1.
- its six sub-categories
- all 337 clothing PDPs: JSON-LD `sku`, `p.product-cs-composition`, and US `data-fp`
- the store locator
- the About, Terms, FAQ and Lookbook pages

Ownership comes from the Autorité de la concurrence (5 Mar 2025) and Modaes (27 Jan 2026).

**Section 4 (own doors).** This is a positive zero: no US door of any format. The locator's country selector offers 9 European countries only. The `/fr/fr/ajax_generate_xml_map.php` endpoint at a 20,000 km radius returns 158 unique stores, none in the US.

| Format | Doors | By country |
|---|---|---|
| Own-door | 44 | France 41, Spain 1, Luxembourg 1, Switzerland 1 |
| Concession | 96 | Printemps, Galeries Lafayette, El Corte Inglés, Brown Thomas, House of Fraser, PKZ and others |
| Outlet | 18 | |

- I inferred formats from the store names, because `magasin_type` is 0 on every row.
- The `/en/en/shop.php` page the US customer sees returns only 8 of the 158 stores, because its store database is scoped. The `/fr/fr/` endpoint gives the full list.
- `worklist_conflict: US stores`. The worklist `why` says "US stores" and the brand's locator shows none.

**Stockists.** None listed. The locator carries only The Kooples' own doors, corners and outlets. I wrote one `none` row.

**Prices (USD, full price; collaborations and marked-down Archives items avoided).**

| Garment | Low | High | Basis |
|---|---|---|---|
| Tee | $95 | $135 | pair |
| Polo | $150 | $195 | range |
| Dress shirt | $215 | $275 | range |
| Jeans | $245 | $260 | range |
| Dress pants | $230 | $415 | range |
| Sweater | $230 | $415 | pair |
| Outerwear | $465 | $1,095 | range |
| Shoes (loafer) | $545 | $545 | single |

- **Tee:** cotton/poly Mixed tee, then the 100% cotton tee.
- **Dress shirt:** the formal shirts are all $215, and the high is the corduroy shirt.
- **Dress pants:** the low is a grey wool suit pant whose JSON-LD EUR price (145) looks like a reprice. Its siblings are EUR 195 / $245.
- **Sweater:** the entry crewneck is already 55% silk, so the high is the dearest regular crewneck, a merino cable knit.
- **Outerwear:** the high is a lambskin coat. The bomber with a reverse-sheepskin collar was not used.
- **Shoes:** three loafers, all $545.
- **Search** is a JS overlay (`/en/en/#search=shirt` gave 139 results).

**Fibre verdict.** Each colour has its own article number and URL, so I counted styles by title with colour words removed, matched on the same composition and the same US price: **337 colourways became 260 styles** (`title_dedup`). Composition is stated on all 260.

- **Natural-led overall:** 89% natural, 5% synthetic, 6% cellulosic. Shape is `one`.
- **Elastane:** on the main line of 37 styles; 5% or more on 2.
- **No category is synthetic-led:**
  - Outerwear is 31 natural of 41.
  - Shirts are 24 natural and 11 viscose or lyocell of 35.
- **Lines:**
  - *What Is* (12 styles) is all-natural (100% cotton).
  - *Denim* (10) is all-natural.
  - *Iconics* (36) is mixed: 33 natural, 2 synthetic, 1 cellulosic.

**Craft and tech.** I propose craft **2** (low confidence; close to 1) and tech **1**.
- **Craft:** no owned facility, maker or mill is named, and no PDP states a country in page text. Every PDP links a Fairly Made traceability showcase (AGEC law), but it is JS-rendered and I could not read it.
- **Tech:** no named technical fabric anywhere. 205 of 260 styles carry the ACT eco label.

**Ownership.** The prompt's hypothesis is not supported.
- **The Kooples is not part of SMCP (Maje/Sandro) and not LVMH-backed.** Groupe Verdoso, a French investment group founded by Franck Ullmann, took sole control of The Kooples Production SAS. The Autorité de la concurrence cleared the deal on 5 March 2025.
- The seller was MF Brands (formerly Maus Frères), which had owned the brand since 2019 (Modaes).
- Founded in Paris in 2008 by "the Elicha brothers" (the about page gives no first names).

**Mark as written.** `mark_as_written: THE KOOPLES` (all-caps logotype; the copy writes "The Kooples").

**Not reached.**
- **Vinted:** /brand/the-kooples served a generic catalogue.
- **B Corp:** the directory query was not applied.
- **GOTS:** no claim on the site, and no organic fibre in any composition.
- **Fairly Made showcases:** JS-only, so not read.

## Flags for merge
1. **Archives markdown inside the RTW navigation.** 157 of the 260 styles show a markdown on the US listing. They are in the men's Ready-to-wear navigation, so they are in the census at their compare-at prices. A separate Archives/men node (416 items) was not counted. If the map wants current-season only, the census would be about 103 styles.
2. **Style method.** The Kooples gives every colour its own article number and URL, so the handle rule does not collapse colourways. I used title dedup instead. "Mixed plain T-shirt navy blue" stayed separate from its three "Mixed T-shirt, straight, plain" siblings because the titles differ.
3. **Two suspicious compositions filed as read:** "100% Merino Wool, 4% Polyamide, 1% Elastane" (sums to 105) and "100% Merino Wool, 10% Cashmere" (sums to 110).
4. **Concession and outlet formats are inferred from the store names.**
   - Brown Thomas Dublin, House of Fraser Glasgow and PKZ Zurich are coded as concessions.
   - One Nation (an outlet centre near Paris) is coded as an outlet.
   - Nice airport is coded as an own door. Its operator was not stated.
5. **Currency.** USD comes from Global-e fixed US prices. Whether duties are included (`USD_landed`) is not stated anywhere on the site.

Out of scope but noticed: the store's footer links a Fairly Made AGEC traceability index (PDF, updated September 2026).


## Thursday Boot: full record, wave B batch 5 (read 2026-10-11)

**What was checked.** I read the US store at thursdayboots.com. It runs on Shopify, prices in USD, `Shopify.currency.rate` is 1.0, and the country is US. No men's record carries a `compare_at_price` (the house tags itself "honest-pricing"), so every price is a full price. I read eleven collection feeds (`/collections/<handle>/products.json`): men's jackets, shirts & apparel, shirts, sweaters, men, boots, shoes, loafers, sneakers, dress shoes and warehouse. I also used `/search/suggest.json` to look for tees, polos and trousers. Composition comes from the feed `body_html` feature bullets. One product page was read in full (Oxford Shirt), and it carries no percentage composition beyond the bullets. Other pages read: Our Story, Our Product, Our Values, the FAQ, the León page, the Goodyear welt guide and the pages sitemap. Outside the store I read the brand's own blog founder interview (blog.thursdayboots.com), Grailed, and Vinted, which returned a 403.

**Section 4** was not re-read. Counts were carried over: 5 own doors in the US and 5 worldwide, with 0 outlets and 0 non-US. While moving between pages, the tab loaded `/pages/locations` once by mistake. Nothing on it was read or used.

**Stockists.** The brand lists none. There is no stockist or retailer page in the navigation or the pages sitemap. The FAQ lists only the brand's own verified channels: its site, an Amazon store, Facebook and Instagram shops, and a resale store. The file has one `none` row.

**Fibre verdict.** 36 styles from 177 handles. The range is one cloth story:
- 33 styles natural-led (92%), 1 cellulosic-led (3%, the Chambray Workshirt at 70% Tencel and 30% linen), 0 synthetic, and 2 undisclosed.
- The two undisclosed styles are the Waxed Trucker and Ranger jackets, which give only "waxed canvas from Halley Stevensons".
- 1 style contains elastane on the lead colourway (Mechanic Jacket, 2%).
- Natural-led categories: Jackets (23 styles, mostly leather and suede), Shirts (11, cotton and linen), Sweaters (2).
- The house names no lines with five or more styles.

**Prices.** Four garments are filled; the rest are `NONE`.

| Garment | Low | High | Basis |
|---|---|---|---|
| Dress shirt | $98 (Oxford) | $128 (Japanese-flannel Buffalo Check) | range, casual button-downs only |
| Sweater | $108 (Ribbed Crewneck) | $148 (Highland, superfine merino) | range |
| Outerwear | $120 (Denim Trucker) | $399 (Motorcycle Jacket, lambskin) | range |
| Shoes | $168 (Handsewn Loafer) | $188 (Lincoln penny loafer) | range |

- **`NONE` slots:** tee, polo, jeans and dress pants. The only trousers on the site are "Thursday Threads" goods from Kato and Unbranded. These are third-party: the vendor field says so, the Kato pages say "Made By Our Friends at Kato", and Kato fulfils the orders. They are out of the census and out of prices.
- **Outerwear exclusions:** Bronco ($689) and Stallion ($649) are shearling. Flight Jacket ($425) has a shearling collar. Alpha M Bomber is a collaboration. The Varsity "10 Year" colourways are anniversary editions.
- **Exotic skins:** none in 314 men's footwear records. Boots run $199–$549, and the top is Shinki horse cordovan, which is not exotic.

**Craft and tech.**
- Proposed craft is **3**. Mills and tanneries are named on product pages: Halley Stevensons, Horween, Shinki, C.F. Stead, Seidel, Badalassi and Wickett & Craig, plus Le Farc on Our Product. The Goodyear welt process is documented.
  - What is missing: no maker is named. Our Story's "investing in our own manufacturing facility" names no place, so it is a claim and not evidence. Production is placed only by city: León, Porto, Alicante and Arkansas.
  - Apparel states a country on 18 of 177 handles (Portugal 16, Turkey 2).
- Proposed tech is **2**. Footwear has owned names: StormKing, WeatherSafe suede and the Thursday Chrome tannage. Apparel has one licensed insulation (Loftherm, on the Varsity only).

**Contradictions with the worklist or record.** The worklist reads "shoes" for what the brand sells. The site also sells a 36-style men's apparel range: leather jackets, fabric jackets, shirts and sweaters. The worklist "why" ("NYC store") is consistent with the carried count.

**Mark as written.** `mark_as_written: Thursday Boot`. The site writes "Thursday Boot Company", and the tail is dropped per the 8 Oct ruling. Key kept.

**Not reached / NC.**
- **Vinted:** the brand page served a generic catalogue, and `/api/v2/catalog/brands` returned HTTP 403. I stopped there.
- **GOTS:** not checked. The site claims organic cotton but names no certifier.
- **`quote_date`:** NC, because the blog post is undated.
- **Lookbook:** none found.

Status is `partial`.

## Flags for merge
- **Style method:** each colour has its own handle and its own SKU, built as a colour prefix plus a model code (BLKRACR, TBKRACR and so on). Neither the article number nor the handle identifies a style, so I counted by the model code after the colour prefix: 36 styles. A literal handle count (the 11 Oct ruling) would give 177. Please rule.
- **Buffalo Check:** I split it into two styles. Both share code BFL, but they differ in price ($98 and $128), cloth (organic cotton and Japanese flannel) and the feed's loop group.
- **Ranger Jacket:** the feed's loop tag groups it with the Station Jacket, but it has its own name and code (DCK), so I kept it separate.
- **Compositions that vary by colourway:** Denim Trucker (77/23 cotton/lyocell against 100% cotton), Forever Flannel (100% cotton against 50/50 and 60/40 cotton/rayon) and Everyday Button-Down (the Light Grey colourway is 62% polyester, 33% rayon and 5% spandex). Each style row carries the first colourway's composition.
- **Suspicious composition:** the Oxford Shirt claims "2-Way Stretch" but names no elastane. It is filed as read, with no elastane.
- **Flight Jacket:** it has a shearling collar on a leather body. I treated it as fur-on trim and left it out of prices. If it is allowed, the outerwear high would be $425.
- **Sweater high:** the Highland Sweater's neckline is not stated as a crew.

**Out of scope but noticed.** The site also sells women's footwear and jackets, bags, belts, socks, a resale store ("ReBoots"), and the third-party "Thursday Threads / Thursday Friends" goods. The founders are filed from the brand's own blog (Nolan Walsh and Connor Wilson); a Stitchdown interview title names Connor Wilson as founder too.


## Timberland: full record, first read 2026-10-11 (blocked after page 1), retried 2026-10-11 (status partial: search_url, lookbook, GOTS, world doors NC)

**Mark as written:** Timberland. The note carries `mark_as_written: Timberland`.

## Retry, 2026-10-11

**Access.** Every timberland.com page was reached by tab navigation, at least 5 s apart, with no `fetch()` on timberland.com (the vans.com method). No challenge was served at any point: men's clothing listing pages 1-4 (155 of 155 tiles), 66 product pages (one per style), the men's footwear and Shoes listings, the loafer PDP, the Timberland PRO workwear listing and the store locator. The first pass's 403 came from an in-page `fetch()` of page 2; navigation does not trip it.

**Prices (all eight filled, USD, full price; exact figures are whole dollars).**
- Tee: $30-70, range (Elements Graphic Tee to Heavyweight Long-Sleeve Waffle T-Shirt). **Tee-high URL check:** the $40 Shorewood Heavyweight Short-Sleeve T-Shirt URL resolves, $40, 100% organically grown cotton. It is the dearest short-sleeve tee but no longer the filed high.
- Polo: $40-70, range (Oyster River SS polo to Long-Sleeve Rugby Polo).
- Dress shirt: $75-85, range. Timberland makes no dress shirt, only casual woven button-ups (Indigo Check shirts, Denim Pocket Shirt). Overshirts are excluded.
- Jeans: $80-90, range (Straight to Relaxed; Baggy and Carpenter also $90).
- Dress pants: $60-70, range. There is no dress trouser, so chinos are used: Topsfield Twill Chino to Sandown Cavalry Twill Pant.
- Sweater: $60, single. The Williams River cotton crewneck is the only sweater.
- Outerwear: $85-700, range (Coach Jacket to Wenham Leather Field Coat). The Wenham in cotton is $260, so the Wenham is also a same-style pair. This supersedes the first pass's $120-600 from page 1. Shacket and overshirts are excluded.
- Shoes: $160, single. The Authentic Loafer is the only loafer among 37 men's Shoes tiles.
- **Timberland PRO:** counted as a sub-line labelled PRO, identified by its `/timberland-pro/` breadcrumb and the PRO mark. Its men's workwear listing (201 tiles) is all footwear plus 2 care items and a hat, so PRO has no clothing and no loafer and changes no cell.
- Only markdown seen: Wharf River Waffle Hoodie ($70 list, $49.99 sale), not used.

**Fibre (full census; replaces the 18-style partial).**
- 155 tiles collapse to 66 styles by product code (ID minus 3-character colour code), ratio 155/66. Baggy Denim Pant (TBC0YHAR, TBC0YHEX) and Indigo Check shirt (TBC0YH82, TBC0YH81) carry two codes each and are counted separately.
- 66 of 66 state a composition in the PDP Product Detail bullets: 57 natural-led (86%), 9 synthetic-led (14%), 0 cellulosic-led.
- Stretch: 3 styles carry elastane (1-3%), none at 5% or more. The Quick-Dry Stretch Cargo Pant is 56% polyester / 44% elastomultiester, which is not elastane.
- By category: tees-polos 16/16 natural, sweats 17/17, shirts 6/6, denim 5/5, knitwear 1/1, trousers 4 natural + 1 synthetic, outerwear 8 natural + 8 synthetic.
- Shape `one`: outerwear is a tie, so no 10+ category is synthetic-led.
- **Line verdicts:** the house's title series (Shorewood, Exeter River, Wareham, Oyster River, Weatherline, Wenham, Northwood, Axis Peak, Rindge, South Cabot, Wharf River) each hold 2-3 styles. None reaches 5, so there are no line verdicts. As read: Weatherline and Axis Peak are all nylon; Wenham is cotton, cotton/nylon and leather.
- **Flagged compositions (filed as the Fabric Composition line):** 3 denim pants and the Denim Pocket Shirt also carry a stray "Made with 100% recycled nylon" bullet. The Rugby Polo Sweatshirt (80/20 cotton/poly) and Sandown Cavalry Twill Pant (97/3 cotton/elastane) also carry "100% Organically grown cotton".

**Stockists (www locator dealer check).** The www store locator (SOCi, hosted.meetsoci.com/timberland, embedded at /en-us/store-locator) lists authorised resellers and Timberland PRO dealers alongside Timberland stores. Read by state through the locator's own endpoint:
- 12,874 US rows. 75 are Timberland stores and outlets (23 + 52 by icon), which matches the 21 + 54 on file; doors were not touched.
- The other 12,799 rows were split as follows:
  - 11,165 doors in dealer chains with 5+ US doors, summarised below and not written as rows.
  - 32 non-shop records (freight forwarders, consolidators, distribution centres, e-commerce and receiving addresses), dropped.
  - 1,440 shop rows written to stockists.csv after merging exact duplicates (the same shop listed as both reseller and PRO dealer).
- Chains are grouped by normalised name plus a keyword merge of obvious variants (e.g. "Des Moines Scheels" goes to Scheels). Grouping is approximate, so some single-door rows may belong to small chains.
- Dealer chains, US doors: Foot Locker 1,142; Hibbett Sporting Goods 871; Dick's Sporting Goods 714; Journeys 672; Macy's 663; Rack Room Shoes 546; DSW 515; Shoe Carnival 438; Footaction 393; Kids Foot Locker 368; Grainger 337; Dillard's 333; Nordstrom 275; Champs Sports 270; Olympia Sports 249; Boot Barn 207; Meijer 202; Finish Line 197; Tradehome Shoes 152; Off Broadway 140; Brown's Shoe Fit 137; Shoe Sensation 133; The Athlete's Foot 127; Super Shoes 91; Shiekh 90; Rogan Shoes 88; K&G 81; Academy Sports + Outdoors 79; REI 73; Downtown Locker Room 65; Cintas 65; Jimmy Jazz 50; Work 'n Gear 46; Robert Wayne Footwear 45; Boscov's 43; Blain Supply 36; Vanderbilt's 32; Von Maur 31; Warehouse Shoe Sale 29; Lady Foot Locker 28; Shoe City 28; Scheels 28; City Gear 26; Saf-Gard Safety Shoe 26; Work World 25; Expressions 24; Saks Fifth Avenue 23; Cavender's 22; Rochester Big & Tall 21; Shoe Station 20; Bloomingdale's 20; Eblen's 20; Bob's Stores 20; City Blue 20; French's Shoe Store 19; Elliott's Boots 19; Dr. Jays 18; Hayes Shoes 17; Buchheit 17; GB Shoes 16; Sports Sensation 16; Stride Rite 16; Shoeteria 15; Schuylkill Valley Sports 15; Theisen's 14; Lenny's Shoe & Apparel 14; TNT Fashions 14; Coastal Farm 14; Casual Male 14; Whistle Workwear 14; Jax Outdoor Gear 14; Bomgaars 13; Gellco 13; Sports Addition 12; Sneakers 12; Work Boot Warehouse 11; Ritz Safety 11; Barebones Workwear 11; Legends 10; Houser Shoes 10; and 64 smaller chains of 5-9 doors (Beck's Shoes, Boot World, Family Footwear Center, Sneaker King, Hyper Active, Runnings, Bootleggers, Peltz Shoes, D&B Supply, E. Edwards Workwear, Vanderloop Shoes, Buster Brown Shoes, Vulcan Safety Shoes, Nokomis Shoe, Home of Economy, Ramsey Outdoor and others).

**Also updated:** named_makers, named_mills and made_in_stated_share. No maker, mill or country appears on 66 PDPs; bullets say "Imported" only. Proposed craft stays 2 and tech stays 2. Tech: no owned fabric technology on clothing; TENCEL is licensed.

**Still NC:** search_url, own_doors_world, lookbook (4 cells), GOTS (2 cells). Not attempted on this retry.

## Flags for merge (retry)
- Tee high moved from $40 (short-sleeve) to $70 (long-sleeve waffle tee) under the `range` rule. If the map wants the short-sleeve staple only, the high is $40 Shorewood (URL verified).
- The stockists file is large (1,440 rows) and the locator data is noisy: duplicate shop names and misspellings as SOCi holds them. Merge may prefer to keep only the chain summary.
- Outerwear category is an exact 8/8 natural/synthetic tie. The standing rules do not say how a tie reads for `shape`; it is filed as `one`.

## First pass (earlier 2026-10-11, superseded where the retry says so)

**Mark as written:** Timberland. Page titles write it that way and the store directory writes "Timberland®". The note carries `mark_as_written: Timberland`. I did not read the header logotype as text.

## The block
- www.timberland.com runs on VF's Nuxt 3 "nora" front end with Bloomreach search, behind PerimeterX.
- Page 1 of the men's clothing listing (`/en-us/c/men/clothing-10049`) loaded in the tab with its server-rendered data: 48 of 155 tiles.
- My first in-page fetch of `?page=2` returned HTTP 403 "Access to this page has been denied" with a px-captcha challenge. Following the spec, I stopped timberland.com for the rest of the run.
- Not reached as a result: pages 2–4, all product pages, compositions, footwear, Timberland PRO, site search and the www store locator.
- An earlier navigation to a guessed URL (`/c/mens/clothing`) gave the site's 404 page ("The Timberland vault is locked"). That was a wrong path, not a block.

## Prices (sections 1–2)
- **USD confirmed:** the feed's `currency: USD` matches the displayed prices ($130 Strafford jacket, $30 Elements tee).
- **Every figure comes from page 1 only.** Lows are the lowest found there and highs the highest found there.
- **Tee:** $30–40.
- **Polo:** low $70 (Long-Sleeve Rugby Polo).
- **Jeans:** low $80 (Straight Denim Pant).
- **Outerwear:** $120 (Winnick shell) to $600 (Stratham Leather Bomber). The price facet shows 2 tiles at $500–999, so one dear tile is unread.
- **NC:** dress shirt (Shirts filter: 7 tiles), dress pants (only a canvas carpenter pant seen), sweater (Sweaters filter: 1 tile), shoes.
- **Category filter on the 155 tiles:** T-shirts 42, Sweatshirts 40, Jackets & Outerwear 36, Pants & Shorts 24, Shirts 7, Polos 5, Sweaters 1.
- **Listing links come from the menu data.** The men's nav has only T-shirts, Jackets & Vests, Sweatshirts & Hoodies and Bottoms. Polo, dress shirt and sweater therefore point to the men's clothing parent.

## Fibre (section 3)
- **Not read.** I found no line verdicts.
- `return_styles.csv` holds 18 styles from the 48 tiles read. A style is the product ID minus its 3-character colour code, e.g. TBC0YHF2 + CM9/P47/546/CN1.
- Composition is `NC` throughout. `pure` and `single_fibre` also carry `NC`, which is outside their enums; it was used because nothing was read. The category is derived from the title.
- **Timberland PRO:** it is sold on the same store under the Timberland PRO mark (`/en-us/c/timberland-pro/mens-workwear-10178`). Under the sub-line rule it would count, labelled as PRO. No PRO tile appeared in the 48 read, and the PRO pages were not reached.

## Doors (section 4)
- Carried as given: 21 own doors and 54 outlets (US); world NC. The locator was not re-read.
- VF's FY2026 10-K cites "147 VF-operated stores" for Timberland. That is a filing, so it is noted here only and is not a door source.

## Stockists (section 5)
- 1 NC row. locations.timberland.com lists only Timberland stores.
- I could not check whether the www locator lists authorised dealers because of the block.

## Sections 6–13
- **Owner:** VF Corporation (10-K for the fiscal year ended 28 March 2026). Timberland and Timberland PRO are managed as one operating segment in Outdoor from Q1 FY2026.
- **Craft: proposed 2, provisional.** The 10-K sources products "primarily" from about 216 independent contractor factories, mainly in Asia, and names no owned plant. I did not reach Item 2 (Properties).
  - Heritage is dated and placed: 1952 Abington Shoe Company, Nathan Swartz, Newmarket NH, the 1973 boot.
  - Process is partly documented: injection moulding, and LWG silver/gold tanneries (Timberland co-founded the LWG in 2005).
  - The source for the heritage and process facts is timberland.co.za, run by the South African distributor (Keystone Apparel). It is not the US brand site.
- **Tech: proposed 2, low confidence.** The only evidence is listing facets: Waterproof 6, Insulated 16 and Water-resistant 12 of 155 tiles.
- **Quote:** the house line on vfc.com.
- **Signature product:** the Premium 6-Inch Waterproof Boot.
- **Grailed:** 8.1k listings.
- **Vinted:** brand id 44.
- **B Corp:** no. The directory search returns only consultancies naming Timberland as a client.
- **GOTS:** NC.
- **Lookbook:** NC.

## Flags for merge
- **The whole price, link and fibre layer needs a re-run on timberland.com from a fresh session.** In that session, navigate between listing pages and do not `fetch()`, because PerimeterX challenged the fetch.
- **The tee-high URL ($40 Shorewood Heavyweight tee) was built on the listing's slug-ID pattern and not opened.** It needs one check.
- **Founding place:** the pages I read do not state where the Abington Shoe Company started in 1952. Only the later move to Newmarket NH is stated.
