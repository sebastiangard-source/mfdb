# NOTE — seat_saint_croix_2026-11-06 (Saint Croix)

Read 6 November 2026. Status: **partial only because GOTS could not be read** and a few cells carry caveats (below). Everything else is filled and sourced.

## Files returned
`return.csv` (132 columns, one row), `return_styles.csv` (171 styles), `return_categories.csv`, `return_fibres.csv`, `return_lines.csv`, `own_doors.csv`, `stockists.csv`, `facts_first.csv` (the early row), this note.

## Added for the updated brief (dials and neighbourhood)
- `dials.csv`: 38 rows, one per dial, each with a proposed score, a counted or quoted fact, a URL and a confidence. Scope: men's feed (210 records; 171 clothing styles), all 171 descriptions read via the feed, 13 men's product pages read with photos, plus FAQs, About, Sourcing, the home page and two collection pages.
- Two dials are `NC`: `golffice` (no occasion copy at all) and `sail` (no boating register).
- Lower-confidence calls Sebastian may want to look at first: `finbro` (1 by the brand's pages, but 19 quarter-zips and 9 vests are 16% of the range), `ital` (3: half the clothing is Italian-made, but the brand frames it as complementary), `dur` (4, with the lifetime-repair promise arguing for 5), `bruv`, `status`, `prep`, `outdoor`.
- Scale floors: where a dial's floor is 1 and the brand has nothing (denim, fren, briish, scandi, street, avant, weird, ivy) I scored 1 and said "none found"; where the dial has a 0 tier or says "down to a single item" (boat, racquet, ski, western, rock, workwear, surf, shoes) I scored 0.
- Neighbourhood for the Chicago door: Magnificent Mile, in `own_doors.csv` `note`. The Chicago store's brand-run status is still unconfirmed (see below).

## What was read
- **Store/currency:** saintcroix.com, Shopify US storefront (`Shopify.country` US, currency USD, rate 1.0). Two displayed prices matched the feed: Tattersall Cotton Shirt $295, Boiled Wool Jacket $1,800. The site also has en-gb and en-ca markets (not read).
- **Men's scope:** the seven `/collections/mens-*` feeds. Their union is 210 records and equals `mens-ready-to-wear`. The other 46 store products are women's and excluded. In scope = **171 clothing styles**; out of scope = 38 socks and 1 golf head cover. (My first-pass figure of 168 was a filter error.)
- **Fibre:** composition and made-in sit in each product's Details block (in the feed's description). All 171 parse and sum to 100. Hash cross-checks confirm the 171 rows, handles and compositions in the file match what the browser held. Lead fibre: 170 natural (112 cotton, 50 wool, 3 silk, 3 cashmere, 2 linen) and 1 synthetic (Five-Pocket Woven Wool Pants, 54% microfiber). Elastane/Lycra on 7 styles, 2 at 5% or more. Microfiber appears in 47 styles, always with no polymer named, so it is filed as other-synthetic. Shape: one.
- **Named lines (brand's own collections, men's clothing):** Classics 26, Performance 16, Limited Release 50, Luxury Fall 2026 50, Luxury Spring 2026 58, Luxury Fall 2025 29. Every line is all-natural by the 90% rule. No synthetic line exists.
- **Doors:** the Stores page is a Stockist.co widget with 33 pins: one named Saint Croix Chicago, and 32 men's-clothing stockists.
- **Founding and ownership:** the brand's own About page: 1960, Bernhard Brenner, Knitcraft Corporation, Winona, MN; 90,000 sq ft site; Miller Waste Mills (Winona) since 2023–24. A brand news post (c. 2015, undated) names Brenner as founder and says the brand gives factory tours.
- **Secondhand:** Vinted brand "St. Croix" (id 2993196): 390 men's listings. Grailed designer "St. Croix": 419 listings. Brand spellings: Vinted's API returned 403, so I did not check for other spellings; the Vinted brand may include other St. Croix labels.
- **Search URL:** `/search?type=product&q=` returned 32 product links for "sweater".

