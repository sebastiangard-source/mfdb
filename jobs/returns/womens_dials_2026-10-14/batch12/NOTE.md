# Batch 12: womens_dials_2026-10-14, thread 3

Read on 14 October 2026 in Chrome, on each brand's own US store. There are 10 brand rows and 795 style rows. `reconcile.py` gives 10 exact matches, 0 to rewrite and 0 unmatched. No empty cells, and every enum is valid.

## What was checked

| brand | store / platform | styles (site) | sampled | with composition | status |
|---|---|---|---|---|---|
| ARGENT | Shopify | 348 | 80 | 79 | read |
| CAMI NYC | Shopify | 223 | 80 | 79 | read |
| Courrèges | /us · Next.js on Magento REST | 142 | 78 | 78 | read |
| Danielle Frankel | Shopify | 275 | 79 | 50 named, 0 with % | **partial** |
| HATCH Collection | Shopify | 250 | 78 | 73 | read |
| Joe's | Shopify | 289 | 80 | 79 | read |
| KALLMEYER | kallmeyer.nyc · Shopify | 184 | 80 | 79 | read |
| LESET | Shopify | 236 | 80 | 80 | read |
| Marina Rinaldi | us.marinarinaldi.com · Max Mara group | 516 | 80 | 76 | read |
| PatBO | Shopify | 386 | 80 | 70 | read |

Every house is a proportional stratified sample of 80, with the site total in `styles_total` and the basis in `sample_basis`. Three samples came out under 80 because a non-clothing item was drawn and dropped: Courrèges (slingbacks, a ring), Danielle Frankel ('Customization', a service) and HATCH (two sleepwear pieces).

## Headlines

- **Made-in-New-York and Made-in-LA houses:** KALLMEYER (50 of 80 New York) and LESET (53 of 80 Los Angeles). Danielle Frankel says made to order in the Garment District at its own atelier. PatBO places its making in its own Uberlândia atelier and embroidery school. Those last two are the only proposed craft 3s in the batch, and neither is shown with an address or photo.
- **Triacetate is a women's-map fibre.** Marina Rinaldi's cady family (71% triacetate, 29% polyester) and LESET's Barb, Ari and Arielle sets put 17 and 16 sampled styles on triacetate. It sits in the cellulosic bucket, which keeps both houses out of 'split'.
- **PatBO is the most synthetic house so far:** 60% synthetic-led, mostly polyester and polyamide knits and chiffons in dresses.
- **Named fabric families**, useful for a lines table: ARGENT's Seasonless Wool (30% of sample, sold on temperature regulation), Joe's Weightless, Comfort Stretch and Super Stretch denims, LESET's fabric sets, HATCH's Bodyflex, Softsculpt and Softest Rib, and Marina Rinaldi's Persona sub-line (34 of 80).

## What contradicted the record or the brief

1. **Danielle Frankel publishes no percentages.** Its spec table gives 'Fabric: Silk wool' and its descriptions name fibres, so those are filed as named-fibre compositions with the first-named fibre leading. "Silk wool" therefore files as silk, which makes fab_silk 5. The real blend is probably wool-majority, so **I'd hold fab_silk and fab_wool for this house.**
2. **Marina Rinaldi** composition comes from the PDP JSON-LD `material` field. It matched the rendered "Composition and care" block on the one page I checked by hand, but I validated 1 page, not the 10 the playbook asks for. "Made in Italy" appears only in the logo's title attribute, so made-in is 0% on product pages.
3. **Courrèges's** `_next/data` category route ignores `?page`, so I paged the store's Magento REST feed instead (36 per page). Composition and country of manufacture come from that feed; they matched the PDP Details tab on the one style opened. Every product states its country, across ten of them (Portugal and Madagascar lead).
4. **3.1 Phillip Lim-style hidden countries recur:** Joe's, CAMI NYC ('Imported' only) and Marina Rinaldi state no country on the page.
5. **Worklist rows to recheck:** PatBO `sweater_sold = no` matches the site, but its outerwear sits only inside Tops (3 jackets), so that link is a parent. Danielle Frankel's `shoes_sold = yes` is only the Birkenstock collaboration.
6. **House data that contradicts itself, filed as the composition states:** ARGENT has a "Seasonless Wool" dress whose fabric line says silk charmeuse, and a skirt titled viscose/polyester whose composition is 100% cotton. KALLMEYER has a polo titled "Cotton Wool" that is viscose/acrylic. CAMI NYC has a "Polyacetate" skirt whose percentages say viscose.

## Parser notes (carried into batch 11, whose figures did not change)

- `98%, Wool` (percent before the comma) and `38%%Polyester` normalised.
- `Tri-Acetate` read as triacetate.
- EU codes AC, PL, PA, EA, VI, PC handled. AC was read as acetate, which is a judgment call: it could be acrylic (KALLMEYER, one style).
- 'Apaca', 'Llama', 'Elite' (PBT), 'EME', 'Piolyamide', 'Naylon' and 'elastodiene' are mapped and noted in the style row. Decimal commas (PatBO's 95,5%) parse correctly.

## What the brief got wrong or left open

- Several houses have **no garment-level navigation** (Danielle Frankel sells everything under Bridal). There the link is the only stable listing that holds the garment, and `links_kind` says so.
- Maternity (HATCH) and plus-size (Marina Rinaldi) houses read the same way as the others. Whether the map wants them dialled alongside the others is a design call for the Spectrum thread.

## Not reached

- Courrèges's PDP "Traceability" tab rendered empty. It may hold supplier data worth a second look.
- No current craft scores are in the worklist, so there is no moves table.
