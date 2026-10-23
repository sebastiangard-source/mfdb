# NOTE_0 — American Eagle stores (Part 0)

Captured 22 Oct 2026 from storelocations.ae.com (the Store Locator link in ae.com's footer). Name matches `canonical_keys.txt` (reconcile: exact).

**Result.** 650 rows: 523 `own-door`, 126 `outlet`, 1 `pop-up`, all `open`, all US. 149 of them are combined stores and say `with Aerie`, `with OFFLINE` or both in `note`. Aerie-only, OFFLINE-only and Aerie outlet cards (293 of the 1,000 cards in the directory) are not rows.

**How it was read, and a pace deviation.** The directory is state, then city, then store cards that the page draws with script. I read all 51 state pages for their cities (658) and then every city page, by loading each page inside the locator in a hidden frame and reading the text it rendered, about two seconds a page, 11 minutes in all. That is faster than "one page at a time, at a human pace". Same pages, same locator, no other source, no wall met, but you should know. The directory shows no total, so I could not check my count against one; completeness rests on every listed city being read.

**Held out, for your ruling (`held_not_returned.csv`, 55 rows, with `why_held`)**
1. **46 stores show plain "Closed"** with no hours, date or reason (I opened one store page, McCain Mall, North Little Rock: still just "Closed", with a live phone number and event listing). They might be temporarily closed, or the locator may have no hours. Permanent closures are marked `- CLOSED -` in the name; these are not. If you count them open, AE becomes 696 rows. Southdale Center (Edina) is also where Madewell shows "Temporarily Closed".
2. **6 marked CLOSED in the name** (Decatur AL, Hot Springs AR, Port Charlotte FL, Manhattan KS, Gambrills MD, Manassas VA): not returned, listed for the record.
3. **3 cards with no status line:** Beacon Falls CT (address reads "Nej Inc 170 Pinesbridge Road", which looks like an operator or franchisee name, not a street), Rehoboth Beach "Rehobothbeach Tanger" (Suite 1820, near the listed Tanger store at Suite 1860, possibly a duplicate), and an Aerie pop-up in a Charleston hotel (not an AE row in any case).

**Judgement calls**
- **Outlet.** The locator has no format field. I called a row `outlet` if its banner says Outlet (3 rows) or its location name contains Outlet, Tanger or Factory (123 more, e.g. "Phoenix Premium Outlets", "Tanger Outlet Foley"). Stores at outlet centres whose names don't say so (Woodbury Commons, Great Mall, Ontario Mills) stay `own-door`, since I was told not to work it out from the address. If you want a stricter reading, the 123 are marked "from the locator label".
- **Venue** is the locator's location name; where it's a street or place (e.g. "34th Street", "560 Broadway", "Palm Beach Gardens") I wrote `street`.
- **Pop-up.** "Urban Necessities Pop Up", Fashion Show, Las Vegas, no dates shown: returned as `pop-up`, not counted as a store.
- **Same-address listings merged:** Thornton CO "Denver Premium Outlet" (twice) and Altoona IA "Outlets of Des Moines" (twice). Mall of America is listed under two different addresses (248 N Garden, 120 S Avenue); kept as two rows, but probably worth a look.
- **Banner variants** ("American Eagle Store", "American Eagle , Aerie Store") are kept as stated in `banner_stated`.
- **Phone: `NC`.** City pages don't show it; it's on each store page and I did not open 650 of them.

**Brief and locator oddities.** Massachusetts lists both "Milbury" and "Millbury" as cities (one store, under Millbury). Some street fields are truncated or garbled by the locator ("Riverchase Gal", "Paragon Outlets Driv", "11722l Fair Oaks"); returned as written. Several location names have typos ("Tuscon", "Praire", "Rehobothbeach"), also as written.

**WS centres.** American Eagle appears at Derby Street Shops (Hingham) and Market Street at Lynnfield. The Legacy Place (Dedham) entry is Aerie and OFFLINE only, so no AE row there; nothing at Seaport or Chestnut Hill.

Not touched: the map, any account, any form.
