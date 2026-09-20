# garment_links_2026-09-19 — men's garment links, per brand per garment

**Issued** 19 September 2026 · **Kind** links · **Pilot** 8 brands first · **Returns to** the Spectrum thread

Read `audit_protocol.md` first.

## The job

Every priced garment on a brand's card is a link. Today it is the brand's site search with a garment
word appended, and that returns women's and kids' product alongside men's. Replace it, for every brand
and every garment it makes, with **the URL of the brand's own men's listing for that garment** — a
navigation category page where one exists, a filtered search only where none does.

Good examples, one of each kind:

- navigation category: `https://shop.lululemon.com/c/men-pants/n1u9dn`
- navigation collection: `https://fahertybrand.com/collections/mens-shirts`
- filtered search, where no category page exists: `https://www.outerknown.com/search?q=polo&f=extra.gender%3AMens`

`return_template.csv` has one row per brand and one cell per garment. `NC` is a cell to fill; `NONE`
is a garment the brand does not make (already verified by the price pass) and needs no link — leave
it. `site_domain` and `search_url_on_file` are what the map holds; start from them, and correct the
domain in `note` if it is wrong.

## What a correct link is

1. **Men's only.** Open it and read the first two rows of tiles: every product is men's. A page that
   mixes genders, or a search that returns women's items, is wrong even if the URL says "men".
2. **The right garment.** The listing is for that garment — tees, polos, dress shirts, jeans, dress
   pants (or chinos where a brand has no dress pants), sweaters (knitwear), outerwear (jackets and
   coats), shoes. A parent category is acceptable when the brand has no finer one (`men-tops` for
   polos), and `note` says so.
3. **Stable.** A category or collection slug, not a campaign, sale, "new arrivals" or a facet state
   that expires. Where the only men's-only route is a search with a gender filter, that is the link.
4. **Live.** Returns a page with product on it today. A 200 with no tiles is a failure.
5. **The brand's own store.** Never a department store, marketplace or stockist.

Prefer, in order: a men's category page for the garment; a men's collection page; a men's parent
category; a search filtered to men's. Record which you used in `note` per brand, briefly.

## Rules

- `NC` means not found after looking; say why in `note` (no men's listing exists; gender not separable;
  site blocked). An empty cell is an error.
- One URL per cell, absolute, https, no tracking parameters.
- Names must match `canonical_keys.txt` exactly; run `reconcile.py` before returning.
- **Failure classes:** a "men" path that serves a unisex listing (Lady White Co., MAN–TLE, unisex
  houses — check the tiles); a facet URL that resets to all genders on reload; a locale redirect that
  swaps the store; a search that fuzzy-matches unrelated product (Valstar's `jeans` returns 17 items
  and no jeans).
- Do not touch the map. Return `return.csv` and `NOTE.md`, nothing else.

## Time box

Ten minutes a brand. Send the eight pilot rows first — Lululemon, Faherty, Outerknown, Todd Snyder,
J.Crew, Polo Ralph Lauren, Brunello Cucinelli, Lady White Co. — and stop. The last is there because
its range is unisex and the rule has to say what happens.
