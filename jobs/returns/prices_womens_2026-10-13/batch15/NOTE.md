# prices_womens_2026-10-13 — batch 15

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Hurley | $28 / $55 / $55 | Basic by the rule; hand-band check (surf and swim) | women's only |
| Kiyonna | none / $88 / $96 | **hand-band** (rule reads Premium) | own label only |
| LAPOINTE | none / $590 / $750 | True Luxury | complete |
| Mestiza New York | none / $250 / $278 | Accessible | Daytime line |
| Sea | $365 / $225 / $195 | Accessible | complete |
| Terez | $74 / none / $250 | **hand-band** (activewear) | own label only |
| Ciao Lucia | none / $245 / $295 | Accessible | own label only |
| GRACE LING | none / $995 / $1,290 | True Luxury | complete |
| Jamie Haller | $198 / $375 / $550 | True Luxury | complete |
| Jordan | $30 / none / none | **hand-band** (athletic and shoe-led) | women's only |

## Where the brief would give a confident wrong answer

1. **Licensed merch and kids' items inside women's feeds:**
   - **Terez:** 316 girls' products and about 330 Terez x MLB, NFL and NBA licensed pieces. Only about 120 own-label women's items remain.
   - **Ciao Lucia:** kids' "Ciao Bambini" dresses ($98–105), which would set the dress low.
   - **Jordan:** Nike College licensed tees mixed into the women's Jordan listing.

   All were excluded.
2. **Shoes are only collaborations.** Every Ciao Lucia shoe is a collaboration (Larroudé, K. Jacques, Viani Milano), so shoes are `NONE` for its own label.
3. **Hurley reads Basic.** With a $28 tee and a $55 woven shirt it passes the Basic test. Like O'Neill, it is a surf and swim brand where swim is most of the women's stock.
4. **Shoe houses with apparel.** Jamie Haller is a shoe-led label that now sells a full apparel range, so it is banded on apparel. On its $515 ballet slipper the shoe rule would read Accessible. Jordan has no blouse or sweater, so it is hand-band.
5. **Sale-only lines read at regular price.** Both of Kiyonna's sweaters carry "Sale!" in the title and were read at compare-at ($96), as with NYDJ's shoes in batch 13. Kiyonna's tops are jersey; only one is described as woven, so the blouse is `single`.
6. **Occasion lines split by the site.** Mestiza New York files products as Daytime, Cocktail and Evening. Only Daytime was read. LAPOINTE's gowns were excluded from dresses.

## How prices were read

| Site | Method |
|---|---|
| Hurley, Kiyonna, LAPOINTE, Mestiza, Sea, Terez, Ciao Lucia, GRACE LING, Jamie Haller | Shopify `/products.json` feed, in stock only, with descriptions where needed |
| Jordan | nike.com women's Jordan clothing (242) and shoes (301) grids, scrolled until every product loaded |

## Garment notes

- **No tee:** Kiyonna, LAPOINTE, Mestiza, Ciao Lucia, GRACE LING. Sea's only short-sleeve tee is an embroidered, fringe-hem top ($365).
- **Feather and embellished pieces as house style:**
  - LAPOINTE's feather coat ($9,800) is the outerwear high and may be runway.
  - Its $2,590 cashmere turtleneck with shearling trim was excluded.
- **Pre-order seasons.** GRACE LING sells most of its line as seasonal pre-order. These were kept as the main collection.
- **Single styles:**
  - Blouse: Kiyonna.
  - Sweater: Mestiza.
  - Jeans: LAPOINTE.
  - Outerwear: Terez, GRACE LING.
  - Tee: Sea.
- **`NONE` because the brand doesn't sell it:**
  - Hurley: jeans, outerwear (shacket only), shoes.
  - Kiyonna: tee, jeans (stocked NYDJ only), outerwear, shoes.
  - LAPOINTE: tee, shoes.
  - Mestiza: tee, jeans, shoes.
  - Terez: blouse, jeans, shoes.
  - Ciao Lucia: tee, jeans, shoes.
  - GRACE LING: tee, jeans, shoes.
  - Jamie Haller: dress.
  - Jordan: blouse, sweater, jeans.

## Files

- `return.csv`: 10 rows
