# seat_wave_b — batch 3 (Greyson through Kenzo) · 11 October 2026

## Files

- `return.csv`: 10 rows.
- `return_styles.csv`: 1,646 styles.
- `stockists.csv`: 2,139 rows.
- `return_counts.csv`: 5 brands.
- `own_doors.csv`: the running master, 1,245 rows. It now carries `lat` and `lon`: new rows hold the locator's own coordinates where the feed gives them, and earlier rows hold `NC`, because those locators weren't re-read.

All brand names match the canonical keys exactly, no cell is empty, all values are from their allowed lists, and every store count equals its rows. Hoka's 13 unread styles carry `NC`, the schema's not-checked token.

## Batch 2 rulings applied (11 Oct)

- **Clarks** tee slot is NONE.
- **G/FORE** dress shirt slot is NONE.
- Everything else stands as filed.
- **Converse:** the ruling text reads "pony hair out … shoe high $130", but $130 *is* the pony-hair shoe. With pony hair out, the high stays at **$125** (Chuck 70 GORE-TEX Hairy Suede, a long-nap suede, not hair-on hide). Flagged for merge.

## Retry, 11 Oct afternoon

- **Hoka: filled.** No block on the second pass.
  - Tee high is $100. The $79 was a markdown of a $98 colourway.
  - Sweater is NONE: the Kaitoro Knit Crew is a sweatshirt, flagged.
  - Shoes are a range, $60–280, since Hoka sells no loafer.
  - All 13 missing compositions were read. Fibre is now 9% natural and 88% synthetic.
- **Kapital: still blocked.** The store is still IP-restricted ("リモートホストIPが制限されています", meaning this IP is restricted), checked at 11:32 EDT. Prices and fibre stay `NC`, and need a different IP or a later day.

## Blocked mid-read (original run)

- **Hoka:** hoka.com started serving a DataDome challenge (HTTP 403) on the 20th product page.
  - Missing: the sweater slot, all seven shoe cells, and 13 of 32 compositions (`NC`).
- **Kapital:** kapital-webshop.jp IP-restricted the browser after a pagination loop, which our crawl caused.
  - Missing: all prices and 385 of 386 compositions (`NC`).
  - Doors and craft were read from kapital.jp, which wasn't blocked.
- The agents' spec now carries anti-block rules: read listings first, paginate only up to the stated count, space product pages at least 1.5 s apart, and stop at the first block.

## Flags for merge (not covered by the standing rules)

| Brand | Flag | Filed |
|---|---|---|
| Hart Schaffner Marx | Licence-only brand: no catalogue, prices or doors of its own. Retailer prices were not used. | Price cells `np`; styles 0; doors 0 |
| Hart Schaffner Marx | Event calendar used as a stockist source (it gave the 1 independent) | 1 row; chains summarised in its NOTE |
| Greyson | Only own-label shoes are Del Toro collaborations | Low $475, high NONE |
| Greyson | Members-only Players Club tees | In the census, out of the tee low |
| Helly Hansen | Vail store sits under a resort retailer's Locally account, operator not named | Own door, flagged; could be `held` |
| Helmut Lang | Jeans and outerwear highs are sale-only stock still in navigation | $598 / $1,998 at list price; current full-price highs are $368 / $1,398 |
| Hoka | Hike pant used as dress pants (Converse precedent) | `single` $108 |
| Human Made | Store serves USD to US visitors and is built in yen | USD filed, yen in the note |
| Human Made | Ningen-sei seasonal collection treated as a capsule | Out of the tee high (otherwise $225) |
| John Elliott | Denim washes each have their own article number | Counted by model: 81 (about 94 by article) |
| John Lobb | 13 US stockists, not 14. Saks has 5, so the chain rule applies | Rows written and chain summarised; register to decide |
| Kapital | Only quotation is in Japanese | Filed with a translation in its NOTE |
| Kenzo | No majority-cashmere crewneck | Sweater high $685 cotton-wool cable |

## Things found

