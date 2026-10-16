# doors_bhj_2026-10-16 · batch 1 (pilot) · 16 Oct 2026

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
| Boucheron | 3 | 0 | 0 | 3 |
| Piaget | 5 | 0 | 2 | 26 |
| **Total** | **246** | **4** | **20** | 270 door rows |

## What was checked

Only the brand's own US locator was used for each brand; `return_counts.csv` gives the read method. No bot walls were hit. Cookie banners were answered with the most restrictive choice ("technical only" or "reject all"). The map was not touched, except at Boucheron, where the locator shows results only through a map-driven list (see below).

## What was not reached, or is weak

- **Boucheron**: the count of 3 is what the locator returned with the "Boucheron boutique" filter while the map showed the whole US. No country list page exists, because the "All stores" link loops back to the same locator. Phone numbers sit on detail pages and were not read, so they are `NC`.
- **Van Cleef & Arpels, Aspen**: the store is listed, but its detail page renders empty. The row has the street name from the store name, with zip and phone `NC`.
- **Bulgari, address line 2 dropped.** Bulgari's pages carry a "nearby stores" panel that uses the same CSS classes. Line 2 values repeated across unrelated stores (for example "Suite 2220" and "Suite 131A"), so they were not trustworthy. Line 1, which usually holds the suite, was kept.
- **Bulgari phones**: two rows have phones that the locator itself duplicates (Palm Beach shares a number with two retailers, and Aventura shares Bal Harbour's). Both are flagged in `note`.
- **Stockist counts** for the retailer layers of Harry Winston and David Yurman were not counted.

## What contradicts the existing record or the brief

- **The brief's examples of concessions don't all show up on the locators.** It names "Cartier and Van Cleef inside Saks or Neiman Marcus" and "David Yurman inside Nordstrom".
  - Cartier's US directory lists no shop-in-shops at all, so Cartier shows 0 concessions as listed. That means not listed, not absent.
  - Van Cleef & Arpels does list its 5 Neiman Marcus boutiques, and David Yurman lists one inside Nordstrom.
- **Department-store doors with no brand name.** Bulgari, Chopard and Piaget list Saks, Neiman Marcus and Bloomingdale's doors as "official retailers", under the store's own name. I treated these as **stockists** (counted in the note, not returned), because they don't carry the brand's name. Only doors the locator names as the brand's boutique (for example "BVLGARI Neiman Marcus Beverly Hills" or "Piaget Boutique … Saks Fifth Avenue The Vault") are returned as concessions. Say if you want this ruled the other way.
- **Piaget Chicago** is a "Piaget Boutique" run by Burdeen's Jewelry. Under the watch rule it is an own door, with Burdeen's in `operator`.
- **Tiffany's Blue Box Cafe** (2 rows) was left out as a restaurant, by analogy with the RH rule.

## What the brief got wrong, or should change before batch 2

1. **There is no stockist column.** The brief asks for Rolex, Omega, TAG Heuer and the European furniture houses to count stockists "in `return_counts.csv`", but the template has no column for them. In this batch they are in `note`. Suggest adding `us_stockists` (with `NC` allowed) before batch 2, where Rolex and Omega will have hundreds.
2. **"Empty cell is an error" clashes with optional columns.** For street stores, `venue` is set to `street`. Where the brand runs the door, `operator` is `brand`. Where there is nothing to say, `note` is `none`. If you'd rather have these blank, they are easy to strip.
3. **"Flagship"** appears in `note` only where the locator itself says "Flagship" (Tiffany, 6 rows). Nothing is inferred.
4. **Phones** are normalised to `NNN-NNN-NNNN`.
5. **Ulta Beauty inside Target (batch 5).** As far as I know, Target and Ulta announced the partnership would end around August 2026, so those shops may be gone by now. I'll check against Ulta's own locator when I get there, rather than assume.
