# seat_wave_b — batch 1 (Aether Apparel through Church's) · 10 October 2026

## Files

- `return.csv`: 9 rows, 132 columns.
- `return_styles.csv`: 1,833 styles.
- `stockists.csv`: 2,386 rows.
- `return_counts.csv`: counts for the 6 brands whose stores were read here.
- `own_doors.csv`: 1,051 earlier rows plus 55 new, 1,106 in all.
- `held_door_counts.csv`: the earlier held-brand counts, with the rulings below applied.

All brand names match the canonical keys exactly (reconcile.py). No cell is empty, every value is from its allowed list, and every store count equals its own_doors rows (held and closed rows are not counted). Three prices were checked against the live pages: Carhartt WIP Base T-Shirt $38, Chubbies Tide Pool sweater $79.50 (filed as $80), and Balmain silk/cotton jumper $990. All three match.

## Earlier batch: rulings applied

- **Hoka** is back as listed: 14 own doors and 2 outlets. The Orlando and Las Vegas stores are flagged because the addresses look like outlet centres (your ruling).
- **G/FORE Pebble Beach** stays `held` and is not counted (10 Oct ruling, not reverted). G/FORE has 4 own doors.
- **Positive zeros** (Church's, Fred Perry, Kenzo, Maison Kitsuné) carry `worklist_conflict` notes.
- **Clarks Puerto Rico** has 7 stores, not 9. The locator holds 9 PR records, and the other 2 (A296 and A297) are entries named "Puerto Rico Warehouse".
- **Moose Knuckles** still has a probable duplicate Las Vegas outlet row. It is left in until you rule on it.
- **The `closed` status is in use from this batch.** Aether Apparel's Jackson WY store is the first `closed` row.

## Changes made at merge

- **Ariat** `own_doors_us`: the agent filed 31 (own doors plus outlets). I set it to 18 own doors so it reads the same way as the other brands. The 13 outlets are stated in `doors_basis`.
- **Belstaff** `own_doors_world`: the agent filed 23, which included 15 non-US outlets. I set it to 8 own doors.

## Rulings needed, by brand

| Brand | Question | What was filed |
|---|---|---|
| Aether Apparel | Fibre census: should the 94 archive-sale styles be included? Their pages load, but they are out of the site navigation. | Excluded: 91 styles counted |
| Aether Apparel | AETHERstream, the roving trailer pop-up | `held` |
| Aether Apparel | Craft: do licensed membranes such as Dermizax count as named mills? | 2 (3 if they do) |
| Ariat | Gretna NE is labelled Ariat Store but sits inside Nebraska Crossing Outlets | Outlet, by the venue rule |
| Ariat | Stages West, Pigeon Forge: another banner, operator not stated | `held` |
| Ariat | The 72 dealer chains (6,871 doors; Tractor Supply, Boot Barn, Buckle and others) | Summarised in this note, not written as rows |
| Asics | Craft 2 or 3: supplier factories are named at company level only | 2 |
| Balmain | Outerwear high | $9,100 embellished bomber. Alternative: $5,990 shearling |
| Balmain | Sweater: the cheapest crewneck is already majority silk | Pair, $990 to $1,650 merino |
| Belstaff | Outerwear high | $2,950 shearling coat. If shearling counts as fur: $2,095 leather jacket |
| Belstaff | Phoenix capsule left out of every high | Excluded |
| Bogner | Style count: by article number or by model | 197 by article (187 by model) |
| Bogner | Outerwear low is a FIRE+ICE mid-layer | $260. Cheapest shell instead: $450 |
| Carhartt WIP | Craft 3 or 4: brand says it owns three Tunisian factories, but none is named | 3 |
| Carhartt WIP | Sid Pant composition reads "38% Lycra", probably a site error | Counted as elastane, flagged |
| Chubbies | NFL-licensed polos | Left out of the polo high |
| Church's | Shoe high | $1,850 Royal Collection Viscount. Main-line top is Kingsley at $1,370 |
| Church's | Prada's 2025 annual report says 27 owned stores; the locator shows 23 | Locator figure (23) filed |

## Other things found

- **Belstaff** changed hands: Castore owns it, completed 28 August 2025. A record showing INEOS is out of date.
- **Bogner** is owned 60% by Katjes International and 40% by the Bogner family, from 1 September 2025. Its one US store, on Madison Avenue, opened in 2021 as a pop-up run by FlagshipRTL.
- **Asics** states fabric composition on only 12 of 233 styles, so its fibre figures are `NC`.
- **Columns left `NC`** across the batch: mostly Vinted (Vinted blocked automated lookups), B Corp and GOTS, and lookbooks.
- **Carhartt WIP** has no San Francisco store (`worklist_conflict`). **Aether Apparel** also has a Park City store, which the worklist doesn't list.

---

# Per-brand notes


## Aether Apparel — NOTE (read 2026-10-10)

**Checked**
- Section 4: read in Chrome from the brand's locator, https://aetherapparel.com/stores, and each store page. Also checked the sitemap for store pages the index doesn't link to.
- Sections 1 to 3: the men's range comes from the Shopify feed on secure.aetherapparel.com. Composition and origin come from each style's Next.js PDP payload, in the Material and Origin accordion sections. That payload matches the rendered page, which I checked by hand on the Coastal Waffle Sweater.
- Sections 5 to 13: our-story, guarantee, catalog, FAQ and Grailed.

**Doors:** 5 US own doors: LA, NYC, SF, Aspen and Park City.
- Park City (UT) is not in the worklist claim. The site carries a seasonal notice saying the store is closed 15 Oct to 25 Nov.
- AETHERstream is on the locator but is a roving trailer with no current stop. I recorded it as a `held` pop-up.
- AETHERoutpost (Jackson WY) has a store page that says PERMANENTLY CLOSED. The page is in the sitemap but not linked from /stores. I recorded it as a `closed` row.
- No non-US stores, so world is 5. The worklist claim "LA, SF, NYC, Aspen" is right but leaves out Park City.

**Mark as written:** AETHER (all caps logotype). mark_as_written: AETHER.

**Fibre:** 91 men's clothing styles (266 colourway listings). 84 state a composition. Split: 44% natural, 48% synthetic, 0% cellulosic. 24 styles contain elastane.
- Outerwear (33 styles) is synthetic-led.
- Sweaters are all natural (merino and cashmere).
- Tees, polos and henleys are mostly 100% cotton made in Portugal or Peru.
- Line verdicts: Snow is all-synthetic (5 of 10 styles disclose a fibre; the other 5 name only a membrane, e.g. "Dermizax 3L"). Motorcycle is mixed (cotton Mojave, nylon Ramble and Mulholland). Base Layers is mixed (merino blend vs Polartec polyester).
- Excluded: 94 archive style stems whose PDPs are still live but are tagged `algolia-ignore` / archive-sale and are not in navigation. A census of the full feed would roughly double the range with old stock.

**Not reached / NC**
- Vinted brand id: the API lookup was blocked by the tool.
- B Corp: the directory search did not filter in the browser.
- Owner today: no statement on the site, and I did not search filings.
- Founding place: the story gives none. HQ is LA per the LA store page.
- Pronunciation.

**Brief issues / judgement calls**
- The brand makes no dress shirt and no dress trouser. I used casual button-downs and chinos and said so in the note.
- No jeans: NONE.
- The polo listing link points to mens-tees, because there is no polo collection.
- The census uses the navigated range (mens-view-all), not the full feed (see Fibre above).

**Out of scope but noticed**
- Collaboration footwear (Fracap) is sold alongside the own-label boots.
- The Insider paid membership gives 20% off; I took list prices only.


## Ariat: note (read 2026-10-10)

**Checked**
- Own doors: ariat.com/stores (33 entries), every stores.ariat.com store page (JSON-LD address), and the Locally own-store map (ariat.locally.com, company_id 2820; 32 stores). The count is 31 US doors: 18 own-door (3 of them Ariat Work) and 13 outlet.
  - Gretna NE (Nebraska Crossing Outlets) is labelled "Ariat Store". I coded it as an outlet under the venue rule. This needs a ruling.
  - Two doors are held. Stages West, Pigeon Forge TN, is on the Ariat stores page under another banner, and the operator is not stated. Castle Rock CO "Ariat Outlet" is listed, but its store page throws "Error in exception handler", it is missing from the Locally map, and no address is published.
  - The non-US page lists distributors only, so `world_non_us` is NC.
- Prices: the PDP price and compare-at price were read for each garment. All eight garments are `range`. Ariat sells no dress shirt, dress trouser, chino, crewneck or loafer. Exclusions (FR, breeches, shirt jackets, exotics) are in `note`.
- Fibre: 695 men's clothing styles from the union of 11 men's category grids. Men-Clothing alone misses 150 workwear/FR/scrub styles. 667 of the 695 state a composition (Materials accordion on the PDP). Status `complete` for the census. The record as a whole is `partial` (see below).
- Stockists: Locally dealer feed, 9,036 US entries (+133 CA). 2,129 smaller dealers are written as rows (names with fewer than 5 US locations, after chain-variant and mall rows were dropped). The 72 multi-door chains (6,871 doors) are **not** written as rows. The largest are Tractor Supply 2,459, Boot Barn 570, Buckle 436, Academy 322, Rack Room 271, Dunham's 250 and Dillard's 242. `shop_kind` is set by rule, not checked shop by shop. Many rows are feed stores, co-ops and hardware stores, which fail register door one.

**Not reached (NC):** lookbook, Vinted, Grailed, B Corp, GOTS, signature product, pronunciation, founding place.

**Against the worklist/record:** the "own stores" claim is confirmed. "The Boot Jack Ariat Outlet" (Mercedes TX) is a dealer, not an Ariat door, and is kept in stockists.

**Brief issues**
- `own_doors_us` is ambiguous between own-door only (18) and own-door plus outlet. I filed 31 and split the figure in `doors_basis`.
- A census limited to Men-Clothing would have undercounted the range by 21%.

**mark_as_written:** ARIAT. The header logotype is set in capitals; site copy writes Ariat.

**Fibre line verdicts**
- **All-natural:** jeans fit families M2/M3/M4/M5/M7/M8, DuraStretch (90%), Pro Series and Retro. Pro Series and Retro are mostly 100% or 82–85% cotton shirts.
- **All-synthetic:** TEK/VentTEK (22 styles) and Caldwell.
- **Mixed:** Rebar (68/32), FR (77/20/3) and Team.
- Denim is 100% natural-led. Outerwear is the synthetic-led category (58% of disclosed styles), along with scrubs and the polyester "sweaters".

**Out of scope but noticed:** most of the men's range is workwear and FR PPE. FR inherent fabrics (modacrylic/aramid/lyocell) are filed as other-synthetic.


## Asics — full record, wave B batch 1 (read 2026-10-10)

**Mark as written:** ASICS (all caps, as the storefront and logotype write it). Key kept as `Asics`. Also in `note` as `mark_as_written: ASICS`.

## What was checked
- **Store:** asics.com/us/en-us, Salesforce Commerce Cloud on a PWA Kit front end. Data came from the page's `mobify-data` preloaded state. Category hits are colourway-level variation groups and carry `masterId`. Search `/us/en-us/search/?q=` works (q=jacket returned 219). USD.
- **Prices:** read from the men's clothing feed (533 hits) and from men's shoes sorted by price in both directions. The 4 garments filled are tee, polo, outerwear and shoes, all on a `range` basis. The other 4 are `NONE`: ASICS sells no dress shirt, jeans, dress trouser or chino, or crewneck sweater. Its "Sweat Crew Neck Top" is a sweatshirt. Compare-at prices were used where an item was on sale. Polos have no category of their own, so the polo link is the men's T-Shirts & Tops parent.
- **Fibre census (complete denominator, partial composition):**
  - The men's clothing feed is `cgid AA10300000` refined to `c_productArea=Clothing`. It returned 533 colourway hits, which collapse to 234 masters. One women's style (Road High Waist 8in Sprinter, 2012C967) leaked in and was dropped, leaving **233 styles**. All 234 PDP payloads were read, so the denominator is complete.
  - **Composition is stated on only 12 of 233 styles:**
    - 10 give a full composition (Thermopolis pieces, some cotton/poly graphic tees, two Resolution pieces, a French terry jogger, the Metarun packable gilet).
    - 2 give a partial figure: "main fabric contains 65% recycled polyester".
  - The other 221 give only feature bullets. Examples: "soft cotton blend", "PrimaLoft Gold", "at least 50% recycled content". Composition only ever appears in `productSpecs.technology`, which is the Materials & Technology accordion. `productSpecs.fabric` and `countryOfOrigin` are empty on all 234. I checked rendered pages against the payload on 3 PDPs: they matched.
  - Status is `partial` at about 5% coverage. `shape` and the category lists are `NC` because no verdict can be drawn.
  - Product titles in `return_styles.csv` are taken from the URL slugs, so they are not the exact product names.
- **Fibre line verdicts:** none can be given. Every named line (METARUN, ACTIBREEZE, LITE-SHOW, FUJITRAIL, MATCH, ROAD, HERITAGE and others) is undisclosed. Of the 12 disclosed styles, 9 are synthetic-led (polyester or nylon) and 3 are cotton-led poly/cotton tees.
- **Doors:** carried as given (2 own-door, 47 outlet; world NC, since the locator covers US+CA only). The locator was not re-read for doors.
- **Stockists:** the Locally widget (company_id 1682) lists about 9,900 US stockists, and I did not capture them all, as briefed. Within NY, MA and CA I queried 24 regional centres, which returned 1,414 locations. From those I kept **89 independent specialty run shops**, judged by name. Excluded: chains (Dick's, Foot Locker, Famous Footwear, DSW, Macy's, Snipes, Journeys, Fleet Feet franchises, Road Runner Sports, JackRabbit), golf shops and ASICS's own doors. Several kept shops are small multi-door regional operators (Marathon Sports 15, Super Runners 4, Heartbreak Hill 4, A Snail's Pace 5); `note` flags them. Running Warehouse is mostly an online retailer.
- **Sections 6–13:**
  - Tech: 4 proposed.
  - Craft: 2 proposed.
  - Origin: 1949, Kobe, Kihachiro Onitsuka (corp.asics.com history).
  - Quote: "Create Quality Lifestyle through Intelligent Sport Technology" (ASICS Vision, corp.asics.com/en/about_asics/spirit).
  - Signature product: GEL-KAYANO (33).
  - Grailed URL: confirmed live.

