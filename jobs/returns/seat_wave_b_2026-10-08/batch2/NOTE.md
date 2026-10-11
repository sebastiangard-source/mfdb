# seat_wave_b — batch 2 (Clarks through G/FORE) · 11 October 2026

## Files

- `return.csv`: 10 rows, 132 columns.
- `return_styles.csv`: 2,196 styles.
- `stockists.csv`: 522 rows.
- `return_counts.csv`: counts for the 5 brands whose stores were read here.
- `own_doors.csv`: 1,105 rows from batch 1 plus 124 new, 1,229 in all. This is the running master.
- `held_door_counts.csv`: unchanged since the batch 1 rulings.

All brand names match the canonical keys exactly (reconcile.py). No cell is empty, every value is from its allowed list, and every store count equals its own_doors rows (held and closed rows are not counted).

## Batch 1 rulings of 11 October, applied

- **Belstaff outerwear high** is now the Trialmaster Panther Jacket in Dark Dusty Taupe, $2,095. The feed price was checked, and the product has no compare-at price and no Phoenix tag. The $1,975 Panther ICON carries the Phoenix tag and is excluded.
- **Hoka Orlando and Las Vegas** are outlets, giving 12 own doors and 4 outlets. Ariat Gretna was already an outlet.
- **Moose Knuckles:** the duplicate Las Vegas row is dropped, so the count is 3 outlets.
- **Standing rules are now in the agents' spec:** shearling and fur, capsules and limited editions, licensed lines, counting styles by article number, outlet centres, held rows, duplicates, filings, craft evidence, dealer chains, and the meaning of own_doors_us and own_doors_world.

## Rulings needed

| Brand | Question | What was filed |
|---|---|---|
| Clarks | Both tees carry a "Limited Edition" badge. Clarks sells no other tee. | Tee `single` $30, flagged. The alternative is NONE |
| Clarks | Styles: counted by handle (3) or by article number (10)? Clarks gives each colour its own article number. | 3 by handle, treating the article numbers as colourway codes. Same fibre verdict either way |
| Columbia | Collegiate and pro-team product (410 + 78 products) | Excluded as licensed lines |
| Columbia | Columbia-branded goods made by licensees (graphic tees, golf, underwear; 207 styles) | Included. They move natural from 22% to 41% and set the $18 tee and $40 polo lows |
| Converse | Pony hair as hair-on hide under the fur rule | Excluded. Otherwise the shoe high is $130 |
| Crockett & Jones | $670 Teign suede low: possibly an unmarked reduction | $670 filed. The next consistent regular price is $750 |
| Crockett & Jones | Craft 5 or 4: driving shoes are Made in Italy, maker not named | 5 |
| Emporio Armani | "Giorgio Armani Honolulu Ala Moana" row inside the EA directory | `held` |
| Emporio Armani | Jeans high: $575 DENIM LAB, which may be a special line | $545 |
| Emporio Armani | Dress pants low: the $445 product is titled "chinos" | $445. The clean dress trouser is $595 |
| Emporio Armani | Outerwear high | $2,995 wool coat. Alternative: $2,195 cashmere |
| Fjällräven | G-1000 (65% polyester) reads synthetic-led on 69 styles | Filed as read. A map note may be wanted |
| G/FORE | Dress shirt: the category is mostly knit piqué | `single` $325 flannel overshirt, the only woven shirt |
| G/FORE | Polo high: Cooling Cotton Sweater Polo, listed under polos | $350. Without it the high is $185 |
| Fred Perry | Craft 3 rests on the Made in England line (about 9 styles) | 3 |

## Things found

- **G.H. Bass stores are `NC`, not 0.** The brand's store locator returns `401 Unauthorized` for every country, so the stores could not be checked. The site's privacy policy names G-III Apparel Group as owner (G.H. Bass IPCo LLC), and ALDO U.S. operates the site, so the owner is not Authentic Brands. The locator is a shared Aldo app that also carries Sperry, so Sperry's 8 October read should be re-checked.
- **Eddie Bauer stores are confirmed at 0:** eddiebauer.com has no store locator. Authentic Brands owns the brand, Outdoor 5 LLC has run e-commerce since February 2026, and the old store operator filed Chapter 11 on 9 February 2026.
- **Emporio Armani has 4 own doors.** SoHo is the only street store; the other 3 are airport boutiques, with Dufry operating ORD and LAX. There are 93 concessions. The locator has errors: DC is coded WA, the Tysons ZIP is wrong, and Chestnut Hill has an old ZIP.
- **Crockett & Jones** has 2 NYC stores. Its prices include duties (`USD_landed`).
- **G/FORE's parent** is filed as Peter Millar, and Peter Millar as Richemont (since 2012). The Richemont link was not re-checked this pass and needs verifying.
- **Fred Perry's** Modern Slavery Statement says 32 shops worldwide. That is a filing figure, so it is mentioned here only.
- **Columns left `NC` across the batch:** mostly Vinted (its API returned 403), B Corp and GOTS, and lookbooks.

---

# Per-brand notes


## Clarks: full record, wave B (read 11 Oct 2026, filed as 10 Oct)

**Checked:** US store clarks.com/en-us (Next.js; listing data in `__NEXT_DATA__`, Algolia index `prod_product_us`). Men's all-styles: 478 records, all loaded. Men's Clothing & Accessories: 99 records, all loaded. Originals clothing: 16 records. I also read 11 apparel PDPs and 7 footwear PDPs, the about page, the Styles & Stories hub, and the corporate made-to-last sourcing and policy pages. Off-site: Goodwin (Feb 2023) and World Footwear (Jan 2021) for ownership, and Grailed.

**Section 4:** Carried as instructed: 37 own-door + 135 outlet (US, incl. 7 PR); world NC (406 non-US raw records). The locator was not re-read for doors. One locator search (Boston) was run for section 5 only.

**Clothing, yes, but only a token range.** The men's clothing in navigation is:
- 2 Clarks Originals tees (Trek and Fam, $30, 7 colourway records, both carrying a "Limited Edition" badge)
- 1 Cloudsteppers Everyday Hoodie ($39.99 regular, 3 records)

