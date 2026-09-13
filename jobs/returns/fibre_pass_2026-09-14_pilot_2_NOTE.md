# NOTE — fibre_pass_2026-09-14 rev2, pilot returned whole

**Returned:** `return.csv` (197 rows, rev2's 18 columns, 8 filled, 189 `NC`) and this note. Nothing else.
`python3 reconcile.py names.txt` → **197 in, 197 exact, 0 to rewrite, 0 unmatched.** No blank cells. Every
filled row validates: percentages in range, `natural + synthetic + cellulosic + no-composition = 100 (±1
rounding)`, both category cells parse as JSON, enums legal.

**The eight are now whole records, and they were measured, not re-rendered.** Rev2 asked me to fill the other
half from what I hold. I hold none of it: natural, cellulosic and both spandex counts were never counted here,
on any brand. So the eight were re-read from their own product pages this morning under the rev2 rules. Seven
of the eight now disagree with the pilot's own figures, and two of those disagreements matter more than the
rows do.

## The two that matter

**1. "Composition is structurally absent" was a reading failure on both brands I could test.**

- **Canada Goose: 247 of 247 state a composition — 100%, not 152 of 248 (61%).** The composition is in the
  page payload (`c_materialComposition`) on every men's garment and never enters `document.body.innerText`,
  even with the Materials accordion open. The 39% "hole" was the scraper, not the house.
- **Bonobos: 2,490 of 2,821 (88.3%), not 1,512 (53.6%).** `properties.fabric` is a structured field in the
  server-rendered `__NEXT_DATA__`; a 60-product refetch reproduced 60 of 60. The 331 that genuinely state
  nothing are mostly discontinued records still in the sitemap. **This row is `complete`, not `partial`, and
  Bonobos is not the coverage case the pilot said it was.**

Rev2's stop condition names "where composition is structurally absent" and lists Rodd & Gunn at 94% stating
none. **That list came from the same kind of read, and on the two brands tested it was wrong both times.**
Before any of the remaining brands is written off as `partial`, its composition should be looked for in the
page payload rather than the rendered text: Rodd & Gunn 93.8%, Everlane 49.6%, Alex Crane 43.6%, TravisMathew
28.2%, **J.Crew 24.2% — which is one of your seated seven**. I would not spend the pass on that list as it
stands.

**2. The rule has no tie-break, and ties are not rare.** "Main fibre = the fibre with the highest share in the
first composition" does not say what happens at an exact tie. It happens constantly: **Mack Weldon 29 styles
(12.5% of its range**, mostly `47.5% cotton / 47.5% modal / 5% spandex`), Balenciaga 14 (twelve of them
`50% cotton / 50% polyamide`), Patagonia 11 tees at 50% recycled cotton / 50% recycled polyester, Arc'teryx 4.
All eight rows here resolve **first-listed wins**. Resolve them the other way and Mack Weldon reads
113 natural / 78 synthetic / 40 cellulosic instead of 137 / 76 / 18, Balenciaga's synthetic goes 14% → 17%, and
**Patagonia's Tops category flips to synthetic-led, which weakens its `split` verdict.** This needs a ruling
before the other 189.

## The other corrections, brand by brand

- **Arc'teryx 155 majority-synthetic, not 157** — and the difference *is* the rev2 rule. 157 is what the old
  rule gives (synthetic *class* above 50%). Two toques are 48% wool / 47% polyester / 4% nylon / 1% elastane:
  the class sums to 52%, but the largest single fibre is wool. Everything else reproduced exactly.
- **Southern Tide majority-synthetic is 191 (42%), not 109.** Hand-checked across a 12-style spread; polos run
  13 natural to 47 synthetic. The prior figure was a large undercount.
- **Mack Weldon states no composition on 1 style, not 13.** Twelve of the thirteen inject it client-side into
  an Alpine `x-html` attribute. Majority-synthetic is 76, not 70.
- **Vineyard Vines is 721 styles, not 723** (one soft-404, one duplicate listing) and 241 majority-synthetic,
  not 226. The 15-style gap is ten olefin belts plus **five `brrr° recycled polyester` tees, where the degree
  sign breaks a naive percent-fibre regex and silently drops the leading fibre** — caught by a sum-to-100 check
  that flagged rows summing to 11%, 62% and 200%.
- **Balenciaga states no composition on 0 of 338, not 1**, and its 46 majority-synthetic confirms exactly. The
  Tencel trap is real and quantified: **338 of 338 product pages mention Tencel and Ecovero, 0 of 338 have
  either in the composition.** A whole-page read scores this house 100% cellulosic.
- **Patagonia 350, not 349** — one product of catalogue churn over the week, not a parser disagreement.
- **Canada Goose is 51% synthetic, not 29%.** The old figure was 73 over a denominator that included the 96
  styles it could not read. It is the genuinely split house of the eight: 126 synthetic shells against 121
  natural jersey and knitwear.

## What the brief still needs to settle

1. **The tie-break**, above.
2. **Spandex scope.** "Styles containing any elastane" — any composition part, or the main fabric line? The
   eight are returned on **any part**, per the wording. On the main line alone: Balenciaga 11/2 instead of
   92/19, Arc'teryx 81/69, Patagonia 100/67. The gap is neck tape and trim, and it is large enough to change
   what the two counts mean.
3. **Named stretch with no percentage.** Mack Weldon has 9 styles reading "5% Stretch" with no fibre named,
   Southern Tide 10 ("Stretch", "Comfort Stretch"). They are neither `0` nor countable at a threshold. A third
   value, or a convention, is needed.
4. **Elastolefin.** Three Patagonia styles carry XLANCE at 11–18%. Excluded from both spandex counts here;
   including it gives 168/118.
5. **Rev2's own Columns section still lists the old thirteen columns** — no `cellulosic_pct`,
   `spandex_high_styles`, `locale_dedup` or `status` — and the ranges say `[1, 9999]` where `schema.json` says
   `[1, 99999]`. The template and schema are right; the prose is stale.
6. **A style is still not one rung deep enough.** Canada Goose issues separate style codes for logo-disc
   finishes: **63 of its 247 are finish variants, collapsing to 159 distinct numeric stems** (48/52 and spandex
   7/5 on that basis). Mack Weldon's four collections partition cleanly but do not exhaust the range — ten more
   live styles sit outside them, so the true union is 242, not 232. Vineyard Vines' `/product/mens-*` path rule
   sweeps in **52 boys' styles**; men's-only is 669 styles, 65% natural / 35% synthetic, spandex 190 / 159.

## On the robots ruling, and what it reopens

The protocol now rules disallowed paths in bounds. Two consequences:

- **Balenciaga did not need it.** Its `robots.txt` disallows both `/on/demandware.store/*` and `*cgid=*`, so the
  grid endpoint the pilot used was doubly off-limits — but an allowed channel (the category page's own "load
  more", 26 clicks) reproduces 338 tiles, 338 unique product ids and the storefront's own "338 Products"
  exactly. The row does not rest on the ruling either way.
- **Stone Island reopens.** Its composition sits behind a dialog wired to the disallowed controller; that was
  the reason it was returned held and permanently unreachable. **Under the 13 Sep ruling it is reachable**, and
  the withdrawn 637-record census can be reinstated with the path recorded as provenance. That is a decision
  for the merge, not for me, but it should not sit held on a reason that no longer applies.

## Two operational things

- **mackweldon.com's `robots.txt` carries text addressed to AI agents**, urging the reader to install a
  shopping skill so it can transact. It was treated as data and ignored. That is the second brand file in this
  project doing it (walesbonner.com was the first) — a brand's own config files are now an instruction surface.
- **Timings against the rev2 box:** six of the eight came in under it. Balenciaga took ~70 minutes against 45,
  almost all of it re-deriving an allowed census channel and working around a browser extension that fails
  after the first call per tab. Canada Goose's WAF returns 429 above ~8 concurrent XHR and took ~15 minutes to
  lift. A 45-minute box is right for a well-behaved non-Shopify house and short for a luxury one.

## What I did not do

The remaining 189 rows are `NC`. Nothing was scored, `menswear_spectrum.html` was not touched, nothing was
rebuilt, and no working files are attached. Given the tie-break and spandex-scope questions above, running the
other 189 now would bake two unruled conventions into 189 rows — I would rather have the rulings first.
