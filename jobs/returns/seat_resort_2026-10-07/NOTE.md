# seat_resort_2026-10-07 — return note

Read 7 October 2026, in Chrome, on each brand's US storefront. `reconcile.py` on every brand name across the four files: 2 in, 2 exact, 0 rewrites, 0 unmatched. No empty cells. Nothing on the map was touched.

## The swim question, answered first

| | styles | swim | swim share | excl. swim | natural / synth / cellulosic (all styles) | excl. swim |
|---|---|---|---|---|---|---|
| Frescobol Carioca | 107 | 24 | 22% | 83 | 73 / 21 / 5 (1 undisclosed) | 78 natural, 5 cellulosic, 0 synthetic-led |
| Orlebar Brown | 227 | 41 | 18% | 186 | 75 / 19 / 4 (5 undisclosed) | 171 natural, 9 cellulosic, 3 synthetic-led, 3 undisclosed |

Swim was counted and is in the denominator: 23 of FC's 24 swim styles and 39 of OB's 41 are synthetic-led. Outside swim, both houses are one-cloth natural houses (`shape` = one, `synthetic_categories` = []). The high natural share is real. It comes from linen, cotton and merino shirts, polos, trousers and shorts.

**Swim looks bigger by listing than by style.** At OB swim is 30% of colourway listings (199 of 653) but 18% of styles: the Bulldog alone has 57 print listings. At FC it is 49 of 244 listings, or 22% of styles. If a reader's sense is that these ranges are mostly swim, that comes from the prints.

## What was read

- **Frescobol Carioca.** Read `products.json` (370 records; page 3 returned 0). US scope is the "live in US" tag with a US price, which matched every navigation collection read. Compositions come from the body HTML. That gives 244 listings and 107 styles by SKU stem, and the swim set matches `/collections/swimwear` (48 + 1 listings). Two displayed PDP prices confirm USD. Also read: the stockist.co list (122 rows), the retail page, about, heritage, Art of Summering, Behind the Prints, the blog sitemap, and Companies House 05551772.
- **Orlebar Brown.** Read `/en-us/products.json` (755 records; page 5 returned 0) and fetched all 653 in-scope PDPs for the composition accordion, the garment country and the displayed price. Displayed and feed prices agree on 652; one exception is noted. Also read: the stockist.co locator (61 rows), every store page sampled, About, Sustainability, the AW26 lookbook, and Companies House 05502027.
- **Both brands.** Vinted men's brand filter (ids read from the facet); Grailed designer pages; B Lab directory; GOTS database (no match for either).

## What the brief got wrong, or could not say

1. **"Orlebar Brown's locator mixes own stores and stockists; read the labels."** On 7 Oct the locator has no labels, and every one of its 61 rows links to an OB store page. It lists no third-party stockists, so `stockists.csv` holds a single NONE row for OB. What the locator does mix is operators. Six own-door rows carry partner email domains (Salt Water, Greece ×2; Mizzen, UAE ×3) and Kuwait has no email. I filed `own_doors_world` = 32 (operated by OB); the figure counting every OB-branded own-door is 39. US = 10 either way. The `format` enum has no franchise value, so these rows sit as own-door, with the operator in `status` and `note`.
2. **"A shop inside a department store or hotel is a concession."** For OB this rule moves a lot: 13 of its 20 concessions are hotel or resort shops (Setai South Beach, Carlton Cannes, InterContinental Madrid, Rosewood, St Regis and others). The Setai row is the US case to check: it could be a street-front unit.
3. **No style code at OB.** The Item No. is per colourway. Styles were built as house model title × main composition × house category (`title_dedup`). Re-cutting on another rule needs only `return_styles.csv`.
4. **Knitted polos.** FC tags its knitted polos as both Knitwear and Polo Shirts, so they were filed as knitwear by garment. OB files every polo under Polo Shirts, so they were kept there by house label. This affects the category table only, not the brand totals.
5. **Jeans.** OB makes no men's jean, so the cell is NONE. FC's only jean is Mendes; its listing link is the Move Freely Denim collection, a parent that also holds the jacket, shirt and tee.
6. **Shoes.** Neither house sells a loafer pair. OB's own-label footwear is a swim shoe, a swim trainer and a sandal (`range`). FC files its Leme slippers and Marina deck shoes under its own "Loafers" collection, so the cell is a range across that collection.

## Contradictions with the record or the press

- **FC founding.** The brand says 2013. The company was renamed FRESCOBOL CARIOCA LTD on 3 Dec 2012 (incorporated 2005 as Glowing Star / Frescobol Ltd). Mr & Mrs Smith (2018) gives 2009. Filed: 2013, as the brand states it.
- **FC "where it makes things."** For clothing the claim does not hold on the brand's own pages. Only 5 of 107 men's clothing styles state a country, and none names a maker or a mill. It does hold for bats (handmade in Brazil) and shoes (handcrafted in Italy). Proposed craft 2 (1 if bats and shoes are set aside).
- **OB data issues.** OB's "Main:" composition field gives the lining on the Dorien gilet, so its merino shell was filed instead. Bray rash guards are polyamide in "Main" but polyester in the fabric line; "Main" was filed. The Maitan Broderie title says "Made In Italy" but the PDP says Portugal. One Ob-T Merino listing shows $375 against $295 for its twins.
- **Ownership.** OB's PSC filing shows Chanel Limited at 75%+ since 25 Sep 2018. FC's only PSC is founder Harry Brantly (25–50%). YFM Equity Partners lists a £3m growth investment (2019), but no parent is named, so FC is filed as independent.

## Proposals (Sebastian rules)

| | tech | craft |
|---|---|---|
| Frescobol Carioca | 2 — 21% of styles claim performance (all swim, quick-dry), commodity cloth | 2 — country on 5% of clothing, no names; one documented shirt |
| Orlebar Brown | 2 — 7% claim performance; ECONYL and SEAQUAL licensed; UPF rash guards, water-repellent jacket | 2 (strong) — garment country on 95% of styles and fabric origin on 89%, but nothing named and nothing owned |

## Not reached / judgement calls to check

- **OB pronunciation:** NC; nothing on the site.
- **FC Vinted:** only one brand id (548551) appears in the men's facet. Many "frescobol" listings carry no brand id.
- **FC stockist count:** the page header says 212, but the locator API returns 122 (the header is hard-coded theme text). Some postcodes lost their leading zero in the locator; they are kept as listed and flagged.
- **FC SoHo store:** `own_doors_us` = 1, from the brand's retail page. FC's own Portonovi outpost also appears on its stockist list; it is flagged on both rows.
- **Time box:** sections 1–5 overran for OB, because all 653 PDPs were read rather than sampled. Nothing is NC for time.

## Out of scope but worth keeping

- FC sells a $27,000 La Marzocco espresso machine and coffee cups in its feed, from the Cafezinho Carioca collaboration. Its "Belmond" capsule is made for Belmond hotels, and 9 Belmond and One&Only hotels are on its stockist list.
- FC stockists for the register: 23 rows are clothing boutiques (door one). 63 are hotel or resort shops, which need a door-one check. The 2 Haremlique rows are another brand's own shops.
- OB carries retailer- and hotel-exclusive styles on its own site ("for MR PORTER", "for Hotel Du Cap") and two collaborations (James Bond 007, Automobili Lamborghini). None was used as a price high.
- OB's About page claims "more than 50 direct stores, and over 250 additional locations", but the locator shows 61 OB-branded points.
- OB's Sustainability page says "96% of our products are made in Europe". PDPs agree: Portugal accounts for 159 of 215 styles that state a garment country, and Cambodia for 2.
