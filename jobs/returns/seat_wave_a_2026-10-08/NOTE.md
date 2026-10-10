# seat_wave_a_2026-10-08 — consolidated return, all 36 brands — NOTE

Read 8–10 October 2026. This combines batches 1 (v2) to 4 into one file per schema. It contains:

- `return.csv`: 36 rows × 132 columns.
- `own_doors.csv`: 2,190 door rows.
- `stockists.csv`: 189 rows.
- `return_styles.csv`: 2,255 style rows.

`reconcile.py` gives 36 exact matches, 0 to rewrite and 0 unmatched. Headers, enums and the
no-empty-cell check pass on every file. Facts-first rows are in `facts_first.csv`, returned
8 October.

**Every row is `partial`.** 596 of 4,752 cells (12.5%) are `NC`. The common reasons:

- Fibre on large houses is a documented sample, not a census.
- B Corp is mostly `NC`, because the B Lab directory renders by script and can't be fetched.
- Vinted ids and GOTS were often unreachable once the web-search budget ran out.
- A handful of sites block fetching or browsing outright.

Own US door counts are filed for 31 of 36 brands. The five still `NC` are adidas, Ministry of
Supply, Red Wing, The North Face and Woolrich, each with the reason in `doors_basis`.

| brand | NC /132 | own US doors | craft | tech* |
|---|---|---|---|---|
| Abercrombie & Fitch | 10 | 156 | 1 | 2 |
| adidas | 19 | NC | 2 | 3 |
| Alden | 9 | 2 | 5 | 1 |
| Allen Edmonds | 49 | 55 | 4 | 2 |
| AllSaints | 8 | 17 | 2 | 2 |
| Bally | 5 | 1 | 2 | 1 |
| Birkenstock | 6 | 14 | 5 | 3 |
| Calvin Klein | 14 | 2 | 1 | 2 |
| Chrome Hearts | 50 | 10 | 4 | 1 |
| Cole Haan | 7 | 23 | 1 | 4 |
| COS | 16 | 12 | 2 | 1 |
| Dr. Martens | 10 | 52 | 3 | 3 |
| Dunhill | 16 | 1 | 3 | 1 |
| Gant | 12 | 0 | 2 | 2 |
| Issey Miyake | 9 | 1 | 3 | 4 |
| Johnston & Murphy | 21 | 89 | 2 | 2 |
| L.L.Bean | 14 | 62 | 3 | 3 |
| Louis Vuitton | 22 | 85 | 3 | 2 |
| Mackage | 12 | 4 | 2 | 2 |
| Ministry of Supply | 8 | NC | 3 | 4 |
| New Balance | 22 | 90 | 4 | 4 |
| Nike | 16 | 75 | 2 | 4 |
| Off-White | 18 | 1 | 1 | 1 |
| Orvis | 9 | 31 | 2 | 3 |
| Paul Stuart | 11 | 4 | 3 | 1 |
| Pendleton | 25 | 16 | 4 | 2 |
| Red Wing | 11 | NC | 4 | 3 |
| Stüssy | 18 | 4 | 1 | 2 |
| Supreme | 40 | 6 | 1 | 3 |
| The North Face | 15 | NC | 2 | 4 |
| Tod's | 23 | 8 | 4 | NC |
| Tommy Hilfiger | 14 | 3 | 1 | 2 |
| Tracksmith | 11 | 2 | 3 | 3 |
| Uniqlo | 27 | 87 | 2 | 4 |
| UNTUCKit | 10 | 69 | 2 | 3 |
| Woolrich | 9 | NC | 2 | 2 |

\*Tech is on a provisional 1–5 scale, because no tech rubric was issued.

## How it was read

- Two web-fetch workers ran at a time, one request at a time. An early run of ten in parallel
  exhausted the rate limit and was re-run.
- Store locators and pages that hide data from a fetcher were read in Chrome, one page at a time.
- No block, bot check, login or cart was worked around. Three sites showed a bot check in the
  browser, and the read stopped at each: adidas, COS and The North Face. **Those checks were raised in
  your own Chrome**, so those sites may ask you to verify on your next visit.
- Allen Edmonds prices sit behind "add to cart" and were not read.

## Rulings waiting on Sebastian

There are 31 in all, listed in each batch's `NOTE.md`. The ones that change many rows:

1. **Sample fibre percentages are filed inconsistently. Re-cut them before merging.**
   - Nine houses carry brand-level percentages from a sample with `styles_total` `NC`: A&F, adidas,
     COS, Gant, L.L.Bean, New Balance, Nike, The North Face and Uniqlo.
   - At least five more put the sample size in `styles_total`, or compute percentages over the
     sample rather than over the range: AllSaints (74), Calvin Klein (55), Tommy Hilfiger (60),
     Tracksmith (60 read of 70) and Mackage (86 read of 119).
   - Near-census rows (per-style counts close to the range): Tod's, Issey Miyake, Stüssy, UNTUCKit,
     Bally, Ministry of Supply, Woolrich and Paul Stuart (324 counted, 52 read).
   - `return_styles.csv` holds every style read, so the columns can be recomputed on one rule here.
   - The decision: accept sample figures, or hold the columns at `NC` until there is a census?
