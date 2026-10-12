# seat_wave_b — batch 4 (Kjus through Palace) · 11 October 2026

## Files

- `return.csv`: 10 rows.
- `return_styles.csv`: 911 styles.
- `stockists.csv`: 1,089 rows.
- `return_counts.csv`: 4 brands.
- `own_doors.csv`: the running master, 1,268 rows.

All brand names match the canonical keys exactly, no cell is empty, all values are from their allowed lists, and every store count equals its rows.

## Retry, 11 Oct afternoon

- **Kjus: prices filled, fibre partial.** It was blocked again (Akamai 403) after 37 product pages.
  - Prices: tee $99, polo $109–139, golf trousers $199, sweater $179–229, outerwear $299–2,999 (Orange Label cashmere tech jacket, flagged).
  - Dress shirt, jeans and shoes are NONE.
  - Fibre: 37 of 215 styles read, all ski or lifestyle. Golf and sale styles stay `NC`.

## Blocked mid-read (original run)

- **Kjus:** kjus.com started returning Akamai "Access Denied" (HTTP 403) during the locator sweep.
  - Doors are complete for the lower 48 states. Only northern Alaska, Hawaii and Puerto Rico were cut off.
  - Prices and the fibre census are `NC`.

## Flags for merge (not covered by the standing rules)

| Brand | Flag | Filed |
|---|---|---|
| Koio | Store locator page is a 404; the help centre mentions an NYC store but gives no address | Doors `NC` |
| Koio | Every regular loafer is $275 | Shoes `pair` $275/$275 (could be `single`) |
| Kjus | Aspen and Vail Kjus shops sit on a resort retailer's Locally account, not the brand's locator | Not counted; `worklist_conflict` |
| Lanvin | No woven shirt and no outerwear; the only trouser is a sold-out flannel drawstring | Dress shirt and outerwear NONE; dress pants `single` $1,200 |
| Lanvin | Product pages say "VAT and Duties included" | `USD_landed` |
| Lucchese | Snap-front Western shirts | Not counted as button-front (otherwise the dress-shirt low is $165) |
| Lucchese | Sport coat has 18 article numbers, one per cloth | 18 styles, as ruled |
| Maison Kitsuné | Savoir-Faire is called a "premium capsule" by the brand, but its $2,315 coat sits in regular Outerwear | Excluded; outerwear high $940 |
| Maison Kitsuné | Café Kitsuné-label tees and sold-out older-season styles in navigation | Counted, not priced |
| Marni | 100% cashmere polo jumper, $1,550 | Not used; polo is the cotton range |
| Moose Knuckles | Fur and shearling outerwear | Excluded; high $1,495 Neo Bunny leather |
| Moose Knuckles | Gold Series article suffixes | Merged into 83 styles (96 if separate) |
| Nanamica | Only footwear is REGAL collaborations and a limited sandal | Shoes NONE |
| Nanamica | Spiber Brewed Protein has no class in the fibre list | `other` (2 styles) |
| On | Two own store lists disagree; outlets appear only on the shop locator | 19 own + 2 outlets; world 51, but On's 20-F counts 38 China locations not on the stores page |
| Palace | Outerwear low is a track jacket listed under Jackets | $178 (otherwise $198 coach jacket) |

## Things found

- **Kjus** belongs to Acushnet (acquired 2019). It has no US own door; there is one pop-up in Greenwich, CT. Its US stockist list holds a single row, which looks like a test entry.
- **Lanvin** is controlled by Fosun through Lanvin Group, per the FY2025 20-F. The US men's online range is only 25 styles.
- **Nanamica** is 96.7% owned by Goldwin.
- **Moose Knuckles** is majority-owned by Cathay Capital, with Bosideng holding more than 30%. It still sells fox fur, despite a 2021 fur-free headline.
- **Lucchese's** El Paso factory is evidenced by the brand's own blog and process page. It is unconfirmed whether the factory is owned or leased.
- **Figures from parent companies, press and brand statements are mentioned only, never filed as door counts:**
  - Marni: 96 stores (OTB).
  - Maison Kitsuné: 38 stores (its stale About page).
  - Moose Knuckles: "almost 50" stores (press).

---

# Per-brand notes


## Kjus: full record, read 2026-10-11 (partial: site blocked twice; retry filled sections 1–3 in part)

**Mark as written:** KJUS. The site title reads "KJUS | Premium Golf & Ski Apparel" and the footer reads "KJUS NORTH AMERICA INC.". The key stays `Kjus`, and `note` carries `mark_as_written: KJUS`.

