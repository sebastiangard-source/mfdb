# The six items — status

**13 September 2026.** Nothing new beyond these six. Nothing is scored. No depth measurement was extended
beyond the 96 brands already in the table, and no other dial was opened.

---

## 1. The seven row-level files — SENT

`rubric_tech_universe_2026-09-12.csv` (verdict table) · `rubric_screen_tech_origin_2026-09-11.csv` (67 rows) ·
`rubric_screen_tech_worklist_2026-09-11.csv` (36 rows) · `rubric_screen_tech_flag_validation_2026-09-12.csv`
(38) · `rubric_screen_tech_false_negative_sweep_2026-09-12.csv` (31) · `rubric_tech_census_2026-09-12.csv` ·
`rubric_screen_tech_origin_screenbrands_2026-09-12.csv` (23).

The verdict table and the census are re-sent below with the four new brands folded in (item 3).

## 2. Depth table normalised to styles — DONE, 71 of 96 carry one

Five new columns: `styles_denominator`, `styles_basis`, `pct_basis`, `partial`, `partial_reason`.

- **23 rows are already style-level** — colourways were not separate records on those sites, so the share as
  measured is a style share. `styles_basis = equals_records`.
- **39 rows carry a style denominator the pass reported** (e.g. Redvanly 1,027 records → 244 styles).
- **9 rows carry a derived denominator** from a reported records-per-style ratio (Ted Baker 1.55, BOSS 2.03,
  Wythe 2.8...). Marked derived, and marked partial.
- **25 rows have no style denominator at all** and say so in `partial_reason` — Cuts, Charles Tyrwhitt, Zegna,
  Sunspel, Filson, Prada, Sease, Eton, Lacoste, Canali, Aspesi, Moncler, Visvim and the rest. Colourways are
  separate records there and no style count was taken.
- **73 rows are marked partial.** The reason is the same in most cases and is worth stating plainly: **a style
  denominator does not make the share style-level.** Where the numerator was counted on colourway records, the
  percentage stays a record share until someone re-counts the numerator per style. `pct_basis` says which each
  row is. I did not re-read any site to produce this, as instructed.

Three units are not styles at all and cannot be converted: **Proper Cloth** (made-to-measure fabrics),
**Indochino** (fabric × garment), **Son of a Tailor** (configured products). Each says so.

## 3. The four new brands — ADDED to both files, against the 204-key list

`canonical_keys_204.txt` is the 200 plus Borgo28, Duck Head, Merz b. Schwanen, Saint James. The domains file is
**204 rows**; the verdict table is **204 rows** (152 yes · 48 no · 4 unclear).

| brand | store | verdict |
|---|---|---|
| Borgo28 | borgo28.com (Shopify, 315) | names a technology — **licensed only, all composition-line** (Tencel, Modal, Supima, Lycra). A clean `none` if fibre brands in a composition line don't count. |
| Duck Head | duckhead.com (Shopify, 772) | names a technology — licensed: PrimaLoft Black on 17, Drirelease on 7 |
| Merz b. Schwanen | merzbschwanen.com (Shopify, 657) | names a technology — **house**: a full fabric system on its own fabrics page, loopwheeled on 141 |
| Saint James | **us.saint-james.com** (Shopify, 465) | names a technology — **house**: UVYL / U.V. Skin-Protection microfiber on 26 |

Two things from that pass you should know. **Saint James's apex redirects to the French store** — censusing
`saint-james.com` counts the French catalogue. And **Merz b. Schwanen appears nowhere in this thread's earlier
artefacts**, despite the 11 Sep seating note, so this is a first pass on it rather than a re-check.

**A harvester bug worth propagating:** an `&reg` decoder that did not require the semicolon read the Shopify
market querystring `?locale=en&region=US` as a trademark symbol and scored a phantom mark on every page of
every Shopify store. It was caught and fixed in this pass. Any earlier row in this lineage that leaned on a
trademark-symbol harvest over a Shopify store should be re-checked against that.

## 4. Patagonia — FINISHED, 518 of 518, and the three denominators resolved

It is not partial. The site gives three answers and they reconcile:

- **518** — the grid paged to exhaustion. Every one has a numeric product id.
- **562** — the storefront counter. **562 = 518 + 25 + 18 + 1**: 25 colourway-level tiles for seven Nano-Air
  styles that are already in the 518, 18 third-party goods (Hestra gloves, Farm to Feet socks) and one book.
