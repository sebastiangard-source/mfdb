# NOTE_0: Kirna Zabête stores (add_kirna_zabete_2026-10-20, Part 0)

Read 20 Oct 2026 in Chrome from kirnazabete.com/pages/stores, plus /pages/about-us for context.

**Result:** 7 US own stores, all open, all permanent. 0 outlets, 0 pop-ups, 0 concessions. Counts match rows (7 = 7). `reconcile.py`: 1 exact, 0 rewrites.

**Stores:** SoHo (160 Mercer St), Madison Ave (943 Madison Ave), East Hampton (66 Newtown Ln), Palm Beach (340 Royal Poinciana Way, Ste 305), Bryn Mawr (915 Lancaster Ave, Ste 170), Nashville (2001 Warfield Dr), Miami (106 NE 40th St).

**For you to rule:**
1. **Miami venue.** The page prints "Miami Design District" above the street address. I returned `street`, because it is a district and not a named center. If you count it, change the one cell.
2. **East Hampton** is `own-door`. The page says open all year, with no dates and no "seasonal". The About page says it began as a pop-up and was made year-round.
3. **Palm Beach** venue is `Royal Poinciana Plaza`, named on the page.

**Where the site contradicts itself:** the About page says "four uniquely vibrant stores" in one place and "seven boutiques" in another. It also says Nashville was the "sixth store" (Nov 2023) and Miami followed (Sept 2024), which makes seven. The store page lists seven. I returned seven. The "four" looks like stale copy.

**Not checked:** I did not look for stores outside the site's store page. No shop inside another retailer, no outlet, and no "opening soon" store is named. The Broome Street store is mentioned only as moved, so it is not returned.

**Brief:** nothing wrong. Note that `us_stockists` is `NONE` because the site lists no stockists. The brief's counts template does not say what to put for a store that is itself a stockist of others.
