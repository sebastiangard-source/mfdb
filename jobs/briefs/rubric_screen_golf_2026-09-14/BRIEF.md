# rubric_screen_golf_2026-09-14 — Golf dial screen — the top ten

**Issued** not yet · **Kind** rubric_screen · **Pilot** 4 rows first · **Returns to** the Spectrum thread

Read `audit_protocol.md` before starting. This brief carries everything it requires.
If any instruction below would make you produce a confident wrong answer, stop and say so
before doing it. Returns that say *the brief got this wrong* have been worth more than
the ones that said *done*.

## The job

_One paragraph. What is being checked, for which brands, and what a finding looks like._

## What to return

Two files, nothing else:

1. `return.csv` in exactly the schema in `schema.json` (a template with the brand keys
   prefilled is in `return_template.csv`). One row per brand. Never prose.
2. `NOTE.md`: what was checked, what was not reached, what contradicted the existing
   record, and what this brief got wrong.

Send the first 4 rows before doing the rest. Format errors caught at 4 rows cost
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
- Any single brand takes more than 25 minutes: mark it `NC` with a note and move on.
- A source that cannot be resolved (page 404s, locator caps at N): record what the widget
  itself says and do not fill from memory.

## Columns

- `brand` — key
- `golf_products` — int [0, 9999]
- `total_products` — int [0, 99999]
- `golf_pct` — int [0, 100]
- `house_tech` — enum one of ['owned', 'licensed', 'none', 'unclear']
- `source` — provenance
- `note` — str
