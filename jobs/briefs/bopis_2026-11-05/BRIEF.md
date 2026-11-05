# bopis_2026-11-05: which brands offer buy online, pick up in store

**Issued** 5 November 2026 · **Kind** research read (browser and web) · **243 brands, a pilot of ten and ten runs of 25** · **Returns to** the Spectrum thread

Read only. You gather and propose; Sebastian rules.

## The question

Of the brands with five or more of their own US stores, how many let a customer buy online and pick the order up in one of those stores (BOPIS)? We want a yes, none or unclear for each brand, with the brand's own words as the evidence. The Spectrum thread does the counting from your rows.

## What counts

BOPIS is **yes** only when all of these hold:

- the brand's own US website sells the product;
- the customer pays online (or the order is placed online and paid for there);
- the customer collects it at a **brand-owned US store**.

These do not count as BOPIS. Record them in their own columns:

- **Reserve in store:** the customer holds an item online to try on, and pays at the store. Set `reserve_in_store` = `yes`. `bopis` stays `none` unless there is also a pay-online pickup.
- **Curbside:** a way of doing pickup, not a separate service. Set `curbside` = `yes` only when the brand offers pickup too.

Pickup that happens somewhere else does not count:

- at a department store or retailer (Nordstrom, Saks, Neiman);
- at a locker, post office or carrier point;
- at a stockist.

Ship-to-store counts as BOPIS, with `timing` = `later`. Same-day or "ready in hours" is `same_day`. If a brand offers both, `both`.

## The worklist

`worklist.csv` holds 243 brands: every brand on the men's map and The Cyprus Brand Explorer with **5 or more own full-price US stores**. Outlets, concessions and department-store counters are not counted toward the five. The count is the one each map already shows (`own_us_stores`, with `count_source` naming the map).

It is in reading order: the pilot first, then `run1` to `run10`, biggest store counts first. The columns are the run, the order, the brand, the maps it is on, its store count, its band or tier and its site.

Ten brands on the maps have no store count and are not in the pack: Dickies, G.H. Bass, Helmut Lang, Katin, Koio, Perfect Moment, Quoddy, RVCA, Woolrich and Y-3. Don't add them.

## For each brand

Return one row in `return.csv`, with the columns of `return_template.csv`. The example row is invented; do not copy its values.

- **`ecom_us`:** `yes` if the brand's own US site sells its product; `no` if it does not sell online in the US (some houses only show the range); `NC` if you could not tell.
- **`bopis`:** `yes`, `none` (the brand does not offer it) or `unclear` (the pages disagree, the evidence is behind a cart, or the brand says "select stores" without naming them).
- **`timing`:** `same_day`, `later`, `both` or `ND` when bopis is `yes`. `NONE` when bopis is `none`.
- **`scope`:** `all` (every own full-price store), `select` (the brand names some stores or says "participating"), `outlets_only` or `ND`. `NONE` when bopis is `none`.
- **`fee`:** `free`, `paid` (put the amount in `note`) or `ND`. `NONE` when bopis is `none`.
- **`reserve_in_store`** and **`curbside`:** `yes`, `no` or `ND`.
- **`source_kind`:** `help_page`, `product_page`, `store_page`, `site_banner` or `other`.
- **`source_url`:** required for every `yes`. For a `none`, give the help or shipping page you read.
- **`quote`:** the brand's own words, 15 words at most and verbatim, such as "Free in-store pickup". For a `none`, the exact heading of the delivery page you read, or `ND`.
- **`confidence`:**
  - `high` for a `yes`: the option is on a product page or store page and the brand's help page states it.
  - `medium` for a `yes`: one of those.
  - `low` for a `yes`: seen only indirectly. Say why in `note`.
  - For a `none`, see the checks below.
- **`read_date`** and **`note`:** the date you read it. Use `note` for anything a reader needs: a fee amount, a store subset, a pickup window, or a wall you hit.

## Rules

- **The brand's own US site is the only source.** No press, no reviews, no Google, no store-finder apps, no third-party pages. If the brand's site is a global site, set it to the United States first.
- **Where to look, in this order:** the help or FAQ page on shipping and delivery; the shipping options listed on a product page; the store locator or a store page; the site banner or footer. A phrase to search is "pick up", "pickup", "click and collect", "collect in store", "store pickup", "ship to store", "BOPIS".
- **Store availability checkers.** You may type a public ZIP (02116 for Boston, 10001 for New York, 90210 for Los Angeles) into a brand's store availability or pickup checker. Don't enter a name, email, phone number or street address.
- **No cart, no checkout.** Do not add anything to a cart and do not start checkout. If the only place the option could be seen is the cart, return `unclear` with `note` = `cart_only`. List those brands at the top of the run note. Sebastian will rule on whether to allow adding an item to a cart (with no purchase).
- **`none` checks.** Two places on the brand's own site that discuss delivery and are silent on pickup is a `none` at medium confidence. Three (help page, a product page and the store locator) is high. Name them in `note`.
- **Sub-lines are read on their own.** Carhartt WIP is not Carhartt. A brand's outlet site is not its full-price site.
- **Brands with a partner-run site.** If the US site is run by a partner and not the brand, set `ecom_us` to `yes`, say so in `note`, and read what the site offers.
- **Cell values.** `NC` means nobody looked or you were blocked; `ND` means the page doesn't state it; `NONE` means the brand does not do it. No empty cells. Never leave a blank and never write 0.
- **Read only.** Don't sign in. Never buy, sign up, follow, like or message. Keep private account details out of returns.
- **Pace.** One page at a time, at a human pace.
- **Bot walls.** One plain try. If a check box appears, ask Sebastian once. Anything else: move on, mark the row `NC`, and name the wall in `note`. If a tool refuses a page, don't work around it.
- **Names.** Use the brand name exactly as it appears in `worklist.csv`. Run `reconcile.py` on your names before each return (`python3 reconcile.py names.txt`, with `canonical_keys.txt` beside it) and fix any near misses.

## Order, return and time box

1. **Pilot (ten brands):** J.Crew, Lululemon, Levi's, Patagonia, Alo, Hermès, Chanel, Gucci, Veronica Beard and Todd Snyder. They are chosen to cover a large chain, a small chain, a luxury house and a brand that may not sell online. Return `pilot/return.csv` and `pilot/NOTE.md`, then stop and wait for Sebastian's word.
2. **Runs 1 to 10:** work down `worklist.csv` in order. Return each run of 25 as `run<N>/return.csv` and `run<N>/NOTE.md` as it finishes (run 10 has 8).
3. **Each NOTE.md** starts with the `unclear`, `cart_only` and low-confidence rows. Then give the run's counts: how many `yes`, `none`, `unclear` and `NC`, and of the `yes` rows how many are `same_day`, `later`, `both` and `ND`.

Allow about three minutes a brand. Past the time box, return what you have and put `NC` on the rest.
