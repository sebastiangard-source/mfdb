# prices_womens_2026-10-13 — batch 12

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| SACHIN BABI | none / $395 / $465 | True Luxury (gown house; hand-band check) | complete |
| SILVIA TCHERASSI | none / $590 / none | **hand-band** (rule can't read; blouse reads True Luxury) | complete |
| Tanya Taylor | $225 / $295 / $395 | Accessible | complete |
| ARGENT | $75 / $225 / $350 | Accessible | complete |
| CAMI NYC | $185 / $275 / $245 | Accessible | own label only |
| HATCH Collection | $68 / $128 / $268 | Accessible (maternity; hand-band check) | complete |
| SIMONMILLER | $165 / $245 / $295 | Accessible | complete |
| Diane von Furstenberg | $198 / $358 / $328 | Accessible | own label only |
| Elie Saab | none / $1,200 / $1,550 | True Luxury | ready-to-wear only |
| Extreme Cashmere | $475 / none / $400 | **hand-band** (knit house) | complete |

## Where the brief would give a confident wrong answer

1. **Evening and gown houses.** These need hand-band checks like Rene Ruiz in batch 8:
   - **Sachin & Babi:** gowns are 234 of 495 in-stock products.
   - **Silvia Tcherassi:** 27 "atelier" evening dresses ($4,500–6,500).
   - **Elie Saab:** most dresses are long gowns, plus Haute Couture (408) and Bridal (93) on the same feed.

   All of these were excluded from the day-dress range. Silvia Tcherassi has no cotton tee or sweater, so the rule can't read.
2. **Placeholder products.** Elie Saab's feed holds 618 untyped "Look NN" products at $9,999. Left in, they would set every high.
3. **EUR by default.** Extreme Cashmere prices in EUR and has no US subfolder. I set the store's own country selector to United States, which reprices in USD (e.g. EUR 1,450 → USD 1,600), and read the feed after that.
4. **Stocked brands, resale and collaborations on own sites:**
   - DVF: Trove resale and stocked LGR and lablpx.
   - CAMI NYC: "3rd Party" brands.
   - ARGENT: AGOLDE x Argent jeans.
   - HATCH: Janie and Jack and Solly Baby collaborations.
   - Tanya Taylor: a unisex "Creative Club" capsule tee ($95), which would otherwise be the tee low.

   All were excluded.
5. **Cotton-only tee rule at a knit house.** Extreme Cashmere's tees are cashmere from $245. Only its cotton-cashmere tees ($475–500) were used, and their cotton share isn't stated. This is the same issue as Gabriela Hearst in batch 10.
6. **Maternity.** HATCH is cut entirely for pregnancy and nursing, so all its trousers are pull-on. Maternity isn't one of the brief's specialty categories, but it may want hand-banding.

## How prices were read

| Site | Method |
|---|---|
| All ten | Shopify `/products.json` feed, in stock only |
| Silvia Tcherassi, Tanya Taylor | plus product descriptions to classify fabric and sleeves |
| DVF | fabric read from product tags |
| Extreme Cashmere | feed read after switching the store country to US |

## Garment notes

- **Sweater with no plain crewneck:** DVF's lowest crew is $498, so the $328 cotton-knit Annie Sweater was used.
- **Single styles:**
  - Tee: Tanya Taylor, SIMONMILLER, DVF.
  - Sweater: HATCH.
  - Jeans: CAMI NYC, SIMONMILLER, Tanya Taylor, DVF, HATCH.
  - Shoes: Elie Saab (ballerina).
- **Outerwear:** SIMONMILLER's $795 Jetz coat is faux shearling and was left out to be safe. If faux counts, it is the high.
- **Shoes without a flat or loafer:** Sachin & Babi (pumps) and Silvia Tcherassi (sandals), so both are `range`.
- **`NONE` because the brand doesn't sell it:**
  - Sachin & Babi: tee, jeans.
  - Silvia Tcherassi: tee, sweater, jeans.
  - Tanya Taylor: shoes.
  - ARGENT: shoes.
  - CAMI NYC: shoes.
  - HATCH: shoes.
  - DVF: shoes.
  - Elie Saab: tee.
  - Extreme Cashmere: blouse, jeans, shoes.

## Files

- `return.csv`: 10 rows
