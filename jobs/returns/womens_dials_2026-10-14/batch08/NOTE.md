# Batch 08 — womens_dials_2026-10-14, thread 2

Read 14 October 2026 in Chrome, on each brand's own US store. 10 brands, all `read` (Gianvito Rossi: craft and links only — no clothing). 714 style rows. `reconcile.py`: 10 exact, 0 rewrites, 0 unmatched. Method as in batch 06; percentages are of sampled styles, `fab_*` of sampled styles with a composition.

## What was read

| brand | channel | styles (census) | sampled | with composition |
|---|---|---|---|---|
| Lela Rose | Shopify feed descriptions | 242 | 80 | 55 |
| Gianvito Rossi | SFCC (shoes only) | — | — | NONE |
| Khaite | Shopify feed + PDP 'Material' | 219 | 80 | 79 |
| M.M.LaFleur | Shopify feed + PDP care list | 977 | 75 | 73 |
| Oscar de la Renta | Shopify feed + 'Materials & Care' | 396 | 80 | 80 |
| Re/Done | women's collection feed + PDP 'Content:' | 233 | 80 | 73 |
| Rene Ruiz | Shopify feed (PDP text is the feed text) | 487 | 81 | **0** |
| Still Here | Shopify feed descriptions | 75 | 75 (census) | 71 |
| TOTEME | RTW collection feed + PDP details, 'Made in', 'Manufacturer' | 384 | 83 | 83 |
| ViX Paula Hermanny | Shopify feed + PDP 'Material' tab | 522 (clothing only) | 80 | 55 |

## Headlines

- **TOTEME is the strongest making disclosure in thread 2 so far:** every product page names the garment maker, the country of make, and where the cloth was woven/knit and dyed. 71 of 83 sampled pages name a manufacturer (Texmade and Confetil in Portugal, Simiz in Romania, Mergü and Orjin Deri in Turkey, Zhejiang Langyi in China), 59 a country. The suppliers are also on Open Supply Hub, with Fair Wear audits. **Proposed craft 3**: the makers are third parties and nothing is owned. Fibre is natural-led (wool, organic cotton, silk, linen, leather), with viscose leading the jersey and fluid pieces (29%).
- **Denim houses, all-cotton:**
  - Still Here: rigid 100% cotton on all 13 jean fits; 92% natural, 0% synthetic-led.
  - Re/Done: 81% natural; upcycled vintage Levi's beside a new-make range.
  - Neither says where its jeans are made. Still Here → 1. Re/Done → 2, for the documented upcycling: "over 200,000 pairs" reconstructed.
- **Work-wear stretch:** M.M.LaFleur (OrigamiTech, WonderTex, PowerStretch and others — tech 3). It names sixteen factories with city and founding year, but no product page ties a style to a maker → craft 3.
- **Evening houses:**
  - Oscar de la Renta splits day (cotton, wool, silk) from evening (polyamide tulle, polyester faille).
  - Lela Rose is US-made on 64% of pages (craft 2).
  - Rene Ruiz discloses no fibre at all (below).
- **ViX Paula Hermanny:** its resort RTW range (522 styles) was read; swim and cover-ups were excluded.
  - Fibre splits two ways: linen, cotton, rayon and silk on one side; polyamide/elastane "Brazilian Lycra" and polyester mesh on the other (`split`).
  - 50 of 80 sampled pages say "Made in Brazil".
  - Casa ViX in Petrópolis trains seamstresses "certified to work at ViX", which implies in-house sewing → craft 3. Make it 2 if in-house making that is only implied should not count.

## Not reached / partial

- **Rene Ruiz:** only 1 of 758 products states a fibre (a gown, 100% polyester). Every other page names only the cloth: brocade, crepe, mikado, organza, sequin, tulle, fil coupé. All 81 sampled styles are `ND`. `fab_*`, shape and the class percentages are filed as `ND`, not 1 or 0, because a 1 would assert absence.
- **Heritage `NC`:** Still Here (no date or story), Khaite and Lela Rose (about pages returned no text).
- **ViX:** 21 of 80 sampled pages, mostly final-sale prints, have no composition.

## Contradicts the record / for the map

- **ViX sells sweaters.** The worklist says not sold, but the store has a "Sweaters" page with 11 knit cardigans. I filed the link and did not write NONE. `assemble` flags the conflict on purpose.
- **ViX pages contradict themselves:**
  - Tuca dress: copy says "viscose and elastane", composition line says 93% polyester 7% elastane.
  - Clarissa dress: tab is titled "Rayon", line says 85% polyamide 15% elastane.
  - Composition line filed in both cases.
- **Parent links:**
  - Re/Done: blouse → Tops, trousers → Bottoms, shoes → Shoes x Accessories.
  - Rene Ruiz: blouse and trousers share "Suiting, Tops, Pants & Jumpsuits"; outerwear → Wraps & Boleros (shawls, typed Accessory).
  - Still Here: tee and blouse → Tops; trousers and dress → Shop All (no page of their own).
  - TOTEME: tee → Tops.
- **Store mixes:**
  - Re/Done mixes vintage resale and third-party upcycled goods into its feed; totes excluded.
  - Rene Ruiz sells shapewear inside its clothing types; excluded.

## What the brief got wrong (adds to batches 06–07)

1. **"Cloth named, fibre not" needs a rule.** Rene Ruiz is the clearest case. I filed cloth names (brocade, mikado, faille, scuba, "metallic tulle") as undisclosed. I also fixed the parser so that "metallic" without a percentage is no longer read as a metal fibre.
2. **Swim houses that also run real RTW** (ViX, likely Agua Bendita and ERES in batches 09–10): the brief's exclusion of swim leaves a large in-scope range. I read that range rather than returning NONE. Cover-ups (sarongs, caftans, pareos) were treated as swim. Please confirm.
3. **Supplier transparency is not graded by the craft rubric.** TOTEME names a maker per product; M.M.LaFleur names its factories; FARM Rio (batch 07) lists suppliers on Open Supply Hub. The rubric rewards *owning* the making. Naming third-party makers lands at 3 at best, however complete the disclosure. That may be what you want, but it should be explicit.

## Method notes

- Parser fixes this batch (re-ran batches 06 and 07; outputs unchanged):
  - "lin" (French linen) now matches only as a whole word — "poplin" no longer reads as linen.
  - Finish words (metallic) are ignored when no percentages are given.
- Still Here is a census: 75 styles, all read. The leather and suede versions of the Cool and Sport jeans are kept as their own styles.
- TOTEME presents prices in USD over an SEK base (`Shopify.currency.rate` 0.102); prices were not used.