- **Helmut Lang** is a sister company of Theory under Fast Retailing USA, not part of Theory (Fast Retailing 2025 Modern Slavery Statement).
- **Helly Hansen:** Kontoor's purchase closed on 31 May 2025 (CAD 1.3 bn, per its 10-Q). HH Workwear is sold on its own site and is not counted.
- **Human Made** listed on the TSE Growth market on 27 Nov 2025. Its only US presence was a 2023 pop-up (now `closed`). There are 14 own doors abroad.
- **Hart Schaffner Marx** is owned by ABG-HMX LLC (Authentic Brands). The worklist's "six register shops" claim is not supported: the brand names one independent.
- **John Elliott** has a second US store at 270 Lafayette, NYC, which the worklist leaves out.
- **Figures from filings and brand statements are mentioned only, never filed as door counts:**
  - Kenzo: 104 stores (LVMH).
  - Hoka: 62 stores, own and outlet combined (Deckers 10-K).
  - John Lobb: 19 stores (brand's own story page).

---

# Per-brand notes


## Greyson: full record, wave B batch 3 (read 2026-10-11)

**What was checked.** I read the US store at greysonclothiers.com. It runs on Shopify, prices in USD, and `Shopify.currency.rate` is 1.0. Feed prices match the displayed product-page prices (Tomahawk Cashmere Crewneck $380, M65 Mod Military Jacket $598). The men's "Shop All" collection (`/collections/mens`) holds only 273 products, and the category collections carry styles it leaves out. So the census is the union of 32 men's navigation collections (the clothing categories, Golf, Tennis, Activewear, Dress Sport, Essentials, Players Club, New Arrivals, Limited Product and Sale): 429 products in all. Of those, 317 are in-scope men's clothing handles, which make 311 styles. I read all 317 product pages for the Materials & Care block, and the description and JSON-LD where that block was missing. Other pages read: Our Story, the Fabric Library, the men's lookbook and the pages sitemap. Two press sources were used for founding and ownership: insider.fitt.co (Feb 2025) and Crain's Detroit (May 2019).

**Section 4** was not re-read. Counts were carried over: 10 own doors in the US and 11 worldwide (Seoul), with "operator not stated" on every row.

**Stockists.** The brand lists none. There is no stockist or retailer page in the footer or in the 195-page pages sitemap, and seven guessed paths all return 404. The stockists file has one row with `locator_kind` set to `none`.

**Scope decisions.**
- Licensed product is out of the census and out of prices:
  - the NFL, Detroit Lions, MLB and varsity collections (323 listings, overlapping)
  - 9 collegiate items that sit inside Shop All
  - Ryder Cup 2025, 125th U.S. Open and LIV Ripper GC items
- Kept in the census:
  - Greyson x Ford Heritage pieces (collaboration)
  - Soft Goods pieces (collaboration)
  - the "us-open-tennis" handles, which are now titled "Limited Icon Racquet" and carry no marks
  - Throwback Detroit
- Styles are counted by product handle. SKU stems are season-coded per colourway (MCLSCK71 and MFA26K71 are the same Colorado Hoodie), so a SKU stem identifies a season and colourway, not a style. I collapsed 6 exact-title duplicate listings, taking 317 handles to 311 styles. Colourway ratio: 766/311.
- 52 styles are tagged limited. They are counted in the census and never priced.

**Fibre verdict.** The range is split: 33% natural, 64% synthetic and 1% cellulosic, with 5 styles (2%) undisclosed. 205 of 311 styles contain elastane, 176 of them at 5% or more.
- Knitwear is 100% natural (20 of 20: merino, wool/cashmere, cashmere).
- Shirts lean natural (10 of 15).
- Polos and tees are 75% synthetic-led (84 of 111 disclosed). Outerwear, trousers, shorts and tailoring are also synthetic-led.
- Sweats split evenly, 32 natural and 32 synthetic.

Lines (by title series and the Fabric Library programs):

| Line | Styles | Verdict |
|---|---|---|
| Guide Program | 22 | all-synthetic |
| Sequoia Program | 21 | all-synthetic: nylon-faced double knit, 40% cotton back |
| Montauk Program | 7 | all-synthetic |
| Colorado | 10 | all-synthetic |
| Kennebec | 10 | all-synthetic |
| Rhinebeck | 6 | all-synthetic |
| Trailwolf | 6 | all-synthetic |
| Saratoga Program | 11 | all-natural (merino) |
| Aspen | 8 | all-natural |
| Fireside | 9 | all-natural |
| Alpha Slub | 6 | all-natural |
| Soft Goods | 6 | all-natural |
| Gaston | 5 | all-natural (linen-led, 39% viscose) |
| Players Club | 32 | mixed: 81% synthetic |
| Feed the Wolf | 9 | mixed |
| H.S. | 8 | mixed |

Omaha (6 styles) is cotton-led on paper but 56% synthetic by blend (brrr° polyester and nylon).

**Prices.** Seven garments are filled and jeans is NONE (no denim in any men's category).
- **Tee:** $60 to $110 (range). The Members Only Spirit Wolf tees at $48 are left out of low as members-only product.
- **Polo:** $110 to $280 (range). The high is the merino Saratoga Waffle Stitch Sweater Polo, which the house lists under Polo Shirts. The dearest regular performance polo is $140.
- **Dress shirt:** $190 to $220 (range), from the Woodward and Gaston dress shirts. Camp-collar shirts ($170) and knit button-fronts are left out.
- **Dress pants:** $160 to $250 (range), from the Montauk Performance Trouser to the Sequoia Tuxedo Trouser.
- **Sweater:** $240 to $380 (pair), from the merino crewneck to the cashmere crewneck.
- **Outerwear:** $190 to $598 (range).
- **Shoes:** see Flags.

**Craft and tech.**
- Proposed craft is **2**, with 1 arguable. No maker, mill or facility is named. The garment's country of making is almost never stated; the exceptions are "Made in USA" and "Crafted in Detroit" on Soft Goods and Ford collaboration pieces, and "Imported" on one trouser. 18 styles say the fabric is Italian, mill unnamed.
- Proposed tech is **3**: the licensed brrr° cooling fibre is named, and the Guide Program uses it, together covering 28 of 311 styles (9%). The Fabric Library also names house fabric programs (Montauk, Sequoia, Falcon, Dune). Nothing is owned.

**Contradictions with the worklist or record.**
- The worklist "why" says "own stores?". Section 4 found 10 US doors, so there is no conflict.
- The site gives no founding date or place. 2015 and Hawthorne, NY (the first HQ) come from press; the HQ is now Detroit.
- Ownership: private and founder-led (Charlie Schaefer, founder and CEO). A $20M Series A in Feb 2025 was led by NewBound Ventures and Chris Koch.
- The worklist band reads "accessible". The prices sit there: sweater $240 to $380, dress shirt $190 to $220.

**Mark as written.** `mark_as_written: GREYSON`. The header logotype is all caps; copy writes "Greyson Clothiers". The 8 Oct ruling already sets the mark as Greyson, without "Clothiers".

**Not reached / NC.** Vinted, Grailed, B Corp and GOTS were not read, so status is `partial`. The FAQ page rendered empty in the browser and was not read.

**Flags in the style file.**
- Kennebec Camo Short: the composition sums to 102% (68/29/5). Filed as read; sister styles read 66/29/5.
- Siasconset Quarter-Zip: the composition lists "Nylon" and "Polyamide" as separate fibres (the same fibre). Filed as read.
- "Polymide" (a house typo) on several pages is read as polyamide.
- Throwback Detroit Varsity Jacket: the page says only "100% Satin" (a weave), so it is filed as ND.
- A customer review on the Tomahawk page says the sweater is made in China. That is not the brand's statement and is not used.

## Flags for merge
1. **Shoes:** the only own-label shoes are Greyson x Del Toro collaborations (Suede Milano Loafer $475, Icon Wolf Velvet Slipper $495). Low is filed as $475 and high as NONE under the collaboration rule. If Del Toro counts as a maker rather than a collaboration, the slot becomes a pair at $475 / $495. If collaborations are barred from low as well, shoes become NONE.
2. **Members-only product:** the Members Only Players Club collection and the Spirit Wolf tees are sold through the site to members. I kept them in the census, but they sit outside the tee low. Is members-only product regular range?
3. **Camp-collar shirts as dress shirts:** if they count, dress shirt low becomes $170 (Rhodes Seersucker Camp Shirt).
4. **Licensed-scope edge cases:** Greyson x Ford Heritage (a corporate brand licence) is kept in the census as a collaboration, and Ryder Cup and U.S. Open items are treated as event-licensed and out. Both standing rules name only collegiate, pro-team, league and character licences.

**Out of scope but noticed.** The site sells women's, kids', golf accessories, home goods and pickleball paddles (Greyson x JOOLA). An app and a "Black Wolf" paid membership exist. The Locations page lists West Palm Beach, Detroit and New Orleans among the stores.


## Hart Schaffner Marx: full record, wave B (read 11 Oct 2026)

**Checked:** I read hartschaffnermarx.com, a Squarespace brochure site. It has five pages: Home, Retailers (`/stores`), Events (the MTM calendar), About and The HSM Fit. I also read `/sitemap.xml` and the JSON for all 143 event pages (`?format=json`). Off-site, I used trade press for ownership and checked Grailed.

**No store.** The brand sells nothing on its own site: no products, no prices, no cart, no search. So:
- Every price cell is `np`, and every men's listing URL is `NC`, because no brand listing exists.
- The fibre census is 0 styles. No product pages are published, so the fibre line verdicts are none: no lines, nothing to measure. I set `status` to `partial` for this reason only.
- I saw overcoats ($450–595), blazers and rain jackets on Nordstrom's brand page. That is not a source and nothing from it is filed. The dress shirt, dress pants and outerwear slots cannot be priced from a brand source.

**Section 4: 0 own doors (positive zero), world 0.** Locator: https://hartschaffnermarx.com/stores. The page lists "ONLINE RETAILERS" only: Dillard's, Bloomingdale's and Nordstrom, each linking to that store's brand page. There is no map widget and no locator feed. `own_doors.csv` is header-only.

**Stockists: 1 row.** Fitzgerald's Men's Store in Grand Rapids, MI, an independent. It hosted 4 MTM events (Apr and Oct 2025) listed on the brand's own calendar. The calendar is a brand page but not a stockist list, so `locator_kind` is `press/other`.

Chains with 5 or more US doors are summarised here, not written as rows. These are distinct event venues, 2022–2026:
- **Dillard's:** 60 venues (118 events, 23 states; latest 20 May 2026). Also on the Retailers page.
- **Nordstrom:** 11 venues (13 events, all 2023). Also on the Retailers page.
- **Von Maur:** 6 venues (6 events, 2023–25).
- **Macy's:** 1 venue in PA (2 events, 2024–25).
- **Bloomingdale's:** Retailers page only, no events.

The current October 2026 calendar is empty.

**Worklist conflict:** the worklist says "carried by six register shops". The brand's own pages name only one independent (Fitzgerald's). The other five can't be confirmed from a brand source.

**Owner:** ABG-HMX, LLC (Authentic Brands Group), per the site footer. ABG won the HMX IP at auction in December 2012 (MR Magazine, 18 Dec 2012). Per MR Magazine (2 Aug 2018), Peerless Clothing International holds the men's tailored clothing licence, alongside dress shirts, neckwear and boys' tailoring. The same 2018 report says W Diamond Group would keep manufacturing in a new Des Plaines, IL plant. That is press only. I did not verify the 2026 manufacturing arrangement, and the brand names no factory.

**Craft 2 / Tech 1 (proposed).**
- Craft: dated, placed heritage (Chicago, 1887, Harry and Max Hart) and a site-level "proudly made in the USA". No named maker, mill or process, and nothing owned.
- Tech: nothing named.

**mark_as_written:** Hart Schaffner Marx. I read it from the page title and footer; the logotype is an image and I did not read it.

**Not reached:** Vinted (the brand URL served a generic catalogue). B Corp and GOTS were checked by search only; I did not open the directory.

## Flags for merge
- There is no first-party store, so the band can't be set from brand prices; all eight slots are `np`. Should retailer prices (Nordstrom, Dillard's) ever be admitted for licence-only houses? That is a ruling for Sebastian.
- Stockist sourced from the MTM event calendar rather than a stockist list: confirm this route is acceptable.
- styles_total 0 with NC percentages: zero means "no first-party catalogue", not "no clothing".


