# prices_womens_2026-10-13 — batch 8

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Oscar de la Renta | none / $1,190 / $1,490 | True Luxury | complete |
| Re/Done | $120 / $295 / $295 | Accessible | own-made only |
| TOTEME | — | **`NC`: blocked** | see point 1 |
| ViX Paula Hermanny | none / $198 / none | **hand-band** (swimwear) | complete |
| Khaite | $320 / $880 / $990 | True Luxury | complete |
| M.M.LaFleur | $80 / $179 / $199 | Accessible | own label only |
| Rene Ruiz | none / $395 / none | **hand-band** (gown and cocktail house) | complete |
| Good American | $58 / $98 / $128 | Premium | full-price vendor only |
| Cinq à Sept | $85 / $195 / $265 | Accessible | complete |
| Rains | $75 / $165 / $175 | Accessible by the rule; hand-band check (rainwear) | complete |

## Where the brief would give a confident wrong answer

1. **TOTEME couldn't be read.** toteme.com/en-us, www.toteme.com and toteme-studio.com all ended on Chrome's "Privacy error" (certificate) page. I don't click through certificate warnings, so the row is `NC`. The warning may be local to this browser session, so it's worth a retry from another network or by hand.
2. **Sites where most of the feed isn't the brand's own full-price product:**
   - **Re/Done:** about 3,500 of 4,228 products are vintage resale (RE/DONE Vintage, Vintage Levi's) or collaborations (Hanes, KAIA, Disney, Peanuts, Coca-Cola). Only 261 in-stock products are RE/DONE-made.
   - **Good American:** 731 products sit under a separate `ga-sale` vendor.
   - **M.M.LaFleur:** files stocked FRAME jeans and EMU slippers under its own vendor name. Left in, FRAME would set the jeans low at $210.
3. **Khaite names every top "Top", knit or woven.** Blouses were picked by reading product descriptions: woven fabric and not sleeveless. The cheapest "tops" ($680–740) are ribbed cotton knits. The woven entry is $880.
4. **Exotic skins at the top of the shoe range.** Khaite's $10,800 Miles loafers are alligator, and its $7,800 pants are haircalf. All were excluded as exotic. M.M.LaFleur's Grace Loafer is *embossed* croc, which is leather, and was kept.
5. **Possible runway pieces:**
   - Khaite's $20,000 Dan Dress and Oscar de la Renta's $7,990 fringe jersey dress are the dearest "regular" dresses on each site. They aren't flagged as runway but may be.
   - Khaite's $17,800 Dani Top was excluded as a sleeveless embellished piece.
6. **Rains prices in EUR by default.** rains.com shows EUR. The US market (us.rains.com) was used, and its USD was confirmed on product pages.

## How prices were read

| Site | Method |
|---|---|
| Oscar de la Renta, Re/Done, ViX, Khaite, M.M.LaFleur, Rene Ruiz, Good American, Cinq à Sept | Shopify `/products.json` feed, in stock only |
| Rains | Shopify collection feeds on the US market |
| TOTEME | not read (certificate warning) |

## Garment notes

- **No tee:** Oscar de la Renta, ViX and Rene Ruiz. Rene Ruiz's only "tees" are shapewear.
- **Rene Ruiz** is a gown house: 460 of 758 products are gowns, all excluded. Its dress range is cocktail dresses only.
- **Jeans filed as pants:** Oscar de la Renta sells only embroidered or cutout "denim pants" ($2,490–3,990).
- **Single styles:**
  - Re/Done: shoes (Western Boot).
  - Rene Ruiz: blouse and outerwear (Lace Jacket).
  - Rains: tee.
- **`NONE` because the brand doesn't sell it:**
  - Oscar de la Renta: tee, shoes.
  - ViX: tee, sweater, jeans.
  - Rene Ruiz: tee, sweater, jeans, shoes.
  - Good American: shoes.
  - Rains: jeans, dress.

## Files

- `return.csv`: 10 rows (TOTEME all `NC`)