All three are tagged Mens/Womens/Unisex. Everything else is socks, caps, belts, wallets, bags, water bottles and shoe care. A women-only Cloudsteppers Packable Jacket sits in the men's node and was excluded.

**Census:** 3 styles by handle (10 article numbers, ratio 10/3), 3 of 3 with a composition, 100% natural, no elastane, shape one. Line verdicts: Clarks Originals tees all-natural (100% cotton). Cloudsteppers is a single hoodie, a cotton-polyester blend with no percentages; it is filed cotton-led and flagged. Neither line reaches 5 styles.

**Prices:**
- Tee: single at $30.
- Shoes: pair, $100 Corsley Plain to $170 Un Briley Step (regular loafers).
- The other six garments: NONE.

**Needs a ruling:**
1. Every tee is badged Limited Edition. The standing ruling says a limited edition is never a high, so either the tee stays as single $30, or the tee goes to NONE.
2. Style counting: the record uses product handle (3 styles). If styles are counted by article number, the figure is 10. The verdict is the same either way.

**Stockists:** None listed. The locator holds only Clarks stores and outlets, and no stockist page exists, so I wrote one `none` row. No dealer chains could be summarised from a brand source, even though Clarks is widely wholesaled.

**Craft 2 / Tech 2.**
- Craft: no owned or named factory. The corporate page gives an SS22 country split (China, Cambodia, India and Vietnam lead) and says the factories are shared with other brands. No PDP states a country. The Steads tannery is named on 11 Originals records. Heritage is dated (Street, 1825).
- Tech: own-named footwear cushioning systems, plus GORE-TEX and Vibram on a few styles. There is no clothing tech.

**Not reached:** Vinted brand id (NC). Ownership percentages after 2023 were not verified in the Viva Goods filings.

**mark_as_written:** Clarks

**Worklist:** "own US stores" is confirmed (37).

**Out of scope, noticed:** One hoodie handle is misspelt "clousteppers-everyday-hoodie". The site is running a 25% cart promotion, but the displayed prices are regular.


## Columbia: full record, wave B batch 2 (read 2026-10-10/11)

**Mark as written:** Columbia. The logotype reads "Columbia" and the storefront page titles read "Columbia Sportswear". The key is kept as `Columbia`, and `note` carries `mark_as_written: Columbia`.

## What was checked
- **Store:** columbia.com runs on Salesforce Commerce Cloud with a PWA Kit front end. All data came from the site's own Shopper API, called through the page proxy (`/mobify/proxy/api`, siteId `Columbia_US`, prices in USD):
  - product-search on `refine=cgid=men`: 1,693 master products;
  - product payloads for all 1,693, including the regular and sale pricebooks.
- **Composition check:** the composition field (`c_fabric`) matched the PDP accordion text on 10 varied pages (SSR HTML `<li>`).
- **Search:** `/search?q=` works (jacket returns 600).
- **Prices:** 6 garments are filled, all on a `range` basis. Jeans and sweater are `NONE`.
  - Columbia makes no dress shirt. Casual button-ups were used instead.
  - Columbia makes no dress trouser. Chinos were used instead.
  - There is no loafer, so the shoe cell is cheapest to dearest footwear.
  - Prices are regular-pricebook prices. Two were checked against the displayed strike-through: Larry tee $18 and Chill Creek LS $140.
  - Big and Tall codes were kept out of the price picks.
- **Doors:** carried exactly as given (21 own-door, 142 outlet; world NC). The locator was not re-read for doors.
- **Stockists:** none. The only locator ("Store Locator - Brand and Outlet Stores", columbia.com/stores/, which embeds stores.columbia.com) lists Columbia's own stores. columbia.com has no dealer or retailer list. One `none` row is filed.
- **Sections 6–13:**
  - Tech: 5 proposed.
  - Craft: 2 proposed. There is no owned factory: the CSC Impact Report cites 330 third-party Tier 1 vendors. No maker, mill or country is named on any PDP.
  - Origin: 1938, Portland, Columbia Hat Company (Paul Lamfrom). Source: the Our Story page.
  - Quote: Gert Boyle, "Early to bed, early to rise, work like hell and advertise." (Our Story page).
  - Signature product: the Bugaboo Interchange (1986).
  - Grailed URL: confirmed live.

## Fibre census (complete denominator, 96% composition coverage)
- **Styles counted:** 667 men's clothing styles. Product codes were collapsed on their 6-digit stem: Big and Tall come as separate codes, 884 codes in all, which became 667 styles.
- **Excluded from scope:**
  - Collegiate team product: 410 masters, each team its own code.
  - NFL/MLB team product: 78 codes.
  - Kids and women's items that leak into the men's feed.
  - Footwear and accessories.
- **Coverage:** 641 of 667 styles state a composition.
- **Split:** 41% natural, 55% synthetic, 0% cellulosic-led. 153 styles contain elastane. Shape is `split`.
- **Licensee effect:** the natural share depends heavily on 168 licensee-made graphic tees, which are all cotton. Without the 207 licensee styles the range is 22% natural and 77% synthetic.
- **Line verdicts:**
  - All-synthetic: **Titanium** (52 styles), Silver Ridge, Terminal Tackle, Bahama, Steens Mountain, Tech Trail, Wild Cast and most named outdoor series.
  - All-natural: **licensee graphic tees** (168, cotton), Pitchstone (6) and Rapid Rivers (5).
  - Mixed: **PFG** (110: 81 synthetic, 28 natural), PHG (24), ROC (13) and Landroamer (10).
  - 166 styles sit in no named line.

## Needs Sebastian's ruling
1. **Collegiate and pro-team product.** It is out of both prices and fibre on the licensed-lines ruling. Collegiate alone is 410 masters, more than half the size of the counted range. Please confirm it stays out of the census.
2. **Licensee-made Columbia goods are kept in.** These are graphic tees (HYB codes), golf (OCS) and underwear/sleepwear (DGU). They carry the Columbia name, but they move the fibre headline by about 19 points. Two of the price cells are licensee items: tee low ($18 graphic tee) and polo low ($40 golf polo).
3. **Templated composition.** 165 of those tees state their composition only as one identical feature bullet ("100% cotton for lightweight comfort"). It is filed as read and flagged on every row.
4. **Tech 5.** This rests on owned, documented platform technologies across most of the range. The 119/667 share is a lower bound from titles and compositions only.