## Helly Hansen: full record, read 2026-10-11

**What was checked.** All reads were in Chrome, tab 39485845, on hellyhansen.com `/en_us/`. The site is a Next.js front end on Magento (Vaimo).

**Own doors (section 4).** The store finder (`/en_us/store-finder`) is a Locally widget, company_id 58. I read its `conversion_data` feed in the tab from 56 map centres until no new ids appeared: 9,929 unique points worldwide, 3,794 of them in the US.
- **US: 13 Helly Hansen-bannered rows. 9 own doors:** Denver, Boulder, Breckenridge, Vail, Beaver Creek, Park City, Annapolis, Newport and Boston Seaport. **4 outlets:** Fashion Outlets of Chicago, SF Premium Outlets (Livermore), Woodbury Common, and Seattle Premium Outlets (Tulalip). The outlet calls come from the venue, because the feed has no format field. The Tulalip row is named only "Helly Hansen". I identified its venue from the address (10600 Quil Ceda Blvd).
- No concessions or pop-ups are listed. Lat/lon are the locator's own.
- The worklist claim "own US stores" is confirmed.
- **World:** 48 non-US HH-bannered rows after dropping 2 duplicates (Courmayeur is listed twice; Warsaw Annopol 2 is listed twice under two names). That is 35 own doors and 13 outlets, so `own_doors_world` = 44.
- I excluded dealer rows that carry HH in their name: Cabesto HH/Musto, Au Vieux Campeur HH Winter, Tamec Helly Hansen Workwear, El Corte Inglés/HH Marbella. Musto (also HH-owned) has its own Locally account and is not counted.

**Stockists (section 5).** Same feed. US non-HH rows were deduplicated by id.
- Chains with 5 or more US doors are summarised here instead of written as rows: Tractor Supply Co. 1,891; REI 192; Sportsman's Warehouse 133; West Marine 109; Nordstrom 89 (department store); Murdoch's Ranch & Home Supply 47; Christy Sports 37; Erik's 34; Sun & Ski Sports 31; Work 'N Gear 29; Mountain High Outfitters 27; Work World 22; Scheels 19; Dick's Sporting Goods 15; Sports Basement 15; D&B Supply 15; Coastal Farm & Ranch 15; Four Mountain Sports 13; Ski 'N See 13; North 40 Outfitters 11; Russell's Western Wear 9; Whistle Workwear 9; C-A-L Ranch Stores 8; Peter Glenn 8; Backcountry 8; Alaska Industrial Hardware 8; Buckman's 7; Boyne Country Sports 7; The Paper Store 7; Epic Mountain Gear 7; evo 6; JAX 6; Vail Sports 6; High Country Outfitters 5; Saint Bernard 5; Lenny's 5; Big Ray's 5; Eastern Mountain Sports 5; Cabela's/Bass Pro 5; Heavenly Sports 5; BlueZone Sports 5; Westerlind 5; Boot Country/Work Country 5.
- That leaves **876 rows** in `stockists.csv`. I dropped 2 Locally test stores ("Tims Test Store", "Locally Test Store #5").
- The feed has no shop type, so `shop_kind` is my reading of the name. The list is heavy with workwear, industrial, farm, marina, resort and club accounts; most of the Tractor Supply and workwear chain doors are probably HH Workwear distribution. The note column flags non-clothing names. Apply the register tests before merging.
- **Transfer:** the proxy blocked a direct download (CONNECT 403). I copied the rows out of the tab in pages of 100 and checked the counts: 889 rows exported, 876 written plus 13 dropped (8 AIH and 3 Christy Sports rows that belong to the summarised chains, and the 2 test stores).

**Prices and listing links.** I took full prices from Magento `regular_price`, the minimum across variants, in USD. Shoes sell in the US but there is no loafer, so the shoe slots are a range. There are no jeans and no dress shirt or dress trouser: jeans are `NONE`, the shirt slot uses casual woven shirts, and the trouser slot uses the single chino.

**Fibre (section 3).** The census is complete for the men's navigation: Jackets 196, Midlayers 84, Pants 100, Tops 89 and Base Layer 41 give 430 unique articles. I removed 1 pack, which leaves **429 styles**, keyed by 5-digit article number.
- Composition comes from the Magento `fiber` field. It matches the rendered "Fiber content:" row on the PDPs I checked.
- 427 of 429 state one. The two that do not are the Ægir Ocean Dry Suit 2.0 and the LIFA Merino Boxers.
- **15% natural, 85% synthetic, 0% cellulosic.** 95 styles contain elastane, 83 of them at 5% or more. The shape is **split**: tees, hoodies and sweaters are natural-led, and every jacket, pant, fleece and polo category is synthetic-led. Swim is 4 trunks and board shorts.
- **Lines, wholly synthetic:** Ægir, Odin, HP, Infinity, LIFALOFT, Alpha, Verglas, Daybreaker, Solen, ULLR, Sogn, Versalite, Ridge, Escape. Together that is 161 of the 429 styles.
- **Lines, mixed:** LIFA (17 synthetic and 12 merino-led of 30), Crew, Koster, The Ocean Race, Arctic Ocean, HH Tech.
- **No line is all-natural.** I took lines from series names in titles; 136 styles sit in no named line.

**Owner.** Verified from Kontoor filings: the acquisition completed on May 31, 2025 (10-Q for Q2 2025), bought from CTC Triangle B.V. for CAD 1.3 billion (about USD 960 million). The 8-K exhibit of June 2, 2025 announces completion.

**Not reached:** lookbook, Vinted, Grailed, B Corp and GOTS (all `NC`), and colourway ratio. The supplier list on hellyhansen.com was not opened.

## Flags for merge
- **HH Workwear.** It is not sold under Helly Hansen on the US store. It has its own domain (hhworkwear.com), and the US men's navigation has a hidden, empty "workwear" category, so it is not counted. The brand locator does mix workwear dealers in (Tractor Supply, Work 'N Gear and others).
- **Vail.** The store is listed under a separate Locally account (101960) that also lists a Kjus and an Oakley store. It is likely run by a third-party resort retailer, but no operator is named. I kept it as an own door with a flag; it may want `held`.
- **Non-US doors.** World counts take Helly Hansen-bannered rows at face value. The locator does not state which non-US stores are franchises.
- **Suspicious compositions, filed as read and flagged:** 5 styles list no "Shell" part. The Gravity and Powdreamer 2.0 jackets list lining only; the Legendary pants, Sogn Bib Cargo and ULLR D Bib list "Shell 2" only. The main line was taken from the first listed part.
- **Unisex items.** 22 Unisex or ungendered items in the men's navigation are counted.
- **Tech 5 / craft 2 as proposed.** Tech 5 rests on an owned, dated technology stack named on 44% of the range. Craft 2 because there is no owned or named making and no country of origin.
- **Mark.** `mark_as_written: Helly Hansen`. The logotype is set in capitals.


## Helmut Lang: full record, wave B batch 3 (read 11 Oct 2026)