## Not reached (NC)
- Lookbook, Vinted, pronunciation.
- B Corp and GOTS: no B Lab or GOTS directory was opened, and one web search found nothing.
- `quote_date`: the Spirit page is undated.
- Worldwide doors.

## Needs a ruling / brief issues
- **Craft 2 vs 3:** ASICS publishes Tier 1/2 supplier references at corporate level but names no maker on any product page. I proposed 2. Onitsuka Tiger's owned Japanese factory belongs to a separate sub-brand and was not counted.
- **Tech 4:** the core technology (GEL, FF BLAST) is in footwear. On clothing, 47 of 233 style titles carry a named ASICS technology or performance line.
- The brief's 8-garment frame fits a sports house poorly: half the cells are `NONE`. Band-setting by dress shirt and sweater will fall through to trousers and outerwear (athletic pants up to $120, outerwear up to $290).
- Out of scope but noticed: ASICS's own "classification" field mislabels 4 garments as "Men's Trail Running Shoes".


## Balmain: full record, wave B batch 1 (read 2026-10-10)

**What was checked.** I read the US store at us.balmain.com/en-us. It runs on Shopify and charges in USD (rate 1.0). Two listing prices matched the feed on the rendered page. The full feed (`/en-us/products.json`) holds 674 products across 3 pages. I also read every men's collection feed. The men-rtw-view-all page says "104 items", which matches the feed. Those 104 listings collapse to 94 styles on the 12-character model+fabric code, which each product page prints as `Item:`. All 94 styles state a composition ("Main material:"), and all 104 listings state a country of making. I also read four house pages: About, Pierre Balmain, The Architects of Balmain, and the FW26 collection / SS27 runway pages.

