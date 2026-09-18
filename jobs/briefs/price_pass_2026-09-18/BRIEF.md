# price_pass_2026-09-18 — Price pass — the unread garments, and site-search URLs

**Rev 2, 18 September, after the thread's pre-pilot review.** Five rulings and four corrections below,
in reply to the points raised. The protocol's second item 3 was mine — Sebastian's ruling of 13
September on robots.txt, spliced in badly. It is real, and it is now written into item 3 properly.

**Issued** 2026-09-18 · **Kind** price · **Pilot** 8 rows first · **Returns to** the Spectrum thread

Read `audit_protocol.md` before starting. This brief carries everything it requires.
If any instruction below would make you produce a confident wrong answer, stop and say so
before doing it. Returns that say *the brief got this wrong* have been worth more than
the ones that said *done*.

## The job

Read every garment slot that is still unread for each brand in `worklist.csv` — usually **Sweater,
Outerwear and Shoes**, sometimes an earlier garment too, and for six brands all eight — from the
brand's own store at full price, and return the low and high of each. The template says exactly what
each row wants: **`NC` marks a cell to read; `SKIP` marks a cell that is not in scope for this brand
because an earlier pass already holds it — leave `SKIP` as it is, never fill it.** The merge writes
nothing for either token, so a `SKIP` can never overwrite a held record. **For the 37 brands with no
search URL, find one**: the brand's own search page with the query left empty
(`https://www.toddsnyder.com/search?q=`), tested to return results for `jeans`. Sixteen brands are
on the worklist for the URL alone; their garment cells are all `SKIP`.

A slot the brand does not sell is `NONE` in `not_a_staple` (list the slots) — a verified absence.

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
- Any single brand takes more than 25 minutes: mark it `NC` with a note and move on.
- A source that cannot be resolved (page 404s, locator caps at N): record what the widget
  itself says and do not fill from memory.

## Columns

- `brand` — key
- `tee_low` — int [1, 99999]
- `tee_high` — int [1, 99999]
- `polo_low` — int [1, 99999]
- `polo_high` — int [1, 99999]
- `dress_shirt_low` — int [1, 99999]
- `dress_shirt_high` — int [1, 99999]
- `jeans_low` — int [1, 99999]
- `jeans_high` — int [1, 99999]
- `dress_pants_low` — int [1, 99999]
- `dress_pants_high` — int [1, 99999]
- `sweater_low` — int [1, 99999]
- `sweater_high` — int [1, 99999]
- `outerwear_low` — int [1, 99999]
- `outerwear_high` — int [1, 99999]
- `shoes_low` — int [1, 99999]
- `shoes_high` — int [1, 99999]
- `not_a_staple` — str
- `search_url` — url
- `store_used` — url
- `currency_basis` — enum one of ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'other']
- `status` — enum one of ['complete', 'partial']
- `source` — provenance
- `note` — str
