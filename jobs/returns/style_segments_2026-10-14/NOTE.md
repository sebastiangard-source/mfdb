# NOTE — style_segments_2026-10-14

## What I did

1. I read all three input files and reproduced the 11 October cut from its rules. All 370 rows matched, and so did the stated counts.
2. I settled on 15 segments before placing any brand (`taxonomy.md`). Then I wrote 17 ordered rules over the dials and ran them on all 370 brands.
3. I reviewed every placement against its `why` line and made 37 named overrides. Each one says why in `rule_or_reason` and is marked `medium` or `low`.
4. I added secondary segments where a brand sits on a border, and I built the crosstabs from `own_doors`, `store_tier` and `band` exactly as given.
5. I compared the segments with the Cyprus tiers file and computed medians from the price columns.
6. Nothing was rescored, no web research was done, and the input files are untouched.

**Confidence:** 316 high, 42 medium, 12 low.
- The 12 low rows are real rulings: Ferragamo, Givenchy and Etro (status dial), Sandro, Paul Smith, Sid Mashburn, Isabel Marant, Vince, Emporio Armani, Bally, Boggi Milano and Aether Apparel.
- Rows with no culture register scored are capped at `medium`.

## Where the brief would have produced a confident wrong answer

1. **NC covers nine brands, not two:** Dickies, G.H. Bass, Helmut Lang, Katin, Koio, Perfect Moment, Quoddy, RVCA and Woolrich. A crosstab built on "two NC" would have dropped seven brands or counted them as zero doors. They have their own NC column, and their doors are not added to any total.
2. **"Expect about twenty moves."** There are 82 rows with a first-cut segment different from the final one, so 82 have a value in `moved_from_first_cut`. Renames alone do not count as moves.
   - About 20 are misfiles of the kind the brief lists. These include J.Crew, Southern Tide, Zegna, Alo, Alden, Buck Mason, Lemaire, Margaret Howell, Gap and Ferragamo.
   - The rest come from rule changes the misfiles required:
     - Technical brands with outdoor/ski/surf ≥4 now file as Outdoor rather than Performance (10 brands).
     - Golf-first brands now file as Prep, club & course (3).
     - The style-5 houses move from Quiet luxury to Runway houses (4).
     - The ski-luxury brands move from Quiet luxury to Outdoor (3).
     - The Paris and London designers move from Tailoring to Fashion insider (8).
     - Performance-fabric basics move to Basics (6).
   - Holding moves to twenty would have left those classes half-fixed.
3. **Runway houses has four brands, not three:** Burberry, Dior, Fendi and Lanvin. Merging it would have folded Saint Laurent, Celine and Valentino into "Quiet luxury," which a member would read as wrong. I redefined the segment instead (see `taxonomy.md`).
4. **"Tailoring at 60 is too wide" is only half right.** The fuss dial did pull in the wrong brands, and 15 of them are now out. But the right fix also brings in the suit and dress-shirt makers that the dials had placed elsewhere: Jos. A. Bank, Indochino, Eton, Charles Tyrwhitt, Proper Cloth, State & Liberty and Zegna. The segment ends at 54 because the map is heavy in tailoring, not because of a rule error.
5. **The tiers file does not cover the whole map.**
   - 36 brands in `brand_dials.csv` are absent from it, and 4 are "Not established." Zadig & Voltaire is "Pending price read."
   - Read literally ("everything except Basic out and Wholesale-only is in"), the brief would put all 41 of those brands in the universe. I counted them as not ruled, and the `note` column says which applies.
   - Six of them have doors and would qualify: Onward Reserve, Undefeated, Mollusk, Lady White Co., Represent and Pilgrim Surf + Supply.
6. **Door counts differ between the two files for five brands:** Kith 12 vs 14, L.L.Bean 61 vs 62, Pendleton 15 vs 16, Polo Ralph Lauren 44 vs 47, and RRL 25 vs 26. Kith's difference crosses a tier boundary (Coastal circuit here, Networks in the tiers file). I used `brand_dials.csv` throughout and flagged each case in `note`.
7. **"Wave B/C" cannot be identified.** No column marks the 109 brands seated after 8 October. Instead, I used the number of culture registers above 1: 11 brands have none and 23 have one.
   - I found no `why` line that plainly contradicts a register scored 1. For example, no surf house has surf = 1.
   - The thin rows are marked `medium`. Auralee, with no register at all, had to be placed by hand.
8. **`USD_landed` is not USD.** Fifteen brands are priced that way, seven of them Fashion insider. I followed the brief's rule and left them out of the price medians. `findings.md` reports the result with them included, which leaves the ranking unchanged.
9. **Golden Goose's secondary segment.** The brief calls Golden Goose "Hype and Status," but there is no Status segment. I used Loud luxury as its secondary segment.

## Dials that look wrong (not rescored; brands placed on the rest)

- **`fuss` on dress-shirt makers:** Eton is −2 and Charles Tyrwhitt is −3, for ranges that are entirely dress shirts.
- **`status` 3 on luxury houses:** Ferragamo (37 doors), Givenchy and Etro.
- **`boat` 4–5 on Italian tailors:** Kiton, Stefano Ricci, Zilli, Brioni, Isaia, Rubinacci, Cesare Attolini and Zegna. This is what sent Zegna to Prep in the first cut.
- **`style` 3 on Palace,** a weekly-drop label.
- **`street` 4 on Wales Bonner,** which reads as designer.
- **`street` 3 on Puma,** against 4 for adidas.
- **`racquet` 4 on Sunspel,** whose range is mostly tees and underwear.
- **`tech` 4 on Uniqlo, Rothy's, Cole Haan and Brax.** For these brands it measures fabric or fit, not sport.
- **`status` 4 on Alo,** against 3 for Ferragamo.

## What I could not do

- I could not check placements against anything outside the folder.
- Secondary segments are judgment calls traceable to the dials. They are not produced by a rule.
- The resale, drop-cadence, press and men's-share dials proposed in `findings.md` would remove most of the 37 overrides. Until they exist, the overrides stand as rulings for Sebastian.
