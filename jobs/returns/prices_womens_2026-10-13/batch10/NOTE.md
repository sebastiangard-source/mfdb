# prices_womens_2026-10-13 — batch 10

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Cozy Earth | $48 / none / none | **hand-band** (bedding and lounge) | complete |
| Jockey | $24 / none / none | **hand-band** (underwear, named in brief) | complete |
| Pucci | $1,215 / $1,025 / $1,900 | True Luxury | complete |
| Favorite Daughter | $78 / $178 / $178 | Accessible | own label only |
| HANRO | $110 / none / none | **hand-band** (underwear and sleepwear) | tee only |
| La DoubleJ | $270 / $620 / $470 | True Luxury | complete |
| O'Neill | $28.99 / $58 / $64 | Basic by the rule; hand-band check (surf) | complete |
| Adam Lippes | none / $690 / $690 | True Luxury | complete |
| GABRIELA HEARST | none / $750 / $690 | True Luxury | complete |
| Guizio | $48 / $128 / $128 | Premium | complete |

## Where the brief would give a confident wrong answer

1. **Kids' lines inside the main feed.** Pucci Junior (119 products) shares Pucci's product types. Left in, Pucci's tee entry would read $120 and its blouse $250, instead of $1,215 and $1,025. These were removed by the `junior kids` tag.
2. **Brands with no cotton tee.** Every Gabriela Hearst "T-shirt" is a cashmere, silk-hemp or merino knit ($690–1,990), and Adam Lippes sells none. Tee is `NONE` for both. The brief defines the tee as cotton or cotton-blend. If a cashmere tee should count, Gabriela Hearst's tee entry is $690.
3. **More hand-band brands:**
   - Cozy Earth and HANRO are lounge and sleep brands. Only HANRO's cotton tee qualifies; the rest of its range is sleep and lounge.
   - Jockey is named in the brief.
   - O'Neill is a surf brand that passes the Basic test on a $28.99 graphic tee.
4. **Placeholder products in the feed.** Gabriela Hearst's feed holds 1,453 "Lookbook" placeholder products plus a menswear line. Both were excluded before reading.
5. **Exotic skins and embellished pieces at the top end.** Excluded from highs:
   - Gabriela Hearst: a $27,990 snakeskin biker jacket, embroidered tops to $15,500, and crochet-star knits to $13,750.

   Kept as the dearest regular pieces, but possibly runway (worth a check):
   - Adam Lippes's $11,900 beaded-tulle dress.
   - Gabriela Hearst's fringe suede trench ($15,000 in black; a second colour lists at $25,000).

## How prices were read

| Site | Method |
|---|---|
| Cozy Earth, Favorite Daughter, HANRO, O'Neill, Adam Lippes, Gabriela Hearst, Guizio | Shopify `/products.json` feed, in stock only |
| Pucci | Shopify feed on the /en-us market, with USD checked against product pages |
| La DoubleJ | server-rendered category pages, read page by page. Dresses read 240 products over 12 pages, which may be capped |
| Jockey | women's activewear and lifestyle catalog page (48 products) |

## Garment notes

- **Favorite Daughter:** "Logo Shop" merch, the "Nobody Wants This" TV collaboration and the National Daughters Day capsule were excluded, as were "boyfriend" (blazer-type) jackets.
- **La DoubleJ:** two jeans that look like a denim-brand collaboration ($328–368) were excluded.
- **Single or same-price ranges:**
  - O'Neill's two woven shirts are both $58.
  - Pucci's cotton tees are all $1,215.
  - Cozy Earth has one jacket, so it's `single`.
- **`NONE` because the brand doesn't sell it:**
  - Cozy Earth: blouse, sweater, jeans, shoes.
  - Jockey: blouse, sweater, jeans, outerwear, shoes.
  - HANRO: everything but the tee.
  - O'Neill: jeans, shoes.
  - Adam Lippes and Gabriela Hearst: tee.

## Files

- `return.csv`: 10 rows
