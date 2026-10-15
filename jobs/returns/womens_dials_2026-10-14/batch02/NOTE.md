# Batch 02 — womens_dials_2026-10-14, thread 1

Read 14–15 October 2026, in Chrome, on each brand's own US store. The batch-01 review points are still open, so I applied these defaults throughout (each can be re-cut from `return_styles.csv` without re-reading):

- **Multi-brand stores are read as own labels only.** This follows the wave C Beams ruling. It affects Evereve, Aritzia and Reformation (3 Patagonia styles were dropped).
- **Category mapping, the denim dial, sleepwear and the 80-style sample** are all handled as in batch 01. Knit tops go to `tees-polos`, wovens to `shirts`. `fab_denim` = denim garments. Sleepwear and swim are excluded. The `shape` test uses 5 or more sampled styles.

`reconcile.py`: 10 names in, 10 exact, 0 to rewrite, 0 unmatched.

## What came back

| brand | status | styles (with comp.) | nat / syn / cell % | spandex | shape | denim·cash·linen·cotton·wool·synth·silk | tech | craft |
|---|---|---|---|---|---|---|---|---|
| Altar'd State | partial | 80 (63) | 26 / 44 / 9 | 25 | split | 3·1·1·4·1·5·1 | 2 | 1 |
| Lilly Pulitzer | read | 80 (80) | 62 / 25 / 12 | 43 | split | 2·2·2·5·1·4·2 | 3 | 1 |
| Evereve | read | 80 (80) | 42 / 34 / 24 | 32 | split | 3·2·2·4·1·4·1 | 1 | 1 |
| Aritzia | partial | 73 (73) | 42 / 51 / 7 | 27 | split | 2·2·2·4·2·5·2 | 4 | 1 |
| Tory Burch | read | 80 (80) | 76 / 12 / 11 | 16 | one | 3·1·2·5·3·3·2 | 2 | 2 |
| Reformation | read | 76 (73) | 55 / 12 / 29 | 22 | one | 3·2·3·4·2·3·3 | 2 | 4 |
| Brandy Melville | partial | 80 (80) | 86 / 11 / 2 | 15 | one | 2·1·1·5·2·3·1 | 1 | 2 |
| Michael Kors | partial | 80 (80) | 34 / 58 / 9 | 23 | split | 3·1·1·4·2·5·1 | 2 | 1 |
| Lucky Brand | read | 80 (80) | 71 / 15 / 14 | 20 | split | 4·1·2·5·1·3·1 | 3 | 1 |
| Eileen Fisher | partial | 80 (80) | 71 / 4 / 25 | 39 | one | 2·2·2·4·3·2·2 | 3 | 3 |

In this table, `partial` means at least one cell is `NC`. The `note` column in each row names the cells. "With comp." counts styles whose page gives a composition. At Reformation, 3 leather pieces name the material but give no percentage.

### Craft

This batch is more spread out than batch 01, which was all 1s.

- **Reformation — 4.** This is the highest proposal so far and needs your eye. Its about page says it makes "at our Los Angeles factory and at our partner factories". 6 of 76 sampled pages say "made in Los Angeles". It publishes its full Tier 1 factory list (August 2026 PDF; linked, not opened). 74 of 76 pages state a country. The ownership rests on the brand's own statement. If the Tier 1 list shows no owned LA facility, this should be a 3.
- **Eileen Fisher — 3.** All 80 pages state a country. A journal piece names two Fair Trade cut-and-sew factories (PT Tainan, PT Ungaran) and what they sew. Renew is owned, but it is second-life remaking, not production.
- **Tory Burch — 2.** 13 of 80 pages state a country (Italy for denim, India for hand-embellished pieces, Portugal for jacquards). Nothing else is named.
- **Brandy Melville — 2.** 79 of 80 descriptions state a country: China 42, Italy 26, "Europe" 9, Switzerland 2. Nothing else is stated, and the US store has no about page.
- **The other six are 1.** Michael Kors says "Imported" on every page. Lucky Brand states no country at all; its one placed claim (selvedge from Louisiana cotton, sewn in LA) is a single capsule with no mill named.

### Tech

