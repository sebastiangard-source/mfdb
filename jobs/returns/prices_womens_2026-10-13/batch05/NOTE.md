# prices_womens_2026-10-13 — batch 5

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Anine Bing | $100 / $225 / $195 | Accessible | complete |
| Under Armour | $28 / none / none | **hand-band** (sportswear; rule can't read) | complete |
| Vilebrequin | $240 / $295 / $210 | Accessible by the rule; **hand-band check** (swim/resort) | complete |
| True Religion | $62 / $99 / $149 | **Premium on struck prices; see point 1** | complete |
| Ganni | $145 / $270 / $335 | Accessible | complete |
| NIC+ZOE | $58 / $98 / $98 | Premium | own labels only |
| Hill House Home | none / $118 / $248 | **Accessible, borderline; see point 2** | complete |
| Lafayette 148 | $248 / $498 / $598 | True Luxury | complete |
| STAUD | $98 / $245 / $295 | Accessible | complete |
| Roller Rabbit | $58 / $88 / $178 | Premium by the rule; **hand-band check** (pajama/resort) | complete |

## Where the brief would give a confident wrong answer

1. **True Religion has the same problem as Lucky Brand.** Almost every tile is marked 30–70% under a struck "Regular price", plus a site-wide EXTRA20 code. The row uses the struck figure and reads Premium. On what people actually pay, True Religion would sit near Basic. The ruling asked for on Lucky in batch 2 should cover True Religion too.
2. **Hill House Home: one sweater decides the band.** The brand sells only two pullovers.
   - The $178 Deirdre is a wrap, which is a cardigan-type, so it was excluded under the sweater rule. That leaves the $248 Amelia. The mean (blouse $118, sweater $248) is $183, which reads Accessible.
   - If the wrap counted, the mean would be $148, which reads Premium.
   - Hill House also sells no tee, so the Basic test can't apply.
3. **Brands outside the brief's named list whose ranges don't fit the rule:**
   - Under Armour (sportswear) has no blouse, sweater, jeans or dress, so `NONE`. Its tees are polyester performance tees.
   - Vilebrequin (swim and resort) prices beach linen and silk.
   - Roller Rabbit's biggest category is pajamas. The row leaves out all sleep and lounge.

   I'd add all three to the hand-band list alongside Beyond Yoga and SKIMS.
4. **More multi-brand stores.** NIC+ZOE sells Paige, Varley, Chan Luu and others. Own label was kept by Shopify vendor: NIC+ZOE, NZT, nz by NIC+ZOE and Gold Label. Gold Label is NIC+ZOE's premium sub-line.
5. **Capsules priced as part of the main range.**
   - Vilebrequin's Premium Capsule (lace and silk-crêpe pieces, $820–1,600) sits inside its ready-to-wear category. It was matched by style code and excluded.
   - Ganni's Disney pieces (Minnie Mouse and Daisy Duck tees and sweaters) appear in its normal t-shirt and knitwear grids, not only under "GANNI x Disney". They were excluded.

## How prices were read

| Site | Method |
|---|---|
| Anine Bing, NIC+ZOE, Hill House Home, STAUD, Roller Rabbit | Shopify `/products.json` feed, in stock only |
| Under Armour | server-rendered listing pages read page by page (`?page=N`), plus site search for dresses |
| Lafayette 148 | server-rendered category pages (`?p=N`, 96 per page) |
| Vilebrequin | full ready-to-wear grid (86 products) and the Premium Capsule grid |
| True Religion, Ganni | category grids; True Religion's 'Regular price' field per tile |

## Coverage limits (also in each row's `note`)

- **True Religion:** grids were read at 120 per page, because larger pages hung the browser. The denim read 115 tiles.
- **Under Armour:** the pants listing returned 30 products.
- **Hill House Home:** product types are style names, so garments were classified by title.

## Other notes

- **Garment substitutions:**
  - Blouses: STAUD makes only two button shirts. Its woven "tops" are mostly sleeveless and were not used. Hill House's blouse is its woven Nap Top. Roller Rabbit's entry blouse is a kurta.
  - Trousers: True Religion and Under Armour make no tailored trouser, so pull-on, cargo or sport pants were used, as noted per row.
- **`NONE` because the brand doesn't sell it:**
  - Hill House Home: tee, jeans, shoes.
  - Under Armour: blouse, sweater, jeans, dress.
  - Vilebrequin: jeans, outerwear, shoes.
  - True Religion: shoes.
  - NIC+ZOE: shoes.
  - Lafayette 148: shoes.
  - Roller Rabbit: jeans, and shoes (slippers only).
- **Licensed or third-party pieces kept out:**
  - Under Armour's "Unless Essentials" crew.
  - Roller Rabbit's stocked vendors.

## Files

- `return.csv`: 10 rows
