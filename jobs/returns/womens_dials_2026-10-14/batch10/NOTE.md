# Batch 10 — womens_dials_2026-10-14, thread 2

Read on 14 October 2026 in Chrome, on each brand's own US store. All 10 brands are `read`, giving 797 style rows. `reconcile.py`: 10 exact, 0 rewrites, 0 unmatched. The method is the same as in batch 06. Percentages are of sampled styles; `fab_*` figures are of sampled styles that have a composition.

## What was read

| brand | channel | styles (census) | sampled | with composition |
|---|---|---|---|---|
| Ulla Johnson | Shopify feed descriptions ('Composition:') | 456 | 80 | 80 |
| Adam Lippes | Shopify feed + PDP 'Product Details' | 206 | 79 | 79 |
| Agua Bendita | Shopify feed + PDP 'Care and Composition' | 157 (clothing, swim excluded) | 78 | 61 |
| Cozy Earth | Shopify feed + PDP details metafield | 136 (women's) | 80 | 80 |
| Favorite Daughter | Shopify feed descriptions, PDP where blank | 394 | 80 | 79 |
| GABRIELA HEARST | womenswear collection feed ('Details' list) | 293 | 81 | 80 |
| Guizio | Shopify feed descriptions | 469 | 80 | 78 |
| HANRO | Shopify feed descriptions | 389 (lounge and sleep) | 80 | 56 |
| IRO | SFCC grid (/us/) + PDP 'Product details' | 251 | 80 | 80 |
| Jockey | store's product API (api.jockey.com) — the same bullets as the PDP | 127 (women's apparel) | 79 | 79 |

## Headlines

### Natural-led houses

- **GABRIELA HEARST** is 95% natural ("only certified natural fibers"): wool, cashmere, silk, linen, Sea Island cotton, leather. The only synthetic in the sample is a recycled-nylon lace bodysuit.
- **Adam Lippes** is 82% natural: silk, cashmere, Italian wool, cotton poplin.
- **Ulla Johnson** is 66% natural and silk-heavy, with viscose jersey (22% cellulosic) and polyester satin/lurex jacquards.

### Synthetic-led or split

- **Guizio** is the only synthetic-led house in the batch (59%): polyester suiting and corsets, mesh and satin dresses, acrylic/nylon knits (`split`).
- **Jockey** is split: cotton and organic-cotton stretch lounge against EverActive recycled-polyester activewear and polyester/rayon scrubs.
- **Cozy Earth** is 55% cellulosic (viscose from bamboo), with spandex in 46 of 80 styles.

### Tech

- **Three 2s, no 3+.**
  - GABRIELA HEARST: Aloe Linen, on about 4 of 81 sampled styles.
  - Jockey: EverActive, a named activewear line, on 19 of 79 sampled styles (24%). It is a line name over ordinary blends, not a fabric with stated properties — make it 1 if a line name should not count.
  - Cozy Earth: bamboo-viscose lines (Bamboo Stretch-Knit, Brushed Bamboo) with a cooling claim, about 45% of styles. No fabric is named as such.
- Everyone else is 1.

### Craft

**GABRIELA HEARST (4).** The strongest in thread 2 so far:

- 73 of 81 sampled pages state a country (Italy 69).
- The hand-knits name their maker, Manos del Uruguay.
- Wool comes from the founder's family farm, and the process record is dated.
- The garment factories are unnamed and not owned, which keeps it from a 5.

**HANRO (3).** Founded 1884 in Liestal. It describes mercerisation and hand-sewn lace, and states in-house fabric making with Austrian production on many pages. No factory is named.

**IRO (2).** Every sampled page states a country (seven countries, China the largest). No maker is named.

**Agua Bendita (2).** Colombian artisan embroidery with "a named artisan on every piece", but no artisan or workshop is visible on the site. Make it 3 if the label is taken on trust.

**The rest get 1.** Jockey has 150 years of dated history, but every page says only "Imported", and its ethics page describes audited third-party factories (WRAP co-founder, 1997).

## Not reached / partial

- **No walls this batch.** IRO's root redirects to /fr by location; the /us/ paths were used directly.
- **Gaps in composition:**
  - HANRO: 24 of 80 sampled pages name no fibre. Many others name fibres without percentages; those are filed as named, with lead percentage `ND`.
  - Agua Bendita: 17 of 78 pages give none. One dress gives an incomplete line (31% cotton, 23% linen), filed as written.
  - Favorite Daughter: one jacket composition is cut off on the page, filed `ND`.
- **Heritage `NC`:**
  - Agua Bendita: no date or place.
  - Favorite Daughter: founders named, no date or place.

## Contradicts the record / for the map

- **The worklist says not sold, but the store sells:**
  - Cozy Earth: a wool-cashmere cardigan and a sweater dress (worklist: no sweater).
  - Jockey: a varsity jacket and scrub jackets (worklist: no outerwear).
  - (Batch 09: GUEST IN RESIDENCE tees.)
  - In each case I left the link `NONE` per the worklist and kept the pieces in the fibre read.
- **Parent links:**
  - Jockey: its store has no per-category pages, only filter URLs. Tee → the women's tops filter; trousers → bottoms; dress → the apparel filter, which includes "Dresses, Skirts & Skorts".
  - Cozy Earth: dress → women's Clothing; outerwear → Hoodies & Sweatshirts (one quilted jacket).
  - Agua Bendita: tee and blouse share "Shirts and T-Shirts"; outerwear → Kimonos and Tunics.
  - Ulla Johnson: trousers → Pants and Jumpsuits.
- **Jockey scrubs** (tops, pants, lab coat) are sold in the women's department and were kept. Some are labelled "unisex". A pet pajama listed under women's was dropped.

## What the brief got wrong (adds to batches 06–09)

1. **Underwear, sleep and bedding houses** (HANRO, Jockey, Cozy Earth): their women's clothing is mostly pyjamas, lounge and robes. Filing those as `other` leaves thin garment groups, and `natural_pct` describes a lounge range, not ready-to-wear. The brief should say whether sleepwear is in scope for these houses. I read it and filed it as `other`.
2. **Non-fibre materials by weight.** Two GABRIELA HEARST knits are 60% glass beads, so the beads lead. I filed what is written (`other`). A rule is needed on whether embellishment counts.
3. **Fibres named without percentages** (HANRO) are not covered by the ND/NONE/NC codes. I filed the named fibres with lead percentage `ND`, rather than calling the page `ND` outright.
4. **Line names vs fabric names** (Jockey EverActive, Cozy Earth bamboo lines): the tech rubric should say whether a branded line over ordinary blends counts as a "named fabric".

## Method notes

- Parser changes this batch: TENCEL™/Lenzing™ modal and lyocell are normalised to modal and lyocell. I re-ran batches 06–09 after the change: 0 style rows changed, and the brand rows are identical.
- **Jockey:**
  - The catalogue was read from the store's own API, which serves the PDP.
  - Where a page gives one composition per colour (solid against heather), the first is read.
