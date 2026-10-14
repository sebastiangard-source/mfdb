# prices_womens_2026-10-13 — batch 6

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| TWP | $150 / $375 / $395 | Accessible (mean $385, near the $400 cut) | complete |
| Wolford | $235 / $255 / $295 | **hand-band** (rule reads Accessible) | complete |
| Chloé | $550 / $1,190 / $890 | True Luxury | complete |
| UGG® | $52 / $138 / $118 | **Premium by the shoe-house rule; see point 1** | complete |
| Varley | $60 / none / $99 | **hand-band** (activewear, named in brief) | complete |
| ba&sh | $95 / $235 / $260 | Accessible | complete |
| Akris | $835 / $595 / $695 | True Luxury | complete |
| La Ligne | $95 / $195 / $195 | Accessible | complete |
| Nili Lotan | $165 / $250 / $420 | Accessible | own women's line only |
| DÔEN | $128 / $158 / $258 | Accessible | complete |

## Where the brief would give a confident wrong answer

1. **The shoe-house rule, again.** UGG bands on its flat ($135 Zora Ballet Flat), which reads Premium on the mean cuts. Its apparel would also read Premium. This is the same gap as Steve Madden in batch 3: the shoe rule has no Basic cut. UGG's cheapest moccasins ($120–140) are filed as slippers, and a $300 UGG x JW Anderson loafer is a collaboration. Both were excluded.
2. **Women's and men's on one site.** Nili Lotan sells a men's line through the same store, tagged only by collection (`mens-*`, `all men's`). Those products were removed by their tags. A feed read without that filter would mix men's shirts and sweaters into the women's ranges.
3. **Kids' products inside women's categories.** La Ligne's knitwear feed carries $75 kids' Marini sweaters. They are tagged `kids` but have the same product type as the women's knits. Left in, La Ligne's sweater entry would read $75 instead of $195.
4. **Limited lines that look like the main range:**
   - DÔEN's "Heirloom" hand-crochet and embroidered tops ($528–598) and its $2,998 Anniversary dress.
   - ba&sh's "Wellness Collection" (a $215 jacket and a $285 dress).

   All were excluded as capsules. ba&sh's dress and outerwear lows would otherwise drop.
5. **Some sites hide their product feed.** Varley and La Ligne run headless storefronts that refuse `/products.json`. Their Shopify store domains (`vvarley.myshopify.com`, `lalignenyc.myshopify.com`) still serve it. That is the same catalogue, priced in USD (checked on a Varley product page).

## How prices were read

| Site | Method |
|---|---|
| TWP, Akris, Nili Lotan, DÔEN | Shopify `/products.json` feed, in stock only |
| Varley, La Ligne | the same feed from the brand's `*.myshopify.com` domain |
| Chloé | category grids scrolled to load (blouses 38, knitwear 49, pants 65, dresses 64, coats 62, shoes 168 products) |
| Wolford | ready-to-wear clothing grid, all 150 items |
| UGG | default category grids. A large `?sz=` listing returned "Access Denied", so it was not retried that way |
| ba&sh | category grids, `?sz=300` |

## Garment notes

- **Blouse:**
  - Chloé's "blouses" grid is all tops (ruffle and silk tops); none is named a shirt.
  - DÔEN names one blouse (The Jane Blouse, $158), so it's `single`. Its other woven pieces are "Tops", often sleeveless.
  - Varley has no woven shirt, so `NONE`.
  - Wolford's and UGG's single shirts were not checked for fabric.
- **Tee:** Chloé and Akris tees are expensive.
  - Every Chloé tee carries the logo, and they start at $550.
  - Akris's cotton tees are all $835.
  - Nili Lotan's $150 Muscle Tee is sleeveless and excluded.
- **Outerwear:** Wolford's only jacket is a tailored "Scuba Tailor Jacket", blazer-type, so `NONE`.
- **`NONE` because the brand doesn't sell it:**
  - Wolford: jeans, outerwear, shoes.
  - UGG: jeans.
  - Varley: blouse, jeans.
  - Akris: shoes.
  - La Ligne: shoes (one collaboration slipper only).

## Files

- `return.csv`: 10 rows
