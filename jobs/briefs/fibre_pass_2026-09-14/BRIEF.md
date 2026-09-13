# fibre_pass_2026-09-14 — Fibre pass — the range, measured for 197 brands

**Revised 13 September after the pilot return.** Changes: a `status` column; `cellulosic_pct` and
`locale_dedup` columns; the time box; the null-vs-NC note on the seated seven; a rayon ruling pending.
The pilot's eight rows are held, not rejected — they are half a record each, and `fibre` lands whole
or not at all. Fill the other half from what you already hold where you can.

**Issued** 2026-09-13 · **Kind** fibre · **Pilot** 8 rows first · **Returns to** the Spectrum thread

Read `audit_protocol.md` before starting. This brief carries everything it requires.
If any instruction below would make you produce a confident wrong answer, stop and say so
before doing it. Returns that say *the brief got this wrong* have been worth more than
the ones that said *done*.

## The job

Measure, for each brand, how its current men's clothing range divides by main fibre, from the brand's
own product pages — never from a stockist, never from a category name, never from memory. Seven houses
are on the map already (J.Crew, Faherty, Peter Millar, Merz b. Schwanen, Todd Snyder, Comme des
Garçons, Loro Piana) and their rows are the template: `examples_seven_seated.json` in this folder holds all seven. A finding is a count of **styles** (not colourways, not listings), the share whose main
fibre is natural (cotton, wool, linen, silk, cashmere) and synthetic, the number of styles containing
any spandex/elastane, and a verdict on whether the house is one cloth story or two. Swim and underwear
are excluded from the split verdict. Main fibre means the fibre with the highest share in the first
composition listed.

**Before doing any new work: if you already hold fibre or spandex counts for brands from an earlier
pass, return those first, in this schema, as the pilot.** The handoff records a thread holding spandex
counts for up to 163 brands that never reached the build. If that is you, that return alone is the job.

## What to return

Two files, nothing else:

1. `return.csv` in exactly the schema in `schema.json` (a template with the brand keys
   prefilled is in `return_template.csv`). One row per brand. Never prose.
2. `NOTE.md`: what was checked, what was not reached, what contradicted the existing
   record, and what this brief got wrong.

Send the first 8 rows before doing the rest. Format errors caught at 8 rows cost
minutes; caught at the end they cost the pass.

## Rules

- Brand names must match `canonical_keys.txt` exactly. Run `python3 reconcile.py names.txt`
  before returning. Zero rewrites, zero unmatched.
- `NC` in a cell means *nobody looked*. An empty cell is an error. Never leave a cell blank.
- `source` is required on every row that carries a finding. A URL. `N/A` is not a source
  and the row will be held.
- Do not touch `menswear_spectrum.html`. Do not rebuild the tool. Do not send working files.
- Out of scope but noticed: record it anyway in `NOTE.md` or an extra column, do not discard it.

## Stop conditions

- More than a third of the pilot returns nothing usable: stop, the brief is mis-aimed.
- A source that cannot be resolved (page 404s, locator caps at N): record what the widget
  itself says and do not fill from memory.
- **Time box: 25 minutes on a Shopify house, 45 on anything else.** Past that, `NC` with a note.
- **Where composition is structurally absent** (Stone Island behind a disallowed dialog; Rodd & Gunn
  stating none on 94%; no first-party store), return `styles_total` and `styles_with_composition`,
  the rest `NC`, `status` partial, and the reason. That is a finding.

## Known failure classes for this job — every one has fired before

- **Colourways are not styles, and it is the default.** Five of eight houses in one batch listed one
  product per colourway, in five different encodings: colour after a dash, colour in the handle, colour
  as a variant, colour as a separate product code. Velvet showed 352 against a true 241; Duck Head 196
  titles against a true 90. Report which method you used to dedupe in `style_method`, and the raw
  listing count over the style count in `colourway_ratio` (e.g. `352/241`). A ratio of 1.00 on a house
  with colour options is itself suspicious.
- **Any extractor returning the same value on 100% of rows is reading page furniture.** Robert Talbott
  showed *made in America* on 85 of 85 from a navigation link. Check the string on a page with no
  product on it before believing it.
- **The vendor field is not the boundary.** Judge by product code, product name and parallel
  collections. Arpenteur's 17 shoes are all other makers' under its own vendor string.
- **Naming regime is not substance.** John Smedley is all knitwear and scores 6 of 107 on a knit
  word-count because its products are called Lundy and Bradrick. Count from compositions, not names.
- **A paginated feed returns page one to every static fetch.** `/products.json?limit=250&page=N` until
  a page returns fewer than 250. Read the record count before capturing.
- **`Shopify.currency.rate` ≠ 1.0 with USD active means the feed is shop-currency.** Record the rate in
  `feed_currency_rate` (e.g. `1.0`, `1.183`, `not shopify`). It is not a fibre fact, but it is free
  while you are there and it settles the price basis for the price thread.
- **Locale and market duplication is a sixth encoding of the colourway problem.** Baracuta's 992
  sitemap entries were 283 handles × 4 locales; Kith's feed hard-caps at 25,000. `colourway_ratio`
  does not catch it; `locale_dedup` says what you removed (e.g. `4 locales → en-us only`, or `none`).
- **Regenerated cellulosics — rayon, viscose, modal, lyocell/TENCEL, cupro, acetate — are neither
  natural nor synthetic.** Count them in `cellulosic_pct`. `natural_pct + synthetic_pct +
  cellulosic_pct + (no composition) = 100`. Whether the map folds cellulosics into one side is a
  ruling not yet taken; keeping them separate means the answer costs nothing later. PAIGE's
  performance denim is 54% rayon — that row moves 44 points on the ruling.
- **The seated seven carry `"x": null` for three houses.** In the page that renders as "not counted",
  which is your `NC`, not zero. Treat those three as unmeasured for spandex; if you can count them
  while there, do.
- **Composition coverage decides whether the row is a finding.** `styles_with_composition` over
  `styles_total` below about 60% means the percentages rest on a minority of the range — return the
  numbers, set `status` to `partial`, and say why in the note. MAN–TLE at 54 of 131 was held for this.

## Columns

- `brand` — key
- `styles_total` — int [1, 9999]
- `styles_with_composition` — int [0, 9999]
- `natural_pct` — int [0, 100]
- `synthetic_pct` — int [0, 100]
- `spandex_styles` — int [0, 9999]
- `shape` — `one` if a single cloth story, `split` if two clear halves; enum one of ['one', 'split']
- `synthetic_categories` — json list of category names where synthetic leads, e.g. `["Polos & shirts","Shorts"]`; `[]` for a one-cloth house
- `natural_categories` — json list of the top three natural-led categories
- `style_method` — enum one of ['product_code', 'title_dedup', 'handle', 'manual']
- `colourway_ratio` — str
- `feed_currency_rate` — str
- `source` — provenance
- `note` — str
