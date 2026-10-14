# prices_womens_2026-10-13: response to the 13 Oct evening reissue

**Batch 1 re-sent** (`prices_womens_batch01/`). Batches 3–16 were already returned in full. All 156 rows are in `prices_womens_ALL_return.csv`, with 0 empty cells, and `reconcile.py` says safe to merge.

## Core-garment rule applied to every Basic reading outside batch 2

| Brand | Batch | Before | After the core-garment check |
|---|---|---|---|
| **GUESS** | 3 | Basic | **Premium**. The core tee passes (plain Crewneck Tee, $29). The core shirt fails: the $69 Cropped shirt was passed over, and the plain Cotton Shirt is $89. It stays Basic only if its $79 Satin shirt is ruled core. |
| EDIKTED | 4 | Basic | Basic stands. It is fast fashion with no core line, and every plain woven button-up is under $80. |
| Rip Curl | 4 | Basic | Basic stands. The core tee is the small-logo tee, and every woven shirt is under $80. |
| Cotopaxi | 4 | Basic, hand-band | Holds on the $65 short-sleeve Perenne shirt, not on the $85 long-sleeve Afuera. Hand-band. |
| O'Neill | 10 | Basic | Basic stands. It sells only two woven shirts, both $58. |
| Hurley | 15 | Basic | Basic stands. |
| Aerie | 1 | Basic, hand-band | Basic stands. |

The core rule can only move a brand out of Basic, never into it. So no Premium or higher reading needed a re-check.

## Lucky Brand precedent

**True Religion** (batch 5) is the one other brand banded on a struck "Regular price". I re-checked it this evening. The tee shows $62 regular and $21.99 sale ("65% OFF"), under "LAST DAY!" and "UP TO 60% OFF SALE" banners. That reads as a dated promotion, not a standing comp-value like Lucky's. It is left at Premium on the regular price and flagged for your ruling. The site then put up a bot check, so its shirt and sweater sale prices could not be read.

## Retry list

- **TOTEME (batch 8): now read in full.** This evening's certificate error has cleared. It proposes **True Luxury**: blouse entry $380 (Signature cotton shirt) plus sweater entry $520 (Fine crew knit) gives a mean of $450.
- **Still `NC`:**
  - LOFT (batch 1) and prAna (batch 9): blocked by the same PerimeterX "press and hold" bot check on category pages.
  - Sam Edelman (batch 9): stuck on the Cloudflare verification screen.

  None of these checks was attempted.

## Files

- `prices_womens_batch01/`: `return.csv` and an updated `NOTE.md`.
- Updated rows in batches 03, 04, 05, 08 (TOTEME), 10 and 15.
- `prices_womens_ALL_return.csv`.
