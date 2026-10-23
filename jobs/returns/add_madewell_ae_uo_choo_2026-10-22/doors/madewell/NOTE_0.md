# NOTE_0 — Madewell stores (Part 0)

Captured 22 Oct 2026, Chrome, madewell.com/store-locator (Directory view). Brand name matches `canonical_keys.txt` (reconcile: exact).

**What was read.** The directory lists 164 stores in 41 state/DC pages. I read every state page for its cities, then every city page for its stores. The per-state counts match the directory's own counts in all 41 places. One plain read each, no bot wall, no CAPTCHA, a newsletter pop-up closed once.

**Result.** 162 rows returned: 160 open, 2 opening. All `own-door`, all US.

**For Sebastian to rule on**
1. **Two "Temporarily Closed" stores held out:** Scottsdale (7014 E Camelback Rd, AZ) and Southdale (1562 Southdale Center, Edina MN). The brief says closed stores are not returned and `status` allows only open/opening, so I left them out. If you count a temporary closure as open they add two rows (164).
2. **Men's-only shops (7)** appear as their own Madewell locations: Silver Lake LA, Marina District SF, Abbot Kinney Venice, Brookfield Place NYC, Bridgeport Village Tigard, South Congress Austin, 14th Street DC. They sit at different addresses and phones from the women's stores, so each is a row, flagged in `note`. Drop them if the Explorer counts only women's doors.
3. **Venue.** The locator has no venue field, only a store label. Where the label is a centre name I used it; where the label is a city, street or neighbourhood (e.g. "Greenwich", "Newbury Street", "Soho") I wrote `street`. Several labels are shorthand for a centre (Lynnfield = MarketStreet, Natick = Natick Mall, Chestnut Hill = The Shops at Chestnut Hill, King of Prussia, Short Hills) and are `street` under the rule, since the locator doesn't name the centre. Worth your eye if venue matters for the WS-centre match.
4. **Outlets: 0.** None of the 164 is labelled outlet and the locator has no format field. I did not infer outlets from addresses. The Madewell filter in the URL (`brands=madewell`) suggests J.Crew-group banners sit behind other filters; I did not open those.
5. **Concessions and stockists: NC.** Not on this locator. Madewell shops inside J.Crew or Nordstrom would be counters in any case.

**Contradicted or surprising.** The brief says Madewell is "at 10 WS centers". The locator shows four of your five Insider properties: Legacy Place (Dedham), Derby Street (Hingham), Chestnut Hill and Lynnfield (listed under city names, so not matched by label). Nothing at Seaport. I did not map to WS centres beyond that; the 10 figure is not something this locator can confirm.

**Brief notes.** `return_counts.csv` has no field for temporarily closed, which is why that sits in the note. No duplicates under "same address, one store": the Brookfield, Marina District and Abbot Kinney pairs have different street addresses.

**Not touched:** the map, any account, any form.
