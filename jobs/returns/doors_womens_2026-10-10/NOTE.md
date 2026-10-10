# doors_womens_2026-10-10 — all 36 brands, return note

Combined return for all four batches, rebuilt 10 October 2026 after your rulings.

- **Files.**
  - `return_doors.csv`: 4,422 rows.
  - `return_counts.csv`: 36 rows, in worklist order.
  - `out_of_scope_doors.csv`: 166 rows.
- **Totals.** 3,688 own doors, 518 outlets and 150 concessions are counted. There are also 63 counter rows and 3 pop-up rows; these are kept in the file and counted nowhere.
- **Checks.**
  - `reconcile.py`: 36 of 36 names match exactly.
  - No row has an empty cell.
  - Every ZIP has 5 digits or is NC, and every state has 2 letters.
  - Each brand's door rows plus out-of-scope rows equal the US rows read from its locator.
- **Where the rulings stand.** The rulings below replace the "Decisions to rule on" sections in the four batch notes that follow. Where a batch note disagrees with this section, this section is right.

## Rulings applied, 10 October

1. **Department-store listings are now counters: 63 rows.** These rows have `format` = counter, are counted nowhere and are kept in `return_doors.csv`. The store group is in `operator`.

   | Brand | Rows |
   |---|---|
   | Maje | 34 |
   | Eileen Fisher | 19 |
   | Max Mara | 7 |
   | Ganni | 2 |
   | Tory Burch | 1 |

   - **Tory Burch.** The extra row is Macy's Herald Square. It is "Coming Soon", has `status` = opening, and was a concession in batch 3. It is the 63rd row; your count of 62 left it out.
   - **Max Mara and Ganni.** I opened their store pages and found no shop-in-shop, boutique or corner wording.
   - **Concessions left.** The only concessions now in the return are the 150 Aerie locations inside American Eagle, as you ruled.
2. **Outlet by location: 113 doors switched to `format` = outlet.** Each has `note` = "outlet by location".

   | Brand | Doors |
   |---|---|
   | Aerie | 54 |
   | White House Black Market | 37 |
   | Athleta | 6 |
   | Soma | 5 |
   | Aritzia | 3 |
   | Tory Burch | 3 |
   | Anine Bing | 2 |
   | Ganni | 2 |
   | LoveShackFancy | 1 |

   - **111 by the flag.** These are the doors the batch notes flagged as sitting in an outlet centre.
     - The White House Black Market flag covers 37 doors. Batch 1 said 36, which was a miscount.
     - The 2 Ganni doors are the GANNI Postmodern stores.
   - **2 found on a sweep.** Neither had been flagged: Soma Ellenton (Ellenton Premium Outlets) and Aerie at Woodbury Common.
3. **Set-aside groups.**
   - **Kept in `out_of_scope_doors.csv` as candidate keys for the women's map.** They are not rows under the parent brand.

     | Group | Rows |
     |---|---|
     | Maeve | 3 |
     | FP Movement | 99 |
     | Free-est | 4 |
     | OFFLINE by Aerie | 44 standalone stores, plus 5 American Eagle stores that carry OFFLINE |

   - **Lilly Pulitzer Signature Stores.** The 43 stores are now own doors, with `operator` = "independently owned Signature Store". Lilly now has 114 own doors and no outlets.
   - **Roller Rabbit's The General Store by RR (Nantucket).** It is now an own door, with `note` = "multi-brand shop under the brand's name".
   - **Max Mara's 5 records that appear only in the locator data.** They stay out of scope and are not counted. One of them, Aventura, is a Bloomingdale's listing and was recoded to counter there as well.
4. **Unchanged, as you confirmed.**
   - Equipment and Joie stay NC.
   - DVF stays at 1 row.
   - Puerto Rico rows stay in.
   - J.Jill and Lilly show no outlets.

## Still open (small)

