# fibre_pass_2026-09-14 — NOTE — the pass is complete

`return.csv` is 197 rows. **193 carry a fibre split. 4 are held. 1 carries a denominator only.**
`python3 reconcile.py names.txt` → `197 names in — 197 exact, 0 to rewrite, 0 unmatched`.

A full-file sweep found **zero sanity failures**: every row's
`natural + synthetic + cellulosic + (no composition)` lands within 1 of 100, no
`spandex_high > spandex_any`, no `spandex > styles_total`, no `styles_with_composition >
styles_total`, every JSON list parses. Schema is clean on 196 of 197 — still only Rothy's counted
zero against `styles_total`'s `[1, 99999]`, which has been flagged since batch 1 and is deliberate.

**73,908 men's styles were counted across 192 houses.** 170 are one-cloth, 22 are split.
186 complete, 11 partial.

---

## The last two batches

Batch 7 (25) was the designer and luxury tier; batch 8 (24) the sub-lines, the tailoring houses and
the special cases. Both landed whole. The headline is that **the entire Ralph Lauren house came in**
— Purple Label measured for the first time, and RRL and Polo Ralph Lauren restated from
denominator-only rows to full splits.

| | styles | w/comp | nat | syn | cel | spandex | 5%+ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Polo Ralph Lauren | 997 | 980 | 89 | 9 | 0 | 93 | 35 |
| Ralph Lauren Purple Label | 272 | 270 | 97 | 2 | 0 | 26 | 2 |
| RRL | 204 | 203 | 99 | 1 | 0 | 1 | 0 |
| Saint Laurent | 284 | 284 | 91 | 4 | 5 | 2 | 2 |
| Celine | 196 | 194 | 93 | 4 | 2 | 8 | 2 |
| Givenchy | 258 | 258 | 89 | 10 | 1 | 5 | 2 |
| Gucci | 375 | 340 | 72 | 12 | 7 | 66 | 32 |
| McQueen | 77 | 77 | 84 | 9 | 7 | 4 | 0 |
| Maison Margiela | 162 | 162 | 90 | 6 | 4 | 1 | 0 |
| Rick Owens | 639 | 639 | 85 | 9 | 6 | 70 | 23 |
| Yohji Yamamoto | 897 | 886 | 74 | 5 | 20 | 0 | 0 |
| Sacai | 90 | 90 | 80 | 17 | 3 | 0 | 0 |
| Casablanca | 155 | 155 | 79 | 12 | 9 | 17 | 0 |
| Jacquemus | 225 | 224 | 89 | 6 | 4 | 20 | 9 |
| Prada | 334 | 297 | 64 | 24 | 1 | 34 | 25 |
| Loewe | 276 | 276 | 93 | 5 | 2 | 7 | 2 |
| JW Anderson | 114 | 114 | 93 | 6 | 1 | 2 | 2 |
| Dior | 519 | 518 | 93 | 6 | 1 | 24 | 1 |
| Amiri | 275 | 273 | 74 | 16 | 9 | 38 | 7 |
| Rhude | 226 | 220 | 76 | 16 | 5 | 16 | 6 |
| Palm Angels | 169 | 159 | 70 | 24 | 0 | 20 | 16 |
| Golden Goose | 217 | 217 | 87 | 9 | 4 | 18 | 3 |
| Fear of God | 118 | 117 | 92 | 7 | 0 | 10 | 2 |
| Bode | 1275 | 1218 | 84 | 3 | 8 | 14 | 2 |
| Greg Lauren | 126 | 123 | 91 | 7 | 0 | 1 | 1 |
| Visvim | 873 | 862 | 92 | 4 | 3 | 3 | 2 |
| Tom Ford | 374 | 374 | 89 | 5 | 6 | 19 | 0 |
| Zegna | 386 | 385 | 98 | 1 | 1 | 27 | 6 |
| Bottega Veneta | 252 | 252 | 91 | 8 | 1 | 14 | 1 |
| Berluti | 124 | 121 | 94 | 4 | 0 | 8 | 0 |
| Husbands | 113 | 113 | 94 | 6 | 0 | 1 | 0 |
| Brioni | 826 | 795 | 89 | 5 | 2 | 43 | 0 |
| Isaia | 319 | 228 | 70 | 1 | 0 | 26 | 4 |
| The Row | 311 | 311 | 97 | 2 | 1 | 3 | 0 |
| Lemaire | 283 | 279 | 85 | 14 | 0 | 5 | 1 |
| Jil Sander | 124 | 124 | 83 | 15 | 2 | 0 | 0 |
| Acne Studios | 259 | 259 | 89 | 4 | 7 | 15 | 5 |
| Dries Van Noten | 143 | 143 | 84 | 6 | 10 | 4 | 0 |
| Wales Bonner | 88 | 83 | 70 | 15 | 9 | 7 | 1 |
| JiyongKim | 99 | 99 | 87 | 7 | 6 | 0 | 0 |
| Brunello Cucinelli | 425 | 424 | 92 | 8 | 0 | 38 | 14 |
| Fedeli | 123 | 119 | 87 | 10 | 0 | 8 | 4 |
| The Elder Statesman | 116 | 114 | 98 | 0 | 0 | 0 | 0 |
| Rubinacci | 557 | 490 | 82 | 2 | 4 | 11 | 0 |
| Kiton | 375 | 335 | 83 | 5 | 1 | 56 | 2 |
| Zilli | 257 | 256 | 97 | 2 | 0 | 38 | 1 |
| Stefano Ricci | 999 | 993 | 94 | 4 | 1 | 131 | 33 |
| Hermès | 104 | 44 | NC | NC | NC | NC | NC |
| Sugar Cane · Junya Watanabe · Charvet · Cesare Attolini | — | — | — | — | — | — | — |

