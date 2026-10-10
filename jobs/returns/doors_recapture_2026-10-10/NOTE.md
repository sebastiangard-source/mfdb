# Rulings of 10 October: applied

**Clean-up after the rulings (10 Oct, later):**
- **Held rows and borderline concessions:** the 6 held Ralph Lauren rows stay out of every count, and Sandro, James Perse, Buck Mason and Lacoste stay concessions, as you agreed.
- **Batch B0 venues:** batch B0 had filled 50 `venue` cells from addresses rather than locator wording. Those cells are blank now, and each row's note keeps the old value.
- **Kiton and Rag & Bone names:** 9 store names are back to the locator's wording (5 Kiton, 4 Rag & Bone). The helper's bracketed disambiguation has moved to `note`.
- **Ralph Lauren label check:** completed after Sebastian cleared the site's human check. See point 2.


**Files now:** `return_doors.csv` has 5,891 rows. `return_counts.csv` has 142 brands: Ralph Lauren Purple Label and RLX are new. `return_shops.csv`, `out_of_scope.csv` and `spot_check.csv` (new) come with it. `reconcile.py` matched all 142 names exactly, and the rows agree with the counts for every brand.
**Totals now:** 3,611 own stores, 1,441 outlets, 599 concessions, 137 counters (counted nowhere), 55 pop-ups.

1. **One number = own stores.** The split columns are unchanged.
2. **Ralph Lauren flagships.** The rule is "the doors that sell the label", read from each flagship's own store page. All 38 pages were read on 10 Oct; Sebastian cleared the site's human check himself. Each row's note lists the brands its page shows.
   - **Polo Ralph Lauren: 47.** That is 11 Polo stores plus the 36 flagships whose page lists Polo, or shows no brands list (Tampa, Valley Fair: "page showed no brands list"). East Hampton (31-33 Main St) and Miami Design District (170 NE 40th St) list Purple Label Collection only, so they are not under Polo.
   - **Ralph Lauren Purple Label: 23.** All are multi-label flagships whose page lists Purple Label; there is no standalone Purple Label store in the US directory.
   - **RRL: 26.** That is 7 RRL stores plus 19 flagships whose page lists RRL or "Double RL".
   - **RLX: 2.** That is Oak Brook and Troy. The full US directory walk has no RLX-banner store, so the count is 0 + 2.
   - Every flagship row under these keys is flagged "multi-label flagship (banner Ralph Lauren)".
   - **Held, not counted:** 4 flagships listed as closed and 2 Ralph Lauren-banner outlets (agreed 10 Oct).