## Not reached (NC)
- Lookbook, Vinted, B Corp, GOTS, pronunciation.
- `quote_date`: the page is undated.
- Worldwide doors.
- `ownership_url` was linked from the footer but not opened.

## Out of scope but noticed
- The men's feed contains about 10 women's and 27 kids' styles.
- Sorel and Mountain Hardwear do not appear in the columbia.com men's feed.


## Converse: full record, wave B batch 2 (read 2026-10-11, read_date filed as 2026-10-10)

**Mark as written:** CONVERSE (the storefront logotype is all caps with the star-chevron). The key stays `Converse`. Also recorded in `note` as `mark_as_written: CONVERSE`.

## What was checked
- **Store:** www.converse.com, the US store on Salesforce Commerce Cloud (Sites-ConverseUS-Site). Prices are in USD. The grid paginates with `?start=N&sz=24&format=page-element`; `Search-UpdateGrid` returned 410. Site search `/search?q=` works (t-shirt returned 73).
- **Prices:** 6 garments are filled and 2 are `NONE` (jeans and sweater; men's clothing has neither).
  - Tee: $30–40, range.
  - Polo: $70–80, range. This includes a long-sleeve rugby the house calls a polo.
  - Dress shirt: $70, single. It is a short-sleeve ripstop button-up, the only woven shirt.
  - Dress pants: $70, single. Straight Leg Pants is the only non-sweat trouser.
  - Outerwear: $75–110, range. Both are a track jacket and a fleece jacket.
  - Shoes: $60–125, range. There is no loafer.
  - Licensed character tees (Minions, Hello Kitty, Dragon Ball Z) are out of prices. Limited Edition, Converse x collaborations, SHAI 001 and Custom/By You are out of the shoe high.
- **Fibre census (complete):** men's clothing navigation, cgid `mens-clothing-all`.
  - 68 colourway hits collapse to **38 styles** by product code. All 38 PDPs were read.
  - All 38 state a composition in the Details bullets: 32 cotton-led, 6 polyester-led, 0 cellulosic, 2 with 3% spandex.
  - Shape is `one`. Outerwear is synthetic-led but holds only 3 styles.
- **Fibre lines (title-series, the house names no fabric lines):**
  - **Chuck Taylor Patch** (7 styles): mixed. The cotton and cotton-poly tees, hoodies and joggers sit beside a 100% polyester zip-up jacket and track pant.
  - **CONS** (3) and **Converse Garage** (2) are under 5 styles, so they get no verdict.
  - The licensed collabs (8 styles) are all cotton-led.
  - **Headline:** the tees are wholly cotton and the jackets wholly polyester. The range is a small merch-led capsule of 38 styles.
- **Doors:** carried as given (2 own-door, 58 outlet, 1 pop-up; world NC). The locator was not re-read.
- **Stockists:** none listed. `/stores-all` is a directory of Converse-operated stores only. I wrote one `none` row.
- **Sections 6–13:**
  - Tech: 2 proposed. Clothing has no named fabric; footwear has GORE-TEX (licensed), CX and TecTuff.
  - Craft: 2 proposed. Heritage is dated and placed (Malden MA, 1908). No product page names a maker, mill or country.
  - Owner: Nike, Inc. since 2003, per converse.com's own history page.
  - Quote: from the house history page, which is undated.

## Not reached (NC)
Lookbook, Vinted, Grailed, B Corp, GOTS, pronunciation, quote_date, worldwide doors.

## Needs a ruling
- **Run Star Crush Pony Hair ($130):** I excluded it from the shoe high as hair-on hide, under the fur-on ruling. If pony hair is allowed, the shoe high becomes $130. Chuck 70 Leopard Pony Hair ($115) was excluded on the same reasoning.
- **Two full-zip jackets:** the fleece jacket and the mesh zip-up are labelled "Men's Top" under Tops & Tees. I classed them as outerwear by garment. The jackets filter itself holds 1 style.
- **Band-setting:** this falls through to trousers and outerwear, since Converse sells no dress shirt and no sweater.

## Out of scope but noticed
- Converse shoes are tagged "Unisex", and the men's shoe grid is that unisex set (162 masters).
- Character licences make up 8 of the 38 men's clothing styles (21%).


## Crockett & Jones: full record, wave B (read 10–11 Oct 2026)

**What I checked:** The US store at us.crockettandjones.com. crockettandjones.com geo-redirects there; it runs on Shopify in USD. I read:
- the Our Stores page (USA, UK and Europe tabs) and both NYC store pages
- the factory shop page
- the Store or Stockist locator (Roseperl app), searched from New York with no radius limit and max_results 26, which returned 11 rows
- the full products.json (814 products) and the men's loafer feed (121 products; the listing states 81)
- the heritage, in-the-making and material-guide pages, plus 8 men's PDPs across 8 categories
- off-site: Grailed and the B Lab directory

**Section 4:** 2 US own doors, both in NYC: 11 East 55th St, and 156 Spring St in SoHo. The worklist claim "NYC store" is confirmed and slightly understated. World: 12 own doors (2 US + 10 non-US: London 6, Birmingham 1, Paris 2, Brussels 1). There is also the Northampton Factory Shop, which the brand itself calls an outlet for substandard shoes ("SUBS"). I counted it in world_non_us (11), but not as an own door.

**Clothing:** None. The store sells shoes, belts, socks, wallets and leather goods, shoe care, and refurbishment services. All seven garment slots are NONE. The fibre census is 0 styles, so return_styles.csv is header only. Fibre line verdicts: none, because there are no clothing lines.

**Shoes (pair):** From $670 (Teign Navy Suede) to $1,460 (Bury 2, Hand Grade). **Flag for Sebastian:** the $670 low has no compare-at price, but the same Teign in dark brown is $770, and Richmond 2 Camel Suede at $670 likewise sits below the other Richmond 2 colours. So $670 may be an unmarked reduction. The next consistent regular price is $750 (Harvard 2 suede, in several colourways). The site banner says DUTIES & TAXES PAID, so I filed the currency as `USD_landed`.

**Stockists:** 9 other shops on the brand's US locator. Thom Sweeney NYC is another brand's own door; the other 8 are independents.

**Craft 5 / Tech 2 (proposed).**
- Craft: Crockett & Jones owns its Northampton factory (Magee/Perry Street, in use since 1891). The founding family (1879) still owns it, and the process is documented department by department. Caveats: the site says driving shoes are Made in Italy, with no maker named, and no tannery is named anywhere. A 4 is defensible if those weigh.
- Tech: only licensed or treated components, on about 15% of styles (Dainite soles, Scotchgard-treated repello suede).

**Not reached:** Vinted (NC). The brand slug served the generic catalogue, and the brand API was blocked in the browser tool. Ownership rests on the brand's own statement; I did not pull the Companies House filing.

**mark_as_written:** Crockett & Jones (the logotype writes it as CROCKETT & JONES).

**Out of scope, noticed:** The site says "100% Made in England" and that "the entire collection" is made in Northampton, yet its own driving-shoe PDP block says Made in Italy.


## Eddie Bauer: note (read 2026-10-11 in Chrome; read_date filed as 2026-10-10 per spec)

**Checked**
- **Own doors: positive zero.** eddiebauer.com is now a Shopify store (4gqgby-g9.myshopify.com) and has no store locator anywhere:
  - The header and footer carry no store link.
  - `/stores` and seven common locator paths 404. `/store-locator` and `stores.eddiebauer.com` (the old locator host) redirect to the home page.
  - The pages sitemap (25 pages) has no store page.
  - The return policy covers online and phone orders only.
  - The help centre FAQ (eddiebauer.gorgias.help) has no store entry.
  - The result is 0 own-door, 0 outlet, 0 concession and 0 pop-up in the US, with `worklist_conflict: own stores`. `world_non_us` is NC because no market (US, en-CA, fr-CA) has a locator.
  - `own_doors.csv` is header-only: zero rows means zero doors. I did not write a placeholder row, because it would break the rule that counts equal rows.
  - No operator or licensee stores are listed, so the operator ruling did not apply.
- **Prices:** seven garments read from the feed and confirmed on rendered PDPs. Marked-down items use the compare-at price. Shoes are `NONE`: there is no footwear in the 1,154-product feed.
- **Fibre:** a census of the men's navigation (`mens-all`, 268 products) less belts and the hat, giving 267 product codes. All 267 state a composition, in the PDP accordion MATERIALS & CARE. The census is complete.
- **Stockists:** the brand lists none. There is one `none` row.

**Not reached (NC):** lookbook, Vinted, Grailed, B Corp, GOTS, pronunciation. For this reason the record `status` is `partial`.

**Against the worklist/record:** the worklist says "own stores". The locator shows none, which confirms the accepted 8 Oct correction (stores closed).
- From press only, and not used for the count: AP reported on 10 Feb 2026 that store operator Eddie Bauer LLC filed Chapter 11 on 9 Feb 2026. At that point it had about 180 US/Canada stores, and Catalyst Brands held the store licence.
- AP also reported that Authentic Brands Group keeps the IP, that e-commerce and wholesale moved to licensee Outdoor 5, LLC from 2 Feb 2026, and that stores outside the US and Canada are run by other licensees.
- Source: https://abc7ny.com/post/retail-operator-outdoor-sportswear-pioneer-eddie-bauer-files-bankruptcy/18575429/

**Brief issues**
- A zero-door brand has no row shape in `own_doors.csv`. I used header-only. Please rule whether a placeholder row is wanted.
- The feed mixes legacy YE codes and new EB codes. Some pairs look like the same garment re-coded: two Radiator 1/4-zips and two Eddie's Favorite Thermal Crews. They are counted by code, as ruled, which may overstate the style count by a handful.

**mark_as_written: Eddie Bauer.** This is the site title, footer and vendor field. PDPs mention a "branding transition" between a block logo and a script logo; both read Eddie Bauer.

**Fibre line verdicts:** 56% natural-led, 43% synthetic-led, 1% cellulosic. The shape is `split`: outerwear (88% synthetic-led) and fleece/sweats are synthetic; tees, shirts and denim are natural.
- **All-natural:** Legend Wash (8), Eddie's Favorite (9), Vintage Soft (11, 70/30 cotton/poly), Camano (6), Signature (5) and the EB graphic tees (24, 60/40 cotton/poly).
- **All-synthetic:** Guide Pro, Mountain Trek, CirrusLite, Radiator.
- **Mixed:** Journey (modal/poly/cotton).

**Flags:**
- EB000958M "Chutes Microfleece Shirt" is listed as 100% cotton. That looks wrong for a microfleece; I filed it as read.
- YE01944M has an "oolyester" typo, read as polyester.

**Out of scope but noticed:** much of the men's range is on clearance (Clearance tags, prices 30–60% below compare-at).


## Emporio Armani: full record, wave B (read 2026-10-10/11)

**Scope and label filter.** I used the armani.com US store (`/en-us/`). Each house has its own path there (`/emporio-armani/`, `/giorgio-armani/`, `/ea7/`, `/armani-exchange/`) and its own `Brand` value in the store's Algolia index (`index_us_en`). I read that index from inside the page, filtered to `categoryPageId2 = "emporio-armani > man > clothing"`:
- It returned 974 colourway records, which matches the "974 items" count on the men's clothing listing.
- Every record says `Brand = EMPORIO ARMANI`, so no Giorgio Armani, EA7 or Armani Exchange product came in.
- Styles are the model+fabric code, which the URL carries as `cod-MODEL-FABRIC-COLOUR`. That gives 677 styles.
- 16 non-garments sit inside the clothing tree and were dropped: 13 sock styles, a beach towel, a cap and slippers. That leaves **661 styles in scope, and all 661 state a composition.**
- I checked the composition field against the rendered product pages. One trap: every product page also server-renders "recently viewed" Giorgio Armani items, so a page-wide regex returns "97% CASHMERE" on every product. The index field is the clean source.

**Section 4 (own doors).** `armani.com/en-us/store-locator` returns a 404. The footer's "Our locations" link goes to a Yext directory at locations.armani.com. Its Emporio Armani US page lists 99 cards. I read each store's own page for its address and phone.
- **Breakdown of the 99 cards:**
  - **4 own-door:** SoHo (134 Spring St), the only street store; Dufry-run airport boutiques at O'Hare and LAX; Miami International Airport, operator not stated.
  - **93 concessions:**
    - 91 department-store counters: Bloomingdale's, Neiman Marcus, Saks and Nordstrom.
    - Richards Greenwich.
    - DFS Galleria Waikiki.
  - **1 held:** "Giorgio Armani Honolulu Ala Moana Center" sits in the EA directory, but both its name and its brand field say Giorgio Armani.
  - **1 duplicate dropped:** "Uomo Los Angeles Saks" has the same address and phone as "Uomo Beverly Hill Saks".
- **The accepted correction checks out.** It said 92 department-store counters. I count 92 counter rows before the duplicate is dropped and 91 after.
  - Women's (Donna) and men's (Uomo) counters in the same store appear as separate rows, and I kept them that way.
  - The locator has no store-type field, so I read the format from each name and address.
  - There are no outlets under the EA banner: Armani Outlet is a separate brand on the locator.
- **Outside the US:** 473 EA directory entries in 55 countries, all formats mixed. own_doors_world is therefore NC.
- **Errors in the locator itself:**
  - Washington Neiman Marcus is listed as state WA; it is DC (ZIP 20015). I coded it DC.
  - The Tysons ZIP is given as 23338.
  - The Chestnut Hill The Street row uses ZIP 02167. That is the old code and points to the Bloomingdale's men's store at 55 Boylston St.
  - The host store for "Austin The Domain" is my inference: Neiman Marcus, from the address.
- **For a possible ruling:** the Santa Clara and San Jose Valley Fair rows may be one counter. I kept both in own_doors and merged them in stockists.

**Stockists.** There is no stockist page. The 70 stockists rows are the distinct host stores behind the locator's counters: 30 Neiman Marcus, 27 Bloomingdale's, 13 Saks, 2 Nordstrom, 1 Richards, 1 DFS. None of them qualifies for the register (department stores and concessions). Richards, a specialty store, is coded independent; it is a concession all the same.

**Prices.** All eight garments are filled, at full price in USD. Sale price equalled full price on every record, and four prices were confirmed against the rendered pages. The search is an overlay only, so search_url is `NONE`.
- **Judgements for Sebastian:**
  - **Jeans high:** the $575 J41 "DENIM LAB" jeans were set aside in favour of $545 jacquard jeans.
  - **Dress pants low ($445):** the product is titled "chinos" but is filed under Classic Trousers with a crease. The cleanest dress trouser is $595.
  - **Outerwear:** this is a range, $445 down jacket to $2,995 wool coat. The elevated option would be the cashmere coat at $2,195.
- **Excluded from highs** (Runway pieces, shearling, hair-on pony calf, a capsule):
  - Runway: the $3,595 coat, $1,075 trousers and $775 shirt.
  - The $5,200 shearling blouson.
  - The $14,000 pony-hair trench.
  - The $795 New York capsule monkstrap.

**Fibre verdict.** One cloth story: 67% natural-led, 16% synthetic-led, 17% cellulosic. 232 styles have elastane on the main fabric line, 146 of them at 5% or more, mostly underwear.
- No category is synthetic-led. Outerwear is an exact tie at 39 natural-led and 39 synthetic-led.
- **Lines, all named by the house:**
  - Armani Jeans (7) and Lunar New Year (5) are each all one fibre class: Armani Jeans all-natural, Lunar New Year all-cellulosic.
  - Runway (21) is 90% natural, so it counts as all-natural.
  - Essential (74), Signature (30), Icon (26) and Travel Essential (21) are mixed.
  - Icon leans synthetic (50%, mostly crêpe jersey). Travel Essential is 57% cellulosic.
  - 465 styles sit in no named line.
- **Suspicious composition:** EM004586, "Plain-knit virgin wool jumper", is filed as modal, silk and elastane and listed under T-shirts. I recorded it as read and flagged it.

**Craft 1, tech 2 (proposed).**
- **Craft:** no product page names a maker or a mill. Only 18 of 677 descriptions state a country of making, and no first-party page documents an owned factory.
- **Tech:** Travel Essential is a house-named travel line with performance claims. Nothing in it is licensed or owned technology.

**Not reached (NC):** owned facility, founders and place, Vinted, Grailed, B Corp, GOTS, signature product. For the quotation I found nothing quotable on the EA pages or the legal pages I read, so it is `NONE`.

**Mark as written:** EMPORIO ARMANI, with the eagle set between the two words in the header logotype. Key kept.

**Worklist:** the worklist's "own US stores" is wrong in substance. The US network is 1 street store plus 3 airport boutiques; the other 93 locations are counters.

**Out of scope:** the Neiman Marcus Mazza Gallerie (DC) counter is still listed on the locator. Press reports say that store closed in 2023. I did not verify this and coded the row `as listed`.


## Fjällräven: full record, read 2026-10-11 (read_date filed as 2026-10-10 per spec)

**What was checked (Chrome tab only, fjallraven.com US path `/us/en-us/`)**
- **Own doors.** I read the brand's store locator (`/us/en-us/store-locator/`). It is a Locally widget, company_id 1392, and I read its `conversion_data` feed in the page. I queried 18 map centres and every one returned the same 986 points (700 US, 283 Canada, 3 stray EU dealers), so the list is complete. Of those, 35 are Fjällräven-named. In the US that is **21 own doors** labelled "FJÄLLRÄVEN BRAND STORE" and **3 outlets** labelled "OUTLET STORE": Castle Rock, Freeport ME and Seattle Premium Outlets. I spot-checked the labels on the rendered store pages for Boulder, Fjällräven & Co and Freeport. Canada has 10 own doors and 1 outlet. `world_non_us` is NC because the locator covers North America only. No concessions or pop-ups are listed. No US door names its operator, so nothing confirms franchise or partner operation in the US. The worklist claim "20-plus US stores" is confirmed. "Fjällräven & Co", 304 Newbury St, Boston, is a second Boston brand store with no hours posted; it may be new or a different concept.
- **Stockists.** The same feed lists 676 US non-brand points. Chains with 5 or more US doors are summarised here, not written as rows: REI 192, Tillys 37, Mountain High Outfitters 23, Gearhead Outfitters 21, Half-Moon Outfitters 17, Sports Basement 15, Mast General Store 10, Backcountry 8, Christy Sports 8, Newbury Comics 8, JAX Outdoor Gear 6, Fleet Feet 6, Whole Earth Provision Co. 5 and Al's Sporting Goods 5. That leaves **315 rows** in `stockists.csv`. Locally does not give a shop type, so `shop_kind` is my reading of the name. Dillard's Tulsa and Charles Department Store are filed as department store, the two Toad&Co doors as other-brand own doors, and the rest as independent. Several of the "independent" rows are small regional chains or non-clothing shops (bike shops, a hatchery, bookstores, Ron Jon). Apply the register's door-one and door-two test before merging.
- **Prices and links.** All prices are full price in USD, read from the listing tiles. No tile carried a discount. Shoes are `NONE`: there is no footwear in the US navigation, and site search for "boots" returns only gaiters and trousers.
- **Fibre.** I read every page of the men's Jackets (80), Trousers (62) and Tops (108 unique tiles; the counter says 114 because of cross-listing) listings, then the spec block on all 250 product pages. I dropped 4 members-only-outlet items, which leaves **246 styles** keyed by F-code article number. 245 have a composition. Compositions add to 100 on every parsed row.

**Fibre verdicts:** 27% natural-led, 72% synthetic, 1% cellulosic, shape **split**. G-1000 is 65% recycled polyester and 35% organic cotton, so it reads polyester-led, and that makes Jackets (73 of 76) and Trousers (41 of 43) synthetic. Knitwear (21 of 25) and tees (24 of 35) are natural-led. 20 styles contain elastane, all at 5% or more.
- Lines (the house "Family" field) that are **all-synthetic**: Abisko 38 of 38, Keb 19 of 19, Polar/Expedition 17 of 17, Greenland 9 of 9 (all G-1000), and High Coast 11 of 12.
- **Mixed**: Övik 47 natural / 18 synthetic / 1 cellulosic of 66. This is where the wool knits and cotton shirts sit. Also mixed: Vardag (10 natural of 22), Bergtagen (3 of 25), Singi and Hoja.
- No line is all-natural.

**Needs Sebastian's ruling**
- **The mark.** `mark_as_written: Fjällräven` comes from the product data and body copy. The US site title writes "Fjallraven" and the SVG logotype was not read.
- **G-1000 as "synthetic".** By the main-fibre rule it is correct, but it puts a cotton-hand heritage fabric on the synthetic side for 69 styles. Flagging it in case the map wants a note.
- **Craft proposed at 2.** No owned facility, no named maker or mill, and no country of origin on any of the 246 product pages. The only evidence is a dated, placed founding. **Tech proposed at 4**: an owned, trademarked G-1000 and Greenland Wax system on 28% of the range, plus licensed GORE-TEX PRO and PrimaLoft.
- **Price picks.** Polo is `single` (Övik Polo, $105). The jeans are G-1000 five-pocket trousers, not denim. With no dress trouser or chino, dress pants are filed as the range of casual Outdoor Trousers. The Expedition Down Jacket Black Edition is excluded from highs as a limited edition. Even without it, the $855 outerwear high is held by three regular jackets.

**Contradicts the record / out of scope but noticed**
- **Suspicious composition.** The Expedition Pack Down Hoodie lists a "100% acrylic" shell, while its sister down styles are 100% recycled polyamide. Filed as read and flagged on the row.
- The Canada Shirt and Canada Shirt Solid list the G-1000 panel first. The flannel body is 45% acrylic. Both are filed on the first composition, per rule.
- **Annual report.** The Fenix Outdoor 2024 report gives no Fjällräven store count, only segment totals: Brands segment 42 stores, Global Sales 41. It also records a 30% stake in Arctic Fox s.r.o., which runs 6 Fjällräven stores in Czechia and Slovakia.
- **Not reached:** Vinted, the B Corp and GOTS directories, and colourway counts. The Grailed URL was constructed, not opened.
- I tripped Locally's bot check once while fetching store pages quickly. I backed off, and it did not affect the feed read.


## Fred Perry: full record, wave B batch 2 (read 10–11 Oct 2026)

**Checked:** US store www.fredperry.com/us/ (Magento, US | USD). All 12 men's navigation categories were paginated. Every listing on the /us/men all-products grid (651) maps to a counted clothing style, a shoe, or one of 48 accessory listings. All 223 men's clothing PDPs were read from the More Information table (composition, collection, bullets, price). Line pages read: Baseline, Sport, Sharp, Made in England, Collaborations, Limited Edition, Only at Fred Perry, Back Catalogue Exclusive. Also read the site map, the Made in England and Sweatband Subculture articles, the Modern Slavery Statement (FY2024), the Companies House PSC register and Grailed.

**Section 4:** Carried from held_door_counts.csv as instructed (US 0, positive zero; world NC), and the locator was not re-read. worklist_conflict: worklist says own US stores in NYC, LA. The site map's shop-finder index agrees with the count: its only US entry is Fred Perry New York (Broome St), the closed store. The Modern Slavery Statement says "216 direct retail outlets, 32 of which are owned and operated" by the group. That is a filing figure, so it is noted here and not used.

**Prices:** All 8 slots were read, jeans NONE. No markdowns appeared on any PDP. Collaborations (Craig Green, Comme des Garçons SHIRT, MEYBA, Kris Van Assche, Corbin Shaw, George Cox, Sanders) and Limited Edition pieces are excluded from every high.
- Tee: $65 to $125.
- Polo: M3600 $110 to M1212 Made in England $185.
- Dress shirt: Fred Perry makes no dress shirt, so the Oxford button-down pair is used, $160 to $175.
- Dress pants: range of the two non-track trousers, $185 to $200.
- Sweater: cotton crew $160 to RWS merino crew $215. This is a named judgement because there is no cashmere.
- Outerwear: Crinkle Harrington $255 to Made in England Harrington $500.
- Shoes: no own-label loafer (both loafers are George Cox collaborations), so this is a range, $145 to $255.

**Fibre (complete):**
- 223 styles, all with composition, from 730 colourway listings.
- Split by fibre: 75% natural, 24% synthetic, 0% cellulosic (one viscose-led knit).
- Spandex appears in 11 styles, 6 of them at 5% or more. There is 1 swim style.
- Shape is **split**:
  - Natural-led: Knitwear (95%), Polo Shirts (95%), T-Shirts (95%), Shirts (94%), Sweatshirts (100%).
  - Synthetic-led: Track Jackets (94%), Coats & Jackets (66%), Trousers (69%, mostly track pants).
- **Line verdicts:**
  - Craig Green (17 styles), Comme des Garçons SHIRT (3) and Corbin Shaw (1) are all-natural.
  - Every own line is mixed: Sharp 36 styles (81% natural), Sport 29 (72%), Baseline 24 (83%), The Fred Perry Shirt 9 (89%; M2721 tennis polo is poly/elastane), Made in England 9 (78%).
  - No own line is wholly natural or wholly synthetic. 103 styles sit in no named line.
- J3321 "Oversized Cotton Parka" is filed as 100% Recycled Polyamide, as the page states, but its bullets say cotton twill shell. This is flagged in the style note.

**Stockists:** The brand lists none. There is one `none` row: no stockist page, /us/stockists returns 404, and the shop finder lists own shops only.

**Proposed craft 3 / tech 1:**
- Craft: Fred Perry owns no factory (35 supplier factories in six countries, per the MSS). It names its Leicester makers, UK Piqué and ESP, and documents their process, but only for the Made in England line (about 9 styles). There is a fair case for 2. Sebastian to rule.
- Tech: no licensed or owned technology is named on any PDP.

**Not reached:** Vinted is NC (the brand slug serves a generic catalog and the API returns 403). No lookbook or campaign page was found on the US site. B Corp and GOTS are NONE on the brand's own claims; the B Corp directory was not checked directly. Founders and the founding place come from the brand's Sweatband article. Hit Union ownership is from FashionNetwork (2018), and Companies House shows only the UK holding company.

**mark_as_written:** Fred Perry (the logotype and nav set FRED PERRY in caps).

**Out of scope, noticed:**
- The site misspells the collab collection as "Kris Van Asche" on PDPs. The site map writes Kris Van Assche.
- The Back Catalogue Exclusive styles in the site map (SG/SD/SK codes) do not appear in the men's grid.
- M12 appears on the Limited Edition page, probably a single colourway.


## G.H. Bass: full record, wave B batch 2 (read 11 Oct 2026, filed as 10 Oct)

**What I checked:** the US store ghbass.com (Shopify, USD, `Shopify.currency.rate` 1.0). I read the full `/products.json` (208 products on one page; page 2 was empty), the men's navigation tree, the men's loafers collection (49 listings), 12 men's PDPs across loafers, boots, a boat shoe and a Chelsea boot, the Craftsmanship and Our Story pages, the privacy policy and terms of service, the store locator, and Grailed.

**Section 4, own doors: NC.** The locator at /pages/store-locator does not return data. On load, and again on a zip search (10001), the page's own `POST /apps/store-availability/api/metaobject-store-information` returns `HTTP 401 {"error":"Unauthorized"}`, and the page shows "Error. Something went wrong." On first load the page showed "No stores near your location", but that message came from the same failed call. I also tried country US, CA, PR and GB and the /en-ca path, and all returned 401. Shopify pickup availability is empty, and the metaobject sitemaps are empty. As a result, own_doors.csv has a header and no rows, and counts.csv is all NC.
- The earlier accepted correction (stores closed in 2020, so 0) could not be verified from the locator. I did not substitute any figure for it.
- worklist_conflict: the worklist says "own stores". This cannot be confirmed. It needs a human read once the locator works again.

**The brief is wrong on ownership.** The privacy policy (effective 23 Sep 2026) names **G.H. Bass IPCo LLC, an entity within G-III Apparel Group**, as owner of the brand's IP. The Aldo Group runs the website day to day. The terms name ALDO U.S. Inc. of Montreal as site operator. The site does not name Authentic Brands anywhere. Any future Bass store row should carry "operated by Aldo (licensee of G-III)" unless the locator says otherwise.

**Clothing:** none. The feed holds 194 footwear products, 11 shoe-care products and 3 laces. Men's navigation has no apparel. That gives seven NONE garment slots, a fibre census of 0 styles, and a return_styles.csv with the header only. Fibre line verdicts: none, because no clothing lines exist.

**Shoes (pair):** $130 to $250.
- Low: Regent Penny Loafer at $130.00 full price.
- High: Logan Weejuns penny loafer at its $250.00 compare-at price. It is marked down to $169.99. I checked the compare-at against Larson Oyster ($195 compare-at), which matches Larson Black at $195 full price.
- The dearest loafer at full price on the day was Venetian Gathered Weejuns black at $245.
- Collaborations excluded from the high: Wallabee Weejuns (Clarks Originals) $295, Buck Mason Larson $295, Metalwood Sportocasin $275.

**Stockists:** the brand lists none. I wrote one `none` row.

**Proposed craft 2, tech 1.** The making process is documented: handsewn moccasin, beefroll, Blake-stitched resoleable sole. The heritage is dated and placed: 1876, Wilton and Farmington, Maine. Against that, the site names no current factory, maker or tannery, and 0 of 12 PDPs state a country of origin. There is no named or licensed technology.

**Not reached:** Vinted. Its brand API returns 403, and /brand/g-h-bass resolves to the unfiltered catalogue. No lookbook was found on site (the Explore hub holds guides only).

**mark_as_written:** G.H.BASS. It appears in the title tag, the navigation and the vendor field on 19 products. The other 189 products carry the vendor "GH Bass".

**Out of scope, noticed:** the locator script is a shared Aldo app with Sperry and Aldo icon sets. Its 401 may also affect Sperry's locator, which was read on 8 Oct, so it is worth re-checking. Grailed files the brand as "G.H. Bass & Co." (788 items).


## G/FORE: full record, wave B batch 2 (read 2026-10-10)

**What was checked.** I read the US store at www.gfore.com. It runs on Salesforce Commerce Cloud and prices in USD (JSON-LD `priceCurrency` USD, and the tile and product-page prices match). The men's clothing grid, `/c/men/clothing?sz=500`, states "155 Products". Those 155 tiles are 155 colourway tiles of 91 product codes. The union of the 8 sub-categories (polos, pants, shorts, pullovers & quarter-zips, outerwear, hoodies & tees, sweaters, dress shirts) is the same 91 codes, with 18 codes listed under two or three categories. I also read all 91 product pages and their Materials blocks. Shoes: `/c/men/shoes` holds 45 codes (41 golf, 2 loafers, 2 sneakers or slip-ons). Other pages read: the About page, the Storemapper feed behind `/f/stores.html`, and one press report (mr-mag.com, 2018).

**Section 4** was not re-read. Counts were carried over: 4 own doors in the US and 5 worldwide (Seoul); Pebble Beach stays held. One clue for that ruling: the same Storemapper feed lists "Pebble Beach" (Pebble Beach Golf Links, 17-Mile Drive) as a GOLF CLUB account. That suggests the arcade shop may be run by the resort. Not verified.

**Stockists.** There are 122 US rows: 75 tagged GOLF CLUB (club or resort pro shops, which are not register shops), 3 Bloomingdale's (department store), and 44 retailers, 4 of them untagged. The rows also include 3 small chains under 5 doors: Craig Ryan (4), Hornacek's (3) and Pro Golf Seattle (3). I dropped 3 Canadian rows that fell inside the US bounding box (two Golf Town stores in British Columbia and TPC Toronto). Five chains with 5 or more US doors are summarised here, not written as rows:
- Golf Galaxy / DICK'S: 130 (85 Golf Galaxy, 27 Golf Galaxy Performance Center, 18 DICK'S House of Sport)
- PGA TOUR Superstore: 55
- Roger Dunn Golf: 17 (California and Hawaii)
- Golf Exchange: 6 (Ohio and Kentucky)
- Saint Bernard: 5 (Texas)