2. **Concessions.** Department-store shop-in-shops are counted apart from own doors (Louis Vuitton
   85 not 102, AllSaints 17, Tod's 8). Confirm.
3. **Outlet-only fleets.** Calvin Klein (2 full-price of 115) and Tommy Hilfiger (3 of 139) are filed
   on venue alone, because the locators have no type field.
4. **"Factory"/made-for-outlet styles in prices.** Calvin Klein excluded them and Tommy Hilfiger
   included them. One rule is needed.
5. **Shearling = fur-on.** It is excluded from highs at AllSaints, Mackage, Paul Stuart, COS and Tommy
   Hilfiger. It moves several outerwear highs by thousands of dollars.
6. **Tech rubric.** None was issued, so every `proposed_tech` is provisional.
7. **Bands.** Mackage looks premium, not true luxury. Ministry of Supply (12 live styles, stores
   closing) and Bally (one US door, restructuring) may need their seats reconsidered.

## Biggest corrections to the existing record

- **Bally** is in restructuring and Swiss production has ended.
- **Paul Stuart** was sold by Mitsui in December 2025.
- **Woolrich** has no US locator, and its rights are split between owners.
- **Issey Miyake** has a US e-store.
- **Dr. Martens** sells no men's clothing in the US.
- **Red Wing** sells tees and owns three plants plus a tannery.
- **Orvis** closed 31 stores.
- **UNTUCKit** was sold to Randa.

The worklist "why" lines were wrong or stale for at least 16 brands.

## Not in this return

There is no rebuilt tool and no merge into the map. Working files are not attached.

---

# Per-brand notes

## Abercrombie & Fitch


**Status: partial.** `reconcile.py` found 1 exact match, 0 rewrites and 0 unmatched.

### What stopped the read

- **Not enough reads.** About 12 WebFetch reads succeeded before the WebFetch proxy began returning **HTTP 429** on every request. That covered robots.txt, the sitemap index, the US category sitemap and nine men's listing pages.
- **The block covered every domain.** It hit abercrombie.com, sec.gov, the ANF investor-relations site and Wikipedia, and it continued for more than 30 minutes, with retries spaced 4 to 10 minutes apart.
- **Curl was refused too.** Curl to www.abercrombie.com was refused by the egress policy (403 CONNECT). Neither block was worked around.
- **Pages refused and not retried, as the proxy instructed:**
  - classic-essential-tee PDP
  - premium-heavyweight-20-tee PDP
  - a-and-f-essential-crew-sweater PDP
  - 100-cashmere-crew-sweater PDP
  - mens-tops-all-t-shirts-t-shirts
  - the store locator (ViewAllStoresDisplayView)
  - the "others" sitemap
  - the FY2025 10-K (anf-20260131.htm) and its Ex-21
  - the Q4 FY2025 results release
  - Wikipedia

### What was checked

- **Store and currency.** The store is www.abercrombie.com/shop/us (storeId 10051, a WebSphere-style platform). Prices are in USD on the US path, and many tiles were read. The robots.txt names the sitemap index `/api/ecomm/util/sitemap/index/anf` (48 sitemaps). The US category sitemap lists 191 men's category URLs, and these were used for the listing links.
- **Prices (section 2).** All eight garments are filled from listing tiles. No PDP was read, so no compare-at was confirmed on a product page. Sale tiles show "Was $X, now $Y" and were excluded or taken at the compare-at price. Truncation and judgement calls are given garment by garment in the row's `note`.
  - **Tees:** priced by colour ($19/$25, $35/$40).
  - **Dress pants:** A&F's "Dress Pants" category is the A&F Collins suit trouser line.
  - **Shoes:** own-label is inferred, because the unbranded loafer tiles name no brand. The Sperry and G.H. Bass shoes were excluded as stocked footwear.
  - **Polo high:** this is a judgement call. It is a merino collared sweater that A&F files under Polos. The dearest knit-jersey polo seen was $70.
- **Fibre (section 3).** The sample is listing tiles only: 86 men's clothing styles from 8 listings, deduplicated by title.
  - **Duplicate IDs collapsed.** A&F gives each jean wash and suit-pant variant its own product ID, so these were collapsed by title.
  - **Excluded:** multipack tees, which are the same style.
  - **Compositions found: 24 of 86.** All come from the product title ("100% Cotton …", "100% Merino Wool …", "100% Cashmere …", "100% Linen …"), plus one from tile copy. None comes from a PDP composition field. They are flagged for verification.
  - **The other 62 are `NC`.** Blends named without percentages ("Linen-Blend", "Wool-Blend", "Vegan Leather") are not compositions.
  - **What this does not cover.** The denominator was not established, because the product sitemap was not read. Brand aggregates are therefore `NC`. Categories not reached: graphic tees, hoodies/sweats, shorts, swim, underwear, active and suits.
- **Ownership.** Owner: Abercrombie & Fitch Co. (NYSE: ANF). `ownership_url` is the FY2025 10-K, found by search but not read. The founding facts (1892, New York, David T. Abercrombie) come from general record and were **not verified** from a filing this pass.
- **Resale.**
  - **Vinted:** brand ID 93, from vinted.co.uk/brand/93-abercrombie-fitch (search result only).
  - **Grailed:** /designers/abercrombie-fitch, seen through its category subpages in search results. The root page was not opened.

### What was not reached (all `NC`)

- **US door count:** this was the main ask and stays `NC`. The doors file is header-only. The locator was refused.
- **Figures still on file, from facts-first and not re-read:**
  - 239 Abercrombie-brand stores in the Americas.
  - A truncated locator read showing about 157 "Abercrombie & Fitch" and about 83 "abercrombie kids" US entries before it cut off mid-Pennsylvania.
  - Outlets are not labelled by banner on the locator.
- **Stockists:** not checked, so the file is header-only. It does **not** assert that A&F lists no stockists.
- **Not reached:** tech, craft (the 10-K sourcing language was not read), lookbook, B Corp, GOTS, quote and signature product.

### Contradictions and brief issues

- **Facts-first entry tee confirmed.** The $19 entry tee in facts-first matches this read. Its $240 outerwear top also matches, as the dearest outerwear seen. The coats listing was truncated at 59 tiles, though, so the top is not proven.
- **"200+ US stores" (`worklist why`) is still unverified.**
- **The brief's US door count needs a browser read or the 10-K's store table.** The 10-K reports by region (Americas, EMEA, APAC), not by country. The locator lists A&F, abercrombie kids and outlets on one page, with outlets identifiable only by mall name. A WebFetch read truncates partway through the list.
- **The fibre section is listing-tile only.** Title-stated "100% X" compositions likely describe the shell only. Re-read the PDPs before merging any fibre figure.
- **The tech score scale is provisional.** No tech rubric was issued, and no `proposed_tech` was given.


### Doors — browser read 2026-10-10 (main thread)

own_doors_us NC → 156. Browser read of locator 2026-10-10: 301 US records = A&F 156 full-price + 39 outlet; abercrombie kids 87 full-price + 19 outlet (kids mostly co-located with A&F; 49 share its phone). own_doors_us = A&F-banner full-price incl. 2 coming-soon; outlets from the site's isOutlet flag. World NC: 438 records include e-commerce/inventory entries.


### Re-run 2026-10-10 (gap-fill)

Doors and the door columns were left alone (main thread's browser read). WebFetch worked throughout this time, with no 429. About 110 fetches were made, one at a time. Two PDPs returned a "JavaScript is disabled" shell: essential-popover-20-hoodie-63459319 and essential-short-56790824. One guessed slug errored: mock-neck-sweater-63845820. None was retried another way. `reconcile.py` returned 1 exact match, 0 rewrites and 0 unmatched. **Status: still partial.**

**Prices (section 2), confirmed on product pages.** No compare-at price showed on any figure filed, so all are full price.
- **Tee:** $19 / $40, both PDPs read.
- **Sweater:** the $200 100% Cashmere Crew is confirmed. I read the listing at start=0, 45 and 90 (about 55 styles). It is the only cashmere crew, and nothing dearer appeared.
- **Outerwear:** the $240 Wool-Blend Long Mac is confirmed. The listing ends at about 91 tiles and was read whole. The dearest excluded item is a $210 Collins blazer.
- **Dress pants:** $100 / $130 confirmed. 63481018 shows $130. A second ID under the same title (62037362) shows "Was $120"; both are recorded in the styles file.
- **Changed: `jeans_high` 100 → 110**, Relaxed Workwear Jean (63492820): $110 exact, BODY 100% cotton, "Rigid Denim". The jeans listing has about 120 tiles across start=0, 45 and 90. The low of $80 stands.
- **Not re-read:** shoes (the loafer compare-at is still listing-only), polo and dress shirt.
- **Graphic and licensed tees** run $45–65 and were not used as a high.

**Fibre (section 3).**
- **Sample:** 77 men's styles have compositions read from PDPs across all ten categories (tees-polos 11, shirts 11, knitwear 19, sweats 4, trousers 8, denim 6, shorts 5, outerwear 7, tailoring 1, underwear-swim 5). This is short of the ~100 target because of the fetch cap.
- **Where the composition is:** in the rendered details text ("BODY:" / "SHELL:" lines). WebFetch does not expose the page payload, so it was not inspected.
- **Of the 77 (sample, not the range):** natural-led 81%, synthetic 14%, cellulosic 5%, none undisclosed. 22 styles carry elastane on the main line, 5 of them at 5% or more. The shape is `one`: no category with 10 or more styles is synthetic-led.
- **Synthetic pockets:** Collins suiting (the $100 Suit Pant and the Slim Blazer are polyester/viscose), the Go-To Pant (100% polyester), the Menswear Relaxed Straight Trouser, YPB active and the mesh shorts, swim, and performance underwear.
- **Swim:** 3 styles, and the listing is complete.
- **`styles_total` stays NC:** the range denominator was not established.
- **Still outside the sample:** 14 title-derived compositions and 25 NC rows from 10-08 are kept in the file.
- **Title vs composition contradictions:**
  - "The A&F Collins Linen-Blend Shirt" reads 100% linen.
  - The Sailing Jacket's copy says "a nylon fabric", but its shell line is 75% cotton / 25% nylon. The composition line was used.
  - "Vegan Leather" is a 100% viscose backing with a polyurethane coat.

**Origin and ownership (section 8).**
- **FY2025 10-K, Item 1:** "incorporated in Delaware in 1996". At 31 Jan 2026 the company operated 829 stores: 306 Abercrombie (239 Americas, 36 EMEA, 31 APAC) and 523 Hollister, plus 60 franchise stores. There is no US-only figure.
- **Sourcing (10-K):** about 124 third-party vendors in 15 countries. Vietnam supplied about 37% of receipts and Cambodia about 26%; the largest vendor supplied about 8%.
- **Founding:**
  - 1892 is confirmed by the about page ("1892 David Abercrombie founds Abercrombie Co.").
  - New York City is confirmed by a 30 Jul 2026 company release ("origin in New York City dating back to 1892").
  - The middle initial "T." and Fitch joining / the 1904 rename come from the earlier record. The about page confirms only "incorporated in the state of New York" in 1904.

**Sections 6–13.**
- **Tech:** proposed 2 on the provisional scale.
  - Owned house fabric names: softAF, Vintage Stretch, and YPB's neoKNIT, motionTEK and powerSOFT.
  - Licensed: Coolmax, on the Collins Performance shirt.
  - 14 of 77 read styles (18%) carry a named fabric. softAF is a hand/weight name, not documented R&D.
- **Craft:** proposed 1. All 77 PDPs state only "Imported." (0% give a country). No makers or mills are named, no owned facility exists, and no process is documented.
- **Lookbook:** there is no on-site men's lookbook page. The Fall 2026 "Denim Made Iconic" campaign is mixed men's and women's (NY Giants players for men's), and the source is the IR release.
- **Quote:** from the about page, house voice: "Abercrombie & Fitch is an effortless and elevated American lifestyle brand".
  - Alternative from Corey Robinson, brand president, in the 30 Jul 2026 release: "Abercrombie has been at the intersection of fashion, sport and culture throughout our entire 134-year history".
- **Signature product:** jeans (Relaxed Straight Jean). This is a judgement from the denim-franchise campaign; the brand names no single signature item.
- **B Corp and GOTS:** NC. The B Lab directory is JS-rendered and showed no results through WebFetch. GOTS was not checked. Neither should be read as "no".
- **Grailed:** the /designers/abercrombie-fitch page is live.
- **Vinted:** brand_ids 93 with catalog 5 is confirmed as "Abercrombie & Fitch" / Men, with 500+ results.

**Stockists:** the brand lists none, so the file has one `none` row.


## adidas


**Conditions.** I read with WebFetch and WebSearch only. adidas.com refuses curl at the agent proxy (CONNECT 403), so there was no bulk feed pull. WebFetch returned HTTP 429 for about 25 minutes across every domain. Pages refused that way were not retried:
- `adidas.com/us/stores/united-states`
- `adidas.com/us/men-polo_shirts`
- three adidas Annual Report 2025/2024 pages and the AR25 PDF
- `grailed.com/designers/adidas`

No bot detection was worked around.

### What was checked
- **Store and currency.** I read adidas.com/us in USD (`price_en_us`, $ on the grid). The adidas PLP JSON (`/api/plp/content-engine`) and the product JSON (`/api/products/<article>`) are readable through WebFetch. The product JSON carries `Main Material:` composition and canonical URLs.
- **Feed size (fibre).** The men's clothing grid states 3,278 items (69 pages of 48). The API `count` is 3,286. These are **articles (colourways)**, not styles; the style key is `model_number`.
  - I paginated none of it. WebFetch truncates each JSON page at about 17–35 tiles.
  - I read 16 styles, a purposive spread across tees, polos, shirts, knitwear, sweats, trousers and outerwear. That is about 0.5% of articles.
  - Brand-level fibre percentages are `NC`. On the sample only: 5 natural-led, 9 synthetic-led, 1 cellulosic-led (modal) and 1 undisclosed. Tees and the woven shirt are cotton; trousers, track and outer layers are recycled polyester or polyamide.
  - Composition was present on 15 of 16 product JSONs.
- **Prices.** All eight garments are list prices from price-sorted JSON pages. One caveat applies to every high: **the sort key is sale price, not list price**, so a marked-down item with a higher list price could sit past the pages read.
  - Jeans are `NC`. The search redirects to the adidas "Jeans" sneaker landing, and no men's denim trouser outside Y-3 was seen.
  - The dress-shirt row is a single item: the FS+ woven twill button-up at $65. It is the only non-Y-3, non-collab button-front shirt found.
  - Shoes are a `range` (no loafer), from Adilette Aqua slides at $25 to F50 cleats at $300.
- **Y-3 exclusion.** Every PLP item carries `division`. I skipped every item with `division = Y-3` or a "Y-3" title prefix. That matters, because Y-3 fills the top 16 tees, top 17 jackets and 34 of the top 36 shoes by price. I also excluded both Y-3 Concept Stores from the doors file.
- **Collaborations never used as a high.** Excluded: Willy Chavarria, entire studios, Hellstar, Metallica, Tyrrell Winston, Pharrell Williams, the Mercedes-AMG and Audi F1 team kit, and the SPZL F.C. club polos.
- **Doors.** The index reads "United States (179)". The city list, read from the same locator on adidas.co.in, sums to **177 over 154 cities**. Barceloneta is Puerto Rico.
  - The locator mixes six banners: adidas Store, adidas Outlet Store, adidas Brand Center, adidas Flagship Store, Originals Flagship/Store, and Y-3 Concept Store. The banner is in each store's name, so a full split is possible at one page per city.
  - Banners were read for 5 cities and 18 doors:
    - 9 full-price adidas (Store, Brand Center, Flagship, Originals)
    - 5 outlets
    - 2 Y-3 (excluded)
  - `own_doors_us` and `own_doors_world` are therefore `NC`. The doors file holds the 16 non-Y-3 doors read. The 154-city list is at `scratch/adidas/us_cities.txt`.
  - Many single-store cities are outlet-mall towns (Cabazon, Gilroy, Wrentham, Kittery and others), so the full-price share is likely well under half. That is not established.
- **Craft.** All 16 product pages say only "Imported". adidas says it "outsources most of its production" and publishes a twice-yearly Global Factory List (July 2026 file). The heritage is dated and placed: 18 Aug 1949, Herzogenaurach. **Proposed craft 2**, a borderline call between 1 and 2.
- **Tech.** Tech scale is PROVISIONAL (no rubric issued). All named technologies are owned. 4 of the 16 styles name one in the title or description; the attribute `technologies` list looks like generic filter data and was not counted. **Proposed 3.**
- **Quote.** "Through sport, we have the power to change lives." This is the house purpose statement on adidas-group.com About/Profile (undated page).

### Not reached
- Annual-report store counts (world own-retail, by format): all 429.
- Full US banner split.
- Non-US doors.
- Partner stockists in the storefinder.
- Lookbook, Vinted brand id, B Corp and GOTS directories, and the signature product (all `NC`).
- Grailed `/designers/adidas` is filed from indexed sub-pages (`/designers/adidas/menswear/...`); the page itself was not opened.

### Contradictions and brief notes
- Facts-first's "179" is a locator header and mixes outlets and Y-3. Its city list sums to 177, which I confirm. Do not seat 179 as full-price doors.
- Facts-first's top price ($300 Mercedes-AMG F1 jacket) is team kit, a collaboration, so it is not a high. The outerwear high is the TERREX Xperior Hybrid PRIMEKNIT CLIMAPROOF+ Jacket at $380.
- **"Originals Cashmere Sweater" ($180) is 13% cashmere and 66% modal.** It is not an elevated fibre, and no majority-cashmere knit was found.
- **Brief issue:** for a house where the colourway is the article, "count the feed" through WebFetch gives an article count, not a style count. A style count needs the model-level facet, or a feed pull the proxy does not allow here.

### Re-run 2026-10-10 (gap-fill)

**Conditions.** WebFetch/WebSearch only, one fetch at a time, ~105 fetches. No 429s. The product JSON (`/api/products/<article>`) and PLP JSON (`/api/plp/content-engine?query=<category>`) answered normally through WebFetch; no bot check was served on any URL fetched in this pass. `/api/plp/content-engine/search` now returns ROBOTS_DISALLOWED to WebFetch (not retried). Doors were not attempted: the main thread's browser read hit adidas.com's bot check (HTTP 403 "I am not a Robot") after ~60 city pages; doors_adidas.csv (72 rows) and doors_summary_adidas.txt are unchanged.

**Prices (all eight).**
- I re-read all 13 price products on product JSON. Every cell holds the list price (`standard_price`). Where an item was marked down, the cell holds the compare-at price; none changed.
- Marked-down items: tee high KR4026 lists $100, on sale at $85. JN6799 lists $25, on sale at $19. KS4328 lists $65, on sale at $33. H46100 lists $55, on sale at $28.
- **Jeans: NC → $110–$120 range.** adidas does sell men's jeans. The `men-denim` listing has 29 items, all Originals and gender M. I read the complete list from the price-ascending and price-descending pages together.
  - Low: Firebird Adicolor Denim Jeans KS4966, $110 list ($77 sale), 100% cotton. A second product, SST Denim Jeans IB6947, lists $110 and is not marked down.
  - High: ADILENIUM 6 DENIM Jeans LH3342, $120 list, not on sale.
  - Excluded: SONG FOR THE MUTE ADI008 Denim Pants at $170, a collaboration.
  - The 2026-10-08 note said no denim trouser outside Y-3 was seen. The cause was a search redirect to the Jeans sneaker; the category query finds the denim.
- **Shoes low:** IF0895 Adilette Aqua lists $25, while 8 other colourways list $30. I kept $25 and flagged it.
- **Dress pants:** TRIPLE PLEATED PANTS (KR9140, Premium Adicolor, $120 list) is a non-golf pleated trouser. It falls inside the existing $80–$130 range, so the cells are unchanged.
- **Caveat that still applies:** the PLP sort runs on sale price, so a high could still hide behind a markdown.

**Fibre: sample extended 16 → 72 styles.**
- I added 56 styles: the first distinct non-Y-3 models, in default grid order, from these listings:
  - men-t_shirts (662 articles)
  - men-hoodies (316)
  - men-pants (456)
  - men-jackets (425)
  - men-shorts (402)
  - men-jerseys (517)
  - two denim styles
- Collaborations and licensed federation/club kit were kept in the fibre sample because adidas sells them. They are never used as a price high.
- I found no men's knitwear, sweater or polo slug: `men-sweaters` and `men-polos` fall back to all-men (5,845). Knitwear is therefore thin (2 styles), and polos are 3.
- **Results, on the sample only:**
  - Composition is stated on 71 of 72.
  - Natural 30 (42%), synthetic 40 (56%), cellulosic 1 (1%), undisclosed 1 (1%).
  - Spandex on the main line: 7 styles, 6 of them at 5% or more.
  - Shape on the sample is split: tees-polos (23, jerseys pull it synthetic), outerwear (15) and shorts (8) are synthetic-led; sweats (14) are natural-led.
- `styles_total` stays NC: the grid counts 3,278 articles (colourways), and the style count is not determinable without full pagination. `colourway_ratio` is NC for the same reason.
- `tech_share_of_range` (25) is still on the first 16 styles only.

**Annual report 2025 (adidas AG).** Read at report.adidas-group.com.
- **Stores:** 2,022 own-retail stores at the end of 2025 (2024: 1,933), made up of 886 concept stores and 1,136 factory outlets. The 886 includes flagships, brand centres **and concession corners** ("dedicated adidas brand spaces within our customers' stores"). No region or format split is given, including in the additional-information PDF.
  - `own_doors_world` stays NC rather than seating 886 as full-price own doors.
  - DTC is 40% of sales; the chart labels show own retail 23% and e-commerce 17%.
- **Sourcing** (evidence for craft, which stays at 2): "we outsource almost 100% of our production to independent manufacturing partners". 92% of 2025 volume was made in Asia: Vietnam 27%, Indonesia 18%, China 16%. The largest factory made about 6% of volume. The only owned facilities named are 21 of 60 distribution centres.
- Founding (1949, Herzogenaurach, Adi Dassler) is unchanged. The owner is now cited to AR 2025 instead of MarketScreener (ownership_url changed old → new for that reason).

**Remaining NC cells.**
- **Vinted: id 14.** `brand_ids[]=14&catalog[]=5` on vinted.com shows the brand filter "adidas", category Men, 500+ results. The id was tried from recall and confirmed by that page.
- **Signature product: Samba OG Shoes (B75806, $100).** In adidas's own words: "Born on the pitch, the Samba is a timeless icon of street style." It is also #2 on the default all-men grid.
- **Lookbook: NC.** Search found only press and third-party coverage, with no brand-hosted lookbook within budget.
- **B Corp: NC.** The B Lab directory is script-rendered, the /company/adidas profile URL gave a client error, and no web evidence turned up.
- **GOTS: NC.** No evidence found.

**Not changed:** stockists file (still not read), doors file, quote, tech, pronunciation.


## Alden


**Status: partial.** This is a shoe-only house. Seven garments are `NONE`. The fibre section is 0/`NONE` because Alden sells no clothing; its accessories are belts and shoe care. The styles file is header-only.

### What was checked
- **aldenshoe.com:** the home page, History (PageID=2), Standards of Quality (PageID=5), Genuine Welt Construction (PageID=6), Genuine Shell Cordovan (PageID=7) and the Stores page (PageID=3). The site has no cart and publishes no prices. Its catalog is a PDF that was not read.
- **The Alden Shop, San Francisco (aldenshop.com, a Shopify store):** the home page, our-story, hours-location and privacy-policy pages, plus one read of `/collections/loafers/products.json`.
- **Alden of Washington DC (aldenshoedc.com):** the home page only.
- **Ownership sources:** the Stridewise interview with Ralph Bonato of Alden Madison (Jan 2021), the Alden of San Diego FAQ, fromsqualortoballer (2014) and Wikipedia's citations (NYT 2011, Forbes 2008, Horween).

### Not reached
- **WebFetch returned HTTP 429 (rate limited)** from mid-run onward. This happened on every domain, after waits of up to 7 minutes. Pages refused:
  - aldenshoedc.com FAQ
  - aldenshop.com contact page, loafers collection and stock-loafer feed
  - horween.com/history
  - grailed.com/designers/alden
- **curl was refused by the egress proxy** for aldenshoe.com and aldenshop.com, so I made no other fetch attempt.
- **Shoe prices are `NC`.** The only figure read was $708.00 (no compare-at) on four calf tassel moccasins in the SF shop's feed: 662, 561, 663 and 660. The output was truncated after these, so shell cordovan styles and the top of the range were not read. These are SF-shop prices, not aldenshoe.com prices.
- **Stockists are `NC`.** The locator's state names carry no links in the fetched markup, and `?State=MA` returns the same index page. The result list was never readable.
- **Not established:** `own_doors_world`, `made_in_stated_share`, Vinted id, GOTS and `search_url`.

### Contradictions and flags
- **Two own doors are filed: SF (170 Sutter St) and DC (921 F St NW).**
  - Neither aldenshoe.com nor either shop's site says the shop is factory-owned.
  - The basis is secondary: the Stridewise 2021 interview, the San Diego dealer FAQ and a 2014 blog.
  - Supporting detail: the DC shop's email is on the factory domain (WashDC@AldenShoe.com).
  - Treat both as soft until Alden confirms.
- **Alden Madison (NYC) is an independent licensee** per its co-owner in 2021, so it is excluded from doors. The worklist's "own stores in NYC, DC, SF, Boston" is wrong for NYC, and no Boston own store was found.
- **Horween is not named anywhere on aldenshoe.com.** The shell cordovan page says only "the single tannery still producing genuine shell cordovan". Horween is named by third parties and by the SF shop's collection handle (`horween-shell-cordovan`).
- **Craft is proposed at 5.** The basis is the owned Middleborough factory: the brand's own claim (built 1970, founded 1884 in the same town), corroborated by NYT 2011.
- **Tech is 1 on a provisional scale.** No tech rubric was issued. Shoe soles (Vibram, Dainite) were not checked.
- **Quote:** it comes from the brand's own welt page. An alternate is in the row's `note`.
- **Grailed URL:** the base page was not fetched. Its subpages (/formal-shoes, /casual-leather-shoes) appear in the search index.
- **B Corp:** filed as no. A search of bcorporation.net found no Alden listing; the directory itself was not fetched.

### Re-run 2026-10-10 (gap-fill)

About 22 fetches and searches, made one at a time, with no 429s this run. curl to aldenshop.com was refused again by the egress proxy (CONNECT 403), so all reads went through WebFetch.

**Shoes: NC → filled.** Source is The Alden Shop SF only; no independent-retailer prices were used.
- **Loafers collection:** `/collections/loafers` shows "1-30 of 30 products". There is no strikethrough or sale label. Prices run $694–$967.
  - The products.json feed truncates after about 5 products, because each product carries roughly 30–42 size variants. The collection HTML was used for the full list, and product `.json` for verification.
- **Low: $694.00 (exact)**, the 6221L Unlined Penny Loafer (snuff suede, rubber sole).
  - Product .json: all 30 variants are $694.00, with no compare-at.
  - 6224L (dark brown suede) is also $694.
- **High: $967.00 (exact)**, the 563 Tassel Moccasin in Color 8 shell cordovan.
  - Product .json: all 42 variants are $967.00, with no compare-at.
  - Tied at $967 with the 664 Tassel Moccasin (black shell) and the 684 and 6845 Full Strap Slip-On (shell). 563 was chosen because the tassel moccasin is the signature.
- **Shell cordovan collection:** 52 products over two pages, read in full. No shell loafer is above $967. Bluchers, boots and oxfords run $971–$1,048, but they are not loafers.
- **Basis is `pair`:** the entry loafer is unlined suede, the elevated loafer is shell cordovan. Calf tassel moccasins are $708. The 9694F penny is titled "Limited to Stock On Hand", but at $708 it affects neither end.
- **Old listing URL changed:** all-footwear → collections/loafers.
- **Horween not named:** the 563 product body does not name the tannery or state made-in.

**Ownership: still soft, no change.** None of these pages states who owns or operates the shop:
- aldenshop.com: our-story, faq
- aldenshoedc.com: home, FAQ (PageID=3), the-alden-story

Both shops say only that Alden Shoe Company is "still a family owned business". A WebSearch turned up no first-party statement. Doors stay at 2 soft.

**Stockists: still NC.**
- Re-fetching the locator shows no hrefs, form, onclick or script for the state/region list; it is plain text.
- `?State=Massachusetts` returns the index page.
- The Wayback Machine is blocked to WebFetch (SITE_BLOCKED).
- The results URL pattern could not be found by search.
- Alden Madison and the other independent Alden-name shops were not added, because the brand's own list could not be read.

**Remaining NC:**
- **GOTS:** the global-standard.org database URL 302-redirected to a different domain (global-standards.org). I did not follow it. A WebSearch found nothing; leaving NC. GOTS is a textile standard and Alden sells leather shoes.
- **Vinted:** vinted.com/brand/alden returned a generic page with no Alden id, and a search found none.
- **own_doors_world:** two Japanese-language searches on Alden Tokyo (operator, authorised importer) gave nothing usable. No evidence that any shop outside the US is factory-owned.

**Not touched:** doors, stockists and styles files (no new data). The styles file stays header-only because there are no clothing styles.


## Allen Edmonds


**What blocked the read.** WebFetch returned HTTP 429 (rate limit) on every domain (allenedmonds.com, grailed.com, wikipedia.org) from about 10 minutes in, and kept doing so for 35+ minutes with waits of 2–6 min between tries. curl from Bash was refused by the session egress policy (CONNECT 403) and was not used. No workaround was tried. These pages were refused and must not be re-fetched in this run, but a later run should read them: /browse/apparel, /browse/apparel/{sweater,shirts,pants,outerwear}, /the-journal/made-here, the Shoe Bank store page, grailed.com/designers/allen-edmonds and en.wikipedia.org/wiki/Allen_Edmonds.

**Checked**
- Men's shoes listing (/browse/shoes/mens). It is server-rendered, has no product prices, and shows "starting at" labels on the Icons collections only: Oliver $299; Randolph, Park Avenue and Strand $349; Chandler $399; Higgins Mill $449. Not used as prices.
- One product page (Miller Reserve Penny Loafer 3031226). It shows "See Price In Cart", "Product Data Is Missing" and out of stock. It has no JSON-LD offers and no country of origin. The only endpoints found are cart and account routes, and no product JSON endpoint was found before the 429s started. Shoes: NC.
- Store sitemap (from sitemap.xml). It has 61 entries: 57 full-price-looking store pages, 3 outlets (Shoe Bank Port Washington, Galleria West Outlet, Charlotte Premium Outlets) and 1 "Recraft Customer Service" page, which was excluded. The doors file uses all 60 stores, but city, state and zip come from the URL. Street, phone and status were read for only one store (Scottsdale 39128). Port Washington Studio doors can't be told apart in the sitemap. The one exception is 141A Newbury St, which the 2023 Business Wire release names as the first one.
- Caleres 10-K for FY2025 (FYE 31 Jan 2026), https://www.sec.gov/Archives/edgar/data/14707/000001470726000053/cal-20260131x10k.htm:
  - It reports "58 Allen Edmonds stores in the United States … including 18 Port Washington Studio stores and 3 outlet stores". End of 2024 was 56 and end of 2023 was 57.
  - The plan is "approximately two new … and close approximately five stores in 2026".
  - Suggested retail is $300–$595, and the Reserve Collection is $800–$2,995.
  - "Our Port Washington and Santiago facilities manufacture footwear and certain accessories for our Allen Edmonds brand". Santiago is in the Dominican Republic.
  - It gives no in-house versus sourced share for Allen Edmonds. Item 2 (Properties) was past the fetch limit.

**Contradictions**
- The worklist claim of "60-plus own US stores" is wrong. The filing gives 58 including 3 outlets, so **55 full-price** (including 18 PWS). This supersedes facts_first's 56 (FY2024, 12 PWS). The sitemap shows 57 full-price, and the gap is unreconciled: a duplicate Scottsdale id (39127/39128) and two Boston 02109 pages may be stale.
- "Wisconsin" / made-in-USA: the filing shows a second owned factory in the Dominican Republic, and the one product page read states no origin. The US-made share of the range is **not established**. Forum and blog reports of India-made models were seen in search titles only and were not used.

**Not reached:** apparel (so own-label garments are unverified and the seven garment cells are NC, not NONE), styles and fibre (the styles file is header only), the stockist list, tech, lookbook, Vinted and Grailed, B Corp and GOTS, and the founding place and founders.

**Brief notes**
- No tech rubric was issued (proposed_tech is NC).
- The apparel nav has no polo or tee node.
- proposed_craft 4 is provisional and rests on the filing. It should drop to 3 if a later read shows that most of the current range is imported and Port Washington mainly does recrafting.
- The quote was read through a WebFetch extractor and needs one verbatim check against the release.

### Re-run 2026-10-10 (gap-fill)

About 30 WebFetch calls, one at a time, with no 429s. No Cloudflare or bot check showed on allenedmonds.com pages, but store pages were not fetched (a Cloudflare check showed in the browser, per the brief), and the doors file is unchanged. curl from Bash is still refused by egress (CONNECT 403) for allenedmonds.com and the blob-storage sitemap, so it was not used.

**Shoe prices: np.** Product pages (Miller Reserve, Carmine Reserve, Park Avenue 3023014) and four apparel pages all serve "See Price In Cart", "Product Data Is Missing", an empty "Style #" and no JSON-LD. The only API path visible is /api/calxa/account/logoff. No product JSON is published in the page, and no endpoint was guessed. The price appears only after add-to-cart, which was not done. Unchanged: the collection "starting at" labels and the 10-K range ($300–$595; Reserve $800–$2,995).

**Apparel is mainly stocked.**
- /browse/apparel is titled "Handpicked essentials from our favorite makers". The Spring Style Guide (/port-washington-studio/the-collection/shop-the-look) says: "partnering with apparel labels that share our commitment to craft".
- Listing grids are rendered in the browser and show no tiles to WebFetch. The "Allen Edmonds Apparel" brand page (/browse/brands/allen-edmonds) shows "0" items.
- The product-groups sitemap (about 346 entries; the converted text ends mid-URL at "harris-wharf-patterne", so a few final entries may be unread) holds about 96 apparel URLs. About 83 have a third-party brand in the title: Barbour, NN07, Bugatchi, Les Deux, Eton, Schott NYC (including several "Schott NYC x Allen Edmonds" leather jackets, which are collaborations and never a price), Officine Générale, Civilianaire, Far Afield, Altea and Harris Wharf.
- 13 titles name no brand. They are listed in styles_allen_edmonds.csv, but their **own-label status is not established**:
  - Page titles and metas follow one template ("Shop the X by Allen Edmonds") on stocked Barbour items too.
  - "Classic Bedale Wax Jacket" is a Barbour model name.
  - Schott sells a "Wool Town Coat" here as 3030500.
  - Composition, origin and price are not served on any product page, so the styles rows carry composition NC.
- Garment cells:
  - Polo, dress shirt, jeans and dress pants: NONE, because only third-party labels were found (NC → NONE). If Sebastian prefers, these can revert to NC, since the sitemap tail is unread.
  - Tee, sweater and outerwear: NC.
  - styles_total: NC.

**Made-in share: NC.**
- /browse/featured/handcrafted-in-america is headed "Handcrafted in Port Washington, Wisconsin": "Exceptional shoes and boots, all purposely handcrafted in Port Washington, Wisconsin using the finest imported materials."
- The grid did not render, so the US-made subset cannot be counted, and no product page states an origin.
- Having a separate "Handcrafted in America" listing implies that not all of the range qualifies. Together with the 10-K's Santiago (Dominican Republic) factory, this supports keeping craft at **4** (unchanged), not 5.
- The process page is now first-party evidence: 360° Goodyear bench welt, "more than 40,000 individual lasts", hand finishing, "right here in Port Washington". It names no tannery.

**Changes (old → new):**
- founded_place: NC → Belgium, Wisconsin. founders: NC → Elbert W. Allen. Both are verified on /the-journal/made-here/our-legacy, which names no other founder. Ralph Edmonds is not mentioned there, so he is not added.
- heritage_claim: now dated and placed, from the brand page. process_documented: now the brand page. craft_url_2: Business Wire → the process page.
- named_makers and named_mills: NC → NONE (none named).
- tech: ["Weather Ready","Dainite"], from product titles in the sitemap ("Weather Ready" Penn and Powell; Park Avenue "with Dainite sole"). It is owned plus licensed, and the share is NC. proposed_tech is 2 on the provisional scale, since no tech rubric was issued.
- Lookbook: yes, "THE SPRING STYLE GUIDE" (no year stated), men's.
- Grailed: the /designers/allen-edmonds page exists.
- Vinted: no brand id found (the brand URL resolved to a generic items page), so NC.
- B Corp: the bcorporation.net directory returned fetch errors twice, and no web evidence was found, so NC. GOTS: NC.
- Quote: verified verbatim on Business Wire. The attribution in the release is "senior vice president and general manager for Allen Edmonds" (wording adjusted).
- Stockists: the brand lists none. The nav offers only Stores and Find a Store, and no retailer or stockist page was found, so the file has one `none` row. Nordstrom is a third-party report only.
- Signature: the legacy page says Park Avenue and Strand "remain best-sellers", which supports the Park Avenue proposal.

**Still open:** shoe and apparel prices, which need a cart read in a browser; own-label confirmation for the 13 unbranded apparel styles; the made-in share; B Corp; Vinted id; the door street, phone and status fields (Cloudflare).


## AllSaints


**Why partial.** About 12 WebFetch reads went through. After that, every WebFetch call on every domain (allsaints.com, Wikipedia, Drapers, FashionNetwork, lioncapital.com) returned HTTP 429 from the fetch proxy. I retried over about 30 minutes, waiting 2, 5, 7 and 8 minutes between tries, and none got through. Bash curl to allsaints.com was refused at the proxy (CONNECT 403). I did not try any workaround. WebSearch still worked, but it returns titles only, so I used it for leads and not as evidence.

### Checked (live, 2026-10-08)
- **Store.** The US store is https://www.allsaints.com/us. Prices are in USD. The platform is Salesforce Commerce Cloud (`Sites-allsaints-us-Site`). robots.txt disallows `/search`, `prefn/prefv`, `srule`, `pmin/pmax` and `cid`. US product sitemaps were not reached.
- **Men's clothing size.** The men's clothing grid says "556 items". That counts tiles, including colourway duplicates, so it is not a style count.
- **Grids read in full (names and prices only, no hrefs):**
  - knitwear: 81/81
  - coats & jackets: 67/67
- **Grids read in part:**
  - leather jackets: 36 tiles, with URLs
  - t-shirts: first 24 tiles, with URLs
  - all clothing: first 96 of 556
- **Product pages read:** 3 (Tonic tee, Seyka, Xylon). Each page states its composition and "Made in", and all three say Turkey.
- **Filed prices:**
  - tee low $49
  - sweater $139 to $279 (range)
  - outerwear $229 to $829 (range)
  - Everything else is NC. Prices I saw but did not file are in the row's `note`.

### Seyka shearling ($2,999), checked by code and gender
- The product ID is **USW088LF-827**. USW is the women's code family; every men's style read was USM.
- Even so, it sits only under Men > Collection > Leather Jackets, on a `/menswear/` URL. The model is 6'2" wearing M/L, and the `/womenswear/` path opens the same men's page.
- So facts-first's guess that it is womenswear is **not supported**. It looks like a unisex style sold in the men's range.
- I still kept it out of the outerwear high, but for a different reason: dyed-sheepskin shearling is fur-on, and the never-fur rule bars it from a high. **Sebastian to rule.**
- If it is allowed, the outerwear high becomes $2,999.

### Not reached (NC)
- Section 2: polo, dress shirt, jeans, dress pants and shoes, plus the tee high.
- Section 3: the fibre census (only 3 styles were read).
- Section 4: doors. The locator at /us/stores/ was never read and `doors_allsaints.csv` is header only. Per facts-first, US outlets exist (Orlando, Chicago/Rosemont, Livermore, Seattle/Tulalip) and must be split out from full-price stores when counted.
- Section 5: stockists. I did not check whether the brand lists any, and the file is header only.
- Sections 6–13: tech, craft, lookbook, Vinted/Grailed, B Corp/GOTS and the quote.

### Ownership (unresolved, owner_today = NC)
- **2011:** search titles show Lion Capital and Goode Partners buying AllSaints (Retail Week; FashionUnited "All Saints bought by investment firms").
- **Possible sale:** Drapers ran a story titled "Lion Capital considering AllSaints sale, say reports", but I could not open it, so I have no date or detail.
- **John Varvatos link:** FashionNetwork and The Impression report AllSaints' results together with John Varvatos, and ABL Advisor reports a "Wells Fargo … growth facility to AllSaints and John Varvatos". That points to a combined group under Lion Capital, but I have not confirmed it.
- **No completed sale is established.** Whether Lion Capital still owns AllSaints needs the latest Companies House accounts (AllSaints Retail Ltd or its parent) or the Drapers piece.
- **Founding:** usually given as 1994, London, Stuart Trevor and Kait Bolongaro. I left it NC because I did not verify it here.

### Contradictions with worklist and facts-first
- The worklist's "40-plus US stores" is still unverified.
- Facts-first's womenswear guess on Seyka does not hold: it is a men's-merchandised USW code (see above).
- The men's nav has no polo node. Knit polos sit under Knitwear: Aspen $139 to Beton $179 at full price. The Cyclone Cable Polo is on sale with a $219 compare-at.

**Recommendation:** re-run AllSaints in a fresh session once the fetch quota resets. Sections 4–13 need a browser-free read of /us/stores/ and a direct reading of the ownership sources.

---

### Re-run 2026-10-10 (gap-fill): status still partial

**Fetches.** I made 116 WebFetch calls, one at a time, and got no HTTP 429. Bash curl to allsaints.com is still refused by the proxy (CONNECT 403, policy denial), so every read went through WebFetch. WebFetch refused two paths as robots-disallowed: `?srule=` sorting and lioncapital.com/portfolio. I did not work around either.

I did not touch doors. `doors_allsaints.csv` was left exactly as the main thread wrote it. One thing to flag: its `brand` column reads `allsaints` (lowercase). The canonical key is `AllSaints`.

### Section 1–2: prices
All eight garments are now filed with product and URL, except the sweater low URL.

| Garment | Low | High | Basis |
|---|---|---|---|
| Tee | $49 Tonic | $99 Xander | pair |
| Polo | $119 Reform piqué SS | $149 Mode Merino SS | range |
| Dress shirt | $129 Maddox | $239 Brook Western | range |
| Jeans | $179 Slim-Straight | $299 Flocked | range |
| Dress pants | $229 Ware | $249 Blunt (York and Moor also $249) | range |
| Sweater | $139 (unchanged) | $279 Harry, URL now filed | range |
| Outerwear | $229 Denim Trucker, URL now filed | $829 (unchanged) | range |
| Shoes | $269 Bloom loafer | $349 Jules loafer | pair |

Notes on the prices:
- **Tee:** the high is a judgement call. Graphic tees go to $119. The Raine long-sleeve waffle is $149. The $149/$169 3-packs are excluded.
- **Polo:** the men's nav has no polo node.
  - The Reform piqué polo was found through the product sitemap. It is not in any grid I read.
  - The Beton polo ($179) is long-sleeve, so it is not a polo high.
  - The Cyclone polo's $219 compare-at belongs to a 50%-off clearance item and was not used.
  - The polo listing link is the Knitwear parent node.
- **Dress shirt:** the brand makes casual shirts only.
  - The $129 low has a resort collar. The cheapest classic-collar long-sleeve shirt is Bond at $149.
  - Brook shows $229 on the grid and $239 on the product page. I filed the product-page price.
- **Dress pants:** there is no tailored-trouser node.
  - The Pants grid mixes in chinos and sweatpants.
  - The Clyston suit trouser has a $499 compare-at, but it is on sale and not in the grid, so I excluded it.
  - The $569 leather pants are not dress pants.
- **Shoes:** prices come from the loafer grid (5 tiles). I did not read the shoe product pages.
- **Sweater low URL is still NC.** The $139 Statten Ramskull Crew Neck tile sits past the first 48 tiles, which are the only ones whose links the fetch returns. The sort parameter that would bring it forward is robots-blocked.
- **Search:** `search_url` is filed as https://www.allsaints.com/us/search?q=. Results are rendered client-side; the page meta reports "7 results" for "statten".
- **Men's listing links** are filed for all eight garments.

### Section 3: fibre (documented sample, not a census)
**What was read.** I read 74 men's styles from their product pages: 3 on 10-08 and 71 on 10-10.

| Category | Styles read |
|---|---|
| Tees and polos | 11 |
| Shirts | 15 |
| Knitwear | 16 |
| Outerwear (incl. 6 leather) | 16 |
| Denim | 5 |
| Trousers (incl. 1 tailoring) | 7 |
| Sweats | 5 |

- Composition sits in the "Fabric & care" DOM text. There is no JSON-LD `material` field and no structured composition field in the payload WebFetch sees.
- The men's clothing grid states 556 tiles, including colourways. The US product sitemap holds only about 280 URLs and misses the Tonic tee and most tees, so it is not a usable census. The distinct-style denominator is therefore not established.

**Results** (shares of the 74):
- 73 of 74 state a composition. Cora Leather Jacket showed none, and no Made in either.
- Natural 77%, synthetic 11%, cellulosic 11%.
- 12 styles have elastane on the main line.
- Shape on the sample: `one`.

**Where the synthetics and cellulosics sit:**
- **Trousers:** synthetic in half the sample. Blunt and York are 100% polyester; Moor is 78% recycled polyester.
- **Knitwear:** the alpaca-named knits are polyamide-led (Soren 45% polyamide, Parx 57%, Senner 55%, Galactic 40%). Their names over-state the alpaca.
- **Shirts:** 6 of 15 are cellulosic-led, using ECOVERO viscose or TENCEL lyocell.

**Composition flags:**
- Clyston's page prints "98% wool, 25 elastane". I read it as 2% elastane by the sum check; it needs verifying.
- Hawthorne is $159 on its product page and $149 on the grid (a colour difference). Ward is $199 on its product page and $179 on the grid.

### Section 5: stockists
The brand lists none. The footer links only the Store Locator. The file has one `none` row.

### Sections 6–13
- **Tech:** LENZING ECOVERO and TENCEL, both licensed. They appear on 7 of 74 styles (9%). Proposed **2**. This is a provisional scale; no tech rubric was issued.
- **Craft:** proposed **2**.
  - The 2026 Modern Slavery Statement (All Saints Retail Limited, signed by Peter Wood, 25/09/2026) says: "AllSaints does not own the companies or factories that produce our goods." It reports 175 tier-1 suppliers in 16 territories, with sites on Open Supply Hub.
  - No maker or mill is named on any product page.
  - Made in is stated on 73 of 74: Turkey, Portugal, China, India, Cambodia, Vietnam and Canada.
- **Origin:**
  - The brand's own document says "Established in London in 1994" (Modern Slavery Statement).
  - The founders, Stuart Trevor and Kait Bolongaro, come from Wikipedia only; no brand page I read names them.
- **Ownership:** Lion Capital LLP. It took a majority stake in May 2011 with Goode Partners, and Goode exited in 2012 (Wikipedia, citing the Guardian, Telegraph and WSJ). WWD in 2018 calls Lion the "parent company". I found no completed sale in 2024–2026:
  - FashionUnited's 24 Oct 2025 piece on FY25 results mentions no sale; it reports the Wells Fargo facility extended to 2030.
  - The Modern Slavery Statement names no parent.
  - The Drapers "considering sale" story is still unread and undated.
  - Companies House was not readable (fetch error), so Lion's current control is not confirmed from filings.
- **Lookbook:** there is no standalone lookbook. The homepage runs "The Autumn Collection" campaign imagery, and the men's section has Shop The Look and Fall Outfits edits. Filed `no`.
- **Grailed:** verified at /designers/allsaints.
- **Vinted:** brand id NC (vinted.com fetch error).
- **B Corp:** NC (the B Lab directory fetch errored; the Modern Slavery Statement does not mention B Corp).
- **GOTS:** filed `yes` on the brand's own claim. The Modern Slavery Statement and the ESG page say IDFL certified it for GOTS, OCS, RWS, RAS, RMS and RCS. I did not check the GOTS public database.
- **Quote:** "Since the beginning, music has always been a part of our heritage." This is the house voice, from the About Us page (undated). The alternative is: "We recognise we have a responsibility towards our planet, and the people involved in making our clothes."
- **Signature product:** the homepage names "leather, denim and T-shirts" as its "signature styles". I kept the leather biker jacket and changed the URL to the Neo Leather Biker Jacket.

### Old → new
- `read_date`: 2026-10-08 → 2026-10-10.
- `signature_product_url`: leather-jackets listing → Neo product page (rules ask for the product on the brand's own store).
- `signature_product` text: now cites the homepage's "signature styles".
- `outerwear_low_product`: style code added.
- No price was changed. The Seyka ruling is left as it was, pending Sebastian.

### Not reached
- The sweater low URL.
- A full style census and the colourway ratio.
- Vinted, B Corp, Companies House filings and the Drapers sale story.
- The shoe product pages, so shoe prices rest on the grid only.
- The blazers: the Bay blazer URL redirects to a fragrance page, and there is no tailoring node.


### Doors — browser read 2026-10-10 (main thread)

own_doors_us NC → 17. Browser read 2026-10-10: 59 US records = 18 own-door (17 open + Boston 41B Newbury coming-soon) + 10 outlet + 31 concession (30 Bloomingdale's, 1 Macy's Herald Sq). Locator mixes concessions with own stores, no type flag. World total not given.


## Bally


**Status: partial.** Partway through the read, the WebFetch proxy began rate-limiting (HTTP 429) every domain and asked not to retry the refused URLs. A Bash/curl route to bally.com was denied by proxy policy (CONNECT 403). No block was worked around.

### Checked
- **US store.** https://www.bally.com/en-us runs on Shopify. **USD is confirmed on two displayed prices**: the tee at $250.00 USD and the biker jacket at $3,750.00, with the selector reading "United States (USD $)". This resolves the facts-first flag on the $3,750 feed figure.
- **Men's ready-to-wear census.** The collection page states 35 products. The only subcollections checked were Knitwear (3) and Tracksuits (1). 21 product pages were read for composition and price. These 14 were not read:
  - 6311692, 6308559, 6312833, 6309741 and 6313958 were refused with a 429.
  - The rest were never attempted after the limit hit: 6311404, 6314485, 6314258, 6309961, 6314345, 6314257, 6311403, 6313977 and 6314486.
  - Their prices come from collection tiles.
- **The US store sells nothing.** Every variant on every product read, and on the 6-product feed page, is `available:false` / "Out of stock". Prices are displayed but cannot be bought.
- **Markdowns.** Many styles are marked down a uniform 30%, and compare-at prices are filed as full price.
- **Composition.** Bally writes fibres by name with almost no percentages; the car coat is the only one with a percentage (65% polyester, 35% cotton). On the 21 styles read:
  - 16 are natural-led (7 of them leather), 5 synthetic-led, 0 cellulosic.
  - 2 carry named stretch with no percentage.
  - The brand-level percentages are `NC` because 14 styles are unread.
  - Bally gives each colour its own product code, so 35/35 overstates the number of distinct styles.
  - `category_house` comes from product_type where the feed showed it (9 styles); for the rest it was inferred from the navigation.
- **Contradiction on one product.** "Blouson In Navy Blue Nylon" has details that say "Woven polyester". The details are filed.

### Not reached
- The store locator, so there are no doors, no stockists and both door counts are `NC` (the doors and stockists files are header only).
- Men's shoes, so all shoe cells are `NC`. This matters for a shoe house.
- About and craft pages, lookbook, quote, signature product, Vinted, Grailed, B Corp and GOTS.

### Owner, crisis and craft (from search-result headlines only; articles refused with 429)
- **Owner.** Regent, L.P. affiliate, bought from JAB with the deal announced August 2024 (fashionunited.uk, Walder Wyss, just-style).
- **2026 crisis.** Headlines report:
  - "Bally Faces Swiss Restructuring Procedure, Regent Reinstates Long-term Commitment" (WWD).
  - Insolvency in Germany (LaConceria).
  - A rescue blocked (Bilanz).
  - Five Swiss shops closed (cash.ch).
  - "Bally in deep crisis" (shoegazing, 2026-08-04).
  - A bankruptcy filing with €216m debt (modaes, date unread).
  - US store closures, Dec 2024 (tonetoatl).
- **Swiss production.** Headlines report that **Bally ended shoe production in Switzerland** (fashionunited.de 2026-05-18; SRF "after 175 years"; fashionnetwork). Caslano layoffs were reported in 2025.
- **What this means for the record.**
  - The worklist line "Swiss shoe-and-clothing house, US stores" needs re-checking on both counts.
  - The Caslano/Schönenwerd making is now heritage, not current evidence.
  - None of the 21 product pages names a maker or mill or states a country of origin, so the proposed craft score is **2**, with low confidence.
- **Before anyone rules.** Owner and status should be confirmed by reading the WWD and swissinfo articles.

### Brief issues
- Tech has no rubric; the score of 1 is on the provisional scale.
- The sweater cell is the only crewneck, which is probably part of the Christmas capsule. It is flagged in the row's note.
- The dress shirt (single, $550) was read from a collection tile only; its product page was not read.


### Doors — browser read 2026-10-10 (main thread)

own_doors_us NC → 1. Browser read 2026-10-10: locator shows one US door (South Coast Plaza, Costa Mesa); no outlets or concessions listed. Country filter offers only 6 countries; 93 records not a global count. Treat as what the locator shows, not proof of closures.


### Re-run 2026-10-10 (gap-fill; doors untouched; ~40 fetches, one at a time, no 429)

**Checked**
- **All 35 men's RTW styles are now read.** The handles came from the collection feed (`products.json?limit=9&page=1..4`, 9+9+9+8 = 35, which matches the stated count). The 14 PDPs that were unread are now read. Every variant is still out of stock.
- **Dress shirt confirmed on its PDP.** "Woven cotton", "Shirt collar", "Mother-of-pearl buttons", "Button cuffs"; regular price $550.00, sale price $385.00.
- **Shoes.** Men's Shoes lists 110 products and Loafers & Moccasins lists 25.
  - **Low: Gusto Loafer, $575.00.** Calf leather, EVA sole, cemented construction, no markdown. The Switz Moc Loafer is also $575.00.
  - **High: Scribe Un Loafer in Black Deer Leather, $1,150.00.** Goodyear construction, no markdown. Filing it as the high rests on a named judgement that deer leather is not an exotic skin. If Sebastian rules that it is, the alternative is the Regent Loafer in Black Grained Leather at $925.00 compare-at.
  - **Compare-at.** It was checked on two Regent colours: $825.00 each, both 30% off.
- **Listings tile-checked.** Shirts & T-Shirts has 9 products, Pants 9 (shorts included) and Coats & Jackets 15. On one fetch Coats & Jackets showed an unrendered `{{ count }}`, so it was re-fetched. Men's Shoes was also checked.
- **Search.** `/en-us/search` is robots-disallowed, and WebFetch refused it (ROBOTS_DISALLOWED), so `search_url` stays NC.
- **Fibre roll-up.**
  - All 35 styles name a fibre, so 35 have a composition under rules_fibre's named-fibre rule. Only the car coat gives a percentage.
  - The split is 28 natural (80%), 5 synthetic (14%) and 2 cellulosic (6%); the cellulosic pair is the Christmas Capsule shirt and pants in "Viscose twill".
  - 2 styles carry named stretch.
  - "Wool blend" (3 pants) is filed as lead wool, `pure` blend, because only wool is named.
  - Shape is one, with no synthetic-led category; the house's Coats & Jackets is 10/15 natural.
  - Lines: Christmas Capsule (3) and Tennis Collection (2), both under 5.
  - `lead_pct` is ND throughout, so no percentage-based figure is possible.
- **Stockists: none.** There is no stockist page in the nav or footer, and the locator (main-thread read) lists only Bally boutiques and outlets.
- **Brand pages.**
  - The About Us page gives "Born in Switzerland in 1851" and Carl Franz Bally, with a family-run ribbon factory in Schönenwerd, so the founding is now verified from the brand.
  - It also still claims "multi-generational artisans based in Caslano" and Scribe "still handmade in Switzerland". The press contradicts this (below), so the page is stale.
  - The Sustainability page names no B Corp, GOTS or LWG certification; FSC/PEFC packaging only.
- **Lookbook: no.** No lookbook was found on bally.com. `/pages/ss26-collection` ("SS26 Collection", men's and women's) is a shop landing page with campaign carousels, not a lookbook, so all four lookbook cells are filed as NONE. The homepage also labels men's as "Resort 2026".
- **Vinted.** Brand id 2603 (`vinted.com/brand/2603-bally` resolves to Bally); the men's catalog URL shows 500+ results.
- **Grailed.** The `/designers/bally` page is valid.
- **B Corp: no.** This rests on no profile at `/find-a-b-corp/company/bally` (fetch error) and no mention on brand pages; the directory search itself was not run.
- **GOTS: NC.** The database was not queried; there is an organic-cotton tee but no certification is claimed.
- **Quote.** It is in the house voice from the About Us page (undated). The alternative is "Bally dares to be different, always designing with longevity in mind."
- **Signature product.** Scribe, created by Max Bally in 1951 per the About Us page. A Scribe collection URL was not found (`/collections/scribe` errored), so the URL is a Scribe Un loafer PDP.

**Changed (old → new)**
- Sweater 1250 → NONE, all seven cells plus the listing. The PDP says the only crewneck is "from the Christmas Capsule Collection", and capsules are excluded. The main range has no other sweater; the knitwear listing is this one plus two silk-cotton polos. Sebastian to rule: NONE is imperfect, because a capsule sweater does exist.
- `owned_facility`, `heritage_claim`, `process_documented`, `founders`, `owner_today`, `craft_url_1` and `craft_url_2` were rewritten after first-hand reads. `proposed_craft` stays at 2.
- The previous note's "€216m debt (modaes)" was wrong. The modaes headline says €21.6m and its body says CHF 20m.

**Restructuring: dated facts (first-hand reads)**
- **2024-08-15.** An affiliate of Regent (owner of Escada and Club Monaco) buys Bally from JAB. The price is undisclosed; Bally had about 320 stores and about 1,500 staff, with HQ in Caslano (fashionunited.uk).
- **Start of 2026.** Mario Grauso becomes CEO, succeeding Ennio Fontana. Bally Studio (Florence) closed in 2025 and the Bally Foundation was wound down (fashionunited.de, 2026-05-18).
- **May 2026.** Caslano shoe production ends:
  - 27 remaining production staff are dismissed, by the end of August 2026 at the latest.
  - About 100 administrative staff remain.
  - About 250 people worked at Caslano two years earlier.
  - Sources: FashionNetwork 2026-05-15; SRF 2026-05-22 ("after 175 years", last men's shoes leaving Caslano); fashionunited.de 2026-05-18, citing La Conceria.
  - The Lugano flagship is closing (SRF).
- **2026-06-15.** Bally Schuhfabriken receives a provisional composition moratorium (Nachlassstundung) from the Zug cantonal court:
  - It runs to 2026-10-15, with Transliq AG as trustee.
  - The company's seat had just moved from Caslano to Zug (ms-aktuell).
  - The debt is about CHF 20m per the unions (fashionunited.uk) and modaes 2026-06-21, but bluewin (2026-07-28) estimates about CHF 100m. Unreconciled.
- **July 2026.**
  - A Lugano court blocks the transfer of the brand to Aare LLC, a US company founded in May 2026, and the brand is "seized by the bankruptcy office" (fashionunited.uk 2026-07-29, citing LaRegione).
  - Regent rejects a whole-group offer from Roberto Martullo.
  - Bally Holdings GmbH was founded in April 2026 with brand licensing among its purposes.
  - Of the Swiss stores, only Zurich Bahnhofstrasse and St. Moritz remain; workforce is about 1,000 (bluewin 2026-07-28). Geneva, Lucerne, Basel, Lugano and Lausanne are closed (ms-aktuell).
- **August 2026.** Regent tells WWD it remains committed to Bally long term (as reported by ms-aktuell). The WWD article itself returned a client error and was not read.
- **2026-09-16.** The Munich court orders preliminary insolvency administration for B. D. Retail Deutschland GmbH (formerly Bally Deutschland GmbH; case 1500 IN 3348/26). Metzingen, the last German store, is preparing a closing sale (ms-aktuell 2026-09-18).
- **Not read.**
  - swissinfo has no 2026 Bally story in search; only older Schönenwerd closure items.
  - LaConceria's timeline is paywalled; only its lead was read.
  - The outcome after the moratorium ends on 2026-10-15 is unknown.

**Still open**
- `own_doors_world` (the locator is not global).
- `search_url`.
- `feed_currency_rate`: `Shopify.currency.rate` cannot be read via WebFetch, but USD is confirmed on displayed prices.
- GOTS.
- Status stays **partial**.
- The worklist line "Swiss shoe-and-clothing house, US stores" is now wrong on both counts: there is 1 US door, and Swiss production has ended.


## Birkenstock


**What blocked the read.** Part way through, every WebFetch call came back `HTTP 429` from the fetch proxy. This hit every domain tried: birkenstock.com listing pages start=408 to 480, the sec.gov FY2025 20-F and EX-99.1, retailtouchpoints.com, birkenstock-group.com (two pages), grailed.com and fool.com. The proxy said not to re-fetch those pages, so they were not retried. Bash egress to birkenstock.com was refused at the proxy (CONNECT 403), so no sitemap or feed was pulled. Nothing was worked around. Everything after section 2 rests on search-result titles or on facts-first, and the cells say so.

**What was checked**
- Men's listing https://www.birkenstock.com/us/men/ read in default order with `?start=N`. 17 of 36 pages were read (start=0 to 384), which is 408 of 848 tiles (48%). The page ignores `sz`. The price-sorted route was not used.
- Shoes (`range`): low $34.95 (Barbados Essentials EVA Black), high $240.00 (Prescott Lace Men Oiled Leather Concrete Gray). Both are whole-dollar rounded. The high is the dearest regular price in the half that was read, and the unread half could change it. The low URL was found by search and not opened. The high has no US product URL; the listing page is cited instead.
- Clothing: the men's filter offers only Sandals (357), Shoes (470) and Accessories (72). The accessories pages (https://www.birkenstock.com/us/men/accessories/) hold socks, shoe care, insoles and foot care, and no clothing. So the seven non-shoe garments are `NONE`, the fibre counts are `0`/`NONE`, and the styles file is header-only.

**Not reached**
- Store locator, so the doors file is header-only and the stockists file has one row marked `NC`.
- 20-F store count, factory list and controlling holder.
- Craft product-page facts (named makers, made-in share, process).
- Founder and founding place.
- Quote, lookbook, B Corp and GOTS.

**Contradictions and flags**
- facts-first gave "Arizona Mixed Synthetic $117.95" as the entry price. The true low is $34.95 (EVA). Its high of $220 is also beaten, by $240 (Prescott Lace Men).
- The men's grid leaks kids' product (Arizona Kids EVA, Zermatt Kids) and women's socks.
- The Bend Low tile shows its price inconsistently ($165 listed, "Was $160").
- Doors (22 US / 111 world) are carried from facts-first unverified. Facts-first itself says those are press figures, not the locator.

**Craft.** Proposed 4, provisional. The group's own press pages are titled with investment in and expansion of its own German production sites (Görlitz is named). The 20-F was not readable to confirm that the core range is made in owned plants. If it confirms that, the score should go to 5.

**Brief issues.** Tech uses a provisional scale; no tech rubric was issued. Proposed 3: own-named materials (Birko-Flor, Birkibuc) appear on part of the range, and their share was not counted.

**Next.** Rerun sections 4, 8 and 11–13 and listing pages start=408 to 840 when WebFetch is available.


### Doors — browser read 2026-10-10 (main thread)

own_doors_us 22 → 14. Browser read 2026-10-10: 24 Birkenstock-run US stores = 14 full-price (match the site's "Our Classic Stores" list, incl. Boston 205 Newbury St not returned by locator search) + 10 outlet-centre doors (inferred from address; locator does not mark outlets). Authorized-retailer layer (thousands) excluded. Replaces facts-first 22 (Retail TouchPoints, Jul 2026 — total incl. outlets, or a different date).

### Re-run 2026-10-10 (gap-fill, about 45 fetches, one at a time, no 429s)

**Shoe range now complete.** Read men's listing pages start=408 to 840 in default order (19 pages; 846/846 tiles across both passes).
- Low $34.95 stays. Confirmed on the Barbados Essentials EVA Black PDP: regular, unisex with men's sizes, "Made in Germany".
- High changes 240 → 320: Birmingham Slip On Men, Oiled Leather, Black. The PDP shows a regular price of $320.00, currently marked down to $208.00, so the compare-at price is used per rules_prices. The second colour (Roast) also shows Was $320.00. The PDP has no collab or limited label, but its URL slug contains "crafters", which might mean a sub-line; I could not confirm that. If you would rather use a figure that has never been marked down: Boston Bold Shearling $275.00 at full price. Other options: Boston Quilted (compare-at $300.00, marked down), Arizona Leather Croco (embossed calf) $270, London Shearling Oiled $260.
- Excluded: Arizona Lingua Franca $350, a collaboration.
- No clothing on any page. Only socks, footbeds and care items, so the seven garments stay NONE and the styles file stays header-only.

**Craft 4 → 5 (proposed).**
- The FY2025 20-F says "We own the majority of our production sites and one of our largest logistics sites, including machinery". It names Görlitz and Pasewalk (Germany) and Arouca (Portugal), and an agreement to acquire Wittichenau.
- The group production page says footbeds are all made in Germany and products are "primarily assembled in our own factories".
- The US about page says over 95% of products are made in the company's own plants. That page looks old (it gives 6,200 employees, a 2021 figure).
- Made-in is stated on all 4 PDPs read: 3 Germany, 1 Portugal (Prescott Lace).
- Horween leather is named on one PDP.
- The 20-F text the fetcher returned stopped at about 118k characters, inside Risk Factors. Item 4 (business, properties, store count, principal-shareholder %) was not reached, so the in-house share is not taken from the filing.

**Owner.** L Catterton held 55.9% before the Aug 2026 secondary. Afterwards it holds 44.75%, or 42.43% if the option is exercised (FashionUnited, 17 Aug 2026, citing the SEC prospectus supplement). The press figure was not checked against the filing.

**Stores (doors file not touched).**
- own_doors_world 111 is now confirmed from the company's Q2 FY26 6-K (31 Mar 2026: Americas 17 / EMEA 46 / APAC 48). FY2025 year-end was 97.
- Contradiction: the company counts 17 own stores for the whole Americas at 31 Mar 2026, but the browser read found 24 US "Birkenstock store" doors (14 full-price + 10 outlet). Possible reasons: openings since March, outlets counted outside "own retail stores", or some outlet-centre doors run by a third party. Worth a look before the 14/10 split is relied on.

**Founding.** From the brand's own group history page: 1774 is the "first documented mention of Johannes Birkenstock (1749-1812)", with family roots in Langen-Bergheim. Konrad Birkenstock opened his Frankfurt shop in 1896. So 1774 is a documented shoemaker, not a company founding. The cells say so.

**Other cells.**
- Quote: "The guiding idea has been to create shoes that are good for your feet." (group history page, undated). Alternate: "Everyone should have access to our footbed." (US about page).
- Signature product: Arizona, in the brand's words "might just be the quintessential BIRKENSTOCK shoe".
- Lookbook: no. /us/magazine/ has only Birkenstory profiles, and no current own-label seasonal lookbook was found. Collab lookbooks exist.
- Grailed designer page and Vinted id 3203 (men's catalog) are both now verified.
- Stockists: one summary row. locator_kind is "store locator", with an Authorized-retailer layer of thousands of doors (3,547 near NY / 4,205 near DC filter counts). Retailers are not listed.

**Still NC.** B Corp (the B Lab directory fetch errored; no claim seen), GOTS (no claim on the pages read), tech_share_of_range (not counted). Status stays partial on those cells only.


## Calvin Klein


**Status: partial, mostly NC.** About 20 minutes in, the WebFetch proxy began returning HTTP 429 ("rate limited… other pages may be refused too"). It refused every request for the next ~30 minutes, on every domain tried: calvinklein.us, stores.calvinklein.us, sec.gov, pvh.com and ro.calvinklein.com. Bash egress to www.calvinklein.us and stores.calvinklein.us is refused by the organization's egress policy (CONNECT 403), so the sitemap route was closed too. No block was worked around. This looks like a shared proxy limit (several wave-A workers running at once), not a WAF on calvinklein.us. **A re-run should close most of this record.**

### What was read (2026-10-08)
- **Store:** calvinklein.us/en/men. Salesforce Commerce Cloud (`Sites-PVHCKUS-Site`); prices in $.
  - Promotions running: "Friends + Family 40% off Sitewide", 30% off underwear, and an extra 20% off $125+.
- **robots.txt:** disallows /search and /product. Sitemaps: /en/sitemap_0.xml and /en/sitemap-products_sitemap_0.xml (not read).
- **Men's tees listing** (/en/men/apparel/tshirts-tanks):
  - It reports 245 items. These are colourway tiles, 16 per page, paged with `?start=`; `sz` is ignored. `srule=price-low-to-high` sorts on the sale price, not the compare-at price.
  - 48 tiles were read. The compare-at prices seen ran from $35.00 (CK Sport Mesh T-Shirt GMS6K114; tile only, the PDP returned 429) to $99.00 (Tech Knit Crewneck Sweater T-Shirt 40BM348).
  - **These are not filed as low/high**, because 197 tiles were unread and the sort order cannot surface the true compare-at extremes.
- **Second-product compare-at check:** Monologo Tee 4RB861G.
  - Its PDP for colour YAF shows full price $39.00 and sale $19.50.
  - The same style shows $45.00 compare-at on five other colourways.
  - So compare-at varies by colourway. Read several colours before trusting any one figure.
- **Fibre:** one PDP read (Monologo Tee: "100% cotton", "Imported"). No aggregate was filed.

### Not reached (NC)
- Prices for all eight garments.
- Men's listing links other than tees. The candidate URLs from the men's nav are in the row `note`; their tiles were not read.
- The style census and the fibre split, including the underwear/swim denominator handling.
- The doors file: no doors read, so it is header only.
- Stockists.
- Tech, craft, founding, lookbook, Vinted/Grailed, B Corp/GOTS, quote and signature product.

### Contradictions / flags
- **US door count.** facts_first's 114 is the locator total. It includes PR (2) and GU (1), and (per facts_first) the CA page is all outlet centres.
  - The PVH 10-K says North American stores are "primarily located in premium outlet centers."
  - **own_doors_us is not established. Do not seat 114.** The full-price figure may be near 0, but that is unverified.
  - The per-door venue classification the brief asked for was not done.
- **Calvin Klein Collection** (the runway line under Veronica Leoni) is sold at /en/calvin-klein-collection/men (seen in search results only).
  - Under the rules it is never a price high.
  - Sebastian may want to rule whether it is a sub-line to scope out of the fibre read.
- **owner_today = PVH Corp.**
  - It rests on the FY2024 10-K as cited in facts_first. The FY2025 10-K (pvh-20260201.htm) exists but was not reached.
  - Founding (1968, New York, Calvin Klein and Barry Schwartz) is widely reported but was not read on a brand or filing page, so it is NC.

### Brief
The re-run needs a WebFetch budget that survives the tees listing alone: 245 tiles at 16 per page is 16 fetches. Full men's apparel at that page size will be several hundred fetches before any PDP is opened. A documented sample (two price-sorted pages per category plus about 10 PDPs per category) is the realistic scope.

### Re-run 2026-10-10 (gap-fill)

**Status: still partial.** I made about 106 fetches, one at a time, with no 429s. I did not attempt the doors: the main thread is reading the locator in a browser. While this run was going, `doors_calvin_klein.csv` gained about 115 rows written by the main thread; I left it untouched. own_doors_us and own_doors_world stay NC pending that read.

**Prices (all eight filed).**
- **How they were read.** Every figure is the compare-at price, and each filed figure was confirmed on its PDP.
  - Listings show 16 colourway tiles per page. Sorting is on the sale price, and every tile I saw was 30–65% off.
  - Per category I read: default page 1 (polos p1–p2), sale-sorted low-to-high page 1 (tees, polos, sweaters p1–p2), and high-to-low page 1.
  - Floors are therefore near-proven, not fully proven. An unseen tile has a sale price at least as high as the last tile read, so its compare-at could only fall below the filed low with a deeper discount than the tiles already seen.
- **Factory exclusion (a judgement — please rule).** "Factory"-badged (made-for-outlet) styles were excluded from lows and highs as not main range. Where this changed a figure:
  - dress-pants low: $129 instead of $89;
  - sweater low: $89.50 non-Factory against $89 Factory.
- **Calvin Klein Collection** (Spring 2026, 20 men's items, $250–$1,950) is excluded from prices and from the fibre sample.
- **Licensed CK-label categories are counted** (per the PVH FY2025 10-K): tailored clothing by Peerless, footwear by MBF Holdings, swim by G-III.
- **Compare-at varies by colourway** on several styles; the examples are in the row note.
- **Listing links.** All eight are navigation category pages. I checked the tiles on each, and all were men's.
  - dress_shirt: "Shirts" (button-ups). There is no dress-shirt category.
  - dress_pants: the "Pants" parent, which mixes chinos.

**Fibre: a documented sample, not a census.**
- **The sample.** 55 men's styles across 11 categories. 54 PDPs were read today; the 55th is the Monologo Tee from 10-08. Styles were picked from the tiles read; they were not drawn at random.
- **Result.**
  - Natural-led 40 (73%), synthetic-led 12 (22%), cellulosic-led 2 (4%), undisclosed 1. The undisclosed one is a swim short, out of stock, with no composition shown.
  - Elastane on 14; 5% or more on 6.
  - Underwear and swim (3) are in the denominator.
- **Shape is not filed.** Only tees-polos reaches 10 styles in the sample.
- **Synthetic leads in the sample** in pants (2 of 3: the Refined Stretch Pant and the Tech Classic Pull-On), in the activewear shorts, in 3 of 7 outerwear (bomber, Harrington, puffer shell), in 3 of 9 knitwear, and in 1 of 5 sweats (Sherpa hoodie).
  - "Merino blend" knits are 55% PET / 45% wool. Polyester leads despite the name.
  - The "Quilted Nylon Overshirt" PDP says 74% cotton / 26% polyester. It is filed as written.
- **Composition on the PDP:** 54 of 55. **Country of origin:** 54 say only "Imported"; one blazer is "Made in Italy".
- **Listing tile counts (overlapping colourway tiles):** tees 246, polos 123, shirts 139–141, sweaters 128, outerwear 122, jeans 58, pants 94, fleece 124, suiting 14, activewear 22, swim 13 (8 styles), underwear 573.

**Sections 6–13.**
- **Tech: proposed 2.** This is a provisional scale; no tech rubric was issued.
  - Named fabrics: "Liquid Touch" (the house's own fabric name) and LENZING ECOVERO (a licensed fibre brand). Together they appear on 3 of 55 sampled styles.
- **Craft: proposed 1.** No owned facility: the 10-K says all ~1,000 factories are independent. No makers named. One mill named (Lanificio di Tollegno, on one blazer). No process documented. Origin is stated as "Imported", with no country.
- **Founding.** 1968, New York City, per calvinklein.us About Us and the 10-K.
  - Founders: only Calvin Klein is evidenced. Barry Schwartz was not stated on any brand or filing page read.
- **Ownership.**
  - PVH Corp. owns the trademarks, per the FY2025 10-K (pvh-20260201.htm). Calvin Klein was acquired in February 2003. ownership_url was updated from the FY2024 10-K to the FY2025 one.
  - **No store count in the 10-K text I could read.** WebFetch rendered only ~110k characters of the filing, and that text has no Item 2 store count.
  - The filing's wording is now "In Americas, our stores are primarily located in premium outlet centers and, to a lesser extent, in full price and other channels."
- **Lookbook.** The Calvin Klein Collection "Spring 2026" runway page (56 looks). The looks are not labelled by gender; the shop links cover men and women, so this is filed as mixed.
- **Grailed.** /designers/calvin-klein exists. The feed had not loaded when the page was captured.
- **Vinted.** The brand id was not found (the brand page exposes no id), so it is NC.
- **B Corp.** NC: the B Lab directory fetch errored.
- **GOTS.** NC: not checked.
- **Quote.** Calvin Klein, from the calvinklein.us About Us page (verbatim, undated).
- **Signature product.** Logo-waistband underwear. The PVH brand page says "Designer underwear for all. Instantly recognizable waistband".

**Still NC / not reached:**
- Stockists: whether calvinklein.us lists third-party stockists was not checked.
- search_url (robots disallows /search; not tested).
- styles census, colourway_ratio, swim share.
- Vinted, B Corp, GOTS.

**Changed from the earlier record:**
- ownership_url: FY2024 10-K → FY2025 10-K.
- doors_basis: re-worded to say the browser read is pending. The 10-K quote is updated to the FY2025 wording.
- No other non-NC values changed.


### Doors — browser read 2026-10-10 (main thread)

own_doors_us NC → 2. Browser read 2026-10-10: 115 US locations (index sums to 114) = 113 outlet + 2 full-price (530 Broadway SoHo; Rookwood Commons, Norwood OH). Includes GU 1, PR 2. CK Underwear banner 8 doors, all outlets. 14 Mills-type value malls classed outlet.


## Chrome Hearts


### What was checked (all on chromehearts.com unless noted)
- **Home and shop navigation.** The shop has Baccarat, Scents, Underwear (Boxers & Leggings, Intimates, Socks) and nothing else. There is no site search, so `search_url` is NONE. It is not Shopify. curl to the domain was refused at the proxy CONNECT (403), so no feed or sitemap was read.
- **Boxers & Leggings: 6 products, all PDPs read.** Intimates has 6 products, all women's (lace bra, teddy and similar). Socks has 6 products at $255 each; socks are out of fibre scope.
- **Locator** (`/stores`): 36 listings across 9 countries. They split into 29 standalone or mall doors and 7 department-store concessions. The **US has 10, matching facts-first**: Miami is "Temporarily closed" and 7 of the 10 are "Schedule appointment". There are no outlets. The locator never says who operates a store, so every door is counted as the brand's own, unverified.
- `general.html`, `disclosure.html` (CA Supply Chain Act), `magazine.html` and two magazine issue pages. The issues are flipbooks hosted on fliphtml5 and were not read.

### Garments (section 2)
- The site never names clothing. Its meta line reads "Fine Jewelry, Accessories, Shoes, Fragrance & Home Goods Made in the USA", and it has no lookbook.
- **I could not tell from its own site** whether tees, jeans and the other garments are made and unpriced (`np`) or not made (`NONE`). So the 7 clothing garments are `NC`, not guessed. Secondary sources (Wikipedia) say Chrome Hearts makes clothing. A read of the brand's Instagram or of a store would settle it.
- **Shoes are `np`**: the brand's own meta line names shoes.
- The underwear is not one of the 8 garments.

### Fibre
- **Tiny:** 5 men's styles, 4 boxer briefs and the Long Johns. All are cotton-led, and 5 of 5 PDPs say MADE IN JAPAN.
- Leggings were excluded: they run XS–XL with a 20–25 in XS waist, so they are likely women's. **No page states a gender.** The Long Johns were included by garment type; flag for a ruling.
- Four bodies read "95% COTTON, 5% POLYURETHANE". I counted that as elastane (spandex is a polyurethane fibre); flag for a ruling. If it is not elastane, `spandex_styles` is 0.
- **Price conflict:** the Classic Rib boxer shows $130 on the listing and $120 on its PDP.

### Contradictions
- **The site claims "Made in the USA"**, but every priced garment read says Made in Japan.
- **The brief lists "Richard and Laurie Stark" as founders.** Wikipedia gives the founders (1988, LA) as Richard Stark, Leonard Kamhout and John Bowman. Laurie Lynn Stark is co-owner since 1994. Ownership is private (Chrome Hearts LLC); there is no filing.
- **Craft:** the in-house LA (Hollywood) factory is **a claim at second hand only.** The own site shows no factory, no maker and no process. Its CA Supply Chain disclosure says it does not audit suppliers.
- **Proposed craft is 2, low confidence.** It could be 4 once WSJ (1 Nov 2021) or CFDA is read first-hand.

### Not reached
- **The WebFetch proxy returned HTTP 429 after about 20 reads.** These pages are unread: WSJ 2021, WWD 2019, Complex, CFDA, and the fliphtml5 magazine.
- As a result these fields are `NC`: quote, signature product (the signature pieces are not on the brand's store), Vinted id, B Corp and GOTS.
- B Corp: a search restricted to bcorporation.net found no Chrome Hearts listing, but the directory itself was not opened.
- Grailed `designers/chrome-hearts` is confirmed only by indexed sub-pages. Its top page was not opened.
- **Currency:** prices show as "$" and the footer reads "US", but the PDPs told the fetcher "not available in your country".

### Brief note
"Prices only underwear/socks" omits women's intimates, Baccarat crystal and scents, which are also priced. The tech scale is provisional, as stated in the spec; the score here is 1.

### Re-run 2026-10-10 (gap-fill)

Doors file left as is (36 world, 10 US). Styles and stockists unchanged (no new garment PDPs exist on the store). About 30 fetches, made one at a time, with no 429s.

### Garments: np or NONE
- **Own site, re-read.** general.html, magazine.html and magazine S2 V7 were re-read. The site still names no clothing. The fliphtml5 flipbook (online.fliphtml5.com/zossf/zmzk/) exposes metadata only, and its search-text asset errored. **Nothing first-party names a garment.**
- **Tee: NC → np.** In WWD (4 Dec 2019) Laurie Lynn Stark says: "you could grow the T-shirts and have everyone in the world wearing them, but we want to control what we make." That is press quoting the brand about a garment it makes, and the store prices no tee.
- **Jeans, polo, dress shirt, dress pants, sweater and outerwear stay NC.** Press describes most of them, but none of it comes from the brand's own pages or the brand's own quoted words:
  - **Jeans:** "cross-shaped leather patched vintage denim" (WWD 2019, writer's words); "$1,750 denim" (Complex 2020); custom denim "at their Los Angeles factory" (OPENERS, posted 2015, describes SS2010).
  - **Outerwear:** leather jackets appear in Complex, WWD 2019, W 2016 and OPENERS, always in the writer's words.
  - **Dress shirt:** a check shirt in OPENERS 2010, editorial.
  - **Dress pants:** Richard Stark (PAPER 2012, via a stylezeitgeist repost) says he works on "a desk, or a door, or pants, buttons, whatever". That shows Chrome Hearts makes pants of some kind, not dress pants or chinos.
  - **Sweater:** WWD 2019 says cashmere is made in Italy with Loro Piana but names no garment.
  - **Polo:** nothing found.
- **Recommendation for ruling:** jeans and outerwear are np on press consensus if a writer's description is accepted, and dress pants np on the Stark "pants" line. I have not entered these.

### Primary sources read first-hand
- **WSJ, 1 Nov 2021** (Gallagher, "Is 'Made in the U.S.A.' Dead? Not For L.A. Brand Chrome Hearts", wsj.com/articles/chrome-hearts-los-angeles-11635778730): WebFetch returned SITE_BLOCKED. I did not use the archive.org copy, to avoid working around the paywall. **Still unread.**
- **WWD, 4 Dec 2019** (Booth Moore, "Moore From L.A."). The page shows no date; the date comes from Wikipedia's reference and Complex's "2019".
  - The Hollywood campus is 250,000 sq ft, with 13 buildings and eight factories "that make apparel, accessories, furniture, eyewear and more".
  - There is a division per craft (woodworking, leatherwork, metalworking). The article calls this "vertical manufacturing" and gives 900 employees.
  - Cashmere is made in Italy with Loro Piana, and crystal in France with Baccarat.
- **CFDA, 23 Oct 2015** (cfda.com/news/cfdainla-focus-on-manufacturing): Laurie Lynn Stark says 90% of goods are produced "under one roof in the Hollywood facility", with 600+ employed.
- **CFDA, 2022 awards:** the Geoffrey Beene Lifetime Achievement award went to Laurie Lynn and Richard Stark. Nothing on manufacturing.
- **CFDA member profile URL:** fetch error.
- **Complex, 2 Jul 2020:**
  - The brand began in 1988 in an LA garage, started by Richard Stark and leather maker John Bowman. Silversmith Leonard Kamhout "joined shortly after", and the three split in 1994.
  - Complex gives the same campus figures as WWD.
  - Its quotes are second-hand from the Japan Times (1999) and WWD.
- **Founders: kept, reordered.** Old: Stark; Kamhout; Bowman. New: Stark; Bowman; Kamhout, with Complex's nuance added. Wikipedia names all three for 1988. Laurie Lynn Stark is a co-owner and co-recipient of the CFDA award. L'Officiel's editors call her "co-founder", but that is their word and does not settle it.

### Craft, re-proposed: 2 → 4 (medium confidence)
- **owned_facility is now evidence**, not a claim: CFDA 2015 and WWD 2019 both quote the owners and describe the site.
- **named_mills:** Loro Piana appears in press only, on no PDP.
- **heritage_claim:** now dated and placed from press.
- **craft_url_1 and craft_url_2** changed from the own-site disclosure page and boxer PDP to CFDA and WWD, the two carrying the most weight.
- **Why not 5:** the own site documents none of this, and the only garments priced online say MADE IN JAPAN.
- **Contradiction still standing:** "Made in the USA" and "90% under one roof" against Japan-made underwear.

### Sections 6–13
- **Quote:** Richard Stark, WWD 2019: "It's so hard to find craftsmen. We will hire you and teach you and pay you to keep the arts alive" (20 words). Alternate: Laurie Lynn Stark's T-shirt line above.
  - **Flag:** this quote was read through WebFetch's summariser. Confirm the wording on the page before publishing.
- **Signature product: NONE on own store.** The store sells none of the recognised pieces. Complex calls the gothic trucker hat and the leather-cross denim the most recognisable items, which is the writer's view.
- **Vinted:** brand id 95106. vinted.com/brand/95106-chrome-hearts is titled "Chrome Hearts". The URL is built with catalog 5 per the spec, and the built URL itself was not opened.
- **Grailed:** the designers/chrome-hearts top page was opened and is confirmed.
- **B Corp: no.** The JS directory does not render to the fetcher, and two domain-restricted searches found no listing.
- **GOTS: no.** No GOTS claim appears on the PDPs and a search found none. The GOTS database itself was not queried.
- **Lookbook:** none exists. Richard Stark is quoted (Japan Times via Complex): "We don't have any seasons." lookbook_mens and lookbook_url changed NC → NONE.

### Status
Still partial: six garments remain NC pending a ruling on press descriptions, and WSJ 2021 is unread.


## Cole Haan


**Why partial.** After about 12 successful reads, every WebFetch call (colehaan.com, en.wikipedia.org, wwd.com, sec.gov, stores.colehaan.com) came back HTTP 429 from the WebFetch proxy, and it stayed that way through 15+ minutes of retries. It looks like a shared rate limit, not anything Cole Haan did. Bash curl to www.colehaan.com was refused with 403 CONNECT by the egress policy, so it could not be used for the feed. I did not try any way around either block.

**What was read (2026-10-08)**
- Store nav at https://www.colehaan.com/ — Shopify store in USD. Under Men the nav lists shoes, outerwear (under "Outerwear"), bags and accessories. It has no apparel menu.
- `/collections/mens-outerwear-and-apparel/products.json?limit=12&page=1..6`: 53 listings, page 6 empty. These collapse to 26 styles on the `YGroup_P…` tag (one colourway per handle). Composition is in body_html. Every listing says only "Imported", so made_in_stated_share = 0 on outerwear.
- The search `search/suggest.json?q=men's sweater / men's shirt` found **own-label men's tops that are not in the nav**: Founders, Ashland, Cobbler, Trafton and Links polos (T501xx handles) and the Last Stitch Quarter Zip (T50167, $148 list, "Drirelease® technology", no fibre named). The brief's "outerwear/clothing" is right: Cole Haan sells outerwear plus a small golf/knit tops line. The polos were found but not read, because the 429 began. No tees, dress shirts, jeans, dress pants or crew sweaters turned up, but I have not confirmed they are NONE, so those slots stay NC.
- One extra style was seen in the root feed only: Men's Stand Collar Puffer Vest (t40517, $98 compare-at). It is not in the outerwear collection and is not counted.

**Prices.** The site was on promotion on the 8th, so every figure is the compare-at price. Outerwear basis is `range`:
- Low: $258.00, Coated Cotton Barn Coat t40502. Faux Suede Quilted and Quilted with Faux Sherpa are also $258.
- High: $698.00, Smooth Leather Racer Jacket t40498. On Suede Harrington t40496 the sale price equals the list price, $698.00.
- Excluded: Nylon Puffer Vest at $98 (it is a vest) and Smooth Lamb Shirt Jacket at $698 (it is a shirt-jacket).
- Shoes are NC. Facts-first's $175 GrandPrø Topspin and $310 ZERØGRAND oxford were not re-read, and neither is a loafer. The loafer listing URL is taken from the nav only; I did not read its tiles.

**Fibre, on the 27 styles read.** 15 are natural-led (9 wool-blend, 5 leather/suede, 1 cotton), 10 synthetic-led (6 polyester, 4 nylon) and 2 undetermined. That gives 56 / 37 / 0, with 7% undetermined.
- Several "wool" coats are actually polyester-led: the Stretch Wool Top Coat (57% and 64% polyester) and the Wool Peacoat (62% polyester).
- Many newer styles name the fibres without percentages ("Wool-blend shell", "Nylon shell"). Their lead_pct is ND. spandex_styles and shape are NC because the polos were not read.

**Not reached, all NC:** the store locator and doors file (header only; press says "over 100 stores across the US" with no outlet split), stockists (header only, not checked), tech ownership and score (no tech rubric issued in any case), craft, founding facts, lookbook, Vinted/Grailed, B Corp/GOTS, quote, signature product and pronunciation. I did not fill founding (1928, Chicago, Trafton Cole & Eddie Haan) from memory, because I did not read it this pass.

**Contradictions with the brief or facts-first**
- The shelved IPO was a **2020** S-1 (EDGAR CIK 1791100, filed Feb 2020), not 2023. That date comes from the search result title only; I did not read the filing.
- Apax ownership dates from the deal completed Feb 2013 (announced 2012). Current ownership was not re-verified for 2026.
- Facts-first said listing pages show no prices. The collection JSON does carry prices and compare-at prices.
- Shopify product_type is unreliable: several garments are typed "Test".


### Doors — browser read 2026-10-10 (main thread)

own_doors_us NC → 23. Browser read 2026-10-10: 103 US stores = 79 outlet + 24 full-price (23 open + Boston Prudential coming-soon). Venues inferred from addresses. World: locator header 393 stores / 43 countries, mixes outlets; not filed.


### Re-run 2026-10-10 (gap-fill)

About 60 WebFetch calls, made one at a time, with no 429s. I did not touch the doors file or the door columns.

**Prices**
- **Shoes: pair, $150 to $320.** I read the mens-loafers feed in full (`products.json?limit=5`, pages 1–9; page 9 was empty; 38 listings).
  - Low: $150.00, Men's American Classics Hampton Loafers c39762. It sells at full price, and c43270 carries a $150.00 compare-at.
  - High: $320.00, Men's Ledley Grand Penny Loafers c41474, at full price (c41473 and c44501 are the same).
  - The 4.ZERØGRAND Penny compare-at of $230.00 sits inside that range.
- **Polo: range, $98 to $118.** The collections sitemap shows a `mens-golf-apparel` collection that is not in the nav. Its feed has 37 listings, which collapse to 14 styles.
  - Low: $98.00, Ashland Polo t50151, at full price. Founders and SkyWeave have a $98.00 compare-at.
  - High: $118.00, Links Legend Polo t50216. Iconic and All-Day Floral are also $118.00.
  - There is no polo collection, so the listing link is the golf-apparel parent category, which is men's only.
- **Outerwear low changed from $258 to $218.** The new low is Men's Windward Jacket t50173 at $218.00 full price. It is a golf jacket sold in mens-golf-apparel, not in the outerwear collection. The range rule takes the cheapest jacket.
- **Tee, dress shirt, jeans, dress pants and sweater are now NONE.** The collections sitemap has no men's collection for any of them. Site search for pants, t-shirt, jeans, button down and sweater returns only shoes, belts, polos and women's coats.
  - Sweater NONE is a judgement call: the only men's knits are the Last Stitch Quarter Zip ($148, jersey knit) and the Artisan Vest ($158/$178, textured knit). Neither is a crewneck. Sebastian to rule.
- search_url is `/search?q=`. Tested with "polo": 956 results, mixed gender.

**Styles**
- Added 13 golf-apparel styles, for 40 in total. None of them names a fibre, for example "Knit jersey fabric with Coolcore® technology", so all are ND.
- Split by style: 38% natural, 25% synthetic, 0% cellulosic, 37% undisclosed (25 of 40 have a composition). colourway_ratio is 90/40.
- spandex_styles and shape stay NC: 8 styles say "four-way stretch" but name no fibre.
- swim is 0, and 40 is the read count.

**Sections 6–13**
- **Founding:**
  - Year: the brand says only "since 1928" (about-us) and gives no place.
  - Founders: the 2020 S-1 names Trafton Cole and Eddie Haan.
  - Place: Chicago, from the Chicago History Museum (emuseum.chs.org), which is not the brand. Sebastian may want founded_place held, since the brand does not state it.
- **Ownership:** I found no sale after Apax's 2013 deal. The Apax all-investments list carries Cole Haan with no status, so "current in 2026" is not proven.
- **Tech:** The trademarks and patents page lists ZERØGRAND, Grand.OS, StitchLite, FlowerFoam, FlexCraft and SkyWeave as owned marks, with about 221 patents. Coolcore and Drirelease are third-party, so the cell is `both`.
  - Share is 20% (8 of 40 clothing styles carry Coolcore or Drirelease).
  - Proposed 4 on the provisional scale, because owned "Grand" technology runs through most of the loafers read.
- **Craft, proposed 1:**
  - Every page read says only "Imported": 53 outerwear listings, 14 golf styles and 2 loafers.
  - The supply-chain disclosure describes contract factories and names none. The leather claim is "BLC medal-rated tanneries", with the tanneries unnamed.
  - The S-1 gives Vietnam and India as the primary countries of origin.
- **Lookbook: no.** The blogs sitemap holds only /blogs/news, and the pages sitemap has no lookbook.
- **Resale:** Vinted brand id is 69794 (from search-indexed vinted.com URLs). The Grailed designer page exists, titled "Cole Haan Clothing for Men".
- **B Corp: no.** The directory search would not render, the guessed profile URL returned a client error, there were no search hits, and the brand's responsibility pages do not mention it. GOTS is NC; I did not check the directory.
- **Quote:** from about-us, undated. I read it the same way in two separate fetches.
- **Signature product:** ZERØGRAND wingtip oxford (Remastered c45383). This is my judgement, based on about-us calling ZERØGRAND the evolution of its outsole.
- **Pronunciation:** NC, with no source found.
- **Stockists:** the brand lists none. Its locator shows own stores and outlets only. The international-distributors page lists 60 non-US territory websites and names no retailers. Department-store wholesale (Nordstrom and Bloomingdale's, per the S-1) is real but not published as a list.

**Still NC:** feed_currency_rate, own_doors_world, spandex_styles, shape, GOTS, pronunciation. Status stays partial.


## COS


**How it was read.** About 65 WebFetch/WebSearch calls, one at a time, with no HTTP 429.
- Bash curl to cos.com was refused at the proxy (CONNECT 403). No feed or sitemap was pulled.
- WebFetch refused `/en-us/search` as robots-disallowed, so `search_url` is NC.
- `/en-us/about` and `/en-us/design-and-craft` returned fetch errors.
- Doors were not attempted, per the brief: a browser worker is reading the locator. `doors_cos.csv` is header-only; `own_doors_us`, `own_doors_world` and `locator_url` are NC, and `doors_basis` reads "browser read pending".

### Section 1–2: store and prices
- **Store.** cos.com/en-us is the COS US store, priced in USD. It is not Shopify.
- **Live offer.** A "Friends & Family: 25% Off" offer was running, so most tiles showed a markdown. Every filed figure is either the struck-through compare-at or an unmarked full price. Second-product checks agreed:
  - $35 for both the Cotton crew-neck tee and the Regular-fit tee.
  - $89 for both the Pima poplin shirt and the Camp-collar cotton shirt.
  - On product pages, the $110 Signature jeans and the $159 Rider selvedge showed no compare-at.
- **Grids read:**

| Category | Tiles read |
|---|---|
| tees | 90/92 |
| polos | 48/50 |
| shirts | 96/104 |
| jeans | 39/39 |
| pants | 96/123 |
| knitwear | 96/157 |
| knitwear/cashmere | 31/31 |
| coats & jackets | 62/62 |
| shoes | 8/8 |

  All menswear is 542 colourway tiles (`/men/view-all`).

| Garment | Low | High | Basis |
|---|---|---|---|
| Tee | $35 Cotton crew-neck | $229 Cashmere-linen henley t-shirt | range |
| Polo | $59 Interlock cotton | $279 Seamless pure cashmere polo shirt | pair |
| Dress shirt | $89 Relaxed pima poplin | $189 Relaxed silk shirt | range |
| Jeans | $110 Signature regular | $159 Rider raw selvedge | range |
| Dress pants | $129 Cotton slim-fit (Suits > Trousers) | $249 Wool-twill regular tapered (Bellucci cloth) | range |
| Sweater | $99 Slim merino crew | $359 Cashmere crew (GCS) | pair |
| Outerwear | $139 Bonded-twill harrington | $649 Leather blouson | range |
| Shoes | $199 Split suede loafers | $199 Leather penny loafers | pair |

**Flags for Sebastian's ruling:**
- **Tee high.** $229 is a henley t-shirt in the t-shirt path; I found it on the cashmere grid, not in the 90 tee tiles I read. The dearest crew-neck tee seen is $99 (Layered knitted cotton; Ribbed merino wool-cotton). The silk-cotton henley is $139.
- **Dress shirt high.** These were left out of the high:
  - Double-faced pure cashmere shirt, $649 (1348214). It is excluded from the offer and not labelled RUNWAY, but it uses the same 480gsm double-faced cashmere as the RUNWAY coat and blazer, and it is overshirt-weight.
  - Textured-leather shirt, $399. It is not woven.
  - Wool shirts at $249 (1354277, 1354281). They are excluded from the offer, and their runway status was not checked.
- **Outerwear high.** These were left out:
  - Tailored double-faced cashmere coat, $999. It is labelled "EXCLUDED FROM OFFER | RUNWAY".
  - Padded shearling bomber, $999. It is fur-on.
  - Tailored padded leather coat, $749 (1354285). It is excluded from the offer, and its runway status was not checked. If it is regular, the high becomes $749.
  - Tailored double-faced cashmere blazer, $699. It is RUNWAY, and blazers are out of outerwear anyway.
- **Facts-first's $649 outerwear top stands.**
- **Shoes.** The loafers sit at a single $199 price point across three styles. Mules ($169–$199), derbies ($249), boots ($329) and plimsolls ($110) are not loafers.
- **Jeans listing.** `/men/jeans` mixes in denim jackets, overshirts and shorts, though every item is men's.
- **Dress pants listing.** No dedicated dress-pant node was read. `/men/trousers` is the parent, and Suits > Trousers items sit inside it.

### Section 3: fibre (not a range census)
- **US product pages publish a composition line ("Shell: …% …. Excluding trims") on only a minority of styles.**
  - 7 of the 29 men's product pages read had one, all natural-led. The rest describe fibres in prose only ("mulberry silk and cotton knit", "technical nylon"), so they are ND.
  - The pages that do carry a composition skew to certified fibre (RWS merino, GCS cashmere) and organic/recycled cotton. That makes `natural_pct` 24 / `synthetic_pct` 0 / `cellulosic_pct` 0 a property of the sample, not of the range.
- **Summariser caveat.** One page (1281644) read "absent" through an en-eu fetch with a loose prompt and "Shell: 100% Cotton" on the US page with a precise prompt. Some ND rows may therefore be summariser misses. A browser or payload read would settle it.
- **Census not done.** `styles_total` is NC.
- **Colourway ratio** is from the tee grid only: 89 tiles collapse to 43 seven-digit stems, so 89/43 ≈ 2.07. At that ratio the 542 menswear tiles would be roughly 260 styles. That is an estimate and is not filed.
- **Product codes.** A style is the 7-digit stem, and the last 3 digits are the colourway.
- **Not established:** swim (no swim node in the men's nav), `shape` and the category splits.

### Sections 6–13
- **Tech.** No proprietary or licensed named fabric was seen ("technical nylon", "tech-twill" and "scuba-jersey" are generic), so `proposed_tech` is 1. This is on a **provisional scale: no tech rubric was issued.**
- **Craft: proposed 2.**
  - No owned facility. The "London atelier" is a design studio for sketching and draping.
  - 0 of 29 product pages state a country of manufacture or name a maker.
  - One page names a mill: Mario Bellucci, Prato, on 1354279.
  - Two name fibre standards: RWS TE-00047206 and the Good Cashmere Standard.
  - Heritage is dated and placed: "Since 2007", and the first stores opened on Regent Street in March 2007 (Marie Honda, Dezeen 2014).
- **Ownership.** COS is an H&M Group brand (`hmgroup.com/brands/cos`), and the H&M Group 2025 Annual & Sustainability Report (FY Dec 2024–Nov 2025) lists it.
  - The report gives no COS-only or US store count. The only Americas figure is "North & South America" at 769 group stores.
  - hmgroup.com/brands/cos contradicts itself: the text says "257 stores in 50 physical markets", and the figures panel says 200 stores and 40 store markets. Neither is a US figure.
  - It also shows "founded 2025", which is wrong. 2007 is filed, per Honda and cos.com.
- **Lookbook.** The Autumn Winter 2026 runway page exists. The page fetched is women's, with a "Men AW26" toggle, so it is filed as mixed.
- **Vinted and Grailed.**
  - The Vinted COS brand id is 2029 (from a vinted.fr item's brand link). vinted.com with that id and catalog 5 shows "COS" under Men, with 366 results.
  - grailed.com/designers/cos exists.
- **B Corp and GOTS.** NC. The B Lab directory search renders by script, and the GOTS database was not searched. Nothing on cos.com claims either.
- **Quote.** Marie Honda (then MD), Dezeen, 5 Nov 2014. An alternative is the cos.com sustainability page: "Since 2007, the COS ethos has always put exceptional craftsmanship and timeless design first."
- **Signature product and pronunciation.** NC. No brand-stated signature product was found, and no authoritative pronunciation source was checked.
- **Stockists.** One NC row. COS publishes no stockist page that I saw. The locator, which is being read in the browser, may show partner doors.

### Contradictions
- **Facts-first's 12 US stores (Modaes, Jul 2026).** Neither confirmed nor contradicted here, since doors are not attempted. H&M's 2025 report has no US COS figure.
- **Facts-first's tee entry of $45 (Slim ribbed).** This is not the cheapest. The cheapest full-price tee is $35, in two styles.
- **H&M's own brand page** is inconsistent on COS store counts and founding year, as noted above.


### Doors — browser read 2026-10-10 (main thread)

own_doors_us NC → 12. Browser read 2026-10-10: 12 US doors, all full-price (1 Flagship Spring St NYC, 4 Core+, 7 Core); read from the store data the page loaded (page crashed drawing list). 50 markets in country list. Matches Modaes 12 (Jul 2026).

### Browser read 2026-10-10 (fibre pass) — stopped at a bot wall
- First product page opened in Chrome (https://www.cos.com/en-us/men/menswear/tshirts/regular-fit/product/regular-fit-cotton-t-shirt-white-1334757002) served a "THANK YOU FOR YOUR PATIENCE" interstitial ("high interest in our latest collection… try again by refreshing") instead of the product, with Akamai-style sensor scripts under `/yvIZY9/…`. Treated as a bot check and stopped after one page load; did not refresh.
- No style re-read, no new styles, no grid counts. All fibre cells unchanged: styles_with_composition 7 → 7, natural_pct 24 → 24, synthetic_pct 0 → 0, cellulosic_pct 0 → 0, spandex_styles 1 → 1, colourway_ratio 89/43 → 89/43, made_in_stated_share 0 → 0 (sample of 29). status stays partial.
- Retry later from a fresh session, slowly; the composition check on the 22 ND styles is still open.


## Dr. Martens


About 45 fetches and searches, run one at a time. No 429s.

### The store could not be read
Every drmartens.com product, category and search page returned the WebFetch error `CLIENT_ERROR "There was an error while fetching."`. The failures were:
- men's loafers c/01020600
- Adrian Smooth Leather Tassel Loafers p/14573001
- search?text=loafer
- c/clothing
- Core Pocket T-Shirt p/AC536601
- mens c/01000000
- the UK page Embroidered T-Shirt p/AC633001
- icons/1460
- robots.txt
- the support.drmartens.com "Where are Dr Martens made" article

Bash egress to www.drmartens.com was refused at the proxy (`CONNECT 403`), so no sitemap or feed was pulled. Nothing was worked around.

Three landing pages did load, but only as script shells with no tiles or prices: /us/en/, /us/en/men, and the Made in England category page (its copy was read). This matches the failure recorded on facts-first.

**What this leaves NC:**
- All 64 garment cells, including shoes.
- Currency and search URL.
- The fibre roll-up. The styles file is header-only.

**Own-label clothing.** Site-search result titles show Dr. Martens-label clothing on drmartens.com: Core Pocket T-Shirt (AC536601), Men's Resin Polo Shirt (AC462001) and an Embroidered T-Shirt. So tee and polo probably exist, but nothing was confirmed or priced. No garment is marked NONE because nobody could check. The plc's category lists (FY26 results, AR26 p.01) name boots, shoes, sandals, kids, bags, accessories and small leather goods, and never mention apparel.

**Loafers.** The Adrian family is confirmed by search titles on /us/en/: Smooth Leather, Bex, Yellow Stitch and Platform. The FY26 results statement also gives "the Made In England (MIE) Penton Classic Calf Loafers (£220 / €260 / $260)". That figure comes from a filing, not a store read, so it is **not** filed as the shoes high. It would be the likely high if a browser read confirms it.

### Doors
- **US:** own_doors_us is NC ("browser read pending"), the doors file is header-only, and locator_url is NC. All of this is left to the main thread.
- **World:** own_doors_world is 240, from Annual Report 2026 (52 weeks to 29 Mar 2026), Finance review pp.34–35. That is 240 directly-operated stores: EMEA 102, Americas 57, APAC 81. The report does not say whether outlets are in the 240.
- **Excluded:** 15 concession counters in South Korea and 96 franchise/partner stores.
- **Stockists:** one NC row.

### Craft (proposed 3)
- **Owned factory:** this is evidence, not a claim. AR25 names "our Cobbs Lane factory in Wollaston, England". The FY26 results say Made in England footwear is made "at its original Northamptonshire factory". The brand's Made in England page mentions "our original Wollaston factory". A brand blog interview with Stephen Bent describes the factory on Cobbs Lane and a shoemaking apprenticeship.
- **Its share is small.** AR25 p.15 gives planned FY26 Tier 1 footwear sourcing as "1% from our Made In England factory in Wollaston, UK", with 62% from Vietnam, 31% Laos, 4% Thailand and 2% Pakistan.
- **Reading:** the factory is real but makes a token share of output, so I propose 3, not 4.
- **Not established:** named makers, named mills and made-in share. No product page could be read, and the AR26 text the fetcher returned stops at p.46, so the FY26 sourcing split was not re-read.

### Other cells
- **Owner:** Dr. Martens plc (LSE: DOCS). AR26 p.44 names IngreGrsy Limited as the largest single investor. That vehicle came out of a Permira V restructure and held 38.46% at 12 Jun 2024 (Nasdaq report of the RNS). Its current % was not read.
- **Founded:** 1960, at Wollaston (the 1460 boot, R. Griggs). The plc also dates the sole's origins to 1945 (Dr. Klaus Maertens) and production with Dr. Herbert Funck to 1947.
- **Quote:** the plc "Our business" page. The alternate is "As custodians of the brand, preserving its quality, image and reputation is paramount for Dr. Martens." from the plc "Our brand" page.
- **Vinted:** brand id 309, consistent across vinted.com search results.
- **Grailed:** verified (page title "Doc Martens for Men | Grailed").
- **B Corp:** NC. The bcorporation.net directory is script-rendered, and no claim was found in search.
- **GOTS and lookbook:** NC. The brand site could not be read.
- **Signature product:** the 1460. Its URL /us/en/icons/1460 comes from search and did not load to fetch.
- **Tech:** proposed 3 on a provisional scale (no tech rubric was issued). The AirWair air-cushioned sole is owned, and its share of the range was not counted.

### Contradictions
- The brief says Made in England is "its share of the range". The filing gives about 1% of planned footwear sourcing, so it is a small part of the range, not a craft-led one.
- Facts-first called the Americas count "57 ('FY26 data')". AR26 confirms 57 Americas at 29 Mar 2026.

### Next
A browser read of the US store: Adrian/loafer range low and high, the clothing listings (tees, polo, any outerwear) with compositions, and PDP made-in labels.


### Doors — browser read 2026-10-10 (main thread)

own_doors_us NC → 52. Browser read 2026-10-10: 52 full-price own doors + 3 outlets (Citadel, Las Vegas North, Livermore), identified by locator ID series 201-xxx via 52 ZIP searches (nearest-20 results; the ownStore flag is false on all records, ignored). A door in an unsearched metro could be missing. Plc FY26: Americas 57 DTC stores.

### Browser read 2026-10-10

Read the US store (https://www.drmartens.com/us/en/) in Chrome, one page at a time; no bot check, no login, nothing added to bag. About 12 page loads plus in-page site searches.

**Changed (old → new):**
- currency NC → USD (displayed $ prices on PDPs/listings; footer "United States · USD").
- search_url NC → NONE: search runs in-page only; `/us/en/search?text=…` renders no results, typed queries do (tested "loafer").
- sublines_included NC → Made in England line (counted; it sits in the men's loafer listing).
- shoes_* NC → low 150 Mayfare Smooth Leather Loafers ($150.00, p/42503001); high 260 Penton Made in England Leather Loafer ($260.00, p/31858001), basis pair, listing /us/en/mens/shoes/loafers/c/02021400. Listing: 27 items, $150–$260, no markdowns shown. $260 is a tie (Adrian MIE Quilon, Delapre MIE penny, Delapre Repello suede, Adrian Veg Tan Luxe); Penton chosen as it matches the FY26 filing figure, now confirmed on store. Adrian family runs $160 (MIE Adrian $260).
- tee/polo/dress_shirt/jeans/dress_pants/sweater/outerwear, all 8 cells each, NC → NONE. Established by: men's nav = boots, shoes, sandals, accessories (men's shop-all 210 items, no clothing words in page source); no clothing link among 52 site category links; accessories (125 items) = bags, socks, laces, shoe care; site search t-shirt, jacket, trousers = "No results found"; shirt, polo, hoodie, sweater, jeans returned only socks/footwear. The search-title garments from the first pass exist only as dead PDPs: Core Pocket T-Shirt AC536601 and Men's Resin Polo Shirt AC462001 both read "This product is no longer available". The earlier note's "own-label clothing probably exists" is superseded.
- styles_total/styles_with_composition NC → 0; swim_styles, mens_styles_excl_swim → 0; pct/shape/category/colourway/swim-share cells NC → NONE (no current clothing; no roll-up computed — fewer than 10 styles and none current). style_method filled.
- styles file: header-only → 2 rows for the legacy PDPs (100% cotton tee; polo with cotton tag, no %), both flagged not current and excluded from roll-up.
- named_mills NC → C. F. Stead, Leeds (Classic Calf leather, named on the Penton MIE PDP).
- named_makers NC → NONE named on PDPs read.

**Made-in on shoe PDPs:** Penton MIE: "Made in England at our original Wollaston factory." Adrian Smooth (14573001) and Mayfare Smooth (42503001): no country of origin anywhere in page text or source (no Vietnam/Laos/Thailand). So made_in_stated_share stays NC: only MIE pages state origin; a range-wide share was not counted.

**Not changed:** status partial (b_corp, gots, lookbook, tech share still NC). craft_reasoning still says product pages could not be read; the PDP read adds the C. F. Stead tannery name but does not move the proposed 3.


## Dunhill


**Status: partial.** The census is complete, but composition was read on a sample of 44 of 206 styles (21%). Brand-level fibre percentages and shape are `NC`.

Method: WebFetch only, one fetch at a time, about 105 fetches, no 429s. curl to dunhill.com was denied by the proxy (CONNECT 403) and was not worked around. Doors come from the main thread's browser read; `doors_dunhill.csv` was not touched.

### Checked
- **Store.** https://www.dunhill.com/en-us runs on Salesforce Commerce Cloud (Sites-DunhillRNA-Site).
  - Prices are USD ("Ship To: US | USD").
  - Orders ship from France via Global-e. The shipping page does not say whether duties are included, so currency is filed as `USD`, not `USD_landed`.
  - Search is a text-only control, so `search_url` is `NC`.
- **Census.**
  - WebFetch cuts listing pages off at about 22 tiles, so pages were read with `?start=N&sz=22`.
  - Ready-to-Wear: 261 tiles. The Product Type facet sums to exactly 261.
  - Tailoring: 86 tiles, of which 12 are not in Ready-to-Wear (blazers, evening and suit trousers).
  - Total: 273 colourway tiles, which collapse to **206 styles** by product-code stem (the code minus its 3-digit colour). Every tile code is unique.
  - Stem caveat: DU25RL426V8 carries both a "Supima" and an "Interlock" title.
  - Footwear: 35 tiles (14 loafers/slippers, 21 sneakers). Shoes are out of the fibre scope.
- **Fibre sample.** 44 product pages across every category.
  - 40 natural-led, 4 synthetic-led, 0 cellulosic; 4 with elastane.
  - The 4 synthetic-led styles: Lightweight Harrington (polyester), Technical Field Jacket (polyamide), swim shorts (polyester), and **"Sea Island Cotton 5 Pocket Jeans", which is 65% polyester** despite its name.
  - Other conflicts on the page:
    - The Lightweight Harrington's description says "technical cotton blend" but its composition says 100% polyester.
    - The Bourdon DB jacket's composition reads "100% Cashmere Wool", but its description says a wool and cashmere blend; lead fibre and % are recorded as uncertain.
    - The cotton-cashmere cardigan's parts sum to 101.
- **Made in.** Stated on all 44 clothing pages (34 Italy, 10 Portugal) and on both shoe pages (Italy).
- **Prices.** No markdowns were seen on any tile or product page. Every product page price matched its tile except one: the Athluxury Wool Long Sleeve T-Shirt shows $610 on tiles and $595.00 on both colour pages. It is not used as a price cell.
- **Basis judgements:**
  - Tee: range ($360 to $730). The top is a long-sleeve wool quarter-zip that the house files under T-shirts.
  - Polo: the high is a knitted long-sleeve cashmere polo from Knitwear.
  - Dress shirt: range, because there is no majority-silk shirt; the high is the evening shirt.
  - Jeans: denim 5-pockets only. There is no jeans category, so the listing link is the Trousers & Chinos parent.
  - Dress pants: the entry is already Super 150s wool, so the high is the dearest regular formal trouser.
  - Shoes: the high excludes the velvet evening slippers ($1,620–1,900).
  - Outerwear: a clean pair, the Harrington at $1,650 in polyester and at $2,120 in silk. The top of the category is $17,100 (Leather Double-Breasted Trench).
- **Doors.** `own_doors_us` = 1 (Hudson Yards), per `doors_summary_dunhill.txt`.
  - The locator also lists an outlet (Woodbury), a concession (Neiman Marcus Chicago) and a third-party dealer (Art Brown).
  - The Madison Ave flagship (December 2026) is noted as coming soon in `doors_basis` only.
  - `own_doors_world` is `NC`: the locator has no world list, and the Richemont FY26 report gives only a group total (1,393 boutiques).
- **Stockists.** One row: Art Brown New York, from the locator. It is a pen and luxury-goods dealer and likely fails register door one.
- **Owner.** Richemont. The FY26 Annual Report (published 22 May 2026) lists dunhill among the "Other operating segments". Note 39 (principal subsidiaries) was not reached.

### Craft: Walthamstow and Bourdon House, evidence vs claim
- **Bourdon House** (2 Davies St, built 1723). The brand site claims bespoke tailoring is "hand-cut" and "crafted by hand in Mayfair" by master tailors there. This is a brand claim with an address. No photo or filing was checked.
- **Walthamstow.** The brand site says only "our London leather workshop" and never names Walthamstow.
  - The Walthamstow workshop, "in operation since 1936" and making leather goods by hand, comes from The Week (updated 2 Aug 2016).
  - Wikipedia says dunhill "owns and operates a leather and smoking pipe workshop in Walthamstow".
  - It is plausible but not current evidence.
- **Neither covers the clothing range.** None of the 44 ready-to-wear pages names a maker or a mill. Mills are always unnamed ("a British mill", "century-old Italian mill", "a Scottish mill … 200 years", "clothmaker first established in 1722").
- **Proposed craft: 3.** Construction is documented and made-in is stated on every page, and the house owns bespoke and leather making. A 4 would need named or owned making on the ready-to-wear itself.

### Not reached / NC
- Composition on 162 styles.
- Vinted (vinted.com fetch errored).
- B Corp: the B Lab directory renders by JavaScript, and nothing suggests dunhill is certified.
- GOTS.
- World door count.
- The signature-product URL, a Rollagas lighter linked from the brand's lighter-history page, was not opened. The signature is a non-clothing product.

### Contradictions with facts_first / worklist
- The worklist's "NYC and Miami stores" is wrong again: there is no Miami door.
- The facts-first "SOFT COUNT" is resolved by the browser read: 4 locator entries, 1 own door.
- Facts-first top price of $17,100 confirmed.
- Tee entry of $360 confirmed.

### Brief issues
- Tech has no rubric; 1 is on the provisional scale. No named proprietary or licensed fabric was found, and "Athluxury" is a line, not a technology.
- `read_date` is filed as 2026-10-08 per the spec, but pages were actually read on 2026-10-10.


## Gant


**Status: partial.** About 65 web fetches and searches, run one at a time. No blocks met on gant.com. Yelp, newsroom.gant.com and Drapers were refused (robots or client error), so nothing was taken from them. curl to www.gant.com was refused by the egress proxy, so I could not pull a sitemap.

### Doors (the open question)
- **Whether Gant has US own doors today: I found no evidence of any.** No US door was evidenced, so `doors_gant.csv` is header only. The evidence:
  - gant.com has no locator. The browser read found `/store-locator` returns 404.
  - The US FAQ says "All orders are shipped from Europe". The site is operated by "Gant U.S.A Corp" (T&Cs) and orders are tracked through eShopWorld.
  - The last US doors I could find are all closed:
    - New Haven campus store: closed early 2021 (Daily Nutmeg, 8 Sep 2021).
    - 645 Fifth Ave: Yelp title says "CLOSED".
    - Livermore outlet: Yelp title says "CLOSED".
  - MF Brands' Gant page (modified 2025-02-26) has four regional blocks, with region labels inferred from their order:
    - World: 234 stores, 61 countries, 2,082 employees.
    - Europe: 160 stores. Asia/APAC: 74 stores. 160 + 74 = 234.
    - Africa/ME: "79 sales outlets", which matches the partner-run doors WWD describes.
    - North America and Latin America: "1 country" each and no stores.
- **`own_doors_us` = 0 and `own_doors_world` = 234 need a ruling.**
  - Both rest on that inferred mapping.
  - 234 does not say how many are own, franchise or outlet.
  - The same MF Brands page also says "network of 750 stores", and career.gant.com says "more than 600 stores across 80 markets".
  - If the inference is not accepted, both should go to NC.
- No stockists are listed. gant.co.uk's locator (203 doors) covers UK/EU own doors, outlets, pop-ups and concessions only.

### Ownership and origin
- **Owner:** MF Brands Group, which is private and Swiss. It is Maus Frères International renamed in March 2020 (FashionUnited DE), so Maus Frères SA remains the ultimate owner, as the brief said. Maus Frères took Gant private in 2008.
- **CEO:** Fredrik Malm since 1 Dec 2025, replacing Patrik Söderström (FashionUnited, 5 Dec 2025).
- **Founding — verified on the brand's heritage page:** 1949, New Haven, "together with his sons Marty and Elliot, founded Gant of New Haven". The founder is Bernard Gantmacher.
- **Earlier company:** Daily Nutmeg puts Gantmacher's earlier Par-Ex shirt company in New Haven from 1927. Its arrival year for him is 1914; Wikipedia says 1907. I did not resolve this.
- **Heritage claims, evidence vs claim:**
  - Yale Co-op as an early stockist and the Ivy League link: brand claim. Daily Nutmeg corroborates the Co-op best-seller story.
  - Locker loop, box pleat, Esquire 1963 and Elliot Gant's patent: brand claims I did not verify.
  - Former owned New Haven factories (130 Haven St, 1955; 40 Sargent Dr, 1966): evidence, from Daily Nutmeg.

### What was not reached
- **Fibre and composition:** on every PDP, the "Product details & materials" accordion is empty in fetched HTML. I tried gant.com, gant.co.uk and the SFCC Product-Show route.
  - All fibre cells are NC, and so are `made_in_stated_share` and GOTS.
  - `styles_gant.csv` holds 174 style stems from the first 48 tiles of seven category grids, with composition NC except one (Lambswool Crew, "100% superfine Italian lambswool" in its description). Sixteen PDPs were read; their description fibre words are in `note`.
  - A browser read of the accordion would close this.
- **Pagination:** grids serve 48 tiles. `?page=2` re-serves a reshuffled page one, and `start`/`sz` paging is robots-disallowed and refused by fetch. So every price low and high is from the first 48 tiles. Jeans (27) is the exception and was read in full.
- `search_url` is NC because `/search` is robots-disallowed. Swim is NC because there is no swim category in the current navigation.

### Other flags
- **Shoes:** `NONE` refers to the US store only. gant.com has no shoe category, but Gant sells footwear in Europe and took its footwear licence back in-house (Modaes).
- **Outerwear high:** it is a shearling peacoat at $3,135. The dearest non-shearling coat is $1,965.
- **Gant x Yale:** a collaboration, and excluded from every high.
- **Quote:** house voice from the heritage page. An alternative is CEO Söderström in WWD (undated in the fetch): "We started with how we wanted to become the future of American sportswear."
- **Tech:** the scale is provisional because no tech rubric was issued. "Active Recover" is a house-named stretch-denim line with no licensor named. DWR is generic.
- **Vinted:** brand id 6075 comes from the vinted.fr brand URL. The vinted.com page did not fetch, so the id is not verified on Vinted US.
- **Earlier record:** `facts_first` had tee $65 and outerwear high $3,135, and both were reproduced. `doors_summary_gant.txt` (browser read) was left as is.

### Browser read 2026-10-10
- **How it was read.** gant.com (US) was opened in a real Chrome tab, one PDP at a time, about 3 seconds apart. No login, cart, terms or CAPTCHA, and no bot check was met. A "Market confirmation" dialog appeared once; I chose "Continue to United States".
  - In the browser, the "Product details & materials" section is in the rendered DOM: Item No., care, then `Material`.
  - I opened the drawer on the Regular Shield T-Shirt to check it, and it shows the same text.
  - The JSON-LD `material` matched the drawer on the pages I compared (T-shirt, Down Parka).
  - This differs from the earlier fetch read, where the section came back empty.
- **What was read.** 82 of the 174 style codes in `styles_gant.csv`, spread across categories roughly in proportion:
  - knitwear 19, outerwear 18, shirts 14, tees-polos 11, trousers 7, tailoring 6, denim 5, sweats 2.
  - The file has no shorts or underwear-swim rows, so none were read.
  - Every one of the 82 states a composition (no ND).
  - The other 92 codes stay NC. 87311 Lambswool Crew keeps its earlier description-sourced composition.
- **What changed in `full_gant.csv` (old → new).** These are computed over the 82-code sample, not the range. `styles_total` is left NC.

  | field | old | new |
  |---|---|---|
  | styles_with_composition | NC | 82 |
  | natural_pct | NC | 85 |
  | synthetic_pct | NC | 11 |
  | cellulosic_pct | NC | 4 |
  | spandex_styles | NC | 11 (none at 5% or more; highest is 4%) |
  | made_in_stated_share | NC | 0 |

  - The `note` cell's FIBRE clause was rewritten to say this is a sample.
  - Lead fibre is read on the shell/main line. Same-fibre parts are summed: "31% Recycled Wool, 29% Lambswool" = wool 60, and "50% Cotton, 47% Organic Cotton" = cotton 97.
  - Ties go to the first-listed fibre: alpaca 38 / wool 38 = alpaca.
- **Made in.** No PDP of the 82 states a country. The page template carries an i18n slot "Manufacturing: {country}", and it was unfilled on all 82, so made_in_stated_share = 0.
- **Where synthetic leads.** Synthetic leads on 9 of the 82 read. Outerwear accounts for 7 of 18 read:
  - polyamide down jackets/parka
  - Active Cloud
  - Double Coat
  - three "wool"/"flannel"-titled jackets
  - The others are one tailoring (Suit Pants, 56% polyester) and one trousers style (Tapered Wool Flannel Pants).
- **Where cellulosic leads.** Three styles:
  - the Henley and the Wool Blend T-Shirt, both 70% lyocell / 30% wool
  - the Herringbone Overshirt, 50% viscose
- **Knitwear** is all natural-led, but 9 of 19 carry polyamide: up to 40% (Alpaca Wool Blend Jacquard Zip Cardigan), and 34% on the Striped Alpaca polo.
- **Title vs composition contradictions:**
  - **Wool Blend T-Shirt** (2003472): 70% Lyocell, 30% Wool. Wool is the minority fibre.
  - **Wool Blend Double Decker Jacket** (7006689): shell 70% Polyester, 30% Wool.
  - **Tapered Wool Flannel Pants** (1505421): shell 55% Polyester, 43% Wool, 2% Elastane.
  - **Flannel Down Mid Jacket** (7006686): shell 65% Recycled Polyester, 35% Viscose, no wool or cotton.
  - **Hybrid Insulated Flannel Jacket** (7006647): shell 60% Recycled Polyester, 40% Wool.
  - **Suit Pants** (1505389, no fibre in the title, sold as suiting): 56% Polyester, 42% Wool.
  - **Herringbone Overshirt** (3263054, in Shirts): 50% Viscose, 30% Wool, 8% Polyester, 8% Polyamide, 4% "Other Fibers".
  - **Striped Alpaca Wool Blend Polo Sweater** (8060116): 43% Lambswool, 34% Polyamide, 23% Alpaca. Alpaca is third.
  - **Selvedge Jeans** (1000050): shell 67% Cotton, 22% Viscose, 11% Polyester. This is not a pure-cotton selvedge. The page's badge says "made with a majority of organic cotton", but the composition line says plain "Cotton".
  - **Cashmere Suit Pants** (1505437): shell 100% Cashmere. This resolves the earlier "cashmere share not stated" flag in the price note.
  - **Cotton Cashmere Shirt** (3262024): 85% Cotton, 15% Cashmere. This resolves the earlier flag.
  - **Striped Mohair Blend Crew Neck** (8060111): 87% Mohair. This resolves the "mohair blend share unstated" flag.
- **Incidental.** Striped Flannel Mélange Shirt (3263017) states "GOTS – Organic, Certified by Control Union, GOTS-17639". `gots_certified` was not changed, because it was out of this task's scope; it is flagged for a ruling.
- **Desert Jeans** writes "Spandex" (4%) and is counted as elastane. "Other Fibers" (Herringbone Overshirt 4%, Harrington lining) is mapped to `other`.


## Issey Miyake


**Status: partial.** `reconcile.py`: 1 exact match, 0 rewrites, 0 unmatched. About 107 fetches, all one at a time except for one accidental parallel pair early on. There were no 429s. Fetch errors near the end on two US category pages (`/collections/m-shirts`, `/collections/men`) stopped the listing-URL work.

### Biggest finding: facts-first was wrong about the US store

- **A US e-store exists.** us.isseymiyake.com describes itself as "The official website and online store of ISSEY MIYAKE U.S.A." It is Shopify and shows prices like "$585.00 USD". The `/en/` site and its Japanese-only store do not link to it; its "change region/country" link is `#`. I found it through uk.isseymiyake.com in a search result. There are also eu. and uk. storefronts.
- **What I filed.** `store_used` = us.isseymiyake.com and `currency` = USD. All prices are exact whole dollars, so no rounding was needed.
- **No compare-at prices** appeared on any of the 321 US tiles or the 5 US product pages read.
- **The Japanese store was read too.** I read it in full first (JPY, tax included), before finding the US store. It is used only for composition and made-in evidence.

### Men's scope

- **Lines counted.** Men's = HOMME PLISSÉ ISSEY MIYAKE plus IM MEN, read from each line's own collection. No other line is counted.
  - US HOMME PLISSÉ: 222 items over 5 pages, all read.
  - US IM MEN: 99 items over 3 pages, all read.
- **Accessories excluded.** These are items whose code type starts with `a`: ties, bags, socks, stoles, hats, belts and shoes. One reason to use the code rather than the category: the JP alt-category files several bags and hats under メンズ_ニット.
- **Result: 271 men's clothing styles.** 188 HOMME PLISSÉ and 83 IM MEN.
- **One row per style code.** Colourways sit inside each product, so `colourway_ratio` is 271/271.
- **Older seasons included.** Both the US and JP lists still carry earlier seasons in stock. The US codes show hp68/hp66/hp58/hp57/hp46 alongside `basics-*` handles.
- **JP sizes for comparison.** The JP store has 353 HOMME PLISSÉ items (302 clothing) and 162 IM MEN items (137 clothing).

### Categories

The style code's type letters decide the category. I checked this against the JP image alt-categories on all 515 JP tiles and on the product pages read:

- `jj`/`fj`/`jm` → shirts
- `jk` → tops (tees-polos)
- `k*` → knitwear
- `jd`/`fd` → jackets, filed as tailoring
- `jc`/`fc`/`fu` → blousons, filed as outerwear
- `ja`/`fa` → coats, filed as outerwear
- `jf`/`ff` → trousers
- `jg` → skirts
- `ji`/`fi` → jumpsuits
- `je`/`fe` and `jl` → vests and pleated cardigans, filed as `other`

Two judgement calls:
- **d → tailoring vs c → outerwear** is my inference from the product pages read. KERSEY PLEATS fd170 is a tailored jacket; MONTHLY COLORS jc021 is a hooded blouson.
- **Men's skirts exist** (house label メンズ_スカート).

### Composition: 22 of 271 (8%)

- **Where it came from.**
  - 17 from JP product pages of the same style number and title (JP season 63↔US 68, 61↔66).
  - 5 from US product pages: basics-polo, basics-t-shirt, hp46-jk310, basics-jacket, hp66-kn281.
- **JP pages read but not in the US range.** I read 32 JP men's product pages; 13 of them are not in the US range and are not counted:
  - COMPLEAT TROUSERS: PES100
  - PRESS SHIRT: PES71/rayon29
  - KERSEY PLEATS jacket: PES100
  - BRUSH CLOSE-UP vest: cotton52/PES25/linen23
  - RUSTIC KNIT: nylon63/cotton37
  - COMPACT SHIRT LA63FJ054: PES100
  - CURVINESS SHIRT: cotton100
  - FLAT DYE T: PES100
  - PL RAMIE SHIRT: PES65/ramie35
  - RUSTIC MESH skirt: PES100
  - FLOATING LINEN: linen55/acetate45
  - 60/2 JERSEY: cotton70/PLA30
  - BRUSHSTROKE STRIPE: PES100
- **What the sample shows.** HOMME PLISSÉ pleated jersey reads 100% polyester throughout. IM MEN is mixed: wool, cotton and polyester. One elastane: la68-ff032 CLAY, where ポリウレタン 6% on a Japanese label is read as elastane.
- **Shares.** `natural_pct` (3) and `synthetic_pct` (5) are of all 271 styles, per the rules, so they are low.
- **Cells left `NC`:** `shape`, `natural_categories` and `synthetic_categories`. The sample is too thin to read them off a category table. A product-page or feed pass is needed. Feed note: `/products.json` is reachable by WebFetch but truncates after about 13 products. Curl to isseymiyake.com was refused by egress policy (403 CONNECT), and I did not work around it.

### Prices (USD, us.isseymiyake.com)

| Garment | Low | High | Basis |
|---|---|---|---|
| Tee | RELEASE-T BASIC, $230 | BASICS high-neck long-sleeve T, $355 | range |
| Polo | BASICS polo, $330 (the only one) | same | single |
| Dress shirt | COMPACT SHIRT, IM MEN, $445 | EMBROIDERY PRESS SHIRT, HP, $1,195 | range |
| Jeans | NONE | NONE | NONE |
| Dress pants | TAILORED PLEATS 3, $395 | ELEMENTS, IM MEN, $1,675 | range |
| Sweater | BRUSH CLOSE-UP KNIT crew, $415 | RISOTTO KNIT crew, 100% cotton, $750 | range |
| Outerwear | MONTHLY COLORS : FEBRUARY blouson, $575 | ELEMENTS blouson, $3,250 | range |
| Shoes | CIOCCOLATO, $650 | FLIPPER, IM MEN, $835 | range |

- **Dress shirt:** the high is a pressed pleat shirt, not a classic collar.
- **Jeans:** NONE, because there is no denim category and no denim title among 271 US or 439 JP men's titles. Please flag this for a human read.
- **Sweater:** no elevated fibre exists in men's knits.
- **Shoes:** no loafer is sold. ELEMENTS SHOES (¥88,000) is JP only.
- **Not filed:**
  - **Garment listing URLs:** all `NC`. US category handles errored; the JP `m-*` handles exist but mix all lines and were not checked live.
  - **`search_url`:** `NC`, not tested.

### Doors

- **The locator is script-rendered.** Its results panel reads "0 store". Its FLAGSHIP STORES list gives 29 names with no addresses and no ownership labels. The store detail pages also render empty.
- **US doors: 3.** All are recorded with `banner_stated`:
  - **ISSEY MIYAKE / NEW YORK:** 45 Madison Avenue, NY 10010. The brand news page says it opened 2026-05-08 and reuses glass from the "recently closed Tribeca flagship".
  - **PLEATS PLEASE / NEW YORK:** 14 Kenmare St, from press.
  - **BAO BAO / NEW YORK:** 126 Prince St, from press.
- **`own_doors_us` = 1 (45 Madison), a soft count.** Press (fuckingyoung.es) says the flagship "gathers all Issey Miyake lines under one roof". The brand itself does not state that HOMME PLISSÉ or IM MEN are stocked there. Pleats Please is women's and Bao Bao is bags, so neither is counted.
- **The other 26 flagships** are listed by name only. That is 100% of what the locator lists.
- **`own_doors_world` = `NC`.** Men's carriage at those doors is not established. Three of them are men's banners in Tokyo: IM MEN Aoyama, HOMME PLISSÉ Aoyama and HOMME PLISSÉ Daikanyama.
- **Recorded as `own-door`, unconfirmed.** The NY doors are probably run by ISSEY MIYAKE U.S.A. CORP., a group company named in the mynavi profile, but ownership is not stated on the locator.
- **Stockists: header only.** The locator's non-flagship results could not be read, so this does **not** assert that none exist.

### Tech, craft and ownership

- **Tech.** The tech scale is provisional; no rubric was issued. I propose `proposed_tech` = 4, an owned process on a large share.
  - The brand says HOMME PLISSÉ "is founded on the technology of garment pleating" (us.isseymiyake.com/pages/hommeplisse). The JP page calls 製品プリーツ one of the house's representative techniques.
  - `tech_share` = `NC`. No product page states garment pleating for its own style; HOMME PLISSÉ pages say only "プリーツ素材" and link to pleat care. The HOMME PLISSÉ line is 188/271 = 69%, which is an upper bound.
  - A-POC / A-POC ABLE is a separate line, not on the men's lines read, so it is not counted.
- **Craft: proposed 3.**
  - **Evidence:** a documented, house-developed process, "first sewn and then pleated to finish" (UK Pleats Please page; the year 1988 is given for the pleats work). Every JP product page states the country of making (32/32).
  - **Made in:** the HOMME PLISSÉ pleated polyester pieces sampled are made in the Philippines (フィリピン製). Knits, cotton tees and all IM MEN pieces sampled are made in Japan; the CIOCCOLATO shoe is made in China. US product pages state no country (0/5).
  - **What is missing:** no owned factory (the company profile lists only the Tokyo head office), no named maker and no named mill.
- **Owner.** The mynavi recruiting profile of (株)イッセイミヤケ (Issey Miyake Inc., founded 1971-11-02, 899 staff) names 三宅デザイン事務所 (Miyake Design Studio, founded 1970 by Issey Miyake) as the parent. Both are private, so there are no filings.

### Other sections

- **Lookbook:** "IM MEN COLLECTIONS AUTUMN WINTER 2026/27" (us.isseymiyake.com/blogs/immen-aw26).
- **Quote:** the house's own line, not a founder line. A searched founder quote ("Design is not for philosophy…") had only aggregator sources and was rejected.
- **Grailed:** /designers/issey-miyake exists, titled "Issey Miyake Clothing for Men".
- **Not reached (`NC`):** Vinted ID, the B Corp directory and GOTS. A web search found no B Corp listing; that is not a directory read.

### For the brief

The worklist's "Tribeca store and others" is outdated: Tribeca is closed and there are no US doors outside NYC. The facts-first "no US e-store" was wrong. Future passes on this house should start at us.isseymiyake.com.

### Browser read 2026-10-10

Read in Chrome on us.isseymiyake.com (host checked on every page). There was no bot check. Cookies and newsletter were dismissed and nothing was submitted.

**Men's listing links (old → new)**
- tee: NC → https://us.isseymiyake.com/collections/men-all-tops. This is the parent "MEN / ALL TOPS"; the house has no tee node.
- polo: NC → https://us.isseymiyake.com/collections/men-all-tops. Same parent, since there is no polo node.
- dress shirt: NC → https://us.isseymiyake.com/collections/men-shirts
- dress pants: NC → https://us.isseymiyake.com/collections/men-pants
- sweater: NC → https://us.isseymiyake.com/collections/mens-knitwear
- outerwear: NC → https://us.isseymiyake.com/collections/men-jackets-coats
- shoes: NC → a filtered listing, `/collections/socks-shoes?filter.p.m.custom.gender=…122740080734&filter.p.m.custom.product_type_filter=…136100085854` (Gender: Men + Type: Shoes).
  - The house has no men's shoe category. "Socks & Shoes" mixes Pleats Please and me ISSEY MIYAKE (women's) with socks.
  - The filtered page shows 2 tiles: ISSEY MIYAKE FOOT HYPER TAPING and HOMME PLISSÉ CIOCCOLATO.
- jeans: stays NONE.
- **Tiles check.** The grid has 4 columns. Rows 1–2 of each category are IM MEN and HOMME PLISSÉ, except in two places:
  - Tops row 2 holds A-POC ABLE items (at68-fo215, at68-kn463).
  - Knitwear row 2 holds A-POC ABLE items (at58-*).
  - A-POC ABLE is a unisex line. Applying the house's own Gender: Men filter leaves the first two rows unchanged, so these items are tagged men's by the house. They were accepted on that basis.
  - The men's category collections also carry other items tagged Women or Unisex further down. The filter counts on men-all-tops are Men 91 / Women 19 / Unisex 11, and the tags overlap.
  - The earlier "fetch errors" were wrong handles (m-shirts, men). The real handles come from the ONLINE STORE menu.

**Compositions: 22 → 92 of 271**
- 70 US product pages were read, from a quota sample:
  - trousers 18, tees-polos 12, shirts 12, outerwear 8, tailoring 8, knitwear 6, other 4, jumpsuits 2
  - IM MEN 33, HOMME PLISSÉ 37
- The composition sits in the "Product Information" accordion as "Material: … Made In …". It is in the DOM but not in the visible text until the accordion opens.
- None of the 70 was ND.
- "Polyurethane" on the main line (3–6%) is read as elastane, following the earlier ポリウレタン ruling.
- "Composite Fiber (Polyester)" is read as polyester.
- One style is cellulosic-led: la68-fj177, 100% Triacetate.

**Made in**
- 68 of 70 US product pages state a country: 46 Japan, 22 Philippines. The Philippines pages are all HOMME PLISSÉ pleated polyester or cotton.
- The 2 BASICS styles (basics-pants-3, basics-vest) state none.
- This corrects "US PDPs state none (0/5)". `made_in_stated_share` (100, from the JP read) is left unchanged.

**full_issey_miyake.csv (old → new)**
- styles_with_composition: 22 → 92
- natural_pct: 3 → 12
- synthetic_pct: 5 → 21
- cellulosic_pct: 0 → 0. Percentages are of all 271 styles; 66% have no composition.
- spandex_styles: 1 → 3 (la68-ff032, la68-ff034, la68-fj046)
- shape: NC → split
- synthetic_categories: NC → ["trousers","tees-polos","outerwear","tailoring"]
- natural_categories: NC → ["shirts","knitwear"]
- **Category leads among composed styles:**
  - trousers 14 synthetic / 5 natural
  - tees-polos 13 / 3
  - outerwear 7 / 6
  - tailoring 6 / 4
  - shirts 8 natural / 6 synthetic / 1 cellulosic
  - knitwear 6 natural / 5 synthetic
  - other 5 synthetic (n<10)
  - jumpsuits 2 / 1 (n<10)
- Category keys are the standard set. The house menu (Pants, All Tops, Shirts, Knitwear, Jackets & Coats) does not separate tailoring from outerwear.
- **Caveat.** The shape comes from a quota sample, not a census. Outerwear, shirts and knitwear are each decided by one or two styles. The line split is the robust reading:
  - IM MEN is mixed (wool, cotton and polyester).
  - HOMME PLISSÉ pleated pieces are polyester, while its knits and some shirts are cotton blends.
- status stays partial (34% coverage).


## Johnston & Murphy


**Pacing and blocks**
- About 90 WebFetch/WebSearch calls, made one at a time. No 429s and no bot checks.
- curl from Bash was refused by the egress proxy (CONNECT 403 for www.johnstonmurphy.com), so the sitemap could not be pulled that way. That route was not used again.
- WebFetch cuts every page off at about 70–100k characters. In practice:
  - A category grid gives only about 12 colour tiles per fetch, which is often only 1–4 distinct styles.
  - sitemap_0.xml gave only its first ~137 product URLs. These are id-ordered and mostly shoe care, belts and shoes.
  - `sz=` is ignored. `start=` works, but the tile order shifts between fetches.
- Sorting did not work, as the brief said. Neither did a census.
- Robots refusals by WebFetch:
  - /c/men/mens-clothing
  - /c/men/mens-apparel/mens-polos-tees/mens-tees (a guessed slug)
- The doors file is **untouched** (main thread's browser read). The locator was not opened.

**Contradiction with facts_first: the dress-shoe category is readable.** /c/men/mens-shoes/mens-dressclassics was read on 2026-10-10. It states 119 products, and its first ~15 were seen (Tyson, Melton, Ashton, Sullivan, Conard 2.0, Gavney and others). The robots block recorded on 2026-10-08 did not recur through WebFetch.

**How much was read, in grid order**

| Grid | Tiles stated | Pages read | Distinct styles recorded |
|---|---|---|---|
| Apparel parent | 581 | page 1 | — |
| Polos & Tees | 122 | starts 0, 12, 72, 84, 108 (start=0 with sz=60 returned only the first ~12 tiles) | 15 |
| Shirts | 110 | starts 0, 12, 24, 60, 84 | 12 |
| Sweaters & Knits | 101 | page 1 | — |
| Coats, Jackets & Vests | 64 | starts 0, 12, 24 | 13 |
| Pants & Jeans | 38 | starts 0, 12, 24 | 7 (about 36 of the 38 tiles accounted for, so close to complete) |
| Blazers | 41 | page 1 | 6 |
| Slip-Ons & Loafers | 128 | page 1 | — |
| Dress Shoes | 119 | page 1 | — |

- Site searches were also read: sweater, pullover, crew, crewneck (0 results), cashmere (0), trousers (0), tee, dress shirt, loafer, penny loafer, arrister, J&M Collection.
- Shorts and Golf apparel were not read.
- **Styles file:** 71 men's clothing styles.
  - 24 product pages were read for composition.
  - 47 rows are listing tiles only, with composition NC.
  - 14230 has URL NC: the grid gave only its id, so the URL was not guessed.
- **Brand fibre aggregates are NC.** This is not a census.

**Fibre (sample of 24 product pages)**
- J&M publishes fibre names with **no percentages**, for example "Cotton/poly/rayon." Lead fibre is therefore taken as the first one listed. That is an assumption, and every row says so. lead_pct is ND except on single-fibre lines.
- By lead fibre: 11 natural, 9 synthetic, 3 cellulosic, 1 undisclosed (Upton Car Coat: "various fabric blends that combine poly, wool, rayon, and other fibers").
- 12 of the 24 carry spandex/Lycra, with no share published.
- Only three are 100% one fibre: Ovation and Huntley shirts (cotton) and Townsend blazer (wool shell).
- The sample leans split: XC+/XC Flex performance pieces are synthetic, and cotton shirts and chinos are natural-led. This is not filed as `shape` because it is not a census.

**Garments.** All eight were read, each with its product and URL. The figures are from a sample because the grids cannot be fully read; the exact prices are in the full row's note.
- Every one of the 7 pant styles is $129.50. There is no dress trouser, so chinos are used.
- Only one crewneck was found: Weaver Crew Pullover, $109.50, viscose/poly/nylon. No cashmere is on the site.
- Highs exclude the Licensed Collegiate Collection and Game Day prints, as capsules.
- Shoe low is Aragon II Kiltie Tassel Loafer at $119.90. It carries a "Special Value" label on the grid, but its own page shows no compare-at price. **Ruling wanted:** if Special Value counts as an outlet-type tier, the low becomes $155–159 (Humphrey or Cort 2.0 / Upton Perfed Venetian).
- Floyd Penny Loafer ($185) sits under a /sale-mens-shoes/ path and was not used.
- The J&M Collection sub-line has no loafer in what was read. Arrister Double-Monk ($298) is a monk strap.

**Craft (proposed 2)**
- Genesco FY2026 10-K: "We rely on independent third-party manufacturers for production of our footwear products". Sourcing countries listed: Bangladesh, Brazil, Cambodia, China, India, Italy, Pakistan, Peru, Portugal, Sri Lanka, Turkey, Vietnam.
- No owned J&M factory is named.
- All 24 apparel pages say "Imported", with no country.
- Shoes:
  - Arrister Cap Toe (J&M Collection): "Crafted in Portugal for Johnston & Murphy Collection", with "Italian calfskin". No tannery is named.
  - Aragon II and Tyson: no origin stated.
- The heritage page's handmade Goodyear welt (1881) is history, not current process.

**Origin (verified on the brand's heritage page)**
- William J. Dudley came from Northampton, England to Newark, NJ and started the William J. Dudley Shoe Company.
- "heritage dating back to 1850". Fillmore's shoes are dated 1850 on /presidents.html.
- Later, James Johnston and partner William A. Murphy gave the company its name.
- General Shoe (Genesco) acquired it in 1951. It moved to Nashville in 1957.
- No date for the name change was read.

**Doors**
- own_doors_us is 89, per the summary file (62 shops + 27 airport). 66 factory stores = 155 on the locator.
- The 10-K FY2026 gives 153 "retail shops and factory stores in the United States". The 2-door gap is not reconciled.
- own_doors_world is NC: the locator also offers Canada, which was not read.

**Stockists.** Two summary rows (department store, independent) for the 1,496 listings on the SELECT DEPARTMENT & SPECIALTY tab. **The split by shop_kind was not counted.** The browser read gave only the total, so the per-kind counts are NC.

**Tech.** Named on product: XC+™, XC4®, XC Flex® (J&M's own marks), TRUFOAM® (Tyson midsole) and TENCEL®/LYCRA® fibre brands (Washed Chinos). The XC lines are owned and the fibre brands licensed, hence `both`. 20 of the 71 styles read carry an XC name (28%; the sample is weighted to page 1). proposed_tech is 2 on the PROVISIONAL scale; no tech rubric was issued.

**Other fields**
- Lookbook: "Men's 2026 Fall Catalog" (/catalog.html, a Flipsnack flipbook).
- Grailed: /designers/johnston-murphy exists.
- Vinted: /brand/johnston-murphy fell back to a generic catalog page and no brand id was found, so NC.
- B Corp: the directory search errored and a web search found no listing, so NC (likely no).
- GOTS: NC.
- Quote: the heritage page's meta description, in the house's own voice. It was read through the WebFetch extractor; check it verbatim.
- Signature product: NC. No brand page names one.

**Brief notes**
- The brief's "155 vs 153" is confirmed.
- The brief's "dress shoe robots-blocked" did not hold on 2026-10-10.


## L.L.Bean


**Status: partial.** About 110 fetches and searches, run one at a time with no parallel calls. llbean.com served every page I asked for, with no 429s and no blocks. I pulled no feed or sitemap.

### Prices (llbean.com, USD)
- **Tee: $27–$55, range.** Low is the Carefree Unshrinkable Tee at $26.95. The $19.99 on the grid is a sale colour (Light Gold). High is the Insect Shield Field Tee LS, compare-at $54.95. Other tees carry the same $49.95–$54.95 compare-at, which backs it up. I counted only items the house calls "Tee". Henleys, waffle crews and hoodies in the same grid are excluded. The 49th tile was not loaded.
- **Polo: $40–$65, range.** Low is the Carefree Unshrinkable Polo SS at $39.95. High is the Comfort Stretch Performance Pima Polo SS, compare-at $64.95; two products show the same figure. Pima does not count as an elevated fibre, so the basis is range, not pair.
- **Dress shirt: $65–$89, range.** Read from the Dress Shirts category (28 items). Low is the Wrinkle-Free Classic Oxford at $64.95. High is the Signature Premium Pima Oxford, compare-at $89. A short-sleeve Kennebunk sport shirt at $59.95 is cheaper but was not taken as a dress shirt.
- **Jeans: $70–$120, range.** Double L Classic Fit at $69.95 to Signature Heritage Denim at $120. Lined jeans are excluded from the high.
- **Dress pants: $70–$100, range.** There is no dress trouser, so these are chinos: Wrinkle-Free Double L Chino at $69.95 to VentureTek Chino at $99.95. 15 of the 62 pants were behind "load more" and not seen.
- **Sweater: $60–$250, pair.** All Seasons Cotton Blend crew at $59.95 to Signature Cashmere Sweater at $250. The PDP confirms the cashmere sweater is a crewneck and 100% cashmere.
- **Outerwear: $70–$450, range.** Mountain Classic Anorak, compare-at $69.95 (PDP read), to Maine Warden's 3-in-1 Parka with GORE-TEX at $450. Only the first 45 of 259 tiles were seen, and the 259 includes 94 accessories. A sort URL I guessed was ignored by the site. **The high is unverified across the full list.**
- **Shoes: $100, single.** This is the "choose per rules" call the brief asked for. L.L.Bean does sell a loafer: the Casco Bay Venetians at $99.95. The page calls it a handsewn Venetian with "traditional moccasin design", and the image alt text says "Venetian loafer". It is the only loafer in the 47 of 52 tiles I saw in Sneakers & Shoes, so the basis is single.
  - The Handsewn Moccasins (Camp Moc II and Blucher Moc II at $110) and the Allagash Handsewn Mocs ($150–$170) are lace-up boat or camp mocs, so they are not loafers.
  - The Kennebec Slip-On (compare-at $130) does not call itself a loafer.
  - The Bean Boot 8" is $150.
  - Third-party shoes (HOKA, On, New Balance, Birkenstock, Blundstone and others) are excluded.
- **Listing links are all men's category pages.** Two are coarser than a garment page:
  - Outerwear: the parent men's outerwear page, which also carries caps and accessories.
  - Shoes: Sneakers & Shoes (506791), which mixes in third-party brands.
- `search_url` was not tested (NC).

### Fibre: 33 styles, not the ~100 the brief asked for
- **Why 33.** At one PDP per fetch, a ~100-style sample would not fit the 120-fetch cap alongside the doors pages.
- **What the sample covers:**
  - tees/polos: 7
  - shirts: 7, including the Hurricane shirt-jacket
  - knitwear: 6
  - denim: 3
  - trousers: 4
  - outerwear: 6
- **Census.** The men's nav shows 734 items, of which 194 are accessories. Outerwear is a separate 259, of which 94 are accessories and 9 snow pants. Categories overlap (Activewear 135), so `styles_total` is NC and the percentages are of the sample only.
- **Sample result:** 26 natural-led, 7 synthetic-led, 0 cellulosic-led; 5 styles have elastane on the main line.
- **Pattern in the sample (too small to set `shape`):** the heritage lines are all-natural, and synthetics concentrate in outerwear.
  - All-natural: Carefree Unshrinkable, Double L, Chamois, Scotch Plaid, Ragg Wool, Commando, Field Coat.
  - Synthetic: Mountain Classic, Warden's, Access.
- **Disclosure.** Every PDP read states a composition. Three state a named fibre with no percentage (Premium Double L Polo "all-cotton", Chamois "cotton flannel", Field Coat "cotton canvas"); these are filed at 100 as rules_fibre allows. The Mountain Classic Fleece gives only "at least 63% recycled polyester".
- Swimwear facet: 15 listings (not deduped, so `swim_styles` is NC).

### Doors
- **The brief's counts check out.** The store list re-read on 2026-10-10 matches facts_first: 62 open full-price stores (including the 3 Freeport campus stores) + 2 coming soon + 10 outlets + 1 clearance center = 75 US entries.
- **All 75 are in the doors file.** Outlets and the clearance center are `format=outlet`.
- **Addresses: 29 of 75.** I read the store pages for the Freeport campus, every outlet, the clearance center, both coming-soon stores, all of Massachusetts, Huntsville and Naperville. The other 46 rows have street, zip and phone as NC.
- **Flags:**
  - The Berlin MA store's address is in Hudson MA.
  - The Biddeford outlet and Berlin and Peabody stores carry "coming soon" image alt text but post hours; I took open from the list page.
  - The Freeport flagship page advertises a renovation "Grand Opening" running Sept 18–Oct 25, 2026.
  - The Colorado Springs page gives an opening of "Friday, October 30" and Ann Arbor "Friday, October 16", with no year on either.
- **World count is NC.** Japan and Canada were not read. The undated brand Company Information PDF gives 25 Japan stores and outlets and 3 Canada stores, but it also says 47 US retail stores, so it is stale.
- **Stockists: none.** The brand lists none, so the file has one `none` row.

### Craft (proposed 3; a case for 4)
- **Owned making exists, for boots and totes only.** Brunswick and Lewiston, ME: 400+ employees make the Maine Hunting Shoe/Bean Boot and the Boat and Tote. Sources: brand Company Information PDF (undated) and llbean.ca company info (2015 figures).
- **The boot page backs it up.** The Bean Boot 8" PDP says "Made in Maine" and handcrafted in Brunswick. Built to Last (2020) says stitchers train for 26 weeks on a triple-line stitch.
- **The clothing names nothing.** All 33 clothing PDPs say only "Imported". No maker or mill is named anywhere; at most a fabric country is given (Portugal flannel ×2, Italian peacoat wool).
- **Handsewn mocs and Venetians are imported.**

### Other sections
- **Tech: proposed 3 (provisional scale; no tech rubric was issued).**
  - Owned house names: Comfort Stretch (Performance), BeanFlex, SunSmart, ColdShield, VentureTek.
  - Licensed on a meaningful share: GORE-TEX, PrimaLoft, Thinsulate, DownTek, COOLMAX, SUPPLEX, REPREVE, TENCEL, LYCRA, Insect Shield.
  - 10 of the 33 sampled styles carry a named tech.
- **Ownership.** global.llbean.com "Who We Are" says "L.L.Bean is still family-owned to this day". llbean.ca says "privately held, family-owned", with no annual report. Shawn Gorman (great-grandson) is Executive Chairman per the company history page.
- **Quote.** The brand's own page (fr.llbean.ca company-info, English text, quoting President Steve Smith) has: "Sell good merchandise at a reasonable profit, treat customers like human beings and they'll always come back for more."
  - **The brief's wording "treat your customers" does not match the brand page;** I filed the brand's wording.
  - No llbean.com page carrying the Golden Rule was found. The company history, Who We Are and Built to Last pages do not have it.
  - Alternate quote (global.llbean.com, from L.L.'s *My Story*, 1961): "The one thing I learned throughout my lifetime is the fact that outdoor recreation…has added years to my life span."
- **Lookbook: none.** "Fall Collection" is a product grid; the only catalogue item is a request-a-catalog link.
- **Vinted:** brand id 82178, read from an item page.
- **Grailed:** /designers/l-l-bean exists.
- **B Corp and GOTS: NC.** The B Lab directory returned no results to read. The Organic Cotton Waffle Sweater PDP names no certification.
- **Founding date.** The founding year is 1912 per the brand PDF and llbean.ca. The company history timeline opens with 1911, "invents the Maine Hunting Shoe", while the Bean Boot PDP and Built to Last say 1912. This is a small inconsistency on the brand's own pages.


## Louis Vuitton


**Status: partial.** Prices are the lowest and highest among the pages read, not a full scan. Fibre is a documented sample of 76 styles. Doors are complete for the US.

Method: WebFetch and WebSearch only, about 115 fetches made one at a time, no 429s.
- curl to us.louisvuitton.com was denied by the proxy (CONNECT 403). It was not worked around.
- One guessed API URL (api.louisvuitton.com) errored. No other API was tried.
- `read_date` is 2026-10-10, the date the pages were actually read. `captured_on` in the doors file is 2026-10-08, as the spec requires.

### Checked
- **Store.** https://us.louisvuitton.com/eng-us/, prices in USD.
  - Listing pages (24 tiles a page, `?page=N`) show **no prices** to a fetcher. Prices come from product pages only.
  - Sort and price-filter controls have no hrefs, so no price-sorted listing could be read.
  - `search_url` is `NC`: not tested.
- **Census.** Colourway tiles per style facet on all-ready-to-wear:
  - Outerwear and Coats 138, T-Shirts and Polos 120 (category page), Pants 69, Shirts 66, Knitwear 60, Shorts 28, Blazers and Jackets 24, Sweatshirts and Hoodies 11, Swimwear 5. That is about 521 tiles.
  - Facets overlap: short-sleeved knit crewnecks sit under both Knitwear and T-shirts, and cargo shorts sit under Pants.
  - Colourways share an `nvprod` stem. Tiles were not deduplicated to styles, so `styles_total` and the brand percentages are `NC`.
  - The facet counters read through a summariser were unreliable on two pages (they read "1" and "11"). Knitwear (60) and Shirts (66) were counted from the last page. Outerwear 138 and Pants 69 are the counters' own figures.
- **Fibre sample.** 76 product pages across all ten categories, roughly in proportion to the facets: outerwear 19, tees and polos 15, knitwear 10, shirts 10, trousers 7, tailoring 5, denim 4, shorts 3, sweats 2, swim 1.
  - Every page states a composition.
  - **71 natural-led (93%), 5 synthetic-led, 0 cellulosic. 2 have elastane** (a cashmere hoodie at 1%, and a blouson at 3%).
  - The synthetic-led five: Monogram Quilted Liner Jacket and Light Padded Monogram Overshirt (both polyamide), the fleece blouson (polyester/acrylic), Silk Tech running shorts (72% nylon) and swim shorts.
  - Tees, knitwear, shirts, denim, trousers and tailoring were 100% natural-led in the sample. The sample looks like one cloth story with synthetics confined to a few padded or technical outerwear pieces. Not filed as `shape`, because it is a sample.
- **Made in.** Stated on 75 of 76 (71 Italy, 4 France). The Jacquard Pullover ($4,150) states none.
- **Lines.** "LV Trunk Edition", "LV Icons", "LV Fall" and "Spring-Summer 2027 Formal" appear as tile groups on the all-RTW page. Product pages name no line, so `lines` is `-` except for Silk Tech.

### Prices: basis and caveats (all among pages read)
| garment | low → high | basis and caveat |
|---|---|---|
| Tee | $1,010 → $1,770 | range; 15 tees read |
| Polo | $1,250 → $1,890 | range |
| Dress shirt | $1,070 → $2,290 | pair |
| Jeans | $1,260 → $2,400 | range |
| Dress pants | $1,450 → $1,900 | pair |
| Sweater | $1,640 → $1,900 | pair |
| Outerwear | $2,400 → $12,900 | range |
| Shoes | $1,490 → `NC` | one loafer read |

- **Tee:** the high is cotton. The cotton-cashmere tee is 85/15, so it is not elevated.
- **Polo:** the high is the Wool Silk Cashmere Long-Sleeved Polo Shirt (70/20/10), from the "LV Trunk Edition" tile group. Trunk Edition looks like a standing line, not a capsule; **Sebastian to rule**. The alternative high is the Stripy Cable-Knit Polo at $1,640.
- **Dress shirt:** cotton poplin, point collar → Mini Monogram Silk Evening Shirt (100% silk, point collar). The regular Monogram Silk Satin LS Shirt is $2,270, if evening shirts are excluded.
- **Jeans:** no majority-silk or majority-cashmere jean was read. Cotton Cashmere Jeans (47% cashmere) is $2,380.
- **Dress pants:** wool cigarette pant → 55/45 silk-cashmere tailored pant.
- **Sweater:** the cheapest crewneck read (80/20 wool/polyamide) → 100% cashmere crewneck. The wool-cashmere cable crews ($2,020–2,150) are dearer but only 20% cashmere.
- **Outerwear low:** the Embroidered Signature Zippered Blouson's **page contradicts itself**. The composition says 97% cotton / 3% elastane; the description says a wool-blend bouclé and mentions cargo and rear pockets. The price is as displayed. The next cheapest is the Washed Denim Zippered Blouson at $2,900.
- **Outerwear high:** the vicuña Harrington (77% cashmere / 23% vicuña), which counts as elevated per the brief. Excluded as highs:
  - mink pieces (Mink Vest, Mink Track Top);
  - suede and lamb leather: Monogram Embossed Suede Hoodie $6,200, Signature Suede Overshirt $4,900 and Suede Flight Jacket $6,450. Lamb leather is not an exotic skin, so these were excluded on garment type, not on the exotic-skin rule.
- **Shoes:** the loafer listing renders by script, so only the Major Loafer was read ($1,490, Blake construction, "Hand-stitched vamp (1 hour per pair)").
- The RTW price filter now spans **$695–$30,095**; facts-first had $28,595. The $695 item was not identified.

### Doors
- The locator lists 106 entries. 104 are retail after removing Le Café and Le Chocolat.
- **Facts-first's dedupe premise is mostly wrong.** The 9 men's-only stores each have their own suite or street address: Rodeo Dr 420 vs 295, Bellagio 1111A vs 1108A, and so on. They are separate physical doors.
- Only Saks Fifth Avenue NYC appears twice at one address (1st floor and Men's 7th floor, same phone). It was merged, giving **103 physical doors**.
- **`own_doors_us` = 102**: 85 own-door plus 17 LV boutiques inside department stores, filed `concession`. This follows the brief's "physical doors".
  - Under the spec's stricter reading (concessions apart), the figure is **85**.
- Las Vegas Palazzo is filed as `pop-up` because the brand's own URL slug ends "-pop-up". It is not counted.
- `own_doors_world` is `NC`. Non-US doors were not listed (0% of the world), and LVMH does not publish a per-maison store count in what was read.
- **Stockists:** the locator lists only LV stores, so the stockists file has one `none` row.

### Craft, tech, other
- **Craft: proposed 3.**
  - Evidence of owned making is for leather goods only:
    - LV's own site says the Asnières atelier opened in 1859 and has 170 craftsmen making leather goods.
    - An LVMH release says "24 workshops ... including 16 in France". The page is undated, probably around 2019, and covers leather goods.
  - Nothing ties owned or named making to the clothing. 0 makers and 0 mills are named on 76 RTW pages; "Japanese denim" and "finest Japanese mills" appear unnamed.
  - The brief's "owned ateliers (Asnières, etc.)" is true but does not cover RTW.
  - The shoe workshop (Fiesso d'Artico) was not checked.
- **Tech: provisional scale, no rubric was issued.** "Louis Vuitton Silk Tech" (72% reclaimed nylon / 28% silk) is a house-named fabric, seen on 1 of 76 styles, so proposed 2.
- **Founded:** the brand page gives no year. "Arrived in Paris 1837 ... stayed for 17 years before opening his own workshop" implies 1854, filed as arithmetic.
- **Owner:** LVMH. The 2025 interactive annual report was located, but its Louis Vuitton page was not reached (pages 25 and 173 do not mention LV), so it rests on the group name and the brief. Treat `ownership_url` as weak.
- **Quote:** house voice, from LV's own site. The alternative is Pietro Beccari on Pharrell: "His creative vision, which transcends fashion, will undoubtedly lead Louis Vuitton into a new and very exciting chapter." (FashionUnited, 14 Feb 2023).
- **Vinted:** brand id 417, verified on vinted.com (Men catalog, brand filter "Louis Vuitton").
- **Grailed:** verified.
- **Signature product:** Keepall Bandoulière 50, $3,850. It is not clothing.

### Not reached / NC
- Full price scan.
- Style dedupe and brand-level fibre percentages.
- Shoes high.
- World doors.
- Search URL.
- B Corp and GOTS: a web search found nothing, and the B Lab directory was not opened.
- The LV page of the LVMH 2025 annual report.


### Main thread 2026-10-10

own_doors_us 102 → 85: concessions counted apart, consistent with AllSaints (Bloomingdale's shop-in-shops) in batch 1. Sebastian to rule.


## Mackage


**Store and currency.** I read the www.mackage.com Shopify store with the US | EN | $USD selector active. USD is confirmed on two displayed prices: TEE-R shows $190.00 and MARTIN-Z shows $490.00 USD. On 7 outerwear styles the first-variant feed price in `/collections/men/products.json` equals the displayed price. I did not read `Shopify.currency.rate` (`feed_currency_rate` = NC). The site search was not tested (`search_url` = NC).

**Access.** curl to mackage.com failed at the proxy (CONNECT 403). I made no other attempt; all reads went through WebFetch, one at a time, 116 fetches in total. WebFetch truncates the Shopify feed after about 7 products, and composition is not in the feed's `body_html` (KOLTON and LEGEND checked). Composition was therefore read from 86 rendered product pages. Five pages returned fetch errors: CLYDE, ARCHIE, SKAI-PL and EVERETT-GC each failed once and were not retried (budget); the fifth was the about page. There were no 429s.

**Prices.** Full price only. The theme labels every price "Sale price", so I took a price as full when the page showed no compare-at. Three markdowns were seen and their compare-at used: GARRETT $690 → $414, GAGE $750 → $375, and one KRYSTIAN variant $370 → $277.50. TEE-R is $190 full price, which matches facts-first.
- **Outerwear high, corrected:** facts-first filed $3,890 CLYDE; the record now has $1,690 JUDAH-AL. Shearling is fur-on, so every style with shearling, sheepskin panels or fur trim is excluded from the high: CLYDE, DARWIN, MOSES, NIXON, CASH, ARCHIE, BEAR, MORITZ-X (fox and rabbit), OVI, CHANCE-NV and TORRIAN. TORRIAN's `.js` description reads "mixed media shearling jacket" even though its composition lists only leather and merino. KENNETH-PB and OTTO-PB (pebble leather, $1,690) tie with JUDAH-AL. All three are full price with no shearling mentioned.
- **Garments Mackage does not make:** no woven dress or casual shirt (its overshirts are double-face wool shirt-jackets), so dress shirt = NONE. No jeans = NONE. No crewneck sweater: LEGEND, a 53/47 cotton/polyester turtleneck at $450, is the only knit pullover, filed as `single`. No loafer: shoes are a `range` from LUKA-01 sneaker $495 to HERO-MS boot $790.
- **Listing links:** tees, polos, sweater and dress pants use the men's Ready-to-Wear parent page. I verified that page as all men's, 27 styles; Mackage has no finer tee or polo page. `mens-pants-shorts` and `mens-hoodies-sweaters` exist but I did not open them. I verified `mens-footwear`. I took `mens-outerwear` from the navigation without opening it.

**Band check.** Facts-first guessed true luxury, but full prices do not support it. The tee is $190, polos $210–270 and RTW $250–590. Non-shearling outerwear runs $590–1,690; shearling and leather go to $3,890. I propose **premium / upper-premium**, not true luxury. Sebastian rules.

**Fibre.** The men's collection has 145 handles across 3 pages: 119 clothing, 20 accessories and 6 footwear. I read 86 of the 119 (72%): every non-outerwear style (24) and 62 of 95 outerwear styles.
- Percentages are computed on the 86 read, not on 119: 59% natural-led, 41% synthetic-led, 0% cellulosic-led. 14 styles have elastane on the shell, 9 of them at 5% or more.
- Shape is **split**. Read outerwear is 33 synthetic-led and 29 natural-led. All read RTW is natural-led: cotton tees and polos, and cotton/poly double-face jersey sweats at 53/47.
- Style = handle. The fur-trim variants DIXON-F/-BX/-X and EDWARD-F/-X are separate handles; I did not read them and they are not collapsed.
- `colourway_ratio` is NC: card counts per page were inconsistent.
- `category_house` = derived. I could only confirm the house's product types on a few items.

**Lines** (named in titles or on product pages):
- **All-natural:** Double-Face Jersey (7), Brushed Knit (4) and Double-face wool (6).
- **All-synthetic:** Nordic Tech (4), Agile-360 (3) and High-Gloss (3).
- Lines under 5 styles are given for information only.

**Flags for a human read:**
- ALEC and MATHIAS are 3-in-1 Balmacaan coats, yet their pages state the shell as 70% polyester / 30% rayon. That is possibly the liner's composition.
- HENRIK is titled a suede shirt jacket, but its page lists only a recycled-nylon shell.

**Doors.** The locator (store-locator, read 2026-10-10) lists 19 stores and all are written to the doors file:
- **US, 6 stores:** 4 full-price (Boston Prudential, NYC Spring St, NYC Madison Ave, Short Hills) and 2 outlets (Desert Hills, Cabazon; Woodbury Common). This matches the brief.
- **World, 13 more:** Canada 9 (2 of them outlets), Paris 1, Roermond outlet 1, Beijing 1, Tokyo 1.
- **Outlet labels are mine:** the locator puts no outlet tag on any store. I filed 5 stores as outlets because their venue names are outlet centres.
- **Full-price counts:** 4 US and 14 worldwide.
- **Who runs them:** the locator does not say who operates a store. Beijing and Tokyo may be partner-run.

**Stockists.** No stockist page is linked from the site, and the locator lists only Mackage stores. A Stockist.co widget on the locator page did not render, so any wholesale accounts behind it are unread. Filed as `none`.

**Tech.** No tech rubric was issued, so the scale is provisional. Mackage names three technologies:
- Nordic Tech, its own name for a woven shell, sometimes with a membrane.
- Agile-360, its own name for a stretch shell.
- PrimaLoft Silver, licensed.

These appear on 10 of the 86 styles read (12%). Proposed tech score: 2.

**Craft.** The house dates and places its founding ("Founded in Montreal in 1999") and shows certification logos (OEKO-TEX, RDS, LWG Gold, GRS, amfori). PDPs name RWS wool and GRS recycled down. It names no maker, mill or owned facility. No product page checked (~30) states a made-in country. Proposed craft score: 2, with 1 arguable.

**Owner.**
- Private and founder-led: Eran Elfassy, with Elisa Dahan (co-creative director from 2001, per Wikipedia).
- Wikipedia's infobox names APP Group Inc. (Elfassy family) as owner, without a citation.
- InterLuxe (Gary Wassner, Lee Equity-backed) was reported to take an undisclosed stake, per WWD via the Sage republication of 31 Mar 2017. I found nothing on the current status of that stake.
- The 2022 FashionNetwork search hit names a CEO, Tanya Golesic; I did not read it.

**Quote.** Eran Elfassy and Elisa Dahan, answering jointly, in a theFashionSpot interview of 2013-11-18. I read it through the fetch summariser, so check it is verbatim before it goes on the page.

**Not reached (NC):**
- search URL and feed currency rate
- colourway ratio
- Vinted brand id (the brand page showed none)
- B Corp: directory results did not render
- GOTS: PDPs say "organic cotton" with no GOTS named
- signature product and pronunciation
- 33 unread outerwear styles: all men's handles are listed in `scratch/mackage/handles.tsv`; the 33 are those not in `scratch/mackage/comp.tsv`

**Pacing.** I sent three fetches in parallel once, early on (TEE-MNV, TREY, MARCO). Every other fetch went one at a time.


## Ministry of Supply


**Status: partial** (doors, Vinted, GOTS and search URL are NC). About 50 fetches, one at a time, with no 429s.

### Checked
- **Census.** I could not pull the feed with curl: the agent proxy refused the CONNECT with a 403, so I worked through WebFetch only. The product sitemap lists 99 URLs: 47 men's colourway handles, 52 women's, bag and gift-card handles. `/products.json` paged at limit=1 ends at page 98 (page 99 is empty), so the feed and sitemap agree to within one. The 47 men's handles collapse to **12 men's styles**. I read every style's PDP. All 12 state a composition.
- **Fibre.** 3 of 12 styles lead with natural fibre (merino: Travel Merino Tee, Velocity Merino Harrington, Travel Merino Boxer Brief), so natural is 25%. The other 9 lead with synthetic (polyester), so synthetic is 75%. Cellulosic is 0. 6 styles state elastane. Kinetic is warp-knit stretch with no elastane stated. Sorona is DuPont's PTT, so I mapped it to polyester; that makes the Apollo polo and Apollo shirt 100% polyester. No category has 10 or more styles, so shape is `one`.
- **Lines.** Apollo, AeroZero, Kinetic, Velocity, Travel Merino and MPS. MPS is the "(MPS)" handle suffix, which I take to be Ministry Production Systems. Every line except Travel Merino is wholly synthetic-led. Velocity is mixed: its Harrington is merino-led.
- **Previous Generation Velocity Suit Jacket (LW2).** It is live but final sale ($298, compare-at $495). I counted it as its own style because it has a different maker (Matsuoka / Toray-TGE). I did not use it for prices.
- **Prices** (whole USD; the exact figures are the same, at .00):
  - Tee: $88.
  - Polo: $128.
  - Dress shirt: $168 (Apollo 2.0) to $178 (AeroZero compare-at; $150 shown on every colour).
  - Dress pants: $150 (Kinetic) to $248 (Velocity).
  - Outerwear: $198 (Harrington).
  - Jeans, sweater and shoes: NONE in the live range.
  - **The Kinetic Pant breaks the compare-at rule.** The Navy colour shows $150 with no compare-at, while the other colours show $150 with a $178 compare-at. I filed $150 because I suspect the $178 compare-at is stale. Sebastian to rule.
  - Blazers and suit jackets are not priced slots. Kinetic Blazer $398; Velocity Suit Jacket $598 compare-at, $478 shown.
- **Listing links.** `mens-shirts` and `mens-outerwear` are confirmed men's-only through the collection feed. `mens-t-shirts` is empty and there is no pants collection, so tee, polo and dress pants use the parent `mens-shop-all-1`.
- **Tech.**
  - Brand-named fabric families: Apollo, AeroZero°, Kinetic, Velocity, plus Atlas on the tech page, which is not in the live men's range. The fabric-technology page makes no ownership or patent claim for any of them.
  - Licensed fibre trademarks on the PDPs: Primeflex®, Solotex®, Sorona.
  - The Labs page claims "patent-pending Active Textile Tailoring" with the MIT Self-Assembly Lab and a $1.2M research grant. The 3D-knit work dates from 2018 per the timeline, and the 3D Print-Knit Blazer survives only as an old collection handle.
  - I filed `both`. 10 of 12 styles carry a named tech, so share is 83%. Proposed 4 on the provisional scale, since **no tech rubric was issued.** It could be argued down to 3, because the fibres themselves are bought in.
- **Craft: proposed 3.** PDPs name Lever Style (Shenzhen/Dongguan) as maker on 10 of 12 styles and state China on 11 of 12. No owned facility is shown and no mill is named.
- **Founders.** Brand pages name none ("Founded at MIT by engineers"). Wikipedia lists Advani, Amarasiriwardena, Rustagi **and Kit Hickey**; the brief omitted Hickey. Advani appears as Co-Founder & CEO on the Klaviyo Boston 2025 speaker page. Founded 2012 per Wikipedia and the CEO bio; the brand timeline says "2011 — Born at MIT".
- **Owner.** Private and venture-backed: a 2013 seed of $1.1M from VegasTechFund and SK Ventures. I did not establish later rounds or the current owner.
- **Quote.** A house-voice line from the 5-year-plan page. I found no on-site founder quote.

### Doors — not established
- The stores page reads "We're Moving! … new location(s) coming soon" and gives no addresses. The home footer no longer links to it.
- Yelp search snippets (2026) mark NYC 138 Wooster, NYC 268 Elizabeth, DC 3112 M St NW and Santa Monica Place as CLOSED.
- Boston 316 Newbury St is not marked closed in its snippet (Yelp updated Sept 2026), but the Yelp page itself is robots-blocked to WebFetch. I found no press on a Boston closure or move.
- So `own_doors_us` is NC, not 0, and the doors file is header only. A human or browser read of Yelp or Google Maps for 316 Newbury St would settle it.
- The facts-first "SOFT ZERO" should not be filed as 0.

### Contradictions with brief / facts_first
- Worklist "own stores in Boston, NYC, DC, SF": NYC (both sites), DC and Santa Monica are closed per Yelp. I found no evidence of an SF store; the SF door rests only on the undated Wikipedia text.
- The live range is tiny: 12 men's styles. The old collections sitemap shows roughly 100 retired men's styles, including sweaters, chinos, parkas and merino knits. Read together with "We're Moving!", the Last Chance Sale and the on-demand MPS model, this looks like a sharp contraction. The `premium · tech` seat may want a look.

### Not reached
- Vinted brand id.
- GOTS database.
- B Lab directory: the UI is not readable and the company slug errors. `b_corp=no` rests on that, plus the brand citing Climate Neutral rather than B Corp.
- Search URL test.
- `Shopify.currency.rate`.


## New Balance


### How this was read
- WebFetch only, about 70 fetches, all one at a time. There were no 429s and no bot checks.
- WebSearch was unavailable: the shared per-turn search budget was spent, and the first search was refused. I did not work around it.
- curl to www.newbalance.com is refused by the egress proxy (CONNECT 403), so no feed was pulled.
- I did not re-read the doors or the prices. Both come from the browser worker's read of 2026-10-10:
  - `doors_new_balance.csv` and `doors_summary_new_balance.txt` were left untouched.
  - The prices were copied from `nb_prices_browser.json`.

### Contradicts the brief
- **newbalance.com is not blocked for product pages.** `/pd/…html` PDPs, `/made-in-usa/`, `/our-purpose/`, the Made in UK page and the 2025 Sustainability and Impact Report PDF all read normally.
- What is robots-disallowed:
  - parameterised listing URLs (`?start=…&sz=…`, which robots.txt lists);
  - `corporate.newbalance.com`;
  - `/search?q=`.
- Category grids (`/men/clothing/`, `/men/clothing/shirts/`) server-render no product tiles and show an empty count "()".
- **Factories are not only Maine and Massachusetts.** NB's own report lists five New England footwear factories: Lawrence MA, Methuen MA, Norway ME, Central Maine/Skowhegan ME, and **Londonderry NH** (new; production pilots began in 2025). It also lists Flimby UK.
- **The 70% domestic-value claim covers footwear only.** Made in USA apparel pages say "Manufactured in the U.S., from domestically sourced fabrics" and give no percentage.
- **Doors brand key.** The doors file was written by the browser worker and uses `new_balance` in the `brand` column, not the canonical `New Balance`. I did not overwrite it (as instructed). It needs a rewrite at merge, or reconcile will orphan 179 rows.

### Prices (from the browser read; rules applied here)
| Garment | Basis | Low | High | Notes |
|---|---|---|---|---|
| Tee | range | $29.99 | $74.99, Made in USA Heritage Running Graphic Tee | Recorded alternative high: NYC Marathon Race Day Ultra Light Printed T-Shirt, $109.99 (event collection; 74% recycled nylon, 26% Lycra). |
| Polo | single | $54.99 | $54.99 | |
| Outerwear | range | $99.99 | $179.99 | Shohei items treated as collaboration. |
| Shoes | range | $69.99, Made in USA RX40 | $299.99, TDS Niobium C1 | No loafer. |

**Sweater is filed as NONE, a change from the browser JSON.**
- The JSON filled sweater with fleece crew *sweatshirts* (Sport Essentials Fleece Crew $64.99 to Made in USA Core Crewneck Sweatshirt $154.99).
- rules_prices says "not a sweatshirt", and the browser itself notes "No knit sweaters sold".
- The figures are kept here for Sebastian's ruling.

**Dress shirt is NC.** The browser JSON has no dress-shirt entry, and the shirts listing could not be read by WebFetch.

**Jeans and dress pants are NONE**, per the browser read.

`search_url` is NC because `/search?q=` is robots-disallowed and was not tested.

### Fibre: documented sample, 37 styles (`styles_new_balance.csv`)
- `sitemap_0-product.xml` was read via WebFetch, which truncated it at 299 entries. I took every distinct en-US men's apparel code (MT/MJ/MP/MS) in that part: 33 styles. To those I added 4 PDPs from the price read.
- The sample is not random and leans to core/basic lines (Sport Essentials, Athletics, RC).
- `styles_total` is NC; no census was possible.
- All 37 state a composition.

| Category | Styles | Natural-led | Lead |
|---|---|---|---|
| Sweats | 11 | 11 | all cotton |
| Tees-polos | 12 | 5 | synthetic-led |
| Trousers | 5 | 2 | synthetic-led |
| Shorts | 6 | 2 | synthetic-led |
| Outerwear | 3 | 0 | all polyester |

- **Totals:** 54% natural (all cotton), 46% synthetic, 0% cellulosic.
- **Spandex:** 12 styles, 10 of them at 5% or more.
- **Shape: split.**
- **Lines** were read from title series:
  - Wholly natural: Athletics cotton pieces and Made in USA (3 styles, 100% cotton).
  - Wholly synthetic: RC, recycled polyester with NB DRY/ICEx/HEAT.
  - Mixed: Sport Essentials, 60/40 cotton/recycled-polyester fleece alongside 100% cotton tees and a polyester mesh short.
  - Every line is under 10 styles in the sample.
- **Flag:** Basketball Padded Jacket says "Nylon woven fabric" and also "Main body: 100% recycled polyester". Filed as polyester.
- Swim: not established (NC).

### Sections 6–13
- **Tech.** Owned: Fresh Foam and FuelCell (seen on the RX40 and 990v6 pages), ENCAP, NB DRY, NB ICEx/ICE, NB HEAT, NB Sleek. Licensed: Lycra. tech_share 35% = 13 of 37 apparel styles carry a named NB technology. Footwear share not counted. **proposed_tech 4 is on a PROVISIONAL scale; no tech rubric was issued.**
- **Craft: proposed 4**, with a 3 arguable.
  - Evidence: owned factories are documented in NB's own 2025 report and press boilerplate ("owns five athletic footwear factories in New England and one in Flimby, U.K."). About 1,100 associates work in New England and nearly 300 at Flimby, and the factories are on Open Supply Hub.
  - But NB says Made in USA is "a limited portion" of US sales.
  - Of the 37 apparel PDPs, 34 say only "Imported"; 3 state Made in USA (8%). Footwear origin share is not counted.
  - No maker or mill is named on any product page. Horween is named only in a press release.
- **Founding.** Verified in NB's own 2025 report (p.5): 1906, William J. Riley, "New Balance Arch Support Company", Boston, Massachusetts. Wikipedia says only "the Boston area".
- **Ownership.**
  - Privately held and family-owned, with Jim Davis as Chairman (2025 report).
  - Purchase in 1972 and the Davis family's ~95% are from the Forbes profile (an estimate, not NB's words).
  - Release figures: $9.2bn 2025 sales; 14,000 associates. The report says 13,000+.
- **Lookbook: no.** The site has a Made in USA collection grid with a short header. The FW26 Made in USA press release carries 13 images, which is not a lookbook.
- **Vinted: NC.** Vinted pages gave no brand id, and I did not guess one.
- **Grailed:** `/designers/new-balance`. The page title was confirmed, but the feed did not load in the fetch.
- **B Corp: NC.** The directory search is script-rendered, and a guessed profile URL errored. The 2025 report does not mention B Corp.
- **GOTS: no.** Basis: the 2025 report says "In 2025, we did not source any organic or recycled cotton"; cotton is BCI mass-balance. The GOTS database itself was not searched.
- **Quote.**
  - Source: "Our Purpose" page, the house purpose line, 20 words.
  - WebFetch returned it in two fragments ("Independent since 1906, we empower people through sport and craftsmanship" + "to create positive change in communities around the world"), stated to be one sentence.
  - The same wording is in the press boilerplate. Worth one human glance.
  - Alternative quote: the 990v6 line below.
- **Signature product:** Made in USA 990v6, "The designers of the first 990 were tasked with creating the single best running shoe on the market." (NB product page). The 574 and 550 were not read.

### Not reached
- World doors.
- Stockists. The locator lists NB-banner doors only, so the stockists file has one `none` row.
- Men's clothing census and swim.
- Footwear origin and tech share.
- Vinted id.
- B Corp directory.
- Dress shirt.


## Nike


**Conditions.**
- I read with WebFetch and WebSearch only: about 100 fetches and 9 searches.
- The proxy refuses curl to www.nike.com (CONNECT 403), so no feed was pulled.
- WebFetch reports `api.nike.com/product_feed/threads/v2` as ROBOTS_DISALLOWED. I did not try any other route to it.
- There were no 429s and no bot checks.
- **Pacing slip:** one batch of 5 product pages went out in parallel (JA0084, JA0086, IZ3196, IH1121, IX2080). Every other fetch was made one at a time.
- I did not attempt the store locator, as briefed. `doors_nike.csv` is header-only.

### What was checked

**Store and search.** I read nike.com in the US store, in USD. Site search is `https://www.nike.com/w?q=`; I tested it with "mens button shirt", which returned 454 results.

**Two grid limits apply to everything below:**
- The grid server-renders only the first 48 tiles.
- Under WebFetch it ignores `?sort=priceDesc`. The order came back identical to the default.

So every price high is the **highest seen**, not a proven top of range.

**Prices (list prices; compare-at where marked down):**

| Garment | Basis | Low | High | Notes |
|---|---|---|---|---|
| Tee | range | $32, Swoosh tee | $55, ACG Dri-FIT tee | Read from the first 48 of 1,482 "Tops & T-Shirts". |
| Polo | range | $55, NikeCourt Dri-FIT (sale $38.97) | $140, Tailored Performance golf polo (sale $79.97) | Five other Tailored Performance tiles also list $140. All 48 polo tiles were marked down. |
| Dress shirt | range | $75, Club short-sleeve button-down | $120, ACG Aireez long-sleeve button-up | Nike makes no dress shirt; these are casual button-fronts. The Aireez is a button-up, button-down-collar trail top in 72% nylon/28% spandex, and the page does not say "woven". |
| Jeans | range | $115 | $115 | Two Nike SB Loose Denim Skate Pants. The Yuto Horigome signature denim at $200 was not used as a high (athlete-capsule judgement, flagged). |
| Dress pants | range | $75, Club Woven Tapered | $150, Club Rules Pleated (100% cotton) | There is no tailored trouser. Chinos run $100–$130: Tour Repel and 24.7 PerfectStretch. |
| Sweater | single | $90 | $90 | Nike Club Crew-Neck Sweater, 100% cotton. It is the only crewneck knit found, via web search; the nike.com "knit sweater" search returned none. |
| Outerwear | range | $65, Totality Dri-FIT knit jacket | $400, ACG Lava Flow Ultralight down jacket | Club Wool Varsity also lists $400 (54% wool). ACG x US Olympic Team is a collaboration and was excluded. Read from 48 of 174 tiles. |
| Shoes | range | $75, Court Heritage SL | $240, Vomero Premium | Grid tile prices from 48 of 773 tiles. There is no loafer. |

Shoes notes:
- Excluded: Jordan, plus the AF1 GORE-TEX Vibram as a collaboration.
- Kobe and Ja are athlete lines carrying Nike branding and were counted.
- Racing shoes priced above $240 likely exist beyond the tiles read; that is not established.

**Listing links set to NC:**
- Dress shirt, jeans and sweater: no men's category page was found, and the searches mix in kids', women's and footwear items.
- Shoes: the men's shoe grid shows two "Women's Shoes" Air Jordan tiles, which fails the men's-only test.
- The tee link is the parent "Tops & T-Shirts" page, and the dress-pants link is the parent "Pants & Tights" page.

**Jordan scope.** Jordan Brand is sold on nike.com and appears in the men's grids. It carries Jordan/Jumpman branding, not Nike, so I skipped every item titled "Jordan …" or "Air Jordan …" in prices, styles and the fibre sample.

**Sub-lines.**
- ACG counts as a standing sub-line.
- Nike SB, NikeCourt, Nike Golf, Nike Tech, 24.7 and Project F.R.O.G. are counted as Nike-branded lines.
- Project F.R.O.G.'s page presents it as a Nike line, not a collaboration.

**Fibre: documented sample of 64 styles** (target was ~80; I stopped to stay under the fetch cap).
- The men's clothing grid states 2,269 tiles. Each tile groups colourways, but style numbers vary within one title (two Nike SB denim pants share a name), so I did not establish a style count. `styles_total` is NC.
- **How the sample was drawn:** first distinct non-Jordan styles in default grid order from Men's Clothing, Tops & T-Shirts, Polos, Jackets & Vests and Shorts. Shirts, denim, knit and chinos came from searches. One swim style was added.
- **Per category:**

  | Category | Styles read |
  |---|---|
  | Tees-polos | 23 |
  | Trousers | 12 |
  | Outerwear | 10 |
  | Shorts | 8 |
  | Sweats | 5 |
  | Shirts | 2 |
  | Denim | 2 |
  | Knitwear | 1 |
  | Swim | 1 |

- **Results, on the sample only:**
  - Composition is stated on 64 of 64.
  - Natural-led 32 (50%), synthetic-led 32 (50%), cellulosic 0.
  - Spandex on the main line: 5 styles (13%, 3%, 6%, 28%, 10%).
- **Shape is split.**
  - Cotton leads: tees (12 natural vs 11 synthetic, a near tie), trousers (7 vs 5), sweats (5 of 5) and denim.
  - Polyester or nylon leads: outerwear (8 of 10) and shorts (6 of 8).
- **Parsing calls, flagged in the styles file:**
  - DC5094 and FN3730 give the composition as a range ("50-100% cotton/0-50% polyester"). `lead_pct` is the lower bound.
  - The bonded Tech Boreas pieces (IM6227, IM6229) list the face as 100% cotton and the back as 100% polyester. Lead fibre is cotton by the first-listed rule, but `pure` is set to `blend`.
  - Rib, mesh, panel and pocket-bag spandex is excluded per the rules.
- Nike Swim pages use NESS style codes and give no origin line. The swim listing (79 items) mixes in caps, goggles, towels and bags, so `swim_styles` is NC.

**Doors** (FY2026 10-K, year ended 31 May 2026):

| | In-line | Factory | Converse |
|---|---|---|---|
| US | 75 | 212 | 60 |
| Non-US | 50 | 537 | 54 |

- `own_doors_us` = 75 and `own_doors_world` = 125 (in-line only).
- In-line counts include employee-only stores, which the filing does not break out.
- Facts-first's 75 / 212 / 60 is reproduced.

**Stockists.** One row only: the locator URL with NC. I did not read it.

**Tech.** The tech scale is PROVISIONAL; no tech rubric was issued.
- 27 of 64 sampled styles (42%) name a Nike-owned technology: Dri-FIT, Dri-FIT ADV, Therma-FIT, Therma-FIT ADV, Storm-FIT, Storm-FIT ADV, Aero-FIT, Tech Fleece and PerfectStretch. Concentration is highest in performance tops, outerwear and the Tech line.
- One style also carries licensed PrimaLoft, so `tech_owned_or_licensed` = `both`.
- **Proposed 4.** It is not a 5 because cotton Sportswear tees and fleece, about half the sample, carry no named technology.

**Craft. Proposed 2 (borderline with 1).**
- 0 of 63 non-swim product pages state a country; all say "Imported". No maker or mill is named.
- The 10-K documents contract manufacturing: 321 apparel factories in 34 countries and 95 footwear factories in 11.
- Nike publishes a factory map at manufacturingmap.nikeinc.com. It is script-rendered and its contents were not read.
- The only owned making is Air Manufacturing Innovation (footwear cushioning components).
- The heritage is dated and placed on Nike's own site: 25 Jan 1964, Cosmopolitan Hotel, Portland, Knight and Bowerman.

**Quote.** The NIKE, Inc. mission and its footnote, from about.nike.com/en/mission (undated page). The page sets it in capitals; I wrote it in sentence case.

**Signature product.** Air Force 1 '07. Its product page says: "Comfortable, durable and timeless—it's number 1 for a reason." The page does not mention 1982 or use "iconic". I did not read an Air Max page for its wording.

**Other.**
- Vinted brand id 53: the vinted.com/brand/53-nike page shows Nike with 500+ results.
- Grailed /designers/nike exists ("Nike Clothing & Sneakers for Men").

### Not reached
- **Locator:** the per-door list and the banner mix (own vs partner-operated Nike stores) were not read.
- **Lookbook:** none was found for Nike's own men's line. The only hit was a NikeSKIMS lookbook, a women's collaboration that is out of scope. `lookbook_found` = no, and the rest of the lookbook fields are NC.
- **B Corp:** the directory search is script-rendered and returned no results through WebFetch. NC.
- **GOTS:** not checked. NC.
- **Colourway ratio and full category counts** (hoodies, pants and the rest) were not established.

### Contradictions and brief notes
- **Brief:** "factories in Vietnam, Indonesia, China" is right for **footwear** (52/27/16%). For **apparel**, the 10-K names Vietnam ~34%, **Cambodia** ~15% and China ~12%.
- **Facts-first:**
  - Facts-first's tee low ($32 Swoosh) is reproduced. Its outerwear top ($400 ACG Lava Flow Ultralight) is reproduced and is not a collaboration.
  - The Swoosh tee is "50-100% cotton/0-50% polyester". The AI review summary on the page says 100% cotton, which conflicts.
- **worklist "own US stores everywhere":** this overstates the full-price fleet. There are 75 full-price US doors against 212 factory outlets.


## Off-White


**Status: partial.** Prices come from listing tiles. The fibre sample is 13 current styles, not the ~60 the brief asked for. `own_doors_world`, Vinted, B Corp, GOTS and the shoes high are `NC`.

Method: WebFetch only, about 75 fetches made one at a time, no 429s and no bot checks.
- **WebSearch budget ran out** early in the run ("limit: 200 WebSearch calls per turn, shared by every agent"). Only one site search was made, and it was not worked around.
- curl to off---white.com was denied by the proxy (CONNECT 403). It was not worked around.
- WebFetch refused robots-disallowed paths (`?srule=`, bluestaralliance.com/brands, zendesk search). These were not worked around.
- The doors were done by the browser read and were **not touched**. **Flag:** the `brand` column in `parts/doors_off_white.csv` is `off_white`, not the canonical `Off-White`. Assemble will reject it, so fix it at merge.

### Store and census
- US store: https://www.off---white.com/en-us/, Salesforce Commerce Cloud, USD.
- `search_url` is `NC`: the search path is robots-disallowed, so it was not tested.
- Men's clothing shows **189 tiles** on `/en-us/men/clothing/?page=1..8`. 24 a page; page 8 has 21. `?start=`/`sz=` are ignored and re-serve page one; `?page=N` works.
- Deduplicating titles gives **164 styles** (`colourway_ratio` 189/164, `title_dedup`). Because of that method it is approximate.
- Category counters: T-Shirts 72–73 (the counter wavered between 72, 73 and 82 across loads), Shirts 16, Knitwear 14, Outerwear 16, Denim 20, Pants 32–35.
  - Denim mixes jeans, jackets, shirts and shorts. Pants mixes sweatpants, shorts and jeans.
- No swim: 0.
- **Listing tiles carry no product hrefs and no codes** for a fetcher. PDPs render **no price** on 11 of 16 pages. Prices therefore come from the tiles, and each price `*_url` is the listing page it was read on.
  - Tile prices also render on some loads and not others: denim, pants page 2, clothing pages 3, 7 and 8, and shoes pages 2–3 came back without prices.
- The product sitemap (`/en-us/sitemap-product_0.xml`) holds only 50 products: 16 men's clothing URLs covering 13 styles, mostly SS26 tees. These were the only reachable PDPs. The en-gb sitemap is the same 50.

### Prices (whole USD = exact; all full price, no strikethrough seen)
| garment | low → high | basis and caveat |
|---|---|---|
| Tee | $195 → $635 | range |
| Polo | `NONE` | no polo in any of the 189 tiles |
| Dress shirt | $495 → $845 | range; the brand makes only casual shirts |
| Jeans | $515 → $895 | range |
| Dress pants | $580 → $845 | range; no tailored trouser exists |
| Sweater | $595 → $945 | range |
| Outerwear | $795 → $3,695 | range |
| Shoes | $215 → `NC` | high not read |

- **Tee.** Low is the Small Bookish T-Shirt; facts-first's $195 is reproduced.
  - The three AC Milan tees at $195 are collaborations and are excluded.
  - High is the City Nature Relaxed Long Sleeve T-Shirt.
  - Mr. Davis (Miles Davis) pieces are treated as a collaboration and excluded.
- **Dress shirt.** Bowling and regular shirts only. Overshirts are excluded as shirt-jackets: Racing Staff Mesh $895, Color Block Denim Crystal $1,395.
  - The City Nature Regular Denim Shirt ($895, under Denim) would be the high if denim shirts count.
- **Jeans.** 8 of 10 jean styles were priced. Arrow Monogram Degradé Jacquard Jeans and Half Arrow Twist Slouchy Jeans never showed a price, so the high could be above $895.
- **Dress pants.** Cotton gabardine pants stand in for chinos. Sweatpants, track pants and the jersey Lounge Pant ($710) are excluded.
- **Sweater.** Fibre is unread, so an elevated-fibre pair cannot be established. The category blurb says "refined cashmere sweaters", but no tile names cashmere.
- **Outerwear.**
  - **The facts-first $3,800 AC Milan Varsity Jacket is a collaboration and is replaced.**
  - The new high is the Book Fleece Hoodie Bomber. **Its composition was not read.** If it is fur or shearling, the next is the OG Patches Racing Leather Varsity Jacket ($3,500), then the Racing Staff Varsity Jacket ($2,900).
- **Shoes.** 93 tiles, no loafer. Low is the Bookish Sliders, read on the PDP. High is `NC`: shoes pages 2–3 rendered no prices.
  - Page 1 topped at $650 (Out Of Office / Be Right Back), but Strass and Bejeweled versions on later pages were unpriced.

### Fibre
- 13 current-range PDPs were read: 11 tees (2 of them AC Milan), 1 sweatshort and 1 AC Milan hoodie.
  - **All 13 say "Fabric: 100% Cotton"**, and none states elastane.
  - Two canonicals sit under `/sale/` and one under `/archive/`.
- One archive SS25 varsity jacket was also read (75/25 wool/polyamide, leather sleeves). It is filed with a note and not counted.
- The brand percentages, `shape` and the category lists are `NC`. The sample is 8% of styles and is all jersey, so it says nothing about outerwear, denim or knit.

### Doors (browser read, not re-done)
- `own_doors_us` = 1: Miami Design District, own-door, operator unknown. Woodbury Common is filed as an outlet.
- NYC, LA and Las Vegas returned no stores. That contradicts the worklist's "US stores in NYC, Miami, LA".
- `own_doors_world` is `NC`.

### Ownership and origin
- **Bluestar Alliance verified.** PR Newswire, 30 Sep 2024, Paris dateline: LVMH sold Off-White LLC, "the company that owns the Off-White brand", to Bluestar Alliance, LLC.
  - No later change was found, but WebSearch was unavailable to check.
  - Wikipedia's infobox has "Bluestar 60% / Farfetch 40%". The release does not mention Farfetch. Not filed.
- **Founding conflicts in the one release.** It says "Founded in 2012 by Virgil Abloh" and also "Established in 2013".
  - 2012 is Pyrex Vision; the Off-White name dates from 2013 (Wikipedia). Filed as 2013, Milan.
  - The brand's own heritage page (`/brandvision`) gives no year or place.
- Footer: trademarks owned by Off-White LLC; site operated by The Level S.r.l.; seller of record and licensee Progetto 17 S.r.l., Piazza Arcole 4, Milan.

### Craft: proposed 1
- **"Made in Italy/Portugal" has no evidence.** 0 of 16 PDPs read state a country (13 clothing, 1 archive jacket, 2 shoes).
- No maker, mill or facility is named, and the heritage page is about culture, not making. A famous name earns nothing.
- Craft URLs: `/brandvision` and the Half Arrow tee PDP.

### Other sections
- **Tech:** `NONE`. No named fabric or technology on any page read. "Tech T-shirt" is a garment name, not a technology. The tech scale is PROVISIONAL (no rubric was issued).
- **Lookbook:** the FW26 show page has a LOOKS gallery. The season is written "Fall/Winter 2026", and it is a men's and women's mix.
- **Quote:** Ibrahim (IB) Kamara, SS26 "Pop Romance" show page; the page is undated.
  - On the page his title is not stated. The heritage page styles him "Art&Image Director".
  - No Virgil Abloh first-person quote was found on brand pages.
  - The FW26 line "Disruption can't happen in a vacuum." is under 6 words.
- **Grailed:** `/designers/off-white` resolves, titled "Off-White Clothing | Grailed".
- **Vinted:** the catalog page exposed no brand id, so `NC`.
- **B Corp:** the directory did not render results, so `NC`. GOTS was not checked.
- **Stockists:** `none`. The brand lists no stockists: no footer link, and the locator shows only Off-White doors.
- **Signature product:** the Out Of Office Sneakers ($650), a judgement.
- **Mark:** written "Off-White™". Pronunciation `NONE`.


## Orvis


**Status: partial.** About 95 WebFetch calls, run one at a time with no parallel calls. orvis.com served every listing and product page with no 429s and no bot checks. Two paths failed:
- `/search` is robots-disallowed to WebFetch, so `search_url` is NC.
- `/our-history` and `/rod-shop.html` returned fetch errors.

WebSearch was unavailable: the shared per-turn search budget was used up. Every source here was fetched directly. I pulled no feed or sitemap. The site runs on Salesforce Commerce Cloud, and its grids paginate cleanly with `?start=N&sz=20` (20 tiles per page). I did not touch the doors file: `doors_orvis.csv` is the main thread's browser read.

### Scope: Orvis label only
I judged each product by its label, not the vendor field. These resold goods are excluded:
- Barbour, which runs right through the men's grids: 3 shirts, 1 sweater, 16 of 32 jackets, 5 gilets/liners and 1 fleece.
- Mavi jeans.
- Danner, Lacrosse and Le Chameau boots.

### Prices (orvis.com, USD, full price)
- **Tee: $45–$89, range.** Crossed Rods T-Shirt at $45; eight graphic tees share that price. High is the Outbound Merino SS Tee at $89. The DriCast LS Crew grid shows "$49–$69, 28% off", but the PDP shows $69.
- **Polo: $79–$110, range.** Bromley Polo (slub Pima) at $79 and Outbound Merino Polo (87/13 wool/nylon) at $110. These are the only two polos. There is no polo category, so the listing link is the parent Shirts & T-Shirts page, which also carries Barbour.
- **Dress shirt: $98–$119, range.** Orvis makes no dress shirt, so these are casual button-downs. Low is the Country Twill LS Button-Down at $98. High is the River Guide LS at $119, tied with the Tech Chambray Western at $119.
  - Short-sleeve shirts are excluded: the Poplin SS is $79 regular and the Featherweight SS $89.
  - The PRO LT Upland Shirt ($129, nylon/spandex, woven not confirmed) and the Snowy River Brushed Knit ($139, a knit) are excluded from the high. **Taking either would change the high.**
- **Jeans: NONE.** The only jeans sold are Mavi.
- **Dress pants: $119–$139, range.** There is no dress trouser, so these are chinos: 1856 Stretch Twill Chinos at $119 and Out-Of-Office Chinos at $139.
- **Sweater: $129–$179, range.** Merino Piqué Crewneck to Moss Stitch Crewneck (80/20 wool/nylon). No crewneck uses an elevated fibre.
  - The Merino Piqué PDP displays "$129 - $149" in one colour with no sale flag. I took $129; the basis for the $20 spread was not established.
- **Outerwear: $119–$449, range.** Low is the R65 Sweater Fleece Jacket at $119. High is the PRO Fishing Jacket, tied with the PRO ToughShell at $449. These reproduce facts_first's $449. The Barbour Modern Beaufort at $575 is excluded.
- **Shoes: $129–$149, range.** There are two own-label shoes and no loafer: the PRO 6" Deck Boots ($129) and PRO Approach Shoes ($149).

### Fibre: 45 of 93 styles read (48%)
**The census is 93 Orvis-label men's clothing styles, deduplicated on item code:**

| Source | Styles |
|---|---|
| Shirts & T-Shirts | 35 |
| Pants & Shorts | 17 |
| Sweaters | 5 |
| Jackets | 16 |
| Vests | 9 |
| Sweatshirts & Fleece, codes not seen elsewhere | 8 |
| Clothing found only in the fly-fishing grid (PRO HD Underwader Pants, PRO Fishing Bib, DriCast LS Graphic Crew) | 3 |

- I also read the hunting grid (61 items); it added no new clothing.
- Waders, hats, gloves and mitts are out of scope.
- There is no swim category.

**Coverage.** Every PDP read states a composition. 22 of the 45 list fibres without percentages ("Cotton/spandex."); for those, the lead is the first fibre listed and the share is NC.

**Result, on the 45 read only:**
- 25 natural-led, 20 synthetic-led, 0 cellulosic-led (56/44/0).
- 19 styles have elastane on the main line.

**Shape: split, on the sample.**
- Jackets & Vests: 10 of 12 are synthetic-led (nylon and polyester).
- Sweaters: all wool-led.
- Pants & Shorts: 7 of 9 are cotton-led.
- Shirts: 6 cotton-led and 5 synthetic-led.

**Lines:**
- PRO is all synthetic in the sample.
- 1856 and Missouri Breaks are all cotton.
- Outbound Merino is wool/nylon.

**Figure to check.** The 56/44 split and the spandex count are shares of the 45-style sample; they are not shares of all 93. `styles_with_composition` = 45 is the size of that sample and does not mean the other 48 lack a composition.

### Doors
- `own_doors_us` = **31**: the full-price Orvis Retail Stores. That count leaves out the three pro shops at shooting grounds and a resort (Pursell Farms AL, Sandanona NY, Hill Country PA), which read as concessions. **It is 34 if they are counted.**
- There are 2 outlets, at Kittery and Manchester VT.
- World is NC. The locator is US-only; the about page mentions UK operations, which I did not read.

**The October 2025 closures check out** against two sources:
- VTDigger (2025-10-02) and Fox4 (2025-10-10) report 31 stores and 5 outlets closing by early 2026.
- Fox4 quotes Simon Perkins' statement citing "an unprecedented tariff landscape", and says Orvis works with "more than 550 domestic independent dealers".
- Before the closures, VTDigger counted "at least 64 retail locations and five outlets" on the locator.
- Today's 31 + 3 + 2 fits those figures.

### Stockists
The file has one summary row (locator_kind `store locator`). The locator map shows Orvis dealers geolocated around the viewer, with no national total. Per the main thread's browser read, Florida has 37 map points (all dealers) and Massachusetts 1. Many dealers are big-box stores (Bass Pro/Cabela's, Sportsman's Warehouse) or fly shops rather than clothing shops. I did not enumerate them.

### Craft (proposed 2; a case for 1)
- **No country is stated on clothing.** All 45 clothing PDPs say only "Imported". No maker or mill is named; only licensed fabric brands appear (CORDURA, PrimaLoft, Polartec, Thermore, LYCRA, Supplex).
- **The Rod Shop is real but thinly evidenced, and covers no clothing.**
  - The fly-rods page has an image caption: "A worker at the Orvis Rod Shop working on a new fly rod".
  - The same page claims "more than 150 years of rod building experience".
  - The Helios D and Superfine PDPs say "Made in USA", and 12 rods sit in the Made in USA filter.
- **The Manchester, VT location of the rod shop is not stated on any brand page I read** (rod PDPs, rods page, about page, Manchester store page). The brief's claim is unverified here.

### Origin and ownership: verified on the brand's own pages
- **Founding:** about-us says "In 1856, Charles F. Orvis founded the Orvis Company in Manchester, Vermont".
- **Ownership:** about-us says "Privately owned by the Perkins family since 1965".
- **Current management:** the impact page names Simon Perkins as President and says Leigh, his grandfather, "purchased the company" in 1965.

### Other sections
- **Tech: proposed 3** (provisional scale; no tech rubric was issued).
  - Owned names: DriCast and R65.
  - Licensed: OutSmart Fresh (ownership not established), CORDURA, PrimaLoft, Polartec, Thermore, LYCRA, Supplex, DryTouch, TurboDry, MarinoWul+.
  - 15 of the 45 styles read carry one (33%). bluesign certification and YKK zips were not counted as fabric tech.
- **Quote:** from the house mission statement (undated page).
  - Alternative: Simon Perkins in VTDigger, "We are investing in the areas where Orvis makes its greatest impact."
- **Lookbook: none.** The homepage carries only "New Arrivals" editorial, with no catalogue or lookbook link.
- **Grailed:** /designers/orvis exists; the page title is "Orvis | Grailed" and the feed did not render.
- **Vinted, B Corp and GOTS: NC.**
  - Vinted: /brand/orvis gave no brand id.
  - B Corp: the B Lab directory fetch errored.
  - GOTS: no PDP read names any certification.
- **Signature product:** the Helios fly rod. It is not clothing; the clothing alternative is the PRO Fishing Jacket.

### Not reached
- The other 48 style PDPs.
- colourway_ratio.
- Orvis UK doors.
- Dealer enumeration.
- A rod-shop location page.
- A test of the search URL.


## Paul Stuart


**Access.** Every read was a WebFetch, made one at a time: about 92 fetches plus 3 web searches. No fetch returned a 429 or a bot check. A curl to paulstuart.com for robots.txt and the sitemap was refused at the egress proxy (CONNECT 403). That refusal is a proxy policy, not the site, and I did not retry by any other route. The site runs on Salesforce Commerce Cloud (`/on/demandware.store/Sites-PaulStuart-Site`), so `feed_currency_rate` = not shopify. Category grids page with `?start=N&sz=N`. WebFetch truncates a grid at about 45–60 tiles, so each category was read in pages until the header count was met.

### Contradictions with the brief and facts-first

- **The owner is not Mitsui.** On 24 Dec 2025 FashionNetwork reported that Middle West Partners, partnered with Peerless Clothing Inc., acquired Paul Stuart from Mitsui & Co. John Hutchison (ex-Bonobos) became CEO. Mitsui had owned the brand since Dec 2012, per Wikipedia citing the New York Business Journal. Mitsui sold the Japan rights to Sanyo Shokai in 2021, per Wikipedia citing WWD. I did not read the WWD or Retail Touchpoints originals.
- **There is no women's line to exclude.** Wikipedia (citing WWD, Dec 2022) says womenswear production ceased under Trevor Shimpfky. The site nav is men's only.
- **Japan.** No licensed Japan doors are listed on paulstuart.com. Per Wikipedia, Sanyo Shokai runs a Tokyo Kita-Aoyama flagship plus department-store shops. Those are licensee doors, so they are not own doors and are not in the doors file.
- **Outerwear high.** Facts-first filed $6,995, the Modern Suede Coat with Shearling Trim. The record now has **$4,995**, the Double Faced Cashmere Coat, a three-way tie with the DF Cashmere Toggle Coat and the DF Cashmere Soft Jacket.
  - Shearling is fur-on, so all three shearling styles are excluded from the high: 3281161 at $6,995, 32875162 Shearling Toggle Coat at $6,495, and 32472695 Wool Coat with Shearling Gilet at $3,495.
- **Tee $80** matches facts-first.

### Prices (full price; whole dollars, all exact .00 figures)

Most of the range is marked down, with the compare-at price shown. I filed the compare-at in every case. Pages without one carry a "Final Sale" label, which is a returns policy, not a price. USD is confirmed on two displayed prices: tee $80.00 and polo $125.00.

- **Tee:** a single style, the $80 Pima Interlock Logo T-Shirt. There is no tee category; the link is the Polos & T-Shirts page.
- **Polo:** $125 Cotton Pique Logo Polo to $995 Cashmere & Silk LS Polo.
  - The high is 70% cashmere, so it counts as elevated.
  - Linen & cotton polos run to $850.
- **Dress shirt:** $245 to $495, filed as a range.
  - The low is a three-way tie at $245: the Super 140s Cotton BD, The Traveler, and Blue Sea Island (compare-at).
  - The high, $495, is the Phineas Cole Cotton Stripe and Two-Tone Stripe.
- **Jeans:** no denim category exists, so the link is the Pants parent page. The range runs from Denim Five-Pocket Pant 237B3660 at $350 to Vintage Wash Five-Pocket Denim at $595.
- **Dress pants:** $475, the All Year Wool Dress Trouser, to $995, the Summer Breeze Dress Trouser (40/35/25 wool/silk/linen).
  - **Judgment for Sebastian:** the Dress Pants category also carries the $425 Lightweight Technical Cotton Trouser. I treated it as not the staple. If he rules otherwise, the low is $425.
- **Sweater:** paired as $295 Cotton & Linen Summer Sweater (crewneck) against $750 Cashmere Crewneck. The page confirms the low is a crewneck.
- **Outerwear:** $1,295 Quilted Jacket to $4,995 cashmere coat.
  - Vests and overshirts are excluded from outerwear.
  - The cashmere overshirts at $1,695 and the suede overshirt at $1,995 are shirt-jackets.
- **Shoes:** paired as $395 Lord Suede Loafer against $895 Steven Suede Tassel Loafer. Steven is tied at $895 with Sebastian and Skylar.
  - I excluded the $350 Lloyd Espadrille Penny Loafer as an espadrille. That is a judgment.
  - All loafers carry the "Paul Stuart Footwear" brand line.
- **`search_url`** was not tested (NC).

### Census and fibre

**Census.** I read 15 men's clothing category grids in full: 324 distinct style codes. A code is the numeric stem before the colour suffix; the same pattern in a different cloth has its own stem.
- **Shared tiles.** Tiles are colourways, and many styles are cross-listed: polos also appear in sweaters, and the cashmere soft jackets appear in both blazers and outerwear. Each code was counted once. `colourway_ratio` is NC because cross-listing inflates the tile total (about 650 tiles).
- **What is in scope.** The census covers clothing only: underwear (boxers), pajamas, a robe and 4 swim trunks.
- **Not in the census:** shoes, accessories, and sale-only items absent from the category grids. I did not check the sale tree separately.

**Composition was read on 52 PDPs, 16% of the 324,** sampled across every category. 51 state a composition. All `*_pct` figures are shares of those 52, not of 324, which is why the status is partial.
- **Split:** 88% natural-led, 8% synthetic-led, 2% cellulosic-led, 2% undisclosed.
  - The four synthetic-led styles are two performance polos, a technical jersey trouser and the poly Quilted Jacket.
  - The one cellulosic-led style is a "100% Bamboo" jacket, filed as other-cellulosic.
  - The one undisclosed style is the Belsetta coat: the page says "Microfiber", with no fibre named.
- **Stretch:** 8 styles carry elastane, from 1% to 29%.
- **Shape is `one`:** no category is synthetic-led in the sample.

**Lines.** The named lines seen are Phineas Cole (5 read), Traveler Collection (1) and Made in America (2). All are natural-led, but every one is under the 5-style threshold in the sample.
- **How Phineas Cole was identified:** by the brand line printed on the tile and PDP.
- **The stem prefix does not identify it reliably:** 86080674 is labelled Paul Stuart.

### Doors and stockists

All 4 US stores are filed, with addresses and phones. The flagship is written "Madison Avenue at 45th Street" with no number on both store pages, so I left it that way. `captured_on` = 2026-10-08 per the spec; the actual read was 2026-10-10. The brand lists no stockists.

### Tech

No tech rubric was issued, so the scale is **provisional**.
- **Belsetta** ("Italian Belsetta Fabric") is the only named fabric. Whether it is owned or licensed is not stated, so that column is NC.
- The "Performance Cloth" and "Performance Easy-Care Cloth" labels are generic.
- Proposed tech score: 1.

### Craft (proposed 3)

- **Named makers and mills:** they appear on product pages, but only on a minority of the range (5 of 52).
  - Rochester Tailored Clothing; Hamilton Shirts with Thomas Mason cloth; Loro Piana; Somelos; Mackintosh; American Woolen.
- **Made in:** 87% of sampled PDPs state a country (45 of 52). Italy 27, Canada 10, USA 3, Peru 2, Ireland 2, Scotland 1. The other 7 say "Imported" or nothing.
  - Canadian-made tailoring fits the new co-owner, Peerless (Montreal), but no page says Peerless makes the product.
- **Owned making:** the robe's "in-house tailors" at the Madison Ave flagship is the only owned-making claim, and it is unsubstantiated.
  - Made-to-order shoes are "handmade in Italy" with no maker named.
  - Wikipedia says bespoke tailoring is by Oxxford, a partner.

### Other sections

- **Quote:** CEO John Hutchison, from the brand's Made in America page, which is undated. No founder quotation was found in the time box.
- **Not reached (NC):**
  - Vinted brand id: the search page showed no id.
  - B Corp: the B Lab directory did not render. The sustainability page (24 Aug 2023) mentions neither B Corp nor GOTS.
  - GOTS: "organic cotton" appears on product pages with no certification.
  - Signature product: the site calls nothing "signature" or "icon".
- **Grailed:** the designer page exists.
- **Lookbook:** "Fall 2026 Catalog Lookbook" ("Part I. Fall 2026"), men's only.


## Pendleton


**Status: partial.** About 90 WebFetch calls, run one at a time, with no 429s or blocks from pendleton-usa.com. WebSearch was unavailable because the shared per-turn search budget was used up. No browser was used.

### Platform and access
- **Platform:** Salesforce Commerce Cloud, not Shopify. `/products.json` returns a fetch error.
- **Bash was blocked:** the egress proxy rejected the CONNECT to www.pendleton-usa.com (connect_rejected), so I pulled no sitemap or feed. `sitemap_index.xml` lists three child sitemaps, which I did not read.
- **Search not tested:** WebFetch refuses `/search` (ROBOTS_DISALLOWED), so `search_url` is NC.
- **Pagination:** category pages paginate with `?start=N&sz=20`. A larger `sz` is ignored.
- **Embedded instructions:** WebFetch reported text addressed to the reader inside two category pages (wool shirts p2, jackets). I ignored it. It changed no data.

### Census (men's clothing only; blankets and home lead the site)
- **Tile counts:** 7 subcategories with 193 tiles: Wool Shirts 47, Cotton & Linen 48, Tees & Sweatshirts 37, Sweaters 25, Jackets & Coats 18, Pants & Shorts 7, Bathrobes & Pajamas 11. The parent page says 192 to 195.
- **Style count:** the tiles collapse to **135 style stems** (colourway suffix `_NNNNN` and sale suffix `S` removed). `colourway_ratio` is 193/135.
- **Categories:** shirts 54, tees-polos 27, outerwear 18 (includes the Forest Twill shirt-jacket from Wool Shirts), knitwear 17, other 10 (sleepwear and robes, 4 of them unisex robes), sweats 5, trousers 3, shorts 1.
- **No swim, no jeans and no tailoring.** The two men's slippers are accessories and out of scope.
- **Styles file:** `styles_pendleton.csv` has all 135 stems. 45 PDPs were read; the other 90 are tile-only rows with NC fibre cells.
- **URLs not opened:** product URLs were built from the tile code and title. The pattern resolved correctly on all 46 I opened.

### Fibre: 45 PDPs sampled, weighted toward wool
- **Result:** 44 PDPs state a composition. 43 are natural-led and 1 is synthetic-led (Harding Fleece Jacket, 93% polyester). None is cellulosic-led.
- **Elastane:** one style (Astoria Stretch Chinos, 2%).
- **Undisclosed:** one (LS Deschutes Pocket Tee, "premium cotton", no percentage).
- **Blends:** the linen/rayon Shoreline linen shirt and a 65/35 cotton/poly hoodie.
- **Aggregates left NC:** brand percentages and shape are NC because only 33% of styles were read. Read alone, the sample suggests a one-cloth natural house, but the sample is too small to file that.

### Prices (USD, full price)
- **Tee: $35–$65, range.** Low is the Saddle Graphic Tee at exactly $34.50; high is the LS Deschutes Pocket Tee at $65. The listing mixes in sweatshirts.
- **Polo: NC.** There is no polo shirt. The only candidate is the Merino Polo Sweater ($175, in Sweaters, sleeve length not stated). I did not file it as a polo or as NONE.
- **Dress shirt: $110–$230, range.** No dress shirts, so these are casual shirts.
  - Low is the Burnside Doublebrushed Flannel at $110. The Laramie at $98 is snap-front, so it is excluded. The Burnside PDP does not describe its front closure.
  - High is the Board Shirt, whose PDP shows "From $198.00 to $230.00" (OG price $230). Which variant carries $230 is not established.
- **Jeans: NONE.** There is a denim shirt but no jeans.
- **Dress pants: $148, range.** These are chinos: Astoria Stretch and Relaxed Moleskin, both $148. Skyler Cotton/Linen Pants ($119, elastic back) are excluded.
- **Sweater: $128–$295, range.** Low is the Shetland Collection crew at $128. High is the Original Westerley shawl cardigan at the top of its $275–$295 range. Crewnecks alone run $128–$188 (Donegal Fisherman). No elevated-fibre crewneck exists.
- **Outerwear: $248–$625, range.** Low is the Tahoma Canvas Trucker at $248, tied with the Harding Fleece Jacket and the Carson City Ranch Coat. High is the Brownsville Shearling Collar Coat at $625. Vests, CPO jackets and shirt-jackets were not taken.
- **Shoes: $150, range.** Two men's wool slippers (Moc and Plaid Clog), both Pendleton-branded and imported from China. There is no loafer. The listing (`/accessories/shop/shoes-slippers/`) mixes genders, so the listing link is NC.

### Doors and stockists
- **Doors:** not touched. `doors_pendleton.csv` is from the main thread's browser read: 16 own-door, 14 outlet, 4 affiliates excluded. `own_doors_us` is 16, or 18 if the two mill stores count as full-price.
- **facts_first conflict:** facts_first said 21 non-outlet from a 33-location help-center list. The browser read supersedes it.
- **Stockists:** the locator also lists third-party "Other Retailers". These were not transcribed because the brief said not to attempt the locator, so the file has one row with shop fields NC. **This is not NONE.**

### Craft: proposed 4
- **Owned mills (evidence):**
  - Pendleton OR, built 1895, weaves "all jacquard blankets and fabric for apparel".
  - Washougal WA, acquired 1912.
  - Sources: the fact sheet (modified 2026-06-22) and the timeline. The mills page documents every step from scouring to finishing, and mill tours are offered by request.
- **The brief's "Made in USA" premise does not hold for clothing:** **0 of 45 men's PDPs say Made in USA.**
  - All 9 wool shirts and the 6 wool outerwear pieces read (Forest Twill shirt-jacket plus 5 wool coats) say "Imported of USA fabric" or "Assembled in Mexico/El Salvador of USA made fabric", plus "woven in our American mills".
  - The Wool Shirts category copy says every wool shirt is woven in Pendleton's own mills.
  - Cotton shirts, tees, knitwear (including the lambswool Westerley, from China), canvas and chinos are imported with no mill named.
- **Own-mill share:** own-mill fabric covers roughly 25 of 135 styles, or about 18%. This is a lower bound: all 19 wool-shirt stems plus at least 5 wool coats and the shirt-jacket.
- **Country stated:** 34 of 45 PDPs name the assembly country (76%).
- **No garment maker or third-party mill is named anywhere.**

### Other sections
- **Ownership and founding:**
  - The fact sheet says "privately held, sixth-generation family-owned business". The family is the Bishops: the 1876 Kay–C.P. Bishop marriage, and an About-page letter signed by John Bishop. There are no filings.
  - Founded 1909, Pendleton OR (mill rebuilt). Thomas Kay's Oregon weaving dates from 1863, and the timeline calls Kay "Founder". The brief's facts hold.
  - The mills page heading "160 Years of American Manufacturing" counts from 1863.
- **Tech: proposed 2, on a provisional scale (no tech rubric was issued).**
  - Named fabrics are mostly owned names for Pendleton's own cloths: Umatilla wool, AirLoom merino, Oregon Tweed, DoubleSoft, Big Sky Canvas.
  - Ultrasuede is licensed.
  - 10 of 45 sampled styles (22%) carry one.
- **Quote:** from John Bishop's signed letter on the About page, with an ellipsis because the WebFetch quote limit cut the sentence at 120 characters. His title is not shown.
  - The alternate is the mission statement: "To create quality products that embody craftsmanship, enrich lives and connect generations."
- **Signature product:** the Board Shirt, in the brand's own words "still our bestselling shirt today". Blankets lead the site overall.
- **Lookbook:** none found, only a catalog request.
- **Vinted:** brand id not found in fetched pages (NC).
- **Grailed:** /designers/pendleton exists.
- **B Corp:** the directory did not render (NC).
- **GOTS:** NC.


## Red Wing


**Status: partial.** Cells left `NC`: `own_doors_us`, `own_doors_world`, `search_url`, `tech_share_of_range`, Vinted, B Corp and GOTS. About 42 WebFetch calls were made, one at a time. There were no 429s and no bot checks.

### What was checked
- **Apparel:** `/apparel/mens/` shows "24 Results", read in full. That is 24 tiles, which collapse to 6 styles. One product page was read per style.
- **Footwear, all in default order (no sort URLs):**
  - Heritage: 56 of 56, read as three pages of 24 (`start=0/24/48`).
  - Work: 211 of 211, read as two pages of 120 (`start=0/120`). This includes 37 WORX tiles, which were excluded.
- **Product pages:** Engineer #2966, Excelon #3093, SuperSole 2.0 #2412 and Classic Moc #875.
- **Story pages:** the history, USA Made and Red Wing Way pages.
- **Other sources:**
  - sbfoot.com
  - The redwingshoeco.com home page
  - FranNet (modified 2026-03-13)
  - TCB (2011-01-16)
  - Wikipedia
  - The Grailed designer page

### What the brief got wrong
- **Red Wing is not shoe-only.** It sells own-label men's apparel: tees at $25.99–$44.99 and a hoodie at $55.99.
  - The tee is priced. The other six garments are `NONE`, because there is no polo, shirt, jeans, trouser, knit sweater or outerwear. The hoodie counts as a sweat, not a sweater.
  - The fibre section is 6 styles, all of them cotton-led (5 are 100% cotton, the hoodie is 80/20 cotton/poly).
  - None of these is Heritage apparel apart from the Made-in-USA Classic Logo Tee (its meta says "Heritage").
- **Factories:** besides Red Wing MN and Potosi MO, the brand's own USA Made page names **Clarksville, Arkansas** ("since 2003", new facility).

### Ownership and doors (no change to the doors file)
- **No company-owned count is published anywhere I could reach.**
  - redwingshoeco.com says "Our 500+ retail locations".
  - FranNet says "more than 525" US+CA locations "independently owned and operated by authorized dealers, not franchisees". It gives "over 390" and "over 330" dealer-owned in different sections, which contradict each other.
  - TCB (2011) says 425 stores, "nearly 70 percent" independently owned.
- **`own_doors_us` is `NC`**, on the basis given in the brief. A residual (525 − 390 ≈ 135 non-dealer) is not evidenced and was not filed.
- **Blocked to WebFetch by robots:** redwingshoeco.com `/about` and `/dealership-opportunities`. I did not attempt any other route.
- **WebSearch budget was exhausted for the turn**, so no press search (2020–2026) was possible. A follow-up search could still find a figure, for example in the Star Tribune or a Business Journal.

### Verified
- **Founding:** 1905, Red Wing MN, Charles Beckman ("and other investors"), from the brand history page.
- **Ownership:** private and "Still family owned". Allison Sweasy Gettings became CEO in 2023, "the 4th generation Sweasy".
- **S.B. Foot:** joined Red Wing in 1986 (history page). The USA Made page says "All Red Wing leather comes from our own tannery". sbfoot.com's footer reads © Red Wing Shoe Company, Inc.

### Prices
- **Tee:** $25.99, Short Sleeve Pocket T-Shirt #98468, to $44.99, Classic Logo T-Shirt #97610 (Made in USA, titled Unisex but listed under Men's). Basis `pair`.
- **Shoes:** basis `range`, because Red Wing sells no loafer; the Moc styles are lace-ups.
  - Low: $164.99, Excelon #3093. That is its compare-at; the sale price is $123.74 from Oct 6 to 25. Excelon #3094 shows $164.99 with no sale.
  - High: $549.99, Engineer #2966.
  - Heritage alone runs $259.99–$549.99.
- **WORX was excluded, as in facts_first.** Its tiles read "Worx" and carry the "Red Wing Worx" filter. If Sebastian counts it as a sub-line, the low becomes $109.99 (Essentials #5080). This needs his ruling.

### Craft (proposed 4)
- **Heritage:** all 56 men's Heritage tiles say Made in USA, and product pages credit S.B. Foot leather.
- **Work:** of roughly 175 non-WORX tiles:
  - about 33 are "Made in USA" (with variants)
  - about 28 are "Assembled in USA w/ Imported Components"
  - about 114 carry no origin label; the product page says "Globally Sourced"
- **`made_in_stated_share` of 51%** is 117 of 231 men's footwear tiles stating a US origin. The counts come from a small model's reading of the tiles, so treat them as approximate.
- **On Heritage alone this would be a 5.** Sebastian rules.

### Tech
`proposed_tech` = 3 on the **provisional scale (no tech rubric was issued)**.
- Owned: SuperSole, Traction Tred and ComfortForce.
- Licensed: GORE-TEX, Thinsulate, BOA, SWEN-FLEX and Lenzi.
- The share was not counted across footwear. Apparel is 0 of 6.

### Not reached and other gaps
- **Stockists:** the locator is held by the main thread and was not attempted. It lists about 1,200 Authorized Retailers, mostly work and farm stores. The file has one `NC` row.
- **Vinted:** the search page shows no brand id.
- **B Corp:** the directory did not render.
- **Search URL:** robots-disallowed.
- **Lookbook:** none found. "Fall Styling" is a product listing.
- **Possible style split:** #98455 (Long Sleeve Pocket T-Shirt, Olive) was counted as its own style. It may be a colourway of #98474.


## Stüssy


**Status: partial.** I made about 107 WebFetch calls, one at a time, plus 1 WebSearch, which was refused because the shared per-turn search budget was used up. There were no 429s and no bot checks from stussy.com. Five calls returned a plain fetch error: 2 on `115911-garage-jacket-leather-dark-brown`, plus `/pages/about`, `/blogs/news/tagged/lookbook` and the BoF article. latimes.com was blocked (SITE_BLOCKED). No browser was used. The doors file is the main thread's browser read and is untouched.

### Access and platform
- **Platform:** Shopify, USD storefront, prices shown as `$45`.
- **No bulk feed:** a Bash curl of `/products.json` was refused by the egress proxy (connect_rejected, 403 on CONNECT). WebFetch reaches the feed but cuts it off after about 60k characters, which is about 9 products. So no full feed census was possible.
- **Census method:** the collection listing HTML renders every tile on one page, with no pagination. I read Tees 94 tiles, Sweats 76, Tops & Shirts 91, Knits 37, Outerwear 90, Bottoms 93, Swim 19, Denim 31, Footwear 4 and New Arrivals 118. New Arrivals and Denim added no clothing codes.
- **Fibre method:** each collection's `.atom` feed carries the description, including its `Material:` line. WebFetch's cap gives the first ~23 entries per feed, so I read 17 sub-collection feeds and then single PDPs for the rest. I checked the feed text against the PDP by hand on the Lazy Tee, the Classic Pique Polo and the Waffle Cashmere Sweater. They matched.
- **Search URL:** not tested, so it is NC. `feed_currency_rate` is NC because `Shopify.currency.rate` could not be read without a browser.
- **Summariser refusals:** on two `.atom` reads, WebFetch's summariser refused because it mistook my own prompt for text inside the cut-off page. Rephrasing fixed it. This was not page content addressed to an agent.

### Men's scope (Stüssy is unisex)
- **No men's split:** stussy.com has no men's or women's split except in swimwear (Boardshorts vs One Piece & Bikinis). PDPs say "Unisex" (Lazy Tee, Classic Pique Polo, Standard Shirt, Waffle Cashmere, Beach Slipper).
- **Scope:** all clothing in the six apparel collections plus men's-side swim. The 5 women's swim styles are excluded (one-piece, 2 bikini tops, 2 bikini bottoms).
- **Listing links:** every listing link is the unisex collection, because no men's-only listing exists. Under rules_garment_links, a strict reader may want these as NC.
- **Kids Tee:** "KIDS TEE" (1905205) is a graphic title, not kids' sizing; that is my inference from its listing among adult tees. Not verified on its PDP.

### Census: 183 styles
- **Basis:** 449 colour tiles on first listing, 183 product-code stems. Colourways are separate Shopify products, so the stem is the style and `style_method` is product_code.
- **Suffixed codes** (116599t, 112334u, 113155n, 1915000gd) are kept as their own styles. 1915000gd (Basic Crew Garment Dyed) is 100% cotton against 75/25 on 1915000, so it is a different cloth, not a finish variant.
- **By category:**

| Category | Styles |
|---|---|
| outerwear | 40 |
| tees-polos | 38 (incl. thermals and jerseys) |
| sweats | 31 |
| shirts | 15 (incl. Canvas Work Overshirt) |
| knitwear | 13 |
| denim | 13 |
| trousers | 13 |
| shorts | 11 |
| underwear-swim | 8 (7 swim + the undershirt 3-pack) |
| tailoring | 1 (Junya Sport Coat) |

- **Swim:** 5 board/water shorts, the Performance Wetsuit Top and the SS Rash Guard.
- **Collaborations in the census:** 7 Junya Watanabe styles and 1 Our Legacy Work Shop style. They are kept in the census and tagged in `lines`.

### Fibre: 149 of 183 read (81%)
- **Shares of all 183 styles:** natural 112 (61%), synthetic 33 (18%), cellulosic 4 (2%), not read 34 (19%). The not-read styles are not "undisclosed"; every page opened stated a composition.
- **Not read (34):** 13 graphic and garment-dyed tees, 6 zip hoodies, 5 Junya pieces, Garage Jacket Leather dark brown (fetch error), and 9 shorts, pants and swim pieces.
- **Coverage pattern:** all 25 tee stems read are 100% cotton, which is a pattern only and is not filed for the unread ones.
- **Shape: split.** Outerwear is synthetic-led: of 36 read, 21 are synthetic (nylon or polyester shells) and 15 natural (cotton, leather, wool). Tees/tops, sweats, shirts, denim and knitwear are natural-led.
- **Elastane:** 5 styles. Standard Crinkle Shirt 1%, Half Zip Thermal 4%, Soft Shell 8%, Sport Short 8% and Peak Board Short 12%.
- **Cellulosic:** three TENCEL shirts (Matthew) and a viscose Hawaiian shirt.
- **Lines** (named by the house: Basic Stüssy, Big Ol', Classics, Slim) are tagged in `lines` but not measured.

### Prices (USD, full price; no markdowns seen)
- **Tee: $45–$85, range.** Low is Basic Stüssy Tee $45; many graphic tees are also $45. High is LS Ringer Tee $85 (long-sleeve, in the Tees collection); the short-sleeve-only high would be Lazy Floral Tee $60.
  - Excluded: Tees 3 Pack $38 is "Three pack of tagless undershirts", so it is underwear. Junya tees at $65 are collabs.
  - facts_first's "all tees $45" was a partial read.
- **Polo: $90–$100, range.** Classic Pique Polo $90 and Classic Pique LS Polo $100, both 100% cotton. There is no polo collection, so the link is the Tops & Shirts parent.
- **Dress shirt: $145–$180, range, casual button-ups only.** Low is Standard SS Shirt $145; it is short-sleeve, and the long-sleeve Standard Shirt is $150. High is Standard Crinkle Shirt $180. The Junya Button Down at $725 is excluded.
- **Jeans: $160–$200, range.** New Classic Jean Denim $160 to New Classic Jean Denim Cheetah $200, a 491gsm printed denim. All 100% cotton, so there is no elevated pair.
- **Dress pants: $155, single.** No dress trouser exists. The Uniform Pant ("12oz Japanese cotton twill", zip fly) stands in as the chino. The Beach Pants have elastic waists and the leather and suede pants are not chinos, so all are excluded. The Pants listing also mixes jeans and sweatpants.
- **Sweater: $130–$225, pair.**
  - Low is Lightweight Striped Sweater $130, a "Ribbed crewneck" in 72% linen / 28% cotton.
  - High is Waffle Cashmere Sweater $225, a "Relaxed fit crewneck sweater" in 100% cashmere.
- **Outerwear: $185–$1,100, range.**
  - Low is Lightweight Hooded Jacket $185, tied with the Lightweight Mock Jacket and the Waxed Cotton Beach Shell. The Canvas Work Overshirt at $170 is a shirt-jacket, so it is excluded.
  - High is Leather Duster $1,100. Leather is not on the elevated list, so this is a range, not a pair.
  - Collabs excluded: Junya $1,810–$3,380 and Our Legacy Fireman $2,190.
- **Shoes: $65, single.** The Beach Slipper is a Stüssy-branded rubber flip-flop with no loafer. The Our Legacy Work Shop boots ($500 and $590) are collabs, so they are excluded. The Footwear listing mixes both.

### Doors and stockists
- **Doors:** not touched. They come from the browser read: 4 US chapters and 2 US DSM concessions; 29 chapters and 5 DSM worldwide. `own_doors_us` is 4 and `own_doors_world` is 29.
- **Operator not stated:** the directory does not say who operates any door.
- **Santa Ana:** the meta description calls it the "Stüssy Archive store".
- **Stockists:** the brand lists no third-party stockists on the Chapter Directory, so the stockists file has one row with `none`. Other stockist pages were not searched.

### Tech, craft, origin
- **Tech: proposed 2, isolated (provisional scale; no tech rubric issued).**
  - Named licensed tech: GORE-TEX (Guide Shell), PrimaLoft Gold (Rally Insulated Jacket fill), CORDURA (MA-1 flight satin) and TENCEL (3 shirts). That is 6 of 149 read styles, about 4%.
  - "Italian majo-tech soft shell" is not confirmed as a trademark.
- **Craft: proposed 1.**
  - Every PDP and feed description read says only "Imported", so `made_in_stated_share` is 0. No maker or mill is named, no facility is claimed, and there is no about or heritage page.
  - The only sourcing words are generic: "Italian cotton canvas", "Italian wool", "Japanese cotton twill".
  - PDPs give fabric specs (oz, gauge, pigment/garment dye), which is not documented making.
- **Founded:** Wikipedia says "early 1980s" by Shawn Stussy, with Laguna Beach in the infobox. **The brief's 1980 is not verified, so `founded_year` is NC.**
- **Frank Sinatra Jr.:** confirmed as Stussy's partner, and Wikipedia says he is "no relation to the singer". The brief's wording ("Shawn Stussy's former partner Frank Sinatra Jr.") is right, but a reader may assume the singer's son, so the record says otherwise.
- **Owner: private, the Sinatra family.**
  - Wikipedia: "In 1996, Stussy resigned as president and Sinatra bought his share", and "As of 2017, the Sinatra family owns the brand".
  - These cite BoF (3 Jun 2015) and the LA Times (10 Jan 1996). **Neither primary could be fetched, so ownership rests on a secondary source.**
- **Operating entity:** "Stussy Inc." / "Stüssy, Inc.", 17426 Daimler Street, Irvine CA 92614, from `/pages/legal`.

### Mark
- **"Stüssy"** in the site title, og:title, header and PDP copy.
- **"STÜSSY"** in the footer: "© 2026 STÜSSY".
- **"Stussy"** (no umlaut) in legal text: "Stussy is a registered trademark…"
- The canonical key "Stüssy" matches the title form.

### Not reached (NC)
- **Search not available:** WebSearch was exhausted on the first call, and no stockist, quote or B Corp search was possible.
- **Quote:** NC. The brand site has no about page, and the news posts read carry no attributed quotations.
- **Lookbook:** NC. `/blogs/news` shows no seasonal lookbook; `/blogs/features` did not render and the lookbook tag URL errored.
- **Vinted:** NC. `/brand/stussy` served a generic catalog page with no brand id.
- **Grailed:** `/designers/stussy` resolves (title "Stussy Clothing | Grailed"), but listings did not render.
- **B Corp and GOTS:** NC. The B Lab directory did not render results.
- **Pronunciation:** "STOO-see" is common usage and not sourced from the brand. A reviewer may prefer NC.

### Contradictions with facts_first and the brief
- **Outerwear count:** facts_first said "Outerwear collection had only 6 products". The listing shows 90 tiles and 42 codes; the earlier check probably saw a default-limited JSON page.
- **US doors:** the worklist claim "own stores in NYC, LA, SF, Honolulu" is wrong on SF. The fourth US chapter is Santa Ana. This was already flagged.
- **Founding year:** the brief's 1980 is not confirmed (see above).


## Supreme


**Status: partial.** I made about 58 WebFetch calls and 1 WebSearch. The WebSearch was refused because the per-turn search budget was used up, so everything after that came from direct fetches. There were no 429s and no bot checks.

Pacing slip: six tee PDP fetches went out in a single parallel batch. Every other fetch was made one at a time.

The doors file is the main thread's browser read of supreme.com/stores, and I did not touch it.

### Access and platform
- **Platform:** us.supreme.com is Shopify, judging by its `meta-shopify-*` tags.
- **Feeds all failed:** `/products.json`, `/products/<handle>.json`, `/sitemap.xml` and `/search?q=tee` all gave fetch errors. A Bash curl to us.supreme.com was refused by the egress proxy (CONNECT 403).
  - So there was no feed census, and `feed_currency_rate` and `search_url` are `NC`.
- **Category pages:** `/collections/all` renders 0 tiles, because it is script-only. The only readable listing was `/pages/shop`.
- **supreme.com:** the previews (`/previews/fallwinter2026`), the about page and the lookbook bodies are script-rendered. Only titles and meta came through.

### Drop model: what was read
- **One week only:** `/pages/shop` showed 39 tiles on 2026-10-10. That is the current week of FW26; image filenames carry "FW26".
- **No full season:** the season range is not on the shop. The FAQ says "We are only offering a select group of items through the web shop at this time" and "Most of our items do not have set release dates."
- **Previews:** the FW26 preview page exists but renders no items or prices without script. **No preview prices were obtainable.**
- **Prices and fibre are therefore one week's sample, not the season.**

### Prices (USD, all full price; no compare-at prices seen)

| Garment | Basis | Price | Notes |
|---|---|---|---|
| Tee | range | $44–$88 | Low: Sharp, Growl, Tears and Pills Tees, all $44. High: Milan Sequin S/S Top $88, a crewneck jersey top with sequin decoration. The plain-tee high is Script Tee $58. Excluded: Supreme/Hanes Tagless Tees 3-pack $30 (undershirt, collab). |
| Polo | NC | – | None this week. |
| Dress shirt | single | $168 | Quilted Lined Flannel Snap Shirt: casual, snap front, lined. A weak stand-in. |
| Jeans | single | $298 | Slim Straight Selvedge Jean, "Made in Japan". |
| Dress pants | NC | – | No dress trouser or chino this week. The Painter Pant ($178, utility) and GORE-TEX Cargo Pant ($298) are not chinos. Sebastian may rule otherwise. |
| Sweater | single | $178 | Wolves Sweater, "Wool", jacquard. The neckline is not stated. |
| Outerwear | range | $238–$498 | Micro Down Half Zip Hooded Pullover $238, then Faux Shearling Lined Bomber $288, then GORE-TEX N-2B Jacket $498. |
| Shoes | NC | – | The only footwear is the Supreme®/Nike® Air Force 1 Low, $124, "Made exclusively for Supreme". It is a collaboration, so I did not file it as own-label. **Ruling needed: NONE or the AF1.** |

- **Outerwear exclusion:** Supreme/Rita Ackermann Hooded Work Jacket $398 is a collab, so it was excluded.
- **Collaborations are never used as a high.** Rita Ackermann, Hanes and Nike pieces were all excluded.
- **Listing URLs are all NC.** There are no men's or category pages, and the range is unisex and men's-centred.
- **facts_first said "3 jackets"; the shop now shows 4 outerwear pieces.** facts_first's $44 tee and $498 outerwear reproduce.

### Fibre: 27 clothing styles, 23 with composition (85%)
- **Styles:** 27 clothing PDPs read. The style code is the Shopify handle. `colourway_ratio` is NC: each PDP shows one colour, and the other colourways were not read.
- **Composition wording:** compositions are words, not percentages.
  - "All cotton" is filed as 100% cotton.
  - "Poly", "Pertex poly", "GORE-TEX … poly ripstop" and "Wool" are named fibres with no %, so they are filed with `lead_pct` ND, following the Bally precedent.
  - The 3 hoodies and the sweatpant say only "Brushed-back fleece", which names no fibre, so they are undisclosed.
- **Shares of 27:** natural 18 (67%), synthetic 5 (19%), cellulosic 0, undisclosed 4. No elastane anywhere.
- **Shape:** `one`. No category has ten or more styles that are synthetic-led. Tees-polos (10) is natural-led and outerwear is 2–2. Shorts (1, a collab poly soccer short) is the only synthetic-led category.
- **Lines:** only collaboration lines (Supreme/Rita Ackermann 4, Supreme/Hanes 2). None reaches 5, so none was measured.
- **Swim:** 0 styles. The 2 Hanes underwear packs are in underwear-swim.

### Tech (provisional scale; no tech rubric was issued)
- **Named tech, all licensed:** GORE-TEX (N-2B jacket, cargo pant), Pertex (micro down), 3M Thinsulate (2 jackets) and 3M Reflective.
- **Share:** 5 of 27 styles (19%).
- **Proposed: 3.** This is biased by an outerwear-heavy FW week, so 2 is defensible on a full season.

### Craft
- **Made-in:** 1 of 27 clothing PDPs states a country (the jean, Japan), which is 4%.
- **Makers, mills, facility:** none named and none claimed. Process is given at spec level only.
- **Heritage:** the site carries only "EST 1994. NYC."
- **Proposed: 1.** A 2 is arguable on the single Made-in line.

### Origin and ownership
- **Founded 1994, New York City:** **confirmed** from the brand's own meta "EST 1994. NYC." and from Vice (2018-11-16): it "opened on Lafayette street in 1994".
- **Founder James Jebbia:** **confirmed by press.** Vice says "Its founder, James Jebbia", and Wikipedia agrees.
- **Owner EssilorLuxottica since 2 Oct 2024:** **confirmed** by EssilorLuxottica's own release on GlobeNewswire, 2024-10-02. It says the company "has successfully closed" the acquisition from VF, with "an aggregate base purchase price of $1.5 billion in cash".
  - The annual report was **not read**: the essilorluxottica.com investor and newsroom pages are script-rendered, and there was no search to find the PDF.
  - Wikipedia's "completed in July 2024" is wrong. July 2024 was the announcement.
- **WWD gave a fetch error and Vogue was SITE_BLOCKED.**

### Other sections
- **Lookbook:** lookbook/46 is the "Fall/Winter 2026 Lookbook". The site nav still links lookbook/44 (FW25), and lookbook/45 is SS26. Whether it is men's is NC, because the images are not readable.
- **Grailed:** the designer page resolves ("Supreme Clothing | Grailed", canonical /designers/supreme).
- **Vinted:** no brand id found from /brand/supreme or the catalog search, so NC.
- **B Corp:** NC; bcorporation.net gave a fetch error. **GOTS:** NC; not checked.
- **Quote:** Jebbia, from the 2010 Rizzoli book "Supreme", as quoted by Vice (2018). It is verbatim, re-checked on a second read.
- **Signature product:** the Box Logo Tee, per press (Wikipedia). It is not in this week's shop, so its URL is NC.
- **Stockists:** the brand lists none. supreme.com/stores lists own stores only.

### Contradictions with the brief and facts_first
- **US doors are 6, not 5.** facts_first used 2022 press; there is a new Miami store, and LA is listed as West Hollywood.
- **The worklist claim "NYC, LA, SF, Chicago" omits Brooklyn and Miami.**
- **The brief asked for preview prices.** The previews render nothing without script, so this cannot be done by fetch. A browser read of supreme.com/previews/fallwinter2026 would close the season range, as well as polo, dress pants and lookbook gender.


## The North Face


**Conditions.**
- I read with WebFetch only. WebSearch was exhausted for the turn (one call refused), so no searches.
- The proxy refuses curl to www.thenorthface.com (CONNECT 403), so no feed or sitemap was pulled.
- Site search (`/en-us/search?q=`) and the SEC EDGAR browse page are ROBOTS_DISALLOWED to WebFetch. I used no other route to either.
- No 429s and no bot checks from fetches. I made about 86 fetches.
- **Pacing slip:** one pair of product pages (Tri-Blend Pocket Tee and Adventure Tee) went out in parallel. Every other fetch was made one at a time.
- I did not attempt the store locator, as briefed. `doors_the_north_face.csv` is left header-only.

### What was checked

**Store.** thenorthface.com/en-us is the US store, in USD; VF footer, storeId 7001, not Shopify. `search_url` is `NC` because the search path could not be tested (robots-disallowed to WebFetch).

**Grid limit.** Category grids server-render 48 tiles, but only 12 of them carry a name and price. No sort parameter was found. So every high below is the **highest seen**, not a proven top of range.

**Prices.** All are list or compare-at prices; exact figures are in the product cells.

| Garment | Basis | Low | High | Notes |
|---|---|---|---|---|
| Tee | range | $35, Evolution TNF Diamond tee | $85, Summit Series High Trail SS—Graphic | The high is listed in Men's T-Shirts. |
| Polo | range | $55, Adventure Polo | $65, LIGHTRANGE Packable Polo | Both are compare-at prices; the Adventure Polo grid tile showed $55 at full price. |
| Dress shirt | range | $90, Packable SS Shirt | $100, Mountain Falls Flannel | TNF makes casual button-fronts only. The $90 is a compare-at price on a "Final Sale" item. Snap-front Beta, Open Range Fleece and Open Range Insulated shirts are excluded. |
| Jeans | NONE | | | See below. |
| Dress pants | range | $90, Sprag 5-Pocket | $210, Summit Off Width | No dress trouser or chino; woven hike/climb pants read. Rain, snow, down and FUTURELIGHT shell pants are excluded. |
| Sweater | NONE | | | See below. |
| Outerwear | range | $120, Fontanales Wind Jacket | $1,340, Summit CLOUD DOWN AMK Parka | **The high tile is marked Sold Out — please rule.** The next highest are the McMurdo 2L GORE-TEX Down Parka at $950 (facts-first, 10-08) and the Summit Mountain GORE-TEX Pro Jacket at $900 (PDP, in stock). AMK is a Summit Series kit, not a collaboration. |
| Shoes | range | $45, Base Camp Slides III | $550, Summit Series Verto SA GORE-TEX Boots | The high has unisex sizing and sits on a Sale path but shows no compare-at. There is no loafer. |

Listing links:
- Polo and dress shirt share the Shirts & Polos parent category, which has 11 items.
- The T-shirts listing includes unisex graphic tees.

**Jeans and sweater are NONE on inference.** This is not a search result:
- The 29-item Pants grid has no denim.
- The 39-item Hoodies & Sweatshirts grid has no knit sweater.
- The men's navigation has no denim or sweater category.

Search could have settled this, but it was unavailable. Downgrade both to `NC` if you prefer.

**Fibre: a 56-style documented sample (briefed about 80).**
- I stopped early to stay within the fetch budget for the other sections.
- Styles were read one product page at a time, across categories:
  - tees and polos: 14
  - outerwear: 17
  - sweats and fleece: 9
  - shirts: 5
  - trousers: 6
  - shorts: 4
  - baselayer: 1
- The sample is not random.
- Shop All Men's states 539 products, including footwear and accessories. Men's clothing was not censused, so `styles_total` is `NC`.

Results:
- **Fibre split:** 12 natural (21%) and 44 synthetic (79%), with 0 cellulosic.
- **Stretch:** 15 styles have elastane on the main line.
- **Shape is `one` (synthetic).** No category is natural-led:
  - Sweats are 4 natural to 5 synthetic.
  - Shirts are 2 to 3.
  - Tees are 5 to 9.
  - Outerwear is 0 of 17.
- **Cotton:** all of it is "Climate Conscious Cotton", found in the Evolution graphics, hoodies, flannel and rugby.
- **Wool:** appears only in the Summit Pro Baselayer (62% polyester, 38% wool).
- **No product page states a country of origin.**

Lines in the sample:
- **Summit Series** (9 styles): all synthetic except the wool-blend baselayer, where polyester still leads.
- **Evolution** (5 styles): cotton-led.

**Swim = 0.** The Shorts page copy says TNF "doesn't offer true swimwear."

**Doors.**
- VF 10-K for FY ended 28 Mar 2026 (accession 0000103379-26-000030): "286 VF-operated stores" for The North Face.
- VF total is 1,080 stores, about 56% of them in the US, but not split by brand.
- No US split and no outlet split for TNF, so `own_doors_us` and `own_doors_world` are both `NC`, with this basis in `doors_basis`.

**Tech.** Scale is provisional; no tech rubric was issued.
- **Owned (™ on page):** FUTURELIGHT ("our 100% recycled, breathable-waterproof FUTURELIGHT fabric"), DryVent, ThermoBall, WindWall, FlashDry, LIGHTRANGE, Heatseeker, DotKnit.
- **Licensed:** GORE-TEX (2 styles) and Pertex (2 styles).
- **Share:** 37 of 56 styles (66%) carry a named tech, about 63% of them owned.
- **Proposed 4.** A 5 is arguable, because owned tech is on most of the sample, but much of it is finishes (FlashDry, WindWall) rather than fabric R&D.
- **ThermoBall:** the product page names no PrimaLoft partner, so I recorded it as TNF's own on page evidence. The PrimaLoft co-development history is not verified here.

**Craft: proposed 2.**
- No owned facility: the 10-K cites about 216 independent contractor facilities in about 24 countries.
- No named makers or mills.
- 0% made-in stated.
- Founding is dated and placed (1966, San Francisco).

### What was not reached

- **Stockists.** The locator has an "Online Dealers" tab and a dealer filter, but it is blocked by the human check. The stockists file has one `NC` row saying so.
- **Vinted brand id.** The catalog page exposed none.
- **B Corp.** The B Lab directory is script-rendered, so this is `NC`. VF is not known to be certified, but that was not confirmed.
- **GOTS.** Not checked (`NC`).
- **Lookbook.** None was linked from the homepage, so it is filed as `no`. The site runs seasonal shop pages ("New for Fall", FW26 assets), not a lookbook.
- **Other pages:**
  - The FUTURELIGHT innovation page errored.
  - The factory list was not found; the suppliers page links only to the VF Modern Slavery Statement.

### Contradictions with the brief and facts-first

- **Founders.** The brief says Douglas and Susie Tompkins. The brand's our-story page names only "Doug Tompkins", in San Francisco, 1966. Susie Tompkins is not confirmed from a brand page; the `founders` cell says so.
- **Store count.** Facts-first had "approximately 285" stores from the FY2025 10-K. The FY2026 10-K says 286.
- **Wordmark.** The site title writes "The North Face®".

### Quote

- **Filed:** the opening of the mission on the About Us page, truncated with an ellipsis (the full sentence was not extracted).
- **Alternative**, from the our-story page: "Named for the most challenging side of the mountain".


## Tod's


**Status: partial.** ~45 fetches, one at a time, no 429s. WebSearch was exhausted (turn budget used up), so everything came from direct fetches.

### Blocked (exact failures, not worked around)
- **tods.com** returned `CLIENT_ERROR: There was an error while fetching` on `/us-en/` and on the T-shirt PDP `/us-en/T-shirt-in-Jersey/p/X5MB3505800VDNB001/`.
- **todsgroup.com** returned the same error on `/` and `/en/group/history`.
- **SITE_BLOCKED:** nytimes.com, newyorker.com, voguebusiness.com, vogue.com, reuters.com, telegraph, glitz.paris.
- **Client errors:** wwd.com, ilsole24ore.com, businessoffashion.com/people, hollywoodreporter.com, fashionunited and fashionnetwork site search, the bcorporation.net profile, and the Vinted API.

### Used, not redone
- **Doors** (`doors_tod_s.csv`, browser): left as is. own_doors_us = 8 boutiques, plus 2 Bloomingdale's 59th St concession units.
- **Prices** (`tods_prices_browser.json`): mapped as below. Filing calls are in the row note.
  - **Shoes:** the Gommino pair, $775 to $1,145, is filed as the staple.
    - The dearest regular loafer is the $1,295 non-Gommino "Loafers in Leather".
    - **Sebastian to rule** which belongs in shoes_high.
  - **Dress pants:** chinos, $745 to $775. Their URLs were not captured in the browser read, so the URL cells are NC.
  - **Dress shirt:** the $645 high is a mandarin collar, not a collared dress shirt.

### Not reached
- **Fibre.** No product page could be read, so the styles file is header only and every fibre cell is NC.
  - The browser listings show 148 products across 6 categories, with colourways not collapsed.
- **search_url, tech, lookbook, made-in share, named makers and mills, process, quote, Vinted id, B Corp, GOTS:** all NC.
- **own_doors_world:** NC.

### Found
- **Ownership.**
  - Tod's is no longer on Borsa Italiana's A–Z list (2026-10-10).
  - L Catterton lists Tod's as a current investment, oddly under its Asia platform.
  - The 54/36/10 Della Valle / L Catterton / LVMH split rests on Wikipedia's account of the Feb 2024 deal. The final stakes and the delisting date are unread in a primary source.
- **Craft.**
  - **Casette d'Ete factory:** Time, 2006-03-08.
  - **Arquata del Tronto plant (2017) and "7 shoe + 2 leather-goods plants":** it.wikipedia, uncited.
  - **Brancadoro:** the only link found is Diego Della Valle's residence. No plant was found there, so the brief's "Brancadoro factory" is unconfirmed.
  - **Proposed score: 4, low confidence.**
- **Founding.**
  - Filippo Della Valle, cobbler, is confirmed by both Time and Wikipedia.
  - The year is inconsistent: Wikipedia's text says "late 1920s", its infobox says 1920, and it.wiki says "early 1900s". It is filed as NC.
  - Time says Dorino set up shop in Casette d'Ete in the 1940s.
- **Grailed:** https://www.grailed.com/designers/tods is verified.

### Contradictions and flags
- **Labour investigation.** Milan prosecutors opened a caporalato probe into Tod's and three managers and asked for a 6-month advertising ban (Il Foglio, 2025-11-22). The alleged exploitation was at second-level Chinese subcontractors.
  - The earlier request for judicial administration was rejected; Cassation sent it to Ancona.
  - This bears directly on the craft claim.
- **CEO.** John Galantic was CEO from Sep 2024 and reportedly left in May 2026. This is per Wikipedia citing Bloomberg, which was not read.
- **facts_first** called the shop "not clothing-led". Men's ready-to-wear is sold online in six categories.
- **Tech:** no rubric was issued, and the tech cells are NC.

### Browser read 2026-10-10
Read in Chrome (US store https://www.tods.com/us-en/, SAP Commerce-style `/c/` and `/p/` paths, not Shopify), one page at a time. There was no cookie banner and no bot check. Composition is in the rendered PDP text ("Item composition: …", then "Made in …", then "MOD. <code>"). It was validated on every page read, not sampled.

- **Census.** The six men's RTW grids state 5 + 13 + 13 + 22 + 34 + 61 = 148 tiles. Outerwear needed two "view more" clicks.
  - There are 138 unique product codes. Ten tiles are cross-listings: 6 knit polos sit under both Polo and Knitwear, 2 leather/suede overshirts under both Shirts and Outerwear, and 2 colourways repeat.
  - **Style = product code minus the 4-character colour suffix (model + fabric code): 97 styles.** On the numeric model stem alone there would be 90 styles. Same-model fabric variants differ in composition, so they are kept apart: the chino YIN is 97/3 cotton/elastane at $745, while XZC is 100% cotton at $775.
- **PDPs read: 97 of 97 styles.** 96 state a composition. The 97th, "Mandarin Collar Bomber Jacket in Double Fabric" (X1M11522240XIM), redirected to Men/Ready-To-Wear/View-all on two tries. It is filed as ND/undisclosed.
- **Categories (standard).** Each style is assigned by garment:
  - Knit polos go to tees-polos.
  - Leather/suede overshirts go to outerwear.
  - Blazers (3) go to tailoring.
  - Jeans and 5-pocket denim (7) go to denim.
  - Bermuda (1) goes to shorts.
  - The technical "Waistcoat"/gilets stay in outerwear.
  - Resulting counts: outerwear 46 · knitwear 15 · tees-polos 11 · shirts 7 · trousers 7 · denim 7 · tailoring 3 · shorts 1.
- **Main fibre.** Pashmy/suede/nappa jackets read the shell ("100% ovine/lambskin/calfskin leather") as leather. "Ovine fur" (Castello shearling) is other-natural, with lead 100 because the material is named without a percentage. "41% virgin wool, 38% wool" is summed as wool 79.
  - Elastane in knit hems is trim and not counted: Brera, Coach and the Pashmy bombers carry 2–4% there.
- **Lines** (title-series): Pashmy has 21 styles and all are leather-led, so it is all-natural. T15 Wool has 6 styles, all 100% wool, so it is also all-natural.
- **Synthetic-led: 11 styles, all outerwear.** They are 6 in technical fabric (64/21/15 polyamide/PU/elastane, or the 80/20 car coat), 3 in soft-touch microfiber (70/30 polyester/polyamide), 1 technical canvas, and 1 hooded down (51/49 PA/PES).
  - Every other category is 100% natural-led. No cellulosic leads anywhere; lyocell appears only in the 51/49 cotton/lyocell herringbone shirt.
  - 67 of 96 composed styles are a single fibre, 20 of them 100% cotton.
- **Made-in.** 94 of 96 PDPs read say "Made in Italy". The two leather overshirts (X1M04520510ZYJ, X1M04520320XZT) state no country.
  - **Shoes:** four Gommino PDPs all say "Made in Italy":
    - Gommino Loafers in Suede, XXM22L00010RE0S818, $775
    - Gommino Loafers in Leather, XXM22L00010SDLB999, $1,145
    - City Gommino Loafers in Leather, XXM76L0KM10D90B999, $975
    - Boat Gommino Bubble Loafers in Suede, XXM52K05300RE0B211, $925
  - The first two also read "Exposed handmade stitching" and "Leather lining and insole".

### full_tod_s.csv, old → new (NC cells only, plus two placeholder product cells)
- dress_pants_low_product: "cotton chino (title not captured…)" → Chino Trousers in Cotton
- dress_pants_low_url: NC → https://www.tods.com/us-en/Chino-Trousers-in-Cotton/p/X3M81524820YINB601/ ($745; the NEW COLLECTION colourway; S809 and B004 are tagged RUNWAY)
- dress_pants_high_product: placeholder → Chino Trousers in Cotton
- dress_pants_high_url: NC → https://www.tods.com/us-en/Chino-Trousers-in-Cotton/p/X3M81524820XZCB002/ ($775)
- styles_total NC → 97
- styles_with_composition NC → 96
- natural_pct NC → 88 (85/97)
- synthetic_pct NC → 11 (11/97)
- cellulosic_pct NC → 0
- spandex_styles NC → 7. Of these, 6 are at ≥5% (the technical-fabric outerwear at 15–20%); the other is the 3% chino YIN.
- shape NC → one. Outerwear has 46 styles and 34 of them are natural-led; no category of 10 or more is synthetic-led.
- natural_categories NC → ["Outerwear", "Knitwear", "Polo; T-Shirt"]
- synthetic_categories NC → []
- colourway_ratio NC → 138/97
- style_method NC → product_code
- swim_styles NC → 0
- swim_share_of_range NC → 0
- mens_styles_excl_swim NC → 97
- made_in_stated_share NC → 98 (94 of 96 PDPs read)
- Men's listing URLs per garment were already filled from the earlier browser read, and they were re-confirmed live. Status stays partial because other cells (tech, lookbook, quote, etc.) are still NC.
- styles_tod_s.csv: header only → 97 rows. The URL is the colourway read; colourway counts are in `note`.


## Tommy Hilfiger


**Status: partial.** This is the first full record; there was no earlier `full_` file.

**How the run went**
- I made 106 WebFetch calls with no 429s and no bot checks.
- **Pacing breach.** Five tee PDP fetches went out together in one batch. Every other fetch went out one at a time.
- **WebSearch was exhausted** (the turn-wide limit was reached on my first call), so I worked from direct fetches only.
- **Bash route closed.** curl to usa.tommy.com was refused by the egress proxy (CONNECT 403), so the sitemap and feed route was closed. I did not work around it.
- **Doors.** I did not attempt the locator, per the brief. The main thread has since written `doors_tommy_hilfiger.csv` (139 rows) and `doors_summary_tommy_hilfiger.txt`. I left both untouched. `own_doors_us` stays NC for the main thread to set from its read.

### Store
- **Store read:** usa.tommy.com/en. Salesforce-style listings, prices in $.
- **Promotion running:** "40% off your purchase" plus a VIP extra 25% off $250+. Every tile read was 30–75% off.
- **Listings:**
  - 16 colourway tiles per page, paged with `?start=`.
  - `pmin`/`pmax` price filters work.
  - `srule=price-low-to-high` sorts on the **sale** price, so floors are near-proven, not proven.
- **Men's Clothing count:** 1,715 tiles.
- **Search:** `/en/search?q=` returns results for "cashmere sweater" (10) and "swim trunk" (40). An empty query was not tested.

### The "Factory" label — please rule
On usa.tommy.com, "Factory" sits above the title on many styles in the main men's navigation, not only in `/en/factory`. Examples:
- the hero "Prep, Perfected" Regular Fit Stretch Pique Tommy Polo (78JA568);
- a New York Label tee (MW42675, verbatim check of the text before the title);
- THFlex dress shirts and chinos;
- the Classic Crewneck Sweater.

It reads as a channel tag on main-range product. I therefore **counted** Factory-labelled styles. That is the opposite of the Calvin Klein gap-fill, which excluded them.

If Sebastian rules to exclude them, the figures change as follows:

| Garment | Filed | If Factory is excluded |
|---|---|---|
| Tee low | $39.50, Everyday T-Shirt 78JA560 | $44.50, Hilfiger 1985 Athletic Logo T-Shirt XM05718 (no label; its XM prefix is shared with Factory styles) |
| Tee high | $99.50, New York Label Cotton-Linen T-Shirt | $74.50, Varsity Stripe Interlock T-Shirt MW44918 |
| Polo low | $69.50, 78JA568 | $74.50, Regular Fit Tommy Wicking Polo 78JA019 |
| Dress shirt low | $99.50 | $99.50 (01T0590 carries no label; no change) |
| Jeans low | $89.50 | $99.50, Tommy Jeans Slim Bootcut DM23650 (tile only) |
| Dress pants low | $89.50 | not read |
| Sweater low | $84.50 | not read |

### Prices (compare-at only; exact figures are in the row note)
- **Tee:** range $39.50–$99.50. Collaboration tees excluded: Cadillac F1 at $99.50 and $89.50, SailGP.
  - Second-product check: the Everyday T-Shirt is $39.50 on every colour, and so is the Everyday Pocket Tee.
- **Polo:** range $69.50–$179.
  - The listing mixes sweater polos. The high is the New York Label Performance Sweater Polo (53% recycled polyester / 47% lyocell).
  - The lowest cotton piqué is the floor.
- **Dress shirt:** the Dress Shirts category is complete at 14 tiles, and all are THFlex at $99.50, so low = high.
  - Casual oxfords start at $69.50 (78J9041), but the brand makes dress shirts, so the category was used.
- **Jeans:** range $89.50–$179.
  - The 78JA146 PDP shows two price blocks: $99.50 and $89.50. The page metadata says $89.50, and five other jeans tiles are $89.50.
- **Dress pants:** there is no dress-trouser or suit category. Suits & Blazers rendered empty ("Something went wrong").
  - Chinos/pants are used. Range $89.50–$179 (Relaxed Twill Pant, 98/2 cotton/elastane).
  - The $189 SailGP pant (a collaboration) is excluded.
  - **Flag:** 78JA569 shows $79.50 compare-at on some colourways and $89.50 on others. $89.50 is filed; please rule.
- **Sweater:** no men's majority-cashmere or other elevated crewneck was found. The cashmere search returned only a 5% cashmere sweater polo.
  - Basis is therefore range, $84.50 (Classic Crewneck, 100% cotton) to $349 (Fair Isle Wool-Blend Zip Cardigan, 80/20 wool/nylon).
  - The dearest crewneck is $189.
- **Outerwear:** range $99.50 (Tommy Jeans Classic Denim Jacket) to $699 (Mixed-Media Varsity Jacket: wool-blend body, leather sleeves).
  - Excluded: the $1,449 New York Label Shearling Aviator (shearling, and also labelled "Runway"). Also the $1,339 Double-Breasted Coat TQ002983, which its own PDP calls "A limited-edition style from our Spring 2025 runway collection."
  - The $699 Relaxed Suede Moto ties the filed high but is out of stock.
  - The listing mixes vests, blazers and shirt-jackets. The $199 Garment-Dyed Utility Shirt Jacket is not counted as outerwear.
- **Shoes:** pair of loafers, $149 (Flag Hardware Driving Loafer; PDP read) and $199 (Shiny Leather Loafer; tile only).
  - The Dress Shoes listing is complete at 12. Per the 10-K, MBF Holdings licenses Tommy Hilfiger footwear in the US and Canada.

### Fibre (documented sample, not a census)
- **The sample.** 60 men's styles across 10 categories, all PDPs read on 2026-10-10. They were chosen from the listing pages read (high-to-low, low-to-high and default), not at random.
  - The brief asked for about 80; the fetch cap stopped the sample at 60.
- **Result.**
  - Natural-led 52 (87%), synthetic-led 7 (12%), cellulosic-led 0, undisclosed 1. The undisclosed one is the Relaxed Suede Moto: out of stock, "supple suede" in the copy and no composition line.
  - Elastane on 14; 5% or more on 3 (Varsity Interlock Tee 13%, Padded Tech Shirt 15%, Runway Coat 5%).
- **Synthetic-led styles:** NYL Performance Sweater Polo, Padded Tech Shirt, Tommy Jeans Check Overshirt (100% recycled polyester), Down Parka shell, Ripstop Windbreaker, Tommy Jeans Chicago Windbreaker, Swim Trunk.
- **Cellulosics:** they appear only as secondary fibres. Lyocell is 47% of the NYL Performance Polo and 45% of the NYL Quarter-Zip; viscose is 30% of the Lardini blazer.
- **Country of origin:** 60 of 60 say only "Imported".
- **Not filed:** shape, styles census, colourway ratio and swim count. The swimwear listing shows 32 tiles; 9 distinct styles were among the 16 visible.

### Sections 6–13
- **Tech: proposed 2.** This is a provisional scale; no tech rubric was issued.
  - THFlex (the house's own name) appears on 3 of 60 styles: dress shirts and a chino.
  - One shirt cites an unnamed "special flex technology".
- **Craft: proposed 1.**
  - No owned facility. The 10-K says all ~1,000 factories are independent; this is company-wide.
  - No makers named on any PDP.
  - One mill named: "the renowned Lardini mill in Italy" on a Factory-label blazer. Lardini is better known as a tailoring maker, so treat this as weak.
  - No process documented; origin is "Imported" on every PDP.
- **Founding.** 1985, New York City, Tommy Hilfiger.
  - The PVH brand page and the FY2025 10-K say "since 1985" and "Originally established in New York City"; the usa.tommy.com meta also says "since 1985".
  - **Contradiction with the brief:** the brand's own heritage page (`/tommy-hilfiger-heritage.html`) gives **no** founding year or place. It dates only his first store, the People's Place, to 1969. The 1985/NYC fact therefore rests on PVH pages, not on tommy.com body copy.
- **Ownership.** PVH Corp., per the FY2025 10-K (fiscal year ended 1 Feb 2026). It acquired Tommy Hilfiger B.V. in May 2010.
- **Lookbook.** NYFW runway "Spring 2027" at The Plaza: 10 looks, with a men's leather jacket linked, so filed as mixed. The Fall Collection page is a landing page, not a lookbook.
- **Quote.** Tommy Hilfiger on the Tommy Stories page (verbatim, undated). Second option, from the heritage page: "That was the best learning experience I ever had, it was my MBA" (about his early bankruptcy).
- **Signature product.** The stretch piqué polo is a judgement; the cable-knit sweater is the alternative. The evidence is in the row.
- **Grailed.** /designers/tommy-hilfiger exists.
- **Not established (NC):**
  - Vinted: the brand page exposes no id.
  - B Corp: the B Lab directory fetch errored.
  - GOTS: not checked.

### Flags
- **Embedded instructions on two PDPs.** WebFetch reported that FM06089 (driving loafer) and MW42701 (wool shirt) carried "an embedded instruction" about how to format the report. It was ignored, and nothing was acted on.
- **facts_first:** the tee low ($39.50) and outerwear top ($1,449) reproduce. The $1,449 is not a valid high (shearling, Runway).
- **Mark:** facts_first gives "TOMMY HILFIGER". The site writes "Tommy Hilfiger" in titles.


### Doors — browser read 2026-10-10 (main thread)

own_doors_us NC → 3 (low confidence). Browser read 2026-10-10: 139 US locator cards (index sums to 138) = 136 outlet-centre doors + 3 classed full-price only because not in outlet centres (Rookwood Commons OH, Sands Oceanside NY, The Loop Kissimmee FL; low confidence; same treatment as Calvin Klein). Locator has no store-type field; no flagship; Kids is a product line, not a banner; 2 in PR.


## Tracksmith


**Status: partial.** This is the first full record; there was no earlier `full_tracksmith.csv`. All pages were read on 2026-10-10. The doors file's `captured_on` says 2026-10-10, not the 2026-10-08 in the spec, because that is the day the pages were actually read.

### How the run went
- **Fetches:** about 105 WebFetch calls, with no 429s and no bot checks. Many guessed product handles returned fetch errors; those are not blocks.
- **Pacing breach:** one pair of product-page fetches (Harrier Tee and Brighton Base Layer) went out together. Every other fetch went one at a time.
- **WebSearch was exhausted** on my first call (the turn-wide limit), so I worked from direct fetches only.
- **Bash route closed:** curl to checkout.tracksmith.com was refused by the egress proxy (CONNECT 403). I did not work around it.

### Store and feed
- **Store:** tracksmith.com is a headless Shopify store (Astro front end, DatoCMS). The Shopify feed is served at `checkout.tracksmith.com/products.json` and is reachable through WebFetch.
- **The feed carries no composition.** body_html is a one-liner and tags read "Apparel".
- **The feed is unreadable in bulk.** WebFetch cut a 250-product page off at about the tenth product.
- **Result:** composition was read product page by product page. The census is the brand's own listing: Men > Apparel says "95 Results" (95 products, each one handle).
- **Vendor field = manufacturer.** It names 99 Degrees (Grayboy), In Record Time and Ningbo Anwei Woolen Textile (Cashmere Sweater). This is feed data, not a claim on any page. I recorded it as such and did not use it to raise craft.

### Fibre
- **Basis.** The 95 listing products collapse to 70 base styles once city and graphic editions are merged: Heirloom ×7, Brighton city ×5, Grayboy graphics, city tees, long sleeves and reversible singlets.
- **Read: 60 styles, all disclosing composition.** Natural 17, synthetic 41, cellulosic 2, which gives 28 / 68 / 3 (rounding sums to 99). Spandex appears on 43 styles, and on 37 at 5% or more.
- **Shape: split.** Running categories are synthetic-led. Mid-Layers (cotton sweats, Downeaster merino), Underwear (merino) and Lifestyle are natural-led.
- **Merged editions:** only one edition per family was read; the others were merged by title.
- **Not read (10):** Run Cannonball Run Top and Shorts, Parks Tee, Marathon Sweater - Tokyo, Hare A.C. Membership Singlet and Shorts, NDO Anorak (guessed handle 404), NDO Tights, Trackhouse Tee - Tokyo, Trackhouse Sweatpants. These 10 sit outside the denominator, which is the 60 read.
- **Brighton Briefs page contradicts itself:** Fabric & Care says 66/32/2 wool/nylon/elastane, and a feature block says 83/12/5. The first is filed.
- **Lines** (house collections, used in the `lines` column): Twilight, Van Cortlandt, Session, Strata, Meridian, Brighton, Harrier, Trackhouse, Grayboy, Turnover, Chiltern, Federation, Fieldhouse, Franklin. A full line table was not built (not in this spec).

### Prices
- **Missing garments:** dress shirt, jeans and dress pants are NONE. It is a running house, with no wovens, denim or tailored trousers in men's apparel or lifestyle.
- **Sweater — please rule.** There is no crewneck knit sweater in the main range. I filed the **Downeaster** ($170, 100% merino half-zip mid-layer) as the nearest, as a named judgement.
  - The alternative is NONE.
  - Marathon Sweater - Tokyo ($165) is a limited edition.
  - A "Cashmere Sweater" ($169) exists in the feed, but its product page is not live.
- **Shoes:** the own-label Eliot line, ranging from the Runner at $198 to the Racer at $280 (not labelled limited). There is no loafer.

### Doors and stockists
- **Doors:** 2 US own doors and nothing else. The help center says "We have two retail locations": Boston, 285 Newbury St (also corporate offices), and Brooklyn, 147 Wythe Ave. Phones were taken from each Trackhouse page.
- **No Wellesley store.** Wellesley is the 2014 launch shop per the About page. Marathon Sports Wellesley is a stockist.
- **London hub not seen.** The London "hub" in facts_first does not appear on the help center or the partners page; not verified.
- **Stockists:** the "Find a Retail Store" page is a static list: 69 US partners (130 US locations), plus 24 international partners.
  - It gives cities only, with no street addresses.
  - Fleet Feet franchises are filed as independent.
  - Running Warehouse is online only.
  - Spellings flagged "as printed" are the page's own.
  - Register-relevance (door one/two) is not judged here: most are running-specialty shops.

### Tech, craft, ownership
- **Tech: proposed 3, on a provisional scale** (no tech rubric was issued).
  - Licensed: 37.5®, Polygiene®, Nilit®, Schoeller® coldblack® / active>silver™, Polartec®, and Pebax® (footwear).
  - House-named fabrics: 2:09 Mesh, Bravio and Inverno (Italian, mill unnamed), Varsity Cotton (Massachusetts) and Eliot Stretch (Swiss, Schoeller).
  - 32 of 60 styles (53%) carry a named fabric. No owned fibre R&D is evident.
- **Craft: proposed 3.** Nothing is owned.
  - Two makers are named on product pages: FILATI (seamless merino, "since 2016") and P&R Têxteis (Portugal).
  - Two mills are named: Schoeller and Polartec.
  - How We Work lists the manufacturing countries: Poland, Portugal, China, Taiwan, Malaysia, Canada and the USA.
  - Made-in is stated on 4 of 60 styles. The "Made in Italy" on Twilight pages refers to the fabric and is not counted.
- **Founding.**
  - The About page says it launched in 2014 with a shop in Wellesley, MA, and calls itself "an independent running brand". It does not name founders.
  - Crunchbase says the company was founded in 2013 by Luke Scheybeler and Matt Taylor, has 13 investors (including FJ Labs) and has taken debt financing from Dwight Funding.
  - The founders and the venture backing rest on Crunchbase alone (third-party); the funding amounts are hidden there.
- **The worklist claim "Trackhouses in Boston, NYC, Wellesley" is wrong on Wellesley** (as facts_first already said).

### Not reached
- **Lookbook:** the Lookbooks tab loads by JavaScript, so no label was read.
- **Vinted:** the search returns 460 results, but no brand id is exposed.
- **Grailed:** `/designers/tracksmith` served the generic designers index.
- **B Corp:** the directory fetches errored.
- **GOTS:** not checked.
- **Search URL:** not tested.


## Uniqlo


**Conditions.**
- I used WebFetch only, 116 network fetches. A few extra reads re-used cached pages via the offset parameter.
- WebSearch was exhausted (shared turn budget) on the first call, so nothing came from search.
- There were no 429s and no bot checks on uniqlo.com.
- **Pacing slip:** one batch of 4 class-total fetches (limit=1) went out in parallel. Every other fetch was made one at a time.
- I did not attempt the locator, as briefed. `doors_uniqlo.csv` is header-only.
- **Fast Retailing pages failed.** The history year pages, the company profile and `/eng/sustainability/labor/factorylist.html` returned CLIENT_ERROR or SERVER_ERROR. I guessed those URLs because search was unavailable. `/eng/about/history/` loads, but shows 2025 only.

### Channel
- The US product pages load JSON that WebFetch can read directly:
  - Listings: `https://www.uniqlo.com/us/api/commerce/v5/en/products?path=<gender>,<class>,<category>,<subcategory>&limit=&offset=&sort=`
    - Men = 22211. `sort=2` is price ascending; `sort=3` is descending.
  - Product detail: `.../products/<id>/price-groups/00/details`
    - Gives `composition`, `countriesOfOrigin`, prices, `genderCategory` and `sizeGender`.
- A listing page truncates at about 17-20 items under WebFetch, so I worked sorted per category rather than paging whole classes.
- **Sale price groups:** each sale price group appears as a duplicate listing (for example `E455957` at $49.90 in group 00 and $29.90 in group 01). On a sale-only product, "base" is the sale price and no compare-at is exposed. Every price used is a non-promo base price.

### What was checked
**Prices.**

| Garment | Basis | Low | High | Notes |
|---|---|---|---|---|
| Tee | range | $9.90, DRY V-Neck | $34.90, HEATTECH Ultra Warm T-Shirt | The high is a thermal Uniqlo files under T-Shirts (judgement). |
| Polo | pair | $29.90, AIRism Cotton Pique | $49.90, Merino Polo Sweater | The high is "extra-fine Merino", 100% wool. |
| Dress shirt | range | $49.90 | $49.90 | All 21 listings are $49.90. |
| Jeans | range | $59.90 | $59.90 | |
| Dress pants | range | $59.90 | $59.90 | |
| Sweater | pair | $49.90, Lambswool | $99.90, Cashmere crew | |
| Outerwear | range | $49.90, Pocketable UV Parka | $199.90, Seamless Down Coat | |
| Shoes | range | $59.90 | $59.90 | Two unisex shoes; no loafer. |

Exclusions:
- **Coming soon:** Ultra Warm Down Coat ($229.90, "late Oct") and Rugger Shirt ($49.90, "mid-Oct").
- **Collaborations:** UT (e.g. KAWS UNIVERSE, "designed just for UNIQLO", © KAWS), UNIQLO : C, JW ANDERSON, F.RISSO and the Roger Federer Collection. These sit in Uniqlo's own "Special Collaborations" class, which lists 116 men's items.
- **Uniqlo U is counted.** It has 24 men's listings, e.g. Wool Blend Short Coat $129.90 and Fishtail Parka $129.90.

Listing links:
- Tee: `/us/en/men/tops/t-shirts`, read by me. The server render showed 8 men's tiles and "Results: 0 items".
- Outerwear: `/us/en/men/outerwear-and-blazers`. Facts-first read this on 2026-10-08; I did not re-read it.
- The other listing links are NC. I know their API category ids (polo 95672, dress shirt 95673, jeans 23392, dress pants 68286, knit 95668, shoes 154619) but did not verify the storefront URLs.
- `search_url` is NC (not tested).

**Fibre: documented sample of 66 men's styles** (target ~80; stopped at the fetch cap).
- Classes (listings, with overlap): Outerwear 52, T-Shirts/Sweats/Fleece 208, Sweaters & Knitwear 27, Shirts 92, Bottoms 100, Innerwear 97, Loungewear 28, Sport Utility Wear 73, Accessories 61.
- The men's path total is 629 listings, which include accessories and sale duplicates. Uniqlo also gives each pattern of one garment its own product id (14 "Flannel Shirt" ids). So `styles_total` is NC.
- **Sample by category:**

  | Category | Styles read |
  |---|---|
  | Tees-polos | 19 |
  | Outerwear | 13 |
  | Knitwear | 8 |
  | Shirts | 7 |
  | Sweats | 5 |
  | Trousers | 5 |
  | Underwear | 5 |
  | Denim | 3 |
  | Shorts | 1 |

- **Results, on the sample only:**
  - Composition is stated on 66 of 66.
  - Natural-led 35 (53%), synthetic-led 30 (45%), cellulosic 1 (2%; Easy Care Soft Shirt, 57% rayon).
  - Spandex on the main line: 14 styles, 9 of them at 5% or more (AIRism, HEATTECH and the underwear).
- **Shape is split.**
  - Synthetic leads: outerwear (8/13; down and padded shells are polyester), sweats (4/5; sweats are 67% polyester / 33% cotton), trousers (4/5; Smart and Pleated pants are 67/29/4 poly/rayon/spandex) and shorts.
  - Cotton leads: tees, shirts and denim. Knitwear is 5 natural (cashmere, lambswool, merino, cotton) against 3 acrylic or polyester blends.
- **Women's-sized unisex items excluded.** Four items in the men's path came back with `sizeGender: WOMEN` and were dropped: Barrel Jeans E479000, whose description calls it women's; Straight Sweatpants; Milano Ribbed Full-Zip Cardigan; and Sweat Half-Zip.
  - I read `sizeGender` only from the 46th fetch onward. About 20 earlier unisex styles are flagged "sizeGender not read" in the styles file, including the UNIQLO : C Oversized Sweatshirt.
- **Parsing calls:**
  - Composition varies by colour on EZY jeans and AIRism tees. I parsed the first-listed group.
  - Harrington 50/50 cotton/polyester: cotton wins as first-listed.
  - Elastane in cuffs, ribs and waistbands is excluded.
- **Swim:** the men's category tree shows no swim node. Swim shorts, if any, were not separated, so `swim_*` is NC.

**Doors.**
- US 87: the FR North America page, re-read today (87 as of 30 Sep 2026; Canada 39; first US store 15 Sep 2005).
- World 2,543: the FR shoplist, whose latest column is 30 Nov 2025 (Japan 794 including 10 franchise stores, plus International 1,749).
  - The two figures are 10 months apart. Whether International includes franchise doors is unstated. Sebastian may prefer NC here.

**Tech.** The tech scale is PROVISIONAL; no tech rubric was issued.
- 19 of 66 sampled styles (29%) name a technology: HEATTECH, AIRism, DRY, DRY-EX, BLOCKTECH, and Toray's NANODESIGN (licensed, on the Pocketable UV Parka).
- AirSense pages say the fabric was "jointly developed by Toray and UNIQLO" but name no technology. They are counted only where DRY is named.
- BLOCKTECH is thin. The men's BLOCKTECH subcategory holds 1 style, the BLOCKTECH Parka. No BLOCKTECH page mentions Toray.
- The HEATTECH class has 34 men's listings, accessories included.
- **Proposed 4.** Owned named fabrics sit on a large share of tops, innerwear and sportswear. It is borderline with 3.

**Craft. Proposed 2.**
- 0 of 66 pages name a maker.
- Every composition text says "Imported". The payload carries `countriesOfOrigin` codes (VN, BD, KH, CN, ID, IN), but I did not verify that the rendered page shows them, so `made_in_stated_share` is NC.
- Named mills or fibre makers appear on isolated pages: Kaihara (Slim Straight Jeans) and Toray (AirSense ×2, NANODESIGN).
- The FR factory list the brief cites was not reached, because its URL errored. If a human confirms it, a 3 is arguable.

**Quote.** The Fast Retailing Group Mission (parent company, house voice). The FR statement "Changing clothes. Changing conventional wisdom. Change the world." is the alternative.

**Other.**
- Grailed `/designers/uniqlo` exists.
- Vinted shows a "uniqlo" brand filter with 500+ results, but the page exposes no brand id, so it is NC.

### Not reached
- Founding facts. The brief's "1949 Ube (Ogori Shoji) / first Uniqlo 1984 Hiroshima" is **not verified** in this pass and is left NC. I did not fill it from memory.
- The Fast Retailing annual report and listing details.
- The factory list and any owned facility.
- Lookbook, B Corp, GOTS, locator and stockists.
- Colourway ratio.
- Shoe PDPs (only listing prices were read).

### Contradictions
- **Tee entry:** facts-first gives $19.90 (Boxy Cropped). I filed $9.90: DRY V-Neck and DRY Color T-Shirt are both full price with no promo. The Crew Neck T-Shirt's regular price is $24.90; facts-first's $19.90 for it was a limited-time offer.
- **Outerwear top:** facts-first's $179.90 Hybrid Down Parka is reproduced, but the dearer Seamless Down Coat ($199.90, available) is the filed high.
- **Store counts:** the FR shoplist still shows US 77 (Nov 2025) against 87 on the North America page.
- **Brief:** "BLOCKTECH (owned, with Toray partnership)". The pages read show Toray co-development on AirSense and NANODESIGN, not on BLOCKTECH.
- **Men's path sizing:** the men's path includes women's-sized unisex goods, so any census of `path=22211` overstates the men's range.


## UNTUCKit


**Status: partial.** Sections 1–5 are complete apart from two shorts styles whose fabric could not be read. The NC cells are lookbook (4), Vinted (2), B Corp (2) and GOTS (2). WebSearch was exhausted (shared limit), so everything here comes from direct fetches. About 88 fetches in all, run one at a time apart from one slip where two shirt-feed pages went out together. No 429s, bot checks or WAF blocks.

### Store, prices
- untuckit.com is a Shopify store selling in USD. Feed prices match the displayed prices: Black Stone $109, Arnold $115, Ultrasoft Tee $39.50. I did not read `Shopify.currency.rate`.
- `/products.json` is reachable through WebFetch. A curl pull through the sandbox proxy was refused (CONNECT 403), so I did not use it. WebFetch cuts a page at about 76k characters, so I read each men's collection feed (`/collections/<x>/products.json`) in small pages (`limit=5–13`). Collection feed order matches the HTML listing order.
- A sitewide **SALE25** code (25% off) was running, and many styles carry dated "Price on MM/DD/26" markdowns. I took full price or compare-at throughout. Exact figures are in `note` in the full row.
- **Dress shirt:** UNTUCKit sells no tuck-in dress shirt. Its shirts are cut to be worn untucked. The cell uses the Wrinkle-Free long-sleeve button-downs ($109–$115), and the Performance shirts sit at the same two prices.
- **Other gaps in the range:** no dress trousers, so the dress-pants cell uses the chinos. There is no crewneck sweater, so the sweater cell is a range. The only shoes are two own-label leather sneakers at $158 (no loafer).

### Fibre (styles_untuckit.csv)
- **Census:** the nine men's nav collections plus Shorts & Swim give **132 styles**, deduplicated by title, from **288 handles**. I read fabric text for 129 of them:
  - one, the Waffle-Knit Hoodie Sweater, has the placeholder `[confirm fabric content]` in its Fabrics field, so it is filed as ND;
  - two are NC: the 7" Traveler Tech Shorts (not in the collection feed) and the Linen-Cotton Utility Shorts (`rivermarc`, which returned a fetch error).
- **Feed vs listing:** the shirts feed has 111 handles against about 108 HTML cards. Three feed products have no HTML card: Ultrasoft Flannel Shirt ×2 and Wrinkle-Free Foxvine.
- **Title dedup understates SKU stems** in two places: CottonTek™ Brachetto Shirt is 6 stems and Printed CottonTek™ Polo is 3. On a SKU-stem basis the total would be about 139.
- **Totals:** 70% natural-led, 27% synthetic-led, 0% cellulosic, 43 styles with elastane. Shape is `one`: the synthetic-led categories (sweatshirts, 6 styles; jackets & vests, 7) are each under ten styles.
- **Lines (headline):**
  - Wholly natural: **Wrinkle-Free** (31 styles, all cotton, mostly 100%), **Vintage Wash** (12, all 100% cotton), Stretch Cotton (5).
  - **Performance** (31) is 87% synthetic, so its verdict is `mixed`. Its shirts are 92/8 or 94/6 nylon/elastane, and the exceptions are the cotton-led seersucker and Pima polos.
  - Synthetic: Performance Tech and Traveler Tech, all polyester where read.
  - Sport coats are 10 of 11 natural (wool, linen, cotton); the exception is the nylon Performance Tech Blazer.
  - Several 50/50 cotton/polyester styles (Ultrasoft tees and henleys, Hybrid Polo) count as natural only through the first-listed tie rule.
- **Noticed, not acted on:** the cadetto-wf-8 product description contains a stray block of chat-turn markup. I treated it as page data only.

### Doors and stockists
- I did not read the locator again. The main thread read it in a browser: 69 US full-price own doors plus 1 in Canada, with no outlets. `own_doors_us` = 69 and `own_doors_world` = 70.
- The doors file lists US doors only. West Edmonton Mall, the one Canada door, is counted in `own_doors_world` but has no row.
- facts_first quoted the locator as "more than 80 store locations… United States and Canada". The card count is 70, and Randa's release says "more than 70". The 80 is stale copy.
- The brand lists no stockists, so the stockists file has one `none` row.

### Sections 6–13
- **Owner:** **Randa Apparel & Accessories** (privately held). This is confirmed by Randa's own release of 1 Sept 2026, which says the acquisition is complete. The seller is not named. Randa's site lists UNTUCKit among its owned brands. The leadership team stays at the SoHo headquarters.
- **Founding (contradicts the brief):** the brand's about-us page says **2010**, when Chris Riccobono created the shirt. Aaron Sanandres was "brought on in 2011". Randa's release also says founded 2010. The brand does not state a founding city; New York is its headquarters.
- **Tech (proposed 3, provisional scale, no tech rubric issued):** the brand's own named fabrics are CottonTek™, EcoSoft™ and Traveler Tech. Licensed names are SUPIMA®, TENCEL™, brrr° and FUZE, plus LYCRA on the denim. Named tech appears on 14 of 132 styles (11%). The large Performance nylon line carries no named technology.
- **Craft (proposed 2):**
  - Every product page read says "Imported" and no country, so `made_in_stated_share` = 0.
  - No owned facility or named maker. The code of conduct's "UNTUCKit factories" is a claim with no place named.
  - Mills are named on 4 sport coats only: Reda, Lanificio TG di Fabio, Maggia.
  - Process copy (five inspections, batch testing, finishes) is generic.
- **Quote:** Riccobono in Randa's release (2026-09-01). It came through the fetch summariser and should be checked against the page before display. Alternate in the brand's own voice, from about-us: "We've totally reengineered the casual dress shirt to have the perfect untucked length".
- **Not established (NC):**
  - Lookbook: the pages sitemap (186 URLs) has no lookbook page, and I did not read the blogs.
  - Vinted: the page rendered with no brand id.
  - B Corp: the directory URL returned a fetch error and WebSearch was unavailable.
  - GOTS: not checked.
- **Grailed:** `/designers/untuckit` exists.
- **Pronunciation:** NONE.


## Woolrich


**Status: partial.** About 40 fetches, made one at a time. WebSearch was exhausted (turn budget), so everything was read by direct WebFetch. The agent proxy refused curl to woolrich.us (403 on CONNECT, logged as a policy denial), so the Shopify feed was read only through WebFetch, and that truncates at about 15 products per page.

### What was checked
- **Store.** woolrich.com redirects to woolrich.us, a Shopify store ("© 2026 Woolrich USA"). Terms of service: "owned, operated, and administered by Woolrich USA Inc., a New York corporation". No parent or licensor is named. Prices are USD. Feed price matches the page on two products (Cloud Arctic Parka 765.00 / $765; Bering Jacket 525.00 / $525). `Shopify.currency.rate` was not read (NC). Search `https://woolrich.us/search?q=` returns 36 results for "shirt".
- **Census.** `collections.json` counts (Men 199, Mens Tops 68, Mens Outerwear 82, Mens Sale 123) include product that is not listed or not available. The live pages show: Men "33 Products", Mens Tops "19 Products", Mens Outerwear "9 Products", Mens Bottoms 0 (feed empty), Mens Sale "0 Products". The collection feeds agree: Tops 15+4, Outerwear 8 available. **13 men's clothing styles, 28 colourway listings** (SKU stem, e.g. CFWOSI2032). All 13 PDPs were read. All 13 state a composition and a country of origin.
- **Fibre.** 8 natural-led (62%), 5 synthetic-led (38%), 0 cellulosic, 0 elastane. Outerwear is synthetic-led (5 of 7). Every other category is natural-led. Shape is `one` because no category reaches 10 styles. The quilted overshirt (sold under Tops) is assigned to outerwear by garment. On the crewneck, wool and cotton tie at 40%, so first-listed (wool) leads. No named lines were found (`-`).
- **Prices.** All regular price. Tee $95 single. Dress shirt is a casual button-down only: range $155 (Button-Down Checked Shirt in Pure Cotton Flannel) to $185 (Warren). Sweater $320 single (40/40/20 wool/cotton/PA crewneck; no elevated crewneck). Outerwear range is $500 (Wool-Blend Jacket with Hood) to $765 (Cloud Arctic Parka); I excluded the $400 vest and the $495 overshirt. Polo, jeans and dress pants are `NONE` on the live US range today: bottoms are empty, and the polo collections (Mackinack, Monterey) exist with no live product. This looks seasonal, so treat it as "not on sale 2026-10-10" rather than "never made". Shoes are `NONE` on woolrich.us. No garment-level men's category exists below Tops, so the tee, shirt and sweater links point to the parent `mens-tops`.
- **Ownership.** Baoxiniao Holdings acquired the IP for all territories outside Europe, which includes the US (the-spin-off, 10 Jun 2025). BasicNet acquired the European rights and Woolrich Europe S.p.A. from L-GAM: EV €90m, initial €40m, announced 12 Nov 2025, closing Dec 2025 (FashionNetwork). Who owns Woolrich USA Inc. is **not established**. It is most likely Baoxiniao or its licensee, but no page I read says so. Baoxiniao's and BasicNet's annual reports were not read.
- **Craft (proposed 2).** The 1830 Plum Run mill is a heritage claim on the brand site. Wikipedia, citing the WSJ (21 Dec 2018, not read, paywalled), says the closure of the last US plant at Woolrich, PA was announced in **September 2018**. The brief's "closed 2017?" is not supported. Wikipedia also says wool production at the original 1830 site stopped in 1843–45. No maker, mill or process is named on any live men's PDP. Made-in is stated on 13 of 13.
- **Tech (provisional scale; no tech rubric was issued).** PrimaLoft (licensed) is on 2 of 13 styles (bomber, overshirt), so 15%. "Cloud Poly" (parka shell) is a house fabric name whose ownership was not established; I left it out of the list. GORE-TEX / WINDSTOPPER and Manteco / Kuroki appear only in collection names with no live men's product.
- **Doors.** The doors file is header-only, as briefed (main-thread browser read). `own_doors_us` is NC: there is no locator, and there is no evidence either of US closures or of open US doors. Wikipedia's "as of 2023, three stores remain" (Woolrich PA, SoHo, Woodbury) is uncited. `own_doors_world` = 14 comes from the European directory (26 = 14 stores + 12 outlets), so it is a **Europe-only floor**. FashionUnited (14 Jan 2026) corroborates "around 20 stores across Italy, Germany and the Netherlands". Doors in the Baoxiniao territory are not on any brand locator read.
- **Stockists.** None listed by the brand (one `none` row).
- **Quote.** From the house, on the Woolrich Heritage page. It was captured through the WebFetch summariser, so check it against the page before it is filed. Alternative: CEO Lorenzo Flamini, "Our objective is to strengthen our brand identity by focusing on what has always defined Woolrich." (the-spin-off, 10 Jun 2025).

### Not reached / NC
Vinted id and Grailed page: both pages render client-side and showed no brand data. B Corp and GOTS: the directory did not render. `feed_currency_rate`. Lookbook: none on woolrich.us. The homepage hero reads "DISCOVER FALL/WINTER 2026" with no lookbook page, and `/pages/woolrich-editorial` errored. The European site was not checked for a lookbook.

### Contradictions with facts_first / worklist
- facts_first listed the US operator as unknown. It is Woolrich USA Inc. (NY corp, per the terms).
- The worklist claims "oldest US outdoor brand, NYC flagship". The brand site says only "American Heritage Since 1830". The NYC flagship is not on any brand locator; its status is unknown.
- The facts_first prices ($95 tee, $765 parka) are reproduced.
- The range is far smaller than the collection counts suggest (13 live styles against "Men 199").
