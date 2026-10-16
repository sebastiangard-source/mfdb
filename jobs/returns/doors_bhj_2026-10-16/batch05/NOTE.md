# doors_bhj_2026-10-16 · batch 5 · 16 Oct 2026

Batch 5 is the beauty and fragrance stores: Sephora, Ulta Beauty, Bluemercury, Space NK, Le Labo, Diptyque, Byredo, Jo Malone London and Maison Francis Kurkdjian. B&B Italia, also listed under batch 5 on the worklist, went back in batch 4.

`reconcile.py` returned 9 exact matches, 0 rewrites and 0 unmatched. For every brand, the rows in `return_doors.csv` match its counts. No cell is empty.

| Brand | Own | Outlet | Concession | Stockists | US locator rows |
|---|---|---|---|---|---|
| Sephora | 667 | 0 | 1,146 (Kohl's) | 0 | 1,818 |
| Ulta Beauty | 1,558 | 0 | 0 | 0 | 1,558 |
| Bluemercury | 168 | 0 | 0 | 0 | 168 |
| Space NK | **NONE** | 0 | 0 | 0 | 0 |
| Le Labo | 47 | 0 | 0 | 77 | 124 |
| Diptyque | 36 | 0 | 0 | NC | 36 |
| Byredo | 12 | 0 | 73 | 18 | 103 |
| Jo Malone London | 55 rows (about 35 stores) | 0 | 0 | 896 | 989 |
| Maison Francis Kurkdjian | 1 | 0 | 0 | 93 | 94 |
| **Total rows** | | | | | 3,763 |

## Pace and walls

**No bot wall or check box appeared on any site.** Store pages were opened one at a time, never in parallel. The Sephora, Diptyque and Byredo page reads were spaced; the Byredo store-type check and the Jo Malone searches ran back to back.

## The big chains

- **Sephora.** The store list links every store, so no state paging was needed. Each of the 672 US entries was opened for street, ZIP and phone.
  - **5 entries are not stores**, so they aren't returned: Odc (Avon IN), Pdc (Perryman MD), Sdc (Olive Branch MS), Wdc (North Las Vegas NV) and Udc (Salt Lake City UT). Four of them link to no store page. Their names read as distribution centres.
  - **Sephora at Kohl's:** the list names all 1,146 one by one, so they are returned as concession rows, with operator Kohl's. I didn't open their 1,146 pages, so street, ZIP and phone are NC; city, state and the locator's label are filled. Say if you want the addresses; that's about 20 more minutes of paced reading.
  - 374 Sephora rows carry ZIP+4, because that's how their store pages give it.
- **Ulta Beauty.** The directory lists 1,558 stores (1,552 plus 6 on a newer page format), and the row count matches it exactly.
  - **Street, ZIP and phone are NC on every row.** Ulta's store pages are drawn by script, so there's no address in the page.
  - The rows carry city, state, store number and the locator's centre label, which is used as `venue`. Where the label isn't a centre name (for example "Ulta Beauty", "0", or "LAKE GROVE #55"), `venue` is NC.
- **Ulta Beauty at Target:** there are no Target entries anywhere on Ulta's own directory, so concessions are 0, as you asked.

## Calls made

- **Byredo.** Each store page has a "Store type" field, and I followed it:
  - 12 "Byredo Store" are own doors.
  - 73 "Department Store" are BYREDO counters at Nordstrom, Neiman Marcus, Saks, Bloomingdale's and Bergdorf Goodman. They're returned as concessions, with the store in `venue` and `operator`.
  - 18 "Reseller", all Cos Bar, are stockists.
  - Three Department Store entries carry the store's name without BYREDO: US Atlanta Bloomingdales, US Atlanta Neiman Marcus and US LA Nordstrom Americana. I kept them as concessions because their type is the same. Under your batch-1 ruling, a department-store door under the store's own name is a stockist, so say if you'd rather move them.
- **Jo Malone London:** the opposite case. Its department-store doors are listed under the store's own name ("Nordstrom", "Saks Fifth Avenue", and so on), so under your ruling they count as stockists, not rows. There are about 350 of them.
  - The brief's beauty rule names Jo Malone as a brand whose counters are concessions. If you want them as concession rows instead, I can return them from data already read.
- **Jo Malone London duplicates.** The 55 Jo Malone-named rows describe about 35 stores, because the locator lists many stores two or three times under different door IDs.
  - Every such row says so in `note`, with the other door IDs.
  - **`us_own_stores` is 55, to match the rows.** The distinct count is in the note.
- **Maison Francis Kurkdjian:** only one US store carries the brand's name, the Tysons Galleria Boutique in McLean. Everything else on its locator is a retailer.
- **Space NK is `NONE`.** Its US site's store page lists only UK and Ireland stores.
- **Le Labo (added after your link).** The locator waits for the browser's location before it loads anything, which is why it sat on "loading". Without a location it falls back to one request that lists every store, and I read that. It has 124 US entries: 47 Le Labo stores (own doors, including the Nolita Annex) and 77 retailers under their own names (stockists). Le Labo Boston Seaport (70 Pier 4 Blvd) is among the own doors.

## Weak spots

- **Byredo's city counts add up to 110, but there are 103 stores.** The Los Angeles group (11) repeats stores filed under Beverly Hills, Glendale and West Hollywood, and the New York group does the same.
- **Typos are filed as the locator gives them, with a note:**
  - Byredo: "Belleveue". "King of Pussia" is given with state VA, but the ZIP is PA's.
  - Jo Malone London: "Big River Road", against "Big Beaver Road" on its twin entry.
- **Diptyque stockists are NC.** Its finder shows boutiques only.
- **MFK's locator shows no store west of Texas.** That's what it returns from any search point, Los Angeles included.

## Your centres

- **Sephora:** Chestnut Hill (199 Boylston St), Dedham (Legacy Place), Hingham (Derby Street) and Lynnfield (Market St).
- **Bluemercury:** Chestnut Hill (The Street), Legacy Place, Derby Street Shops and Lynnfield MarketStreet.
- **Newbury Street, Boston:** Diptyque (123) and BYREDO (139 B).
- **Jo Malone London** has no Massachusetts own door.

## RH

Left held as you said, with the 7 galleries already filed in batch 3. Nothing more was read from rh.com.
