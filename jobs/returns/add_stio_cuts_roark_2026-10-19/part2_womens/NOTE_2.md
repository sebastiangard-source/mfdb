# NOTE_2 — add_stio_cuts_roark_2026-10-19, Part 2 (women's read)

Read 19 Oct 2026 in Chrome. `reconcile.py`: 2 names, 2 exact. Files: `return_crossover.csv`, `return_prices.csv`, `return_dials.csv`, `return_styles.csv` (155 rows: Stio 116, Roark 39).

## Who got Part 2

- **Cuts Clothing:** stops here. Part 0 found no US own store (`NONE`), so it stays out of the Brand Set on this basis.
- **Stio** (14 own) and **Roark** (8 own): both read. Both answer **`yes`** to women's clothing.

## Headline

| | Stio | Roark |
|---|---|---|
| Women's styles (full read, no sample) | 116 (107 women's + 9 unisex) | 39 |
| Natural / synthetic / cellulosic | 24 / 76 / 0 | 77 / 23 / 0 |
| Shape | split | one |
| Women's prices (low–high) | tee 45–79 · blouse 99–179 · sweater NONE · jeans 139 · trousers 129–169 · dress NONE · outerwear 129–799 · shoes 99–169 | tee 39 · blouse 75–99 · sweater 119–149 · jeans 99 · trousers 89–115 · dress 129 · outerwear 129–299 · shoes NONE |
| Band proposed | Tier 2 (rule reads wrong) | Tier 2 |
| Fabric dials (denim/cashmere/linen/cotton/wool/synth/silk) | 2/1/1/3/2/5/1 | 2/1/1/5/1/4/1 |
| Proposed tech / craft | 4 / 3 | 2 / 1 |

## The band rule at Stio — it reads wrong

Stio has no blouse and no knit sweater (`NONE`). Its women's "sweaters" are down and fleece. So the blouse-and-sweater mean collapses to the woven shirts alone: (99 + 179) / 2 = $139, which is Tier 2. Tier 1 fails on the tee, but the cheapest women's tee is a $45 graphic logo tee; there's no plain one. I've proposed **Tier 2**. If you'd rather band an outdoor house on its outerwear ($129–$799, mostly $199–$479), it reads Tier 3. That's your call.

Roark reads cleanly. Its tee is $39, so it isn't Tier 1. The mean of the blouse and sweater entries (75, 99, 119, 149) is $110.50, which is Tier 2.

## Checked, and how

- **Stio:** `/collections/womens/products.json` (201 items; 116 clothing styles after removing gear, accessories and shoes), plus each PDP's Materials and Care block. Lupine Hooded Jacket and the Women's Teton Elevations Tee have no such block, so I read them from the Features "Materials" line. Prices are full price. The Pinion Down Pullover is marked down inside the women's collection ($202.30 from $289); it's flagged and doesn't feed a price cell. Shoes came from `/collections/womens-shoes-boots`; four of its seven styles are marked down and weren't used.
- **Roark:** `/collections/shop-all-womens/products.json` (64 colourway products, collapsed to 39 styles on the `style:` tag), plus the `product.materials` metafield on each PDP. No markdowns are in the women's collection. I checked the listing links against each collection's feed for women's-only content.
- **Standing defaults:**
  - Own labels only.
  - Lyocell would be kept separate, but no women's style is lyocell-led.
  - `fab_silk` is read: 1 for both, no silk.
  - Unisex listings are counted and flagged (Stio 9; one Roark colourway tagged both genders).
  - There's no sleepwear or swim in either women's range.

## Not reached

- **Stio `tech_share_of_range` (women's):** `NC`, not computed. The men's read gave 75% on the same fabric families.
- **Roark `made_in_stated_share` (women's):** 0%, carried from the men's regex over 106 PDPs on the same template, not re-checked page by page. The row says so.
- **`lines`:** `NC` for Stio. Roark's come from its `franchise:` tags.
- **`where`:** `NC` for both. Neither locator nor any store page says which stores carry women's. Stio's store pages say "full collection".

## Contradicts the brief

- **Roark:** the brief calls it "mainly men's". It is (106 men's styles to 39 women's), but its women's range is real: tees, button-ups, knits, jeans, pants, rompers, one dress, jackets. So it's a `yes`, not `partial`.
- **Fabric emphasis:** this is read off the style table, not the brand's image. Stio's women's range is 76% synthetic-led, with cotton a 3 (18%) and wool a 2 (6%, all PeakWool base layers). Roark is 77% cotton-led.
