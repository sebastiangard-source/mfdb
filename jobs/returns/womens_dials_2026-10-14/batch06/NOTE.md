# Batch 06 — womens_dials_2026-10-14, thread 2

Read 14 October 2026 in Chrome, on each brand's own US store. 10 brands: 9 `read`, 1 `partial` (UGG®). 739 style rows. `reconcile.py`: 10 exact, 0 rewrites, 0 unmatched.

## What was read

| brand | store / channel | styles (census) | sampled | with composition | note |
|---|---|---|---|---|---|
| TWP | Shopify feed + PDP accordion | 200 | 80 | 67 | 13 undisclosed: sequins, leather, ponyhair, placeholder-titled new arrivals |
| Chloé | SFCC grid `?sz=600` + PDP "Product Details" | 363 | 83 | 83 | denim sits under `/p/ready-to-wear-denim/`, outside the RTW path filter; 3 denim added |
| Wolford | SFCC grids + `Product-InfoPicker?material=` panel | 107 | 78 | 75 | hosiery/lingerie out; bodysuits read as tops |
| ba&sh | SFCC grid, paged by 60 + PDP text | 300 | 80 | 80 | 76/80 state a country |
| UGG® | SFCC grid + PDP bullets | 54 | 20 read | 19 | **DataDome wall after ~20 PDPs; retried once, still 403. 34 styles unread** |
| Varley | headless; `vvarley.myshopify.com/products.json` + PDP route data | 669 | 80 | 80 | DoubleSoft® is 124 styles |
| Akris | Shopify feed + PDP "Material:" line | 600 | 80 | 80 | parts run together without separators |
| La Ligne | headless; `lalignenyc.myshopify.com/products.json` + PDP details list | 611 | 79 | 79 | colour-per-product; style dedupe imperfect |
| Miu Miu | SAP Commerce grid `/page/N` + PDP "Materials" | 263 | 80 | 75 | every PDP says "Imported", no country |
| DÔEN | Shopify feed + PDP "Fabric Content" / "Country of Origin" | 416 | 79 | 79 | product_type is a season code |

Percentages in `return.csv` are of the **sampled** styles (undisclosed included); `styles_total` is the census. Fabric figures (`fab_*`) are shares of sampled styles **with** composition, by lead fibre; `fab_basis` gives each share.

## Headlines a reader would want

- **Two-fibre houses:** DÔEN (organic cotton made in India + silk made in China/India), Chloé (silk 31%, cotton 31%, wool 24% — 96% natural-led), Akris (86% natural; wool, cashmere, silk, leather), TWP (cotton-led, 11 of 67 leather).
- **Synthetic houses:** Wolford's clothing is second-skin polyamide/elastane (53% synthetic, 22% cellulosic); UGG®'s apparel read is ~80% synthetic (recycled polyester, acrylic faux fur); Varley splits — knitwear and DoubleSoft® are viscose-led, the active range is recycled polyester/polyamide with 10–22% elastane.
- **Miu Miu** splits: knitwear is cashmere/wool, but outerwear (fleece and pongé down) is recycled-polyester-led.
- **Tech:** only two named house fabrics in the batch — Varley's DoubleSoft® (a comfort jersey, 18% of range → 3) and UGG®'s UGGbraid / UGGfluff / LuxeFluff (3). Nobody here is built on a performance fabric.
- **Craft:** only Wolford shows owned making (Bregenz HQ + Murska Sobota plant, 264 seamless knitting machines, company site) → 4. Chloé, Akris (dated heritage, nothing about where the range is made), ba&sh (country on 95% of PDPs), DÔEN (country on 100%, an unnamed factory is an equity partner) → 2. TWP, Varley, La Ligne, Miu Miu → 1.

## Not reached

- **UGG®:** 34 of 54 styles, the sweater and shoes listing links, and all craft facts — DataDome wall (HTTP 403, "Please enable JS and disable any ad blocker"), one plain retry a few minutes later still blocked, page navigation included. No workaround tried. The `/women-clothing/` path is dead; the live path is `/women-apparel/`.
- **Heritage** not found on ba&sh, Miu Miu (US site) — `NC`.
- Client-rendered brand pages that returned no text to a read: Varley "Our Partners", Akris "double-face" and "cashmere". Makers may be named there.

## Contradicts the existing record / worth checking

- **TWP's feed tags carry a country on 178 of 200 styles — 102 "UNITED STATES"** — but only 2 of 80 product pages state one. If the brand surfaced those tags, craft would move to 2.
- TWP's "Jillian Blazer in Wool Flannel" states 100% Cotton — filed as written.
- Wolford sells a men's tee (52930) inside women's Tops & Jackets.
- Shoes for Akris and La Ligne: worklist says not sold; neither store has a shoe page — consistent.

## What the brief got wrong (or left open)

1. **`rules_craft.md` asks for a NOTE table of proposed ≠ current, and says the worklist carries each brand's current craft score and reason.** This worklist has neither, so no comparison table is possible; every `proposed_craft` here is a fresh proposal.
2. **Scope vs. the batch.** Several brands in batches 6–10 are mostly or wholly outside "women's clothing, not swim or lingerie": Wolford (hosiery/bodywear), Eberjey (sleepwear), HANRO and Jockey (underwear), ERES, ViX and Agua Bendita (swim), Gianvito Rossi (shoes only). Their fibre and fabric figures will be read off a thin or empty slice. I'll return what is in scope and say so per row; the Spectrum thread should decide whether those rows should carry fabric dials at all.
3. **`rules_fibre.md` asks for six files and `status complete|partial`; BRIEF asks for three files and `read|partial|NC`.** I followed BRIEF (three files, `read`). Categories, fibres and lines tables are not returned; `return_styles.csv` holds everything needed to cut them.
4. **The style-row enum has no "tops" category.** Blouses, camis and bodysuits go to `shirts`; jersey tees, tanks and henleys to `tees-polos`. A women's `tops` value would read better.
5. **`fab_denim` has no fibre to count** — it is filed as the share of styles in the denim category or with denim cloth in the title. Wool's figure includes alpaca, mohair, camel and yak.
6. **`shape` keyed on house labels misses splits inside a mixed label** (Wolford's "Tops & Jackets" holds both 100% wool knits and polyamide jersey; it reads `one`). Keyed on the standard category, Wolford would be `split`.

## Method notes

- Where a store is headless (Varley, La Ligne), the `*.myshopify.com/products.json` feed is served with CORS and was used, as `rules_fibre.md` suggests.
- Main fibre = highest share in the first composition listed; multi-part lines are read until the first part sums to 100. Leather, suede, shearling and fur are natural (fur and ramie as `other-natural`).
- Sampling: proportional allocation by the house's category, evenly spaced within each.
