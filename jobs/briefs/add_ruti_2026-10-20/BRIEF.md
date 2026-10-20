# add_ruti_2026-10-20: Ruti, for the Cyprus Brand Explorer

**Issued** 20 October 2026 · **Kind** seating read · **One brand, two parts** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job on Ruti's own US site and store locator. If you cannot run a browser, say so and stop. **You gather and propose; Sebastian rules.**

## The brand

**Ruti** is a women's clothing label with its own boutiques in US shopping streets and centers. It isn't on the Explorer yet. Our records hold only one fact about it: Bloomingdale's carries it. Establish its own US site first and record it.

The Explorer lists fashion brands with full-price stores of their own in the US, sorted into four tiers by what a women's blouse and sweater start at. Ruti needs its stores, its women's prices, its fabric and craft dials, and the facts for its card.

## Part 0: stores (`doors/`), first, returned on its own

Use Ruti's own store locator or stores page only. Return two files:

- `return_doors.csv` (`return_doors_template.csv`): one row per Ruti-named store, US first, then any abroad.
  - `format` is `own-door`, `outlet` or `pop-up`.
  - `status` is `open` or `opening`.
  - Closed stores are not returned.
- `return_counts.csv`: US own stores, outlets and stockists counted separately.

The rules in `rules_doors_reference.md` hold, with the rulings made since:

- **Counters are never rows.** A shop inside a department store (for example Bloomingdale's) is counted in `us_concessions` if the locator makes that easy; otherwise `NC`.
- **Venue only from the locator:** a center it names, otherwise `street`. Never work it out from the address.
- **Same address, one store.** If the locator lists the same store twice, return it once and say so in `note`.
- **A store marked coming soon** is `opening`.
- **Pop-ups with dates** are `pop-up` and don't count as stores.
- **If Ruti has no store of its own in the US,** the row is `NONE`, and Part 1 stops there. Say so in `NOTE_0.md`.

## Part 1: the women's read (`womens/`)

1. **Prices** (`return_prices.csv`, columns of `return_prices_template.csv`).
   - Read eight garments: tee, blouse, sweater, jeans, trousers, dress, outerwear and shoes.
   - For each, give the low and high price, with the product name and URL behind every figure, and a `basis`:
     - `pair`: the entry and elevated versions of one staple;
     - `range`: cheapest to dearest in the category;
     - `single`: one style only.
   - Full price only. Use `NONE` where Ruti doesn't sell the garment.
   - **Leather and suede are never the outerwear high.** Collaborations and capsules are never a high.
   - **Core** means the plain, year-round version of a garment, not the cheapest thing that fits the word.
   - **Band rule (women's cuts):**
     - **Tier 1:** a core tee at or under $35 and a core blouse under $80.
     - **Otherwise,** take the mean of the blouse entry and the sweater entry: under $200 is Tier 2, $200 to $600 is Tier 3, over $600 is Tier 4.
     - Propose the band in `band_proposed`. Where the rule reads wrong, say why.
2. **Dials** (`return_dials.csv` and `return_styles.csv`). Read `DIALS_BRIEF.md`, sections A–E, and return:
   - the women's listing links;
   - an 80-style sample with composition;
   - the fabric dials;
   - proposed tech and craft scores, with `rubric_craft.txt`.

   The standing defaults hold:
   - own label only;
   - lyocell counted as its own fibre;
   - `fab_silk` read;
   - unisex pieces counted and flagged;
   - sleepwear and swim excluded.
3. **Facts** (`return_facts.csv`, columns of `return_facts_template.csv`):
   - what it sells, in one plain sentence under thirty words;
   - the channels it sells through;
   - founding year, place and founders;
   - who owns it today, with a filing where one exists;
   - its signature product;
   - pronunciation, if the brand states it;
   - lookbook;
   - Vinted women's URL and The RealReal page;
   - B Corp and GOTS status, from the certifiers' own directories;
   - one real quotation, under `rules_quotes.md`.
4. **Social, while you're on the site:**
   - its Instagram and TikTok handles, linked from its own site;
   - the follower count each profile shows.

   Put these in `NOTE_1.md`. Read only: never follow, like or message.

## Rules

- **Names** must match `canonical_keys.txt`. Run `python3 reconcile.py` before each return.
- **Cell values:**
  - `NC`: nobody looked.
  - `NONE`: Ruti doesn't sell or do it.
  - `np`: checked, and no price is published.
  - `ND`: the page was read and states nothing.
  - No empty cells.
- **Bot walls:** one plain try. If a check box appears, ask Sebastian once whether he'll clear it himself. Anything else is `held`, with the wall named. Never work around a wall.
- **Pace:** one page at a time, at a human pace. Don't touch the map.

## Return and time box

1. **Part 0:** `doors/return_doors.csv`, `doors/return_counts.csv` and `doors/NOTE_0.md`. Return these straight away.
2. **Part 1:** `womens/return_prices.csv`, `return_dials.csv`, `return_styles.csv`, `return_facts.csv` and `NOTE_1.md`.

Allow fifteen minutes for Part 0 and about an hour for Part 1. Past the box, return what you have, put `NC` on the rest, and say so.
