# NOTE — social_2026-10-20, batch 1 (25 brands, Chico's to Zara)

Read 20 October 2026 in Chrome, read only. No login prompt blocked a count and no check box, slider or rate limit appeared, so no `NC` cells.

## Result
- Instagram: 25 of 25 `done`. All 25 accounts were linked from the brand's own site and all show the verified badge.
- TikTok: 20 `done`, 5 `NONE`. Sixteen were linked from the brand's own site, four were found by platform search (Soma, J.Crew, Lilly Pulitzer, Chico's).
- TikTok `NONE` rows: White House Black Market, J.Jill, J.McLaughlin, Jos. A. Bank, Evereve. Candidates and why they failed the test are in each row's `note`.

## Doubtful, worth a look before merge
- **Chico's TikTok** (@lovechicos, 954 followers). Not verified. It passes on the bio, which links chicos.com/store, and the name and tagline match the brand's Instagram. I did not scroll its videos.
- **White House Black Market TikTok.** @whitehouseblackmarket has 4005 followers, the name "WHBM" and a brand-style bio, but no badge and no site link. I put `NONE` rather than guess. It is probably the brand, so this is the likeliest row to flip if you want to relax the test.
- **Talbots TikTok** shows 8757 followers, a very low figure for a verified brand account. It is what the page displayed.
- **Soma TikTok.** @somaintimates is verified (5410). A second account, @soma (2317, unverified, no bio), was passed over.

## Where I read links from
- Anthropologie, Free People, Banana Republic and Zara show no social links on first load. I found them in the page source after scrolling to the footer (zara.com/us/ for Zara). They are the brand's own markup, so I recorded `brand_site`.
- Aerie: the worklist site is ae.com. I used aerie.com, which links Aerie's own accounts, not American Eagle's.
- Lululemon's site (shop.lululemon.com) and J.McLaughlin, Jos. A. Bank, J.Crew, Lilly Pulitzer and Evereve link Instagram only.

## Regional and split accounts
I did not search for regional, men's or kids' sister accounts beyond what each site links. Every row is `account_scope = main` on that basis. Sister banners were kept separate: Athleta is not Gap, Aerie is not American Eagle, J.Crew is not J.Crew Factory.

## About the brief
- The verified badge was read from the page (Instagram's "Verified" icon, TikTok's blue check icon). I checked it by screenshot on Instagram (Evereve) and TikTok (lululemon).
- `NONE` rows have `NONE` in every cell that would hold a handle or count, to meet "no empty cells". That value is not distinct from "looked and found nothing" for `handle`, but `status` is the authoritative column.
- Pace: roughly one profile every 4 to 7 seconds. Instagram returned nothing empty.
