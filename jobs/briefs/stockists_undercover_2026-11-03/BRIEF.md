# stockists_undercover_2026-11-03: shop records for Undercover's 14 US stockists

**Issued** 3 November 2026 · **Kind** stockist · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. Everything below assumes it. **You gather and propose; Sebastian rules.**

## Why

Undercover has no stores of its own in the US. Its stockist page (https://undercoverism.com/stockist) named 14 US shops when we read it on 8 October 2026. None of them are in our shop register, so the map can't show where to buy Undercover. This brief gets each shop to the standard that Ellicott & Co. and the Northeast shops meet. Then the shops can go in as stockists, and their brand lists can link to the rest of the map.

## The job

### 1. Re-read the locator first

Open https://undercoverism.com/stockist. Filter to the United States and compare what it lists with `worklist.csv`.

- **A shop gone from the page:** keep its row and set `undercover_listed = no`.
- **A new US shop on the page:** add a row at the end, numbered from 15.
- **Lines carried (MENS, WOMENS):** copy them into `undercover_lines` exactly as the page shows them today.

Return that check by itself, before any shop records. Put it in the first section of `NOTE.md`.

### 2. A full record for the eight independents

Rows 1–5, 7, 12 and 14: the two Dover Street Markets, Alan Bilzerian, Blake, Ikram, Maxfield, Nakamuraya and Relish.

For each shop, fill one row of `return_template.csv`, the same columns Ellicott & Co. used, with these fields:

- **Where it is:** street, city, state and ZIP, read from the shop's own site. If the site's address differs from the locator's, use the site's and say so in `note`.
- **What it is:** the shop's `type` and `gender`. Use `womens_with_mens_tail` where the shop is mainly women's but carries some men's.
- **Who owns it, and since when:** `founded`, `owners`, and `ownership` (independent, family-owned, part of a group, and so on).
- **The hours it keeps.**
- **Its brand list,** read from its own source: a Designers or Brands page, the shop's vendor filter, or its menu. Name the source in `brand_list_source` and give the full count in `brand_count`.
- **The brands we already have:** run `python3 reconcile.py names.txt` on that list. Put the exact canonical names that match in `matched_brands`, separated by `;`, and their count in `ub`. A near miss is a rewrite, not a new brand. Don't sift the unmatched brands. Just keep the full list in `NOTE.md` under the shop's name.
- **A story** of three to six sentences, in the register of `shop_example.json`: facts, dates and names, with no adjectives the source didn't supply.
- **Whether Undercover is on the shop's own site.** Set `undercover_on_shop_site` to `yes` when the brand list or the product pages show it, `no` when they don't, and `NC` when the shop doesn't publish one. A `no` doesn't overrule the locator. It just tells us how fresh the link is.

**Watch these shops:**

- **Dover Street Market** has two US doors. They share one website, but each gets its own row, with the store-level details from the site's page for that store. The brand list can be the same for both; say so in `note`.
- **Blake** has a common name. Confirm that the shop at 212 W Chicago Ave is the one you're reading.
- **Ikram** has a common name. Confirm that the shop at 15 East Huron St. is the one you're reading.
- **Alan Bilzerian** is the only one in the Northeast. Do it first.

### 3. A short record for the other six

**Kith, 337 Lafayette St (row 10).** Kith is already on the map as a brand, and this address is already one of its own stores. Fill in the address, hours and `undercover_on_shop_site`. Check whether kith.com sells Undercover. Write `NC` for the story, owners and brand list, and put `already on map as Kith own store` in `note`.

**The five Nordstrom doors (rows 6, 8, 9, 11 and 13).** Department stores are recorded but not seated as stockists unless Sebastian rules otherwise. For each door, give:

- the address and hours from nordstrom.com's store page;
- whether nordstrom.com sells Undercover online, and which lines;
- whether the store page says anything about Undercover or a designer department.

Write `NC` for the story, owners and brand list.

## Rules

- **Names.** Brand names in `matched_brands` match `canonical_keys.txt` exactly. Shop names are written the way the shop writes its own name (Dover Street Market Los Angeles, not DOVER STREET MARKET LOS ANGELES).
- **No empty cells.** `NC` means nobody looked. An empty cell is an error.
- **One source per row.** Put it in `source`, and use the shop's own page where there is one. A press piece can carry the story or the founding facts. Name the outlet in `note`.
- **Bot walls.** Give each one a single plain try. If a check box appears, ask Sebastian once whether he'll clear it himself.
- **Read only.** Don't sign in, add to cart, sign up, follow or message anyone.
- **Don't touch the map.** Don't rebuild anything. Return `return.csv` and `NOTE.md`, nothing else.

## Time box

- Ten minutes on the locator check, then return it.
- Twenty minutes for each full record.
- Ten minutes for each short record.
- Past the limit, return what you have and write `NC` with a note.