- **"Mills" malls.** Seven Aerie doors in Simon "Mills" centres stay own doors: Katy, Gurnee, Arundel, Potomac, Concord, Ontario and Opry Mills. A Grapevine Mills location is an AE & Aerie concession. These centres mix outlet and full-price stores, and the locator does not say which these are. Earlier flags had placed the Sawgrass Mills doors (Aritzia, Anine Bing) and Tory Burch Opry Mills in outlet centres, so those were switched. That leaves Tory Burch Opry Mills as an outlet and Aerie Opry Mills as an own door, which is inconsistent. If every "Mills" centre counts as an outlet centre, the 7 Aerie doors move as well.
- **Tory Burch "Mebane Pop Up".** It sits in Tanger Outlets Mebane and is kept as a pop-up. The locator calls it a pop-up, and the outlet-centre rule addresses stores, not pop-ups.
- **"American Eagle & Aerie" locations in outlet centres.** These stay concessions under the AE ruling. They were not switched to outlets.
- **Max Mara Bloomingdale's "studio" and "cube" records.** The 3 records are in the out-of-scope file and stay concessions there, because "studio" and "cube" read as signs of a branded shop. They are not counted either way.
- **Wolford Wynn Plaza.** It is not in an outlet centre, so it is not switched, even though its store ID is from Wolford's outlet series. It stays flagged.

---

# doors_womens_2026-10-10 — return note

Batch 1 of 4 (worklist rows 1–10). Captured 10 October 2026 in Chrome. Files: `return_doors.csv`,
`return_counts.csv`, and `out_of_scope_doors.csv` (protocol rule 5: recorded, not discarded).

## What was read

| Brand | Locator read | US rows | Own | Outlet | How the list was made complete |
|---|---|---|---|---|---|
| Anthropologie | full store list in the page state | 228 | 223 | 2 | one list, filtered to US; 3 Maeve doors set aside |
| Free People | full store list in the page state | 271 | 168 | 0 | one list; 103 FP Movement / Free-est doors set aside |
| Evereve | state directory, then each store page | 113 | 113 | 0 | directory says 113; 113 read |
| Aritzia | full boutique list in the page state | 83 | 81 | 2 | one list, filtered to US |
| Talbots | "View All Stores", then each store page for the street | 438 | 351 | 87 | cross-checked against "View All Outlets" (none missing) |
| LOFT | "LOFT Stores" and "LOFT Outlet Stores" directories, then each store page | 492 | 358 | 134 | directory headers say 358 and 134 |
| Chico's | radius-search JSON swept on an 88-point grid | 540 | 441 | 99 | endpoint caps at 500 per call; no call above 186; second sweep at a wider radius gave the same 540 |
| J.Jill | Brandify full list | 257 | 257 | 0 | full list and a 5,000-mile search agree, same IDs |
| White House Black Market | radius-search JSON swept as for Chico's | 311 | 311 | 0 | two sweeps, 311 both times |
| Altar'd State | store-search JSON at a 5,000-mile radius from 12 points | 116 | 116 | 0 | every continental query returned the same 116 |

No concessions appear in any of these ten locators. None of them lists department-store counters.

## Decisions to rule on (as sent; ruled 10 Oct, see top)

1. **Sub-banners went to `out_of_scope_doors.csv` and are not counted.** These are the 3 Maeve doors in the Anthropologie
   locator, plus 99 FP Movement and 4 Free-est doors in the Free People locator. I applied the rule that the brand's name
   must be on the door. FP Movement is the hard case: "FP" stands for Free People, and the brand runs it as an extension
   of itself. If you rule it in, the 99 rows are already in the right schema to move across.
2. **Outlet means the locator says outlet.** At White House Black Market the locator never separates outlets. 36 doors
   sit in outlet centres (Premium Outlets, Tanger and similar). They are counted as own doors, with a flag in `note`.
   I did the same for 3 Aritzia doors in outlet centres that the locator does not call outlets. If outlet-centre
   location should be enough to make a door an outlet, filter on that `note`.
3. **J.Jill shows no outlets.** The brief lists J.Jill among the large outlet estates. The locator's own outlet field
   is 0 for all 257 stores, and no store is named an outlet. So either the outlets are not on the locator, or the
   brief is out of date.
4. **Altar'd State lists Kids and "AS Revival" shops as separate stores.** That is 4 of each, some in the same mall
   as a main store. One "AS Revival" record at Jordan Creek has the same suite as the main store. I kept them all as
   own doors and flagged them, because the Altar'd State name is on the door.

## Data the locators got wrong (kept as written, flagged in `note`)

- **Aritzia:** Perimeter Mall's state reads AL, but the address is Atlanta and the ZIP is in Georgia. Kierland's ZIP
  has six digits, so it is left `NC`. Keystone's city is blank, so it reads `not stated`.
