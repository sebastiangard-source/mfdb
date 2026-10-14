# prices_womens_2026-10-13 — batch 1 (all 10 brands)

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched.** A validator found no empty cells. Every priced figure has a product name and a URL, and no low is above its high.

## Result

| Brand | Status | Tee / blouse / sweater entry | Proposed band |
|---|---|---|---|
| Chico's | complete | $46 / $90 / $80 | Premium |
| LOFT | **blocked, all `NC`** | — | — |
| Talbots | complete | $40 / $80* / $90 | Premium |
| White House Black Market | complete | $40 / $79 / $89 | Premium |
| J.Jill | complete | $39 / $79 / $89 | Premium |
| Soma | complete | $45 / $79 / $99 | hand-band (intimates) |
| Athleta | complete | $45 / $99 / $129 | hand-band (activewear) |
| Anthropologie | complete, own labels only | $38 / $98 / $98 | Premium |
| Aerie | complete | $25 / $50 / $60 | Basic by the rule; hand-band check |
| Free People | complete, own labels only | $38 / $78 / $78 | Premium |

\* Talbots' exact blouse entry is $79.50. See point 1 below.

**LOFT is blocked.** Every page redirects to a PerimeterX "Press & Hold — verify you are a human" check. I don't complete bot checks. Ann Taylor runs on the same platform and will likely block the same way.

## How prices were read

Each brand's own full category listing was loaded, then filtered to the garment definition. PDPs were opened to confirm fabric, sleeve or maker.

How each site was loaded:

| Site | Method |
|---|---|
| Chico's, WHBM, Soma | infinite scroll |
| Talbots | `?sz=300` |
| J.Jill | `?page=n` |
| Anthropologie, Free People | paginated `?page=n` reads |
| Athleta | the site's own product-card fields |
| Aerie | category pages and on-site search |

Promotions were running on every site but Anthropologie. Where a tile shows two prices, the struck or "original" figure is used. Promo lines were stripped before reading (WHBM "Save $50 off $200+", Soma "N for $X"). Size-range prices (misses to plus) use the misses figure.

## Where the brief would give a confident wrong answer

1. **Rounding against the band cuts.** Rounded half-up, a $79.50 blouse becomes $80, which is not "under $80". A $34.50 tee becomes $35. The band rule should read the exact figure in `note`. No band in this batch changes, but the rule should say which figure it uses.
2. **Multi-brand stores.** Anthropologie and Free People sell large numbers of other makers' clothes under their own roof. Category extremes there are routinely another brand: a $4,500 Nigel Preston coat and a $2,498 Retrofete dress at Free People, and AGOLDE and Levi's at Anthropologie. Own label was isolated product by product:
   - **Anthropologie:** by the name prefix the site prints (Maeve, Pilcro, By Anthropologie, Daily Practice).
   - **Free People:** by the brand field on each PDP. Free People's main line carries no brand field, so "no brand field and no maker in the name" is treated as Free People. That inference sets FP's blouse low, blouse high and dress high, and is flagged for a spot-check.
3. **Sister banners can hide inside the brand's own site.** Talbots mixes in Haven Well Within, its sister banner with its own stores. Haven product IDs were excluded.
4. **"Blouses & shirts" categories are full of knits.** At WHBM, Free People and Aerie, the category minimum is a knit tee, a mesh layer or a polo. A category-minimum read would understate the blouse entry by $20–40 and could flip a brand to Basic.
5. **The rule doesn't fit intimates and activewear brands.** Soma, Athleta and Aerie do sell the garments, so they are priced. But their figures come from lounge or athleisure pieces. Aerie reads **Basic** by the rule ($24.95 tee, $49.95 woven shirt). Soma and Athleta would read Premium, which overstates a mall intimates brand and a Gap Inc. activewear brand. Hand-banding is recommended, as the brief anticipates.
6. **The crewneck staple and the elevated pair are often missing.** Most mall brands sell no cashmere crewneck, so sweater `basis` = `range` for most. Talbots is the one true `pair`.

## Coverage limits (also in each row's `note`)

- **Athleta:** grids lazy-load. 128 of 329 tops and 90 of 414 tee-search results rendered, so the tee high is indicative.
- **Free People:** tops (8 pages), dresses, jackets and shoes (6 pages each) were capped. Lows are sorted and robust; highs come from the pages read.
- **Anthropologie:** shoes read 753 of 1,461. The dress range is from the "casual everyday" category only.
- **WHBM:** no standing shoe category; read from "New Shoes & Accessories" (sandals and heels, no flat).

## Not womenswear / other

All ten are womenswear.

- **`NONE` because the brand doesn't sell it:**
  - Soma: jeans, outerwear and shoes.
  - Athleta: jeans and shoes.
  - Aerie: jeans and shoes (a Teva sandal is stocked, not its own).
- **Sub-lines:** the ones included and excluded are listed per row in `sublines_included`.

## Files

- `return.csv`: 10 rows, in the template's columns

## Reissue, 13 Oct evening (re-sent: batch 1 had not reached the Spectrum thread)

The data is unchanged except for two notes:

- **LOFT:** retried, still blocked by the same bot check. Still `NC`.
- **Aerie:** checked against the new core-garment rule. The $24.95 Basic V-Neck Boyfriend T-Shirt is the core tee. Both woven shirts are under $80 ($49.95 and $59.95). Basic still reads; the hand-band check is still advised.

No other batch-1 band rests on a cheap tee or shirt. Chico's, Talbots, White House Black Market, J.Jill, Anthropologie and Free People all fail the Basic test on full-price entries of $38–46 (tee) and $78–98 (shirt). So the core rule cannot change them.