**What I checked.** I read the US store at www.helmutlang.com, region United States, in USD. It runs on Salesforce Commerce Cloud (`Sites-helmutlang2_US-Site`).
- Men's Shop All shows 223 tiles. Two pages (start 0 and start 200) reconcile to that count.
- I also read the seven men's category pages and five line pages (Wardrobe Capsule, Chino Twill, Cotton Poplin and Denim, Wardrobe Jeans, Saddle Jeans).
- For all 233 men's colourway ids I read the site's own Product-Variation JSON (material, price, manufacture country). Six rendered PDPs were checked against it by hand, and the "Composition:" lines match.
- I also read the About and FAQ pages, the FW26 lookbook page, the Fast Retailing Group Modern Slavery Statement 2025 and the MAK (Vienna) CV of Helmut Lang.

**Section 4 (doors).** These are carried from the ruling and not re-read: own_doors_us NC, own_doors_world NC, locator https://www.helmutlang.com/. The ruling on 10 Oct is that the field stays NC and no press or Wikipedia figure is substituted. worklist_conflict: the worklist says there is a NYC store, which is not established. I did not look for a door count anywhere else.

**Prices (all USD, 7 of 8 slots).** Shoes are NONE: site search for shoes, loafer and sneaker returns nothing, and boots returns only bootcut jeans. No slot has an elevated-fibre pair, so every slot is `range`.

About half the range (78 of 148 styles) is only on sale. Those prices are filed at the compare-at (list) price. I checked that list price against full-price colourways of the same style: Relaxed Shirt is $368 and Utility Parka is $498, and both match.

- **Tee:** $98 Wardrobe Tee to $368 Shirt Layer Tee.
- **Polo:** there is no polo category, so the link goes to the Tees parent. The range is $268 Piqué Polo (compare-at) to $448 Distressed Rib Polo, which is a knit.
- **Dress shirt:** Helmut Lang makes no formal shirt, so these are casual long-sleeve point-collar "Relaxed" shirts, $368 to $428.
- **Jeans:** $278 to $598. The $598 is the Crushed Bootcut, a metallic-yarn twill sold only on sale. The dearest jean at current full price is $368.
- **Dress pants:** wool tailored trousers, $368 to $498. Leather Utility Pants ($1,195) are excluded.
- **Sweater:** crewnecks, $298 to $428. No crew is majority cashmere. The 70/30 wool-cashmere Brushed Crewneck is $395.
- **Outerwear:** $378 denim trucker (compare-at) to $1,998 Distressed Leather Jacket (compare-at). The dearest at current full price is the $1,398 Leather Moto. Blazers, shirt jackets and overshirts are excluded, and so is the Shearling Vest ($1,595), because it is fur-on.

**Fibre (complete).**
- 148 men's clothing styles, counted by product code. The site prints the code in each PDP's Details list, e.g. Q06HM104. The 221 clothing colourway tiles reduce to 148 styles. Accessories are out: one belt and four bags (women's or unisex leather goods under men's Accessories).
- All 148 styles state a composition. The split is 93% natural, 5% synthetic, 2% cellulosic.
- Only one style has spandex: the Mesh Layered Tee (20% elastane). There is no swim.
- Shape is **one**. No category of ten or more styles is synthetic-led. Trousers are the most synthetic category: 3 of 15 are polyester-led wool blends.
- **Line verdicts:**
  - The Wardrobe Capsule (13 styles, wool gabardine tailoring plus jeans and tee), Wardrobe Jeans (7) and Chino Twill (5) are **all-natural**.
  - Cotton Poplin and Denim (9) is **mixed**, at 89% natural: 8 of 9 styles are natural-led, which is just under the 90% bar. The one exception is the Tencel camp shirt, which is cellulosic-led.
  - Saddle Jeans (3) is under the five-style floor.
  - 117 styles sit in no named line.
  - No line is wholly synthetic.
- Two styles carry 9% metallic yarn (Crushed Bootcut Jeans, Crushed Carpenter Jacket). They are filed as written and flagged in the style note.

**Stockists.** There is one `none` row. The brand lists no other shops: no stockist page, and /stockists/, /stockist/, /retailers/ and /where-to-buy/ all return HTTP 410. The footer and FAQ have no retailer or store link.

**Proposed craft 2 / tech 1.**
- Craft: no maker, mill or owned facility is named. The manufacturing country is stated on 142 of 148 styles (Vietnam 87, Portugal 40, China 8, India 4, Peru 2, Turkey 1), and fabric-origin countries are stated too. The founding is dated (1986) but not placed on the brand site, and no making process is documented. That is a 2.
- Tech: no owned or licensed performance technology is named. TENCEL is named on 3 styles, but it is a fibre trademark, not a performance technology.

**Ownership (from the filing).** The Fast Retailing Group MSS 2025 (signed 28 Jan 2026 by Tadashi Yanai; US statement dated 3 Feb 2026) says Helmut Lang New York LLC is a wholly owned subsidiary of Fast Retailing USA, Inc., which is itself wholly owned by Fast Retailing Co., Ltd. It sits **beside** Theory LLC, not under it. The worklist shorthand "Fast Retailing (Theory)" is right about the parent but imprecise about the chain. In Japan the brand is sold by Link Theory Japan (Fast Retailing group page). The site footer names the operating entity as Helmut Lang New York LLC.

**mark_as_written:** HELMUT LANG. The logotype and copyright line are in capitals; the copy writes Helmut Lang.

**Not reached.** Vinted is NC. The B Corp directory and GOTS database were not checked directly; both are NONE on the brand's own claims. "Organic cotton" appears on 10 styles with no certification named.

## Flags for merge
- **Sale-only stock.** About half the men's navigation range is sale-only past-season stock: the P- and Q01–Q05 codes, all still in Shop All. Following the standing rule, it stays in the census and the compare-at prices stand. The jeans and outerwear highs (Crushed Bootcut $598, Distressed Leather $1,998) both come from it. If the thread prefers current full-price highs, they are $368 and $1,398.
- **Polo and tee highs.** These are knit-polo and layered-tee pieces. The standing rules don't settle whether they count as the staple.

**Out of scope, noticed.**
- The FW26 lookbook mixes men's and women's looks. It includes a women's Shearling Bomber at $2,498 and a Sculptural Coat at $1,198.
- The men's Accessories nav carries four women's or unisex bags.


## Hoka: full record, wave B batch 3 (read 2026-10-11)

**Mark as written:** HOKA. The storefront title reads "| HOKA®" and Deckers writes HOKA®. The key stays `Hoka`, and `note` carries `mark_as_written: HOKA`.

## The block (read this first)
- **What happened:** www.hoka.com/en/us/ opened normally at the start (no "Access is temporarily restricted" this time). Midway through reading product pages, it began serving a **DataDome challenge**:
  - `fetch` returns HTTP 403, a 768-byte page titled "hoka.com" whose body reads "Please enable JS and disable any ad blocker".
  - A normal page load shows only a captcha iframe.
  - The first 19 PDPs went through at about 250 ms spacing, sequentially. The block started on the 20th.
- **Retries:** at about +15, +30, +45, +55 and +65 minutes. It was still blocked every time. I did not attempt the captcha.
- **NC because of the block:** `search_url`, the sweater and shoe price cells, 13 of the 32 style compositions, heritage and founding, lookbook, and signature product. Status is `partial`.

## What was checked
- **Store:** hoka.com/en/us, Salesforce Commerce Cloud (Sites-HOKA-US), USD. Category grids return the full set with `?start=0&sz=200`. Tiles are per colourway; product codes are 7 digits, and two carry a `P` suffix (1173530P, 1173510P).
- **Men's clothing census:** men's nav Tops (12 masters / 35 tiles), Bottoms (11 / 23, which includes the 7 in Shorts) and Outerwear (`mens-outwear`, 9 / 13).
  - Total: **32 styles** and 71 colourway tiles. Every grid also carries 6 shoe tiles from the menu, which were dropped.
  - Socks, hats and accessories are out of scope. "View all apparel & gear" says 65 products and serves 64 tiles; it adds only socks, hats and packs to the clothing set.
  - 1 all-gender tee (Mosaic Logo) sits in men's Tops and is counted.
