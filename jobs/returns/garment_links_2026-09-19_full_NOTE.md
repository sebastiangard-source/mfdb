# garment_links_2026-09-19 — full return (204 rows)

**Returned:** `return.csv`, one row per brand, template columns unchanged.
- `reconcile.py`: 204 exact, 0 rewrites, 0 unmatched.
- **1,270 links found · 210 NONE left as they were · 152 NC.**
- 142 brands are fully linked. 40 of the NCs are the five houses that block the browser.

**Method:** read live in Chrome, 19–21 September 2026.
- US store, no login. Each URL was loaded fresh by direct navigation, and its first 8–10 tiles were read.
- Shopify gender tags were also read from `products.json` / `/products/<handle>.js`.
- Tracking parameters were stripped, and each link was confirmed to hold on reload.
- Candidates came from each site's own men's navigation, not from guessed slugs.

**Your rulings, applied throughout:** unisex items filed and sized as men's pass; multi-line houses use the unfiltered men's category; a men's-filtered search that returns mostly the right garment is accepted; Lady White Co. is out.

## 1. Verification

I re-read a random 26 links, including 8 with query parameters. Every one loaded, stayed on its own path, and kept its filter on a clean reload. No women's or kids' tiles appeared. Two failed and are now NC in the file:

- **Visvim polo.** The men's Cut & Sew facet holds no polo at all. The same URL is right for tee.
- **Club Monaco dress pants.** The men's pants page has one product, sold out and final sale. Its whole men's range looks to be winding down; the sweater link (1 product) is a thin pass.

That is 2 bad cells in 26, so on the order of 5–10% of the passing links are likely to be weak rather than wrong. The `note` column flags the thin ones per brand.

## 2. What the pass found that the map has wrong

**The site domain on file is not the US store (8).** The links use the real store; `site_domain` should be corrected.

| brand | on file | real US store |
|---|---|---|
| J.Lindeberg | jlindeberg.com | www.jlindebergusa.com |
| Isaia | www.isaia.it | www.isaia.us |
| Kiton | kiton.com | us.kiton.com |
| Isabel Marant | isabelmarant.com | us.isabelmarant.com |
| Baracuta | www.baracuta.com | us.baracuta.com |
| Peserico | peserico.it | us.peserico.com |
| Sid Mashburn | www.sidmashburn.com | shopmashburn.com (shared with Ann Mashburn) |
| Sugar Cane | selfedge.com (a third-party retailer) | no brand store — see §3 |

**Locale paths missing on file:** Finisterre (`/en-us`), Rodd & Gunn (`/us`), Eton (`/us/en/`), NN07 (`/en/us/`), Boggi (`/en_US`, and the on-file search sends US shoppers to the UK store), Ted Baker and Scotch & Soda (their `/us` paths now 404; both stores moved).

**34 of the `search_url_on_file` values are dead or wrong-locale.** Every card link built on them is broken today: Aimé Leon Dore, Ami Paris, Brioni, Canali, Carhartt, Cesare Attolini, Comme des Garçons, Corneliani, Diesel, Dries Van Noten, Eton, Filson, Herno, Hiroshi Kato, Isaia, Kiton, Massimo Dutti, Moncler, NN07, Our Legacy, PAIGE, Paul & Shark, Paul Smith, Prada, Rhude, Rick Owens, Scotch & Soda, Sid Mashburn, Son of a Tailor, Stone Island, Ted Baker, Thom Browne, Tom Ford, Valentino. This is the strongest argument for the brief: a sixth of the map's current links go nowhere.

## 3. Brands with no usable own store (all garments NC)

- **Comme des Garçons** and **Junya Watanabe**: comme-des-garcons.com is a lookbook with no commerce. The only CDG-operated shop is Dover Street Market, a multi-brand retailer, which rule (e) excludes.
- **Charvet**: charvet.com is a one-page contact card for the Place Vendôme shop. No catalogue at all.
- **Sugar Cane**: no US or brand store. sugarcane.jp is an information site; the only shop is Toyo Enterprise's Japanese store, with no garment categories.
- **Cesare Attolini**: the e-boutique says it is under maintenance, and every category link redirects to the homepage. Worth a re-check later; its categories are also season-scoped (`Trousers FW` vs `SS`), which will not be stable when it returns.
- **Industry of All Nations**: unisex throughout, with no men's split and women-tagged items in every listing. The Lady White failure class, on a brand that is in the map.

## 4. The five blocked houses

Saint Laurent, Gucci, Balenciaga, Bottega Veneta and Celine are NC, 40 cells. The extension cannot load these stores, exactly as in the price pass, where you read them by hand. They need the same treatment, or a reader that isn't this browser.

## 5. Patterns worth a ruling before the merge

1. **Tees and polos share one category at most luxury houses** (Prada, Dior, Fendi, Burberry, D&G, Valentino, Hermès, Loro Piana, Kiton, Canali, Zegna's peers, Tom Ford, Brunello Cucinelli). Both columns then hold the same URL. It's correct, but it means two cards' links are identical, and on several of them the polos start below the fold.
2. **Dress pants rarely exist as a category.** The link is usually a trousers or mixed pants page; a handful are one or two products (Tecovas, Mack Weldon, Y.Chroma, Rakho).
3. **Jeans is the weakest column** — 35 NCs. Most are houses that sell two or three jeans filed inside trousers, with no denim category and no clean search.
4. **Thin pages.** Several passing links have fewer than five tiles (Patagonia sweaters at 3, Lululemon sweaters at 5, Wythe polos at 3, Fedeli, Y.Chroma). They're real categories, but they will look sparse from a card.
5. **Sub-line houses.** RLX and RRL have no clean per-garment URLs; those rows use the line's shop-all page with a category parameter, which survives reload. Ralph Lauren Purple Label uses the `/r/purple-label` path refinement, except for pants, where it isn't valid.
6. **54 links carry a query parameter** because the store has no clean path for that listing (Banana Republic's `cid`, Brooks Brothers and RLX facets, Visvim's `item_category`, gender-filtered searches). All 8 that I re-read held on a clean load, but they are the cells most likely to rot.

## 6. Still open from the pilot

- **NONE does not mean "does not make" for shoes.** Since ruling S5, shoes NONE means "no loafer" and sweater NONE means "no crewneck". 98 rows carry shoes NONE, including brands that plainly sell shoes. The template's wording should not reach the map's copy.
- **The link and the price cover different things.** The shoes price is a loafer range and the sweater price a crewneck range, while the links go to all shoes and all knitwear, as briefed.
- **Outerknown dress pants** is still a weak parent (`mens-pants`: jeans, sweats, one chino). NONE may be the better answer.

Per-brand routes and caveats are in the `note` column; provenance is in `source`.
