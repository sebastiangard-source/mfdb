# Handoff: final own-door location data — all brand-owned stores

**From** Location Thread IV · **2026-09-23** · **Files** `own_doors_final_2026-09-23.csv` (3,005 rows, 129 brands) ·
`own_doors_zero_line_2026-09-23.csv` (17 brands with a positive zero or an SG drop)

## What the file is

One row per brand-owned door in the US, `format = own-door` throughout (outlets, concessions, shop-in-shops,
parent-store departments, closed and non-retail rows are **excluded** — they live in the per-brand
classified files). `status` is `open` (2,998), `coming soon` (4), `temporary` (2), `seasonal` (1).

It is a union of two sources, and the `source_file` column says which:

| Source | Rows | Brands | Quality |
|---|---|---|---|
| This thread's classified captures (Sept 4–6) | 880 | 32 | **brand-stated format**, addresses verified against store pages, decisions applied |
| `locations_2026-08-29.csv` master, `status = open` | 2,125 | 97 | **pre-recapture** — the typing the audit found inflated; not yet reclassified |

Where a brand was recaptured, its master rows are gone (671 dropped) and the capture rows stand. Where it
was not, the master's `open` rows are carried as they were, with `format_basis` saying so; its `unresolved`
rows (283) are excluded, since the audit showed those are mostly outlets.

## The 32 recaptured brands (authoritative)

A Bathing Ape · Banana Republic · Barbour · Billy Reid · Boggi Milano · Bonobos · Brooks Brothers · Brunello
Cucinelli · Burberry · Canada Goose · Canali · Celine · Charles Tyrwhitt · Dolce&Gabbana · Drake's · Eton ·
Etro · Golden Goose · Indochino · Kith · Lacoste · Madhappy · Purple Brand · Ralph Lauren (incl. Polo, with
`banner_stated`) · RRL (Double RL standalone) · Redvanly · Saint Laurent · Tecovas · Ted Baker (0) ·
Theory · Todd Snyder · Vineyard Vines · Zegna.

All SG decisions of Sept 6 are applied: Ralph Lauren brand key, Central Valley 8018 as outlet, Brooks Brothers
Assembly Row/Dolphin/Freeport/Junction Commons/Manchester Square as Factory and Destiny USA as full-price,
Canada Goose Troy 2801 and Bellevue 111, Zegna Bloomington MN, Charles Tyrwhitt Belmont as boutique.

## The 97 carried brands (provisional)

Everything else is the 29 August master unchanged — including four brands the prior thread captured (Alo,
J.Crew, Dior, BOSS) whose capture files never reached this thread and so appear here at their master rows.
The largest carried blocks, and therefore the ones most exposed to the outlet-inflation pattern:
Lululemon 379, J.McLaughlin 164, Vuori 110, Faherty 91, Gucci 73, Carhartt 68, Marine Layer 57,
TravisMathew 57, State & Liberty 45, Buck Mason 42. Each needs the same recapture before its count is trusted. The
`format_basis` column carries `master store_type=… (pre-recapture)` on every one of these rows so the two
grades never mix silently.

## Zero-door line

Seventeen brands with no US own door, each with a positive record (`own_doors_zero_line_2026-09-23.csv`):
Palm Angels, Baracuta, Criquet, Paul & Shark, Zilli, Brax, Easy Mondays, J.Lindeberg, Les Deux, Samsøe
Samsøe, Rakho, Wythe, Ted Baker, RLX, Purple Label (standalone), and Club Monaco / Scotch & Soda as SG drops.
These are not absent from the dataset; they are present at zero, and the availability layer must say so
rather than showing a blank.

## Regional roll-up

NE+NY own-doors 572; Massachusetts 131. Boston roll-call for the recaptured brands is in
`HANDOFF_location_thread_IV_2026-09-06.md`.

## What is not in this file, by design

- Outlets (32 brands' worth), concessions, shop-in-shops, parent-store departments (RRL/Purple Label/RLX
  inside Ralph Lauren) — in the classified files and `rl_lines_departments_2026-09-05.csv`.
- Stockists — `stockist_brands_2026-09-12.xlsx` (NE+NY register, with Assembly His and kloTH) and the
  Mid-Atlantic Phase 1–2 workbooks.
- Department store chain lists — `dept_store_brands.csv`.

## Merge order

1. Re-key the master's Polo Ralph Lauren block to Ralph Lauren (corrections note, item 3).
2. Replace the master wholesale with this file, keeping `source_file` and `format_basis` as columns.
3. Rebuild `locations_unified` on the Spectrum keys; the brand-store channel then carries the corrected
   counts for the 31 and the provisional ones for the 97, labelled.
4. Queue the ten largest carried brands for recapture on the seven-recapture template.

## Two repairs made while assembling this file

- `canada_goose_classified_2026-09-05.csv` had been truncated to zero bytes by an edit on Sept 6; rebuilt
  from the source workbook with the Troy and Bellevue decisions applied (18 rows).
- Golden Goose's two duplicate listings (Rodeo Drive, South Coast Plaza) are excluded here on the worker's
  flags; the classified file keeps them, flagged. Tecovas reads 65 open own-doors in its file (the Sept 5
  note said 64); the file is authoritative.
