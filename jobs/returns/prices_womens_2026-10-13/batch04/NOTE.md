# prices_womens_2026-10-13 — batch 4

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Zadig & Voltaire | $98 / $258 / $268 | Accessible | complete |
| 7 For All Mankind | $98 / $198 / $198 | Accessible | complete |
| EDIKTED | $32 / $48 / $48 | Basic | complete |
| St. John | $395 / $695 / $595 | True Luxury | complete |
| Rip Curl | $26.95 / $44.95 / $64.95 | Basic | complete |
| Beyond Yoga | $58 / $118 / $88 | **hand-band** (rule reads Premium) | complete |
| Maje | $135 / $320 / $190 | Accessible | complete |
| Max Mara | $305 / $490 / $435 | **True Luxury, without Weekend; see point 1** | complete |
| Splendid | $48 / $128 / $138 | Premium | complete |
| Cotopaxi | $35 / $65 / $150 | **Basic by the rule; hand-band check** | complete |

## Where the brief would give a confident wrong answer

1. **Max Mara: Weekend Max Mara and Sportmax are on the same site.** Both have their own US stores, so they were treated as sister banners and excluded. Together they make up about half of every category. Left in, the entry points fall to Weekend's (tee $195, blouse $275, sweater $260), but Max Mara would still read True Luxury on the mean. 'S Max Mara, Max Mara Studio and The Cube are included as sub-lines. Runway pieces were skipped. The main thread should confirm Weekend is a sister banner and not a sub-line.
2. **Cotopaxi reads Basic on a graphic tee.** Its cheapest tee is a $35 own-art graphic tee, exactly at the cut, and it sells no plain tee under $55. It is an outdoor brand (fleece, insulation, trail pants), and the rule has almost nothing to read. Hand-banding is suggested.
3. **Some sites list products that are no longer sold.** 7 For All Mankind's feed holds 1,865 products, many of them retired. A sold-out $138 bootcut would have set the jeans low, and a $78 tee that is out of stock would have set the tee low. From this batch on, the Shopify reads use only products with an in-stock variant. Earlier rows that say "may include sold-out styles" (Veronica Beard, batch 3) were read the older way.
4. **Licensed footwear.** Splendid's shoes are all listed under vendor "Vida" and tagged `dropship::vida`. They are Splendid-branded shoes made and shipped by a licensee, and they were treated as own label. The main thread should decide whether licensed footwear counts.
5. **Clearance with no struck price.** EDIKTED marks final-sale items "no-returns" and shows them at the cut price with no struck figure (for example $15 sweaters). These 333 items were excluded as not full price.

## How prices were read

| Site | Method |
|---|---|
| 7 For All Mankind, EDIKTED, St. John, Rip Curl, Beyond Yoga, Splendid, Cotopaxi | Shopify `/products.json` feed, filtered to women's and in stock |
| Zadig & Voltaire | category grids, `?sz=200` |
| Maje | category grids, `?sz=300`; original price where a markdown shows |
| Max Mara | category grids, with the line label on each card used to split sub-lines |

## Coverage limits (also in each row's `note`)

- **Max Mara:** the coats grid read 72 products, so the outerwear low ($850 Studio jacket) may be understated.
- **Zadig & Voltaire:** 11 of 20 shoe tiles had a price, and the US site sells no flats.
- **St. John:** a "Fall Humberto 2026" capsule in the feed was kept out of lows and highs as a possible capsule. 132 "ShopSimon" off-price products were excluded.

## Other notes

- **Activewear and outdoor ranges:**
  - Beyond Yoga is named in the brief as activewear. Only its lifestyle pieces were priced (woven shirts, pullovers, non-legging pants).
  - Cotopaxi's trousers are trail pants. Neither brand makes a tailored trouser.
- **Knit house:** St. John's knit pant and knit jacket are its core tailoring, so they were kept as trousers and outerwear.
- **Sweater basis:**
  - Splendid is a true `pair`: Libby Crewneck $138 and Tori Cashmere Crewneck $198.
  - The others are `range`, because no single crewneck exists in both an entry and an elevated version.
- **`NONE` because the brand doesn't sell it:**
  - 7 For All Mankind: shoes.
  - EDIKTED: shoes.
  - St. John: shoes.
  - Beyond Yoga: jeans and shoes.
  - Cotopaxi: jeans and shoes.
- **Collaborations excluded:** Rip Curl x Farm Rio; Splendid x @Cellajaneblog; EDIKTED's licensed (Barbie) pieces.

## Files

- `return.csv`: 10 rows
