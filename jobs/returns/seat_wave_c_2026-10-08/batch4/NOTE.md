# Wave C full records: batch 4 of 9, 12 October 2026

Brands (worklist rows 31–40): Gap, Goldwin, Golf Wang, Hender Scheme, Hickey Freeman, Holderness & Bourne, Imogene + Willie, Jos. A. Bank, Katin, Kiel James Patrick.

Files:
- `return.csv`: 10 rows, 132 columns, no empty cells.
- `return_styles.csv`: 1,115 style rows (9 houses; Hickey Freeman has no style table).
- `own_doors.csv`: 446 rows (Gap 393, Goldwin 23, G-Star 13, and the rest).
- `stockists.csv`: 64 rows.

Reconcile is clean on all four files (11 names including G-Star: 11 exact, 0 to rewrite, 0 unmatched). Every site was read in Chrome on 12 October; the workspace still gets a 403 on every brand host.

## The two re-reads
- **G-Star own doors.** Read from the store finder's own data call (`/en_us/find-a-store/getstores?country_iso=US&output_details=1`). It lists 101 US points of sale: 88 multi-brand and 13 mono-brand (10 "Mono brand", 3 "Mono brand / Footwear"). All 13 mono-brand doors are now rowed in this batch's `own_doors.csv` (brand G-Star) with street, city, state, ZIP, phone and store-page URL.
  - The count is unchanged: 9 full-price doors, plus 3 outlets (Sawgrass Mills, Jersey Gardens, Woodbury Common). Belmont Park Village (2601 Hempstead Turnpike, Elmont NY) has no format word in its name, so it is not counted.
  - Soho's record carried a temporary closure, 27 Jul–17 Aug 2026. That is past.
  - The 8 Oct facts-first split by "type" does not match the finder's category field. These rows use the category field.
- **Blundstone craft: proposed 2.** The our-story page dates the house (founded 1870, Hobart factory) and names the owners (the Cuthbertson family since the 1930s). It also says production "expands internationally" and products are now "manufactured in six sites around the world, including Hobart". No site is named except Hobart, and none of the 213 US products states a country.

## What was read
- **Shopify houses** (Goldwin, Golf Wang, Holderness & Bourne, Imogene + Willie, Katin, Kiel James Patrick): the full `/products.json` feed, available products only. Composition came from the product body or PDP.
- **Gap** (large house): the site's own product-search API, men's department, 769 rows. PDP "Fabric & care" bullets were read for all 290 men's styles. Stores: all 393 store pages, with the format taken from each page's `store_type`.
- **Jos. A. Bank** (large house): the site's own search service across eight men's categories, 7,732 records. Composition comes from the Product Details attribute.
- **Hender Scheme**: the official online shop (wear and shoes categories), plus the henderscheme.com archive, shops and stockists.
- **Hickey Freeman**: hickeyfreeman.com is one landing page with no shop.
- **Price spot-check:** every pick was re-read live.
  - **Shopify houses:** 71 picks via the product `.js` record (Goldwin 11, Golf Wang 10, Imogene + Willie 13, Katin 14, Kiel James Patrick 11, Holderness & Bourne 12).
  - **Jos. A. Bank:** 14 picks via the productview record. Every Jos. A. Bank `/p/` URL was also opened.
  - **Corrections:**
    - Goldwin's trouser high: the PERTEX SHIELD PRO Mountaineering Pants (490) sold out after capture. The high is now the Hyperdense Taffeta U/S Destra Pants (430).
    - Jos. A. Bank's 1905 dress shirt: its URL needs the part-number suffix (`…-5BHB`), because the bare title slug returns 404.
    - Listing URLs that 404'd (Katin, Kiel James Patrick, Holderness & Bourne, Jos. A. Bank) were replaced with collection paths that resolve.

## Large houses: stratified samples
**Gap and Jos. A. Bank** carry category-stratified samples in `return_styles.csv`. Both say so in `status`, `style_method` and `note`.
- **Gap:** 152 rows. `styles_total` 244, `styles_with_composition` 244 and `colourway_ratio` 816/244 are full own-catalogue counts. Swim is NC at catalogue level.
- **Jos. A. Bank:** 123 rows (clearance copies dropped). `styles_total` 653 and `styles_with_composition` 555 are full own-clothing counts. `colourway_ratio` is NC.
- **Bias warning:** fibre shares, spandex count, shape and categories come from the sample. The sample is not proportional to category size.

