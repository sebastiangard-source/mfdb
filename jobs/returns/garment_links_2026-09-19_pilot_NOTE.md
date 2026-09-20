# garment_links_2026-09-19 — pilot return, rulings applied 19 Sep 2026

**Returned:** `return.csv`, 7 rows. The template columns are unchanged, and so are the NONE cells.
- There are no NC cells left.
- `reconcile.py`: 7 exact, 0 rewrites, 0 unmatched.

**Method:** every link was read live in Chrome on 19 Sep 2026.
- It is the US store, with no login.
- Each URL was loaded fresh by direct navigation, and the first 8–10 tiles were read.
- On Shopify stores the gender tags were also read from `products.json` / `/products/<handle>.js`.
- Tracking and query parameters were stripped, and the links were confirmed to hold on reload.

## Rulings (Sebastian, 19 Sep 2026). These apply to the full pass.

1. **Unisex items inside a men's category pass.** The brand has filed the item as men's and sizes it as men's. A link fails only if a women's-only or kids' item appears, or if the listing is itself a unisex range.
2. **Lady White Co. is out of scope**, and not on any list.
3. **Multi-line houses use the unfiltered men's category pages.** Example: Polo Ralph Lauren, where Polo, RRL and Purple Label are interleaved. This is consistent with the price-pass rule that sub-lines count.
4. **A men's-filtered search that returns a few neighbouring garments is accepted** when it is the only men's-only route. Example: Outerknown's polo search, 3 polos + 2 tees. The search still has to return the garment; a search that returns none of it, like Valstar `jeans`, stays NC.

## Still open (not blocking the pilot)

- **NONE does not mean "does not make" for shoes.** Since price-pass ruling S5, shoes NONE means "no loafer" (and sweater NONE means "no crewneck").
  - 98 of 204 template rows have shoes NONE. This includes brands that sell shoes: Rick Owens, Fear of God, Barbour, Levi's.
  - Leaving them unlinked is right if a card links only priced cells. The template's wording ("a garment the brand does not make") should not reach the map's copy.
- **The link and the price cover different things.** The card's shoes price is a loafer range and its sweater price is a crewneck range, but the links go to all shoes and all knitwear, as briefed.
- **Dead links on file.** Brunello Cucinelli's `search_url_on_file` (`www.brunellocucinelli.com/en-us/search?q=`) is the corporate site and returns a 404. The real store is `shop.brunellocucinelli.com/en-us/`, as `site_domain` says.
- **Houses that block the browser will come back NC ("site blocked") in the full pass.** These are Saint Laurent, Gucci, Balenciaga, Bottega Veneta and Celine.
- **Outerknown's dress_pants link is weak.** It is the `mens-pants` parent (jeans, sweats, one chino), because the brand has no chino or trouser collection. It may deserve NONE.

## Per brand (full notes in the csv `note` column)

| brand | routes | domain on file |
|---|---|---|
| Lululemon | 7 category pages (`/c/<slug>/<id>`; the nav's query strings were dropped) | correct |
| Faherty | 7 men's collections + 1 parent (tee = tees/henleys/polos). Jeans collection is live but not in the nav | correct |
| Outerknown | 4 collections, 2 parents (dress_shirt, dress_pants), 1 men's-filtered search (polo) | correct |
| Todd Snyder | 8 men's collections (`mens-` handles) | correct |
| J.Crew | 8 category pages. Tee and polo use clean sub-category paths; the nav reaches them through a facet parameter | correct |
| Polo Ralph Lauren | 8 men's category pages, whole men's store | correct |
| Brunello Cucinelli | 6 category pages + 2 parents. Tee and polo share `t-shirts-polos`; jeans uses the `denim` category | correct; search_url dead |

**Not reached:** everything outside the pilot.
