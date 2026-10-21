# NOTE_1: Kirna Zabête, women's read (add_kirna_zabete_2026-10-20, Part 1)

Read 20 Oct 2026 in Chrome from kirnazabete.com. Files: `return_designers.csv` (118 rows), `return_prices.csv` (2 rows), `return_facts.csv` (1 row).

## Own label: yes
Kirna Zabête sells its own label, listed under the vendor name "Kirna Zabête Exclusive Collection" (73 styles; mostly dresses, tees, sweaters and trousers; no jeans or shoes). It is the second row in `return_prices.csv`. Its prices sit at $95 to $695, far below the store.

## How the prices were read (a method change you should know about)
The site draws its listings with JavaScript. I read each designer's collection through the store's own collection data feed (`/collections/<designer>/products.json`), not by scrolling the pages. It returned all 118 designer collections and 2,386 styles, with sale markings. The brief asked for the listing pages, so this is a different source for the same listings. The cell for each product gives its URL.

- **Full price:** low = cheapest style not marked down. High = highest pre-markdown price, so a marked-down style can be the high (tee and blouse highs are).
- **Excluded:** capsule, collab, archive, vintage, unique and Levi's x sacai styles; leather and suede from the outerwear high (and low).
- **Garment types** follow the store's own labels. Sweater excludes cardigans. Dresses exclude gowns.
- **Own label** is included in the whole-store row. Two store lows are own-label styles (tee $95, trousers $315).

## What the numbers say
Starting prices: blouse $200, sweater $220 (mean $210) puts the store in **Tier 3**. Medians: blouse $890, sweater $780 (mean $835) put it in **Tier 4**. The rule was written for a single brand, so I propose Tier 3 on the cuts as written and flag that the median reading is Tier 4. The own label alone is Tier 3 (mean $350, from only 2 full-price blouses and 6 sweaters). Your ruling.

Other store medians: tee $105, jeans $620, trousers $960, dress $1,490, outerwear $2,250, shoes $1,020. Blouse and sweater 90th percentiles: $1,950 and $2,200.

## Things I could not settle
- **Trousers high** ($4,600) is a pair of Khaite leather pants. The leather rule covers outerwear only, so I kept it and flagged it.
- **Outerwear low** (Dodiee fringe bolero, $650) is not checked for suede.
- **Tee high** ($1,200) is an Alaïa knit top the store files as a tee, on markdown.
- **"Consignment" tag:** 537 styles carry a price tag reading consignment. The one I opened was a new raffia bag, so I kept them. Not verified.
- **Own-label outerwear:** the only style (The Blazer) is marked down from $695 to $278, so there is no full-price low (`ND`).
- **Designer list:** includes non-clothing designers (jewelry, books, home, fragrance) because the brief asked for every designer. `Pepela` has a collection page with 0 styles. 19-69 and `Girl W/ Knife`, `Tay Ham` and similar are tiny collections. `price_low` is `ND` for 23 designers: 22 where every style is on markdown, plus Pepela (no styles).

## Facts
- **Founded** 1999, New York (96 Greene Street, SoHo). **Founders:** Beth Buccini and Sarah Easley (The Zoe Report). The site names only Beth and an unnamed college friend.
- **Owner:** Beth Buccini, sole owner since the end of 2015 (About page). Private; no filing found.
- **Channels:** I wrote `O;D` (own stores, own website). The template's `O;D;W` codes are not defined anywhere in the brief, so this is a guess.
- **Quote:** from The Zoe Report, not the brand's own site, because the site's own press page links out. Verified word for word on the page. The page shows no date (`ND`).
- **Pronunciation** "KEER-NAH ZAH-BETT" comes from the Instagram bio linked from the site, not the site itself.
- **Vinted:** brand id 869887, 151 listings. Some may be the Kirna Zabête x Target line (not checked).
- **TheRealReal:** no brand page. `/designers/kirna-zabete` returned 0 items (`NONE`).
- **B Corp** directory search: 0 results. **GOTS** database search "Kirna": no records. Both returned `no` / `NONE`.
- **Lookbook** columns: `NC`. The brief does not ask for them.

## Social
Instagram (the only social link on the site): **@kirnazabete**, 92.9K followers, 2,347 posts, 836 following, as the profile showed it. No TikTok linked. Read only; nothing followed or liked.

## Where the brief or the site was wrong
- The site contradicts itself on store count ("four" and "seven"); see `NOTE_0.md`.
- `reconcile.py` reports "Kirna Zabête (own label)" as unmatched against the key "Kirna Zabête". The brief requires that name, so it is intentional.
- The brief says the median is easy to give "if the listing makes that easy". It was, but the median and the starting price put the store in different tiers; that is the finding.
