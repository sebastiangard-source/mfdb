# Wave C full records: batch 3 of 9, 11 October 2026

Brands: Eastside Golf, Edward Green, Evan Kinori, Express, Flint and Tinder, Freenote Cloth, Frye, Fusalp, G-Star, Gallery Dept.

Files:
- `return.csv`: 10 rows, 132 columns, no empty cells.
- `return_styles.csv`: 1,208 style rows (9 houses; Edward Green is shoe-only).
- `own_doors.csv`: 302 rows (Express 226, Fusalp 53, G-Star 13, and the rest).
- `stockists.csv`: 141 rows.

Reconcile is clean on all four files (10 exact, 0 to rewrite, 0 unmatched). Every site was read in Chrome on 11 October. The workspace still gets a 403 on every brand host.

## What was read
- **Shopify houses** (Eastside Golf, Evan Kinori, Freenote Cloth, Frye, Fusalp, Gallery Dept.): the full `/products.json` feed, available products only, with composition from `body_html` or product pages.
- **Flint and Tinder** has no site of its own. It is Huckberry's house label, read through Huckberry's tiles API for the brand page (309 in-stock colour listings, 126 styles). The API gives compare-at price, country of origin and description.
- **Edward Green** (Magento): all 158 shoe listings, the loafer pages, about, both store pages and the stockist page. Prices are shown "US Duty Paid", so the currency is `USD_landed`.
- **Express** (custom React + GraphQL): read through the site's own Apollo client. 22 men's categories give 426 products; composition (`fabricCare`) was read for all 426. Stores: all 226 store pages in the stores.express.com directory.
- **G-Star** (Next.js + Algolia): the site's own search index with its public key. 5,410 men's colour records / 2,158 styles; 1,835 clothing styles.
- **Price spot-check:** 50 picked products were re-read from the product `.js` record (Eastside Golf 14, Freenote 11, Gallery Dept. 10, Evan Kinori 10, Frye 5). Five corrections came out of it:
  - **Freenote Cloth's SKU stem joins colours that are priced differently.** Four picks were moved to the handle that actually carries the price: jeans low (Belford Straight 14.50oz Kaihara, 285), shirt low and high (Dayton Chambray 220, Sinclair Ivory 360), trousers low (Workers Chino Khaki 280).
  - **Frye's Huck Racer** is 645 in cognac/black; the moka/tobacco colour first picked is 599.
  - **Eastside Golf's Breaker Polo** (132) is a woven wind shirt with a bungee hem, not a polo. The polo high is now the Multi-Color Scenic Pique Polo (98).
  - **Eastside Golf's Links Sweater** low (115) is the navy colour's compare-at. Prime green is 128.

## Large houses: stratified samples
**Express and G-Star** carry a category-stratified sample in `return_styles.csv`. Both say so in `status`, `style_method` and `note`.
- **Express:** 139 rows (every k-th product per category, up to 12 per category). `styles_total` 425, `styles_with_composition` 344 and `colourway_ratio` 1971/426 are full-catalogue counts. The 1,971 colour tiles were counted before one women's blazer-vest was dropped, hence 426 in the ratio.
- **G-Star:** 176 rows (up to 5 per product type). `styles_total` 1,835, `styles_with_composition` 1,798 and `colourway_ratio` 4744/1835 are full-catalogue counts. Swim is NC at catalogue level.
- **Bias warning:** the fibre shares, spandex count, shape and categories come from the sample. The sample is capped per category, so it is **not proportional to category size**. Small categories weigh as much as large ones.

## Exclusions you should know about
- **Collaborations** are out of prices and the style layer:
  - Eastside Golf: Nike x Eastside Golf shoes.
  - Evan Kinori: MAN-TLE down jacket.
  - Flint and Tinder: Cash Diamond Snap Western Shirt, Rancourt loafer, Rios of Mercedes boot.
  - Freenote: Golden Age Supply, Codina Leather, Bell & Oak, Bowman Hat, Tatton Baird.
  - G-Star: WVB and Yay Abe.
  - Gallery Dept.: UGG footwear, LA Rams anorak.
- **Third-party product** is excluded:
  - Eastside Golf: Nike and Jordan golf shoes, even where the vendor field says Eastside Golf.
  - Evan Kinori: orSlow jean, and the Objects range (furniture, ceramics).
  - Freenote: Viberg, John Lofgren, Red Wing, White's, Nicks and Fenoglio boots.
  - Frye: Frye Exchange resale (Trove, Recurate).
