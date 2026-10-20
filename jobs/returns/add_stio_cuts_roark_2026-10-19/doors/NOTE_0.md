# NOTE_0 — add_stio_cuts_roark_2026-10-19, Part 0 (doors)

Captured 19 Oct 2026, Chrome, brands' own locators only. `reconcile.py`: 3 names, 3 exact.

## Result

| Brand | US own | US outlets | Stockists | Part 2? |
|---|---|---|---|---|
| Stio | 14 (Mountain Studios) | 0 | 349 (locator's by-state counts) | Yes |
| Cuts Clothing | NONE | NONE | ND | No |
| Roark | 8 (Expedition Union) | 0 | NC | Yes |

No stores outside the US on either locator. Concessions `NC` for all three (no locator lists any).

## Checked

- **Stio:** `/pages/store-locator` list view (14 Mountain Studios, then "Authorized Retail Locations" by state), and all 14 store pages for venue and Upcoming Events. The only dated pop-up is the YOTEL Boston event (22 Oct, two hours); it's in as a `pop-up` row with `opening`, not counted. Every studio also lists an 11/5 "Season Kickoff Party" in-store; these are events, not doors, so they aren't returned.
- **Cuts Clothing:** `/pages/store-locator` exists (it's in the page sitemap and titled "Store Locator") but renders nothing after waits and a reload. No other store page in the sitemap, menu or footer. About and Returns mention no store. Recorded as `NONE`, consistent with the August record.
- **Roark:** `/pages/store-locator` lists eight "Expedition Union" stores, all marked OPEN, with no phones and no store pages. The retailer search below it is a Stockist.co widget that returns the 10 nearest to the browser's location and no total, so stockists are `NC`, not 10.

## For Sebastian to rule

1. **Stio Castle Rock**: listed as a Mountain Studio, but its page offers "exclusive deals on past-season apparel, only available here". The address is on Factory Shops Blvd, but the locator names no outlet centre, so I left it `own-door` with venue `street`. If you rule it an outlet, it's 13 own and 1 outlet. Freeport also mentions past-season discounts but says it carries the full collection, so it's kept as own-door.
2. **Roark Palisades Tahoe**: the locator gives only "The Village at Palisades Tahoe". Street, city and ZIP are `ND`. I took state CA from the resort name; please check.
3. **Cuts "retail locations"**: a Cuts help-centre article is titled "Can I use my VIP membership discount in retail locations?" The answer says the discount is site-only and names no stores. With the empty locator page, this might mean stores are planned or wholesale doors exist. I found nothing to count.

## Contradicts the record / brief

- Nothing contradicts the Cuts record (no own stores).
- Brief says Stio has "a few stores of its own in mountain towns". The locator has 14, including Boston and Freeport.
- `operator` is `ND` on every row: no locator names a partner operator, and none says the brand runs the store itself.
- Both Stio and Roark stores also sell partner brands' gear, according to the store pages. They're still brand-named full-price doors.

## Observed on a page, not acted on

The Stio 404 page (`/pages/stores`) printed the text "STOP CLAUDE" at the foot of its body. I treated it as page content and kept going. Flagging it in case it matters.
