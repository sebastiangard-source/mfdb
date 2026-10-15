# batch04 — womens_dials_2026-10-14, thread 1 reissue

Read 15 October 2026 in Chrome on each brand's own US store. 10 brands, 792 style rows. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. No empty cells, and every enum is legal.

## What was read

| brand | platform / channel | styles in scope | sampled | ND | tech | craft |
|---|---|---|---|---|---|---|
| SKIMS | headless Shopify (Hydrogen); `/products.json` 404s | no total shown (100 distinct on first grid pages) | 80 | 0 | 3 | 1 |
| 7 For All Mankind | Shopify feed + PDP `fabric-composition` attribute | 445 | 80 | 1 | 3 | 2 |
| EDIKTED | Shopify feed + PDP detail list (fibre names, **no %**) | 6,298 | 80 | 1 | 1 | 1 |
| Rip Curl | Shopify `womens-clothing` collection + PDP spec table | 344 | 80 | 0 | 3 | 2 |
| St. John | Shopify feed + PDP Product Details list | 302 | 80 | 2 | 2 | 2 |
| Beyond Yoga | Shopify feed + PDP free text | 310 | 80 | 3 | 5 | 2 |
| Cotopaxi | Shopify feed + the house's product API the PDP renders from | 104 (after men's dropped) | 72 | 7 | 3 | 2 |
| Maje | SFCC, `view-all-clothing?sz=800` + PDP Composition & care | 589 | 80 | 1 | 1 | 2 |
| Max Mara | client-rendered grids, scrolled in Chrome across 13 categories | 304 | 80 | 0 | 2 | 4 |
| Splendid | Shopify feed; composition injected client-side, so each sampled PDP was opened in Chrome | 530 | 80 | 2 | 2 | 1 |

Every share is out of all styles in the table, ND rows included. **Understated because of ND:** Cotopaxi (7 of 72 rows ND: down and fleece pieces that say only "100% recycled shell/fabric"; this understates synthetic). Beyond Yoga and St. John are lightly affected (3 and 2 rows).

## Headlines

- **Max Mara is the only proposed craft move above 2.** Its own mm-world page names Manifatture di San Maurizio, a plant outside Reggio Emilia making "over 100,000 coats and jackets" a year. I proposed a **4**: owned and named, but it covers coats only and no product page states a country.
- **Beyond Yoga, tech 5.** 88% of its 310 in-stock styles carry a house-trademarked fabric (Spacedye™, glowzone™, LuxeFleece™ and others); the Spacedye family alone is 39%.
- **7 For All Mankind** names its own denim fabrics (Slim Illusion, Luxe Vintage, B(air), Weightless) on 31% of styles. That is proposed tech 3, not 4, because none of them is a performance fabric.
- **SKIMS**: its tech score rests only on Nike's Dri-FIT in the NikeSKIMS co-brand (12 of 80 styles in the line, 2 naming Dri-FIT). The Spectrum thread may prefer a 2.
- **Fabric dials of note:**
  - Max Mara: wool 5 (49% wool-led, plus camel, alpaca and cashmere).
  - 7 For All Mankind: denim 5 and cotton 5.
  - Splendid: cellulosic 34%, with 7 lyocell/TENCEL-led styles kept as lyocell.
  - St. John: cellulosic is the largest class at 40% (viscose knits).
  - Silk reaches 2 only at Maje, Max Mara and St. John.

## What contradicted the record or the brief

- **EDIKTED publishes no percentages.** The detail list reads "Rayon, Spandex". Per rules_fibre a named fibre counts as a composition, so the lead is the first-listed fibre, and `lead_pct` and `elastane_pct` are `ND` on those rows. That is 75 of the 80 rows; the other 5 state percentages. Spandex is counted by presence. Its shares are softer than any other house's.
- **SKIMS has no total.** The headless store server-renders 12 tiles per collection and lazy-loads the rest with no counter. The sample is 80 of the 100 distinct styles on the first grid page of 19 collections, so `styles_total` is the sample, not the range. The payload trap from rules_fibre fired here: the first composition string in the page payload belongs to a recommended product on some pages, and it caught three faux-leather styles. All 80 rows were re-read from the server-rendered Fit & Fabric list.
- **Cotopaxi** tags 8 men's-named products (e.g. "Capa Insulated Vest - Men's") into the women's outerwear tree. They were dropped, not counted as unisex. 72 rows remain.
- **Maje** soft-404s: an unknown category path returns 200 with a default grid. Every link was checked by the product-code family in its first tiles.
- **Max Mara** sells its own lines on one store: Weekend Max Mara is 34 of 80 sampled rows, plus 'S Max Mara, Studio, Sportmax, The Cube and Elegante. They are kept and tagged in `lines` from the model-name prefix.
- Worklist `_sold` flags: none were wrong. Thin categories exist where the flag says yes:
  - Beyond Yoga blouse: 1 woven top.
  - Rip Curl and St. John jeans: 4 styles each.
  - Max Mara jeans: 1 denim style in the sample, no jeans-only category.
  - Cotopaxi dress: 2 dresses.
  - In each case the link is a parent category, and the `note` says so.
- **Unisex:** Beyond Yoga lists one LuxeFleece Unisex Half Zip in the women's section; it is counted and flagged.
- **Sports bras** (Beyond Yoga) and **bras** (SKIMS) were excluded as intimates. If the Spectrum thread wants sports bras in for activewear houses, Beyond Yoga's synthetic share rises.

## Not reached / limits

- Made-in country is almost never in product text. Maje delivers it through a Fairly Made widget and a label QR code, which I did not read. Cotopaxi gives a factory country (Cambodia) on about 10% of styles.
- Cotopaxi's per-product factory tab links to a factory profile that I did not open.
- St. John's reputation for in-house knitting does not appear on its own site; its craft 2 rests on what the site shows.
- No bot walls met.

## Out of scope but noticed

- Max Mara's "/editorial/denim" is a campaign page that looks like a jeans listing; it was not used.
- Rip Curl's wetsuit neoprenes (Flashbomb, E-Bomb, Dawn Patrol) are its real tech story, but they sit outside the clothing table.
