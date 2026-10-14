# womens_houses_and_held_2026-10-14 — Part 2: Kapital, UGG, Y-3, Sanderlak

Read 14 October 2026 in Chrome. Files:

- `return.csv`: 4 rows, 132 columns, no empty cells.
- `own_doors.csv` (Sanderlak, 1 row) and `stockists.csv` (Sanderlak, 5 rows).
- `facts_first.csv` (Sanderlak). This is an extra; the brief asked for a facts-first row.

`reconcile.py`: 4 exact, 0 rewrites, 0 unmatched.

| brand | status | prices read | styles / with composition | natural / synthetic / cellulosic | own doors US / world |
|---|---|---|---|---|---|
| Kapital | partial | 7 of 8 (shoes `NONE`), JPY | 387 / 387 | 83 / 11 / 5 | 0 / 12 |
| UGG | partial | polo and outerwear; shoes `NC` | 35 / 35 | 40 / 60 / 0 | 10 (carried) / `NC` |
| Y-3 | complete | 7 of 8 (polo `NONE`) | 111 / 110 | 40 / 52 / 8 | `NC` / `NC` |
| Sanderlak | partial | 7 of 8 (shoes `NONE`) | 35 / 0 | `NC` | 1 / 1 |

## Kapital

**Prices are in JPY as displayed, tax included, not converted.** There is no US storefront and no USD option. The WEB SHOP linked from kapital.jp is kapital-webshop.jp. Two prices were checked on the product pages: 10,780円 and 18,480円.

**Styles.** All 387 men's product pages were read for composition, which took longer than the 30-minute box.

- Japanese fibre names were mapped (ポリウレタン counted as elastane).
- Multi-part labels were read up to the main 100%.
- 14 styles carry elastane, none at 5% or more.

**Why the row is `partial`.** After about 400 page reads, a later listing fetch returned 403. I stopped there, so `colourway_ratio` is `NC`.

**Doors:** the Shop List names 15 shops, all in Japan.

- 12 are own doors.
- 3 corners on Hankyu Men's Osaka 5F are treated as concessions.

**Craft:** I propose **4**.

- The Company page lists four own sewing factories and an own dye works in Kojima, and the company was established in March 1985.
- A few pieces state Nepal, Vietnam or China, so owned making doesn't cover the whole range.
- A 5 is arguable if those are ruled minor.

## UGG

- **No wall at first.** The homepage loaded, and the Men's link opened `/men/` (194 results) with no wall. The men's apparel listing and all 35 apparel product pages read.
- **Then the wall.** Opening `/men-footwear/` brought up "Verification Required — Slide right to secure your access", a slide puzzle naming "automated (bot) activity on your network".
  - Not solved.
  - One plain reload about five minutes later showed the same wall.
  - So shoes and all facts pages are `NC`.
- **Few garments at full price.**
  - The only tee is the UGG × Willy Chavarria collab.
  - The only button-up and the only trouser are on markdown.
  - The crewneck is a sweatshirt.
  - So tee, dress shirt, dress pants, sweater and jeans are `NONE`.
- **The polo** is the Lendon Rugby Top, which UGG calls a "rib polo top".
- **Doors** carried as the brief says: 10 own, 36 outlets, 1 concession.

## Y-3

- **Store.** I read adidas.com/us/y-3, which redirects to `/us/y_3`. It has 139 men's clothing articles (111 styles, all at full price) and 78 shoes. Composition comes from each style's product data, its "Main Material" line.
- **Doors stay `NC`.** adidas.com/us/stores rendered no locator, and www.y-3.com still doesn't resolve. The brief's 0 isn't confirmed from a locator.
- **Outerwear high is $1,000** (GTX Padded Hooded Coat). It leaves out two leather jackets ($1,800 and $2,000) and the wool blazer.

## Sanderlak

**Fibre: no composition is published.** Product pages have a "Details" tab, which the FAQ says carries care and provenance, but it's empty on every page. So the fibre split is `NC` and the row is `partial`. Descriptions name a fibre on 26 of 35 styles.

**Doors: one store.** The NYC Flagship at 2 E Broadway (Wednesday–Saturday, 12–7). It's the only store worldwide. The FAQ still says "available exclusively online", which is out of date.

**Stockists** are the five retail partners the FAQ names from December 2025: SSENSE, Net-a-Porter, Moda Operandi, Bergdorf Goodman and Saks Fifth Avenue. The site has no stockist page and gives no addresses.

**Craft: I propose 2.**

- The site says only "crafted in Europe or the United States".
- Maharam is named as the textile partner on four styles (the dégradé jacquard).
- No maker or owned workshop is named.

**Signature product:** the Maharam Coat. The site itself calls the Maharam jacquard "Sander's signature".

**Quote:** the house's own line from the Explore page.

**Not found:** Sanderlak isn't on Vinted or Grailed by brand search.

## Across the four

- **Certifications:** B Corp is `no` for all four in the bcorporation.net directory (searched Kapital, Deckers, adidas, Sanderlak). GOTS wasn't searched and is `NC`.
- **Vinted** brand IDs come from Vinted's brand search:
  - Kapital: 576107
  - UGG: 2239 and 5853977
  - Y-3: 117012 and 6397426
- **Rows not written:** `proposed_tech` is `NC` throughout, because there's no tech rubric in the pack. `return_styles.csv` wasn't written, since the brief didn't list it. The per-style reads are summarised in the rows and this note.
- **Outerwear highs:** I excluded leather, shearling, blazers, vests and one-off remakes for the men's brands too, matching the women's 14 October ruling. Rule if men's should differ.