## Contradictions and corrections to the brief
1. **"No prices on the home page"** is true of the home page text only. Collection and product pages show them.
2. **Made in the USA is half the clothing range.** The brand says all knitwear is "fully produced in America" and only "select complementary pieces" are made in Italy. On product pages, 86 of 171 men's clothing styles say Made in Italy, including 77 of 79 shirts. One knitwear style (a quarter-zip hoodie) says Italy. No maker is named. Socks all say Italy; USA covers 85 clothing styles (52 of 53 knitwear, 20 of 21 polos and tees, 10 of 13 outerwear).
3. **Chicago may not be brand-run.** The brand has its own page for Saint Croix Chicago (900 N. Michigan Ave, Level 3, Suite L3-10; manager named; email at stcroixshop.com) but does not say it is company-owned. A tourism page describes the older "St. Croix Shops" as independently owned, and the Edina Galleria shop is listed closed. So `own_doors_us = 1` is a locator-based count and may be 0. Sebastian rules.
4. **Founding year:** the brand's own timeline says 1960; Visit Winona says Winona roots in 1964. I used the brand's. Wikipedia's St. Croix (clothing) entry is unsourced and gives no year.
5. **Handle/title mismatch:** style 4143 "Pinstripe Jacquard Wool Sweater" carries the handle `cloque-knit-cotton-polo-3360`; confirm the page before using the URL (flagged in `return_styles.csv`).
6. **The Stores page** returns only its heading as page text; I read the widget's location list.
7. **Name variants:** site and copyright line say "Saint Croix"; resale and older labels say "St. Croix"; the older brand site was St. Croix Collections.

## Prices (men's, regular price, USD)
Entry $295 (woven cotton shirts); top $1,800 (Boiled Wool Jacket, Limited Release). Jeans and shoes are NONE. Caveats:
- Tee: 3 jersey tee styles, all $385 (Mock Neck Tee, Tee, Banded Tee).
- Dress shirt is the casual woven button-front, $295–$410.
- Dress pants: 3 trousers; the top, Interlock Wool-Silk-Cashmere Pants ($1,150), is a knit.
- No elevated-fibre crewneck exists, so the sweater high is the dearest crewneck (merino wool, $1,290).
- Outerwear is 8 vests, 2 shirt-jackets and 3 jackets; jackets alone are $1,450–$1,800.
- Sale: the feed carries one compare-at price in the men's range; the Archive Sale shows "70% OFF" and none of it was used.

## Proposed craft (Sebastian rules): 4
Owned Winona mill and a dated history argue for 5 on knitwear; the Italian-made shirts and unnamed makers and mills hold the whole range at 4. Evidence: the About and Sourcing & Technique pages.

## Not resolved
- **GOTS:** the certifier database would not load in the browser, and it is robots-blocked for the fetch tool. Left `NC`. A web search found no GOTS claim by the brand.
- **B Corp:** the directory search for "Saint Croix" returned no entry by that name, so I recorded `NONE`. The directory shows a relevance-ranked list and I read the first page only; treat as medium confidence.
- **Pronunciation:** the brand states none. "saint KROY" is the St. Croix River's pronunciation (Wikipedia IPA /ˈkrɔɪ/); recorded as unconfirmed for the brand.
- **Tech score:** `proposed_tech` is `NC`; no tech rubric was in the folder. Evidence is in the `tech_*` cells.
- **Lookbook:** `NONE`. I found none in the navigation, footer, blogs or sitemap; the news blog is stale (2015).
- **Signature product:** `NONE`. The brand calls the knit-in collar stay a "signature" technique (a technique, not a product).

## Out of scope but noticed
- The brand began a womenswear expansion in 2025 (not read).
- Miller Waste Mills now recycles unused Saint Croix material (brand claim).
- Nothing was signed into, added to a cart or submitted. I declined non-essential cookies on saintcroix.com.
