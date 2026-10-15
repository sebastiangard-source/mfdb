# batch05 — womens_dials_2026-10-14, thread 1 reissue

Read 15 October 2026 in Chrome on each brand's own US store. 10 brands, 688 style rows. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. No empty cells, and every enum is legal. The validator reports one expected mismatch: True Religion carries `styles_total` NC with no style rows, because it is held.

## What was read

| brand | platform / channel | styles in scope | sampled | ND | tech | craft |
|---|---|---|---|---|---|---|
| Anine Bing | Shopify feed + PDP text | 262 | 80 | 1 | 2 | 2 |
| True Religion | SFCC, **held at a PerimeterX wall** | NC (women's view-all counter reads 1,452) | 0 | — | NC | NC |
| Under Armour | SFCC women's grids + PDP JSON-LD `material` | 277 | 80 | 0 | 5 | 1 |
| Vilebrequin | SFCC, women's ready-to-wear only | 50 | 50 (all) | 4 | 1 | 2 |
| Ganni | SFCC `/us/clothing/?sz=400` + PDP | 340 | 80 | 0 | 2 | 1 |
| Hill House Home | Shopify feed + PDP | 240 | 78 | 3 | 1 | 2 |
| NIC+ZOE | Shopify feed, own-label vendors only + PDP Material + Care | 712 | 80 | 2 | 3 | 1 |
| Lafayette 148 | Magento category grids + PDP Materials block | 450 | 80 | 0 | 2 | 4 |
| Roller Rabbit | Shopify `womens-clothes` collection + feed `body_html` | 176 | 80 | 0 | 1 | 2 |
| STAUD | Shopify feed + PDP Fit & Fabric | 503 | 80 | 1 | 1 | 1 |

Every share is out of all styles in the table, ND rows included. **Understated because of ND:** Vilebrequin, where 4 of 50 rows are ND (linen and broderie pieces), which understates linen. Hill House Home (3 dresses), NIC+ZOE (2), Anine Bing (1) and STAUD (1) are lightly affected.

## Headlines

- **True Religion is held.** About a dozen grid requests in, every page returned a 307 to a PerimeterX/HUMAN "px-captcha" page. One plain retry about 15 minutes later in a normal tab hit the same wall, so it was not worked around.
  - Filed: the jeans link (verified: 91 women's jean styles on the first page) and shoes NONE per the worklist.
  - Everything else is NC. The other women's nav paths seen before the wall are listed in `note` but were not tile-checked.
- **Lafayette 148, proposed craft 4.**
  - The site claims the house owns "our very own workshop and production facility in China" and calls itself "a truly vertical company".
  - The 1996 SoHo garment-factory origin is dated and placed.
  - The craftsmanship pages document how the blazers and the hand-finished double-face coats are built.
  - Against a 5: the facility is unnamed beyond its country, product pages say only "Imported", and the mills are unnamed. The Spectrum thread may read the vertical claim as a 5.
- **Under Armour, tech 5.** The house is built on its own named performance fabrics. It is the batch's only synthetic-led house (78% synthetic), with a `split` shape.
- **Ganni** also shapes `split`: synthetic-led coats, jackets and pants sit beside a cotton-led core of tops, dresses and denim.
- **Fabric dials of note:**
  - Lafayette 148 is the batch's broadest natural spread: cashmere, cotton, wool, silk and synth all at 3.
  - Roller Rabbit is 74% cotton-led (cotton 5, 92% natural), mostly Indian cotton and block prints.
  - Vilebrequin: linen 4 and silk 3.
  - STAUD: cotton 4, synth 4 (polyester occasion dresses) and silk 3.

## What contradicted the record or the brief

- **Worklist `_sold` flags corrected:**
  - Roller Rabbit, **shoes = yes, not no.** `/collections/shoes` sells Roller Rabbit x Flabelus collab slippers and Mary Janes (kept as collab) plus own-label flip flops and quilted slippers.
  - Roller Rabbit, **tee = yes is doubtful.** Tees exist only in the Pima pajama range (excluded as sleepwear) plus one pointelle tee in the casual range. With no tee listing, the cell is NC and the row is `partial`. The Spectrum thread may prefer to set the flag to no.
- **Flags confirmed where thin:**
  - Vilebrequin sweater: one crochet sweater, in the sweatshirts category.
  - Hill House Home sweater: 2 knits in stock.
  - Under Armour: no blouses, sweaters, jeans or dresses.
- **Unisex:** Under Armour lists UNLESS pieces and collegiate replica jerseys in its women's grids. They are counted and flagged.
- **Third-party and own lines:**
  - NIC+ZOE: 181 third-party clothing products (Varley, Paige, Chan Luu and others) were dropped. "Gold Label" and "JKT" vendor strings were treated as third-party; if either is a house line, the range is slightly understated.
  - Roller Rabbit x Hill House Nap Dress and Nap Skirt are kept and tagged in `lines`.
  - Vilebrequin x Abu Dhabi: one collab dress, kept and tagged.
- **Lyocell kept as its own fibre:** NIC+ZOE has 4 lyocell-led styles and Hill House Home has 1.
- **Hill House Home:** Nap Dresses are counted as dresses per the thread. Home goods, kids, sleepwear and swim are excluded. 2 sampled rows (a wallpaper and a baby onesie) were dropped after reading, leaving 78.
- **Composition-reading fixes:**
  - Lafayette 148 shares a style code across fabrications (e.g. the Lafayette Flare Pant in crepe, wool and cashmere). Each fabrication is kept as its own style, with a `-a/-b/-c` suffix.
  - STAUD and Lafayette 148 state composition in two page formats each, and the first automated pass missed one of them. Both brands were re-run until only genuine ND remained.
  - Typos filed as meant: "Raime" (ramie, Lafayette 148), which was added to the parser as a natural fibre, and "Polymide" (polyamide, NIC+ZOE).

## Not reached / limits

- **Made-in coverage on product pages is uneven:**
  - Anine Bing: 100% of PDPs state a country.
  - Hill House Home: about 90%.
  - Roller Rabbit: about 78% (mainly India).
  - Lafayette 148: "Imported" only, though fabric origin often appears.
  - STAUD, Ganni and NIC+ZOE: 0%.
- **STAUD's about-us page renders empty** (navigation and footer only), so its craft 1 rests on what the site shows.
- **Bot walls:** True Religion only.

## Out of scope but noticed

- **Roller Rabbit's product feed carries supplier names** in the vendor field (Affina, Revolution Knits, Sophistica, Sapphire and others). They are not stated on any product page, so they were not counted as named makers. They may interest the craft audit.
- **Lafayette 148's house fabric names** (Finesse Crepe, Punto Milano, Techno Stretch Twill) are cloth names, not technical claims. Tech is proposed at 2 on stretch content alone.