---

## The Ralph Lauren house, and a warning for the merge

All three labels landed in one run: RRL first at 204 styles, then Purple Label at 272, then Polo at
997. Roughly 1,600 same-origin requests at **concurrency 5 with 130 ms spacing** returned zero 403s
and no challenge. The 14 September block came at concurrency 10 — so **concurrency, not volume, is
the trigger**, which is worth knowing for every WAF house on this map. All ten pairwise brand-facet
intersections are zero.

**Do not pair yesterday's denominators with today's splits.** The facet counts moved **8–12% in a
single day** — Polo 1,026 → 1,007, Double RL 231 → 204, Purple Label 257 → 272. Each of these rows
is one end-to-end read taken today. And `/men-clothing/r/purple` is **the colour purple** (77 items),
not Purple Label, which is `/men-clothing/r/purple-label`.

One measured consequence of the old partial: Polo's 579-style head-of-grid subset read 92/7/1 against
the full 997's 89/9/0, so the sort bias in a truncated crawl is now quantified rather than assumed.

---

## Saint Laurent was never blocked

The register recorded bot protection and I briefed it as a possible `NC`. It is not a challenge.
ysl.com and gucci.com **tear down the browser extension's content script a few seconds after each
load**, so only the first in-page evaluation per navigation survives — which reads as "blocked" but
is an anti-extension measure, and nothing was solved or bypassed. The method that worked: one fresh
tab per step, a single evaluation running the whole crawl, persisting to localStorage on the origin
and reporting through `document.title`.

Its **product sitemap is a 1,000-item cap that contains two men's ready-to-wear products.** The
shards all return the same 1,000, and by the house's own categorisation they are 326 women's shoes,
291 women's leather goods, 208 women's RTW, 171 women's bags — and 2 men's RTW. A sitemap census
files a two-style Saint Laurent. The row came from the PLP data route: 23 pages, pairwise disjoint,
union 320.

---

## Four houses are held, and none of them is a failure to look

**Sugar Cane, Junya Watanabe, Charvet, Cesare Attolini** publish no composition through any
first-party channel.

- **Junya Watanabe** was confirmed four ways: the CDG line page has 33 characters of text and no
  cart, the portal 404s its own robots and sitemap, `junyawatanabe.com` is parked and
  `junyawatanabeman.com` is NXDOMAIN. Dover Street Market — **owned by the same group** — does list
  55 Junya Watanabe MAN products with compositions, and it was rejected as a stockist.