- **Aritzia — 4.** Its named fabric families carry 47% of sampled styles.
- **Lilly Pulitzer, Lucky Brand and Eileen Fisher — 3.** The house-named cloths are Luxletic (UPF 50+), Cloud Soft / Liquid Denim, and Washable Stretch Crepe / Washable Flex Ponte. These are the same kind of evidence as Chico's Travelers™ in batch 01.
- **Reformation — 2.** It licenses many fibre brands (TENCEL, ECOVERO x REFIBRA, Naia Renew, CIRCULOSE, NATIVA). They are sustainability fibres, not technical cloths, so I left `tech_named_fabrics` as NONE (performance) and listed them there.

## Contradicts the worklist

- **Altar'd State sells shoes.** The worklist has `shoes_sold = no`, but there is a New Shoes node. The cell is filed `NONE` per the brief.
- **Lucky Brand sells shoes.** The worklist has `shoes_sold = no`, but `/shoes/womens` lists 41 styles. The cell is filed `NONE` per the brief.
- **Michael Kors sells tees.** The worklist has `tee_sold = no`, but the Tops node carries T-shirts (2 of 11 sampled tops are Watch Hunger Stop tees). There is no tee node. The cell is filed `NONE` per the brief.
- **Evereve is a stockist,** not a house. Its feed has 114 vendors, and EVEREVE is 1,108 of 4,784 products. It was read as own label only.
- **Eileen Fisher sells shoes but has no shoes node.** A site search returns 84 results (sandals, clogs, sneakers), and `/shop/accessories/shoes` redirects to Sale. The cell is `NC`, as with Aerie's jackets in batch 01.
- **Brandy Melville outerwear:** 1 jacket and 1 vest exist, but there is no jackets or outerwear collection. The cell is `NC`.

## Not reached, or read with less than the playbook asks

- **Aritzia's census is partial.** Its Algolia index stops at 1,000 hits (of 1,862). The sample is drawn from the 916 master styles it returned.
- **Altar'd State:** 17 of 80 sampled pages state no composition, mostly sweaters. Heritage was not read.
- **Michael Kors strata come from product names.** The site's Category filter could not be fetched by URL. Its own counts are in `sample_basis`. There is no brand-history page on the US store, so heritage is `NC`.
- **Eileen Fisher grids show more tiles than their stated totals** (look-book tabs). So some styles carry another node's house label. Category is taken from the product name, so the dials are unaffected.
- **Tory Burch's census is first page per node** (185 styles). The view-all page and `?page=N` added nothing new.
- **Tory Sport is no longer a separate store.** `/sport/clothing/` lists main-line styles, and a 10-page check found no named fabric.

## Parsing traps found (all fixed before return)

- **Marketing percentages ahead of the real line.**
  - Michael Kors: 6 pages say "contains at least 85% organic cotton", then the bullet says "100% cotton".
  - Eileen Fisher: "made with 100% organic cotton and garment dyed…", then the composition.
  - The fixes: MK re-reads its 6 pages and uses the composition bullet; EF is read from the Fabric block only.
- **Qualifier words that hid the fibre.** These are Reformation's "Regeneratively Grown", "NATIVA", "Naia Renew"; Eileen Fisher's RMS / RWS / RCS, "Recycled PA" and "Eco Vera"; and Tory Burch's "patent", "goat suede" and "moda acrylic" (read as modacrylic).
- **Typos filed by intent.** Brandy Melville has "cashmire", "poliamida", "a crylic" and "84.3%, acrylic". Altar'd State has "Model" and "Spamdex". Evereve has "Moda" and "Acylic".
- **Lining and trim lines after the shell.** Tory Burch's Patent Leather Skirt was first captured as its lining only, and its Corduroy Skirt as a marketing line. Both were re-read.
- **Sum limit raised from 101 to 102.** This keeps Reformation's Ines Top ("97% Polyester and 5% Spandex") whole. Re-running batch 01 under the new parser changes nothing.
- **Compositions that don't sum to 100 are filed as written** and flagged: Rally Point Plaid Top (90), Amanda Pointelle Tee ("305 Polyester"), Ines Top (102).
- **One composition contradicts its own page.** Michael Kors' Faux Fur Trim Wool Blend Coat is described as "Wool blend/faux fur", but its composition bullet reads "70% cotton/30% elastane". It is filed as written.

## Out of scope but noticed

- Lucky Brand product pages have no H1, so titles come from the URL slug (cased, otherwise as written).
- Eileen Fisher re-issues a garment under a new style number each season (e.g. Washable Flex Ponte Slim Pant F6TJX-P0696 and S5TJH-P0696). These are kept as separate styles.