**Section 4** was not re-read. I carried the counts over from held_door_counts.csv: 13 own doors in the US, 81 worldwide.

**Stockists.** The locator lists one US shop that Balmain does not own: Bloomingdale's 59th St, typed as a department store. It is the same concession counted in section 4. The site has no stockist page, so no shop qualifies for the register.

**Not reached / NC.** No Vinted brand id: vinted.com/brand/balmain served a generic catalogue and the brand API returned 403. B Corp and GOTS are also NC because the directory searches rendered no results. Status is `partial` for those cells only.

**Contradictions with the worklist or brief.**
- None on doors.
- The US e-store's men's range is small: 94 styles. It does not reflect the global collection.
- Every men's lookbook and show page on the US site is womenswear. Under Antonin Tron (since 2025) there was no men's show content.

**Mark as written.** BALMAIN, with PARIS set small beneath it in the header logotype. Key kept as `Balmain`.

**Fibre verdict.** One cloth story. 82% of styles are natural-led, 11% synthetic (all 8 swim styles plus a padded nylon jacket and a sequin velvet jacket) and 7% cellulosic. 7 styles contain elastane, 5 of them at 5% or more.
- The **Balmain Vintage** line is all-natural (19 styles: cotton and wool).
- The **Balmain Insect** line is mixed (7 styles; 6 natural, 1 cupro velvet bomber).
- No category with 10 or more styles is synthetic-led apart from swim, which is excluded from the verdict.

