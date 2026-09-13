# NOTE — fibre_pass_2026-09-14, pilot return

**Returned:** `return.csv` (197 rows, the template's keys, 8 filled, 189 `NC`) and this note. Nothing else.
`python3 reconcile.py names.txt` → **197 in, 197 exact, 0 to rewrite, 0 unmatched.** No cell is blank.

---

## First: I am probably not the thread you are looking for

The brief says a thread holds **spandex counts for up to 163 brands**. **That is not this thread. I hold no
spandex count for any brand, and none was ever measured here.** Every `spandex_styles` cell in this return is
`NC`, and it will stay `NC` unless the fibre pass is run properly. If the handoff points at a thread with 163
spandex counts, it is a different one and it is still worth finding.

What this thread does hold, from a technology-dial pass finished 13 September, is a **majority-fibre
measurement for 96 brands** — which is adjacent to your job but is not your job, and the difference matters:

| your column | what I hold |
|---|---|
| `styles_total` | a denominator for 96 brands — **71 style-level, 25 colourway-level with no style count** |
| `styles_with_composition` | held for most of the 96, usually as "how many state no composition" |
| `synthetic_pct` | held — share whose **main fibre is synthetic**, which is your definition |
| `natural_pct` | **never measured.** Not derivable: my rule counts rayon/viscose/modal/lyocell as neither, so natural and synthetic do not sum to 100 |
| `spandex_styles` | **never measured, any brand** |
| `shape`, `synthetic_categories`, `natural_categories` | never measured. I have category breakdowns, but not which categories synthetic *leads* |
| `style_method`, `colourway_ratio` | held for most of the 96 |
| `feed_currency_rate` | never captured |

So the honest maximum from prior work is **roughly half your schema for 96 of 197 brands**, not a completed
pass. The eight rows here are the ones where my denominator is genuinely styles, the numerator was counted at
style level, and composition coverage is known — the only rows that can be re-rendered into your schema without
a lie in them.

## What the eight say

Arc'teryx 77% · Patagonia 67% · Vineyard Vines 31% · Canada Goose 29% · Mack Weldon 30% · Southern Tide 24% ·
Balenciaga 14% · Bonobos 9%. Every one is `PRIOR PASS` in its note, with the read date and the channel.

## What this brief got wrong, or left me unable to follow

**1. There is no `status` column.** The composition-coverage rule says "return the numbers, mark `status`
partial, and say so in the note" — but `schema.json` and `return_template.csv` have thirteen columns and none of
them is `status`. **Bonobos is the case: 1,512 of 2,821, 53.6%, below your floor.** I put the word PARTIAL at
the front of its `note` because there was nowhere else to put it. Add the column, or say that a note prefix is
the convention.

**2. `natural_pct` and `synthetic_pct` cannot both be measured against the natural list as written.** Your
natural list is cotton, wool, linen, silk, cashmere. Rayon, viscose, modal, lyocell, acetate and cupro are on
neither list, so the two percentages do not sum to 100 and a validator that assumes they do will reject good
rows. It matters more than it sounds: **PAIGE's flagship performance denim is 54% rayon** — majority-synthetic
reads 1% or 45% for that brand depending purely on this ruling.

**3. The seated seven use a different vocabulary for "not measured".** `examples_seven_seated.json` gives
`"x": null` for Merz b. Schwanen, Comme des Garçons and Loro Piana, where your schema says `NC`. If null means
*nobody looked*, three of your seven template rows are carrying an unmarked hole; if it means *zero*, then Loro
Piana has no spandex anywhere and should say 0. Worth settling before those seven anchor the scale.

**4. "Styles, not colourways" needs one more rung.** Several houses in this universe put **one product per
colourway AND one line per size-run or market**, so a de-duplicated style count still over-counts: Baracuta's
992 sitemap entries were 283 handles × 4 locales; Les Deux's 606 records are 321 styles; Kith's feed hard-caps
at 25,000 records and its men's collection alone exceeds 10,000. `colourway_ratio` catches the first, not the
second. I would add *locale duplication* to your failure list.

**5. The 25-minute stop is too short for this job on a non-Shopify house.** On Shopify a census is minutes.
Off it, establishing the denominator alone ran 20 minutes on one house and the whole brand 40; Carhartt and
Hermès each blew past an hour. If 25 minutes stands, most of the Italian and luxury half of the list will come
back `NC`, which is honest but empty.

## Brands where this pass will not produce a finding, and why — before you spend the time

Composition is structurally absent or unreachable on these, all verified this week:

- **Stone Island** — composition is not in the rendered DOM at all. It sits behind a dialog wired to
  `/on/demandware.store/`, which that site's **robots.txt disallows**. Permanently unreachable by an allowed
  path. Return it `NC`.
- **Rodd & Gunn — 93.8% of the catalogue states no composition.** The PDP has no fabric panel.
- **Everlane 49.6%**, **Bonobos 46.4%**, **Canada Goose 38.7%**, **Alex Crane 43.6%**, **TravisMathew 28.2%**,
  **J.Crew 24.2%** state none. J.Crew is one of your seated seven.
- **A Bathing Ape (US)** — no description and no composition anywhere on the site; the JS endpoint returns the
  title as the description.
- **Hackett** — there is no US storefront; the US-facing locale is ROW, and its pages are client-rendered.
- **Charvet, Comme des Garçons, Junya Watanabe, Cesare Attolini** — no first-party store to census. Comme des
  Garçons is one of your seated seven; its row came from somewhere other than a first-party catalogue.

## Two things you already have that this pass needs

Both were built here this week and are attached to the previous return rather than re-derived:

- **A verified domain and channel register for all 204 keys** — the brand's own live store, the platform, and
  **the cheapest census channel that actually returned products, with the count it returned**. 105 Shopify, 45
  Salesforce Commerce, 49 custom, 1 Magento; 93 have a working `products.json`, 91 a usable product sitemap, 9
  need a category crawl, 7 have nothing. **Fifteen domains in circulation are wrong, dead or moved** (sease.com
  is a private individual's homepage, rhude.com a photographer, purplebrand.com a marketing agency,
  paulshark.com dead against a live paulandshark.com), and counterfeit "official stores" outrank the real store
  for at least five brands. A fibre pass pointed at those domains returns confident zeros.
- **Feed traps, per brand**: Ted Baker's root `products.json` answers 200 with 38 products against a real 1,302;
  Paul Smith's US sitemap is a well-formed empty urlset while the real 3,635 sit in `base.xml`; Rhone has no
  product sitemap and no feed at all; J.Lindeberg's feed looks complete at exactly 7,500 of 7,755.

## What I did not do

No new measurement. No scoring. I did not touch `menswear_spectrum.html`, rebuild anything, or send working
files. The remaining 189 rows are `NC` and stay that way until you say whether the eight are the right shape —
and whether, given the answer at the top of this note, you still want this thread to run the pass at all.
