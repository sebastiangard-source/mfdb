# add_kirna_zabete_2026-10-20: Kirna Zabête, for the Cyprus Brand Explorer

**Issued** 20 October 2026 · **Kind** seating read · **One business, two parts** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job on Kirna Zabête's own US site and store pages. If you cannot run a browser, say so and stop. **You gather and propose; Sebastian rules.**

## The business, and how it differs

**Kirna Zabête** is a women's fashion boutique founded in New York, with stores of its own under the Kirna Zabête name. Unlike the other brands on the Explorer, it is **a multi-brand store**: most of what it sells is made by other designers.

The Explorer usually places a brand in a tier by the starting price of its own blouse and sweater. For a store, that rule needs the designers it sells, so this brief asks for those too. Sebastian will rule on how it is placed.

Find out early, and say in `NOTE_1.md`, whether Kirna Zabête also sells **its own label**. If it does, read that label as a brand, as in Part 1 below.

## Part 0: stores (`doors/`), first, returned on its own

Use the store pages on Kirna Zabête's own site only. Return:

- `return_doors.csv` (`return_doors_template.csv`): one row per Kirna Zabête store, US first.
  - `format` is `own-door`, `outlet` or `pop-up`.
  - `status` is `open` or `opening`.
  - Closed stores are not returned.
- `return_counts.csv`: US own stores, outlets and pop-ups counted separately.

The rules in `rules_doors_reference.md` hold, with these rulings:

- **Venue only from the site:** a center it names, otherwise `street`. Never work it out from the address.
- **Same address, one store.** If the site lists one store twice, return it once.
- **Seasonal or summer shops** (for example in the Hamptons) are `pop-up` if the site gives dates or calls them seasonal, and `own-door` if it lists them as permanent. Say which in `note`.
- **Shops inside another retailer** are not rows. Count them in `us_concessions`.

## Part 1: what it sells and at what price (`womens/`)

1. **The designers** (`return_designers.csv`, columns of `return_designers_template.csv`).
   - Read the site's designer list and give one row per designer it sells: `designer`, the listing URL, the number of styles listed, and the lowest and highest full-price item shown.
   - Don't scroll to count. Where the listing doesn't show a count, put `ND`.
2. **Prices** (`return_prices.csv`, columns of `return_prices_template.csv`).
   - Read the same eight garments as for a brand: tee, blouse, sweater, jeans, trousers, dress, outerwear and shoes. Read across the whole store, from the site's own category listings.
   - For each garment, give:
     - **low:** the cheapest full-price item;
     - **high:** the top of the regular range;
     - the product name, designer and URL behind every figure;
     - `basis` = `range`.
   - **Leather and suede are never the outerwear high**, and nor are capsules, collaborations or one-of-a-kind pieces.
   - In `note`, give the **median** blouse and sweater price if the listing makes that easy. For a store, the median says more than the cheapest item.
   - `band_proposed`: your reading at the women's cuts (blouse-and-sweater mean under $200 is Tier 2, $200 to $600 is Tier 3, over $600 is Tier 4). Say plainly that the rule was written for a single brand.
3. **Own label.** If Kirna Zabête sells its own label, add a second row to `return_prices.csv` with `brand` = "Kirna Zabête (own label)", read as a single brand.
4. **Facts** (`return_facts.csv`, columns of `return_facts_template.csv`):
   - what it sells, in one plain sentence under thirty words;
   - the channels it sells through;
   - founding year, place and founders;
   - who owns it today, with a filing where one exists;
   - its best-known designers in `signature_product`;
   - pronunciation, if the site states it;
   - The RealReal and Vinted pages, if any (`NONE` is likely, since it's a store);
   - B Corp and GOTS status, from the certifiers' own directories;
   - one real quotation, under `rules_quotes.md`.
5. **Social:** Instagram and TikTok handles linked from its own site, with the follower count each profile shows, in `NOTE_1.md`. Read only: never follow, like or message.

There is no fabric, tech or craft read for a multi-brand store.

## Rules

- **Names** must match `canonical_keys.txt`. Run `python3 reconcile.py` before each return.
- **Cell values:**
  - `NC`: nobody looked.
  - `NONE`: it doesn't sell or do it.
  - `np`: checked, and no price is published.
  - `ND`: the page was read and states nothing.
  - No empty cells.
- **Bot walls:** one plain try. If a check box appears, ask Sebastian once whether he'll clear it himself. Anything else is `held`, with the wall named.
- **Pace:** one page at a time. Don't touch the map.

## Return and time box

1. **Part 0:** `doors/return_doors.csv`, `doors/return_counts.csv` and `doors/NOTE_0.md`. Return these straight away.
2. **Part 1:** `womens/return_designers.csv`, `return_prices.csv`, `return_facts.csv` and `NOTE_1.md`.

Allow fifteen minutes for Part 0 and about forty-five for Part 1.