**Prices.** All eight garments are filled. Notable judgements:
- **Outerwear:** the high is a $9,100 embellished satin bomber. It is in the regular PF26 range, not tagged runway or capsule. Sebastian may prefer the $5,990 shearling bomber.
- **Sweater:** the entry crewneck is already majority silk, so the high is the dearest regular crewneck.
- **Dress shirt:** the low is $850, the cheapest long-sleeve shirt. A $790 short-sleeve shirt was set aside.

**Craft and tech.**
- Proposed craft is **2**: every men's product page states a country of making, but none names a maker or a mill, and the "Parisian ateliers" claim applies to couture and made-to-order.
- Proposed tech is **1**: no named fabric technology on any men's page.

**Out of scope but noticed.**
- The locator gives Dallas Highland Park the ZIP 72505; it is likely 75205 (already flagged in own_doors.csv).
- Organic-cotton and recycled-wool claims appear on 11 product pages with no certifier named.


## Belstaff: full record, read 2026-10-10

**What was checked (all in Chrome tab, belstaff.com US market `/en-us/`)**
- Own doors: Our Stores page (`/en-us/pages/customer-service-our-stores`), all 23 entries read from the DOM. US: 1 own door, 62 Gansevoort St, New York. Worldwide there are 8 own doors (7 UK plus NYC) and 15 outlets (11 UK, Roermond, Metzingen, Neumünster, Wertheim). The page lists no concessions or pop-ups. The worklist claim "NYC store" is confirmed.
- Stockists: the Stockists page has two tabs. 43 US shops are on the main "North America" list and 4 more US shops only on the Motorcycle tab, which gives name and city only. That makes 47 rows. Canadian shops were dropped. The locator gives no city, so cities come from the ZIP. Three state labels on the locator are wrong (Beecroft & Bull filed under CA but in VA; Joseph's filed under OR but in ME; Woodstock Sports filed under NY but in VT). I corrected them and noted it on each row. The Great Puton's ZIP is kept as listed (02589).
- Prices and links: the Shopify feed `/en-us/products.json` has 580 products. It returns USD even though `Shopify.currency.rate` is 1.367 (the shop's base currency is GBP). Feed prices matched the displayed page on two products. None of the chosen prices has a compare-at price.
- Fibre: 177 men's clothing styles (407 colourway listings, grouped by the 6-digit Item Code). Compositions are not in the feed. I read them from the DETAILS panel on each product page: 132 give percentages, 39 name fibres without percentages, and 6 give none. The house Material tag is unreliable: the Chassis jacket and gilet are tagged "Cotton" but are 85% polyamide / 15% elastane. Waxed Millerain cloth with no split stated is marked ND, because the same cloth reads 65% polyester on sister styles.

**Fibre verdicts:** 84% natural-led, 13% synthetic, 0% cellulosic, shape *one*. Outerwear (69 styles) is 45 natural to 21 synthetic. Knitwear, tees/polos and sweats are all natural-led. Lines: **Icons** (14 styles) is all-natural (13 of 14; the Icon Gilet is polyester). **Phoenix collection** (7) is all-natural. **Waxed Jackets** (17) is mixed: the motorcycle waxed jackets in Millerain technical cloth are 52–65% polyester, while the lifestyle 6oz waxed jackets are 100% cotton. Elastane: 18 of the 132 styles with percentages contain it, 5 at 5% or more (mostly denim and down shells).

**Needs Sebastian's ruling**
- Outerwear high is the Snowfield shearling coat at $2,950. Should shearling count as fur? If so, the high becomes the Trialmaster Panther leather at $2,095.
- Everything in the "limited-edition Phoenix collection, a capsule of Belstaff classics" is excluded from the highs. That includes Harrow, a superfine-wool crew at $550 that would otherwise have been the sweater high, and Lincoln, a cashmere-blend quarter zip.
- The mark: the logotype is an SVG that was not read. `mark_as_written: Belstaff` comes from the site title and body copy and is unconfirmed.

**Contradicts the record / out of scope but noticed**
- **Ownership changed:** INEOS sold 100% of Belstaff to Castore. The deal was announced and stated complete on 28 Aug 2025 (ineos.com), and INEOS took a stake in Castore. Any "INEOS-owned" note is out of date.
- The about page says Belstaff's own factories (Longton, Silverdale) closed in the 1990s. No owned making today, so craft is proposed at 3, at the low end, resting on named mills (British Millerain; Duca Visconti di Modrone on the Trentham trouser). Tech is proposed at 3: CE-certified moto garments with D3O armour, Cordura and Millerain, all licensed, on about 10% of styles.
- Some colourways carry odd non-round prices ($478.50, $540.02, $1,086.88) with no compare-at. These are probably unflagged markdowns. None was used.
- Not reached: Vinted (NC). The B Corp directory was not opened; nothing was found on the brand's responsibility page or by search.


## Bogner — full record, 10 Oct 2026

**Checked (Chrome, bogner.com en-us store, SFCC):** own-store locator (en-us, de-de and de-ch identical); men's clothing ItemList (`/en-us/c/men/clothing/453662/?sz=400`) cross-checked against seven sub-category ItemLists, with no stems missing; all 197 in-scope PDPs (JSON-LD offers plus Material & care block); men's shoes; glossary, history, brands, facts, shoe and news pages; Grailed; Vinted US; B Corp directory.

**Doors:** the locator lists 16 own stores: 1 in the US (New York, 755A Madison Ave) and 15 abroad (DE 10, AT 2, CH 3). It itemises no outlets, concessions or partner stores. The Numbers & Facts page claims 64 retail/concession/partner stores and 13 outlets worldwide, but lists none of them, so they are not counted. The worklist says "own US stores" (plural) and the locator shows one. A 2021 news page says the Madison Ave store opened as a FlagshipRTL winter pop-up; it is now listed as a BOGNER Store, and the operator is not stated.

**Sub-lines:** I applied the rules_prices sub-line rule. BOGNER Sport and FIRE+ICE are sold under the Bogner name in its own store, and neither is a canonical key, so both are counted in prices and fibre. `sublines_included` says so, and each style row names its line. Three price cells come from a sub-line: the tee low and outerwear low are FIRE+ICE, and the outerwear high is BOGNER Sport.

**Prices:** I read 7 of 8 garments in USD. Jeans are `NONE`: the men's range has none, and site search for "jeans" returns only women's styles. There is no formal dress shirt (the Kent-collar casual shirt is used) and no tailored trouser (the "Riley Business" drawstring trouser is used). Shoes are `range` because there is no loafer.

**Fibre (197 styles, 100% disclosed):** natural 38, synthetic 60, cellulosic 2. Ninety-two styles carry elastane, 67 of them at 5% or more. Shape is **split**: outerwear and bottoms lead synthetic, knitwear, shirts and tees lead natural.
- Line verdicts: **BOGNER Sport** 86% synthetic (84 styles, mixed, near all-synthetic). **FIRE+ICE** 78% synthetic (36, mixed). **BOGNER** mainline 75% natural (77, mixed).
- Wholly natural categories: **knitwear 20/20 and shirts 6/6**.
- Style key is the 3-segment article stem. Ten stems share a model number with a different cloth; counting by model gives 187. Ruling wanted on which to file.
- The composition column holds only the main fabric line (Shell 1, 1. Layer).

**Craft (proposed 2) / tech (proposed 3):** see the reasoning in return.csv.
- Craft: there is no owned making, and no garment makers are named. Garment country of origin appears on 0 of 197 PDPs; the Balli mill is named on 2. Shoes are made in Italy by an unnamed Marche family business.
- Tech: licensed Thermore, comfortemp, Ecodown and YKK AquaGuard are on 19 PDPs. Gore-Tex appears in the glossary only.

**Mark as written:** BOGNER (all caps). Also in the `note` of return.csv as `mark_as_written: BOGNER`.

**Not reached:** GOTS database (`NC`). The Vinted brand id is not exposed in the page (`NC`); the brand URL is given, but it is not filtered to men's.

**Noticed, out of scope:**
- Ownership changed: Katjes International took 60% on 1 Sep 2025.
- New CEO is Arne Freundt (ex-PUMA), from 1 June 2026.
- Clothing PDPs carry no country of origin.
- The `/men/clothing` ItemList includes accessories (hats, belts, helmets), which I excluded.


## Carhartt WIP: note (read 2026-10-10)

**What was checked.** I read only carhartt-wip.com pages. US store: us.carhartt-wip.com, which runs on Shopify Hydrogen (headless). `/products.json` returns 404, so the census came from the site's own Searchspring feed (site `1d460p`, collection `men-all`, 856 listings, 9 pages) plus one PDP per style.

**Section 4, own doors.**
- The US locator (`/en-us/stores`) lists 4 stores: 3 in the US and Toronto (market-ca). The 3 US stores are Los Angeles (136 S La Brea), Brooklyn (132 Bedford Ave) and New York (286 Lafayette St). It lists no outlets, concessions or pop-ups.
- The global locator (www.carhartt-wip.com/en-de/stores) gives 102 non-US stores: Germany 10, Europe 52, Toronto 1, Asia Pacific 39. Three Hong Kong rows are marked "(Corner)" and two are "Shinsegae Dept". These are probably department-store corners. I counted them in `world_non_us` and did not split them out. No row on either locator states an operator.
- **worklist_conflict:** the worklist claims "own US stores in NYC, LA, SF". There is no San Francisco store; the second NYC-area store is in Brooklyn.

**Prices.** USD, checked against two PDPs. The feed has no sale prices. Seven garments are basis `range`; shoes are `NONE`.
- The brand makes no dress shirt (casual button-downs only), no dress trouser (chinos used instead) and no sweater in an elevated fibre.
- Footwear appears only as collaborations, so there is no own-label shoe.

**Fibre.**
- 225 men's clothing styles, counted by I-number stem from 652 colourway listings. All 225 state a composition.
- Split: 90% natural, 10% synthetic, 0 cellulosic. 5 styles contain spandex; 2 have 5% or more.
- Shape is `one`. The only synthetic-led category is Sweaters (5 of 7), which is under the 10-style threshold.
- Line verdicts: **OG is all-natural** (26 styles, all cotton). **Icons is 17 of 18 natural** (the Simple Pant is 65/35 poly/cotton), so it reads as mixed by one style. T-shirts (74), denim (12) and shorts (8) are 100% natural-led. Synthetic styles sit in nylon jackets, fleeces, poly/cotton work pants and shirts (Craft, Master, Simple) and acrylic sweaters.
- I only produced `return_styles.csv` and the roll-up. The categories, fibres and lines files from rules_fibre.md were not asked for in AGENT_SPEC, so I did not write them.

**Stockists.** The US locator page itself lists 108 US physical stockists: 73 independents and 35 department-store doors (34 Nordstrom, 1 Bloomingdale's). It also lists 8 online stockists. The data was read from the page's own loader data, which includes the rows behind each "Show all". The locator has some typos and odd entries, which I recorded as listed:
- "San Fransisco" and "Calabasis" are misspelled.
- Reserve Supply in Houston carries an Austin zip.
- Sneaker Politics on Arnould Blvd is listed under New Orleans with a Lafayette zip.

**Ownership.**
- The imprint names Work in Progress Textilhandels GmbH (Weil am Rhein, HRB 412212, Local Court Freiburg) as "Carhartt WIP authorized distributor".
- The history page dates the licence: Work in Progress was set up in 1994 as Carhartt's exclusive distributor in Europe, and in 1996 got the licence to manufacture Carhartt products outside the USA. Edwin Faeh is named as founder.
- The US shop is operated by WIP ECOM LLC in New York (terms page).
- I did not reach the Handelsregister or Bundesanzeiger filings, so shareholders are NC.

**Craft, proposed 3.** The brand says it owns three facilities in Tunisia and that about a third of its garments are made there, at owned or long-term partner sites. But no facility is named, no PDP states a country of origin, and no mill is named. It would be a 4 if Sebastian accepts the brand's own statement and factory video as evidence. **Tech, proposed 1.**

**mark_as_written:** Carhartt WIP

**Not reached.** Vinted, Grailed, the B Corp directory and the GOTS database, all marked NC because reads were limited to carhartt-wip.com. I also did not reach the Handelsregister filings.

**Brief / tooling.**
- The agent proxy blocks curl to the site, so all data came through the Chrome tab.
- The Sid Pant PDP says "46% Cotton, 38% Lycra, 16% Polyester", which looks like a site error or Lycra T400. I read it as elastane and flagged it.
- One PDP (I037584) has a truncated description bullet. Its composition came from the PDP's main-material field instead.


## Chubbies: full record, 10 Oct 2026

**Checked:** the store locator (`/pages/stores`, read in Chrome), the full Shopify feed (the storefront is headless and `/products.json` returns 404 on www, so the feed was read from `chubbies.myshopify.com/products.json`, 1,797 records), about 40 product pages for composition and price checks, the About page, and Grailed.

**Own doors:** 9 own doors and 1 outlet, all in the US: FL 2, MN 1, NC 1, SC 1, TX 5. The locator labels Allen "OUTLET", and the address is Allen Premium Outlets. The locator lists no store outside the US, so `world_non_us` = 0. The worklist claim of "US stores" is confirmed. One oddity: the Houston entry gives its address as Memorial City Mall, but its Get Directions link opens a Google Maps place at 645 Heights Blvd, which is probably the old Heights store. I counted it once, at the listed address.

**Stockists:** none listed. The stores page says "or at a wholesaler" but names none, and the Prospective Wholesalers link redirects back to the stores page.

**Prices:** 7 of 8 garments priced. Shoes are `NONE` (no footwear in the feed).
- The dress shirt is a casual button-up (Friday and Sunday shirts).
- The dress pants are chinos and casual pants.
- Sweater is `single`: there is one crewneck knit.
- The polo high leaves out the NFL-licensed polos at $69.50.

**Fibre:** 121 men's styles, all 121 with a stated composition.
- Split: 43% natural, 53% synthetic, 4% cellulosic. 64 styles contain elastane.
- Shape is `split`: shorts are synthetic-led (18 of 31), while tees and polos, button-ups and lounge are natural-led.
- Style = the 3-digit SKU stem. Stems 444 (Sunday shirts) and 501 (Friday shirts) each cover fabrics that differ, so I split them by sub-style.
- One conflict: on the Sunday knit shirt, the product description says "100% cotton" and the page's Fabric section says 65% polyester / 35% cotton. The Fabric section is filed.
- The swim brief's composition is written on the site as "78% Elastane / 22% Spandex". It is filed as written and is almost certainly a site error.

**Swim:** 20 of 121 styles (16.5%), and 31.6% of colourway records (427 of 1,350). The 5.5" Classic Lined Swim Trunk alone has 194 prints. 19 of the 20 swim styles are synthetic-led. Men's styles excluding swim: 101.

**Line verdicts:**
- All-natural: Originals (8 styles, 98/2 cotton stretch) and Comfort (6, garment-dyed cotton).
- All-synthetic: Everywear (9), Ultimate Training (6), Classic Swim (6) and Classic Lined Swim (5).
- Mixed: Friday Shirt (5).

**Proposed:** tech 2 (house-named performance fabrics, nothing licensed) and craft 1 (no named maker or mill, no country of origin on the product pages, founding dated but not placed).

**mark_as_written:** chubbies (the header wordmark is lowercase).

**Not reached / NC:** founded_place (the About page does not say where), lookbook, Vinted brand id, B Corp and GOTS. Ownership is Solo Brands per the About page only; the filings were not read.

**Out of scope but noticed:**
- The "FOR HER" link goes to cheekies.com, a separate brand.
- "AFTERPARTY" is a separate subdomain (afterparty.chubbiesshorts.com) and was not read.
- NFL by Chubbies is a large licensed range (539 feed records tagged NFL). It is counted in the styles.
- The feed carries a hidden `COO:` tag on only 3 styles.


## Church's — full record, wave B batch 1 (read 10 Oct 2026)

**Checked:** US store church-footwear.com/us/en/ (USD confirmed on two PDPs against JSON-LD). Also the full US sitemap.html category tree, the men's loafer grid (all 66 loaded), the men's accessories grid, 12 sampled men's PDPs across six footwear categories for made-in, the history and craft pages, and the AW26 campaign. Off-site: the Prada Group Annual Report 2025 (ownership, structure), Prada's Northampton page and Grailed.

**Section 4:** Carried from held_door_counts.csv, as instructed. US 0 (positive zero), world 23 non-US, locator not re-read. worklist_conflict: worklist says NYC store. The brand history mentions a 1920s New York store, which is probably where the claim came from. Prada AR 2025 p.52 reports 27 owned Church's stores at year-end 2025 against 23 on the locator. Not substituted, because filings are not a door source. Flagged for Sebastian.

**Clothing:** None. Church's sells no clothing. The men's tree is footwear plus accessories (shoe care, socks, belts, gloves and scarves, hats, umbrellas, bags). Seven garment slots are NONE. The fibre census is 0 styles in scope, so return_styles.csv is header only. Fibre line verdicts: none (no clothing lines exist).

**Shoes (pair):** $890 Rock Ferry Roadrunner loafer to $1,850 Viscount (Royal Collection). The high is a named judgement. The main-line top is Kingsley at $1,370. Crocodile (exotic) and fur-lined Peebles are excluded.

**Stockists:** The brand lists none for the US (no stockist page; locator has no US). One `none` row.

**Craft 4 / Tech 1.** Church's owns its Northampton factory, and its process is documented. Part of the range is stated Made in Italy with no maker named.

**Not reached:** Vinted brand id (API 403), so NC.

**mark_as_written:** Church's (footer CHURCH'S).

**Out of scope, noticed:** One sandal PDP (EX0034) carries priceCurrency EUR in its US JSON-LD.
