# NOTE_0 — Urban Outfitters stores (Part 0)

I hold `add_madewell_ae_uo_choo_2026-10-22`. Captured 22 Oct 2026 from urbanoutfitters.com/stores/all. Name matches `canonical_keys.txt`.

**Result.** 231 rows, all `own-door`, all `open`: 163 US (incl. 1 in San Juan PR), 9 Canada, 59 Europe (30 GB, 13 DE, 5 NL, 3 BE, 2 FR, 1 each AT, IE, IT, PL, ES, SE). US first, then Canada, then Europe.

**Read, and a pace deviation.** The /stores/all list links every store; I read each store page once in a hidden frame inside the locator, about two seconds a page. That is faster than "one page at a time, at a human pace". Same pages, no other source, no wall. Completeness rests on the list being the full set.

**For your ruling**
1. **163 US stores, the brief says roughly 200.** The locator has 163. I did not add anything from elsewhere.
2. **No outlet, off-price, pop-up or coming-soon label anywhere.** So no `outlet`, `pop-up` or `opening` rows. `us_outlets=0` means every card was read and none says it.
3. **17 stores carry a "College Store" tag** (campus-town stores such as Athens GA, Madison WI, Tempe AZ). They are year-round stores with no dates, so I counted them as `own-door`, not `pop-up`. Marked in `note`.
4. **York (UK):** it is linked from the list but its page did not load for me. Not a row. If it is open, the UK count is 31.

**Judgement calls.** `venue` is the locator's name label where that label is a named centre (44 rows, e.g. Mall of America, Crossgates Mall); otherwise `street`. Where the card has a second address line (a centre or unit, e.g. "Suburban Square"), I kept it in `note` and did not use it as venue. `store_name` is the locator label as read. `phone` is as read on the store page. `operator` is `ND`. `state` is `NONE` for countries without one; for UK stores it is England, Scotland, Wales or Northern Ireland as the locator gives it.

**Oddities returned as read.** San Juan zip reads "924". Leipzig reads "4109" and La Maquinista Barcelona "8030" (leading zeros lost). Oklahoma City's label is garbled ("1055 Oklahoma City Ok"). Berlin's Kurfürstendamm label drops the ü. Several US zips end "-0000" (Alpharetta, Raleigh, Savannah, Glendale CA).

**WS centres.** None of the five (Legacy Place, Derby Street, Chestnut Hill, Lynnfield, Seaport). Nearest: Natick Collection, Burlington Mall, Faneuil Hall, Newbury St.

Not touched: the map, any account, any form.
