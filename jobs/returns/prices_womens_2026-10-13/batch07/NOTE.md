# prices_womens_2026-10-13 — batch 7

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| FARM Rio | $75 / $120 / $198 | Accessible (mean $159, just over the cut) | complete |
| A.L.C. | $110 / $350 / $495 | **True Luxury, borderline; see point 1** | complete |
| L'AGENCE | $100 / $275 / $325 | Accessible | full-price vendor only |
| Cult Gaia | none / none / $398 | **hand-band; proposed Accessible** | complete |
| Frances Valentine | $122 / $198 / $198 | Accessible | own label only |
| Camilla | $239 / $529 / $599 | True Luxury | complete |
| Carolina Herrera | none / $590 / $790 | True Luxury | complete |
| Eberjey | $68 / $128 / $148 | **hand-band** (sleepwear, named in brief) | complete |
| Lela Rose | none / $350 / $450 | **Accessible at exactly $400; see point 1** | complete |
| Alexander Wang | $175 / $375 / $295 | Accessible | women's collections only |

## Where the brief would give a confident wrong answer

1. **Two brands sit on the $400 line.**
   - **A.L.C.:** on its crewneck staple (Teddy Crew, $495) the mean is $422.50, which reads True Luxury. On its cheapest pullover (a $425 merino v-neck) the mean is $387.50, which reads Accessible. The row follows the brief's "crewneck pullover is the staple" and uses $495.
   - **Lela Rose:** the mean is exactly $400. "Over $400" is True Luxury, so this reads Accessible.
   - Both should be confirmed by hand. Throughout the job I have usually taken the cheapest pullover as the sweater entry where no plain crewneck exists. A.L.C. is the first brand where that choice changes the band.
2. **No tee and no blouse.** Cult Gaia sells neither (its tops are knit or sculptural), so the rule cannot read. On its other entry points (sweaters $398, dresses $328, jeans $398) I'd band it Accessible. Carolina Herrera has no tee, but its blouse and sweater give a clear True Luxury.
3. **Sale stock in a separate vendor.** L'AGENCE lists 649 of 1,829 products under a separate "L'AGENCE Sale" vendor. Only full-price "L'AGENCE" products were read. A plain feed read would mix the two.
4. **Runway pieces aren't labelled.** Carolina Herrera's coats run to $15,990 (gold-embroidered, organza and sequin pieces). These look like runway looks but are not marked as such. The outerwear high was held at a $3,790 jacquard cocoon coat.
   - The dress high ($10,990 embroidered organza) was kept, because the brief prices the dearest regular dress. It may also be a runway look and should be checked.
5. **More collaborations inside the main feed:**
   - FARM Rio: adidas, Havaianas flip-flops, Stanley, Ana Leovy.
   - Carolina Herrera x Miron Crosby boots ($2,295).

   All were excluded.

## How prices were read

| Site | Method |
|---|---|
| FARM Rio, A.L.C., L'AGENCE, Cult Gaia, Frances Valentine, Camilla, Eberjey, Lela Rose | Shopify `/products.json` feed, in stock only |
| Alexander Wang | Shopify per-collection feeds for the women's categories (the site also sells men's) |
| Carolina Herrera | category grids, clicking "View 20 more" until done. Tops 74, knitwear 34, pants 30, coats 30, dresses 120 and shoes 29 products; 18 shoes carried a price |

## Garment notes

- **Tee:**
  - Camilla tees are printed silk or jersey from $239.
  - Every Alexander Wang tee carries a logo or crystals.
  - Frances Valentine sells one short-sleeve tee, so it's `single`.
- **Blouse:**
  - FARM Rio's tulle, jersey and sleeveless "blouses" ($80–120) were excluded, leaving woven blouses from $120.
  - Eberjey has one woven button-front top, so it's `single`.
- **Jeans:**
  - FARM Rio and Carolina Herrera file jeans as denim "pants".
  - Carolina Herrera has one denim style, so it's `single`.
  - Lela Rose sells denim skirts and jackets but no jean, so `NONE`.
- **Shoes:**
  - No flat or loafer at Camilla (printed thongs to boots) or Alexander Wang (kitten mule to boots), so both are `range`.
  - Lela Rose's three shoe listings are all sold out, so `NONE`.
- **`NONE` because the brand doesn't sell it:**
  - Cult Gaia: tee, blouse.
  - Carolina Herrera: tee.
  - Lela Rose: tee, jeans, shoes.
  - Eberjey: jeans, outerwear, shoes.
  - A.L.C.: shoes.

## Files

- `return.csv`: 10 rows