- **Fibre (partial):** 19 of 32 PDPs read; composition is in the Fabric accordion (`.material-container`).
  - 16 are synthetic-led (polyester or nylon).
  - 3 are cotton tees. Two of them state only "Responsible Cotton" with no percentage, filed as named fibre on the Belstaff precedent.
  - 0 are cellulosic-led. The Essential Tee and the Recovery Pant carry 9–11% lyocell.
  - 14 have elastane, all at 5% or more.
  - Filed figures: natural 9%, synthetic 50%, NC 41% (13 styles, all of Outerwear plus 4 shorts).
- **Fibre lines:** read by title series: Race Day (4), EveryRun (3), Novafly (3), Glide (2), SkyFlow (2), SkyFill (2), Woodland (2), Essential Recovery (2).
  - **None has 5 or more styles, so no line gets a verdict.**
  - The headline: every running line read is wholly synthetic (recycled polyester with elastane). The only natural pieces are three logo cotton tees in the lifestyle corner of Tops.
- **Prices:** regular prices are taken from the listing tiles read before the block (tiles show the original price beside any sale price).
  - Tee: $38–79, range.
  - Polo, dress shirt and jeans: `NONE`.
  - Dress pants: $108, single (hike pant, flagged).
  - Sweater: `NC`.
  - Outerwear: $118–448, range.
  - Shoes: `NC` (the shoe grid was never reached).
- **Doors:** carried as given (12 own-door + 4 outlet, world NC). The locator was not re-read for doors.
- **Stockists:** stores.hoka.com runs on Locally. One `conversion_data` call (company_id 1428, map centre 39.8,-98.6, diag 3000) returned 5,366 markers; regional re-queries for AK, HI, PR and three US regions added none. The US and PR breakdown:
  - **4,865** markers in all.
  - **18 excluded:** 17 HOKA-named own or outlet doors (section 4's business), plus "Deckers Retail Store" in Goleta (the parent's own store).
  - **86 banners of 5+ US doors (3,616 doors) are summarised below** instead of written as rows.
  - **1,231 rows** are in `stockists.csv`. Of these, 3 are small department stores, 6 are other brands' own doors (L.L.Bean ×4, Toad&Co, Goldwin) and the rest are independent. Medical, uniform and safety-shoe shops, warehouses, and Public Lands (a DICK'S banner with 3 doors) are flagged in the row note.
- **Owner:** Deckers Outdoor Corporation. The 10-K for 2013 records a noncontrolling interest bought in May 2012 and the remaining interest acquired in September 2012.
  - The FY2026 10-K: "Independent third-party contractors manufacture all of our products"; production is predominantly in Vietnam and Indonesia.
- **B Corp:** no. The bcorporation.net directory has no Hoka or Deckers entry under either query.
- **Vinted:** brand id 5827029. All 9 sampled items carry it.
- **Grailed:** /designers/hoka (2.8k listings).

## Chains of 5 or more US doors (summary, not rows)
DICK'S Sporting Goods 713 (incl. House of Sport-named and one Warehouse Sale row; "DSG House of Sport" 11 separately), Foot Locker 345, Fleet Feet 283 (franchise), JD Sports 245, Hibbett 207, REI 192, Kids Foot Locker 157, Journeys 146, Tradehome 142, Nordstrom 89 (department store), Shoe Station 82, Brown's Shoe Fit 77, Bass Pro Shops 61, Road Runner Sports 49, Champs 48, Fit2Run 42, Von Maur 37 (department store), SCHEELS 35, Saf-Gard 32, Sun & Ski 31, Mountain High Outfitters 30, Marathon Sports 27, Rogan's 25, Beck's Shoes 25, Cabela's 21, Gearhead Outfitters 21, Half-Moon 17, Big Peach 15, Sports Basement 15, Lucky Feet 13, Second Sole 12, Comfort One 12, Mast General 12, PR Run & Walk 10, Runners Roost 10, Big River 10, Schuler 10, Footwear etc. 10, Shoe Fly 10, AppRunCo 9, Great Outdoor Provision 9, Parts Unknown 9, City Jeans 9, High Country Outfitters 8, Shoe Mill 8, Peter Glenn 8, Happy Feet 8, Bootlegger's 8, GB Shoes/Houser 8, Elliott's 8, Lebo's 7, Fitness Sports 7, Gazelle Sports 7, Universal Athletic 7, Charm City Run 7, Pants Store 7, TYLER'S 7, Pacers 6, Columbus Running 6, Sound Feet 6, Runner's Depot 6, Running Wild 6, Vulcan Boot Camp 6, and 23 banners at exactly 5 (Lucky Shoes, Foot Traffic, Pro Bike + Run, Al's, Sole Provisions, A Snail's Pace, Lucky Road, Dick Pond, Whole Earth, Orleans Shoe, Foot Solutions, TC Running, Englin's, Alabama Outdoors, EMS, Sunset Shoes, Queen City Running, Westerlind, Martin's Family, Natural Comfort, Shoe City, Hawley Lane).

