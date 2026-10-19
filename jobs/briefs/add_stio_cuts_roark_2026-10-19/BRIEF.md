# add_stio_cuts_roark_2026-10-19: Stio, Cuts Clothing and Roark, for both maps

**Issued** 19 October 2026 · **Kind** seating read · **Three brands, three parts, each returned as done** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job on the brands' own US sites and store locators. If you cannot run a browser, say so and stop. **You gather and you propose; Sebastian rules.** Nothing you return places a brand or sets a score until he says so.

## The three brands

- **Stio:** outdoor and mountain clothing from Jackson, Wyoming, sold for men and women, with a few stores of its own in mountain towns. Not on either map yet.
- **Cuts Clothing:** Los Angeles, founded 2016, fitted tees and office-to-gym basics. **It is already on the men's map**, with no stores of its own as of August. Read only what this brief asks for Cuts, not a full men's record.
- **Roark:** travel and surf clothing from California, mainly men's. Not on either map yet.

## Part 0: doors first (`doors/`), all three brands

Do this before anything else and return it on its own: whether each brand has full-price stores of its own in the US decides what the rest of the job is for. Use the brand's own store locator or stores page only.

- `return_doors.csv` (`return_doors_template.csv`): one row per brand-named store, worldwide, US first.
  - `format` is `own-door`, `outlet` or `pop-up`.
  - `status` is `open` or `opening`. Closed stores are not returned.
  - Fill `operator` where a partner runs a store under the brand's name.
- `return_counts.csv`: one row per brand, with US own stores, outlets and stockists counted separately.

The rules in `rules_doors_reference.md` hold, with three rulings made since:

- **Counters are never rows,** including in department stores and even when the locator names them as the brand's. Count them in `us_concessions` if that's easy; otherwise `NC`.
- **Venue only from the locator:** a centre it names. Otherwise `street`. Never work it out from the address.
- Retailers that stock the brand under their own name are stockists, counted only. A store marked "coming soon" is `opening`.
- **A brand with no store of its own in the US is `NONE`, not `NC`.** Pop-ups with dates go in as `pop-up` and don't count as stores.

## Part 1: the men's record (`part1_mens/`)

The men's map record, as in the wave C seats. The rules files in the folder are the standing ones and win over anything here.

**Stio and Roark: a full record.** Return `return.csv` (one row per brand, every column of `return_template.csv`) and `return_styles.csv` (`schema_styles.json`).

1. **Store, currency, search** (`rules_prices.md`): US storefront, with USD confirmed on two displayed prices.
2. **Eight men's garments** (`rules_prices.md`, `rules_garment_links.md`): low and high, with the product and URL behind every figure, full price only.
   - Stio's outerwear high is its top technical shell or insulated piece.
   - Roark's tee and its "travel" shirts are the staples.
3. **Fibre by style** (`rules_fibre.md`): count styles, not colourways.
4. **Stockists** the brand itself lists, in `stockists.csv` (`stockists_template.csv`).
5. **Tech:** named fabrics and treatments.
   - Stio names its own fabrics and licensed ones (Pertex, Polartec and similar).
   - Say which are the brand's own and which are licensed, from the product pages.
6. **Craft** (`rules_craft.md`, `rubric_craft.txt`): six facts, two URLs, a proposed score and the reasoning.
7. **Origin and ownership** as the brand states them, with a filing where one exists.
8. Lookbook.
9. Vinted men's and Grailed.
10. B Corp and GOTS, from the certifiers' own directories.
11. One real quotation (`rules_quotes.md`).
12. The signature product.

**Cuts Clothing: doors only.** Part 0 covers it. The rest of its men's record is carried. If its prices look clearly wrong on the site today (the record has the tee at $48 to $98), say so in `NOTE_1.md`; don't re-read them.

## Part 2: the women's read (`part2_womens/`)

This is for the Cyprus Brand Set, which lists every fashion brand with full-price stores of its own in the US. Do Part 2 only for a brand whose Part 0 count shows **at least one US own store**. For any other brand, say so in `NOTE_2.md` and stop there.

1. **Does it sell women's clothing?** Return `return_crossover.csv` (`return_crossover_template.csv`), with the definitions unchanged from the crossover pass:
   - `womens_clothing` is one of:
     - `yes`: a women's clothing range under the brand's own name.
     - `partial`: thin, unisex sizing only, or in some stores only.
     - `no`: none.
   - Fill `where` only when the locator or a store page says the store sells women's. Otherwise `NC`, and say why in `evidence`.
   - A women's range that is footwear or accessories only counts as `no`.
2. **Women's prices**, only where the answer is `yes`. Return `return_prices.csv` (`return_prices_template.csv`).
   - Read eight garments from the women's section only: tee, blouse, sweater, jeans, trousers, dress, outerwear and shoes.
   - Give low and high, with the product and URL behind every figure, and a `basis` of `pair`, `range` or `single`.
   - Use `NONE` where the brand doesn't sell the garment for women.
   - **Leather and suede are never the outerwear high.**
   - The band rule at women's cuts: a core tee at or under $35 and a core blouse under $80 is Tier 1. Otherwise take the mean of the blouse and sweater entries: under $200 is Tier 2, $200 to $600 is Tier 3, over $600 is Tier 4.
     - Propose the band in `band_proposed`.
     - Where the rule reads wrong for an outdoor or athletic house with no blouse, say so and propose a band.
3. **Women's dials**, only where the answer is `yes`. Read `DIALS_BRIEF.md` (sections A to E). Return `return_dials.csv` (`return_dials_template.csv`) and `return_styles.csv`, covering:
   - the women's listing links;
   - an 80-style women's sample with composition;
   - fabric dials;
   - proposed tech and craft.

   The standing defaults hold:
   - Own labels only.
   - Lyocell is kept as its own fibre.
   - `fab_silk` is read.
   - Unisex listings are counted and flagged.
   - Sleepwear and swim are excluded.

Where a brand answers `no` or `partial`, the Brand Set lists it on its men's prices, as it does the other men's-only brands. Nothing more is needed.

## Rules

- **Names** must match `canonical_keys.txt`. Run `python3 reconcile.py` before each return.
- **Cell values:**
  - `NC`: nobody looked.
  - `NONE`: the brand doesn't sell or do it.
  - `np`: checked, and no price is published.
  - `ND`: the page was read and states nothing.
  - No empty cells.
- **Sources:** full price only. Use the brand's own site and locator first, then press that quotes the brand.
- **Bot walls:** one plain try. If a check box appears, ask Sebastian once whether he'll tick it himself. Anything else is `held`, with the wall named. Never work around a wall.
- **Pace:** one page at a time, at a human pace.
- Don't touch either map. Anything out of scope but noticed goes in the part's `NOTE`.

## Return, in this order

1. `doors/return_doors.csv`, `doors/return_counts.csv` and `doors/NOTE_0.md`. Return these straight away.
2. `part1_mens/return.csv`, `return_styles.csv`, `stockists.csv` and `NOTE_1.md`.
3. `part2_womens/return_crossover.csv`, `return_prices.csv`, `return_dials.csv`, `return_styles.csv` and `NOTE_2.md`.

## Time box

- **Part 0:** fifteen minutes a brand.
- **Part 1:** forty minutes a brand for sections 1 to 4, and thirty for 5 to 12.
- **Part 2:** thirty minutes a brand.
- Past the box, return what you have, put `NC` on the rest, and say so.