- **702** — the sitemap's `mens-` URLs. Roughly 27% larger than anything the men's storefront shows. Unusable.

**518 is the denominator used**, on the multi-brand-separation rule. Full-catalogue result: names a technology
**308 — 59.5%**, claim naming nothing 26.4%, majority synthetic 67.4%, three products state no composition.
**31 families, not the sample's 20** — GORE-TEX 12 (matching its own facet exactly), Polartec 15, PrimaLoft 7
were all sample zeros and are real. The block that stopped the earlier run was never a rate limit: it is scoped
to the page session and a top-level navigation clears it.

## 5. The 451 unclassified marks — CLASSIFIED

`rubric_tech_marks_index_2026-09-13.csv` now carries `kind`, `owner` and `basis` on every row:

| | marks |
|---|---|
| mill or fibre supplier (incl. certifications, flagged in `basis`) | 207 |
| house-named fabric | 192 |
| noise | 178 |
| unclear | 11 |

**Two ownership corrections that matter to the top step:**

- **TurboDry is not Mizzen+Main's** — it is registered to NexTex Innovations (US reg. 6181671), a third-party
  fabric supplier. It was carried as a house mark.
- **PUREPRESS is not Ralph Lauren's** — it is Cotton Incorporated's durable-press finish, licensed out. Polo
  carries it.

Also reclassified away from the house bucket: **Ecodown** is Thermore's, **DriTan** is ECCO's, **Alsavel** is
Loro Piana's, **AuraLite** reaches Our Legacy only through a Satisfy collaboration, and Zegna's **MegaGrip** and
**LiteBase** are Vibram's. In the other direction, **NovaPoly is genuinely BOSS's own**, and Zegna's **High
Performance** is a real cloth name despite reading like a descriptor.

Three structural findings in the noise bucket, because they affect how the index should be read:

- **~50 rows are harvester exhaust** — analyst annotations and page furniture glued onto marks
  (`composition_only)`, `dream[house]`, `venezia calf leather (house`, `5 of 120 pdps`). They were classified on
  the underlying mark where one was buried inside; the extraction step needs a cleanup pass before the index is
  used for anything but triage.
- **Fit and garment names are indistinguishable from fabric names to a scraper** — Mott & Bow's street names,
  Vineyard Vines' Shep Shirt, TravisMathew's Heater Series, Peter Millar's Crown Sport/Crafted/Comfort. Those
  went to noise with the reason stated; if you want a fourth "house sub-line" bucket, those plus Rhone's
  Commuter and Citizens' Archive Denim are the population.
- **Collaboration bleed-through is a different animal from supply**: Kith's Yeti, Tumi and Salomon marks,
  Malbon's adidas ULTIMATE365. They sit in the supplier bucket for now and are flagged in `basis`.

Counts are still floors — the source field was truncated at 300 characters per brand at harvest.

## 6. Stone Island — REPRODUCED for the naming half, HELD for the rest

Its `robots.txt` disallows `*/on/demandware.store/*`, which is where the earlier 637-record census came from.
**That census is withdrawn.** What an allowed path (the product sitemap, plus ordinary PDPs) reproduces:

- **The denominator, to 98.3%** — 618 records / 292 styles against the withdrawn 637 / 298. The deltas are
  sitemap staleness and catalogue drift.
- **(a) names a technology: 174 of 618 = 28.2%**, a census from the sitemap alone, because the slugs carry the
  fabric name. Against the withdrawn 29.4%, with **12 of 13 families within one record** and five exact.
  **PrimaLoft is the exception and is held** — it is named only in descriptions, never in a product name.
- **(b) is held.** 0 of 74 rendered PDPs made a bare performance claim, but the site throttles rendering to
  about two products a minute, so that is an indication, not a census.
- **(c) is held permanently.** Composition is not in the rendered DOM at all — it sits behind a dialog wired to
  the disallowed controller. This is also why the earlier pass reported a suspiciously low synthetic share.

The depth row is restated on the allowed path and marked partial with all of that in `partial_reason`.

**One cross-brand flag:** `Disallow: */on/demandware.store/*` is near-boilerplate on Salesforce Commerce Cloud.
Forty-five brands in the domain register run on that platform, so anything in this project that reached
composition through that endpoint deserves the same audit.