## The block (read this first)
- kjus.com/us/en is Salesforce Commerce Cloud (Sites-kjus-Site). Akamai sits in front of it.
- **What happened:** after about 1,600 in-page calls to the locator endpoint `Stores-GetNearestStores` (concurrency 3, about 150 ms apart), the site began returning HTTP 403 "Access Denied" (Reference #18.d7fd117.1791728241). I stopped the site for the rest of the run, as the spec requires.
- **NC because of the block (first run):** every price cell, `currency`, `search_url`, the whole fibre census, made-in share, named makers and mills, tech share of range, the signature product and the lookbook. **Superseded in part by the Retry section below.**
- **Before the block, the live site gave me:** the men's navigation, the FAQ and the locator. After it, I read three brand pages (Tech Guide, About, pronunciation) through web.archive.org captures and said so in each cell.
- **Re-run:** sections 1–3 need a fresh session on kjus.com. Start with the listing grids. Leave the locator alone; it is done.

## Own doors (section 4)
- **No locator link in the footer.** The FAQ points to a "Store Locator", which is the SFCC Dealer Locator at `Stores-Find`.
- **The page itself is broken.** Its Google Maps client throws `InvalidClientIdMapError`, so a search returns nothing. The page's own endpoint still works. Its parameters are latitude, longitude, countryCode and maxdistance, and the server caps the radius at 50 miles (tested).
- **Sweep:** I read it on a 0.9-degree grid. All 1,462 lower-48 points completed and Alaska south of 58.5N completed. The 403 cut off northern Alaska, Hawaii and PR.
- **Cross-check:** `Stores-GetAllStores` returns the same 2 records, so I treat the list as complete.
- **US: 0 own doors, 0 outlets, 0 concessions, 1 pop-up.** The pop-up is Greenwich Pop-Up Shop at 117 Greenwich Ave, CT, with the locator's own lat/lon.
- **The second record is a dealer.** Katy Golf Club in Parsons, KS is filed in stockists.csv. It carries a `test@test.com` email and a "default-coordinate" id, so it may be stale.
- **worklist_conflict:** the worklist says "own US stores (Aspen, Vail)". The brand's locator shows neither.
  - The batch-3 Helly Hansen note saw a "Kjus" store on a separate Locally account (101960) that also lists HH Vail and Oakley. That is probably a resort retailer's account, not KJUS's locator, so it is not a door source here.
- **World:** `NC`. The locator is scoped to the US site, and the EU stores were not read because of the block. kjus.com press-release titles name flagship stores in Zurich and Munich (NOTE only, not a door source).

## Stockists (section 5)
- **1 row:** Katy Golf Club, a golf-club pro shop. The register excludes club pro shops; it is recorded as the locator gives it.

## Fibre
- First run: not read (blocked). See Retry below for the 37-style read. The men's navigation shows three families: Golf (rain-and-wind, jackets-and-vests, midlayers, polos, bottoms), Ski (jackets, pants, midlayers, baselayers) and Lifestyle.

## Sections 6–13
- **Tech: 4, as proposed.** The Tech Guide (archive capture 2026-07-12) names about 13 house technologies, among them VaporTemp, Hyper 3D Stretch, Hollow Pima, graphene and carbon-capture polyester. A Patents page is linked from the footer. No fabric is shown as owned and the share of range is unread.
- **Craft: 2, provisional.**
  - Acushnet's 10-Ks say KJUS finished goods are sourced from third-party vendors, so there is no owned making.
  - No mill is named on the Tech Guide. The heritage is dated and placed.
  - It could fall to 1 if the product pages state no origin.
- **Owner:** Acushnet Holdings (NYSE: GOLF), acquired July 2019 (FY2019 10-K), price undisclosed.
- **Founding:** 2000. The founders are Lasse Kjus and Didi Serena per FashionNetwork 2019.
  - The brand's own accounts disagree on the place. The FAQ says "originally founded in Switzerland". The brand story describes an early office in an old Oslo train station.
- **Quote:** Lasse Kjus, from the brand's pronunciation page. **Pronunciation:** "Shoo-ss", per Lasse on the same page.
- **Grailed:** 1.7k listings. **Vinted:** `NC` (the brand-filter API returned 403). **B Corp:** no, from a directory search. **GOTS:** no, from a database search with no match.

## Flags for merge
- **Positive zero against the worklist claim.** Aspen and Vail are not on the brand's locator. They may be retailer-operated KJUS-bannered shops listed elsewhere, such as the Locally account 101960 seen in the HH batch. If Sebastian wants operator-run resort shops counted, someone needs to read that account. Under the standing rules it is not the brand's own locator.
- **Katy Golf Club** looks like a test or stale locator entry (test@test.com).
- The whole price, link and fibre layer needs a re-run once kjus.com lets the browser back in.

## Retry 2026-10-11 (sections 1–3)
- **Access:** https://www.kjus.com/ loaded normally (no block) at the start of the retry. Locator not touched.
- **Grid:** https://www.kjus.com/us/en/men/ states 237 products; read in one page (`sz=240`), 237 unique product URLs. 22 are accessories (beanies, gloves, caps, belts, a tumbler, a bottle), so **215 men's clothing styles**. 118 of the 215 tiles sit on `/sale/` paths (many marked "previous season"). They are on the Men grid, so they are in the census denominator. Each colour is a variant under one product code, hence ratio 215/215.
- **Second block:** product pages were opened by navigation, about 6 s apart. Page 38 (a sale PDP, `sale/mens-inverness-shirt/MC62-I00.html`) returned Akamai "Access Denied" HTTP 403, Reference #18.4c7fd117.1791733197, **at 11:39:57 EDT**. Five more queued navigations in the same batch fired before I could halt; all five were 403s. The site is stopped. Data was read back from page storage, with no further requests.
- **Prices (from listing tiles, full price, current range; sale and previous-season tiles excluded):**
  - Tee: $99 single (Hollow Pima T-Shirt).
  - Polo: $109–139 range.
  - Dress shirt: NONE.
  - Jeans: NONE.
  - Dress pants: $199 range (golf trousers).
  - Sweater: $179–229 range.
  - Outerwear: $299–2,999 range.
  - Shoes: NONE.
  - Currency USD. Tile prices matched the product page on all 37 pages read. `search_url` NC (not tested).
- **Listing links:** these are navigation hrefs and product-URL paths. The listing pages were not opened, so the tiles were not checked.
- **Fibre (partial):** 37 of 215 styles read (17%), all with a stated face-fabric composition. Every page read was Ski or Lifestyle; Golf and the sale styles are unread.
  - On those 37: 6 natural, 31 synthetic, 0 cellulosic. 24 contain elastane, 22 of them at 5% or more.
  - Natural: 2 merino sweaters, 2 Orange Label jackets, the Yellowstone wool-blend shirt and the Inverness cotton/cashmere hoodie.
  - **Line verdicts:** FRX (5 styles) is all-synthetic. Formula (4) is synthetic but under the 5-style bar. Orange Label (2) is natural (Loro Piana merino and cashmere).
  - The read range splits: synthetic-led outerwear against natural-led knitwear. Treat it as ski-skewed.
- **Tech:** 19 of 37 pages name a house technology: Graphene 10, FAST Thermo Core 8, VaporTemp 4, Hydraulic 4. Four use Toray Dermizax, which is licensed. **Tech stays 4.**
- **Craft:**
  - 0 of 37 pages state a garment country of origin.
  - No maker is named.
  - Loro Piana cloth "made in Italy" is named on 2 Orange Label jackets.
  - **Craft stays 2.** The provisional flag is cleared on the sample read.
- **Still NC:** `search_url`, composition for 178 styles (all of Golf, all of the sale styles, and most of Lifestyle), the signature product and the lookbook.

### Flags for merge (retry)
- Sale styles in the census: 118 of the 215 Men-grid styles are sale/previous-season tiles. If Sebastian wants the census limited to the current range, the denominator is about 97. The first-pass price slots already exclude sale stock.
- Dress shirt NONE: the only woven button-fronts are on sale (Flex Linen Long-Sleeve Shirt, Inverness Texture Shirt). The current-range "shirts" are midlayer overshirts.
- Orange Label: it is treated as a sub-line in the main navigation and counted for the outerwear high ($2,999 Cashmere Tech Jacket). If it is a capsule, the high falls to the next jacket ($1,999 Verbier Luxe is also Orange Label; then $1,699 Frozen Smoke).


## Koio: full record, wave B batch 4 (read 11 Oct 2026)

**Checked:** koio.co (Shopify, USD, rate 1.0): the full `/products.json` (122 products, 1 page; sitemap 121 handles, all in the feed), the men's loafers collection, PDPs for Catania Suede Loafer (Taupe), Lido Suede Loafer (Fawn) and Capri Triple White, site search and search-suggest for garment words, the FAQ, Italian Craftsmanship, About Us, Our Vision, Sustainability, Lookbooks, the pages sitemap, footer and help centre (koio.gorgias.help, all 7 categories). Also Grailed, B Lab directory, Vinted.

**Section 4 (own doors): NC.** koio.co has no store locator. The help centre's "To find your nearest location, click here" links to `koio.co/pages/store`, which is 404. `/pages/stores` is 404, and `/pages/locations` redirects to `/pages/stores`. No stores page appears in the pages sitemap, and there is no Shopify pickup-availability data. The help centre does say orders may ship "from our retail store in NYC" and that cash is accepted "in stores only", so a store probably exists, but the brand publishes no address. I wrote no rows (own_doors.csv is header only) and did not take an address from press. worklist claim: NYC stores.

**Clothing:** none. The feed is 100 footwear, plus laces, insoles, shoe care, a dust bag, a gift card and shipping insurance. Searches for tee, sweater, shirt, jacket, hoodie, pants, socks and hat return only shoes. Seven garment slots NONE; fibre census 0 styles (return_styles.csv header only). Fibre verdicts: none.

**Shoes (pair, 275/275):** all 9 regular men's loafers (Catania 4, Lido 5 colourways) are $275 full price. Low is filed as Catania Taupe (made in Porto) and high as Lido Fawn (made in Florence). I confirmed the feed price against both displayed PDPs.

**Stockists:** none. Koio says it is direct-to-consumer, and there is no stockist page.

**Craft 2 / Tech 2 (proposed):**
- Craft: country stated on 100 of 100 footwear products (Italy 79, Portugal 21; FAQ: Ostuni line Spain).
- The Florence partner factory is unnamed: a claim, not evidence.
- A named tannery (Conceria Brotini, Conceria Carpanese) appears only on the Rose Anvil collaboration.
- Tech: OrthoLite Hybrid insole (licensed) on 93 of 100; Vibram on 1; apple-leather Vegan 01 (4).

**Not reached:**
- Vinted: the catalog API returned 403 on the first call, so I stopped.
- Ownership: the brand names its founders only; owner_today is NC.
- Lookbooks page: the latest is FW21 (stale).

**mark_as_written:** KOIO (logotype and Shopify vendor field). Body copy writes "Koio".

**Out of scope, noticed:** the feed has no women's footwear product type even though women's handles exist (e.g. capri-triple-white-womens). products.json may be market-scoped. This does not affect a men's record.

## Flags for merge
- **Own doors NC, not zero.** The brand's own help centre asserts an NYC retail store, but its locator link is dead. The Spectrum thread may want a human check or a later re-read of koio.co/pages/store.
- **Loafer low = high ($275).** Filed as `pair` with identical figures because every regular loafer is one price. `single` may be the better basis.
- **Two production countries in the loafer pair** (Portugal for Catania, Italy for Lido). The map may care.


## Lanvin: full record, wave B batch 4 (read 11 Oct 2026)

**Checked:** US store www.lanvin.com/en-us (Salesforce Composable Storefront / PWA Kit, site `lanvin_us`, USD). The men's RTW listing loads through the SCAPI shopper-search proxy that the page itself uses; the listing gives 31 colourway tiles for `men-ready-to-wear-view-all`, and the four subcategories add up to the same 31 (Coats & Jackets 1, T-shirts & Sweat-shirts 19, Pants & Shorts 6, Knitwear & Polo 5). All 31 variation groups were read through shopper-products: composition (`c_materialDescription`), country of making, price and sale flag. The field was checked against rendered PDPs (flannel trousers, both crewnecks, the loafer), and they agree. Also read: Loafers & Derbies (3 tiles), History of the House, the Winter 2026 and Summer 2027 show pages, the FY2025 20-F on SEC EDGAR, and Grailed. There was no WAF and no block.

**Section 4:** Carried over as instructed; the locator was not re-read. The US has 3 own doors (Madison Ave, Las Vegas Crystals, South Coast Plaza) and 0 outlets. 11 non-US doors are listed with formats not split, so the world count is NC. The 20-F has no Lanvin store count.

**Prices** (all full price; no item flagged as sale):
- Tee: $590–990 (range).
- Polo: $1,250 (single).
- Dress shirt: NONE.
- Jeans: NONE.
- Dress pants: $1,200 (single, flagged).
- Sweater: $1,450 / $1,950 (pair, wool then cashmere crewneck).
- Outerwear: NONE.
- Shoes: $1,160 (single loafer).

**Fibre (complete):**
- The range is 25 styles (31 tiles). Styles were counted by master article number (model + fabric + season). All 25 state a composition.
- Split: 96% natural, 4% cellulosic (the bonded viscose polo), 0% synthetic. No spandex on any main fabric line; elastane appears only in rib trims. No swim.
- Shape is **one**.
- **Line verdict:** Lanvin Ribbon (8 styles, a title series) is all-natural, all cotton or cotton-cashmere. No line is synthetic. Lanvin Embroidered (3) and Mother and Child (2) are under 5 styles. 12 styles sit in no named line.
- Categories:
  - tees-polos 7, sweats 11 (cotton jogging pants assigned here by garment), knitwear 4 (the cardigan the house files under T-shirts), trousers 2, tailoring 1.

**Stockists:** None listed. There is one `none` row.

**Proposed craft 2 / tech 1:**
- Craft: all 25 PDPs state the country: Italy 16, Türkiye 5, Portugal 4.
- No maker, mill, owned facility or process is named.
- The heritage is dated and placed (1889, Paris; menswear tailoring from 1926).
- Tech: none.

**Owner:** Lanvin Group Holdings (NYSE: LANV) through Arpège SAS / Jeanne Lanvin SA, where minority holders own 4.73%. Fosun International is the controlling shareholder (FY2025 20-F).

**Not reached:** Vinted (NC). B Corp and GOTS directories were not checked (NONE is based on the brand's claims).

**mark_as_written:** LANVIN

## Flags for merge
- **Outerwear NONE.** Men's Coats & Jackets holds a single item, a one-button super150 wool blazer at $2,650 (SS23 carry-over). It is excluded as a blazer, so the slot is NONE.
- **Dress pants.** There is no dress trouser. The only woven trouser is the drawstring "Fluid Wool Flannel Trousers" at $1,200, sold out in all sizes. It is filed as single. Should it stand as dress pants?
- **Dress shirt NONE.** There is no woven shirt of any kind in men's navigation. The flannel trouser copy mentions a "matching overshirt" that is not online.
- **Band inputs are thin.** Only the sweater pair gives a dress-shirt/sweater signal, and both sweaters sit above $400.
- **Currency.** US PDPs show "VAT and Duties included", so prices are filed as `USD_landed`. Please confirm or rule `USD`.
- **Suspicious compositions (all filed as read):**
  - Fluid Wool Flannel Trousers says "100% silk woven" (API and PDP agree).
  - Ribbon jogging pants "in cotton and cashmere" says 100% cotton.
  - The reversible tee "in cotton and taffeta" says cotton only.
  - The layered sweatshirt interleaves two unlabelled 100% polyester parts with 95/5 cotton-cashmere.
- **Unlabelled second parts.** Several compositions list a second unlabelled "100% polyester knitted". On the tees and cashmere sweaters it is read as the embroidered logo, so those styles are filed natural. On the bonded double-face polo it is read as the second face, so the polo is filed as a blend.
- **Genderless polo.** One polo colourway (2910) has a women's primary category, but it sits in men's Knitwear & Polo. It is counted once.

**Out of scope, noticed:** Section 4 already logged the press figure of 7 stores as stale. A men's online offer of 25 styles is very thin for a true-luxury house: most of it is Curb sneakers (75 shoe tiles), and the clothing is mainly logo jersey.


## Lucchese: full record, wave B batch 4 (read 2026-10-11)

**What was checked.** I read the US store at lucchese.com. It runs on Shopify, prices in USD, `Shopify.currency.rate` is 1.0, and the country is US. Every men's record has a `compare_at_price` of 0 and the sale collections are empty, so every price is a full price. I read two feeds:
- `/collections/men-ready-to-wear/products.json`: 159 records, which matches the page's own count of 159.
- `/collections/men/products.json`: 674 records, which added 24 apparel records and 278 boot/shoe records.

I read 179 men's apparel product pages one at a time, 1.5 s apart, for the bullet list that holds the composition (it is not in the feed). Other pages read: Our Process, the timeline, the store locator, the two stockist pages, two brand blog posts (John Muse; Inocenta Espinoza, factory worker), Shop the Look, and Grailed. Two outside sources were also used: Fox Business (25 Oct 2025) and Texas House Resolution 2374 (2023).

**Section 4** was not re-read. Counts were carried over: 28 own doors in the US and 28 worldwide, plus 4 outlets.

**Stockists.** The brand lists none. `/pages/stockists` and `/pages/lucchese-retailers` exist but render empty, and the store locator lists only Lucchese stores. The file has one `none` row.

**Fibre verdict.** 139 styles, counted by article stem (AZnnnnn; the colour suffix collapses), from 179 handles. The range is one cloth story:
- 89% natural, 6% synthetic, 2% cellulosic, 3 styles undisclosed.
- 19 styles contain elastane.
- Natural-led: shirts, tees, sport coats, jackets, denim and knitwear. Leather and suede lead most of the outerwear.
- Synthetic-led: only the recycled-polyester Golf Polos (5 article numbers) and two polyester/polyamide vests.

Lines:

| Line | Styles | Verdict |
|---|---|---|
| El Paso | 19 | all-natural |
| San Antonio | 11 | all-natural |
| Lucchese Sport Coat | 18 | all-natural (wool, silk, linen, cashmere blends) |
| Lucchese Golf Polo | 5 | all-synthetic |

**Prices.** All eight garments are filled.

| Garment | Low | High | Basis |
|---|---|---|---|
| Tee | $65 | $75 | range |
| Polo | $110 | $148 | range |
| Dress shirt | $195 | $375 | range (San Antonio button-front only) |
| Jeans | $225 | $325 | pair (selvage Cavalry Blue) |
| Dress pants | $195 | $285 | range (chino-type; no dress trouser) |
| Sweater | $325 | $645 | range (no crewneck staple) |
| Outerwear | $395 | $1,495 | range |
| Shoes | $350 | $1,895 | range |

- **Shoes:** the low is the Ridgeline Penny Loafer. The high is the Knox, a non-exotic regular boot, per the brief. Every boot above $1,895 is alligator, crocodile or caiman, or is The Watchman ($1,995, sold out and tagged low-stock-remove).
- **Exclusions:** Dallas Cowboys licensed product, the Chris Stapleton collaboration, shearling, and the exotic vest are out of prices.

**Craft and tech.**
- Proposed craft is **4**. The El Paso factory has partial evidence:
  - The brand's own blog places "the El Paso factory" at its Walter Jones Blvd location and quotes a 33-year worker.
  - Our Process documents pegging, hand lasting, hand stitching and hand tooling, with step photos.
  - 183 of 278 men's boot/shoe records say "Handmade in Texas".
  - What is missing: no filing was found, the site gives no full address, and owned versus leased is not shown.
  - Apparel is sourced: Italy 18, USA 7, Vietnam 6, India 2, Canada 1. 76% of styles state no country, and no maker or mill is named.
- Proposed tech is **1**: no named fabric technology.

**Contradictions with the worklist or record.**
- The worklist "why" says "own stores across Texas and the Southwest". That is consistent with the carried count.
- The worklist reads "shoes" for what it sells. The site also sells a 139-style men's apparel range: shirts, sport coats, outerwear, denim and knitwear.
- PitchBook gives founding as 1983 and an acquisition in 2010. The brand gives 1883, and its chairman says he bought the company after 1997. Ownership is filed from the brand's blog. PitchBook is noted here only.

**Mark as written.** `mark_as_written: LUCCHESE`. The logotype is all caps with "SINCE 1883"; copy writes "Lucchese Bootmaker". Key kept.

**Not reached / NC.**
- **Vinted:** `/brand/lucchese` served a generic catalogue, and the brand-search API returned HTTP 403. I stopped at the first 403, per the spec.
- **GOTS:** not checked.

Status is `partial`.

## Flags for merge
- **Sport-coat line:** the Lucchese Sport Coat appears under 18 separate article numbers (one per cloth) and is counted as 18 styles. The same applies to the Golf Polo (5). The rule says to count by article number, and that is what was filed.
- **Article stem AZ20042:** it carries titles from two shirt lines (El Paso Cowboy Fit, El Paso Square Dobby, and one "San Antonio Cowboy Fit"). It is counted as one style.
- **Lasso Houston Rodeo Tee:** it carries the Houston Rodeo logo, an event licence and not a team or league. It is kept in the census and does not affect prices.
- **Suspicious compositions:**
  - Wyatt Chore Coat: 64/10/11, which sums to 85%.
  - Daniel Sweater: the description says "wool blend"; the bullets say 60% alpaca / 40% silk.
  - Both are filed as read.
- **Fur-on and sheepskin pieces** (Kyle Shearling, Shearling Trucker "100% Sheepskin", Dustin vests, McGuire Vest with muskrat lining) are counted in the census as leather-class. None is priced.
- **Dress-shirt rule:** Western snap-front shirts are the house staple. Should snap-front count as button-front? If so, the dress-shirt low would be $165 (Austin Classic Fit).

**Out of scope but noticed.** The site also has women's apparel, home goods and a Made-to-Order program. `/pages/dealer-sign-in` points to a wholesale dealer network that the brand does not list publicly.


## Maison Kitsuné: full record, wave B batch 4 (read 11 Oct 2026)

**Checked:** US store maisonkitsune.com/us/. The platform is Magento (Hyvä) with Algolia search and Global-e pricing, in USD. The men's Ready to Wear grid shows 312 tiles over 8 pages. That matches the 312 records the page's own Algolia index (`mk_live_us_products`, category "Men /// Ready to Wear") returns. The index was read in-page; it carries `mk_composition`, price and stock. The 7 RTW sub-listings and the men's shoes listing were opened. 17 PDPs were opened, mainly for the TRACEABILITY "Made in" field and descriptions. Also read: the Savoir-Faire page, About, Founders, Fabrics & Care, the SS27 show page, Grailed and the B Corp directory.

**Section 4:** Carried over as instructed; the locator was not re-read.
- US: 0 own doors (positive zero).
- World: 63 non-US boutiques, plus 30 cafés and 3 archives. Two Vancouver entries are miscoded US.
- worklist_conflict: worklist says NYC stores, café.
- The About page says "38 locations ... including New York City ... and Los Angeles" and "more than 400 points of sale". That text is stale (it says "nineteen years" and carries a 2021 copyright). It is noted here only and is not a door source.

**Prices:** All 8 slots read. Nothing was on markdown.
- Tee $115–340 (range).
- Polo $130–260 (range).
- Dress shirt $250–430 (range). Maison Kitsuné makes no dress shirt, so casual button-fronts are used.
- Jeans $330 (two styles at the same price).
- Dress pants $390 (single: the wool flannel cropped pleated pant).
- Sweater $380–565 (pair: extrafine merino crew, then 78% alpaca crew).
- Outerwear $535–940 (range).
- Shoes $575 (the one loafer).
- Not priced:
  - MK x Kuro collaboration.
  - Savoir-Faire capsule. The brand's own page calls it "a premium capsule".
  - Paraboot collab.
  - Café Kitsuné-label merchandise.
  - Kids pieces.
  - Sold-out older-season articles still listed in navigation.

**Fibre (complete):**
- 195 men's clothing styles from 310 colourway records. 194 state a composition.
- How the 195 are counted:
  - Styles are counted by article number (model + fabric code), with the colour suffix dropped.
  - 183 come from the RTW tree. Seven "Fox Head Kid" pieces sitting in men's RTW were excluded.
  - 12 are men's pieces reachable only through men's Selections.
- Split by fibre: 91% natural, 6% synthetic, 2% cellulosic, 1 undisclosed.
- Stretch: 6 styles have any spandex on the main fabric line. Only 1 is at 5% or more (the boxer pack).
- Shape is **one**. Outerwear is the most synthetic category at 7 of 17, and it is still natural-led.
- **Line verdicts:**
  - All-natural: Our Foxes (82 styles, 94%), MK x Kuro (12), Fox Head (9), Grey Fox (9), Savoir-Faire (8).
  - Mixed: Our logos (29, 86% natural).
  - No line is wholly synthetic. 57 styles sit in no named line.
  - 129 of 195 styles are 100% cotton.

**Stockists:** One `none` row. The locator lists own boutiques, cafés and archives only, and /us/stockists, /us/retailers and /us/points-of-sale return 404.

**Proposed craft 2 / tech 1:**
- Craft:
  - Every PDP sampled states the country (14 of 14; Portugal 7, China 3, then Italy, Morocco, Romania and Lithuania with one each).
  - No maker, mill or owned facility is named.
  - The "Paris atelier" (Savoir-Faire page) is a claim. The Kojima, Okayama making belongs to the Kuro collaboration.
- Tech: water repellency and "technical" fabrics are all unbranded.

**Not reached:**
- Vinted: NC.
- GOTS directory: not checked. Organic cotton is stated, but no certification is claimed.
- Founding year: not stated on any page read. 2002 is filed as an inference and flagged.

**mark_as_written:** Maison Kitsuné. Page titles read "| Maison Kitsuné"; the homepage logo link reads "MAISON KITSUNÉ PARIS".

## Flags for merge
- **Savoir-Faire capsule.** The brand calls it a capsule, so it is never a high. Its double-face 100% cashmere Double Breasted Coat ($2,315) also sits in the regular men's RTW Outerwear listing. If Sebastian treats it as regular range, outerwear high becomes $2,315.
- **Sold-out older-season articles still in navigation.** These are the 32 sold-out tiles on page 8, from AM/FM/GM/HM/JM codes. They are counted in the census but not priced. Pricing them would move tee low to $100 and sweater low to $305.
- **Café Kitsuné-label tees and sweatshirt.** These are in men's RTW and counted in the census, but not priced. Café Kitsuné is a sister label. Tee low would be $94 if they counted.
- **Founding year 2002 is inferred.** It is not stated on the brand's pages; please confirm.
- **Sweater slot.** No majority-cashmere crewneck exists. The 70/30 wool-cashmere piece is a hoodie ($620).
- **Suspicious compositions, all filed as read:**
  - The Wool Blend Fleece Hoodie lists "1% OTHERS FIBERS".
  - The Leather Bombardier has a shearling collar.
  - The Oversized R-Neck Pullover states no composition in the feed or on the PDP.
- **JSON-LD price does not match the displayed price.** PDP JSON-LD `price` is the displayed USD price divided by 1.2 (e.g. 316.67 for $380). Displayed prices were used.

**Out of scope, noticed:** The About page is out of date (it says "nineteen years" and gives 38 doors and 18 cafés). The site also sells Kitsuné Bien-Être fragrance and Café Kitsuné coffee in the men's tree.


## Marni: full record, wave B batch 4 (read 11 Oct 2026)

**Checked:** The US store is www.marni.com/en-us. It runs on Salesforce Commerce Cloud (site MarniUS) and prices in USD.
- **Men's Ready-to-Wear grid:** the site states 122 results, which are 114 products plus 8 "Look" tiles. I paged it through Search-UpdateGrid (cgid marni-man-rtw, 60 a page, stopping at the stated count). I also read every sub-category: Shirts 41, Knitwear 22, Coats & Jackets 23, Pants 29, Co-ords 16, Denim 4, Sweatshirts & T-shirts 1. Every sub-category product is also in the RTW grid. The first 60 of the 82 men's New-In RTW tiles were checked, and none fall outside it.
- **Product data:** I read the Product-Variation JSON for all 114 products, one at a time, 1.5 s apart. It gave composition, country of making and sales/list price. There was no block or WAF at any point.
- **Also read:** men's shoes (25 tiles), store locator page, Marni Story, Cosmos of Marni, the SS27 lookbook, the OTB brand page and the OTB FY2025 results release.

**Section 4:** Carried as instructed and the locator was not re-read: 9 US own doors, 2 US outlets (Cabazon is classed as an outlet by name, though isOutlet=false), 82 non-US listed with formats not split, world NC. otb.net says "96 stores across the world". That is a parent-company figure, so it is noted here and not used.

**Prices:** All 8 slots were read. No markdowns: price.list is null on every product.
- Tee $450–795 (range).
- Polo $575–850 (range).
- Dress shirt $595–2,100 (range). Marni makes no formal dress shirt, so casual poplin button-fronts are used.
- Jeans $695–1,550 (range).
- Dress pants $670–2,100 (range, all wool).
- Sweater $1,195–1,850 (pair). The entry crewneck is already 100% cashmere.
- Outerwear $1,450–5,600 (range). The high is a nappa lambskin jacket.
- Shoes $1,195 (single). It is the only loafer.

**Fibre (complete):**
- 101 men's clothing styles, all with composition, from 114 colourway products. A style is the article+fabric stem (first 16 characters of the id), with the colour suffix dropped.
- Split by fibre: 88% natural, 10% synthetic, 2% cellulosic. Spandex 0. There is 1 swim style.
- Shape is **one**. Outerwear (18 styles) is the most synthetic category at 5 of 18 nylon pieces, but it is still natural-led.
- **Line verdicts:** the only named line with 5+ styles is Co-ords (navigation, 15 styles), which is **mixed** (13 natural, 2 synthetic "techno fabric"). No line is wholly natural or wholly synthetic. 86 styles sit in no named line.

**Stockists:** None listed. There is one `none` row: the locator shows Marni stores only, and /en-us/stockists and /en-us/retailers return 410.

**Proposed craft 2 / tech 1:**
- Craft: country of making on 101 of 101 (Italy 73, Romania 19, Portugal 8, Albania 1). No maker, mill or owned workshop is named. "Artisanal workmanship" on the story page is a claim.
- Tech: unbranded "techno fabric" and water-repellent taffeta only.

**Owner:** OTB S.p.A. (Renzo Rosso), from the OTB FY2025 results release (17 Feb 2026) and the otb.net brand page. Neither names the founders. Consuelo Castiglioni is taken from press, so it is the weakest cell.

**Not reached:** Vinted is NC. The B Corp and GOTS directories were not checked (NONE is on the brand's own claims).

**mark_as_written:** MARNI. The story copy and OTB write MARNI; page titles write "Marni"; the logotype was not checked separately.

## Flags for merge
- **Polo high.** A 100% cashmere "polo jumper" ($1,550, POMG0096) sits in Knitwear and Shirts. Polo is filed as cotton range 575–850. If Sebastian treats it as the elevated polo, polo becomes a pair at 575–1,550.
- **Shoes.** The "Black leather loafer" is described on its PDP as a Wallabee shoe with strap and buckle. It is filed as the only loafer.
- **Fur-on excluded from outerwear high:**
  - Red fur coat $13,600
  - Cream shearling jacket $8,000
  - Green leather jacket with shearling panels $4,900
  - Fur-collar nylon jacket $3,600
- **Fur-on garments in the fibre census.** Shearling and fur garments are kept in the census. Lamb fur is counted as other-natural.
- **Suspicious composition (filed as read).** Green leather jacket with shearling panels (JUMY0201): the composition states only "100% PBV", while the PDP copy says calfskin with shearling.
- **House fibre codes.** Some compositions are written in house fibre codes (CO1, CO2, WVW, WSK, LYW, PLW, PBV). They are mapped in the style notes, and LYW and PBV were checked against PDP copy. The JSON list splits "Viscose / Rayon" and "Polyamide / Nylon" into two entries. I rejoined them as one fibre.
- **Light blue striped poplin bloomers.** Swimwear URL and beachwear master category, sold as a co-ord. Filed as underwear-swim.

**Out of scope, noticed:** Shoes sold in men's include calf-hair and pony-hair sabots, which are fur-on and would never be priced. The 8 "Look" tiles in the RTW grid are shop-the-look bundles, and they are excluded.


## Moose Knuckles: full record, wave B batch 4 (read 2026-10-11)

**What was checked.** I read the US store at mooseknucklescanada.com/en-us. It runs on Shopify, prices in USD, and `Shopify.currency.rate` is 1.0. The root `/products.json` holds 666 products (3 pages; page 4 empty). The men's range is the union of 23 men's navigation collections: 207 clothing products plus 44 accessories. `men` (207) equals `men-outerwear` (113) plus `men-clothing` (97), less 3 products that sit in both, so the census is complete against the house's own tree. Every colour is its own product handle, carrying an article code (`m35mj128s-1723` = article m35mj128s, colour 1723). That gives 96 articles. Collapsing the letter suffixes (s, gs, g, h, sh: finish, Gold Series hardware, print) to the numeric stem gives **83 styles**, with a colourway ratio of 207/83.

I read one product page per article (96 pages, 1.5 s apart). The composition sits in the "What's Inside" block in the server-rendered page; it is not in the feed's `body_html`. All 96 state a composition and a country of making. There were no blocks.

**Section 4** was not re-read. The counts are carried as instructed: 4 own doors in the US, world NC, plus 3 US outlets.

**Stockists.** These come from the same Stockist widget feed (405 rows worldwide). It has 168 US "Stores Selling" rows (105 at four department stores, 58 at other shops, 5 online-only) plus J-Bees, which carries no tag. `stockists.csv` has 62 rows:
- 58 US shops, including City Hill in Tumon, Guam, coded GU on the Puerto Rico precedent
- 4 online-only accounts: Amazon, Farfetch, Oc2Ber and Shopbop. The feed gives these no country.

Two duplicate feed rows were dropped: Kittery Trading Post and Amazon. The feed leaves `state` blank on almost every US row, so I filled state from the ZIP prefix and said so per row. Leading zeros the feed lost were restored. Two odd ZIPs were kept as given and noted: Red Carpet "1223" and City Man "48021".

The chain rule applies to four department stores, which have no rows:

| Chain | US doors (unique addresses) | Feed rows | Departments listed |
|---|---|---|---|
| Saks Fifth Avenue | 17 | 42 | Accessories, Men, Women, Kids |
| Neiman Marcus | 15 | 36 | Men, Women, Kids |
| Nordstrom | 11 | 18 | Men, Women |
| Bloomingdale's | 9 | 9 | Men & Women |

Asphalt (4 doors), S&W (4) and Gus Mayer (2) fall under the 5-door threshold and are written as rows. Seven of the shops are children's boutiques by name; they are kept, and the register door rule will sort them.

**Prices** (USD, full price; no compare-at prices anywhere in the men's range):
- **Tee:** $95 (Yul Classic) to $175 (Dalon, Pima). Range.
- **Polo:** $125 (Yul) to $195 (Dalon). Range.
- **Sweater:** $475, single. The Gold Series Elowan Crewneck (72% viscose / 28% polyester) is the only men's knit crewneck.
- **Outerwear:** $445 (Dalon Bomber, cotton) to $1,495 (Neo Bunny Leather Jacket). Range. Applying the outerwear-house rule:
  - Fox fur is excluded: Pioneer Fur & Down Parka $2,495 and Pioneer Down & Fur Bomber $1,995.
  - Shearling or sheepskin trim is excluded: Gold Series Original Stirling Parka $1,594, the Original 3Q, Ballistic and Stirling parkas, Toba and Falcon.
  - The high is the dearest fur-free jacket. Two fur-free Gold Series down jackets (Suthep, Stagg) are also $1,495.
  - No fur-free version of the trimmed Originals is sold to men.
- **Dress shirt, jeans, dress pants and shoes:** NONE.

**Fibre verdict.** The range is split: 58% natural, 40% synthetic and 2% cellulosic, with 83 of 83 styles disclosed. 13 styles contain elastane, 11 of them at 5% or more.
- Outerwear (48 styles) is synthetic-led: 30 synthetic, 17 natural (the 74/26 cotton-nylon Originals and Banff shells, plus leather and wool) and 1 cellulosic.
- Tees and polos (13), sweats (12), trousers (7) and shorts (2) are cotton-led.

Lines with 5 or more styles:

| Line | Styles | Verdict |
|---|---|---|
| Dalon | 8 | all-natural (cotton bodies, nylon-blend contrast panels) |
| Hartsfield | 8 | all-natural (100% cotton) |
| Yul | 6 | all-natural (cotton-led; 4 are 72/28 cotton/poly) |
| Originals | 5 | all-natural (74/26 cotton/nylon shell, shearling trim) |
| Gold Series | 19 | mixed: 14 natural / 3 synthetic / 2 cellulosic |
| Bunny | 5 | mixed |

Smaller series (Everest, Iceberg, Brixton, Freehang, Kings, Soho, West-Ed) are all-synthetic. Lines were identified from the navigation collections and the title series.

**Mark as written.** `mark_as_written: MOOSE KNUCKLES`. The storefront title writes "Moose Knuckles"; the domain and copy write "Moose Knuckles Canada". The key is kept.

**Craft 2, tech 2.**
- **Craft:**
  - Every product page states a country of making, but none names a maker or mill. All 96 articles say China (50), Vietnam (33) or Peru (13).
  - The Craftsmanship page claims "three factories" in Canada with 200+ staff, 74 operations a coat, and six named workers. It names no factory or place, and no current men's article says Made in Canada. This is a claim, not evidence.
- **Tech:** the house names its own shearling treatment (Arctic Shearling, Neoshear, which is fur-on) and one recycled "Memory" fabric. Nothing else is named, owned or licensed.

**Contradictions with the worklist or record.**
- The worklist "why" says "US stores"; that is consistent with the 4 carried doors.
- The site's "made in Canada" claim for core coats contradicts every current men's product page; see Craftsmanship above.
- A FashionNetwork headline (July 2021) says the brand "goes fur-free", but the US store still sells two fox-fur pieces, and the Fur Policy page defends fur.
- Press (FashionUnited, 6 Oct 2026) says the brand operates "almost 50 stores worldwide, including pop-ups". Press is not a door source; this is noted only.

**Ownership.** Cathay Capital has been the majority owner since 2019. Bosideng took a stake of more than 30% in 2024, and founders Noah Stern and Ayal Twik exited as shareholders (FashionUnited, 2024 and 2026).

**Not reached / NC.** Vinted was not read. The Grailed URL resolves, but listings did not render. The FW26 lookbook page was read, but its men's content was not confirmed, so `lookbook_mens` is NC. Status is `partial`.

## Flags for merge
1. **Dress pants:** there is no dress trouser or chino. The candidates are Nomad Pants ($325, nylon/poly/spandex technical), Speedy Pants ($295, polyester) and Hartsfield Straight-Leg Pants ($275, cotton fleece). All are filed NONE. If technical pants count, the slot becomes a range of $295 to $325.
2. **Sweater:** the only knit crewneck is a Gold Series piece in viscose/poly, listed by the house under Sweatshirts & Hoodies. It is filed as a single at $475. Gold Series is treated as regular range: it sits in navigation with no limited-edition wording, and its copy reads "Luxury doesn't have to whisper".
3. **Outerwear low:** the Dalon Bomber ($445, cotton) is a sweat-weight bomber that the house files under Bomber Jackets. If it is ruled a sweatshirt, the low becomes $495 (Charlesbourg Jacket).
4. **Style collapse:** Gold Series and print versions share the base numeric stem, so they are collapsed (96 articles to 83 styles). If Gold Series articles should count as their own styles, the total is 96.
5. **Westmount Down Vest:** the composition reads 75% cotton / 26% recycled nylon (101%). It is filed as read and flagged in the style note.
6. **Stockists:** J-Bees (Detroit) carries no filter tag on the feed and is kept as a stockist. City Hill, Guam, is kept as GU.

**Out of scope but noticed.** The store sells women's, kids', bags, hats and gloves. A "Check Authenticity" page and counterfeit warnings exist. The Sustainability page is headed "We are not a sustainable brand".


## Nanamica: full record, wave B batch 4 (read 2026-10-11)

**What was checked.** nanamica.com geo-redirects to **us.nanamica.com** ("nanamica NEW YORK"). It runs on Shopify, prices in USD, and `Shopify.currency.rate` is 1.0. The site search at `/search?q=` returns results ("shirt" gave 95), and the displayed prices match the feed. I read the full `/products.json` feed (152 products) and `/collections/mens` (150). I read the STORE page and its 8 store detail pages, the stockists page, the About page and the company profile on the US site. On the Japanese site I read www.nanamica.com/store/ and /company/. For ownership I read Goldwin's securities report (有価証券報告書) as text on edinetdb.jp. I also checked the 2026FW men's look page and Grailed.

**Section 4 (own doors).** The brand's STORE page lists 8 doors. One is in the US: nanamica NEW YORK, 123 Wooster St, SoHo. It is run by nanamica USA Inc. The US company profile gives that company's address as 123 Wooster St and its founding as May 2019. The worklist claim "NYC store" is confirmed. Outside the US there are 7 doors:
- Japan (6): Daikanyama, D.W.S. (women's), MOUNTAIN in Daikanyama (sells THE NORTH FACE Purple Label), Kyoto, Kobe and Fukuoka.
- China (1): Wukang, Shanghai.

No outlets, concessions or pop-ups are listed. The NY page carries no coordinates (its map is a goo.gl short link), so lat/lon is NC. The Japanese /company/ page lists the same 8 stores.

**Stockists.** The brand's stockists page lists **20 US shops**, all independents, including A-PRIORI, Independence, WEST NYC, Pilgrim Surf + Supply and The Darkside Initiative (2). The page also lists about 200 shops outside the US. It names HBX and Mr Porter as online stockists; I left them out because they are not US shops. Dealer chains with 5 or more US doors: none.

**Scope.** The whole range is unisex: codes end in U and products are tagged MEN+WOMEN. The men's census is /collections/mens less the following:
- 4 skirts and 2 dresses, which appear only in the WOMEN navigation facets
- a camisole sold only in sizes 0/1
- the women-only Band Collar Shirt
- all non-clothing: hats, bags, belts, bandanas, footwear, books and the gift card

That leaves **115 styles**, counted by the house NUMBER (product code). Each code covers its colourways (301 colourways in all). The count includes 8 coming-soon styles and some archive-season stock that sits in /collections/mens.

**Fibre verdict.** Composition is stated for all 115 styles (the MATERIAL line in the product body). Note that the Brewed Protein share below falls outside natural/synthetic/cellulosic, so the three figures add to 99%, not 100.

| Fibre lead | Styles | Share |
|---|---|---|
| Natural | 63 | 55% |
| Synthetic | 47 | 41% |
| Cellulosic | 3 | 3% |
| Brewed Protein (Spiber) | 2 | 2% |

- **No elastane anywhere.** ALPHADRY's stretch comes from 24% Elasterell polyester, which is elastomultiester.
- **Split range.** Outerwear (JACKET/COAT) is synthetic-led: 27 of 41 styles. Tees (14/21), shirts (11/16), trousers (10/17), denim (6/6) and sweats (8/10) are natural-led.
- **Lines.** The ALPHADRY line (6 styles) is all synthetic. The OOAL series (35) is mixed, 16 natural and 16 synthetic. COOLMAX (11) is mostly cotton-led blends. GORE-TEX (7) is mixed: 5 polyester or nylon, 2 Cotton GORE-TEX. Denim is cotton-led but 20–30% polyester (CCY yarn).

**Prices (USD).**

| Garment | Low | High | Basis |
|---|---|---|---|
| Tee | $90 | $180 | range |
| Polo | NONE | NONE | |
| Dress shirt | $220 | $430 | range |
| Jeans | $270 | $390 | range |
| Dress pants (chinos) | $230 | $270 | range |
| Sweater | $300 | $300 | single |
| Outerwear | $370 | $1,130 | range |
| Shoes | NONE | NONE | |

- Polo is NONE because the brand makes none.
- The dress shirt figures are casual woven shirts. There is no formal dress shirt.
- Dress pants are chinos because there is no dress trouser.
- The only sweater is the polyester Crew Neck Sweater.
- Outerwear low is the ALPHADRY Field Jacket and high is the 2L Cotton GORE-TEX Balmacaan Coat. The coming-soon $1,250 down coat and the limited Spiber pieces were not used.

**Craft and tech.** I propose tech **4** and craft **2**.
- **Tech:** licensed GORE-TEX, WINDSTOPPER, PERTEX, PRIMALOFT, CORDURA and COOLMAX, used across 38% of styles. Cotton GORE-TEX was co-developed with Gore Japan, and ALPHADRY is the parent Goldwin's fabric.
- **Craft:** there is no owned or named clothing maker or mill. Only 2 of 115 styles state a country. The only documented process is the loopwheel COOLMAX jersey. Sanyo Leather (a tannery) is named only on the footwear collaborations.

**Origin and ownership.** nanamica inc. (株式会社ナナミカ) was founded in March 2003 in Shibuya, Tokyo. Its CEO is Takeshi Nomura, and the brand's About page names Eiichiro Homma as founder. Goldwin's securities report lists 株式会社ナナミカ as a consolidated subsidiary 96.7% owned by Goldwin (TSE 8111), and nanamica USA Inc. as 100% owned. The edinetdb page is labelled "latest", but the text I matched shows 2022年3月期 (the year to March 2022), so a newer report may differ slightly.

**Mark as written.** `mark_as_written: nanamica` (all lowercase).

**Not reached.**
- Vinted: /brand/nanamica served a generic catalogue and the brand API returned 403, so I stopped there.
- B Corp directory: the search query was not applied. No GOTS claim appears in any of the 152 feed descriptions.

## Flags for merge
1. **Shoes are NONE by analogy.** All own-label footwear is either a REGAL collaboration (GORE-TEX Plain Toe Shoes $470, GORE-TEX Chukka Boots $510) or a limited beach sandal ($30). I applied the limited-edition ruling to collaboration-only footwear. The alternative is a low of $470 with no high.
2. **Unisex scope.** I excluded the skirts and dresses that also carry the MEN tag, and the size 0/1 camisole.
3. **Brewed Protein (Spiber) fibre.** It has no class in the standard list, so I filed it as `other` (2 styles).
4. **Elastomultiester stretch.** ALPHADRY's stretch is not elastane, so spandex is 0. The 6 ALPHADRY styles are stretch cloth all the same.
5. **The worklist's "Japanese" label.** It is right on origin, but the owner is Goldwin, a listed group. The map may want to show that.


## On: full record, read 2026-10-11

**What was checked.** Everything was read in Chrome, tab 39485851, on www.on.com `/en-us/` (Nuxt front end, Algolia product index), on On's shop locator at customer-service.on-running.com, and on sec.gov. The proxy blocks direct downloads from both On hosts, so all data was read in the page and copied out.

**Own doors (section 4).** On has two first-party store sources, and they disagree.
- **On stores page** (`/en-us/explore/stores`, linked as "On stores" in the footer): 51 own stores. 19 are in the US, and 32 are outside it (Asia 14, Europe 13, Oceania 2, South America 3).
- **Shop locator** (`customer-service.on-running.com/en-us/dealers`, linked as "Shop locator"): its JSON (`/dealers/search?all`) holds 10,072 points, 2,847 of them US or PR.
  - It has 13 On-bannered US rows. They cover 11 of the 19 stores, list Austin and Williamsburg twice each (duplicates dropped), and add **2 "On Outlet" doors**: Woodbury Common and Las Vegas North.
  - 8 of the stores-page doors are missing from the feed.
- **US: 19 own doors + 2 outlets.** The worklist claim "own US stores" is confirmed. There are no concessions or pop-ups.
- **Lat/lon:**
  - 11 rows use the locator's own coordinates. The Chicago Rush St row has a positive longitude in the feed, filed as read.
  - 2 use coordinates from the Google Maps place links on the stores page (Newbury St, Chestnut St).
  - 6 are `NC`, because their links are short or cid links with no coordinates.
- **World:** `world_non_us` = 33 (32 stores plus the Bicester Village outlet), and `own_doors_world` = 51. The stores page lists **no mainland China store**.
  - The FY2025 20-F gives 67 retail locations at 31 Dec 2025: 14 Americas, 10 Europe, 5 APAC excluding China, and 38 in China including Hong Kong. That is mentioned here only, not used as a count.
  - Today's page shows 22 own stores in the Americas (US 19, Chile 1, Brazil 2), so the fleet has grown since the filing.

**Stockists (section 5).** These come from the same locator feed, US and PR only.
- **Chains with 5 or more US doors are summarised here, not written as rows** (1,832 rows): Fleet Feet 203 (52 Premium); REI 193; JD Sports 194; Tradehome Shoes 112; Nordstrom 110 (department store); Browns/Brown's Shoe Fit Co. 58; Shoe Palace 49; Road Runner Sports 45; Von Maur 37 (department store); Fit2Run 36; Anthropologie 34; Scheels 29; Mountain High Outfitters 24; Bloomingdale's 19 (department store); Sun & Ski Sports 19; Marathon Sports 18; Gearhead Outfitters 15; Big Peach Running Co. 13; Comfort One Shoes 13; Second Sole 12; Half Moon Outfitters 10; Potomac River Running 10; Sole Desire 10; Mast General Store 9; Runners Roost 9; Great Outdoor Provision Co. 9; Tyler's 8; Gorsuch 8; Shoe Fly 8; JackRabbit 8; Peter Glenn 8; Backcountry 8; Charm City Run 8; Lebo's 7; Whole Earth Provision Co. 7; Running Fit 7; Gazelle Sports 7; Shoe Mill 7; Runner's Depot 7; Sports Basement 7; Big River Running 7; Sole Provisions 7; JAX Outdoor Gear 6; Alabama Outdoors 6; Running Wild 6; Run On 6; Fitness Sports 6; Feature 6; Dick Pond Athletics 5; Pegasus Footwear 5; Columbus Running Company 5; evo 5; The Athlete's Foot 5; Pacers Running 5; High Country Outfitters 5; Sunset Shoes 5; Englin's Fine Footwear 5; Sole Sports Running 5; Incredible Feets 5; Super Runners Shop 5; Grivet Outdoors 5; TC Running Co. 5; iRun 5; Sportive 5.
- **Dick's Sporting Goods has 307 rows.** 41 of them carry a store address in the name field with all fields shifted; they were identified as Dick's from the feed's website field.
- Chains were grouped by name prefix, plus the feed's website field.
- **That leaves 1,000 rows** in `stockists.csv`. `shop_kind` is a reading of the name, because the locator gives no type.
  - The note column carries the locator's own tier (Premium retailer / Retailer) and its has_apparel flag. Most rows are running-shoe specialists with no On apparel.
  - Club, resort and institution shops are flagged, and 5 rows are other brands' own doors (Stio, Birkenstock, Onward Reserve).
  - Apply the register tests before merging. Many of these doors fail door one, since they sell shoes and not clothing.
- 3 shifted or swapped fields in the feed were corrected by hand and noted (Lloyd's Carmel, Front Running Sports, Hanson's Royal Oak). Brainerd's state was blank and is filled from its zip, as noted.

**Prices and listing links.** Full prices are the Algolia `basePrice` in USD, read with the store's own listing filters.
- Ranges for tee, polo, outerwear and shoes. No loafer exists. LN1 limited editions and the $310 LightSpray Cloudboom Strike 2 (limited edition) were excluded.
- `NONE` for dress shirt, jeans, dress pants and sweater: On sells no woven shirt, jeans, trouser, chino or knit sweater.
- Search is an overlay only (`/en-us/search` returns 404), so `search_url` is `NONE`.

**Fibre (section 3).** The census is complete for the men's apparel navigation.
- 114 styles by style code (333 colourways), matching the PLP's own "114 RESULTS".
- Composition and country of origin come from each PDP's server-rendered Materials block. All 114 were fetched one at a time and **all 114 state a composition**.
- **24% natural (all cotton), 76% synthetic, 0% cellulosic.** 54 styles carry elastane on the main line, all at 5% or more.
- Shape is **split**: Hoodies and Sweatshirts are natural-led, and Tops, Shorts, Jackets, Pants and Tights are synthetic-led.
- **Line verdicts (from the feed's `family` field):**
  - **Club is wholly natural**: 17 styles, cotton or cotton-rich fleece, made in Turkey.
  - **Wholly synthetic**: Performance 27, Core 10, Court 10, Zero 6, Train 5. That is 58 of 114 styles.
  - **Mixed**: Focus (7 cotton-blend, 2 synthetic) and Courtside (6 synthetic, 2 cotton terry).
  - Two styles sit in no line.

**Owner.** On Holding AG (NYSE: ONON), Form 20-F for FY2025 (filed 2026-03-03).
- Class B voting-rights shares held by the extended founder team concentrate voting control.
- Substantially all products come from third parties: fewer than 30 suppliers, 16 of them for apparel. In 2025, 65% of apparel units were made in Vietnam, 29–30% in Turkey and 5–6% in China (the filing gives both figures).
- A Zurich LightSpray production facility opened in 2025.

**Not reached:** lookbook, Vinted, Grailed, B Corp and GOTS (all `NC`). The mainland China store list (on-running.cn) was not read.

**`mark_as_written: On`**

## Flags for merge
- **World count.** `own_doors_world` = 51 is the on.com locator figure. The locator leaves out mainland China, which the filing puts at 38 locations including Hong Kong. Decide whether to file 51 or `NC`.
- **Outlets appear only on the shop locator** and not on the stores page. They are filed as outlets because both are labelled "On Outlet" and sit in named outlet centres.
- **Two locator sources disagree** on 8 US doors. All 19 stores-page doors are filed, because the stores page is the brand's own list of its stores.
- **Unisex and limited items in the men's navigation.** 3 unisex styles (2 of them LN1) and 4 LN1 limited-edition styles are counted in the census, because they are in the navigation, but never priced.
- **Club-T composition differs by colourway.** The colourway read says Cotton 100%; another in the page payload says 100% organic cotton. Filed as read.
- **Tights** were put in category `other`, because the standard set has no tights category.
- **Tech 4, craft 2** as proposed. Tech: owned, trademarked footwear technology, and On-named fabric technologies on 35% of men's apparel. Craft: country of origin is stated on 100% of pages, but no maker or mill is named, and the only owned facility is the new LightSpray line in Zurich.


## Palace: full record, wave B (read 11 Oct 2026)

**What I checked:** usa.palaceskateboards.com in Chrome. The store is Shopify Hydrogen (Oxygen), so `/products.json` and `.js` return 404, the window has no `Shopify` object, and product handles are random strings. I read:
- every collection in the store navigation through its React Router `.data` route, all pages: 655 handles in All, and 18 collections
- the `.data` payload of all 474 clothing, underwear and footwear handles, one at a time about 1.7 s apart, with no block (`technicalDetails` holds the composition; a `style_id` metafield groups colourways)
- the Modern Slavery Statement 2026, the Winter 2026 lookbook and range pages, and the advice index
- off-site: the Companies House PSC registers, Grailed and Highsnobiety

**Section 4:** not re-read, as instructed. Carried: 2 US own doors, world NC, locator /shops.
- The Modern Slavery Statement (FY26) lists retail stores in London, NYC, LA, Tokyo, Osaka, Fukuoka and Seoul. That is consistent with 2 US doors. It is not a door source and is mentioned here only.

**Prices (USD as served, whole dollars):**

| Garment | Basis | Price | Product |
|---|---|---|---|
| Tee | range | $48 | Basically A T-Shirt |
| | | $68 | MMIX Heavy Slub |
| Polo | range | $128 | Skull Crest Polo |
| | | $138 | Legacy Polo |
| Dress shirt | range (casual button-fronts only) | $158 | Seer Patch Oxford |
| | | $178 | Surplus Flannel |
| Jeans | range | $168 | P45 |
| | | $268 | P90 Baggy Stitch Jean |
| Dress pants | range (no dress trouser or chino; casual trousers used) | $188 | Ripstop Cargo |
| | | $188 | 10 oz Double Knee |
| Sweater | range (no elevated fibre sold) | $168 | P-Stripe Knit |
| | | $198 | Bare P Knit |
| Outerwear | range | $178 | Palace Tracksuit Jacket |
| | | $398 | Danke Jacket |
| Shoes | single | $298 | P-Lux Loafer |

All 8 slots are filled.

**Excluded from highs:**
- Sheepskin Flying Jacket $1,898 (fur-on)
- Palace Avirex leather jacket $1,570
- South2 West8 River Trek $848, shirt $288 and tees $78
- Betty Boop varsity $548 (character licence)
- New York Cubans tee $78 (Ebbets/team licence)

**Fibre census (drop model: the US store navigation on the day):**
- 139 clothing styles by `style_id`, from 456 colourway handles (ratio 456/139). Every colour has its own handle; the brand's style_id is the style.
- One style_id ("P90") grouped the $268 P90 Baggy Stitch Jean with the $168 P90 Baggy Jean colourways. I split it into 2 styles.
- Out of scope: socks (5 styles, 11 handles), footwear (4), hats, bags, accessories and hardware.
- 27 clothing styles are collaborations or licences, kept in the census: South2 West8 7, Avirex 6, Ebbets 5, Judge Dredd 5, Betty Boop 3, Dick Jewell 1. Also Vans (footwear) and 2 MLB socks.
- Composition stated on 139/139.
- Split: 74.1% natural, 25.9% synthetic, 0 cellulosic. No elastane on any main line; the only spandex is a 16% contrast panel on the Polartec 200 hooded jacket.
- Shape `split`: Jackets are synthetic-led (15 of 26), and shell and track joggers make Bottoms-trousers synthetic-led (7 of 12). Tees, sweats, shirts and denim are natural-led.

Line verdicts, for lines of 5 or more styles:
- all-natural: BASICALLY A (7, the basics), SKULL CREST (6), UNISEX (5), Avirex collab (6)
- mixed: South2 West8 (4 natural / 3 synthetic), Ebbets (2/3), Judge Dredd (4/1)
- Smaller series, under 5 styles: RECON, POLARTEC and BIG RIPSTOP are all synthetic; LEGACY, SOFAR and MMIX are all cotton.
- 64 styles sit in no named line.

**Stockists:** none listed. Palace has no stockist page (/stockists 404), and its own pages list only its own shops. One row filed with `none`.

**Craft 1 / Tech 2 (proposed).**
- Craft: no PDP of 474 names a maker or mill or states a country. The statement names Vietnam, China, Hong Kong and Korea as where key factories were visited, and the brand owns no factory.
- Tech: licensed Polartec 200 (3 styles) and Pertex NetPlus (1). Windstopper by Gore-Tex Labs and Pertex jackets appear on the Winter 2026 range page but not in the store navigation, so they are not counted.

**Owner:** GSLT Holdings Limited (10560823) owns 75%+ of Palace Skateboards Limited (08253929). Lev Tanju and Gareth Skewis each hold 25–50% of GSLT. Founded 2009 in London: the year is from press and the brand's 10th-anniversary coverage; the company was incorporated in 2012.

**Not reached:**
- Vinted (no brand id surfaced)
- B Corp directory (JS, nothing returned)
- GOTS (NC)
- no quote found on the brand's own site

**mark_as_written:** PALACE

## Flags for merge
1. **Quote source.** The quote is Tanju's remark to The Guardian (2016), read via Highsnobiety's write-up. I did not read the Guardian original. It meets the voice rule, but the source is secondary.
2. **Outerwear low.** $178 is a polyknit track jacket that Palace lists under Jackets, following the Human Made precedent. If track tops are not outerwear, the low becomes STACKED COACH JACKET $198 (handle w6vtk39k672x).
3. **Dress shirt and dress pants slots.** These are filled with casual button-fronts and casual trousers (cargo and double-knee), not tailoring. NONE is arguable for dress pants.
4. **Ebbets items.** New York Cubans and Sankei Atoms are vendor "Ebbets" with team marks. I treated them as both a collaboration and a team licence.
5. **Suspicious composition.** TOO HAIRY FLAG KNIT reads 48% nylon, 38% acrylic, 18% wool, which sums to 104. I filed it as read.
6. **Ungendered range.** Listing URLs are the house's own category pages. There is no men's split to filter on.

**Out of scope, noticed:** Palace also runs Manor Place (a skatepark and football venue), linked in the footer. The Winter 2026 range page is far larger than the live store (1.9 MB of text), consistent with the drop model.
