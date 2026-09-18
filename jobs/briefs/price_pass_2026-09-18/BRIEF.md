# price_pass_2026-09-18 — Price pass — the unread garments, and site-search URLs

**Rev 3, 18 September, after the pilot.** Rev 2 lost its Definitions and Failure classes to a bad
edit on my side — the thread noticed and worked to rev 1 plus stated assumptions, which was right.
Both sections are back below, with the thread's staple rules adopted and the pilot's rulings added.
The pilot's seven USD rows are merged; Auralee is held (see currency).

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

## Definitions

- **Sweater** — the crewneck pullover is the staple. Low: the cheapest full-price own-label crewneck.
  High: the most expensive main-line crewneck in an elevated fibre. Not a sweatshirt.
- **Outerwear** — find the cheapest jacket style the brand also sells in an elevated material (suede,
  shearling, cashmere). Low: that style in its entry fabric. High: its most expensive elevated
  version. Blazers, sport coats and shirt-jackets are tailoring or shirts, not outerwear.
- **Shoes** — the own-label loafer is the staple, low to high. Own-label means the brand's name is on
  the shoe and it is not a named third party's (Alden for J.Crew, Dr. Martens for Margaret Howell
  are excluded, whatever the vendor field says). Who owns the factory is irrelevant.
- **Dress shirt** — a woven, collared, button-front shirt. Where a brand has only a casual button-down,
  return it, low = high if it is one style, and say so.
- **Where the staple pair does not exist** (Barbour has no loafer; Margaret Howell's outerwear has no
  entry/elevated pair), return the plain low–high of the category's regular range and write `range`
  at the start of `note`. A range is acceptable; a hold is not needed.
- **Where the entry version is already the premium fibre** (Cucinelli, Loro Piana, The Elder Statesman,
  Kiton, Fedeli), high is the dearest regular crewneck; a judgement between close candidates is fine
  when the product is named in `note`.
- **Full price only.** Sale, outlet and markdown prices are not prices. Use the regular (compare-at)
  price where a product is currently marked down.
- **Whole dollars.** Round half-up; put the exact figure in `note`.

## Tokens

- `NC` — nobody looked. `SKIP` — not this brand's cell, already held. Never fill a `SKIP`.
- `not_a_staple` — the slots the brand does not sell, `;`-joined; **`-` when it sells every slot**.
- A garment the brand does not sell: **`NONE` in both its price cells** (the merge writes a verified
  absence, distinct from not assessed).
- `store_used` — a URL only. Anything else goes in `note`.

## Store and currency

- Use the domain in `worklist.csv`. Prefer that store's US storefront where one exists; otherwise
  read the listed store in its own currency and do not convert.
- **Check one displayed price against the feed before choosing `currency_basis`.** The Shopify rate
  rule (`Shopify.currency.rate` ≠ 1.0 with USD showing ⇒ shop currency) is a hint, not the test:
  Margaret Howell's rate is 1.369 and its US-market prices are fixed in dollars, and the feed agrees.
- **Prices that include duties and taxes are `USD_landed`**, not `USD` (Auralee's US-region prices).
  They are returned, and the merge holds them: a landed price is not a US list price.
- Shared domains (ralphlauren.com): filter by label. The Brand facet leaks other items into counts;
  the per-label category pages (`brands-polo-ralph-lauren-men-outerwear-cg`) are clean.
- **Search URL test:** the URL must return results for a garment word the brand itself uses — `jeans`
  or, where the brand says so, `denim`. Say which word passed in `note`.

## Failure classes for this job

- **A locator or a category page shows the nearest N, not all of them**, and "Show more" may not
  load the tail (Barbour: 36 of 38). Read the count the page states; record a shortfall.
- **The vendor field lies.** Stocked footwear appears under the brand's own vendor string at
  Arpenteur, evan kinori, Malbon, Saint James, Ring Jacket and Margaret Howell.
- **Markdowns wear the full-price field.** Check a second product; take the compare-at price.
- **Two number formats on one site.** Cucinelli prints `$ 1.650,00` on knitwear and `$1,200.00` on
  shoes; a naive parse reads the first as $1.65. Sum-check against the displayed figure.
- **A search URL that returns a 200 and no results is a failure**, not a link.
- **A round feed total is suspicious.** Todd Snyder's `/products.json` returned exactly 3,200.

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
