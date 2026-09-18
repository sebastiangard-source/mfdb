# price_pass_2026-09-18 — Price pass — the three unread garments, and site-search URLs

**Issued** not yet · **Kind** price · **Pilot** 8 rows first · **Returns to** the Spectrum thread

Read `audit_protocol.md` before starting. This brief carries everything it requires.
If any instruction below would make you produce a confident wrong answer, stop and say so
before doing it. Returns that say *the brief got this wrong* have been worth more than
the ones that said *done*.

## The job

Read the three garments the earlier price pass never reached — **Sweater, Outerwear, Shoes** — for
every brand in `worklist.csv`, from the brand's own US store at full price, and return the low and
high of each as `[entry version, elevated-fabric version of the same staple]`. `worklist.csv` says
which slots are open per brand (a few brands are missing an earlier slot too — read those as well),
the brand's store domain and platform from the `site` record, and whether a site-search URL is on
file. **For the 37 brands with no search URL, find one**: the URL of the brand's own search page
with the query left empty, e.g. `https://www.toddsnyder.com/search?q=`, so a garment word can be
appended. Test that it returns results.

A slot the brand does not sell is `NONE` in `not_a_staple` (list the slots) — a verified absence,
different from `NC`. Where the store prices in a currency other than USD, return the figures and set
`currency_basis`; do not convert. The Shopify rate rule from the fibre pass settles the basis:
`Shopify.currency.rate` ≠ 1.0 with USD showing means the feed is in the shop currency.

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

## Definitions

- **Sweater** — a knitted pullover or cardigan for men. Not a sweatshirt.
- **Outerwear** — a jacket or coat, excluding blazers and sport coats (tailoring) and shirt-jackets.
- **Shoes** — footwear the brand makes itself. Shoes it stocks from other makers are not its shoes;
  judge by product code and what the brand says it makes, never by the vendor field.
- **Low** is the entry version of the staple in the current main range; **high** is the elevated-
  fabric version of the same staple (cashmere over merino, shearling over wool). Not the single
  most expensive item in the category, and never a collaboration or a runway piece.
- **Full price only.** Sale and outlet prices are not prices.

## Failure classes for this job

- **A locator or a category page shows the nearest N, not all of them.** Read the count the page
  states before believing a list.
- **The vendor field lies.** Stocked footwear appears under the brand's own vendor string at
  Arpenteur, evan kinori, Malbon, Saint James and Ring Jacket.
- **Markdowns wear the full-price field.** Check a second product before taking a figure.
- **A search URL that returns a 200 and no results is a failure**, not a link. Test with `jeans`.

## Columns

- `brand` — key
- `sweater_low` — int [1, 99999]
- `sweater_high` — int [1, 99999]
- `outerwear_low` — int [1, 99999]
- `outerwear_high` — int [1, 99999]
- `shoes_low` — int [1, 99999]
- `shoes_high` — int [1, 99999]
- `not_a_staple` — str
- `search_url` — url
- `currency_basis` — enum one of ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'other']
- `status` — enum one of ['complete', 'partial']
- `source` — provenance
- `note` — str