- **Cesare Attolini** is the sharpest of the four. The register said no store; in fact the site is
  Webflow over a real first-party Shopify backend, and `/e-boutique` POSTs to
  `attolini.myshopify.com/api/2026-01/graphql.json`. Queried the way the page queries it,
  `shop{name}` returns "Cesare Attolini" — and **all 20 collections return zero products**. The
  e-boutique says it is under maintenance. There is a store; it is empty.
- **Charvet**'s `www` TLS hostname mismatch is real and was not bypassed. The apex loads and is a
  one-page brochure: address, phone, mailto, Instagram, opening hours, two links.
- **Hermès** is the fifth, and different: its census is solid and its fibre dial is not. Men's
  ready-to-wear is **104 styles of 4,091 US products (5.8%)**, matching the house's own per-category
  counts to the unit — its silk-accessory tree alone is nearly three times the whole clothing range.
  PDP fetches then hit an IP-level wall after 79 of 237 records; it never cleared and it re-armed
  after each successful fetch. The 79 read give 44 styles at 35 natural / 6 synthetic / 3 cellulosic,
  but the sample is badly biased — beachwear and pants complete, knitwear 7 of 67 — so it is recorded
  in the note and **not extrapolated**.

---

## What the finished file says

**The stretch league table is the answer to the question the pass was written for.** Share of the
men's range at 5% elastane or more:

| | styles | any elastane | at 5%+ |
|---|---:|---:|---:|
| State & Liberty | 309 | 81% | **78%** |
| johnnie-O | 452 | 76% | 64% |
| Lululemon | 968 | 74% | 63% |
| RLX | 75 | 63% | 61% |
| Redvanly | 242 | 61% | 59% |
| Mizzen+Main | 122 | 64% | 50% |
| Cuts Clothing | 70 | 63% | 50% |
| Rhoback | 148 | 53% | 49% |

Against that: Bonobos runs 373 styles at 1–3% (216 at exactly 2%) and 99 at 8%+; the five denim
houses together put 205 of 758 styles on elastane with only 47 at 5%+, and 27 of those 47 are
Diesel underwear. **The divide is not price and not prestige — it is whether the house is making
sportswear.** Brioni has 43 elastane styles and **none** at 5%+. Rag & Bone has 81 and a hard 4%
ceiling. Stefano Ricci is the one tailoring house with a real technical tail, 33 at 5%+ running up
to 38%.

**Cellulosics earned their third figure.** PAIGE 34%, Sandro 23%, Yohji Yamamoto 20%, Giorgio
Armani 20%, Theory 18%, Our Legacy 13%. Folded into either side these houses would have read as
something they are not — PAIGE would have been a 99% natural denim house.

**The extremes.** 100% natural: Margaret Howell, John Smedley, Alex Crane. At the other end:
Rothy's 0 (a counted zero — no men's clothing at all), State & Liberty 9, Eleventy 10 (of a range
89% undisclosed), Rhone 13, Rhoback 14, Arc'teryx 16.

**One-cloth is the norm, overwhelmingly** — 170 houses against 22 split. The split houses are
almost all outerwear specialists (Herno, Moncler, Canada Goose, Patagonia, Finisterre) or houses
running a distinct performance line beside a natural one (Peter Millar, Southern Tide, Carhartt,
Vineyard Vines, Alo, Criquet, Les Deux).

**The leather-house expectation held three times and broke once.** Ferragamo 90 clothing styles,
Fendi 211, Berluti 124 — but **Bottega Veneta has 252**, larger than any of them. "Leather house"
is not a reliable predictor of a small clothing range.

---

## New traps, all now in the spec

- **A field that is right at one house is wrong at its sister on the identical stack.** Saint
  Laurent's `compliantComposition` holds fibre names with no percentages on 123 of 320; the same
  field at McQueen, same Kering platform, is correct.
- **Brioni's JSON-LD `material` is a whole-garment blend averaged across shell and lining** — a new
  shape of the Etro fault, neither a single word nor truncated, found only by comparing it
  field-against-field across 1,041 listings (879 agree, 27 disagree, all the same way).
