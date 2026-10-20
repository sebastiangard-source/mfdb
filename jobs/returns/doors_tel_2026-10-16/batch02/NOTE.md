# doors_tel_2026-10-16 · batch 2 (eyewear) · NOTE

**Returned:** 476 door rows, all `own-door`, and 8 count rows. `reconcile.py` came back clean: 8 exact, 0 to rewrite, 0 unmatched. No cell is empty.

| Brand | Own | Concessions | Stockists | Locator rows |
|---|---|---|---|---|
| Warby Parker | 370 (18 opening) | 10 | 0 | 385 |
| Moscot | 15 | 0 | 298 | 3,698 |
| Oliver Peoples | 31 | 0 | 1,367 | 1,544 |
| Garrett Leight | 7 | 0 | 457 | 2,264 |
| Gentle Monster | 7 | 0 | 0 | 7 |
| Ray-Ban | 38 | 0 | NC | 38 |
| Persol | 2 | 0 | 485 | 711 |
| Jacques Marie Mage | 6 | 0 | 188 | 713 |

## Rulings applied

- **Counters are never rows** (20 Oct). Warby Parker's 10 "at Target" shops are counted in `us_concessions` and not returned as rows. No other eyewear locator lists a counter.

## Contradicts the brief

- **Warby Parker:** 380 US rows on the locator, not "250 or more". 19 are marked coming soon. One of those is in Target (Culver City), so 18 rows carry `status` = opening.
- **Ray-Ban:** the brand's locator lists only its 38 RAY-BAN stores and online resellers. Sunglass Hut, LensCrafters and Target Optical are not on it, so `us_stockists` is **NC, not 0**. That is different from batch 1, where 0 meant a direct-to-consumer brand's locator listed no stockists. For Ray-Ban, stockists clearly exist; the locator just doesn't show them.
- **Persol:** only 2 US boutiques: Beverly Hills and NoLita.
- **Oliver Peoples:** the store locator has 31 US boutiques, but the OP Boutiques page lists 29. The two extras appear only on the locator, and both are returned with a note:
  - **Las Vegas** is at an outlet-centre address, but the locator calls it a boutique, so it's `own-door`.
  - **Manhattan Village** has no phone or hours, so it may be newly opened.

## Method worth checking

- **US by coordinates.** Moscot, Oliver Peoples, Garrett Leight and Persol have unreliable country fields. Many Oliver Peoples rows in California read `CANADA`, and some read a state code. So I counted US rows by checking whether the coordinates fall inside a rough US outline (lower 48 plus Alaska, Hawaii and Puerto Rico). Counts near the Great Lakes border could be off by a handful.
- **Luxottica brands:** Oliver Peoples (code OP) and Persol (code PO) were read from the locator's own API at api-tab.luxottica.com. I paged it for everything within 6,000 km of central US, which reaches Hawaii. The Waikiki boutique is in the results.
- **Moscot:** the Stockist search caps at 100 rows. MOSCOT Shops are ranked first, so all 27 worldwide shops came back. Southampton is ranked lower but tagged as a shop, and I found it through the coordinate feed. Stockist counts come from that coordinate feed.
- **Jacques Marie Mage:** the locator reads a public Google Sheet, and the counts come from its country column. Two rows mention Puerto Rico and may or may not be counted.
- **Warby Parker `venue`:**
  - The store label is used where it names a centre (Natick Mall, Legacy Place, Prudential Center).
  - Street and neighbourhood labels are `street` (Newbury St., Logan Circle, Wynwood).
  - Ambiguous labels are `street`: King of Prussia, Pentagon City, Cherry Creek, Short Pump, Lehigh Valley, Green Hills.
  - This is a judgement on the label's wording only, with nothing taken from the address. The list is in `build2.py` if you want it changed.
- **Warby Parker phones:** 14 stores carry Warby's general (888) 492-7297 line.
- **Gentle Monster:** Costa Mesa and Valley Fair show "Reopens on 30 Oct / 6 Nov". They're kept as open and noted. The locator gives no phone numbers.
