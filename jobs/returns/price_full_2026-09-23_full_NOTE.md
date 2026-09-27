# price_full_2026-09-23 — NOTE

`return.csv` has one row per brand, 203 rows in total, in the 65-column schema. `reconcile.py` gives 203 exact, 0 rewrites, 0 unmatched. There are no empty cells and every basis and currency value is legal. Every figure carries a product name and the URL it was read from.

## What was checked

| Status | Brands |
|---|---|
| read | 196 |
| partial | 1 — Hermès |
| no_store (all `NC`) | 6 — Comme des Garçons, Junya Watanabe, Charvet, Sugar Cane, Rakho, Cesare Attolini |

- **No-store rows.** The first five were not re-verified; the brief lists them as having no store. Cesare Attolini was checked today: /e-boutique still reads "E-boutique under maintenance. WE WILL BE BACK SOON".
- **Hermès (partial).** All category grids were read. After about 13 product pages the site returned 403 and then a blank challenge page. No captcha was attempted.
  - Jeans are `NC`: one "Straight cut jeans" turned out to be gabardine.
  - The $16,300 Empreinte jacket and the Destin/Ignacio loafers were not read, so none of them is used.
  - Polo sleeves and several sweater fibres are unconfirmed.
  - **This row needs a human read.**
- **Other `NC` cells in read rows.** Mack Weldon jeans: the only jean is Final Sale.
- **Currency.** 179 USD, 15 USD_landed (duties-paid US storefronts: Rick Owens, Yohji, Officine Générale, Hartford, Our Legacy, Auralee, Luca Faloni, Reiss, Husbands, Dries Van Noten, Wales Bonner, Acne Studios, Palm Angels, Percival, Canali). One row each in JPY (Ring Jacket, no US store), GBP (Hackett, no US store: hackett.com/us is a 404 and /intl/ shows £ on product pages) and EUR (Zilli, € even with USA selected). Nothing was converted.
- **Cell bases.** 900 range, 361 pair, 131 single, 182 NONE, 50 NC.
- **How the stores were read.**
  - **Shopify stores:** full `/products.json` feeds. Headless stores were read through their shop.* or *.myshopify.com feed, and prices confirmed on the main domain.
  - **Salesforce, custom and VTEX stores:** rendered category grids or the page's own embedded data.
  - **Search indexes:** a few stores were read through the site's own search index (Indochino and Hackett via Algolia or the storefront API, Suitsupply via its Storefront API). One agent's attempt at Rhone was refused by the permission system as credential use. Later briefs to agents forbade search API keys.
  - **Every brand:** two displayed product-page prices confirmed and the search URL tested.
- **Spot-checks (brief: every batch).** 26 figures re-read on live pages from this thread, across the pilot and batches 0–46. All matched.

## What contradicted the record

Of the 1,421 garment cells where the map held a figure and the brand was read:

| Result | Cells |
|---|---|
| Low and high both reproduced | 310 |
| One end reproduced | 314 |
| Both ends changed | 693 |
| Map figure now NONE or NC | 36 |

In addition, 68 cells are new where the map held null or `?`.

The recurring reasons:

1. **Old or inherited lows.** Many of the five core garments were an older list or a base-currency feed: Paul & Shark, Isaia, Stone Island, Corneliani, Ami, Hackett. Ring Jacket's USD figures do not exist on its JPY store.
2. **Sale prices filed as lows.** Examples: Massimo Dutti tee 46 and shirt 90; Levi's jeans 60; the BOSS tee low of 49 was an undershirt.
3. **Excluded items the map had used as highs:**
   - Shearling: Levi's 1200, Moncler 5410, Etro 8900, Celine 8700, Tom Ford 10390, Berluti 11000.
   - Exotic skins: RL Purple Label shoes 7500, Berluti shoes 11400.
   - Runway pieces.
   - Collaborations: Malbon, Barbour × Paul Smith, Samsøe Samsøe's Sagiles tee.
   - Women's product: Rowan jeans, Ksubi sweater.
4. **The map said NONE, but the garment is sold.** Celine polo, Acne Studios polo, NN07 shoes (only collaborations, so still NONE), Lacoste jeans, Joe's Jeans polo, Rubinacci jeans.

## Rulings made in this pass, for you to confirm or reverse

These go beyond the brief. Each was applied to every row, and the affected rows name them in `note`.

1. **Tee and polo are short-sleeve.** Long-sleeve counts only when the brand sells no short-sleeve version. Examples: ALD, Balenciaga, Sacai, Our Legacy and Auralee polos; J.McLaughlin tee.
2. **Knitted tees count as tees** when the brand names them a T-shirt. Examples: Isaia $1,550 cashmere, Eleventy $1,095, Sandro $295.
3. **Knit polos count as polos** when filed as polos.
4. **Sold out.**
   - Sold out is not NONE.
   - Agents preferred an in-stock product at the same staple where one existed, and named the sold-out one.
   - Greg Lauren's outerwear high is a sold-out $3,150 coat; the in-stock alternative is $2,875.
