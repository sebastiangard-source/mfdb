# doors_tel_2026-10-16 · batch 3 (bags and leather goods) · NOTE

**Returned:** 338 door rows (158 own-door, 180 outlet) and 10 count rows. `reconcile.py` came back clean: 10 exact, 0 to rewrite, 0 unmatched. No cell is empty.

| Brand | Own | Outlet | Concessions | Stockists | Locator rows |
|---|---|---|---|---|---|
| Coach | 136 | 172 | 0 | 0 | 323 |
| Longchamp | 7 | 6 | 22 | 124 | 193 |
| Polène | 2 (1 opening) | 0 | 0 | 0 | NC |
| Cuyana | 5 | 0 | 0 | 0 | 5 |
| Senreve | NC | NC | NC | NC | NC |
| Strathberry | NONE | 0 | 0 | 55 | 61 |
| Mulberry | 1 | 1 | 12 | 0 | 102 |
| Smythson | 1 | 0 | 0 | 0 | NC |
| Goyard | 6 | 0 | 2 | 0 | 38 |
| Moynat | 1 | 0 | 1 | 0 | NC |

## Rulings applied

- **Counters are never rows** (20 Oct). Each counter is counted in `us_concessions` and not returned as a row:
  - Longchamp: 22 "Longchamp Boutique" entries inside Nordstrom, Bloomingdale's and Macy's.
  - Mulberry: 12 Nordstrom shops on its own official-stores list.
  - Goyard: 2 counters in Bergdorf Goodman.
  - Moynat: 1 counter in Saks Fifth Avenue.
- **Strathberry:** every US entry is listed under the retailer's name (Bloomingdale's, Nordstrom, Neiman Marcus, Saks), so they are stockists, not concessions.

## Not reached

- **Senreve: NC.** Every page of senreve.com returns Shopify's "This store is unavailable", including the home page and /pages/stores. A quick search turned up nothing about a closure, so I can't tell whether this is temporary or the store is gone.

## Contradicts the brief

- **Coach:** 136 full-price stores, not "hundreds". There are 172 Coach Outlet stores, 8 of them separate men's outlets at their own space numbers. The locator lists no department-store counters and no stockists.
- **Coach, not returned:**
  - 6 Coach "Coffee Shop" cafés.
  - One Westgate store listed twice at the same address (returned once, per the ruling).
  - 8 directory links whose store page shows only the head-office address (10 Hudson Yards) and no store name: Glendale Galleria, Montebello, Torrance, Christiana Mall, Columbia MD, Columbiana SC, a second Battlefield Mall link, and Opry Mills. These look like closed or moved stores. They are not counted.
- **Strathberry:** no US store of its own (NONE); all its boutiques are in the UK. Of 61 US stockist entries, 6 are online-only and not counted.
- **Smythson:** one US store, on Madison Avenue. The locator lists no US concessions or stockists.
- **Polène:**
  - New York is open. Costa Mesa (South Coast Plaza) is marked "Ouverture prochaine", so its status is opening.
  - I read the page in French because the US site address didn't load.
- **Moynat:** one boutique of its own, at South Coast Plaza. Its New York listing is a Saks counter.

## Method worth checking

- **Coach:** I read all 323 store pages in the directory one at a time, 2.5 seconds apart, with no wall. Coach Outlet stores are `outlet`; all other "Coach …" stores are `own-door`.
- **Coach `venue`:** the store label is used where it names a centre (Westfarms, Woodbury Common, Mall of Georgia). Labels that are a town or street are `street` (Coach Natick, Coach Outlet Lee, Coach Soho). This is a judgement on the label's wording only, and the list is in `build3.py`.
- **Longchamp:**
  - The country-wide query returned 160 US rows. A 122-point sweep of the same endpoint added more, giving 193 in all, 33 of them in Canada or Mexico.
  - Outlet venues keep the locator's "P.O." abbreviation (for example "Desert Hills P.O.") and are not expanded.
- **Mulberry:** the 12 Nordstrom shops count as concessions because they appear on Mulberry's own "Official Stores" list.
- **Goyard Dallas:** "Highland Park Village" appears only in the street address, so `venue` is `street`.
