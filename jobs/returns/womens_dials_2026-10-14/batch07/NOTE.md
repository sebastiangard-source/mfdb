# Batch 07 — womens_dials_2026-10-14, thread 2

Read 14 October 2026 in Chrome on each brand's own US store. 10 brands: 9 `read`, 1 `partial` (Carolina Herrera, fibre coverage). `reconcile.py`: 10 exact, 0 rewrites, 0 unmatched. Same method as batch 06 (see that NOTE); percentages are of the sampled styles, `fab_*` of sampled styles with a composition.

## What was read

| brand | channel | styles (census) | sampled | with composition |
|---|---|---|---|---|
| FARM Rio | Shopify feed + PDP `.composition-content` | 1,089 | 80 | 67 |
| Nili Lotan | Shopify feed + PDP accordion | 394 (275 typed + 119 untyped) | 80 | 80 |
| A.L.C. | Shopify feed + PDP detail bullets | 340 | 80 | 80 |
| Cult Gaia | Shopify feed + 'Composition and Care' accordion | 504 | 80 | 73 |
| Frances Valentine | Shopify feed descriptions | 89 | 80 | 74 |
| L'AGENCE | Shopify feed + PDP 'Composition' list | 728 | 80 | 79 |
| Alexander Wang | women's collection feed + 'materials & care' metafield | 206 | 80 | 80 |
| Camilla | Shopify feed descriptions (US store) | 2,037 | 80 | 58 |
| Carolina Herrera | Next.js PLP `?pageSize=400` + PDP text | 287 | 80 | **27** |
| Eberjey | Shopify feed + 'Fabric & Care' metafield | 170 | 75 | 71 |

## Headlines

- **Silk houses:** Camilla (silk leads the disclosed sample; prints on silk dresses, kaftans, pants), Eberjey's Washable Silk line (100% silk) beside its Gisele line (95% TENCEL™ Modal — wholly cellulosic), Carolina Herrera's disclosed evening pieces.
- **Natural-led tailoring and knits:** Nili Lotan (96% natural — cashmere, silk, cotton, wool, leather), Alexander Wang (wool knits and cotton denim, though partly coded as `woa/pa/ea`).
- **Mixed, polyester-heavy:** Frances Valentine (`split` — polyester 'poly-dupioni' dresses and faux fur against Peru Pima knits), L'AGENCE (silk blouses and cotton denim vs polyester sequins, PU 'vegan leather', nylon lace), Cult Gaia (viscose/nylon knit dresses, polyester gowns vs silk and linen).
- **FARM Rio:** rayon/viscose prints and linen-viscose; knit cardigans acrylic-led.
- **Tech:** no brand in this batch has a named technical fabric. 2 where stretch is claimed without one (A.L.C., Frances Valentine, L'AGENCE, Alexander Wang).
- **Craft:** none above 2. Country-on-page is the common 2 (Frances Valentine 60%, Carolina Herrera 74%, L'AGENCE 'Made in Los Angeles' on denim, Nili Lotan 'crafted in the USA from Japanese denim'). FARM Rio publishes its Tier 1 suppliers on Open Supply Hub — **a 3 if a published supplier list counts as naming makers; please rule.** Camilla claims hand-cut, hand-sewn, in-house prints without a place.

## Not reached / partial

- **Carolina Herrera:** only current-season (Fall 2026) product pages state a composition; Pre-Fall, Resort and icon pages show SKU and fit notes only. 53 of 80 undisclosed → `partial`. No house/heritage page on the US site.
- **Camilla:** 22 of 80 older styles carry no fibre line. The feed keeps years of past prints live (2,037 styles) — the census overstates what is on sale.
- **Heritage `NC`:** A.L.C., Cult Gaia, Alexander Wang, Carolina Herrera (about pages empty or absent).

## Contradicts the record / for the map

- **Links that had to be parents** (no garment page exists): FARM Rio tee → Tops, jeans → Denim (jackets mixed in); Frances Valentine tee and blouse → Tops, jeans → Pants; Camilla tee/blouse → RTW Tops, trousers → RTW Bottoms; Carolina Herrera jeans → Pants; Eberjey every garment → Loungewear or Pajamas.
- Alexander Wang's nav 'Outerwear' page shows a men's puffer in the first rows; 'Jackets' used instead.
- Nili Lotan sells men's in the same feed (97 products, excluded on their tags) and has 119 women's products with no product type.

## What the brief got wrong (adds to batch 06's list)

1. **Eberjey is a sleepwear house** — most of its range is PJ sets. In scope by the letter of the brief (not lingerie, not swim), but a sleep set has no place in the eight-garment link scheme or the category enum (filed `other`). Same question coming for HANRO and Jockey in batch 10.
2. **Compositions in EU codes** (`bd 100.0%: 57.0%woa/37.0%pa/6.0%ea` at Alexander Wang) and **cloth names in place of fibres** ('100% CHINTZ PLISSÉ', '100% dupioni', 'poly-dupioni') need a ruling list; I read codes per rules_fibre and filed bare cloth names as undisclosed.
3. **TENCEL™ Modal** is modal, not lyocell — worth stating in the fibre table, since the word TENCEL alone would file it as lyocell.
