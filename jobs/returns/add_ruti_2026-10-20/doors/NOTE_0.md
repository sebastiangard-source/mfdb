# NOTE_0 — Ruti stores (add_ruti_2026-10-20, Part 0)

**Site:** ruti.com is Ruti's own US site (Shopify, women's clothing). Footer and homepage list "Our Stores"; the full list is at https://ruti.com/pages/stores, with a page per store (stores-pa, -sf, -br, -ak, -sm, -ny).

**Result:** 6 US own stores, all open, none abroad, none marked coming soon, no outlets, no pop-ups. Part 1 proceeds.

- Stores: Palo Alto, San Francisco, Berkeley, Venice (CA), Santa Monica (CA), New York (Madison Ave.).
- Venue: only Palo Alto names a center ("Town & Country" in the page heading). The other five are `street` (headings: Fillmore St., Fourth Street, Abbot Kinney Blvd, Montana Ave., Madison Ave.). Not worked out from addresses.
- Berkeley: index says "Fourth St.", store page "4th St."; same address, returned once.
- Concessions `NC`: the locator doesn't list department-store counters. Stockists `NC`: not looked for.
- Not checked: the map widget (left alone), no closed-store history.
- Brief note: `return_counts.csv` template has no `status` column and no 'operator' rule for own stores; I wrote `NONE` in `operator`.
- `reconcile.py`: Ruti matches `canonical_keys.txt` (see below).
