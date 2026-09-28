# resale_links_2026-09-28 — Grailed, Depop and Poshmark, one men\u2019s link per brand each

**Issued** 28 September 2026 · **Kind** links · **First eight rows returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first.

## The job

Each brand page carries a Secondhand line. It holds a Vinted pill today (`vinted_on_file.csv` shows how
that was done). Add **Grailed, Depop and Poshmark**: for each brand, the URL that opens that marketplace\u2019s
**men\u2019s listings for the brand and nothing else**, using the marketplace\u2019s own brand entity where it
has one, and a text search only where it does not.

## What a correct link is

- **The brand\u2019s own entity first.** Grailed has designer pages (`grailed.com/designers/<slug>`), Depop
  has brand pages and filters, Poshmark has brand pages (`poshmark.com/brand/<Brand>`) with a Men
  department. Use these. A text search is the fallback and is marked as such.
- **Men\u2019s only.** Where the marketplace has a department or category filter for men, it is on. Read the
  first two rows of listings: no women\u2019s or kids\u2019 product. Where a brand entity cannot be narrowed to
  men (some Depop brand pages), say so in `note` and return the narrowest link that exists.
- **Sub-lines and look-alikes**, on the same rulings as the Vinted pass: a sub-line sold under the brand\u2019s
  name is folded in where the marketplace lets you (Levi\u2019s Vintage Clothing under Levi\u2019s); a separate
  company is kept out (Carhartt WIP is not Carhartt; Polo Ralph Lauren is not Ralph Lauren Purple Label);
  a marketplace that merges them is noted. The `_note` column says what each link includes and excludes.
- **Stable.** The entity URL or a canonical search URL, no session, sort or tracking parameters. Confirm it
  holds on a fresh load without login.
- **NONE** where a marketplace has no entity and a text search returns mostly other brands (short names
  like Purple, Frame, Rails, Rowan, Bode are the risk). Say what the search returned.

## Rules

- `NC` nobody looked; an empty cell is an error.
- One URL per marketplace per brand. Absolute, https.
- Names must match `canonical_keys.txt`; run `reconcile.py` before returning.
- Do not touch the map. Return `return.csv` and `NOTE.md` (rulings you had to make, marketplaces\u2019 quirks,
  brands where the entity is missing or merged), nothing else.

Return these eight rows first, without stopping: **Levi\u2019s, Carhartt, Polo Ralph Lauren, Stone Island,
Purple, Frame, Rick Owens, Stefan Brandt** \u2014 a sub-line case, a separate-company case, a family of lines,
a badge brand with a big resale market, two short names that break text search, a designer with a
Grailed-native audience, and a brand small enough to be absent everywhere.

## Time box

Six minutes a brand across the three. Past that, `NONE` with a note.
