# Batch 11: womens_dials_2026-10-14, thread 3

Read on 14 October 2026 in Chrome, on each brand's own US store. There are 10 brand rows, and 560 style rows for the 7 houses that sell clothing. `reconcile.py` gives 10 exact matches, 0 to rewrite and 0 unmatched. No empty cells, and every enum is valid.

## What was checked

| brand | store / platform | styles (site) | sampled | with composition | status |
|---|---|---|---|---|---|
| La DoubleJ | www.ladoublej.com/en-us · SFCC PWA Kit | 642 style×fabric (465 style nos.) | 80 | 78 | read |
| Manolo Blahnik | /us · Magento | no clothing | n/a | n/a | read (links + craft) |
| Monique Lhuillier | Shopify | 334 | 80 | 13 | **partial** |
| O'Neill | us.oneill.com · Shopify | 331 | 80 | 80 | read |
| Pucci | /en-us · Shopify | 371 | 80 | 79 | read |
| Roger Vivier | /us-en · SAP | no clothing | n/a | n/a | read (links + craft) |
| Stella McCartney | /us/en · SFCC | 348 | 80 | 71 named, 0 with % | **partial** |
| 3.1 Phillip Lim | Shopify | 120 | 80 | 80 | read |
| Altuzarra | Shopify | 249 | 80 | 79 | read |
| Aquazzura | /us_en | no clothing | n/a | n/a | read (links + craft) |

Every house was over 80 styles, so each one is a stratified sample of 80. Each house category got a share proportional to its size, and styles were picked evenly spaced through the category after sorting by style code. The row's `sample_basis` gives the site total and the source it was counted from. **The percentages and fab_* figures are shares of the 80 sampled styles, not counts over the whole range.** `styles_total` is the site figure.

## Headlines

- **Silk is real on the women's side.** It leads 26 of 80 at Pucci (fab_silk 4), 15 at La DoubleJ, 10 at Altuzarra and 5 at Lhuillier (of only 13 readable). I'd keep `fab_silk`.
- **Cellulosics are a third bucket worth a dial.** Pucci is 29% cellulosic-led, Stella 31%, O'Neill 26%. On women's ranges viscose sits where synthetics sit on men's.
- **Split houses:** O'Neill (outerwear and snow are synthetic, tees, pants and shorts cotton) and Pucci (synthetic jersey tops against silk dresses and skirts).

## What contradicted the record or the brief

1. **Shoe-only houses (Manolo Blahnik, Roger Vivier, Aquazzura):** sections B and C have nothing to read. I put `NONE` in the fab_* and fibre cells, not 1s. On the 1–5 scale a 1 means "none", which would read as a finding about a range that doesn't exist. If the map needs integers there, convert at merge.
2. **Monique Lhuillier publishes almost no fibre.** Only 32 of 361 clothing listings carry a percentage. Product pages name the cloth (mikado, faille, gazar) and a colour called "Silk White", which I did not read as silk. Coverage in the sample is 13/80, so **I'd hold its fab_* and split.**
3. **Stella McCartney publishes no percentage composition anywhere on the US store** (checked the page, JSON-LD and the controller list). Fibres are named in the copy ("forest-friendly viscose", "RWS-certified wool"), so those count as named-fibre compositions with `lead_pct = ND`, and spandex is ND. Each product page also has a "Sustainability" block that is boilerplate and wrong on some products: a vegan-leather skirt's block talks about silk, a chainmail top's about organic cotton, and one is served in German. I did not use it.
4. **O'Neill sells denim pants** ("Sevie Denim Pants" in womens-pants), but the worklist says `jeans_sold = no`. I left the cell `NONE` as briefed; the worklist may need correcting.
5. **Pucci's `/products.json` is not in dollars:** `Shopify.currency.rate` is 1.14695 with USD active. Composition lives in two places by season: current styles in a PDP "Product Care" block, earlier styles in the feed body. 20 of the 80 sampled Pucci styles are sold out but still listed.
6. **Roger Vivier:** the bare `/us-en` root bounced once to `/gb-en/error`, which is the locale-swap failure class. Deep US paths hold.
7. **3.1 Phillip Lim:** the store's own tags give a country (CHINA on 170 of 174 listings), but product pages never show it. I scored made-in as 0% on the page and noted the tag.

## What the brief got wrong or left open

- **`fab_denim` has no fibre to read.** I scored it on styles in the jeans category **or** whose composition or title says denim. That way denim jackets, skirts and shorts count. `fab_basis` says so.
- **`shape` on a sample:** a category is counted as big (≥10) from the site total, and its lead class comes from the sample.
- **Named-fibre-without-percent** (Stella, Lhuillier cloth lines) is treated as a composition, as rules_fibre allows. The lead is the first fibre named, and `lead_pct` and `elastane_pct` are `ND`. If the Spectrum thread would rather count these as undisclosed, filter on `lead_pct = ND`.
- **No current craft score is in this worklist**, so there is no proposed-vs-current table. All proposals are 1–2: no house in this batch names a maker or mill on product pages.
- `links_kind` notes each place a parent category stands in (trousers under "shorts & pants", tees under "tops", jeans under "pants").

## Not reached

- Aquazzura's made-in: the field loads only on click, so I opened one PDP by hand (ITALY). Roger Vivier: 8 of 12 sampled PDPs were read; 4 sampled links were mis-encoded.
- I didn't open Manolo Blahnik's Archives "The Craft" room beyond its opening quote, because it's an interactive experience.

## Out of scope, noticed

- Pucci's knitwear collection also holds a jacquard dress. Altuzarra's denim pants sit under Pants with no denim node. 3.1 Phillip Lim's `/collections/denim` mixes a bag and two men's pieces.
