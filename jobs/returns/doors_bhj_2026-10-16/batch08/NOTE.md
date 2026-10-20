# doors_bhj_2026-10-16 · batch 8 · 20 Oct 2026

Batch 8 is the last two makeup brands, NARS and Fenty Beauty. It's read on 20 October, so `captured_on` is 2026-10-20 for these rows.

`reconcile.py` returned 2 exact matches, 0 rewrites and 0 unmatched. For every brand, the rows match its counts. No cell is empty.

| Brand | Own | Concession | Stockists | US locator rows |
|---|---|---|---|---|
| NARS | 2 | 0 | 1,360 | 1,362 |
| Fenty Beauty | **NONE** | 0 | NC | 0 |
| **Total rows** | | | | 2 |

## Calls made

- **NARS:** the locator marks 2 entries as NARS boutiques: Houston (4444 Westheimer Road) and Paramus (Garden State Plaza). Each has its own local page.
  - Its counters are listed under the retailer's own name, so they're stockists, as you ruled: Ulta 630, Sephora 356, department stores 272 and 102 others.
  - One Bluemercury entry in Raleigh carries the same flag as the boutiques, but it's a Bluemercury store, so it's counted as a stockist.
- **Fenty Beauty is `NONE`, as you expected.** The site has no store finder, and none of the usual locator pages exists. It names no store of its own.
  - Its retailers aren't listed on the site, so stockists are `NC`.

## Pace and walls

**No bot wall appeared.** Each brand was read with a single search request plus page checks.

## That's the worklist

All 72 brands are now returned across batches 1–8. Two questions are still open:

- **MAC and Charlotte Tilbury counters (batch 7):** do you want them returned as rows?
- **RH (batch 3):** it stays held, with 7 galleries filed.