**Not reached / NC.** Vinted and Grailed are NC: the Grailed designer URL fell back to the generic designers page, and Vinted was not tried. B Corp and GOTS are NC because the directories were not read. No lookbook exists on the site (no lookbook, campaign or journal pages; search "lookbook" returns 0 results), so those cells are `no` / NONE. Status is `partial` for these cells only.

**Contradictions with the worklist or brief.**
- The About page gives no founding date. 2011 and Mossimo Giannulli come from press.
- Ownership: the site's careers link goes to Peter Millar LLC, which confirms Peter Millar ownership (acquired January 2018). Peter Millar's own parent was not re-checked; I filed it as Richemont per older press and flagged it.
- The worklist band reads "accessible". The prices sit there: sweater $225 to $450, dress shirt $325.

**Mark as written.** `mark_as_written: G/FORE`. The header logotype matches the key.

**Fibre verdict.** The range is split: 43% natural, 53% synthetic, 2% cellulosic, and 2 styles (2%) with no composition stated. 58 of 91 styles contain elastane, 51 of them at 5% or more.
- Polos (36 styles) are 72% synthetic-led. Sweats, outerwear and shorts are also synthetic-led.
- Knitwear is 100% natural (10 of 10: cashmere, merino, linen, cotton). Trousers lean natural (5 of 9) and shirts are 6 of 7 natural.

