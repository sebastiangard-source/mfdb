# doors_bhj_2026-10-16 · batch 1 (pilot, revised) · 16 Oct 2026

**Second revision (venues and same-address flags).** `venue` now comes only from the locator. Venues I had worked out from street addresses were reset to `street` for Cartier, Bulgari, Van Cleef, Graff, David Yurman, Chopard, Piaget and Boucheron (84 rows changed in total). Where a store name has the form "City - Label", `venue` now holds the label exactly as written. For concessions, `venue` is the host store as named on the locator, for example "Neiman Marcus" or "Saks Fifth Avenue". Boucheron Miami Bal Harbour and Boucheron Saks Bal Harbour share a street address and ZIP, and both rows now say so in `note`.

**Revised after review.** `return_counts.csv` now has `us_stockists`. Boucheron was re-read: the boutique count goes from 3 to 4, and 4 Boucheron-named Saks shops are added as concessions. Everything else is unchanged.

Batch 1 is the ten high-jewelry houses. All ten locators were read in Chrome. `reconcile.py` returned 10 exact matches, 0 rewrites and 0 unmatched. For every brand, the rows in `return_doors.csv` match the counts in `return_counts.csv` (own, outlet and concession), and no cell is empty.

| Brand | Own | Outlet | Concession | Locator rows |
|---|---|---|---|---|
| Tiffany & Co. | 85 | 0 | 0 | 87 |
| Cartier | 32 | 0 | 0 | 32 |
| Van Cleef & Arpels | 24 | 0 | 5 | 29 |
| Bulgari | 26 | 0 | 2 | 62 |
| Harry Winston | 12 | 0 | 0 | 12 |
| Graff | 7 | 0 | 4 | 11 |
| Chopard | 3 | 0 | 0 | 58 |
| David Yurman | 49 | 4 | 7 | 60 |
| Boucheron | 4 | 0 | 4 | 14 |
| Piaget | 5 | 0 | 2 | 26 |
| **Total** | **247** | **4** | **24** | 275 door rows |

## What was checked

Only the brand's own US locator was used for each brand; `return_counts.csv` gives the read method. No bot walls were hit. Cookie banners were answered with the most restrictive choice ("technical only" or "reject all"). The map was not touched, except at Boucheron, where the locator shows results only through a map-driven list (see below).

## What was not reached, or is weak

- **Boucheron** (rechecked on review): the default map view hid the New York Madison Avenue boutique. The page carries every US store record, so all 14 were read from that and checked against searches centred on New York, Los Angeles and Miami. The result is 4 boutiques, 4 'Boucheron Saks' shops (concessions) and 6 stockists. The Bal Harbour boutique has no phone in its record.
- **Van Cleef & Arpels, Aspen**: the store is listed, but its detail page renders empty. The row has the street name from the store name, with zip and phone `NC`.
- **Bulgari, address line 2 dropped.** Bulgari's pages carry a "nearby stores" panel that uses the same CSS classes. Line 2 values repeated across unrelated stores (for example "Suite 2220" and "Suite 131A"), so they were not trustworthy. Line 1, which usually holds the suite, was kept.
- **Bulgari phones**: two rows have phones that the locator itself duplicates (Palm Beach shares a number with two retailers, and Aventura shares Bal Harbour's). Both are flagged in `note`.
- **Stockists** are now in `us_stockists`. Harry Winston and David Yurman are `NC`, because their retailer layers were not counted.

## What contradicts the existing record or the brief

- **The brief's examples of concessions don't all show up on the locators.** It names "Cartier and Van Cleef inside Saks or Neiman Marcus" and "David Yurman inside Nordstrom".
  - Cartier's US directory lists no shop-in-shops at all, so Cartier shows 0 concessions as listed. That means not listed, not absent.
  - Van Cleef & Arpels does list its 5 Neiman Marcus boutiques, and David Yurman lists one inside Nordstrom.
- **Department-store doors with no brand name.** Bulgari, Chopard and Piaget list Saks, Neiman Marcus and Bloomingdale's doors as "official retailers", under the store's own name. I treated these as **stockists** (counted in the note, not returned), because they don't carry the brand's name. Only doors the locator names as the brand's boutique (for example "BVLGARI Neiman Marcus Beverly Hills" or "Piaget Boutique … Saks Fifth Avenue The Vault") are returned as concessions. Say if you want this ruled the other way.
- **Piaget Chicago** is a "Piaget Boutique" run by Burdeen's Jewelry. Under the watch rule it is an own door, with Burdeen's in `operator`.
- **Tiffany's Blue Box Cafe** (2 rows) was left out as a restaurant, by analogy with the RH rule.

## What the brief got wrong, or should change before batch 2

1. **Stockist column**: resolved. `us_stockists` has been added.
2. **"Empty cell is an error" clashes with optional columns.** For street stores, `venue` is set to `street`. Where the brand runs the door, `operator` is `brand`. Where there is nothing to say, `note` is `none`. If you'd rather have these blank, they are easy to strip.
3. **"Flagship"** appears in `note` only where the locator itself says "Flagship" (Tiffany, 6 rows). Nothing is inferred.
4. **Phones** are normalised to `NNN-NNN-NNNN`.
5. **Ulta Beauty inside Target (batch 5).** As far as I know, Target and Ulta announced the partnership would end around August 2026, so those shops may be gone by now. I'll check against Ulta's own locator when I get there, rather than assume.
