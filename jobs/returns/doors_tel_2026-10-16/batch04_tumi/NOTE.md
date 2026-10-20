# doors_tel_2026-10-16 · Tumi (rerun) · NOTE

**Returned:** 198 door rows (140 own-door, 58 outlet) and 1 count row. `reconcile.py` came back clean. No cell is empty. This replaces Tumi's `held` row in batch 1.

| Own | Outlet | Concessions | Stockists | Locator rows |
|---|---|---|---|---|
| 140 | 58 | 0 | 482 | 739 |

## How it was read

- Sebastian cleared the "Press & Hold" check in his browser on 20 October. After that, the locator's own FindStores endpoint answered normally.
- The endpoint caps each search at 500 miles. I swept it from 40 ZIP codes plus 3 Honolulu checks, 3 seconds apart, and deduplicated by store ID. That gave 739 rows: 683 in the US and Puerto Rico, 53 in Canada and 3 elsewhere.
- No second check appeared during the sweep.

## Contradicts the brief, or needs a look

- **8 TUMI-named stores the locator types DEALER:** Wellesley, the Venetian, and airport stores at LaGuardia B, Newark A, Tampa, SFO, Midway and Reagan National. Under the dealer rule they are own doors, with `operator` = "dealer (not named)" because the locator doesn't name the dealer.
- **2 RETAIL-typed stores named "TUMI Outlet Store":** Castle Rock and Palm Beach Outlets. Both are returned as `outlet`, with a note.
- **Not returned:**
  - Faneuil Hall, labelled "Permanently Closing 7/24"; that date has passed.
  - The TUMI Web Store warehouse in Vidalia, GA.
  - A LaGuardia Terminal C dealer store marked CLOSED.
- **Touro Luggage at Phipps Plaza:** the locator types it RETAIL, but it trades under Touro's name, so it is counted as a stockist.
- **Stockists:** all US dealer rows are listed under the retailer's own name (Nordstrom 110, Dillard's 72, Neiman Marcus 36, Von Maur 34, Macy's 29, Bloomingdale's 28, Saks 28, plus luggage shops). So they are stockists, not concessions.
- **Airport stores:** 30 rows are airport stores: 24 the locator types RETAIL, and 6 of the 8 dealer-run stores above. `venue` is the airport.
- **`venue`:** the store label is used where it names a centre or airport. Town and street labels are `street` (Brickell, Greenwich, Soho, 575 Madison Ave.).
