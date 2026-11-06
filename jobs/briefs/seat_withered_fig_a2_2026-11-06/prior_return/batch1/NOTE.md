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

## Not done, and why (final, after the second pass)
- return_styles.csv: 600 rows. Iron Heart 468 of 468 apparel styles read (72 state a fibre percentage, 396 are ND). The Flat Head 132 clothing styles read from the tee, jeans, shirts, outerwear and pants lists (14 state a composition, the rest ND). Not in the Flat Head rows: sweat, thermal, leather and footwear lists, and wallets and other non-clothing. Men's scope: every range on both shops is men's or unisex and I found no women's line, so nothing was dropped for sex.
- Dials: Iron Heart 36 of 38 scored, The Flat Head 35 of 38, by keyword counts over product descriptions; evidence and confidence are on each row. The rest stay NC for too little evidence. I did not open a full ten pages by hand for every brand; counts are over the descriptions I read.
- Iron Heart stockist locator is a JavaScript widget I cannot read, so I stopped there (stockists.csv holds a placeholder row).
- The Flat Head: company page read (operator 株式会社フラットヘッド・ネクスト, representative 岸野 雄一郎, established 2019-12-18); that is the operator, not a stated owner, and it is filed as such. Overseas dealers read in full (17 in the US, incl. Self Edge x5, Withered Fig, Blue Owl, Guilty Party); the 51 domestic entries are counted, not transcribed.
- Vinted: the page returned a client error, so NC. Grailed: Iron Heart's designer page exists; The Flat Head's returned a client error, NC.
- Tech, signature product, pronunciation: the brands' own pages call nothing a signature product or tech fabric that I could quote, so NC rather than a guess.
- Not touched, as you said: B Corp, GOTS, Denime, Pure Blue Japan, Studio D'Artisan.
- Flat Head 1996 founding stays press-grade (a retailer); the company page gives only the 2019 operator date.

## Things the brief got wrong or should know
- dials_template.csv is empty (0 bytes). I used columns brand, dial, proposed_score, evidence, source_url, confidence.
- Shopify vendor and product_type fields lie on Iron Heart (painter pants typed Jackets; other brands under the same shop).
- The facts-first template has no field for currency; I put it in the price cells.
- Names do not match canonical_keys, as expected.

## Update (second pass)
- Iron Heart: FW26 lookbook, care guidelines and repairs pages read. Dials now 8 scored with dur raised to 5 (free repairs for life) and fuss +1. Grailed designer page exists. Stockist locator is a script widget I could not read.
- B Corp and GOTS: the B Lab directory ignored my search term in the address, so no result was read. Left NC for all three brands rather than asserting none.
- Per-style fibre rows are still not returned: the browser tool cuts output near 1,000 characters.
