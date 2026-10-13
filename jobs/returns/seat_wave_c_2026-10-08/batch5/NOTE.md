# Wave C full records: batch 5 of 9, 13 October 2026

Brands (worklist rows 41–50): Lady White Co., Lands' End, Lardini, Ledbury, Mango, Meermin, Mollusk, Muji, Nautica, Needles.

Files:
- `return.csv`: 10 rows, 132 columns, no empty cells.
- `return_styles.csv`: 1,142 style rows (9 houses; Meermin sells no clothing, so it is NO_STYLES).
- `own_doors.csv`: 209 rows (Nautica 72, Mango 62, Lardini 27, Lands' End 23, Muji 13, and the rest).
- `stockists.csv`: 130 rows (Mollusk 96, Lady White Co. 25, and the rest).

Reconcile is clean on all four files (10 names: 10 exact, 0 to rewrite, 0 unmatched). The style table passes `schema_styles.json` (enums and integer ranges). Every site was read in Chrome on 13 October.

## A change from batches 1–4: whole dollars
`rules_prices.md` says "Whole dollars, rounded half-up, exact figure in `note`". Batches 1–4 filed cents (for example Gap 19.95). This batch follows the rules file: price cells are whole units, and every rounded figure is given exactly in `note` (for example "tee: … exact low 14.95, high 59.95"). JPY prices are already whole. If you want cents back for consistency with batches 1–4, the change is one line in `assemble_b5.py`.

## What was read
- **Shopify houses** (Lady White Co., Lardini, Ledbury, Meermin, Muji, Needles): the full `/products.json` feed, available products only. Composition came from the product body or the product page.
  - Lardini on the `/en-us` market path in USD. The feed price and the displayed price matched on every product read.
  - Needles on Nepenthes' Japanese online store (`onlinestore.nepenthes.co.jp`), in JPY, tax-inclusive. Not converted.
- **Mollusk**: the store has no `/products.json` (headless). It was read through its public Storefront API. Own label is the "Mollusk-Product" tag with MS SKUs.
- **Nautica** (large house): the men's grid with paging. Tile data gives "Comp. Value" and the selling price. Composition comes from the product page "Product Info" for the sample. Stores: a full crawl of stores.nautica.com (state, then city, then store).
- **Lands' End** (large house): the site's own search API for the men's clothing listing (795 products). The product-lookup API gives the fabric bullets for the sample. The men's shoes listing (40 styles). Stores: the locator's XML feed (`/pp/StoreLocator`), read at national radius.
- **Mango** (large house): the 21 men's categories and their subcategories, the product API and the price API (`originalShop` = regular price). Product pages are blocked by a firewall (403), so **no composition was read for Mango**. Stores: 62 US store pages.
- **Price spot-check.** Every Shopify pick was re-read live through its `.js` record: 68 picks (Lady White Co. 12, Lardini 14, Ledbury 9, Muji 16, Needles 15, Meermin 2). All matched. Two Ledbury records carry odd compare-ats:
  - The Collins Knit Polo is priced 145 with a compare-at of 135. The higher figure (145) is filed.
  - The Duval Pinpoint Oxford is on markdown, at 105 against a compare-at of 135. 135 is filed.
- Lands' End, Nautica and Mango picks are from the listing or API data, read once; they were not re-read.

## Large houses: stratified samples
Lands' End, Muji, Nautica and Mango carry category-stratified samples in `return_styles.csv`. **None of the samples is proportional to category size.** Fibre shares, the spandex count, shape and categories all come from the sample. `styles_total` is the full count, except for Mango.
- **Lands' End:** 176 sample rows; 167 of them state a composition.
  - Full own men's clothing is 679 styles and 2,772 colours. That is 795 listing products and 693 style numbers, less 13 socks and one collaboration tee (LE X WAWA).
  - Swim is 13 styles.
  - `styles_with_composition` is NC at catalogue level.
- **Muji:** 116 sample rows (every third style per category).
  - Full catalogue: 341 men's styles and 1,297 colour options. That counts Men's Tops, Bottoms, Outerwear, Innerwear and Loungewear, plus MUJI Labo pieces tagged men's or unisex.
  - All 341 state a composition.
- **Nautica:** 125 sample rows (every fourth master).
  - Full catalogue: 499 clothing masters out of 637 men's masters, including 118 Big & Tall.
  - `colourway_ratio` is NC.
- **Mango: a floor, not a count.**
  - About 978 clothing product ids were seen across the category pages (1,029 including 51 shoes), and 1,569 colour items.
  - Compositions are NC: the product pages were never read. The 144 style rows carry NC in every fibre field, not ND, because ND would mean the page was read.

## Exclusions you should know about
- **Collaborations** are out of prices and the style layer:
  - Lady White Co.: PMLW jeans and denim blouson; MAN-TLE pieces; Moonstar and ROF shoes. That leaves Lady White's jeans and shoes as NONE.
  - Lands' End: LE X WAWA.
  - Needles: Sun Surf, Amarillo, Sorel, FILA, Brooks Brothers, Troentorp, PPACO, Wakouwa, Reebok, Tie A Knot, Ray Adakai.
- **Bows & Arrows exclusives** at Lady White Co. (Padded Crewneck, Lynn Poplin S/S) are tagged COLLABORATION by the house. They are treated as collaborations; see the ruling list.
- **Third-party product** is excluded:
  - Mollusk: every non-Mollusk brand, plus surfboards, wetsuits and art.
  - Ledbury: Beltology and Trafalgar.
- **Needles skirts and tunics** (21 listings) are out of the men's style count. The range is sold without gender.

## Prices: things to know
- **Nautica:** Comp. Value is filed as the regular price (10 Oct ruling). Every men's tile sells below it, and the selling prices are in the garment notes.
- **Mango** picks are "lowest and highest found in the sample", not proven extremes.
- **Pairs:**
  - Lands' End sweater: Fine Gauge Cotton Crew 69.95 against the Cashmere Crewneck 199.95 (100% cashmere).
  - Lardini dress shirt: 540 against 990 (silk).
  - Loafer pairs: Meermin (calf 220 against shell cordovan 375), Needles (¥44,000 against ¥75,900), Lands' End (149.95 against 149.95) and Mango (139.99 against 199.99).
- **Lardini sweater:** the high (1295) is a turtleneck titled cashmere whose composition reads 100% virgin wool. Crewnecks are 715–820 at 90/10 wool/cashmere, which is not majority cashmere. It is filed as `range`.
- **Needles outerwear high** is the Shearling Coat (¥294,800). It is filed as a `range` high (the dearest regular item), not as an elevated pair, because shearling is never elevated. See the ruling list.
- **Ledbury:**
  - The tee is a single undershirt (55).
  - There are no jeans, outerwear or shoes (NONE).
- **Mollusk:** no polo, jeans or own shoes (NONE).
- **Muji:** there is no loafer. Shoes are `range` (sneakers 39.90 to leather Chelsea boots 149.90).

## Fibre: the headline per house
- **Lady White Co.:** 99% natural.
- **Lardini:** 94% natural.
- **Mollusk:** 92% natural.
- **Ledbury:** 91% natural.
- **Nautica (sample):** 78% natural.
- **Muji (sample):** 72% natural.
- **Lands' End (sample):** split, 72% natural / 23% synthetic. Outerwear and performance tops are synthetic-led.
- **Needles:** split, 52% natural / 42% synthetic. The track pants, jersey tees and poly suiting are synthetic-led.
- **Mango:** NC.
- **Meermin:** no clothing.
- **Partial compositions:** 20 style rows carry a parse flag. Most are Ledbury pages that state part of the composition. There is also Needles' rabbit fur and one Needles "ウール9% ナイロン 3%" line.

## Doors
- **Lands' End: 14 US own doors** (all of its 23 locator points are in the US).
  - The 14 are typed "Lands' End Store", have posted hours and list men's.
  - 6 are typed "Outlet Store" (the "Inlet" stores at Richfield, Niles, Woodbury, Rochester, Fox Point, Brookfield). They are rowed as outlets.
  - Bergen Town Center is typed "Store" but sits in The Outlets at Bergen Town Center, so it is an outlet.
  - Honolulu is a school-uniform store and is not counted (for ruling).
  - Rockville is permanently closed.
- **Mango: 62 US doors** read; the list page names 66, so 4 were not reached.
  - 17 show a MEN section.
  - 45 do not and are counted as women's-only, flagged.
  - Store pages give no state, so city and state come from the ZIP. Several site labels are wrong:
    - Cielo Vista Mall is labelled Austin; it is El Paso TX.
    - Pioneer Place is labelled Seattle; it is Portland OR.
    - Legacy Place is labelled Dallas; it is Dedham MA.
    - Natick Mall is labelled Boston; it is Natick MA.
    - Walt Whitman Shops is labelled Long Island; it is Huntington Station NY.
  - World is NC.
- **Nautica: 1 US.**
  - 72 store pages, including 3 in Puerto Rico.
  - 71 sit in outlet centres or outlet malls and are not counted.
  - Mariposa Mall (Nogales AZ) is in a regular mall and is counted, flagged.
- **Muji: 13 US.** These are 10 New York, 2 Massachusetts and 1 Oregon. MUJI Market (New York) is a food store; it is counted and flagged.
- **Lardini: 0 US / 5 world.**
  - The 5 are Milan, Tokyo Aoyama, Tokyo Marunouchi, Moscow and Krasnogorsk.
  - 2 outlets and 20 department-store boutiques (concessions) are not counted.
- **Meermin: 2 US / 4 world.** The US doors are New York and Georgetown; the others are Paris and Madrid.
- **Mollusk: 3.** San Francisco, Santa Barbara and Venice. These are multi-brand surf shops under the brand's name.
- **Lady White Co.: 2.** Both are in Los Angeles.
- **Ledbury: 0, for ruling.** The Richmond store page now redirects to the About page.
- **Needles: 0.** Nepenthes New York and Nepenthes Los Angeles are rowed as other-brand doors and stockists (for ruling).
- **Territories:** Puerto Rico only (Nautica, outlets).

## Stockists rowed
- **Mollusk:** 96 US, with name, city and state; no street addresses. Shops that are not clothing shops by name are marked "other".
- **Lady White Co.:** 25 US, with name and state only. Two are marked "(SS - 27)", meaning future stockists.
- **Needles:** the two Nepenthes US shops.

Not rowed:
- Ledbury and Meermin: direct to consumer, no stockists (NONE).
- Lardini, Muji, Nautica, Lands' End and Mango: the locators list own stores only, and wholesale was not looked for (NC).

## Sections 6–13
- **Craft proposals:**
  - Lardini 5: its own Filottrano facility (20,000 m², 400+ staff), family-run since 1978. A reader may hold it at 4.
  - Lady White Co. 3, Ledbury 3, Meermin 3.
  - Mollusk 2, Needles 2.
  - Lands' End 1, Muji 1, Nautica 1.
  - Mango NC (product pages blocked).
- **Founding:**
  - Lardini 1978, Filottrano.
  - Nautica 1983, New York City, David Chu.
  - Lady White Co. 2015 (place not stated).
  - Founders without a year: Ledbury (Paul Trible and Paul Watson).
  - Not looked for: Lands' End, Mango, Muji.
- **Quotes:** Lardini, Ledbury, Meermin, Mollusk and Nautica. The other five are NC.
- **Vinted:**
  - No brand entry for Lady White Co., Ledbury or Mollusk.
  - Mango has a second ID (MNG).
  - Nautica has a second ID ("Nautica Compétition").
- **Tech fabrics** (`tech_named_fabrics` filled; `proposed_tech` stays NC):
  - Nautica: Navtech, Nautex (own); TENCEL, REPREVE, T-400, LYCRA.
  - Lands' End: SUPIMA; plus house names ThermaCheck, FlexPique, Anyweather, RainDefense, Thermaskin, Wanderweight, Rapid Dry.
  - Ledbury: SUPIMA, TENCEL, Reda, Albini 4-Flex.
  - Lardini: TENCEL. Lady White Co.: SUPIMA.
  - Mango: titles only, Giza cotton and Candiani (denim mill).
  - Meermin: tanneries named (C.F. Stead, Zonta, Annonay, Du Puy).
  - Muji and Needles: NONE.
- **B Corp, GOTS and pronunciation:** NC for all ten.

## What contradicted the record
- **Ledbury's door.** The Richmond shop ruled an own door on 10 October no longer has a page; the URL redirects to About.
- **Mango's own store pages mislabel cities.** At least five are wrong (listed above).
- **Lands' End "Inlet" stores.** Despite the name, the locator types them as Outlet Stores.

## For ruling
1. **Ledbury's door.** `/pages/richmond-store` redirects to the About page, and no address or hours are published anywhere on the site. Filed 0. Keep the 10 Oct own-door ruling (1), or 0?
2. **Needles and Nepenthes.** Every door trades as NEPENTHES, Engineered Garments or South2 West8; none carries the Needles name. Nepenthes is the parent and Needles its in-house brand. Nepenthes New York (307 W 38th St) and Los Angeles (715 S Los Angeles St) are rowed as other-brand doors. Do they count as Needles doors?
3. **Needles outerwear high.** The dearest regular item is a sheepskin shearling coat (¥294,800). It is filed as a `range` high. Should shearling be excluded from the high altogether, given "never fur"? If so, the next is the cowhide Lettered Jacket (¥253,000), and after it the rabbit fur coat (¥176,000), which would also be excluded.
4. **Lands' End: Willis and Geiger.** A leather bomber (699.95) is sold on landsend.com under the Willis and Geiger name. It is counted in the style total but not taken as the outerwear high. Is it a sub-line of Lands' End, or a separate label?
5. **Lands' End floor question.** 14 full-price stores (plus 7 outlets). How much of each floor is men's is not stated, though men's is listed in every store's departments.
6. **Lands' End Honolulu School Store.** It sells school uniforms only. Not counted. Count it?
7. **Mango women's-only doors.** 45 of 62 US stores show no MEN section and are counted, flagged, per the 11 Oct rule. Confirm, and say whether the floor question changes this for a house where most doors are women's-only.
8. **Mango composition.** Product pages are blocked (403 firewall), so every fibre field is NC and craft is NC. Accept as NC, or hold Mango for a second pass from another route?
9. **Nautica Mariposa Mall** (Nogales AZ). It is the only store not in an outlet centre. Counted as 1 own door. Also the floor and channel question: is a house with 71 outlets and 1 full-price door an outlet business?
10. **Muji.** MUJI Market (75 9th Ave, New York) is a food market and is counted, flagged. Also the floor question: clothing is one department in a general-goods store.
11. **Lady White Co. and Bows & Arrows.** The Padded Crewneck and Lynn Poplin S/S are "Bows & Arrows exclusive" and tagged COLLABORATION by the house. They are excluded as collaborations. Are store exclusives collaborations?
12. **Lardini's Russian stores** (Moscow, Krasnogorsk). They are counted as own doors because they carry the Lardini name, but the operator is not stated.
13. **Lardini craft 5.** The house claims its own factory and staff. Is it 5, or 4 because process is described only generally?
14. **Mollusk makers in the vendor field.** On own-label goods, the vendor field names the garment maker (Beview Garments Limited, Dongguan Chaoxiang Fashion Co., Corceli SAC in Peru, Brinell). `named_makers` says no, because the names are in data, not on the page. Do vendor-field makers count?
15. **Whole dollars.** This batch rounds to whole units per `rules_prices.md`, while batches 1–4 kept cents. Which should stand?