- **Freenote's Past Season** range (43, all final-sale markdowns) is excluded.
- **Gallery Dept.:** Chateau Josué and Art That Kills are excluded (see rulings below).

## Prices: things to know
- **Markdown houses:** Eastside Golf, Flint and Tinder, Frye and Express (where nearly everything is promoted). Compare-at or list price is filed as regular.
  - **Eastside Golf** also tags many products "30% Off" with no compare-at. This is read as a checkout promotion, so the listed price is filed as regular.
- **Fusalp** sells in USD through Shopify Markets (rate 1.14775). Feed = displayed page on two products.
- **Shoe cells:**
  - NONE where every shoe is a collaboration: Flint and Tinder, Gallery Dept.
  - NONE where every shoe is stocked third-party: Eastside Golf, Freenote.
  - NONE where no footwear is sold: Evan Kinori, Express, Fusalp.
  - **Edward Green loafers:** 915 (Polperro, suede) to 2925 (Greenwich Unlined, Horween cordovan).
  - **Frye loafers:** 148 (Beau Penny, compare-at) to 278 (Chris Venetian).
  - **G-Star** has own-label shoes but no full-price loafer, so the range is all men's shoes (80 to 310).
- **Fur and exotic skins:**
  - G-Star's E Lammy Coat (1890, shearling) is excluded as fur.
  - Horsehide (Freenote's Grafton, 2400) is kept, as ruled.

## Fibre: the headline per house
- **Evan Kinori:** 96% natural, no synthetic-led style. Linen, hemp, wool, yak, cotton. Two thirds name the fibre in the title without a percentage.
- **Flint and Tinder:** 90% natural; 31 styles with elastane (stretch chinos and denim).
- **Freenote Cloth:** 89% natural. Leather jackets are filed by the hide in the title, because the body text gives the lining. Nine denim styles name no fibre (ND).
- **Gallery Dept.:** 88% natural (cotton throughout); the outerwear category is synthetic-led.
- **G-Star (sample):** 71% natural; jackets, puffers and gilets synthetic-led. Shape "one", because no synthetic-led category reaches 10 sample rows. This is an artefact of the 5-per-type cap.
- **Express (sample):** 50% natural, 29% synthetic. Split: shirts, hoodies, suiting and coats are synthetic-led; jeans, polos and dress pants natural.
- **Eastside Golf:** split, 40% natural / 51% synthetic. Tees, hoodies and sweatshirts are cotton; polos, pants, jackets and sweaters are polyester and nylon.
- **Fusalp:** split, 35% natural / 60% synthetic. Ski wear is synthetic; trousers and knitwear are wool.
- **Frye:** 34 leather and suede jacket styles, 100% natural.

## Doors
- **Express: 226 US.** All 226 directory store pages are rowed.
  - One is an Express Women store (Boca Raton), counted and flagged `womens-only`.
  - The 160 Express Factory Outlet stores (separate directory, 38 states) are outlets, not counted and not rowed.
  - World NC.
- **Fusalp: 2 US (Vail, Aspen), 40 world.** All 53 "Fusalp store" entries are rowed:
  - 5 outlets in outlet centres.
  - 4 department-store counters (concessions).
  - 4 Korean department-store pop-ups (see rulings).
- **G-Star: 9 US** G-Star-named full-price doors, carried from facts-first (8 Oct). The store endpoint was not reached this read. Rowed by name only, without street addresses except Soho.
  - 3 outlets are rowed and not counted.
  - Belmont Park Village (format unstated) is rowed and not counted.
- **Smaller houses:**
  - Edward Green: 0 US / 2 world (Jermyn St, Paris).
  - Evan Kinori: 1 (San Francisco).
  - Freenote: 2 (Los Angeles; San Juan Capistrano, flagged).
  - Gallery Dept.: 2 (Los Angeles, Miami).
- **No own door:** Eastside Golf 0, Flint and Tinder 0 (ruled), Frye 0 (ruled).

## Stockists rowed
- **Eastside Golf:** 112 addressed rows from its stockist.co list (mostly golf clubs and pro shops; 1 UK, 1 Bermuda).
- **Edward Green:** 10 US. **Evan Kinori:** 8 US (names and cities only on the page).
- **Fusalp:** 3 US partner stores of 110.
- **Flint and Tinder:** the 3 Huckberry stores, as `other brand own door`.

Not rowed:
- Freenote: no list (the stockist page returns 404).
- G-Star: 101 US points of sale counted in facts-first, not rowed.
- Express, Frye, Gallery Dept.: not looked for, or no list.

## Sections 6–13
- **Craft proposals:**
  - Edward Green 4: own Northampton workshop with headcount and weekly output, Horween named, process described.
  - Evan Kinori 3: made-in on every style, Fox and Casentino named, hand-linked knitwear described.
  - Freenote 3: every step claimed in California, "Sewn in USA" on 114 of 116 styles, Kaihara named; the workshop is claimed, not shown.
  - Flint and Tinder 2: a country on every style and three mills named; no maker named.
  - Gallery Dept. 2.
  - Eastside Golf 1, Express 1, Frye 1, Fusalp 1, G-Star 1.
- **Founding:**
  - Edward Green 1890, Northampton.
  - Frye 1863, Marlboro MA, John A. Frye.
  - Fusalp 1952, Annecy, Georges Ribola and René Veyrat.
  - Eastside Golf 2019, Olajuwon Ajanaku with Earl A. Cooper.
  - Gallery Dept.'s founder is not filed. The nav names Josué Thomas, but no page says he founded the brand.
- **Ownership:**
  - Express: Phoenix (WHP Global with Simon and Brookfield), from press.
  - Flint and Tinder: Huckberry (house label).
  - Not stated on the site for the others.
- **Quotes:** 7 of 10. Express, G-Star and Gallery Dept. are NC (no about copy read; Gallery Dept.'s about page is 404).
- **Vinted:** no brand entry for Eastside Golf, Evan Kinori, Flint and Tinder or Freenote Cloth. G-Star carries two IDs (G-Star 258, G-Star RAW 2782756).
- **Grailed:** no page for Eastside Golf.
- **Tech fabrics:**
  - Eastside Golf: TENCEL (2 styles).
  - G-Star: LYCRA and Sorona (5 sample rows).
  - Fusalp: NC, because the product-page technical blocks were not read.
  - Others: NONE.
- **B Corp, GOTS and pronunciation:** NC for all ten.

## What contradicted the record
- **Express doors are 226, not 216.** The facts-first crawl missed multi-store city pages.
- **Gallery Dept.'s doors are confirmed live** (11 Oct), with the LA phone number.

## For ruling
1. **Frye's men's jackets are made by a licensee (Moda Piel)** and sold under the FRYE name on Frye's own store. They are counted as own label, and they make up the whole style table and the outerwear cell. Should a licensee line count?
2. **G-Star sub-lines.** RAW Research (RR / GSRR) and the "E" premium pieces are counted as sub-lines sold under the brand. They set the shirt high (RR Baked Shirt 690), the jeans high (GSRR Maxi 590) and the outerwear high (GSRR Parka 1850). If they are capsules, each high falls to the main-line figure given in the cell note.
3. **Fusalp's 4 Korean pop-ups** sit inside Lotte and Galleria department stores. The store e-mails name them pop-ups and give no dates. They are not counted (40 world excludes them). Are they concessions or dated pop-ups?
4. **Freenote's San Juan Capistrano** location keeps office-style hours (Mon–Fri 9–5). It is counted and flagged; it may be the head office with a shop counter.
5. **Gallery Dept.:**
   - Chateau Josué is a sub-label sold on the same store under its own name, not GALLERY DEPT. It is excluded under the "sub-lines sold under the brand's name" test.
   - Art That Kills (the founder's record label merchandise) is also excluded.
   - Please confirm both.
6. **Express womens-only:** the Boca Raton Express Women store is counted under the 11 Oct ruling. Flagged only so you can see it.

## Method notes
- **Long Chrome scripts time out the extension.** The fix was to run each one as a background job that sets a flag, and poll for it. This was used for the Evan Kinori product crawl, the Express GraphQL passes and the Fusalp locator.
- **Express:** a plain fetch to `/graphql` returns an Akamai 400, but the site's own Apollo client works. Page navigation wipes window state, so IDs were carried in sessionStorage.
- **Fusalp's locator** base64-encodes its fields, and country names come back in French.
- **Search URLs not tested:** Evan Kinori, Flint and Tinder (Huckberry) and Fusalp, so those are NC. Express polo has no category URL; the search URL is given as the listing.
