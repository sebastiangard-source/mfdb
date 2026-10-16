# doors_bhj_2026-10-16 · batch 2 · 16 Oct 2026

Batch 2 is the three watch brands and seven fine/demi-fine jewelry brands. All ten locators were read in Chrome. `reconcile.py` returned 10 exact matches, 0 rewrites and 0 unmatched. For every brand, the rows in `return_doors.csv` match its counts in `return_counts.csv`, and no cell is empty. `return_counts.csv` carries the new `us_stockists` column.

| Brand | Own | Outlet | Concession | Stockists | Locator rows |
|---|---|---|---|---|---|
| Rolex | 24 | 0 | 0 | 210 | 234 |
| Omega | 43 | 0 | 0 | 135 | 178 |
| TAG Heuer | 35 | 4 | 0 | 323 | 362 |
| Mejuri | 43 | 0 | 1 | 0 | 44 |
| Catbird | 13 | 0 | 0 | 0 | 13 |
| Monica Vinader | 3 | 0 | 7 | 58 | 68 |
| Missoma | NONE | 0 | 0 | 12 | 12 |
| Gorjana | 149 | 0 | 0 | 0 | 149 |
| Kendra Scott | 174 | 1 | 0 | NC | 197 |
| Ana Luisa | 5 | 0 | 0 | 0 | 5 |
| **Total** | **489** | **5** | **8** | | 502 door rows |

## What was checked

- **Watch brands.** Only stores the locator itself names as a boutique ("ROLEX BOUTIQUE", "OMEGA Boutique", "Boutique TAG Heuer") are rows. Dealers are counted in `us_stockists`. Where a boutique is dealer-run, the dealer is in `operator`:
  - Rolex: all 24 boutiques.
  - Omega: 12 boutiques.
  - TAG Heuer: 10 boutiques ("Operated by …").
- **How each locator was read to the end:**
  - **Omega**'s map lists only what's in view, so all 178 US records were read from the data embedded in the page.
  - **TAG Heuer** was clicked through "Show more" to 39 of 39.
  - **Gorjana**'s numbered list runs to Honolulu (#149), so it isn't capped.
  - **Kendra Scott** was read from its single-page Store Directory, which lists 197 cards. That avoids the nearest-N problem.

## What was not reached, or is weak

- **Kendra Scott `us_stockists` is NC.** "Other retailers" is a separate radius search by zip or state, and I didn't page it.
- **Phone numbers and zips are missing in places** because the list pages don't show them, and I didn't open each store page:
  - Gorjana: no phones.
  - Mejuri: no phones; zips only where the address text had one.
  - Catbird: most zips missing.
  - Monica Vinader and Ana Luisa: no phones.
  
  All of these are `NC`.
- **TAG Heuer gives no state.** I assigned it from the zip, and that is the only derived field in this batch.
- **Omega's locator names have no city** (they're all "OMEGA Boutique"). I appended the city to `store_name` so the rows can be told apart.
- **Omega Denver** is flagged non-corporate, but no dealer is named, so `operator` is `NC`.

## What contradicts the existing record or the brief

- **Missoma is `NONE`.** Every own store on its locator is in the UK. The 12 US entries are all stockists, such as Nordstrom and Saks.
- **Kendra Scott's sister banner.** 6 cards are *Yellow Rose by Kendra Scott*: Dallas West Village (listed twice), Houston Heights, San Antonio Pearl, Nashville 12 South, and Austin South Congress (flagship). Under the sister-banner rule they are a separate brand, not returned here. No filter splits them; they were picked out by name. 16 Kendra Scott cards say "Permanently Closed" and were also not returned. Of the 197 cards, that leaves 175 rows.
- **Monica Vinader** lists 7 Nordstrom shops under "Our stores", separately from 58 Nordstrom doors under "Other stockists". Read as shop-in-shops, the 7 are concessions and the 58 are stockists.
- **Mejuri** lists a Nordstrom (57th St) shop among its own stores; it is returned as a concession.
- **Catbird** lists its "Williamsburg Wedding Annex" as a 13th location, but it is upstairs in the Williamsburg store, at the same address. It is returned as listed, with a note. You may want to merge it.
- **Omega** has 2 stores named "OMEGA BOUTIQUE by …" (GS Gallery Chicago, CD Peacock Oak Brook) that its own data flags `is_boutique=0`. They are included because the rule is the name on the door.
- **Your own centres turn up:**
  - Gorjana lists Seaport, The Street, MarketStreet Lynnfield and Derby Street.
  - Kendra Scott lists Legacy Place and Market Street Lynnfield.
  - Mejuri lists Seaport and Chestnut Hill (27 Boylston St).

## Batch 1 follow-ups (done)

- `us_stockists` has been added to batch 1. The revised `return_counts.csv`, `return_doors.csv` and `NOTE.md` are in `doors_bhj_batch1`.
- **Boucheron recheck changed the count.** The search centred on New York found **Boucheron New York Madison** (747 Madison Ave), which the default map view had hidden. The page holds all 14 US records:
  - 4 boutiques (New York, Las Vegas, Beverly Hills, Bal Harbour).
  - 4 "Boucheron Saks" shops (Houston, New York, Boston, Bal Harbour). The locator types them as retailers, but they carry the Boucheron name, so they are concessions.
  - 6 stockists (Neiman Marcus ×5, Bergdorf Goodman).

## What the brief got wrong, or should change

1. **Venue field: one thing to own up to from batch 1.** In batch 2, `venue` holds only a centre the locator states, or the store label it uses (Gorjana, Mejuri, Kendra Scott, whose labels are mostly centre names). In batch 1, a few venues for Cartier, Bulgari, Van Cleef, Graff and David Yurman were filled from the street address (for example "Cartier Troy" → Somerset Collection) rather than read off the locator. They're right as far as I know, but they aren't locator-sourced. I can blank those to `street` if you want strict provenance.
2. **Rolex dealer names** in `operator` are expanded from the locator's short sub-names: "LONDON" → London Jewelers, "LONG'S" → Long's Jewelers.
3. **Ulta at Target (batch 5), checked early.** Ulta's own store directory and store finder have no "Ulta Beauty at Target" entries today; the word "Target" doesn't appear on either page. Unless that changes by batch 5, Ulta concessions will be 0, with this in the note.
