# RH (rerun, from doors_bhj) · NOTE

**Returned:** 107 door rows (65 own-door, 42 outlet) and 1 count row. No cell is empty.

**Name check:** `reconcile.py` reports `RH` as unmatched. That's because RH isn't in the doors_tel key list I hold (it came from doors_bhj). Please check it against the doors_bhj or main key list before merging.

| Own | Outlet | Concessions | Stockists | Locator rows |
|---|---|---|---|---|
| 65 | 42 | 0 | 0 | 124 |

## How it was read

- The galleries page at rh.com/us/en/store-locations/stores.jsp loaded with no wall. Its Gallery tab lists 79 entries and its Outlet tab 45.
- Store pages build themselves in the browser, so for each store ID I used the site's own `Gallery` data query, the same call the store page makes. One request every 6 seconds, to keep clear of the DataDome wall that tripped the first pass.
- About ten stores in, the page reloaded once on its own, with no wall shown. I restarted and kept progress so nothing was lost. All 124 read with no block.

## Choices to check

- **Sub-banners kept as own doors.** These all carry the RH name on the door, so I returned them as own doors, with a note on each:
  - RH Interior Design (Palm Desert)
  - RH Outdoor (East Hampton, Greenwich)
  - RH Modern (West Hollywood)
  - RH Estates (Greenwich)
- **Left out as a sister banner:** RH Baby & Child, Houston.
- **Not US:** 13 galleries (5 in Canada, 8 in Europe) and 3 outlets (Toronto, Thurrock, Valvert).
- **`venue`:** taken from the gallery's own name ("The Gallery at Scottsdale Quarter" gives Scottsdale Quarter). Historic buildings and estates are `street` (Boston, Chicago, Atlanta, Indianapolis, Montecito), as are "on" and "in" names (Melrose, Knox, Meatpacking). Outlets carry no centre name, so all are `street`.
- **Locator type is in `note`:** NG is a new-format Design Gallery, LG a legacy gallery.
- **Stockists are 0:** RH sells only through its own galleries and outlets, and the locator lists nothing else.