## Exclusions you should know about
- **Collaborations** are out of prices and the style layer:
  - Gap: 46 styles (A.P.C., Malbon, BEIS, Disney, Lichtenstein/Whitney, FIFA, NBA, NFL).
  - Goldwin: Cactus Store, plus the Goldwin 0 PERTEX Gleam Anorak (performance x nur).
  - Golf Wang: Clarks Wallabee.
  - Holderness & Bourne: H&B x Yale Golf Course.
  - Imogene + Willie: Schott NYC, Wrangler, American Woolen.
  - Kiel James Patrick: Jeep, Goslings, F.L. Woods.
  - Hender Scheme: Artek.
- **Third-party product** is excluded:
  - Imogene + Willie: the "3rd party-*" vendors.
  - Jos. A. Bank: Johnston & Murphy, Cole Haan, Haggar, Joseph Abboud and others.
  - Gap: Dropship listings.
  - Kiel James Patrick: vintage resale.
- **Golf Wang album and tour merchandise** (19 pieces: CHROMAKOPIA, TOUR25, Don't Tap The Glass box set) is excluded. This is for ruling, see below.
- **Goldwin:** C3fit (separate compression brand) and FW26 "Coming Soon" pieces are excluded.

## Prices: things to know
- **Markdown houses:** Goldwin, Katin and Kiel James Patrick, where compare-at is filed as regular. Gap and Jos. A. Bank are permanently promoted, so regular or list price is filed.
- **Hender Scheme** is in JPY as displayed, tax-inclusive. Its only garment is the leather collar jacket at ¥204,050. Loafers run from ¥83,160 (loafer #2146) to ¥98,098 (argyle loafer).
- **Hickey Freeman:** the tailoring slots (dress shirt, dress pants, outerwear) are `np`, as instructed. The other slots are NC.
- **Pairs:** the sweater slots of Holderness & Bourne (Buckley, 100% Scottish cashmere, 645) and Jos. A. Bank (Reserve cashmere crew, 199.5).
- **Shoes:**
  - Jos. A. Bank: one own loafer, 119.5.
  - Golf Wang: NONE (all collaboration).
  - Gap, Goldwin, H&B, I+W, Katin, KJP: NONE (no own footwear).
- **Imogene + Willie jeans** top out at 325. The numbered "love fades" limited editions (475–525) are treated as capsules, and the denim carpenter pants (350–395) as work trousers.

## Fibre: the headline per house
- **Imogene + Willie:** 95% natural.
- **Kiel James Patrick:** 93% natural.
- **Gap (sample):** 91% natural.
- **Golf Wang:** 90% natural.
- **Katin:** 78% natural; jackets and sweaters are synthetic-led.
- **Jos. A. Bank (sample):** 69% natural.
- **Holderness & Bourne:** split, 25% natural / 75% synthetic. Only the sweaters and button-downs are natural-led.
- **Goldwin:** 84% synthetic, with every category synthetic-led.
- **Partial compositions:** 14 style rows carry a "main line sums to" flag where the page states only part of the composition (e.g. "50% Polyester").

## Doors
- **Gap: 150 US own doors.**
  - 149 full-price, plus Wichita, whose record lists both Gap banners and Gap Factory Store. Wichita is counted and flagged.
  - One of the 150 is in Puerto Rico (Mall of San Juan).
  - 241 Gap Factory Stores are rowed as outlets and not counted.
  - 2 pages with every day "closed" and no store type are excluded: Fresno 3685 North Gap Drive, and Chester NJ 270 US-206.
  - World is NC.
  - Four street typos on the store pages are written corrected.
  - `state` = NC on four Gap rows means North Carolina, not the token.
- **Goldwin: 1 US / 16 world.** The re-read of the shop list found 8 China shops, where facts-first had only Beijing. The world count rises from 9 to 16.
  - 4 Korean department-store shops are concessions.
  - 3 GRAVITY shops are rowed as other-brand doors, not counted.
- **Golf Wang:** 2 US (LA, NYC) / 4 world (plus London, Sydney). The Dec 2023 holiday pop-ups are closed.
- **Hender Scheme:** 0 US / 6 world. These are the "sukima" own shops in Tokyo (3), Osaka, Fukuoka and Nagoya, flagged.
- **Imogene + Willie:** 2 (Nashville, Austin).
- **Kiel James Patrick:** 1 (Newport RI). The Pawtucket factory is not open to the public.
- **Jos. A. Bank:** 185 registered (not re-read). There is one placeholder row.
- **Katin:** NC, for ruling.
- **Holderness & Bourne:** 0.
- **Hickey Freeman:** 0, flagged.
- **Territories:** none came up in this batch apart from Puerto Rico.

## Stockists rowed
- **Imogene + Willie:** 42 US, addressed.
- **Hender Scheme:** 14 North American, names only (2 Canadian).
- **Hickey Freeman:** Dillard's, the only retailer the site names.

Not rowed:
- Holderness & Bourne: golf clubs, no list.
- Katin and Kiel James Patrick: no list.
- Gap, Goldwin, Golf Wang and Jos. A. Bank: not looked for.

## Sections 6–13
- **Craft proposals:**
  - Imogene + Willie 4: own LA sewing room, team of 12, USA small-batch since 2009, own repair service.
  - Goldwin 2, Hender Scheme 2, Holderness & Bourne 2, Kiel James Patrick 2.
  - Gap 1, Golf Wang 1, Jos. A. Bank 1, Katin 1.
  - Hickey Freeman NC.
- **Founding:**
  - Goldwin 1950, Oyabe City, Toyama.
  - Katin 1954, Surfside CA, Nancy and Walter Katin.
  - Imogene + Willie 2009, Nashville.
  - Founders without a year: Holderness & Bourne (Alex Holderness & John Bourne) and Kiel James Patrick (Kiel and Sarah Patrick).
- **Ownership:** Goldwin Inc. (footer). Hickey Freeman: ABG-HMX, LLC (footer). Not stated for the others.
- **Quotes:** 6 of 10. Gap, Golf Wang, Hickey Freeman and Jos. A. Bank are NC.
- **Vinted:** no brand entry for Holderness & Bourne, Imogene + Willie or Kiel James Patrick. Golf Wang has a second ID for "Golf Wang x Tyler The Creator".
- **Grailed:** no page for Holderness & Bourne.
- **Tech fabrics** (tech_named_fabrics filled; proposed_tech stays NC):
  - Goldwin: GORE-TEX, WINDSTOPPER, PERTEX, POLARTEC, CORDURA, SOLOTEX, THERMOFRAME, CLEANDOWN, Polygiene, KODENSHI, Brewed Protein.
  - Holderness & Bourne: AIRATION®, Swing Knit™ (own).
  - Gap: GapFlex, CashSoft, TENCEL, LYCRA.
  - Jos. A. Bank: COOLMOTION, 37.5, TENCEL.
  - Imogene + Willie: SUPIMA. Katin: TENCEL.
  - Golf Wang, Hender Scheme, Kiel James Patrick: NONE.
- **B Corp, GOTS and pronunciation:** NC for all ten.

## What contradicted the record
- **Goldwin's world doors are 16, not 9.** There are 8 China shops, not 1. The worklist's "SF store" does not exist; the only US shop is in New York.
- **Gap formats:** facts-first had 242 Factory and 2 unclassified. The store_type pass gives 241 Factory, 1 mixed (Wichita) and 2 closed pages.

## For ruling
1. **Golf Wang album and tour merchandise.** These are CHROMAKOPIA, TOUR25 and Don't Tap The Glass pieces sold on golfwang.com under GOLF WANG. They are excluded as music merchandise rather than the clothing line. Are they own label?
2. **Katin's door.** The story page says Sato Hughes and her son Glenn "have since continued to run the original surf shop" in Surfside, but the site gives no address or hours. Own doors are left NC. Count 1, or 0?
3. **Holderness & Bourne collegiate versions.** 211 university-licensed listings are folded into their base models as colourways and not priced. Are they licensed product to exclude?
4. **Goldwin GRAVITY shops.** Three multi-brand ski shops (Kanda, Niseko, Yuzawa) sit on Goldwin's own shop list but trade as GRAVITY. They are not counted.
5. **Hender Scheme "sukima".** The house calls them its directly operated stores, but the name on the door is "sukima". They are counted (6 world).
6. **Hickey Freeman.** The site sells nothing and points to Dillard's. The record is seated as np/NC with own doors 0. Should Dillard's be read for prices, or should the house stay np?
7. **Goldwin Nanjing** sits in Deji Plaza, which also trades as a department store. It is counted as a shop in a shopping centre.

## Method notes
- Outputs that carried `?`, `&` or `=` were blocked by the extension. Everything was rendered into the page and read as text.
- Gap's store type is in each page's markerData JSON. A text match on "Gap Factory" was useless, because the phrase is in the site nav on every page.
- Imogene + Willie's per-product "made in usa" text is also in the site footer, so no per-style made-in share is claimed.
- fibre.py additions: `elasterell` and `elastrell` (as elastomultiester), `other` (as other fibre), and the typo `polyster`.