Banners were grouped by name prefix. Some 2–4-door groups (Houser Shoes, Runner's Roost NY, the Christy Sports rows) remain as rows.

## Flags for merge
1. **The block.** A human read is needed for the shoe prices (no loafer is expected, so `range`), the sweater candidate (Kaitoro Knit Crew, $75–87 on the tile, listed under Outerwear) and the 9 outerwear and 4 shorts compositions.
2. **Tee high.** The Race Day Short Sleeve tile reads $79–$100 across two colourways. $79 is filed. The $100 colourway was not opened, so I could not tell whether it is regular range or a special edition.
3. **Dress pants.** Hoka has no dress trouser and no chino. Woodland Hike Pant ($108, polyester ripstop) is filed `single` on the Converse "Straight Leg Pants" precedent. `NONE` is the alternative.
4. **Band-setting.** Hoka sells no dress shirt and (pending the knit crew) no sweater, so trousers and outerwear decide.
5. **Quote.** The only first-party line reachable is Deckers writing for HOKA on deckers.com/brands. Hoka's own Our Story page was blocked. Replace it if hoka.com reopens.
6. **Worklist `why` = "own US stores opening".** The locator now lists 12 open own doors; `why` reads as stale.

## Not reached (NC)
Search URL, sweater and shoe prices, the 13 compositions, founded year, place and founders, lookbook, GOTS, signature product, pronunciation, and quote date.

## Out of scope but noticed
- **Deckers' own store count:** the FY2026 10-K counts 62 HOKA brand retail stores worldwide, concept plus outlet combined. This is a filing, not a door source.
- **Fashion stockists:** Kith (4), Dover Street Market (NY, LA), Concepts (Boston, NYC), Extra Butter, Bodega, nepenthes NY, Notre, XHIBITION, SOMEWHERE and Luft sit among the running shops. They matter for the register.
- **Feed size:** the Locally feed carries 501 non-US markers (CA, MX, IS, FO, MQ, AW, FR, GL). This is stockists only, and world doors were not my section.

## Retry 2026-10-11
- **Access:** hoka.com was open again, with no DataDome challenge and no 403. The retry ran from about 11:15 to 11:38 local. It read the listing pages first: the `mens-shoes` grid (`?start=0&sz=200`, 98 products) and the `mens-outwear` grid. Then 16 PDPs, each navigated singly about 7 s apart (no fetch loops). Doors and stockists were not touched.
- **Tee high: $100**, Race Day Short Sleeve in the Hoka Citrus Prt colourway. With size M selected on the PDP, Citrus Prt reads $100.00 at full price. Alabaster Flare reads $98.00, marked down to $79.00 (19% off). **The $79 filed earlier was a sale price.** The tile range hides markdowns that carry no strike-through, so the tile reads $79–$100.
- **Sweater: `NONE`.** The Kaitoro Knit Crew ($75–87) is 47% recycled poly, 47% TENCEL and 6% elastane, with a kangaroo pocket with an internal zip and a ribbed neck and cuff. That makes it a sweatshirt-type crew, not a crewneck sweater. Its style row moves from knitwear to sweats.
- **Shoes: `range`** (no loafer).
  - **Low: $60**, ORA Recovery Flip. The tile shows a single price. The ORA Recovery Slide 3 tile reads $48–60; on the PDP, Black and Alabaster are $60.00 while Neon Flame and Sea Glass are $60.00 cut 20% to $48, so its regular price is also $60.
  - **High: $280**, Kaha 2 Frost GTX, at a single tile price.
  - **Excluded:** Rocket X 3 John Elliott ($260) is a collaboration.
- **Compositions:** all 13 were read.
  - The Transport Jacket GTX states none: "GORE-TEX 3L" and a tricot lining only. It is filed `ND`/undisclosed.
  - SkyFill Jacket and SkyFill Vest have no Fabric section. Their shell ("100% recycled polyester") is taken from the Features bullet; the 79/21 side panels are excluded.
  - On the SkyGlow Half-Zip, the main line was read; the house misspells it "Polyster".
- **Fibre roll-up, recomputed:** 32 styles, 31 with a composition.
  - Lead fibre: natural 9%, synthetic 88%, cellulosic 0%. The remaining 3% (1 style) states no composition.
  - Stretch: 20 styles have elastane, all at 5% or more.
  - Shape: `one`. Synthetic leads in Tops, Bottoms and Outerwear; natural categories `[]`.
  - Lines: still none with 5 or more styles. Every line read is wholly synthetic.
- **Still `NC`:** `search_url` (not in the retry scope), so status stays `partial`. Also unchanged from the first read, outside sections 1–3: founding, lookbook, GOTS, signature product, pronunciation and quote date. `tech_share_of_range` still describes the 19-PDP read. The retry PDPs add PrimaLoft (SkyFill, Basecamp), Aeroshell (SkyFlow Wind), Lycra Adaptiv and HeiQ Mint (Race Day Half Tight, Trail Race Short); they were not rolled into the tech cells.
- **Flags for merge (retry):**
  1. Sweater is `NONE` (sweatshirt ruling). The alternative is `single` at $75 or $87 for the Kaitoro, with the regular price per colour unconfirmed.
  2. Tee high is $100 against $98 for the two Race Day colourways. Citrus Prt is a print colourway in the regular grid, not marked limited.


## Human Made: full record, wave B (read 11 Oct 2026)

**What I checked:** humanmade.jp in Chrome. It runs on Salesforce Commerce Cloud with Global-e and serves a US visitor USD prices server-side. I read:
- the HUMAN MADE STORES page (`/en/dealers.html`), which is the brand's own world store and stockist list
- all 60 pages of brand news, searched for stores, pop-ups and US posts
- the NYC pop-up post
- 8 clothing category listings plus shoes and collaboration (sz=500, one tile per master style)
- 365 of 366 PDPs, for the MATERIAL / MADE IN block
- the About page
- off-site: the IR site at ir.humanmade.co.jp (stock information, company overview, CEO message, executives) and Grailed

**Section 4 (yours):** 0 US own doors. This is a positive zero, and it is a worklist_conflict with the claim "NYC store". The brand's list has a USA section, but it holds stockists only. I filed one US row in own_doors.csv: the HUMAN MADE New York Pop-Up Store at 60 White St, Tribeca. It ran 11–12 Nov 2023 and is filed as `pop-up` / `closed`, so it is not counted. That matches the accepted correction.

World: 14 HUMAN MADE-banner doors.
- Japan 9, including the new HUMAN MADE TOKYO flagship
- South Korea 3
- Bangkok 1
- Hong Kong (Repulse Bay) 1

Operators are not stated. HUMAN MADE HUAIHAI in Shanghai (2023 news) is absent from the list, and a China flagship is announced for spring 2027. A ComplexCon booth (Long Beach, 2022 news) is a trade-show booth, not a store, so it has no row.

**Prices (USD as served; JPY base in return.csv note):**

| Garment | Basis | Price | Product |
|---|---|---|---|
| Tee | range | $42 | Striped Pack T-shirt |
| | | $190 | Embroidered T-shirt |
| Polo | single | $170 | |
| Dress shirt | range (casual BD only) | $205 | Oxford BD |
| | | $540 | Embroidered Chambray |
| Jeans | range | $280 | |
| | | $445 | Denim Cargo |
| Dress pants | range (chinos / wool trousers) | $260 | |
| | | $335 | |
| Sweater | pair | $245 | merino |
| | | $420 | Lowgauge |
| Outerwear | range | $245 | Track Jacket |
| | | $1,600 | cow-leather jacket |
| Shoes | single | $245 | DUCK KICK |

All 8 slots are filled. No collaboration is used anywhere.

**Fibre:** 340 clothing styles by product code, with 339 compositions read.
- Overall: 87.9% natural, 8.5% synthetic, 3.2% cellulosic. 3 styles carry elastane, all at 1–2%. Shape `one`.
- Synthetics sit in outerwear (19 of 63: nylon coach and track jackets, down shells) and are not a majority anywhere.

Line verdicts:
- COLLABORATION ITEMS: 43 styles, 41 natural-led, all-natural.
- Ningen-sei (the Japanese-craft dyed collection): 11 styles, 10 natural plus 1 rayon, all-natural at 91%.
- HUMAN HOPE (j-hope): 8 styles, all-natural.
- ONLINE EXCLUSIVE: 13 styles, all-natural.

279 styles sit in no named line.

**Stockists:** 13 US rows from the brand's list, which gives names and cities only (no street):
- Dover Street Market NY and LA
- Union LA
- Billionaire Boys Club NY and Miami (another brand's own door)
- Somewhere DC
- Feature in 4 cities
- A Ma Maniere Atlanta and Houston
- Hirshleifers

No chain reaches 5 listed US doors. The online stockists listed (Mr Porter, HBX) are not US shops and have no rows.

**Craft 2 / Tech 1 (proposed).**
- Craft: the country is stated on about 99% of PDPs, but no maker, mill or owned facility is named. Named processes (loopwheel, selvedge, hand-dyed kakishibu and indigo) are claims, not evidence.
- Tech: no technical fabric is named.

**Owner:** HUMAN MADE Inc., listed on TSE Growth (456A) since 27 Nov 2025. I did not read major shareholders: the half-year report is a PDF that the tab would not render. Founded 2010 by NIGO; the company was set up in 2016 as OTSUMO Co., Ltd.

**Not reached:**
- Vinted (generic catalogue, NC)
- B Corp (directory page did not load, NC)
- GOTS (NC)
- colourway ratio (NC)
- HM31JK010 PDP (HTTP 403, three tries)

**mark_as_written:** HUMAN MADE

## Flags for merge
1. **Currency.** The store serves USD to a US visitor through Global-e, while the catalogue base is JPY (tax incl). I filed USD as the US-facing price, with JPY beside each figure in the note. The rate implied by the figures is about JPY 115-118 per USD. If the thread wants "own currency" here instead, the JPY figures are on file.
2. **Ningen-sei.** This is a recurring seasonal collection (spring and summer items "interpreting Japanese traditional culture"). I treated it as a possible capsule and kept it out of the tee high. If it is ruled regular range, the tee high becomes $225 (NINGENSEI KAKISHIBUZOME T-SHIRT, HM31CS080).
3. **Dover Street Market** is filed as `independent` (a multi-brand store), not `department store`. Rule if you file DSM differently elsewhere.
4. **WZ30CS002** (SHORT SLEEVE SWEATSHIRT) carries a WZ prefix, possibly the WZRD label sold under OTSUMO PLAZA. It sits in the HUMAN MADE sweats navigation, so I kept it.
5. **Suspicious composition:** HM31JK008 SATIN JACKET has a shell that reads "58% COTTON, 2% RAYON". Filed as read.

**Out of scope, noticed:** The range is sold unisex (no gender split). Almost every listing tile carries a SOLD OUT marker in its markup, so I did not judge stock. The brand also runs CURRY UP restaurants beside several stores.


## John Elliott: full record, wave B (read 11 Oct 2026)

**What I checked:** johnelliott.co redirects to www.johnelliott.com, a Shopify store in USD with rate 1.0. I read:
- the Stores page, including the brand's own Google Maps links for coordinates
- the full /products.json (244 products) and /collections/all, which match the "Men's All" navigation
- 20 collection feeds
- About Us, the FAQ, the FW26 lookbook, and two PDPs for the price check (88 USD, 2,498 USD)
- off-site: Grailed, Vinted and the B Lab directory

**Section 4:** 2 US own doors, and the world total is 2 as listed:
- John Elliott Melrose, 8808 Melrose Ave, West Hollywood CA 90069
- John Elliott New York, 270 Lafayette St, NY 10012

There are no outlets, concessions or pop-ups. The Stores page is the brand's whole list, with no region filter, and it shows no non-US door. The worklist claim "LA store" is confirmed but understated, because New York is missing from it. Coordinates come from the brand's own map links.

**Prices (all eight filled):**

| Garment | Basis | Price |
|---|---|---|
| Tee | range | $88–298 |
| Polo | single | $168, long-sleeve OS Rugby Polo |
| Dress shirt | range | $298–598 |
| Jeans | pair (Wyatt) | $298–698 |
| Dress pants | range | $248–398 |
| Sweater | single | $398, cardigan |
| Outerwear | range | $498–2,498 |
| Shoes | range | $998–1,198, Square Toe Boot |

- **Dress shirt:** the Sedwell Dress Shirt at $448 is the only shirt the house calls a dress shirt. The $598 high is sold out in every size, and the dearest in-stock shirt is $498.
- **Dress pants:** there is no dress trouser. Easy trousers with an elasticated waist stand in.
- **Sweater:** there is no crewneck pullover. The only knit is a 90/10 wool-cashmere cardigan.
- **Shoes:** there is no loafer. The Hoka collaboration is excluded.

**Fibre (complete):** 81 styles from 232 clothing products; all 81 state a composition. 89% are natural-led, 9% synthetic-led and 2% cellulosic-led. One style has elastane. The shape is `one`, and no category is synthetic-led.
- **Line verdicts:**
  - All-natural: Mainline (23 styles), Made in Japan (17), Terry (17) and Air Spun (7).
  - All-synthetic: the Performance line, but it has only 2 styles.
  - Mixed: the seasonal collections FW26 (35 styles) and Summer 26 (26).
  - 7 styles sit in no named line.
- **Synthetic styles:** all 7 are athletic shorts, a muscle tee, and the Vero nylon jacket and pant.

**Stockists:** none listed. The FAQ mentions "our stockists", but there is no list, and the five usual stockist paths all return 404. I filed one `none` row.

**Craft 2 / Tech 2 (proposed):**
- **Craft:** the country is stated on 82% of products, across 8 countries. Cone Mills is named on 13 denim products. There is no owned facility and no named maker. A 3 is arguable.
- **Tech:** house-named fabrics only (Air Spun, Vero) plus a 2-style Performance line. No licensed tech. A 1 is defensible.

**Not reached:**
- owner_today: NC. The brand does not state its ownership, and I read no filing.
- Vinted: NC. The brand slug served the generic catalogue, and the API returned 403.

**mark_as_written:** JOHN ELLIOTT

## Flags for merge
- **A store before these two.** The NY store copy calls Lafayette Street John Elliott's "third physical location", so there was an earlier store that is not on the locator now. I wrote no `closed` row, because the locator gives no source for it.
- **Styles counted by model name.** The denim gives each wash its own article number, so for denim the article stem is a colourway. Each product handle is also one colourway. Counting by article stem would give about 94 styles instead of 81.
- **Suspicious compositions.** Two Cupro styles state 64% cupro and 34% polyester, which sums to 98%. I filed them as read and flagged them in the styles file.
- **Domain.** The worklist domain johnelliott.co is now a redirect to johnelliott.com.

**Out of scope, noticed:** The Melrose store page says it carries men's and women's collections, but the online store is men's only.


## John Lobb: full record, wave B batch 3 (read 11 Oct 2026)

**Checked:** johnlobb.com/en_us/ (US store, USD), the full Loafers category (33 products, scrolled to the end), the Limited Edition category (0 products), PDPs for Lopez 75, Bill, Tyne II, Foil, Sommet and Court, site search (sweater, knitwear, shirt, jacket, loafer), the store locator's US stockist pages (each store opened), Our Story, Lopez: Behind the Craft, the AW26 lookbook, Grailed, a Vinted search, and Modaes press on the new Northampton plant.

**Scope:** This is John Lobb Paris (Hermès). The brand's own Our Story says John Lobb Ltd (St James's, bespoke) is a separate family business.

**Section 4:** I carried the counts as given (2 US own doors, world NC) and did not re-read them. Our Story claims "19 global stores". That is a brand statement, not a locator count, so it is recorded here only.

**Clothing:** None. The navigation holds shoes, belts, small leather goods, shoe care and gifts. Searches for sweater, knitwear and shirt return 0 results. All seven garment slots are NONE. The fibre census is 0 styles (return_styles.csv is header only). Fibre verdicts: none, because there are no clothing lines.

**Shoes (pair):** $1,150 (Tyne II) to $2,920 (Bill).
- Excluded: Lopez 75 at $3,200, a 75th-anniversary edition.
- Not taken as the low: Foil at $1,100. It sits in the Loafers listing, but its PDP calls it a boat shoe.

**Stockists:** 13 rows: 8 department-store doors (Saks 5, Neiman Marcus 3) and 5 independents (Stanley Korshak, Richards, Wilkes Bashford x2, Leather Soul). Richards and Wilkes Bashford belong to the Mitchells group.

**Craft 4 / Tech 1 (proposed).** Craft: its own Northampton workshop, a documented 190-step process, and dated heritage. It is held at 4 because the trainers are Made in Italy with no maker named, and no tannery is named. Tech: the only named items are house sole names.

**Not reached:**
- Vinted: NC (brand id not resolved).
- The Hermès URD was not opened. Ownership rests on the brand's own Our Story.
- The Foundry II PDP did not render.

**mark_as_written:** JOHN LOBB

## Flags for merge
- **Stockist count:** the brief and doors_basis say "14 US Saks/Neiman entries". The locator lists 15 US entries in 10 cities: 2 own doors and 13 stockists. Also, 5 of the 13 are independents, not Saks or Neiman. doors_basis is carried verbatim as instructed. It needs correcting to 13.
- **Saks rows written as rows:** Saks has 5 US doors. The 11 Oct standing rule says to summarise a chain with 5 or more doors in NOTE.md instead, but the prompt said to write the department-store entries to stockists.csv. Both are done here: Saks Fifth Avenue 5, Neiman Marcus 3.
- **Leather Soul (Honolulu)** is a shoe specialist. It may fail register door one (clothing).


## Kapital: full record, wave B (read 11 Oct 2026). Status: PARTIAL

**What I checked:** kapital.jp: the Shop List and all 15 shop detail pages, the company profile, the SOHO page, the collection pages and the catalogue archive. kapital-webshop.jp (ebisumart, JPY, prices 税込): the Men's All listing, all 13 pages (386 unique product codes, matching the stated 386件); the ten men's sub-category nodes; one PDP. Off-site: nss magazine for the founder, Grailed, and web searches for a brand stockist list.

**What blocked the read:** kapital-webshop.jp IP-restricted the browser partway through the crawl. The 403 page says "リモートホストIPが制限されています。制限が解除されるまでしばらくお待ちください" (remote host IP restricted; wait until the restriction is lifted). The likely trigger was my sub-category pagination: past the last page those nodes re-serve page 1 rather than going empty, so the loop ran about 20 pages per node. I retried for about 60 minutes and the block did not lift. Because of the block, all price cells are NC, and the fibre census is 1 of 386 styles. A re-read must go slowly. Paginate by the stated count (件) and stop there; do not loop to an empty page.

**Section 4:** 0 US own doors. The locator URL https://www.kapital.jp/shop/search.html is a positive zero. worklist_conflict: the worklist says "NYC store", and the brand's own list has no US door. World: 15 shops, all in Japan:
- 11 own doors
- 3 concessions in Hankyu Men's Osaka 5F
- 1 pop-up, Shirokanedai KOB WEB HOUSE, labelled "EVENT POP UP HOUSE"

There are no outlets. own_doors.csv is header-only, since the file takes US rows only.

**Stockists:** The brand publishes no list of other shops, so stockists.csv has one `none` row. US accounts appear only on third-party sites, not on the brand's own list.

**Craft 4 / Tech 1 (proposed).**
- Craft: The company profile names four owned sewing factories (本社, 御津, 山城, 柳田) and its own dyeing works (カントリー工場) in Kojima/Okayama, established March 1985. These are named, not an unnamed claim. Mills, makers and made-in coverage are unverified because of the block. 5 is defensible if PDPs tie the range to those factories.
- Tech: no technical fabrics seen. Low confidence.

**Fibre line verdicts:** none computed (1 style read: the 11.5oz denim coverall, cotton 100%).

**mark_as_written:** KAPITAL.

## Flags for merge
- Price section unread: kapital-webshop.jp IP block. Needs a slow re-read from a fresh session.
- The webshop PDP carries a hidden `sale_rate` "50%引き" element on a full-price (`teika`) item. It is display:none furniture; a parser must not read it as a markdown.
- Founding year: the brand gives 1985 (company established); press gives 1984 (nss magazine). Filed 1985.
- Quote is in Japanese (house voice, SOHO page). Translation: "Good old things (SOHO) symbolise the spirit of learning from the old to know the new, the root of our creation." Sebastian to rule on a Japanese-language quote.
- B Corp/GOTS NC: the B Lab directory did not render through the fetch tool.

## Retry 2026-10-11
Retry 2026-10-11: still IP-restricted at 11:32 EDT. One load of https://www.kapital-webshop.jp/ (page title "エラー") showed the same message: "リモートホストIPが制限されています。 制限が解除されるまでしばらくお待ちください。" I stopped at once and made no further requests. Prices (8 garments) and the fibre census (1 of 386) remain NC. Named mills, makers and made-in share remain unverified. Doors not touched. Status stays partial.


## Kenzo: full record, wave B batch 3 (read 11 Oct 2026)

**Checked:** US store www.kenzo.com/en-us (Salesforce Commerce Cloud, site KENZO_US2, USD). The men's All Ready-to-Wear grid (389 colourway tiles) and all nine men's categories were paged through the Search-UpdateGrid route at 40 a page; every category matched its stated count. One PDP per article number was read (311 PDPs: composition panel, country of making, JSON-LD price). Also read: men's shoes grid (27 tiles), store finder and All Stores directory, heritage pages (Kenzo Takada's House, East meets West), FW26 and SS27 lookbooks, the Nigo London Museum page, the LVMH maison page, and Grailed.