Lines:

| Line | Styles | Verdict |
|---|---|---|
| Tech Jersey polos | 13 | all-synthetic: 100% polyester or nylon with 7–22% elastane |
| All Play | 12 | mixed: 3 natural, 6 synthetic, 2 cellulosic, 1 undisclosed |
| LTD Release | 21 | mixed but 81% natural; these are limited editions |

Tour (3), The Club (2, all wool) and Maverick (4, all synthetic) are under 5 styles each. 37 styles sit in no named line.

**Prices.** Seven garments are filled; jeans is NONE (search "jeans" returns 0 results). Notable judgements:
- **Limited editions:** LTD RELEASE items (21 of 91) are kept out of every high.
- **Dress shirt:** the "Dress Shirts" category is mostly knit-piqué button-fronts ($195 to $295). The only regular woven, collared, button-front shirt is the Brushed Flannel Overshirt at $325, filed as `single`.
- **Polo:** the high is the $350 Cooling Cotton Sweater Polo, which the house lists under polos. Without it the high would be the $185 Luxe Cotton Blend Polo.
- **Outerwear:** jackets only, $295 to $995. The high is a lamb-suede trucker jacket, not shearling.
- **Shoes:** two regular loafers, both at $495. Golf shoes run $195 to $250 regular (the $350 pair is LTD).

**Craft and tech.**
- Proposed craft is **2**, with 1 arguable: no maker, mill or facility is named; no page states the garment's country of making; 16 of 91 pages say the fabric or yarn is Italian or European.
- Proposed tech is **2**: performance claims (UPF on 15 styles, moisture-wicking on 37) but no named fabric technology.

**Flags in the style file.**
- Oxford Piqué Shirt: the copy says "cotton blend piqué" but the composition reads 78% nylon / 22% elastane. Filed as read.
- Delta Dot Jacquard Polo: the composition is printed out of order. Read as 77% nylon / 9% polyester / 14% elastane.
- The 2 Sugar Skull & Tees collaboration styles: the bare product URL returns HTTP 410, the colour-parameter URL works, and the page has no Materials block. Filed as ND.

**Out of scope but noticed.**
- The site also runs gfore.co.uk and gfore.ca storefronts.
- The footer "Store Locator" link points to /store-locator.html, not /f/stores.html.
- The Storemapper feed holds 630 entries worldwide.
