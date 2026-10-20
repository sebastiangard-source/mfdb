# doors_tel_2026-10-16 · batch 1 (travel) · NOTE

**Returned:** 121 door rows (44 own-door, 77 outlet), 10 count rows. `reconcile.py` ran clean: 10 exact, 0 to rewrite, 0 unmatched. No empty cells.

| Brand | Result | Own | Outlet | Stockists |
|---|---|---|---|---|
| Away | read | 14 | 0 | 0 |
| Monos | read | 5 | 0 | 0 |
| Rimowa | read | 15 | 0 | 0 |
| Tumi | **held** (bot wall) | – | – | – |
| Béis | read, **NONE** | 0 | 0 | 212 |
| Calpak | read | 1 | 0 | 0 |
| Paravel | **NC** (site gone) | – | – | – |
| Briggs & Riley | read | 7 | 0 | 354 |
| Samsonite | read | 2 | 77 | 4,073 |
| July | read, **NONE** | 0 | 0 | 0 |

## Not reached

- **Tumi: held.** The store finder loaded once and showed Store, Outlet and Retail types. The next page, the store directory, returned a PerimeterX "Press & Hold" wall. That isn't a check box, so it's held under the brief. If Sebastian clears the hold in his own Chrome, Tumi can be retried.
- **Paravel: NC.** `tourparavel.com` does not resolve (NXDOMAIN). Press coverage says the site shut down in 2025. There is no locator to read. This is NC, not NONE, because nobody could look.

## Contradicts the brief

- **Rimowa:** the brief expected many retailer and department-store doors. The US locator lists only its 15 RIMOWA Stores. It has Department Store and Pop-Up filters, but no US rows under either. Stockists are 0 *on this locator*, which doesn't mean 0 in the world.
- **Briggs & Riley:** the brief said "few or none". The locator has **7 brand-named stores**:
  - two "by Sunsations" in Las Vegas, which are dealer-run, so `operator` = Sunsations;
  - two in airports (LGA, SLC);
  - Palo Alto, Santa Monica Place and Danville Livery.
  
  Only Sunsations is named as an operator. The others may be dealer-run too, but the locator doesn't say so, so `operator` = none stated.
- **Samsonite:**
  - No "Black Label" stores are listed.
  - The locator's "Our Stores" type includes **one Dillard's** (Greensboro). That's a department store under its own name, so it's counted as a stockist and not returned as a row.
  - "Samsonite Company Store" (Riverhead, inside Tanger) is returned as `outlet` and noted.
  - Only 2 doors are full-price (Faneuil Hall, Century City).
- **July** is Australian. The US site has no store page, and the global page lists no US stores, so it's NONE.

## Method worth checking

- **Samsonite** has no full-list page. I queried the locator's own FindStores endpoint, the same one the page calls:
  - "Our Stores": 250-mile radius from 76 ZIPs, then 30 tighter checks in the Northeast, where three queries hit 15 results. The tighter checks found nothing new, so 80 looks complete.
  - Retailers: the same sweep, deduped by store ID, gave 4,072.
  - Queries ran about 2.5 seconds apart, with no wall.
- **Samsonite addresses:** the locator's own data runs the street line and the centre line together, e.g. `Suite 4105Tulsa Premium Outlets`. I split them at the join and took the centre as `venue`. Each such row says so in `note`. Things to check:
  - Store 0251 Round Rock reads `4401 North IH 858` and is left as given.
  - Store 0740's second line is just "Century City", so it's left as `street`. It is not treated as Westfield Century City.
- **Briggs & Riley:** read from the Storepoint feed the locator page loads: 448 rows worldwide, 361 US by address.
- **Béis:** stockists were counted by parsing addresses from the rendered list, so the count may be off by a few.
- **Away and Monos:** neither locator lists stockists. `us_stockists` = 0 means looked and none listed.
- **Venue:** comes only from labels or second lines on the locators. For Rimowa, "Miami – Bal Harbour" names the town, not Bal Harbour Shops, so it's `street`. "Las Vegas – Wynn" is the resort the locator names.

## Brief notes

- "Same address, one store": Away's NoHo appears twice on one page, but both entries point to the same store record. I returned it once and noted it, not as two entries. Tell me if the ruling meant otherwise.
- `us_own_stores` carries `NONE` for Béis and July, `NC` for Paravel and `held` for Tumi. These are text in a numeric column. Say if the merge wants those in `note` only.
