# NOTE: dials_followup_2026-11-06

Brands: Inkerman, Save Khaki United, Saint Croix. 114 rows (38 dials x 3), names match canonical_keys.txt dials. All three sites were read with a fetch-and-summarise reader (WebFetch). I did not open a browser, sign in, add to cart or submit anything. The map was not touched. Each brand was read by a separate reader and I merged the files without re-scoring them.

## Caveats for your rulings
- **Template:** dials_template.csv was empty (0 bytes). Columns used: brand, dial, proposed_score, evidence, source_url, confidence.
- **Inkerman:** 16 men's product pages read, but 0 of 16 had a care line, so fuss is NC. dur, golffice and sail are also NC. No lookbook link exists, so New New Englanders and the Journal stood in. The site does not label gender, so I treated all listed products as men's. The footwear count is unknown because the page is paginated. Copy conflict: the Long Sleeve Knit Polo in Red Stripe says "cotton" in the description but "100% Organic Linen" in Details.
- **Save Khaki United:** savekhakiunited.com returns a 302 to savekhaki.com. I read 15 men's product pages. Care lines appeared on only 3 of 15 (all "cold wash with like colors"), so fuss is medium confidence. The reader may have missed collapsed accordions. Cashmere and wool are NC because the Sweaters and Shirts collections were not opened. Sail is NC (no boating register). The men's collection page rendered no product list, so scope came from the Men nav and the lookbook.
- **Saint Croix:** 10 men's product pages read, all with care lines (7 of 10 dry-clean or spot-clean, 3 machine wash). No lookbook or Journal link found. denim and sail are NC. The size chart sits behind an FAQ link that was not read, so forg is low confidence. Product photos were not viewed, so logo is text-only and low confidence.
- **Zero scores:** several dials where nothing was seen are scored 0, although the rules print 1 as the floor for most scales. Decide whether those should be 0, 1 or NC. This applies mostly to Save Khaki United and Inkerman.

## Out of scope, noticed
- Save Khaki United: Port Canvas bags (Maine, sailcloth), SKU California activewear, women's Boyville line, 20th anniversary in 2026, Los Angeles production with Saitex LA denim washing. Site display bugs: outerwear says "1-14 of 14" but renders 34 items.
- Saint Croix: womenswear expansion in 2025, Miller Waste Mills ownership since 2024, a Limited Release capsule that includes skirts and dresses, many items "Awaiting Restock", and a Boiled Wool Vest page that shows a list price of $795 above a final price of $875.
- Inkerman: women's categories appear in the nav only.
- No page text contained instructions directed at me.
