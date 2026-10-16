# doors_bhj_2026-10-16 · batch 3 · 16 Oct 2026 (revised)

**Rulings applied (16 Oct).** The Arhaus Loft stores stay own-door. RH Interior Design Palm Desert is own-door. Aurate stays `NC`, with the note saying the site has no store finder. RH is still held; see batch 4 NOTE.

Batch 3 is the last five fine-jewelry brands and the first five home brands. `reconcile.py` returned 10 exact matches, 0 rewrites and 0 unmatched. For every brand except RH (held, see below), the rows in `return_doors.csv` match its counts in `return_counts.csv`. No cell is empty, and no two stores of the same brand share a street and ZIP.

| Brand | Own | Outlet | Concession | Stockists | Locator rows |
|---|---|---|---|---|---|
| Brilliant Earth | 44 | 0 | 0 | 0 | 44 |
| Blue Nile | 23 | 0 | 0 | 0 | 23 |
| Aurate | NC | NC | NC | NC | NC |
| Jennifer Fisher | 3 | 0 | 0 | 122 | 3 |
| Roxanne Assoulin | 2 | 0 | 0 | NC | 2 |
| RH | **held** (7 rows returned) | NC | 0 | NC | 66 |
| Arhaus | 109 | 0 | 0 | 0 | 109 |
| Crate & Barrel | 73 | 14 | 0 | 0 | 88 |
| CB2 | 23 | 1 | 0 | 0 | 24 |
| Pottery Barn | 158 | 18 | 0 | 0 | 177 |
| **Total rows** | | | | | 475 |

## What was checked

- **Brilliant Earth and Blue Nile** are all showrooms. Neither locator says appointment-only: Brilliant Earth "encourages appointments" and takes walk-ins. So no row is flagged "by appointment".
- **Crate & Barrel and CB2** were read state by state under the "U.S. Stores" filter, then the "Outlet Stores" filter. Crate&Kids, Canada, warehouse and franchise types are separate filters and were not read.
- **Pottery Barn** was read from the full list of US store links on its locator page (177). Each store's address and phone came from that store's own page. That gets past the "nearest 3 stores" view the locator opens with.
- **`venue`** comes only from the locator:
  - RH: the "The Gallery at …" line.
  - Crate & Barrel, Pottery Barn and Arhaus: the locator's store label, which is mostly the centre name.
  - Blue Nile: the showroom label.
  - Everything else is `street`.

## What was not reached, or is weak

- **RH is held at a bot wall.** After 7 of the 66 US gallery pages, rh.com showed a "Verify you're human" slider. I opened those pages quickly one after another, and that probably tripped it. I didn't try to get round it.
  - The 7 galleries already read are returned: Birmingham, Scottsdale, Marin, Los Gatos, Newport Beach, Palo Alto, and Palm Desert RH Interior Design.
  - RH counts are `NC`, and the Outlet tab wasn't reached.
- **Aurate is `NC`.** The site has no store locator: /pages/stores and /pages/locations redirect to the homepage, and no store link appears in the header, nav or footer. That may mean the stores have closed, but `NONE` would assert it, and the brand's own site doesn't say so.
- **Jennifer Fisher stockists (122)** may include a handful of non-US doors. Roxanne Assoulin's stockist page names 11 retailer banners, not doors, so its stockists are `NC`.
- **Kids and teen banners, not counted:**
  - Pottery Barn Kids: 38 US stores on its own locator.
  - Pottery Barn Teen: 10.
  - RH Baby & Child: 1 (Houston, on the RH list).
  - Crate&Kids: not read (`NC`).

## What contradicts the existing record or the brief

- **RH Interior Design, Palm Desert** is on RH's gallery list but is a design studio, not a gallery. It's returned as own-door and flagged; please rule. RH Outdoor (Greenwich, East Hampton) is on the list too, but those pages sit behind the wall.
- **Arhaus "The Loft" (9 stores)** looks like a clearance or outlet format by name, but the locator doesn't label it outlet, so those 9 are own-door with a note. Say if you want them moved to `outlet`. The 8 "Design Studio" stores are own doors.
- **Pottery Barn** lists one store in Puerto Rico (Mall of San Juan), returned with a note. It also lists "Franchise Relianc", a logistics address with phone "0", which is not returned.
- **Crate & Barrel** lists a Lancaster outlet labelled "Closed", which is not returned. It labels the Canton outlet "Now Open"; that one is returned as open.
- **Crate & Barrel has two Pasadena stores** (Pasadena and Pasadena Homestore) at different addresses that share a phone number. Both rows say so.
- **CB2's Naperville outlet** sits at the same street address as the Crate & Barrel Naperville outlet. They're different brands, so both are returned, with a note.
- **Your own centres turn up:**
  - Pottery Barn lists Derby Street, The Street Chestnut Hill and MarketStreet Lynnfield.
  - Crate & Barrel lists Derby Street Shoppes.
  - Brilliant Earth lists Chestnut Hill (27 Boylston St).

## Decision needed

**RH bot wall:** will you clear the slider on rh.com yourself? If you do, I'll read the remaining 59 gallery pages and the Outlet tab at a slower pace. If not, RH stays held, with the 7 rows filed.
