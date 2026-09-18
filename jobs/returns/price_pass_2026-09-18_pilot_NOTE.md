# price_pass_2026-09-18: pilot note (8 rows)

## What was checked
All open cells for these 8 rows, read live on 18 Sep 2026 from each brand's own store:

- Todd Snyder
- J.Crew
- Barbour
- Polo Ralph Lauren
- Saint James
- Margaret Howell
- Auralee
- Brunello Cucinelli

`SKIP` cells were left untouched. The script refuses to write to any cell that isn't `NC`. Every cell that was `NC` is now filled. Results:

- Names: `reconcile.py` returned 8 exact matches, 0 rewrites and 0 unmatched.
- Schema: no blank cells, all figures are integers, and all enums are legal.

The row `note` names the product behind every figure, so any cell can be audited or overruled.

## What was not reached
- **The other 170 rows.** That was deliberate: the pilot comes first.
- **Barbour:** the page says "Showing 36 of 38 items", and "Show more" did not load the last two.
- **Materials were not checked product by product.** Fabric comes from product names, e.g. "Italian Suede", "Merino Mouton", "Cashmere".

## What contradicted the existing record or the brief's rules
1. **The Shopify rate rule gets Margaret Howell wrong.** `Shopify.currency.rate` is 1.36883 with USD active, so the rule says the feed is in GBP. But the storefront shows "$640.00 USD" and `/products.json` returns the same 640, so the feed is USD. The store uses fixed US-market prices, and the rule doesn't account for them. **Proposed rule:** check one displayed price against the feed before choosing `currency_basis`.
2. **The vendor field lies at Margaret Howell too.** Its three "Shoes" are Dr. Martens (1461 for MHL) and Mizuno, all under vendor "Margaret Howell". Add Margaret Howell to the rev 1 failure-class list.
3. **Auralee's search URL fails the `jeans` test, but the URL itself works.** Auralee calls jeans "denim": `denim` returns 10 results, `knit` 52, `coat` 12. Under the brief as written this URL is a failure. I've returned it with a note. Please rule on whether the test word can vary by brand.
4. **Auralee's USD prices include duties and taxes.** They are landed international prices, not US list prices, and aren't comparable with the other rows without a flag.
5. **Brunello Cucinelli prints prices in two formats on one site.** Knitwear shows `$ 1.650,00` (European separators) and loafers show `$1,200.00`. A naive parser reads the first as $1.65.
6. **Ralph Lauren's Brand filter leaks.** The Polo Ralph Lauren filter on sweaters also returns polos, caps and boys' items, so its "295 items" count isn't a sweater count. The per-label outerwear page (`brands-polo-ralph-lauren-men-outerwear-cg`, 76 items) is clean.
7. **Markdowns are common enough to matter.** At Todd Snyder, most sweaters below $298 are currently marked down, and the entry crewneck is on sale. I used the regular (compare-at) price, never the sale price.

## What this brief got wrong
1. **Rev 2 deleted the Definitions and the Failure classes without replacing them.** There is now no written rule for low/high, full price, or which shoes count. I worked to rev 1 plus the rules below. These rules decide every number, so please confirm them or replace them:
   - **Sweater:** the staple is the crewneck pullover. Low is the cheapest full-price own-label crewneck. High is the most expensive main-line crewneck in an elevated fibre.
   - **Outerwear:** find the cheapest jacket style that the brand also sells in an elevated material (suede, shearling or cashmere). Low is that style in its entry fabric; high is the most expensive elevated version. Examples: Harrington, cotton → suede; Dylan, denim → suede; Bayport, poplin → suede; safari, technical fabric → shearling.
   - **Shoes:** the staple is the own-label loafer, low to high. "Own-label" means the brand's name is on the shoe and it isn't made by a named third party. Alden for J.Crew is excluded.
2. **"Same staple" often doesn't exist.** Barbour has no loafer and no fabric step in its shoes. Margaret Howell's outerwear has no entry/elevated pair. For those rows I returned the plain price range and said so in the note. Is a range acceptable, or should those cells be held?
3. **Where entry is already cashmere, "high" is a judgment call.** At Brunello Cucinelli I returned cashmere → cashmere-silk ($4,000); $4,400 and $4,600 were also defensible. Expect the same at Loro Piana, The Elder Statesman, Kiton and Fedeli.
4. **There's no token for "looked, and every slot is sold".** An empty cell is an error and `NC` would be false, so `not_a_staple` has no legal value in that case. I used `ALL_SOLD`. Please name the token you want.
5. **The brief doesn't say what goes in a garment cell when the slot is absent.** "NONE in `not_a_staple`" covers that column only. The int columns still need a value, so I wrote `NONE` in `shoes_low` and `shoes_high` for Margaret Howell. `validate.py` may reject it.
6. **The schema only takes whole numbers.** Three prices end in .50: J.Crew 79.50, and Auralee 533.50, 4526.50 and 1149.50. I rounded half-up and wrote the exact figure in the note.
7. **"Dress shirt" is undefined.** Saint James's only men's woven shirt is a casual button-down at $195, returned as low = high.
8. **At full scale this is slow.** Each brand took several page reads, and custom platforms (J.Crew, Ralph Lauren, Brunello Cucinelli, Auralee) needed hand pagination. 170 rows under a 25-minute cap per brand is a multi-day job in one thread.

## Out of scope but noticed
- **Saint James:** 2 products typed "Shoes" under vendor Saint James.
- **Todd Snyder:** `/products.json` returned 3,200 products, a suspiciously round figure. Some items may sit beyond the feed's paging limit. The category reads looked complete.
