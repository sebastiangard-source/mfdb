# prices_womens_2026-10-13 — batch 9

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Simkhai | $125 / $245 / $325 | Accessible | complete |
| Sam Edelman | — | **`NC`: blocked** | see point 1 |
| Ulla Johnson | none / $250 / $470 | Accessible | complete |
| ERES | none / $445 / none | **hand-band** (swim and lingerie; resortwear reads True Luxury) | complete |
| prAna | — | **`NC`: blocked** | see point 1 |
| GUEST IN RESIDENCE | none / none / $225 | **hand-band** (knit house; proposed Accessible) | complete |
| Fleur Du Mal | $78 / $275 / $298 | **hand-band** (lingerie; rule reads Accessible) | complete |
| IRO | $165 / $345 / $345 | Accessible | complete |
| Agua Bendita | $120 / $130 / $170 | **hand-band** (swim; rule reads Accessible at exactly $150) | complete |
| Stella McCartney | $325 / $750 / $850 | True Luxury | complete |

## Where the brief would give a confident wrong answer

1. **Two sites block automated reading.** I don't get past bot checks, so both rows are `NC` and need a retry by hand:
   - **Sam Edelman:** every category page stayed on Cloudflare's "Performing security verification" screen.
   - **prAna:** the homepage loaded, then every category page returned "Access to this page has been denied".

   Sam Edelman is a shoe house and would hit the same shoe-rule gap as Steve Madden and UGG.
2. **Knit houses can't be read by the rule.** GUEST IN RESIDENCE's "shirts" are knitted cashmere (the product descriptions say so), and its one "tee" is a jersey sweater-tee. Tee and blouse are therefore `NONE`. On its $225 crewneck and $265 jeans I'd band it Accessible. This is the knit-house case the brief anticipates.
3. **More swim and lingerie brands.** I'd add ERES, Fleur du Mal and Agua Bendita to the hand-band list. Their ready-to-wear is a side line, priced here as the brief asks.
   - ERES's resortwear starts at $445, which is True Luxury territory, but it has no tee or sweater, so the rule cannot read.
   - Agua Bendita's mean is exactly $150, the Premium/Accessible line.
4. **Men's mixed into women's categories.** Agua Bendita's "Shirts" type holds men's shirts (19 of 50 tagged `men`). They were removed.
5. **Collaborations in the main range.** Stella McCartney sells a $1,690 signed Jeff Koons tee in its t-shirt grid. It was excluded. adidas by Stella McCartney is a separate line and was not read.

## How prices were read

| Site | Method |
|---|---|
| Simkhai, Ulla Johnson, GUEST IN RESIDENCE, Fleur Du Mal, Agua Bendita | Shopify `/products.json` feed, in stock only |
| ERES | resortwear grid, all 231 products |
| IRO | women's ready-to-wear listing (364 results) and shoes, from the server-rendered US pages. www.iroparis.com/us/ redirects to the French site, so the US category URLs were opened directly |
| Stella McCartney | server-rendered category listings (t-shirts 37, shirts-and-tops 86, knitwear 57, denim 34, pants 55, dresses 75, coats 28, shoes 130 tiles) |
| Sam Edelman, prAna | not read (bot protection) |

## Garment notes

- **No tee:** Ulla Johnson (its jersey tops are sleeveless), ERES (tees are loungewear) and GUEST IN RESIDENCE.
- **Sleeveless filter:** Ulla Johnson marks sleeveless styles `-sl-` in the product handle. Those were excluded from the blouse read, which raises its blouse entry from $170 to $250.
- **IRO** tiles carry no product names, so garments were read from product URLs.
- **Shoes without a flat or loafer:** IRO (slingbacks to boots) and ERES (shoes to mules), so both are `range`.
- **`NONE` because the brand doesn't sell it:**
  - Ulla Johnson: tee.
  - ERES: tee, sweater, jeans, outerwear.
  - GUEST IN RESIDENCE: tee, blouse, shoes.
  - Fleur Du Mal: jeans, shoes.
  - Agua Bendita: jeans, shoes.

## Files

- `return.csv`: 10 rows (Sam Edelman and prAna all `NC`)
