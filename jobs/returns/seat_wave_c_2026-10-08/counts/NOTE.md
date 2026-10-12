# Wave C door counts: return note, 10 October 2026

Section 4, in Chrome, for the ten brands that were `NC` in facts-first, plus a full count for Zara.
Files: `return_counts.csv` (one row per brand) and `own_doors.csv` (one row per door read, for the brands where the locator gave doors).

## Counts

| brand | US own | US outlet | US concession | world own | basis |
|---|---|---|---|---|---|
| Birdwell | 0 | 0 | 0 | 0 | no store on site; dealer page only |
| Danner | 6 | 0 | 0 | NC | Locally feed, Danner-named markers |
| Dickies | NC | NC | NC | NC | locator iframe 404 — not counted |
| Frye | 0 | 0 | 0 | 0 | locator redirects to Contact; no store on site |
| Jos. A. Bank | 185 | 1 | 0 | 185 | brand store directory: 186 stores (180 pages read, 6 via search) |
| Outdoor Voices | 0 | 0 | 0 | 0 | no locator; legacy pages without addresses |
| Rancourt & Co. | 0 | 0 | 0 | 0 | no shop on site; factory address only |
| UGG | 10 | 36 | 1 | NC | 'Our Brand Stores' page + Locally feed |
| Universal Works | 0 | 0 | 0 | 6 | stores + partnership-stores pages |
| Y-3 | NC | NC | NC | NC | not retried, per ruling |
| Zara | 102 | 0 | 0 | NC | locator endpoint census, ~10,000 queries |

## What was checked
- **Zara:** the facts-first 69 was a floor. The locator's search endpoint returns stores within about 30 km of a point and has no directory, so I ran it on two offset grids over the lower 48, flood-filled around every hit, plus points in Alaska, Hawaii and Puerto Rico, and checked 72 metro centres: about 10,000 requests, one at a time, with no errors or blocks. That gives 103 records. The first grid missed 2, which the metro check caught; the offset grid found nothing further. One record is an employee-only office and is excluded, so the count is **102**. Greenwich CT lists no Man section. Puerto Rico returns nothing on the US locator.
- Each brand's own locator or store page, read in Chrome. Where the locator was a third-party widget (Locally for Danner and UGG; Where2GetIt for Dickies), I read the widget's own data feed in the page and noted the endpoint.
- Jos. A. Bank: all 186 store pages in the brand's directory, plus the locator search for the six pages that return 404.

## What was not reached
- **Dickies:** the locator is broken on the brand's side. `/en-us/pages/stores` embeds a Where2GetIt iframe that returns 404. Not a zero.
- **Y-3:** not retried, per the 10 Oct ruling.
- **World counts for Danner and UGG:** both Locally feeds include some non-US doors, but neither is the brand's world list, so both are `NC`.

## Zeros that rest on the site saying nothing (for ruling)
Four zeros below come from the absence of any store on the brand's site, not from a locator that returned nothing. I've kept them separate so they don't read like the 26 boilerplate zeros in the locations pass.
- **Birdwell:** no store page; the dealer page lists about 95 third-party shops. The worklist's "Newport Beach store" appears nowhere on birdwell.com.
- **Frye:** `/pages/store-locator` now redirects to Contact.
- **Outdoor Voices:** no locator. 18 unlinked legacy `visit-us` pages remain, with no address or hours.
- **Rancourt & Co.:** the contact page gives the Lewiston factory at 9 Bridge Street with 9–5 hours, and the site never calls it a shop. If it is ruled a factory store on the Oxxford showroom precedent, this becomes 1.

## Judgement calls made
- **Outlet centres (the "an outlet centre is an outlet" ruling):** I counted UGG's stores at Simon's "Mills" value centres (Ontario Mills, Concord Mills, Great Mall, The Mill at Jersey Gardens) as outlets. Jos. A. Bank Leesburg VA is at 241 Fort Evans Rd NE, which is Leesburg Corner Premium Outlets, so it is an outlet; the directory does not say so.
- **Danner Factory Store (Portland):** this is at the factory site, not an outlet centre, so I counted it as own-door and flagged it.
- **UGG Macy's Herald Square:** a branded UGG shop inside Macy's, so a concession.
- **Universal Works Partnership Stores (Lyon, Toulouse, Berlin):** they trade under the UW name and are run by local retailers, so they count as own-door with the operator in `note`, under the operator ruling. The Hankyu Men's Tokyo shop is a concession.

## What contradicted the record
- **Birdwell:** the worklist's "Newport Beach store" is not on the brand's site.
- **Jos. A. Bank:** the worklist's "hundreds of stores" is 186 today.
- **UGG:** 10 full-price US doors, plus one announced for Williamsburg; the other 36 US UGG doors are outlets.

## What the brief got wrong, or left open
- **`own_doors.csv`** holds 349 rows: Danner, Jos. A. Bank, UGG (including the coming-soon Williamsburg store, status `coming soon`), Universal Works and Zara. Zara fields are verbatim from the locator, uppercase as written.
- `return_counts.csv` has no schema in the brief. I used the four door columns from `return.csv` (`own_doors_us`, `own_doors_world`, `locator_url`, `doors_basis`) and added `outlets_us`, `concessions_us`, `locator_kind`, `captured_on`, `source` and `note`, so that outlets are not lost.
- The open Chrome tab at the start held the crashed thread's Dickies feed dump written into the page (tab title "DUMP"). I did not use it as a source.

## Next
The full records (all 81 brands, in worklist order, in batches of ten) start from Alan Flusser. The door rows here will carry into those batches' `own_doors.csv`.
