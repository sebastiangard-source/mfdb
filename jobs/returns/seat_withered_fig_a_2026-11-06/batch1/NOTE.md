# NOTE: batch 1 (Iron Heart, The Flat Head), seat_withered_fig_a_2026-11-06

Status: partial full records, returned at the time box. Corrected facts-first rows are in ../facts_first.csv. UES is next (batch 2).

## What was read
- Iron Heart: the shop's products.json (1,404 products; 821 are vendor Iron Heart), Our Story, Official Stores, two product pages. USD confirmed on two displayed prices at the US setting ($100 and $2,200).
- The Flat Head: tee list (both pages), jeans, shirts, outerwear, pants and footwear lists, history page, shoplist, one jeans page. Yen, nothing converted.
- Denime: loads. No prices, no online shop, no own stores; 109 independent stockists. Brand page says its 2023 relaunch draws on Warehouse's know-how, which is not on the map, so I did not stop on it, but Sebastian should rule.

## Retries
- Pure Blue Japan: connection timed out (www.purebluejapan.jp). Stays NC, facts-first row only.
- Studio D'Artisan: dartisan.co.jp loaded blank. Stays NC, facts-first row only. The browser tool then stopped responding for a while, so I did not retry. No cache or mirror used.
- A human reading their shop lists and prices is the realistic fix, as you said.

## Corrections to my earlier return
- Iron Heart tee entry is USD 100, not 75 (the 75 was UTILITEES, a different vendor on the same site). Top is USD 2,200, not 2,050.
- Flat Head entry tee is JPY 9,900, not 11,000.

## Not done, and why
- return_styles.csv is header only. The browser tool truncates output at about 1,000 characters, so 468 style rows could not be brought back. What I can say: of 468 Iron Heart apparel styles, 72 state a fibre percentage by my text method (58 pure natural, 10 blends, 4 pure synthetic), 396 state none (ND). Flat Head: not counted.
- Dials: 8 Iron Heart and 6 Flat Head scored; the other 30 each are NC. I did not open ten product pages for logo, fuss or comfort.
- Not read: Iron Heart stockists page, lookbooks, Vinted and Grailed, B Corp and GOTS directories, tech, signature product, pronunciation, search URLs, the Flat Head company page and its dealer lists. All are NC.
- Flat Head 1996 founding stays press-grade (retailer); the history page text I read gives the founder's birth year (1959), not the brand's.

## Things the brief got wrong or should know
- dials_template.csv is empty (0 bytes). I used columns brand, dial, proposed_score, evidence, source_url, confidence.
- Shopify vendor and product_type fields lie on Iron Heart (painter pants typed Jackets; other brands under the same shop).
- The facts-first template has no field for currency; I put it in the price cells.
- Names do not match canonical_keys, as expected.

## Update (second pass)
- Iron Heart: FW26 lookbook, care guidelines and repairs pages read. Dials now 8 scored with dur raised to 5 (free repairs for life) and fuss +1. Grailed designer page exists. Stockist locator is a script widget I could not read.
- B Corp and GOTS: the B Lab directory ignored my search term in the address, so no result was read. Left NC for all three brands rather than asserting none.
- Per-style fibre rows are still not returned: the browser tool cuts output near 1,000 characters.
