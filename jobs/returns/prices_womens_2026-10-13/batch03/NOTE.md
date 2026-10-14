# prices_womens_2026-10-13 — batch 3

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Veronica Beard | $138 / $248 / $298 | Accessible | complete |
| Steve Madden | none / none / $69 (shoes $50) | **Premium by the shoe rule; see point 2** | complete |
| GUESS | $29 / $69 / $69 | **Basic; see point 1** | complete |
| Kate Spade New York | $78 / $178 / $178 | Accessible | partial grids (dresses, shoes) |
| Alice + Olivia | $135 / $195 / $295 | Accessible | complete |
| Zimmermann | $225 / $525 / $675 | True Luxury | complete |
| Marc Jacobs | $98 / $298 / $358 | Accessible | partial grid (44 of 79) |
| Jenni Kayne | $95 / $265 / $225 | Accessible | own label only |
| LoveShackFancy | $95 / $225 / $185 | Accessible | complete |
| SKIMS | $48 / $78 / $88 | **hand-band (rule reads Premium)** | complete |

## Where the brief would give a confident wrong answer

1. **GUESS reads Basic only once Marciano is taken out.** Marciano is GUESS's sister banner, with its own stores, and its pieces sit inside GUESS's own category pages. They were excluded by style code (GUESS W…/V…, Marciano G…/digits). Left in, Marciano would set the sweater high at $160 and the blouse high at $200. GUESS's entry pieces ($29 tee, $69 woven shirt) pass the Basic test.
2. **The shoe-house rule has no Basic cut.** The brief says a shoe house bands "on its shoe entry on the same cuts", but the Basic cut is defined by tee and blouse. On the mean cuts, Steve Madden's $49.95 flat reads Premium, which overstates a mall shoe brand. I'd hand-band it. The rule needs a shoe-entry Basic cut before the remaining shoe houses come up.
3. **SKIMS is an intimates and lounge house.** It sells one woven shirt ($78 poplin) and a few woven pants, so the rule reads Premium on very few pieces. Hand-banding is recommended, as for Soma and Aerie in batch 1. NikeSKIMS and Ludovic de Saint Sernin x SKIMS are collaborations and were excluded throughout.
4. **Some brands have no plain tee.** Every Marc Jacobs tee carries the logo, and Kate Spade's only tees are a small-logo tee and a novelty tee. Logo tees were used and flagged in `note`. A tee entry of "plain cotton tee" cannot be met at these brands.
5. **Lifestyle stores hide stocked brands.** Jenni Kayne's jeans are all stocked AGOLDE and RE/DONE, so jeans = `NONE`. LoveShackFancy's shoes are all stocked (Birkenstock, Loeffler Randall) or collaborations, so shoes = `NONE`. Own label was isolated by the Shopify `vendor` field.

## How prices were read

| Site | Method |
|---|---|
| Veronica Beard, Steve Madden, Jenni Kayne, LoveShackFancy | Shopify `/products.json` feed (vendor, product_type, compare_at) |
| Alice + Olivia | Shopify per-collection feeds; the full feed holds about 1,800 legacy products |
| GUESS, Kate Spade, Marc Jacobs | category grids, single-product tiles only |
| Zimmermann | Magento grid, 96 per page; Runway-badged pieces skipped |
| SKIMS | collection grids (headless store, no product feed) |

## Coverage limits (also in each row's `note`)

- **Kate Spade:** only 16 priced tiles render per page. Dresses read 16 of 34, shoes 16 of 27.
- **Marc Jacobs:** the view-all grid rendered 44 of 79 products, so highs for tops, dresses and outerwear may be understated.
- **Steve Madden:** the Natan loafer high ($139.95) skips a same-price "Red Crocodile" finish as a possible exotic.
- **SKIMS:** the elevated-fibre Airy Cashmere Turtleneck ($168) was not checked for majority cashmere; the sweater high is a $178 tweed turtleneck.

## Other notes

- **`NONE` because the brand doesn't sell it:**
  - Steve Madden: tee, blouse.
  - Jenni Kayne: jeans.
  - Alice + Olivia: shoes.
  - LoveShackFancy: shoes.
  - SKIMS: jeans.
- **Collaborations excluded:** Veronica Beard x High Line; Alice + Olivia x Coniglio and Guns N' Roses tees; LoveShackFancy x PINK, x Wrangler and capsules; NikeSKIMS; Ludovic de Saint Sernin x SKIMS.

## Files

- `return.csv`: 10 rows