- **Anthropologie:** Virginia Beach's state field reads "Virginia Beach", so I used VA. Naples is marked "Closing
  (10/18) & Relocating within Waterside Shops (11/18)".
- **Talbots:**
  - Roosevelt Field Mall has no store page and no street line, so its street reads `not stated by locator`.
  - In 13 cards the address was split across the venue line. I merged those lines.
- **ZIPs missing their leading zero:** 10 at Free People, 5 at Evereve, a few at Chico's and WHBM. I restored the
  zero and noted it on each row.
- **Territories:** Puerto Rico doors appear at Anthropologie (1), Free People (1), Chico's (2) and WHBM (2), plus one
  WHBM door in the US Virgin Islands. They are kept and flagged, so you can drop them if "US" means the 50 states.

## Not reached

- **WHBM venue names:** the store pages started returning 403 after about 260 requests. For 49 WHBM rows, `venue`
  reads `not stated` and the row says why. The addresses come from the locator JSON and are complete.
- **Venue for other brands:** Chico's, J.Jill, LOFT and Altar'd State give no venue field, so `venue` reads
  `not stated`. For J.Jill, LOFT and Evereve the store name usually is the centre's name.

## Checks run

- **Names:** `reconcile.py` matched all 10 exactly (0 rewrites, 0 unmatched).
- **Empty cells:** none.
- **Counts:** every brand's row count equals its US count in the locator.
- **Copying:** rows were copied out of the browser by hand, so every brand was re-read from the live locator and
  checked against the file. The check hashes store ID, street, city and phone (Aritzia: ID, street and phone) on
  both sides and compares them. All 10 brands match, row for row:
  - Anthropologie 228, Free People 271, Aritzia 83, J.Jill 257, WHBM 311, Altar'd State 116 and Chico's 540 match
    in full.
  - LOFT 492 and Evereve 113 match in full after each store page was re-read.
  - Talbots: 437 match. The 438th row is Roosevelt Field, which has no store page and was checked by eye.
  - Free People's one difference is intended. Portland, ME has no phone in the locator, and the file says
    `not listed`.
- **Evereve fetch quirk:** when Evereve store pages are requested in parallel, some come back carrying another
  store's record. On the check read, 14 pages did this. Read one at a time, all 14 match the file. My first read
  flagged Brea Mall as carrying the Naperville record. That was the same artifact, not a locator error. The Brea
  row is correct and its note now says so.

---

# doors_womens_2026-10-10: batch 2 note

This is batch 2 of 4 (worklist rows 11–20). I captured it on 10 October 2026 in Chrome. The files are `return_doors.csv`, `return_counts.csv` and `out_of_scope_doors.csv`. This batch has no out-of-scope rows, so that file holds only its header.

## What was read