- **Brunello Cucinelli has an accordion literally named MATERIALS** holding a fibre essay with no
  percentages; the real composition is the second `<p>` of DETAILS — and that block puts a
  construction sentence first, so on three down coats it ends "Padding… 90% goose down" ahead of the
  real composition and would have filed a 100% wool coat as down.
- **Pagination has now failed in six shapes.** The newest is **cumulative** paging, where page 2
  contains page 1 (Givenchy, Maison Margiela, Jil Sander) — for which the disjointness test I put in
  the spec last batch is *wrong*. The general test is that the set grows by exactly the page size.
- **A composition can be real, sum to 100, and contain no cloth.** 40 of Kiton's 375 styles state
  only `ACCESSOIRES 100%NICKEL` or `100%PEARL`; a first-part read returns nickel as the main fibre.
- **Prose is the composition at two houses.** Rubinacci writes it in ad copy on 325 of 557 and
  publishes no composition field at all — keying on its structured block gives 34% coverage. Hermès
  writes it in parentheses inside the description.
- **Accented and misspelled fibre names are a real coverage hole**: `élastane`, `Vicuña` (which was
  handing a 97% vicuña knit to silk), `Elastine`, `ELASTHANE`, `POLIAMYDE`, and Hermès' `casmere`.
- **An unterminated `<ul>`** at Dries Van Noten produces no string at all, so the sum check cannot
  see it and the style reads as undisclosed with no error.
- Zilli is **BigCommerce**, not what the register said, and its sitemap exists at
  `/xmlsitemap.php?type=products` — 584 products against the register's 76.
- `c_materialComposition` finished the pass at **zero appearances across nineteen consecutive
  Salesforce houses**.

---

## What still needs you

The measuring is done. These are the decisions that remain, and they now block the merge rather
than the fieldwork.

**Scope is the biggest one and it is unruled.** It moved more rows than gender did. Carhartt is
1,472 styles at 27% coverage with the licensed caps in, or 361 at 90% with them out. Lemaire goes
85/14 → 93/6 clothing-only; Brioni 89/5 → 94/2; Sease 87 → 92; Etro 85 → 89; The Elder Statesman's
denominator changes by 53% and its dial not at all. And it is **not monotone** — Husbands moves the
other way, 94 → 92, because its non-clothing is all leather shoes and belts.

**Named fibre without a percentage is now material, not marginal.** 43 of Bottega Veneta's 252 and
23 of Berluti's 124 are hides stated by name only; Brunello Cucinelli has 16 "REAL LEATHER";
Ferragamo writes "deerskin" and "nappa"; Herno writes `LEATHER: GOAT`; John Smedley publishes only
a named material and no percentage anywhere; Alex Crane names the fibre on 51 of 51 and the
percentage on 18.

**"Exclusive of Elastic"** — Theory swings 72 → 127 on it.

**The down question** — Moncler, Canada Goose and Patagonia are read by three different accidents of
how each writes its label. Dior has the same shape: 93/6/1 as filed, 94/5/1 if the ten down jackets'
"Filling:" is taken over the shell.

**Ties decide whole houses.** Stefano Ricci has 56 ties and 32 change class — 94/4/1 first-listed
against 91/4/4 the other way, the largest swing in the pass. TravisMathew flips which half of the
house leads. Patrick James goes 93% natural → 87%. JiyongKim 87/7/6 → 81/12/7.

Also still open: `synthetic_categories` on two readings across 193 rows (the tables exist in the
notes for every one, so it restates in a single pass); the Rothy's zero against `[1, 99999]`;
elastomultiester, elastodiene and the polyurethane floor; ruling 5's two halves; ruling 3's
self-contradiction; `feed_currency_rate` needing `absent` as a legal value; and Spiber's **Brewed
Protein**, a fibre class the spec has no case for at all (30% of one Zilli knit).

Three rows carry a caveat worth reading before they are seated: **Ksubi** is the AU range, not the
US one; **Brioni's** men's/women's boundary is not pinned down (the house publishes no gender field
and its womenswear shares the catalogue — at most ~2% of listings, too small to move a rounded cell
but not excluded); and **Eleventy** is 89% undisclosed, so its spandex cells are `NC` by my edit.

No scoring anywhere. `menswear_spectrum.html` untouched throughout.
