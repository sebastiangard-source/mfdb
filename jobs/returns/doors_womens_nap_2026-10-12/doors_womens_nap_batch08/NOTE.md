# doors_womens_nap_2026-10-12 — Part 1, batch 8 (last of Part 1)

**Worklist rows 71–73. Read 13 Oct 2026 in Chrome. `reconcile.py`: 3 exact, 0 to rewrite, 0 unmatched. No empty cells in any of the three files.**

## Result

| Brand | US own doors | US concessions | Notes |
|---|---|---|---|
| Paris Texas | 0 | 0 | 1 boutique, Milan (Via Verri 4); 21 US stockists |
| Roger Vivier | 3: South Coast Plaza; 650 Madison Ave; Bal Harbour Shops | 1: Bloomingdale's 59th St | 104 boutiques worldwide |
| Sorel | `NC` | `NC` | locator behind a bot check |

## Where the brief would give a confident wrong answer

1. **Sorel is `NC`, not 0.** sorel.com/stores shows a "Press & Hold to confirm you are a human" check. It was not attempted, so nobody could look. Sorel needs a read by hand.
2. **Roger Vivier's Bloomingdale's is a concession.** The brand's own list names it "Bloomingdale's Roger Vivier". It is counted as a concession and kept out of `us_own_stores`. The Madison Avenue entry gives two ZIPs (10022 and 10012); the street line's 10022 is used, and the row is flagged.
3. **The Paris Texas domain is a trap.** paristexas.com is the Paris, Texas Chamber of Commerce, and paris-texas.com is parked. The brand is at us.paristexasbrand.com, reached through paristexas.it. Its store-locator page is empty (heading only); the retailers sit on a separate stockists page.

## Wrong or unreachable sites

One was added to `wrong_sites.csv`:

- Paris Texas: `paristexas.com` and `paris-texas.com` are not the brand. The brand's site is `us.paristexasbrand.com`.

## Files

- `return_counts.csv`: 3 rows
- `return_doors.csv`: 4 rows (3 own doors, 1 concession)
- `return_stockists.csv`: 21 rows