| Brand | Locator read | US rows | Own | Outlet | Concession | How the list was made complete |
|---|---|---|---|---|---|---|
| Soma | radius-search JSON (Rio SEO, as Chico's/WHBM), 88-point grid | 259 | 259 | 0 | 0 | two sweeps, 700 and 1,100 km, both 259; largest call 157 (cap 500) |
| Veronica Beard | the locator's Uberall feed, full list | 45 | 45 | 0 | 0 | one call, 52 worldwide |
| Zimmermann | boutique list embedded in the page, plus each boutique page | 35 | 31 | 3 | 0 | 107 worldwide; 35 US + PR; plus 1 pop-up |
| Anine Bing | worldwide store list page, plus each store page for phone | 17 | 17 | 0 | 0 | 34 worldwide under country headings |
| Alice + Olivia | the locator's Storepoint feed, full list | 32 | 32 | 0 | 0 | one call; page says "68 locations found" |
| Maje | SFCC store search, 5,000 mi, plus each store page | 56 | 16 | 6 | 34 | 423 results; repeat from Honolulu found no new US IDs |
| Lafayette 148 | store finder tabs (US Boutiques, US Outlets) | 18 | 12 | 6 | 0 | tabs list every store, no paging |
| STAUD | "Visit Our Stores" page | 12 | 12 | 0 | 0 | single page |
| LoveShackFancy | the locator's Stockist feed, plus each store page for phone | 30 | 29 | 0 | 0 | one call, 32 worldwide; plus 1 pop-up |
| Eileen Fisher | locations.eileenfisher.com/us/ directory, plus each store page | 78 | 52 | 7 | 19 | directory lists every US page |

Several brands' store links from the brief's obvious paths are dead. Each row's `note` and `locator_url` give the working path:

- Zimmermann: /us/store-locator returns 404.
- STAUD and LoveShackFancy: /pages/stores returns 404.
- Eileen Fisher: /stores returns 404.

## Decisions to rule on (as sent; ruled 10 Oct, see top)

1. **Department-store shops returned as concessions (53 rows).**
   - **Where:** Maje (34) and Eileen Fisher (19) list shops inside Bloomingdale's, Saks, Nordstrom, Neiman Marcus and Von Maur in their own locators.
   - **What I did:** I returned these as `format` = concession, with the store group in `operator`.
   - **Why:** the brief says "a shop-in-shop at Nordstrom or Bloomingdale's is a concession", and it also says "department-store counters are not doors". The locator cannot tell a shop-in-shop from a counter.
   - **If you rule them out:** filter `format` = concession. Own and outlet counts are unaffected.
2. **Outlet-format names.**
   - Eileen Fisher's 7 "Company Stores" are counted as outlets and flagged. The locator never uses the word outlet.
   - Lafayette 148's L148 Company Store sits in the locator's own Outlets tab.
3. **Outlet-centre doors the locator does not call outlets.** As in batch 1, these are counted as own doors and flagged:
   - Soma: 4
   - Anine Bing: 2
   - LoveShackFancy: 1 (Woodbury Common)
4. **Pop-ups and seasonal doors.**
   - Zimmermann Palm Beach is named "Pop-up – Boutique Closure", so `format` is pop-up.
   - LoveShackFancy Kansas City is named "Pop-Up", so `format` is pop-up.
   - Kiawah Island's page path says popup, but nothing on its locator does, so it stays an own door and is flagged.
   - Zimmermann Southampton and Alice + Olivia East Hampton are temporarily closed for the season.
5. **Opening.** LoveShackFancy Naples is marked "Coming November 2026", so `status` is opening.

## Data the locators got wrong (kept as written, flagged in `note`)

- **Zimmermann:**
  - The state for Houston reads HI.
  - The city for Plaza del Lago reads CHICAGO, though the address and ZIP are Wilmette.
  - The Boston street line repeats the city and ZIP.
  - Two four-digit ZIPs had the leading zero restored, and one ZIP+4 was cut to five digits.
- **Alice + Olivia:**
  - Six phone numbers have 9 digits.
  - East Hampton has no address at all, so street is `not stated by locator` and ZIP is NC.
- **Soma:** five phone numbers carry a leading 1, and 22 store names read "SOMA".
- **Veronica Beard:** two store-page paths name a different street from the feed address (Chicago, Soho).
- **Lafayette 148:**
  - Three addresses spell the state out in full.
  - NorthPark's phone has a Seattle area code.

## Checks run

- **Names:** `reconcile.py` matched all 20 names so far exactly (0 rewrites, 0 unmatched).
- **Empty cells:** none.
- **Counts:** every brand's row count equals its US count in the locator.
- **Copying:** every brand was re-read from the live locator and compared with the file by hash.
  - Soma, Veronica Beard, Zimmermann, Anine Bing, Alice + Olivia and Maje were checked on store ID, street, city and phone.
  - Eileen Fisher was checked on the whole row.
  - Lafayette 148, STAUD and LoveShackFancy were checked on ZIP and phone, plus street and city where the source has those fields. Their source addresses are free text that I split by hand, and those splits were checked by eye.
  - All 10 brands match.

---

# doors_womens_2026-10-10: batch 3 note

This is batch 3 of 4 (worklist rows 21–30). I captured it on 10 October 2026 in Chrome. The files are `return_doors.csv`, `return_counts.csv` and `out_of_scope_doors.csv`.

## What was read

| Brand | Locator read | US rows | Own | Outlet | Concession | How the list was made complete |
|---|---|---|---|---|---|---|
| Equipment | **no locator on the site** | – | NC | NC | NC | header, footer, About and FAQ read; /stores, /store-locator and /locations all not found |
| Joie | **no locator on the site** | – | NC | NC | NC | as for Equipment; same storefront |
| Diane von Furstenberg | no locator; the footer's "DVF Flagship" page | 1 | 1 | 0 | 0 | the only store page the site links |
| Nili Lotan | Stores page, single list | 8 | 8 | 0 | 0 | single page |
| Tory Burch | US directory, then each of 110 store pages, plus Puerto Rico (1) | 111 | 68 | 41 | 1 | directory lists every page; the JSON feed needs an API key, so it was not used |
| Athleta | state, then city, then store pages | 240 | 240 | 0 | 0 | full crawl |
| Aerie | AE's shared Yext directory, all US and PR pages, filtered by banner | 395 | 244 | 1 | 150 | 1,006 AE/Aerie/OFFLINE records read |
| Brandy Melville | the published store list (locations.brandymelville.com) | 61 | 61 | 0 | 0 | 109 worldwide; the US section was read whole |
| Reformation | stores.html list, then each store page | 64 | 62 + 2 opening | 0 | 0 | the list holds every store |
| Lilly Pulitzer | store-search JSON with the locator's own "Lilly Pulitzer stores" filter | 71 | 71 | 0 | 0 | one call covering all states; "Partner stores" read separately |

## Decisions to rule on (as sent; ruled 10 Oct, see top)

1. **Equipment and Joie are NC, not zero.** Neither site has a store locator or a store page (details in `note`). The two brands share one storefront, whose wholesale contact is an @joie.com address. If they have stores, the source would need to be something other than their own sites, which the brief rules out.
2. **DVF has 1 row.** The site has no locator, only a "DVF Flagship" page (874 Washington Street). This undercounts DVF if other doors exist, but the brief's single-source rule gives nothing more.
3. **Aerie inside American Eagle.**
   - **What I did:** 150 locations named "American Eagle & Aerie", or a variant of that name, are returned as concessions under Aerie, with operator American Eagle. I followed the brief's rule.
   - **What is uncertain:** the locator cannot tell a shop-in-shop from side-by-side doors.
   - **What went to the out-of-scope file:**
     - 44 standalone OFFLINE by Aerie stores (the same sub-banner rule as Maeve and FP Movement in batch 1).
     - 5 American Eagle stores that carry OFFLINE.
     - 3 records named "Aerie - CLOSED".
     - 3 duplicate Aerie records.
4. **Lilly Pulitzer Signature Stores (43 in the US) are in `out_of_scope_doors.csv`** with `format` = partner-store. The locator lists them under its "Partner stores" filter. They are independently owned and trade under their own names (Pink Tangerine, Palm Village and so on), so the Lilly name is not on the door. Department and specialty stockists (53, plus 6 unlabelled partner records) are wholesale and are not returned.
5. **Outlets.**
   - **Tory Burch:** 41 doors are named Outlet.
   - **Tory Burch doors not named outlets:** 3 sit in outlet centres with outlet-series store numbers (Jersey Gardens, Opry Mills, Pleasant Prairie). They are counted as own doors and flagged.
   - **Aerie:** only 1 door is named "Aerie Outlet". 53 Aerie own doors sit in outlet centres and are flagged.
   - **Athleta:** the locator has no outlet type. 6 doors in outlet centres are flagged.
   - **Lilly Pulitzer:** the locator shows no outlets at all, which contradicts the brief's "outlet-heavy" note.
6. **Pop-ups and coming-soon.**
   - Tory Burch "Mebane Pop Up" has `format` pop-up.
   - Tory Burch "Macy's Herald Square - Coming Soon" is a concession with `status` opening.
   - Reformation Corte Madera and Country Club Plaza are COMING SOON with no address.
   - Reformation Scottsdale's page path says pop-up, but nothing on its locator does, so it stays an own door and is flagged.
7. **Lilly Pulitzer inactive records.** 8 records are marked inactive, and every day shows closed. Most are seasonal resort shops. They are returned as temporarily closed and flagged.
8. **Puerto Rico.**
   - Tory Burch lists 1 Puerto Rico door under its own country; it is kept and flagged.
   - Aerie lists 3 Puerto Rico doors under its own country; they are kept and flagged.

## Data the locators got wrong (kept as written, flagged in `note`)

- **Brandy Melville:**
  - The list gives no store names and no ZIPs. ZIP comes from the street line where written (13 rows) and is NC on the other 48.
  - Three rows are filed under a different city than their street line names.
- **Reformation:**
  - Pacific Palisades has no state or ZIP, so the state comes from the list heading.
  - Houston Galleria has no ZIP.
- **Tory Burch:** two pages repeat the suite line. It is written once.
- **Aerie:** one centre (Serramonte) appears once as "Aerie & OFFLINE" and once as "American Eagle & Aerie" at the same address and phone.

## Checks run

- **Names:** `reconcile.py` matched all 30 names so far exactly.
- **Empty cells:** none.
- **Counts:** every brand's row count, plus its out-of-scope rows, equals its US count in the locator.
- **Copying:** every brand was re-read from the live data and compared with the file by hash.
  - Tory Burch, Athleta, Aerie, Reformation and Lilly Pulitzer were checked on whole rows.
  - Brandy Melville was checked on street, city, state and phone.
  - Nili Lotan was checked on ZIP and phone.
  - All match. DVF is one row and was checked by eye.

---

# doors_womens_2026-10-10: batch 4 note

This is batch 4 of 4 (worklist rows 31–36). I captured it on 10 October 2026 in Chrome. The files are `return_doors.csv`, `return_counts.csv` and `out_of_scope_doors.csv`. A combined file covering all 36 brands is delivered alongside.

## What was read

| Brand | Locator read | US rows | Own | Outlet | Concession | How the list was made complete |
|---|---|---|---|---|---|---|
| Ganni | store finder, country group "United States (18)", plus each store page | 18 | 16 | 0 | 2 | group lists every store |
| IRO | US site's stores page, worldwide list ("41 RESULTS") | 3 | 3 | 0 | 0 | single list; radius search returns nothing |
| Roller Rabbit | "Our Stores" page | 13 | 11 | 2 | 0 | single page, with its own "Outlet Stores" heading |
| St. John | store locator with No limit and limit 100 | 32 | 18 | 14 | 0 | 33 entries listed, one of which is the head office |
| Max Mara | store.maxmara.com US directory and its Yext feed | 23 | 16 | 0 | 7 | directory shows 23 US pages, and the feed agrees |
| Wolford | store-search JSON (US), three centres, plus the result cards' categories | 13 | 12 | 1 | 0 | each search returns the same 13 |

## Decisions to rule on (as sent; ruled 10 Oct, see top)

1. **Department-store shops listed as brand stores are returned as concessions** (Ganni 2 Bloomingdale's, Max Mara 7 Bloomingdale's/Saks). This is the same rule as Maje and Eileen Fisher in batch 2.
2. **Max Mara.**
   - Three franchise boutiques (store type NF) are counted as own doors with operator "franchise partner", per the brief's rule on operator-run doors.
   - The locator's feed holds 5 more US Max Mara records that the locator does not publish: 3 Bloomingdale's studios or cubes, Aventura, and a Woodbury outlet. They are in `out_of_scope_doors.csv`.
   - Sister brands in the same feed (Weekend Max Mara, Marina Rinaldi, Marella, MAX&Co., 32 US records) are not returned.
3. **GANNI Postmodern** (the brand's past-season concept, at Woodbury Common and Desert Hills) is counted as own doors, not outlets, because the locator does not call them outlets. They are flagged.
4. **Roller Rabbit's "The General Store by RR"** (Nantucket, a multi-brand concept) is in `out_of_scope_doors.csv`, because the door name is not Roller Rabbit.
5. **Wolford.**
   - 997 Madison Avenue has no category on the locator. It is counted as an own door from its boutique-series store ID.
   - Wynn Plaza is categorised as a boutique but has an outlet-series ID.
   - Both are flagged.
6. **St. John.**
   - The locator app's own configuration reports 34 locations but lists 33: 32 stores plus "St John Knits HQ" (the Anaheim office, not returned). I could not see the 34th record.
   - The locator shows no phone numbers.

## Data the locators got wrong (kept as written, flagged in `note`)

- **Ganni:** most states are written in full. Ala Moana's city reads "Honolulu H".
- **St. John:** the Hilton Head city reads "Bluffon". Boston's ZIP had its leading zero restored.
- **Wolford:**
  - "Columbus Cirlcle" is misspelled.
  - One phone number has 13 digits.
  - The city field mixes city and state.
- **Max Mara:**
  - Cities read "New York 59th Street" and "Ala Moana".
  - Chicago's suite line is written twice.

## Checks run

- **Names:** `reconcile.py` matched all 36 brand names exactly (0 rewrites, 0 unmatched).
- **Empty cells:** none across all four batches.
- **Copying:**
  - Max Mara was hash-checked on whole rows against the live feed.
  - Ganni, IRO, Roller Rabbit, St. John and Wolford are short lists. They were transcribed from the live page output and checked by eye.
