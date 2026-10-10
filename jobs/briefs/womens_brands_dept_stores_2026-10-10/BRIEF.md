# womens_brands_dept_stores_2026-10-10 — every women's clothing brand the big department stores carry

**Issued** 10 October 2026 · **Kind** capture · **Nordstrom and Saks returned first, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job: the brand lists are long, paged, and sometimes
loaded by script.

## Why

A women's version of the map is starting, and its candidate list should come from what the stores
buy, not from anyone's memory. The men's map got its best candidate list from one shop's brand page
(Boyds, 84 names); the women's equivalent is the brand index of each big department store. Read
them all, and the union is the universe a knowledgeable shopper would expect the map to know.

## The job

For each store in `worklist_stores.csv`, open the store's **women's brand or designer index** (the
A–Z list, within women's clothing where the site offers that scope) and return **one row per brand
per store** in `return_brands_by_store.csv`:

- `store`; `brand_as_listed` exactly as the index writes it; `brand_url_on_store` (the brand's page on
  the retailer — this is the provenance, every row needs it)
- `listed_under`: the index the name came from (e.g. "Women > Brands A–Z", "Designers")
- `store_department_label`: the store's own department or tier word where it gives one — Nordstrom's
  "Designer", Saks's "Advanced Designer" and "Contemporary", Bloomingdale's "Designer" and "Contemporary",
  Neiman's "Designer" — as written, `none` where the index has no tiers
- `womens_clothing` yes/no: whether the brand has women's apparel on the retailer (open the brand page
  and look at the categories; a brand that shows only shoes, bags, beauty or jewellery is `no` and
  stays in the file)
- `item_count_as_shown`: the count the brand page displays, if it displays one; `np` if not
- `private_label` yes/no: the retailer's own brand (Nordstrom's Zella and Halogen, Bloomingdale's
  Aqua, Saks's own); record it and mark it
- `off_price_store` yes/no (Nordstrom Rack, Saks OFF 5TH)

Then build `return_brands.csv`, one row per **distinct brand** across all stores: `mark_as_written`
(the brand's own spelling if the stores disagree), `stores` (count), `store_list` (semicolon list),
`full_price_stores` (count excluding the off-price banners), `off_price_only` yes/no,
`departments_seen` (the tier labels, semicolon list), `brand_site_domain` if the retailer links it or it
is obvious from the brand page (otherwise `NC`), `on_womens_register` yes/no against
`womens_register.txt` in this folder. Sort by `full_price_stores` descending.

## Rules

- **The retailer's own index is the source.** Not a search for "brands at Nordstrom", not Wikipedia.
  If an index is paged or lazy-loaded, page it to the end and say in `NOTE.md` how (the count the page
  reports versus the rows you got).
- **Scope is women's clothing.** Shoes, handbags, jewellery, beauty, lingerie-only and kids-only brands
  are `womens_clothing` = `no`, kept in the file, and not counted in `return_brands.csv`. Swim and
  activewear are clothing.
- **One name per brand.** Merge spellings across stores in `return_brands.csv` (TORY BURCH / Tory
  Burch / Tory Burch Sport is two brands only if the retailer lists Sport as its own brand); say in
  `note` what you merged.
- `NC` nobody looked; an empty cell is an error. A store whose index cannot be read in Chrome returns
  one row with `NC` and the block in `note`.
- Do not touch the map. Return `return_brands_by_store.csv`, `return_brands.csv` and `NOTE.md`: what
  was read, how long each index was, what could not be reached, and which store's index looks
  incomplete.

## Known traps

- Nordstrom's brand index is the whole store; filter to Women and, where possible, Clothing, and say
  which filters were on. Its index runs to several thousand names.
- Macy's and Dillard's indexes are long and heavy on private labels and licensed names; private
  labels are marked, not dropped.
- Saks and Neiman's "Designer" and "Contemporary" are department tiers, not brand attributes; a brand
  can appear in both. Record every placement.
- Bergdorf is one store; its index is the luxury canon and is worth reading whole.
- Off-price banners list many brands that the full-price store does not; keep them separate so a
  brand that is only at Rack reads as such.

## Order and time box

Nordstrom and Saks first, returned early without stopping, so the schema can be checked on the two
largest and most differently built indexes. Then the rest in worklist order. An index is an hour or
two; past three hours on one store, return what you have and say where you stopped.