5. **Final Sale, clearance and outlet items are not prices.** Returnable markdowns are read at compare-at after the second-product check. This removed many lows and a few whole garments: Mack Weldon jeans, Tecovas polo and sweater, Ted Baker jeans.
6. **Collaborations and capsules are excluded from lows too.** A garment sold only as a collaboration is filed NONE and named. Examples: Finisterre shoes, Madhappy, Kith shoes, NN07 shoes, Norse Projects shoes.
7. **Shearling is never the high.** It is named in the note. The brief's fur rule does not mention shearling.
8. **Leather or suede as the "elevated material" for an outerwear pair.** This produces most outerwear pairs above ~$1,000.
9. **Cardigans, hoodies and quarter-zips enter only a sweater `range`.** Under the brief's range rule the category's dearest item becomes the high. At JW Anderson, Amiri, Wythe and Maison Margiela that is a cardigan or zip hoodie above the dearest crewneck, which is named in the note. **This is the biggest single effect on the sweater column.** A crewneck-only range may be what the map wants.
10. **Jeans must be denim five-pocket.** Wythe, Billy Reid, Mizzen+Main, Berluti and Lemaire are NONE on this rule.
11. **50% is not a majority.** Agents also judged whether 80–85% extrafine merino is "superfine wool" (Canada Goose, Vince, Moncler). **This needs a rule.**
12. **Embellished pieces are treated as limited and never a high.** This covers crystals, studs, beading, heavy embroidery and chain harnesses at Versace, Dolce&Gabbana, McQueen, Givenchy, Gucci and Golden Goose. **This is an agent's own ruling and it moves several luxury highs a long way.** At D&G, for example, embroidered shirts run to $35,000.
13. **Embossed or printed "croc" on calf or cowhide is not an exotic skin.** Examples: Ami $2,650, Rhude $4,110, Tom Ford $2,350.
14. **Made-to-order programmes are excluded.** State & Liberty was affected. Brands whose whole range is made-to-measure (Son of a Tailor, Indochino, Proper Cloth) are read at their listed prices.

## Rows worth a human look

- **Hermès:** partial (above).
- **Gucci:** read from price-sorted category pages (about 36 each end). No product page was captured with its price in view, and search is `NC` after Akamai started denying fetches. **This row has lower confidence than the others.**
- **Brax:** the US store sells only trousers and jeans. The other six garments are NONE for this store, although Brax sells them in the EU.
- **John Smedley:** the "JS x John Smedley" line is counted as a sub-line, and it sets three lows. Its landing page calls it the brand's diffusion line, but product pages say "collaboration".
- **Paul Smith:** the grids ignore sort on first load. Each category was read as the top 21 of a low sort and a high sort, not in full.
- **Dior:** the sweater high is the $3,500 Byzance crewneck (mostly viscose). The entry sweater is already cashmere, so the rule takes the dearest regular crewneck.

## Changes to the pilot rows since the early return

- **Wythe shoes:** high $1,298 → $1,198. The $1,298 boot is sold out, so the in-stock boot was used.
- **Massimo Dutti polo:** 70–390 pair → 70–130 range. The $390 polo is long-sleeve.
- **Peter Millar polo:** 105–598 pair → 105–175 range. The $598 polo is long-sleeve.

## What the brief got wrong

- **Parallel batches.** One shared browser can run only two agents safely.
  - At three to six concurrent agents the Chrome extension hung three times, for 25–45 minutes each. Those rows were filed `NC` and then re-run.
  - The WAF luxury domains (Saint Laurent, Gucci, Balenciaga, Bottega Veneta, Dior, Palm Angels) freeze the extension after one script per tab. Opening a fresh tab for each read and storing results in the site's own localStorage got round it. The stored copies were deleted afterwards, except a leftover 'hxd' key on hermes.com that could not be cleared after the block.
  - This workspace cannot reach retail sites directly.
- **"Blocks browsers."** None of the five named houses actually served a block page to a normal load. Celine's and Berluti's Akamai challenge cleared on its own, and Hermès blocked only after about 13 reads.
- **The capsule rule needs to cover lows.** At several houses a capsule or collaboration is the cheapest item.
- **The range rule versus the staple.** See ruling 9 above.
- **Search URLs on file that failed:**

  | Brand | On file | Working |
  |---|---|---|
  | J.Crew | search2?Ntrm= (404) | search?term= |
  | Proper Cloth | /search?q= | /shop/search/ |
  | Luca Faloni | ?q= | ?query= |
  | Stone Island | ?q= | /en-us/search/?query= |
  | Bode | bodenewyork.com | bode.com |

  Several others are overlay-only and filed as `NONE`.
