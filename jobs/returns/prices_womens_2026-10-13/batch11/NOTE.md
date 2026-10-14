# prices_womens_2026-10-13 — batch 11

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Monique Lhuillier | none / $995 / $1,995 | True Luxury | complete |
| 3.1 Phillip Lim | $75 / $395 / $495 | True Luxury | full-price only |
| Wacoal | $68 / none / none | **hand-band** (lingerie) | complete |
| Marina Rinaldi | $265 / $335 / $345 | Accessible | main line only |
| PatBO | none / $695 / none | **hand-band** (resort and swim) | complete |
| Proenza Schouler | $450 / $790 / $890 | True Luxury | main line only |
| Joe's | $88 / $148 / $168 | Accessible (mean $158, just over the cut) | complete |
| Altuzarra | none / $895 / $795 | True Luxury | runway excluded |
| Courrèges | $250 / $870 / $550 | True Luxury | complete |
| LESET | $78 / $240 / $220 | Accessible | complete |

## Where the brief would give a confident wrong answer

1. **Diffusion lines on the same site.**
   - **Proenza Schouler White Label** (218 products) is sold alongside the main line. It was excluded as a sister line, as with Weekend Max Mara. On White Label alone the mean would be about $410, so the band stays True Luxury either way.
   - **Persona by Marina Rinaldi** appears only in the sale section and was excluded.
2. **Sale stock outnumbers full price.** At 3.1 Phillip Lim, 599 of 964 in-stock products are tagged final sale or sample sale. Only full-price stock was read; a plain feed read would pull the lows down.
3. **3.1 Phillip Lim reads True Luxury.** Its mean is $445 ($395 blouse, $495 Fair Isle crewneck). It is usually thought of as contemporary, so it's worth a check by hand, but the figures put it over $400.
4. **Runway pieces are labelled at Altuzarra.** Its product descriptions say "featured on the runway" for 27 pieces, including the dearest coats and dresses. Those were excluded. Altuzarra's product names carry no garment detail ("Cara Top"), so garments were classified from the descriptions.
5. **Ceremony and gown lines inside the dress grid.** Marina Rinaldi's dresses include five ceremony pieces ($4,000+), and Monique Lhuillier's feed is mostly floor-length gowns (150). Both were excluded from the day-dress range.
6. **More hand-band brands:**
   - Wacoal is lingerie: about 1,200 of 1,232 products are bras, panties and shapewear. Its 117 "t-shirt" products are T-shirt bras.
   - PatBO is resort and swimwear with embellished ready-to-wear. It has no tee or sweater, so the rule can't read. On its $695 blouse it would read True Luxury.

## How prices were read

| Site | Method |
|---|---|
| Monique Lhuillier, 3.1 Phillip Lim, Wacoal, PatBO, Proenza Schouler, Joe's, LESET | Shopify `/products.json` feed, in stock only |
| Altuzarra | Shopify feed, plus product descriptions for classification |
| Marina Rinaldi | server-rendered category listings on us.marinarinaldi.com, read page by page |
| Courrèges | the US store catalogue behind the site (category pages cap at 36). Prices were checked against the category pages and matched. /en-us/ is a 404; the US site is /us/ |

## Garment notes

- **Sweater with no plain crewneck:** the cheapest pullover was used for Proenza Schouler (polo sweater), Joe's (turtleneck) and Courrèges (mockneck).
- **Tee:**
  - Proenza Schouler's only short-sleeve cotton tee is the Hilma Top, so it's `single`.
  - Marina Rinaldi's viscose tees from $235 were excluded as not cotton.
- **Jeans:**
  - 3.1 Phillip Lim has only cargo and utility denim in full-price stock.
  - PatBO has one denim pant; five-pocket construction is not confirmed.
- **Trousers:** PatBO makes only a pull-on knit pant, so it's `single`.
- **Shoes without a flat or loafer:** Monique Lhuillier and PatBO, so both are `range`.
- **`NONE` because the brand doesn't sell it:**
  - Monique Lhuillier: tee, jeans.
  - Wacoal: everything but the tee.
  - PatBO: tee, sweater.
  - Joe's: shoes.
  - Altuzarra: tee, shoes.
  - LESET: jeans.

## Files

- `return.csv`: 10 rows
