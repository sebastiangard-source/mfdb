# doors_womens_nap_2026-10-12 — Part 1, batch 5

**Worklist rows 41–50. Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. No empty cells in any of the three files.**

## Result

Four brands have US doors of their own, 10 doors in all:

| Brand | US doors | Source |
|---|---|---|
| Sporty & Rich | 2: 8619 Melrose Ave, Los Angeles; 133 Greene St, New York | sportyandrich.com/pages/flagship-store |
| Still Here | 5: Melrose (LA), West Village, Madison Ave, Nolita, Williamsburg | stillhere.nyc/pages/our-stores |
| The Frankie Shop | 1: 59 Crosby St, New York 10012 | thefrankieshop.com/pages/stores |
| Tibi | 2: 120 Wooster St, New York 10012; 28 Market St, St. Simons Island GA 31522 | tibi.com/pages/stores |

Five brands come back 0. Sportmax is `NC` (point 1). No brand in this batch has a US outlet or concession.

| Brand | Own doors on the brand's site | US stockists recorded |
|---|---|---|
| Solace London | none | none published |
| Sportmax | `NC` | — |
| ST. AGNI | 5, all Australia | 143 (incl. 1 Puerto Rico) |
| The Attico | none | none published |
| Thierry Colson | 1, Paris | 21 |
| Vita Kin | none | 4 (names and places only) |

## Where the brief would give a confident wrong answer

1. **Sportmax's locator can't be reached from the US.** Both locator links on us.sportmax.com redirect to the home page, and every other market URL is sent back to the US site. The row is `NC`, not 0. It needs a read from a non-US connection or by hand.
2. **The Frankie Shop's Lower East Side store is gone from its own site.** The locator link still points to the Lower East Side page, but that page now shows the SoHo address. Only SoHo is counted.
3. **Still Here lists six entries but has five doors.** "The Vintage Room @ Madison" is at the Madison store's address and is not counted separately.
4. **Tibi's Vienna studio is not a Tibi door.** It is by appointment and run by partner The Store by Schneeweiss. Tibi's two own stores also appear on its stockist list; they are counted as doors, not stockists.

## Stockist quality: points for the main thread

- **ST. AGNI:** full list read from its stockist.co feed (339 points worldwide). Full addresses with ZIPs.
- **Tibi:** street, city and state, no ZIPs. The page writes Iowa as "IO"; corrected to IA and flagged. An asterisk on the page marks stores that sell Tibi's book; this is kept in `note`.
- **Thierry Colson:** full addresses. One row (Tuckernuck) is a fulfilment warehouse and one (C'est Mimi) is website only; both are flagged.
- **Vita Kin:** names and places only. "The Hamptons" is not a city, so Aerin's city is `NC`.

## Wrong or unreachable sites

One was added to `wrong_sites.csv`:

- ST. AGNI: `stagni.com` is an unrelated accounting firm. The brand's site is `st-agni.com`.

Still Here's `stillherenewyork.com` redirects to `stillhere.nyc`, and Vita Kin's `vitakin.com` to `www.vitakin.com`. Both are the brands' own sites.

## Files

- `return_counts.csv`: 10 rows
- `return_doors.csv`: 10 rows
- `return_stockists.csv`: 230 rows