**Section 4:** Carried as instructed and the locator was not re-read: US 0 own doors (positive zero), 3 outlets (Cabazon, Las Vegas North, Woodbury), 117 non-US listed with formats not split, world NC. worklist_conflict: worklist says US stores. The LVMH maison page gives "104 stores around the world". That figure is from the parent company, so it is noted here and not used.

**Prices:** All 8 slots read. No markdowns on any PDP. Collaborations (Converse and Paraboot on the SS27 page) and the Nigo London Museum limited editions are not in men's navigation and were not priced.
- Tee $160–545 (range).
- Polo $225–545 (range).
- Dress shirt $405–685 (range). Kenzo makes no dress shirt, so casual long-sleeve button-fronts are used.
- Jeans $490–825 (range).
- Dress pants $630–825 (pair: virgin wool, then wool-silk).
- Sweater $490–685 (range). There is no elevated-fibre crewneck.
- Outerwear $630–905 (pair: the same coach jacket in nylon, then cotton-silk).
- Shoes $605 (single). The Citygram loafer is the only loafer.

**Fibre (complete):**
- 304 men's clothing styles, all with composition, from 387 colourway tiles. Styles are counted by article number.
- Split by fibre: 88% natural, 9% synthetic, 3% cellulosic. Spandex appears in 4 styles, none at 5% or more. There is 1 swim style.
- Shape is **one**. Outerwear is the most synthetic category at 37%, but it is still natural-led.
- **Line verdicts** (lines are the house's quoted motif series in titles, plus Kimonos from navigation):
  - All-natural: Boke Flower (21 styles), KENZO Jumping Tiger (19), KENZO Tulip (19), KENZO Loves (14), KENZO Paris Emblem (11, 91%), KENZO Wildflower (10), Eiffel Tower Design (9), Double K (7), Apple Pop (6). Together that is about 116 of 304.
  - Mixed: KENZO Signature (44, 86% natural), KENZO Sounds (21), Boke Flower 2.0 (17, 41% synthetic from track pieces and windbreakers), Kenzogram (16, 31% synthetic), Kimonos (14, viscose-wool kimonos), Varsity (13), Checks (6).
  - No line is wholly synthetic. 45 styles sit in no named line.

**Stockists:** None listed. There is one `none` row: the locator lists KENZO-banner doors only, and /stockists and /retailers return 404.

**Proposed craft 2 / tech 1:**
- Craft: every PDP states the country (Portugal 116, Tunisia 71, China 52, Romania 28 and six more). No maker, mill or owned factory is named. LVMH says a "workshop" sits in the rue Vivienne head office, which is a claim, not evidence of making.
- Tech: water repellency and UV resistance are unbranded. No membrane or insulation is named.

**Owner:** LVMH, read from the LVMH maison page, not from the annual report itself.

**Not reached:** Vinted is NC (generic catalog, no brand id). The B Corp and GOTS directories were not checked (NONE is on the brand's own claims).

**mark_as_written:** KENZO

## Flags for merge
- **Tee low.** The $160 KENZO Sport T-shirt (FG65OTS43401) is in men's All Ready-to-Wear but not in the T-shirts category. Its code carries an "O" infix, as do a few other see-all-only pieces (FG55OPU193LC, FG55OCA183LC). If Sebastian rules these out, tee low becomes $170 (Boke Flower 2.0 T-shirt, FF55TS2004SG).
- **Sweater.** No crewneck is majority cashmere. The 70/30 wool-cashmere Double K jumper is $545, which sits below the $685 cotton-wool cable crewneck filed as high. This matters for the band rule, so it needs a ruling.
- **Genderless pieces.** Three have a WOMEN breadcrumb on the PDP but sit in men's navigation, and they are counted.
- **Older-season article prefixes** (FE65, FF55, FF65, FG55) are still in men's navigation, and they are counted.
- **Suspicious compositions:**
  - The Japanese Garden cardigan (FG65CA8143FD) composition sums to 91%.
  - FG65PA5614MX and FF55TS2004SG list a 0% component.
  - The varsity jacket "in wool and leather" (FG65BL1969ON) states 100% wool only.
  - All are filed as read.
- **Shoes in the Tailoring category.** Five shoes appear in men's Tailoring. They are excluded from clothing.
- **Accessories in men's RTW see-all.** A poncho and a pareo appear in men's RTW see-all. They are excluded as accessories, following their own breadcrumb.

**Out of scope, noticed:** The LVMH maison URL in circulation (/fashion-leather-goods/kenzo) 404s; the live path is /fashion-leather-good/kenzo. Several PDP titles carry typos ("windbeaker", "slik", "chasmere", "viring wool").
