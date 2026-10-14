# prices_womens_2026-10-13 — batch 16 (final)

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 6 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Markarian | none / $895 / none | **hand-band** (evening house; blouse reads True Luxury) | own label only |
| Miss Circle | none / $129 / none | **hand-band** (party dresses; blouse reads Premium) | complete |
| MONSE | $490 / $690 / $560 | True Luxury | own label only |
| Reem Acra | — | **hand-band**; dress `np`, rest `NC` | see point 1 |
| Salt Life | $22 / none / none | **hand-band** (coastal lifestyle; likely Basic) | women's only |
| Yves Salomon | none / $1,000 / $525 | True Luxury | fur-free pieces, main line |

## Where the brief would give a confident wrong answer

1. **Reem Acra publishes no garment prices.** The online store sells only headpieces and headbands ($200–1,600). Every ready-to-wear, bridal and couture collection is a lookbook of unlabelled "Look NN" images, by appointment.
   - Dress is `np`: dresses are plainly sold, with no published price.
   - The other seven garments are `NC`: whether the collections include them can't be told from the site without opening each look.
2. **Yves Salomon is a fur house.** 362 products are tagged fur (mink, fox, rabbit) and many more are shearling or merino-lamb.
   - Garment ranges use only pieces the site tags "sans fourrure" / "fur free".
   - Every shoe is fur or shearling, so shoes are read as sold ($720–1,510) and flagged.
   - YS Army, a diffusion line, was excluded like Proenza Schouler's White Label.
   - The main site prices in EUR; its US store (us.yves-salomon.com) prices in USD and was used.
3. **Shoes that are only collaborations.** Markarian's shoes are Larroudé by Markarian, and MONSE's are Sperry x MONSE, so shoes are `NONE` for both own labels.
4. **Evening and party houses can't be read by the rule.**
   - Markarian: gowns are the core of the range; no tee or sweater.
   - Miss Circle: 398 of 644 products are dresses, and its "Dresses" type also holds skirts.
5. **Salt Life** passes the Basic tee test ($22) but has no woven blouse, so the rule can't finish. It would very likely read Basic.

## How prices were read

| Site | Method |
|---|---|
| Markarian, Miss Circle, MONSE, Salt Life | Shopify `/products.json` feed, in stock only |
| Yves Salomon | Shopify feed on the US store, filtered by the site's fur tags |
| Reem Acra | Shopify feed plus collection pages (no garment prices) |

## Garment notes

- **MONSE's** dress high ($9,000 embroidered) may be runway. Its tailored jackets (blazer-type) and jacket-front shorts were excluded from outerwear.
- **Miss Circle:** faux-fur and faux-mink coats were excluded, consistent with SIMONMILLER and Retrofête.
- **`NONE` because the brand doesn't sell it:**
  - Markarian: tee, sweater, trousers, shoes.
  - Miss Circle: tee, sweater, jeans, shoes.
  - MONSE: shoes.
  - Salt Life: blouse, sweater, jeans, shoes.
  - Yves Salomon: tee, jeans.

## Files

- `return.csv`: 6 rows
