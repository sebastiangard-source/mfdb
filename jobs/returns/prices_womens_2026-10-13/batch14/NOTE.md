# prices_womens_2026-10-13 — batch 14

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Another Tomorrow | $130 / $390 / $450 | True Luxury (mean $420, near the cut) | new stock only |
| EB Denim | $115 / $295 / $225 | Accessible | complete |
| R13 | $295 / $345 / $595 | True Luxury | complete |
| Róhe | $210 / $490 / $590 | True Luxury | US store |
| Toccin | $345 / $325 / $295 | Accessible | complete |
| Amsale | none / none / none | **hand-band** (bridal and occasionwear only) | complete |
| Cara Cara | none / $345 / $395 | Accessible | complete |
| CO | $150 / $495 / $495 | True Luxury | complete |
| Elan | none / $74 / $74 | Premium (near Basic; hand check) | complete |
| Generation Love | none / $175 / $225 | Accessible | women's only |

## Where the brief would give a confident wrong answer

1. **Amsale sells nothing in scope.** It sells bridal gowns, bridesmaid and evening dresses, Little White Dresses, toppers and veils, so all eight garments are `NONE`. The feed's 7,480 products are mostly colour variants of bridesmaid dresses. The row needs a hand band.
2. **Elan sits near the Basic line.** Its blouse and sweater are both $74, but it sells no tee, so the Basic test fails by default. If one of its knit tops is treated as the tee, it could read Basic.
3. **Róhe has a separate US store.** roheframes.com prices in EUR (Netherlands). Its en-US link points to us.roheframes.com/en-us, which prices in USD and was used.
4. **Resale and kids' items in the main feed:**
   - Another Tomorrow sells its own pre-owned line ("AT Authenticated Resale", 108 items) alongside new stock.
   - Generation Love mixes in girls' mini-me dresses.

   Both were excluded.
5. **Shoes that are only a collaboration.** Toccin's only shoes are Toccin x Canfora Capri sandals, so shoes are `NONE` for its own label.
6. **Fur, shearling and hair-on leather excluded from outerwear highs:**
   - Cara Cara: pony-hair and shearling jackets ($2,495–3,295).
   - Róhe: a pony-hair coat ($3,190).

## How prices were read

| Site | Method |
|---|---|
| All ten | Shopify `/products.json` feed, in stock only |
| Cara Cara, CO, Elan | plus product descriptions to check sleeves and fabric |

## Garment notes

- **Tee:**
  - R13 has one short-sleeve tee in stock. Its "Relaxed Cashmere V-Neck" is a short-sleeve knit tee and was not used as the sweater.
  - Toccin's only tee is a knit (fibre not stated).
  - No tee at Cara Cara, Elan or Generation Love.
- **Sweater with no plain crewneck:** CO's lowest pullover is a $495 silk-linen v-neck.
- **Trousers:** EB Denim has only a pull-on pant and a suede bootcut (`range`, flagged).
- **Shoes:** Generation Love's only shoe is a $85 faux-fur house slipper, recorded as `single`.
- **`NONE` because the brand doesn't sell it:**
  - Another Tomorrow: shoes.
  - EB Denim: shoes.
  - Róhe: shoes.
  - Toccin: shoes (own label).
  - Amsale: all eight.
  - Cara Cara: tee, jeans, shoes.
  - Elan: tee, shoes.
  - Generation Love: tee.

## Files

- `return.csv`: 10 rows