3. **Counters.** 137 rows were recoded `format` = counter and are counted nowhere: Reiss 102, Givenchy 27, Herno 6, Loewe's Saks entry (the locator types it NON_RETAIL) and a Gucci Saks beauty counter.
   - **Left as concessions, and close to the line:** Sandro (39, typed "Department store" by the brand's locator), James Perse (10 Bloomingdale's entries), Buck Mason (5 "Bloomingdale's location"), and Lacoste (36 Macy's "Corners"). Say if any should go to counter.
4. **Hermès** stays at 41, with partner- and airport-run stores flagged. The note gives 37 for own-run.
5. **Carhartt** stays at 68.
6. **The 7 lookup ZIPs** stay, each noted.
7. **Paul Smith and Thom Browne:** `read_method` now starts "sitemap:", and the note has a confidence line (medium).
8. **Shops:** a new `register_relevance` column. Cove Creek Outfitters = check. Oxford & Derby = keep. The other 31 = not assessed.
9. **Rothy's Paramus** is not in the file; it was never returned. Carhartt Greensboro and Reno are written as their locator writes them.
10. **HUGO:** `out_of_scope.csv` kept.

## Spot check of the helper batches: 20 of 20 pass
- **What was checked:** 18 door rows drawn at random from the B and C helper batches, plus 2 shops. Each was opened in Chrome and the door was confirmed as written. Detail is in `spot_check.csv`.
- **One replacement draw:** the first draw from batch c2 was a Polo outlet at Wrentham. It couldn't be checked because of the Ralph Lauren bot challenge, so it was replaced with another c2 row (Indochino Philadelphia).
- **Batches covered:**
  - c0: 6 (Banana Republic ×4, Burberry, Lacoste)
  - c1: 2 (Celine, Zegna)
  - c2: 2 (Billy Reid, Indochino)
  - g0: 1 (Rag & Bone)
  - g1: 1 (Sid Mashburn)
  - g2: 2 (A.P.C., Versace)
  - g3: 1 (Rothy's)
  - g4: 3 (Faherty, Lululemon ×2)
  - shops: 2
- **No fails.** Two pages, Zegna and Indochino, show no ZIP; the row's ZIP came from the locator's data. The Celine row's opening status matches the page ("opening soon on 6/11/26", i.e. 6 November).
- **Ralph Lauren rows were not re-checked:** the C133x flagship file and the Polo and RRL directory walk are blocked by the same challenge.

---

# doors_recapture_2026-10-10 — NOTE

**Returned:** `return_doors.csv` (5,849 rows), `return_counts.csv` (140 brands), `return_shops.csv` (33 shops), `out_of_scope.csv` (6 HUGO-only doors).
**reconcile.py:** 140 names in, 140 exact, 0 to rewrite, 0 unmatched.
**Cross-check:** for every brand, the open and closed rows in the doors file add up to the own/outlet/concession figures in the counts file. The one planned exception is the Ralph Lauren-banner rows (see decision 2).

## What was read
- **All 140 brands were read in Chrome, and none is `NC`.** A was read first and delivered earlier today. B and C were split across helper sessions, each working in its own Chrome tab under the same rules. `read_method` in the counts file says how each locator was made to list everything:
  - the locator's own JSON endpoint (Yext, SFCC, Uberall, stockist.co, Storepoint, StoreRocket, Locally, WeSupply);
  - a state or city directory crawl, checked against the store sitemap;
  - a static all-stores page;
  - a grid sweep where the radius was capped (Missoni, Tom Ford, Diesel).
- **Totals across the 140 brands:**
  - 3,531 own doors, against 3,472 claimed.
  - 1,441 outlets and 736 concessions, counted separately.
  - 55 pop-ups, which are not counted.
  - 44 doors listed as opening, which are not counted.
- **ZIPs:** 19 rows have `NC` in `zip`. Each of these locators gives no ZIP; the reason is in the row's note.
- **ZIP worklist:** 137 of the 138 rows now have a ZIP on a returned row.
  - 7 of those ZIPs come from a street lookup because the locator prints none: Eton 330 Madison, the 5 Madhappy doors, and Tecovas Tulsa (whose locator shows a Nashville ZIP). Each says so in `note`; check them before merging if lookup ZIPs are not acceptable.
  - Carhartt Greensboro and Reno match their store, but the locator writes the street differently: "W Friendly Ave Suite 128" with no number, and 13925 rather than 13985 S Virginia St.
  - Not returned: Rothy's, One Garden State Plaza, Paramus, which is no longer on Rothy's locator.
- **Shops:** all 33 were found and none is closed.
  - 31 addresses come from Google business panels, 2 from the shops' own sites. Each source is in `source_url`.
  - Oxford & Derby is described as a men's shoe shop, and Cove Creek Outfitters as a gun shop that also sells apparel. Both are worth checking against the register rules before entry.

## Values used
- **`NC`:** nobody looked. In `zip` it means the locator prints no ZIP.
- **`none` and `none listed`:** looked, and there was nothing.
- **`status`:**
  - `open`;
  - `opening`: coming soon, or an opening date after today, with the date in `note` where given;
  - `closed`: still listed but marked closed or temporarily closed. These are counted.
- **`operator`:** named wherever a partner, licensee or airport retailer runs the door (8 October ruling).

## Counts that moved by more than two
| brand | claimed | own now | outlets | concessions | why |
|---|---|---|---|---|---|
| Alo | 144 | 147 | 0 | 0 | 6 more listed as coming soon. |
| Levi's | 97 | 92 | 160 | 0 | 100 store-typed doors, 8 of them coming soon. The directory has no dealers. |
| BOSS | 59 | 66 | 63 | 147 | 59 run by BOSS itself. The rest: 2 run by operators, 4 airport travel stores, and 1 store tagged HUGO in the data. |
| Dior | 22 | 36 | 1 | 23 | Department-store boutiques are split out as concessions. Only 25 of the 60 boutiques list Men's Fashion. |
| Malbon | 10 | 14 | 0 | 0 | New stores. Malibu and Austin show an address only. |
| Carhartt | 61 | 68 | 3 | 0 | The count was stale, not the rows: the 68 on file were not dealers. |
| Hermès | 36 | 41 | 0 | 0 | Includes 3 airport stores and Hermès at Cuff's (operator); 37 without those. |
| Arc'teryx | 35 | 38 | 10 | 0 | From Locally, filtered to the brand's own retail account; 871 dealers excluded. |
| Loewe | 15 | 18 | 2 | 1 | New doors, including East Hampton and River Oaks. |
| State & Liberty | 45 | 48 | 0 | 0 | 4 more listed as coming soon. |
| J.McLaughlin | 164 | 192 | 0 | 0 | The full list from the locator's widget, all US. |
| Lululemon | 379 | 382 | 38 | 0 | From the all-stores page. 44 pop-ups returned as pop-ups; 85 Canadian stores excluded. |
| Vuori | 110 | 114 | 12 | 0 | Includes 3 stores marked temporarily closed. |
| Banana Republic | 129 | 123 | 168 | 0 | Directory matches the sitemap exactly, so these look like closures. Factory stores are outlets. |
| Polo Ralph Lauren | 44 | 11 | 160 | 0 | The September 44 was 10 Polo stores plus 34 'Ralph Lauren' multi-label flagships. See decision 2. |

## Decisions the merge has to make (where the brief or the record looks wrong)
1. **Outlets and concessions are as large as the own-store count.** Outlets: J.Crew Factory 412, Banana Republic Factory 168, Polo factory stores 160, Levi's 160, Brooks Brothers 88. Concessions: BOSS 147, Reiss 102, Rodd & Gunn 76. The counts split them; the map has to choose what one number means.
2. **Ralph Lauren-banner flagships** (44 rows, 38 of them open) are in `return_doors.csv` under the key Polo Ralph Lauren with note "banner Ralph Lauren flagship (multi-label); not a Polo-only door". They are left out of Polo's counts. The canonical keys have no plain 'Ralph Lauren' entry, so either Polo absorbs them, as the September count did, or they need a key.
3. **Department-store listings that may be counters, not shops.**
   - Possibly counters: Reiss (102), Givenchy (27) and Herno (6) list department stores with no sign of a branded shop. They are returned as concessions with a caution in the note; holding them is defensible.
   - Branded shops, which is why they were kept: BOSS, Dior, Sandro, Zegna (named 'Zegna Nordstrom'), Rodd & Gunn (typed 'Macy's Concession') and Lacoste (typed 'Corner').
4. **Partner-run doors are included with the operator named**, per the 8 October ruling. Stricter counts without them:
   - johnnie-O 22 (24 returned);
   - Southern Tide 35 (41 returned);
   - Hermès 37 (41 returned).
5. **Puerto Rico is handled two ways.** It is included where the locator files it under the US (120% Lino, Banana Republic, Saint Laurent, Brooks Brothers outlet; state `PR`). It is left out where the locator treats it as a separate country (Versace).
6. **Outlet calls made by location, where the locator has no type.** Brooks Brothers (6 such calls), Brunello Cucinelli San Marcos, Buck Mason Desert Hills, A Bathing Ape Cabazon. Belmont Park Village doors (A.P.C., John Varvatos, Billy Reid, Thom Browne) are mixed: classed as outlets where the locator says so, otherwise as own doors.
7. **J.Crew Factory is returned under J.Crew** with banner 'J.Crew Factory'. Is it part of J.Crew on the map?
8. **Mistakes in the locators' own data are returned as written and flagged in `note`.** Examples: Sandro Houston ZIP 78758, Reiss Honolulu ZIP 15237, Fendi Caesars ZIP 80109. Obvious state and city slips were corrected and noted (Carhartt MT to MO, Lacoste Florida Mall CA to FL, Saint Laurent McLean).
9. **Paul Smith and Thom Browne were read from their store sitemaps.** Paul Smith's US locator redirects to the UK, and Thom Browne's shows only 5 stores, so every store page was checked instead. Their counts are less certain than the rest.

## Other notes
- **Venue:** helper sessions were told to take `venue` only from the locator's own wording. In group B0 (AG, Peter Millar, Kiton, Tom Ford and others), some venues were inferred from the address.
- **Store names:** a few were edited to tell them apart, e.g. Rag & Bone's four 'New York, NY' stores and the Kiton NY and Miami stores.
- **Not returned:** stockists, wholesale retailers and restaurants or cafés. Each brand's count of these is in the `note` column of `return_counts.csv`.
