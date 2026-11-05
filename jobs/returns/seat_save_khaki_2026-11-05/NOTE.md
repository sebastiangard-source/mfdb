# NOTE: seat_save_khaki_2026-11-05 (Save Khaki United), read 5 November 2026

**Status: partial.** Facts-first row was returned early. The full record below is complete on prices, doors, stockists, fibre, craft evidence, origin, lookbook, secondhand and certifier checks, and thin or NC on the items listed under "Not reached". Nothing here changes the map; Sebastian rules on every proposal.

## What I read

- Store: savekhaki.com is a Shopify store; `Shopify.country` = US, active currency USD, rate 1.0. USD confirmed on two displayed prices: $60.00 (Men's Short Sleeve Supima Crew Tee, mens-tees page) and $380.00 (The Bull Dog Trucker, mens-outerwear page).
- Men's scope: union of nine men's collections (mens-tees, polos, mens-shirts, mens-bottoms, mens-chinos, mens-sweats, mens-outerwear, mens-lounge, mens-shorts), cross-checked against `/products.json` (284 products, 2 pages, zero page 3). Excluded socks, hats, bags, gifts, gift card, Port Canvas, Third Party vendor goods, women's and Boyville. Result: 121 men's clothing styles, one handle per style.
- Journal and pages read: Who We Are; 20 Years of Save Khaki United; Building a Modern Chino; SKU Behind the Scene (founder note); Coming Full Circle; Rooted in Cotton; Good Work; AW26 lookbook; "To our family".
- External: Grailed designer page, Vinted catalog, B Lab directory, GOTS certified suppliers database.

## What contradicted the brief

- **Own stores.** The brief expected "All SKU Stores" and "Where to Buy" to be two lists. They are one section on the Who We Are page. It says "four retail stores in the U.S." and then lists **five** (SKU 317 and SKU 44 in NYC; SKU California and SKU LA in Los Angeles; SKU Montecito). I counted five because five are named and addressed. Sebastian to rule whether Montecito belongs (it is not in the "two in NYC, two in LA" sentence).
- **Founding.** No year is stated. The brand marks "20 Years" in 2026, so about 2006; founder David Mullen; New York City, near the Lafayette shop. Marked as derived, not stated.
- **"Chinos cut in Los Angeles from imported fabric."** The brand's wording is broader: all SKU-label products are sewn in the USA; fabric or yarn is sometimes imported and the label then reads "Made in USA of imported fabric or imported yarns". The founder note says early chinos were made in China before US production began, and that the brand renamed itself to Save Khaki United when US production started.
- **No prices on the home page.** True for a plain read, but the store shows USD prices on collection and product pages with no selector action needed (country already US).

## Own doors

Five shops, all listed as the brand's own, none labelled pop-up or concession. Not visited; open status not verified. Montecito's phone prints with area code 820 on the page. A 2010-era door decal photo reads 327 Lafayette; the page says 317.

## Stockists

Brand lists 27 domestic and 9 international retailers on the same page. Recorded in stockists.csv with the page as source; shop kinds are assumed from the list only.

## Fibre

114 of 121 styles state a composition (some as a named fibre with no percentage: 14 of the 114). All 114 are natural-led: cotton, Supima, organic cotton, cotton-hemp blends; two hemp-stripe tees carry 10% recycled polyester; one pant has 5% spandex (Twill Cozy Pant), the only elastane. Seven styles state nothing parsable (Legacy Denim Shirt, American Twill Back Terry Sweat Pant, Wide Wale Corduroy Pleated Chino, Harbor Sweater, Supima Zip Bomber, AA Twill Terry Blazer, Overdyed Camo Short); my parser's hit on four of them was not a fibre statement, so verify by eye. Shape: one cloth story. No named lines of five or more styles were measured, so `lines` is `-` and no lines file is returned. I did not build return_categories.csv or return_fibres.csv; the per-style file carries the data to rebuild them.

## Made in USA, product by product

Descriptions that state a made-in line: 49 of 121. Tag icon-local-manufacturing: 87 of 121. Tag imported_textile: 19. Where a made-in line appears it is usually "Made in USA of imported fabric/yarn/with imported fabric" (about 31). I did not open every product page, so the other 72 are "not stated in description", not "not made in USA". The brand's own site-wide statement is that all SKU-label products are sewn in the USA.

## Craft evidence (proposal 3, not a ruling)

Named by the brand: Saitex USA (denim wash, Los Angeles, claims 1 litre of water versus 100), Shai-Tex Inc (knitter, Lynwood CA, 55 circular machines), Cauzza Growers (Supima grower, Buttonwillow CA), Parkdale Mills (yarn), Mount Vernon and Inman Mills (cloth, on some product pages), Candor poplin. Owned: a sample room in Los Angeles, not a factory. The North Carolina spinner closed after 2024 floods; the Feb 2026 update says a new spinner was found, name not given. Heritage is dated and placed only by implication ("20 years", New York).

## Secondhand

Grailed: 163 listings under the Save Khaki United designer page (160 menswear). Vinted: 42 men's results for "Save Khaki United" (61 across all categories, a few unrelated); brand id not read; I did not search "Save Khaki" on Vinted beyond loading the page, and did not search "SKU".

## Certifiers

B Lab directory: searched "Save Khaki"; the results were fuzzy "save" matches with no Save Khaki United entry (B Corp = NONE). GOTS certified suppliers database: free-text "Save Khaki" returned "Your search did not match any records" (GOTS = NONE). These are searches by brand name only; a certified supplier in the chain could be listed under another entity.

## Quote

David Mullen, founder, in the founder note on the SKU Behind the Scene journal post (published 2025-09-27). I kept the quote short; the sentence continues with producing smaller runs, reducing carbon footprint and treating people better.

## Not reached or weak

- Search URL (empty-query test) not tested: `NC`.
- Pronunciation: `NC`. Owner today: `NC` (brand does not state; no filings read).
- Tech section: no tech rubric in the folder; no technical fabrics named; `proposed_tech` = `NC`.
- Per-style titles are as read from the feed and may be trimmed on three long titles; style rows have `lines` = `-`.
- Garment price low/high are `range` basis, not pair, and the listing URLs are parent categories except mens-chinos, mens-shirts, mens-outerwear and polos.
- Signature product (Original Chino) is proposed on the weaker evidence that the brand lists "SK933 The Original Chino" first in its Chino Guide; no page calls it the signature.

## What the brief got wrong

Treating "All SKU Stores" and "Where to Buy" as two lists; expecting no prices on the site; the brand's own count says four while listing five.
