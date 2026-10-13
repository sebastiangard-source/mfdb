# doors_womens_nap_2026-10-12 — Part 1, batch 7

**Worklist rows 61–70. Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. No empty cells in any of the three files.**

## Result

Three brands have US doors of their own, 8 doors in all:

| Brand | US doors | Source |
|---|---|---|
| Le Monde Béryl | 1: 23 East 67th St, New York 10065 | lemondeberyl.com/pages/ny-store |
| Loeffler Randall | 4: SoHo and West Village (New York), Charleston, Nashville | loefflerrandall.com/pages/store-info |
| Manolo Blahnik | 3: 717 Madison Ave; Miami (NE 39th St); South Coast Plaza | manoloblahnik.com/us/storelocator |

Six brands come back 0, and LEGRES is `NC` (point 1). No US outlets or concessions in this batch.

| Brand | Own doors on the brand's site | US stockists recorded |
|---|---|---|
| Herbert Levine | none | 10 (8 store, 2 online) |
| Jennifer Chamandi | none | 2 |
| K Jacques St Tropez | 2, Saint-Tropez | stockist page missing |
| LEGRES | `NC` | — |
| Moon Boot | none | none published |
| NEOUS | none | 5 |
| NODALETO | none listed (see point 2) | 3 |

## Where the brief would give a confident wrong answer

1. **LEGRES' site could not be found.**
   - legres.com is a parked domain for sale.
   - legres.fr is the town council of Lègres.
   - Four other guesses do not load.
   - Search returns only retailers.
   - The row is `NC`. Checking the brand's Instagram bio link by hand is the quickest fix.
2. **NODALETO's Miami store has no address.** An undated page says the brand opened "its first retail store in Miami during Art Basel" for "two years". But it gives no address, and Miami is not on the stores list, so the count is 0. If the store is still trading, it would be 1. Check by hand.
3. **Moon Boot has no locator at all.** The US sitemap and footer hold no store or stockist page, so the count is 0, as the brand's site shows.
4. **K Jacques' stockist page is broken.** The nav links to "Nos revendeurs", but the page returns not-found. Only the two Saint-Tropez boutiques could be read.

## Stockist quality: points for the main thread

- **Loeffler Randall:** 224 US rows from its stockist.co feed. The country field is blank on every row, so US is taken from the state and ZIP. Three John Lewis (UK) rows also have a blank country and were left out. Fixed and flagged:
  - a "CD" state
  - a Biloxi row marked "MI" (Mississippi)
  - a Davenport row with an Iowa City ZIP (kept as written)
- **Manolo Blahnik:** 64 US rows from the locator's own store data, with full addresses and phones. Fixed and flagged:
  - Neiman Marcus King of Prussia was written "Philadelphia 09406"
  - Nordstrom Green Hills was marked Texas
  - one "Joseph" row carries a Louisville ZIP
- **Herbert Levine:** lists "KICK PLEASE – Houston", kept as written.

## Wrong or unreachable sites

One was added to `wrong_sites.csv`:

- LEGRES: no brand site found (point 1).

Moon Boot's `/us` returns 404; the US store is at `/en-us`. That is a dead path on the brand's own domain, not a wrong site.

## Files

- `return_counts.csv`: 10 rows
- `return_doors.csv`: 8 rows
- `return_stockists.csv`: 308 rows
