# add_madewell_ae_uo_choo_2026-10-22: four brands for the Cyprus Brand Explorer

**Issued** 22 October 2026 · **Kind** seating read · **Four brands, two parts each** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job on each brand's own US site and store locator. If you cannot run a browser, say so and stop. **You gather and propose; Sebastian rules.**

## The brands

None of these is on the Explorer yet. Work them in this order:

| # | Brand | Site | Notes |
|---|---|---|---|
| 1 | **Madewell** | madewell.com | J.Crew Group label. At 10 WS centers. |
| 2 | **American Eagle** | ae.com | Sister of Aerie, which is already on the Explorer as its own brand. |
| 3 | **Urban Outfitters** | urbanoutfitters.com | URBN sister of Anthropologie and Free People, both already on the Explorer. |
| 4 | **Jimmy Choo** | jimmychoo.com | Shoes and bags. Capri Holdings. |

The Explorer lists fashion brands with full-price stores of their own in the US, sorted into four tiers. Each brand needs its stores, its women's prices, its fabric and craft dials (not Jimmy Choo; see below), and the facts for its card.

Monos and Ray-Ban were also asked for. They are already on the Explorer as other brands (travel and eyewear) and are not part of this brief.

## Part 0: stores (`doors/`), one brand at a time, each returned on its own

Use the brand's own store locator or stores page only. For each brand, return two files, named with the brand (for example `doors/madewell/`):

- `return_doors.csv` (`return_doors_template.csv`): one row per store under the brand's name, US first, then any abroad.
  - `format` is `own-door`, `outlet` or `pop-up`.
  - `status` is `open` or `opening`.
  - Closed stores are not returned.
- `return_counts.csv`: US own stores, outlets and stockists counted separately.

The rules in `rules_doors_reference.md` hold, with the rulings made since:

- **Counters are never rows,** even inside department stores. A shop inside a department store is counted in `us_concessions` if the locator makes that easy; otherwise `NC`.
- **Hotel spas and similar are not stores.**
- **Venue only from the locator:** a center it names, otherwise `street`. Never work it out from the address.
- **Same address, one store.** If the locator lists the same store twice, return it once and say so in `note`.
- **A store marked coming soon** is `opening`.
- **Pop-ups with dates** are `pop-up` and don't count as stores.
- **Sister banners are separate brands.** Only stores under this brand's own name count.

Brand by brand:

- **Madewell:** outlets are `outlet`. Madewell sections inside J.Crew stores, or shops inside Nordstrom and other stores, are counters, not rows.
- **American Eagle:** count stores under the American Eagle name. Many are combined American Eagle and Aerie stores. A combined store is one American Eagle row; put `with Aerie` in `note`. Aerie-only stores and OFFLINE by Aerie stores are not rows. AE outlet and clearance stores are `outlet`.
- **Urban Outfitters:** outlets and off-price stores are `outlet`. Campus and seasonal pop-ups with dates are `pop-up`.
- **Jimmy Choo:** boutiques under the Jimmy Choo name are rows. Shops inside Saks, Neiman Marcus and other department stores are counters, not rows. Outlets are `outlet`.

The two large lists, American Eagle (roughly 800 US stores) and Urban Outfitters (roughly 200), may need the locator's state-by-state pages. Read them one state at a time. If the locator caps results, say so in the note and read by state or ZIP until the list is whole.

## Part 1: the women's read (`womens/`), one brand at a time

1. **Prices** (`return_prices.csv`, columns of `return_prices_template.csv`, one row per brand).
   - Read eight garments: tee, blouse, sweater, jeans, trousers, dress, outerwear and shoes.
   - For each, give the low and high price, with the product name and URL behind every figure, and a `basis`:
     - `pair`: the entry and elevated versions of one staple;
     - `range`: cheapest to dearest in the category;
     - `single`: one style only.
   - Full price only. Use `NONE` where the brand doesn't sell the garment.
   - **Own label only.** Urban Outfitters sells many outside brands. Read only its own labels (for example BDG, Out From Under, UO) and list the labels you used in `sublines_included`. Madewell and American Eagle also carry a few outside brands; leave those out.
   - **Leather and suede are never the outerwear high.** Collaborations and capsules are never a high.
   - **Core** means the plain, year-round version of a garment, not the cheapest thing that fits the word.
   - **Band rule (women's cuts):**
     - **Tier 1:** a core tee at or under $35 and a core blouse under $80.
     - **Otherwise,** take the mean of the blouse entry and the sweater entry: under $200 is Tier 2, $200 to $600 is Tier 3, over $600 is Tier 4.
     - Propose the band in `band_proposed`. Where the rule reads wrong, say why.
   - **Jimmy Choo** sells no clothing, so the clothing columns are `NONE`. Read women's shoes (core pump entry as the low, top of the range as the high) and note the entry and top handbag prices in `note`. It is banded by its shoe entry, like Manolo Blahnik and Aquazzura on the Explorer: propose the band and say why.
2. **Dials** (`return_dials.csv` and `return_styles.csv`). Read `DIALS_BRIEF.md`, sections A–E, and return for Madewell, American Eagle and Urban Outfitters:
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

   **Jimmy Choo** gets no fabric sample. Return its dials row with the fabric fields `NONE` and only the craft fields read (where it makes the shoes, named makers, made-in share).
3. **Facts** (`return_facts.csv`, columns of `return_facts_template.csv`, one row per brand):
   - what it sells, in one plain sentence under thirty words;
   - the channels it sells through;
   - founding year, place and founders;
   - who owns it today, with a filing where one exists (J.Crew Group, American Eagle Outfitters, URBN and Capri Holdings all file or publish annual reports);
   - its signature product;
   - pronunciation, if the brand states it;
   - lookbook;
   - Vinted women's URL and The RealReal page;
   - B Corp and GOTS status, from the certifiers' own directories;
   - one real quotation, under `rules_quotes.md`.
4. **Social, while you're on the site:**
   - its Instagram and TikTok handles, linked from its own site (the main US account, not a men's or regional one);
   - the follower count each profile shows.

   Put these in `NOTE_1.md`. Read only: never follow, like or message.

## Rules

- **Names** must match `canonical_keys.txt`. Run `python3 reconcile.py` before each return.
- **Cell values:**
  - `NC`: nobody looked.
  - `NONE`: the brand doesn't sell or do it.
  - `np`: checked, and no price is published.
  - `ND`: the page was read and states nothing.
  - No empty cells.
- **Bot walls:** one plain try. If a check box appears, ask Sebastian once whether he'll clear it himself. Anything else is `held`, with the wall named. Never work around a wall.
- **Pace:** one page at a time, at a human pace. Don't touch the map.

## Return and time box

1. **Part 0, each brand as it finishes:** `doors/<brand>/return_doors.csv`, `return_counts.csv` and `NOTE_0.md`.
2. **Part 1, all four together or one at a time:** `womens/return_prices.csv`, `return_dials.csv`, `return_styles.csv`, `return_facts.csv` and `NOTE_1.md`.

Allow fifteen minutes for each brand's Part 0 (forty-five for American Eagle) and about an hour for each brand's Part 1 (thirty minutes for Jimmy Choo). Past the box, return what you have, put `NC` on the rest, and say so.
