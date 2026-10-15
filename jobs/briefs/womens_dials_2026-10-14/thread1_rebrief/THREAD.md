# Thread 1 of 4 — womens_dials_2026-10-14 — REISSUE (batches 4–5 only)

This is a re-issue of the thread 1 pack. The original thread was lost after returning batches 1–3.
**Batches 1, 2 and 3 are already returned and merged. Do not redo them.**

You hold **batches 4 and 5** (20 brands, in `worklist.csv`; `canonical_keys.txt` has only those 20 names).
Work them in batch order and return each as `batch04/` and `batch05/`, each with `return.csv`,
`return_styles.csv` and `NOTE.md`. Read `BRIEF.md` for the job; the other three threads have finished,
so there is nothing to coordinate. Run `python3 reconcile.py` before each return.

## Defaults the earlier batches settled (keep them)

- Own labels only. Stocked third-party brands on a house's site are dropped. Co-branded collabs sold
  under the brand's own name are kept and tagged in `lines`.
- Sleepwear and swim are excluded from the style table; denim counts as a garment.
- 80-style sample per house, read on the brand's own US store, women's only.
- `partial` status means at least one cell is `NC`; name the cells in `note`.
- Shares are of all styles in the table, including those with no composition (ND rows); say in
  `NOTE.md` which brands are understated because of ND.

## Standing instructions added since the first issue

1. **Wrong `_sold` flags in the worklist.** Where the worklist says `no` but the brand does sell the
   garment, fill the listing link anyway rather than filing `NONE`, and say in `note` that the worklist
   was wrong. The reverse too: where it says `yes` and the brand does not sell it, file `NONE` and say so.
2. **Lyocell is separate from other cellulosics.** In `return_styles.csv` keep lyocell/TENCEL as its own
   fibre name, never folded into viscose or "cellulosic". The merge splits lyocell from viscose/modal/cupro.
3. **Silk stays a fabric dial** (`fab_silk`), read like the others.
4. **Unisex listings** (a women's store that lists a unisex garment, or a brand whose women's section
   is thin and the rest is unisex): read them, count them, and flag `unisex` in `note` — not `NC`.
5. **Leather, suede, nappa, lambskin, calf hair and ponyhair are never the outerwear high**; faux is fine.
   This matters only if you touch prices; the main read here is links, fibre, tech and craft.
6. **Never work around a bot wall.** File `held` with the wall named in `note` and move on.

## The 20 brands

Batch 4: SKIMS, 7 For All Mankind, EDIKTED, Rip Curl, St. John, Beyond Yoga, Cotopaxi, Maje, Max Mara, Splendid.
Batch 5: Anine Bing, True Religion, Under Armour, Vilebrequin, Ganni, Hill House Home, NIC+ZOE, Lafayette 148, Roller Rabbit, STAUD.

Cotopaxi, Rip Curl, Under Armour and Vilebrequin are crossovers with men's lines: read the women's
section only. Hill House Home: the Nap Dress range counts as dresses; home goods are not styles.
