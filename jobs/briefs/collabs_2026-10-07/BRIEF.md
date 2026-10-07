# collabs_2026-10-07 — active collaborations, brand by brand

**Issued** 7 October 2026 · **Kind** count · **First ten rows returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first.

## The job

For each of the 204 brands in `worklist.csv`, list every **active** collaboration: a co-branded product
or collection with another named brand that is on sale now, at full price, from the brand or the
partner. One row per brand-partner pair. A brand with none returns one row with `partner` = `NONE`.

A collaboration is a dated, named, linkable fact. Nothing here is a judgment. The map will use the
return three ways: a *Collaborations* line on each brand page; a network of which mapped brands work
with which; and a list of partners that are not on the map yet, which decides which brands get
seated next. The third use is why `partners.csv` matters as much as the main file.

## What counts

**Co-branded**: two named brands, both names on the product, both parties brands (clothing, footwear,
accessories, or a non-fashion brand making product with a fashion house — Todd Snyder × New Balance,
Noah × Barbour, J.Crew × Beams, Aimé Leon Dore × Porsche). This is what fills `return.csv`.

**Logged but not counted** — one row each in `excluded.csv`, with the reason, so nobody re-finds them:

- *Retailer exclusive* — a capsule made for one shop and sold only there (Mr Porter, Nordstrom, Beams
  as the retailer rather than as a brand; say which role Beams is in).
- *License* — a brand name rented to a maker (Carhartt WIP, Champion Reverse Weave Japan, most
  university and team product).
- *Celebrity or designer line* — a person's name on the product, not a brand's (Pharrell at adidas,
  a guest designer's capsule). A designer's *own brand* on the product is co-branded and counts.
- *Artist edition* and *charity capsule*.

**Active** means buyable at full price today from the brand's or the partner's own site, not from a
reseller. A collaboration that recurs (Todd Snyder × New Balance has had drops since 2016) is one row:
`first_year`, `latest_year`, `drops` as a count of distinct releases the brand itself names, `active`
yes if any drop is on sale now. A sold-out drop with no current product is `active` = no and still a
row, because the pair is a real edge; it just will not show as current on the page.

## Columns, `return.csv`

- `brand` — key, from `canonical_keys.txt`
- `partner` — the partner's own mark (New Balance, L.L.Bean, Birkenstock); `NONE` for a brand with none
- `partner_on_map` — `yes` if the partner is also in `canonical_keys.txt`, else `no`
- `partner_kind` — clothing brand / footwear brand / retailer / designer-person / artist / institution / other
- `collab_kind` — always `co-branded` in this file (the others go to `excluded.csv`)
- `what_was_made` — plain words, under twelve: "one sneaker, the 990v3"; "a 24-piece fall capsule"
- `first_year`, `latest_year` — four digits; the same year for a one-off
- `drops` — count of distinct releases, `1` for a one-off
- `active` — yes/no as defined above
- `active_url` — the product or collection page where it is on sale now; `NONE` if not active
- `announce_url` — the brand's own announcement, journal post or collection page for the collaboration
- `source` — the URL the row was read from, if different from the two above
- `note`

## Columns, `partners.csv`

One row per **distinct partner**, built from `return.csv` at the end: `partner`, `partner_kind`,
`site_domain`, `mapped_brands_collaborated_with` (semicolon list), `rows` (count), `note`. Sort by
`rows` descending. This is the seating queue; footwear partners are of particular interest.

## Sources, in order

1. The brand's own site: a collaborations page, journal, lookbook, collection navigation, or search
   for the partner's name. This dates and names the thing and is the only source that makes
   `announce_url`.
2. The partner's own site, the same way. Many pairs are documented better on the partner's side
   (New Balance's site lists its collaborators; Barbour's does).
3. Press — Hypebeast, Highsnobiety, GQ, WWD, BoF — to find pairs you did not know to look for, then
   confirmed on 1 or 2. Press alone is not a source for a row.
4. Resale (Grailed, StockX, eBay) proves a thing existed and nothing else. Never a date from resale,
   never an `active` from resale.

## Rules

- Names must match `canonical_keys.txt`; run `python3 reconcile.py` before returning.
- `NC` nobody looked; `NONE` checked, no active collaboration. An empty cell is an error.
- One row per pair. If you are unsure whether two things are one recurring collaboration or two, they
  are two rows with a note.
- Sub-lines seated as their own key (RRL, Purple Label, RLX, Veilance) are their own rows; a
  collaboration under the parent's name goes to the parent.
- A brand that is itself a frequent partner (Barbour, Levi's, Carhartt) will have a long list. Do not
  cap it; the count is the point. Earlier-than-ten-years pairs with no current product may be a single
  summary row per brand with `partner` = `(earlier, n pairs)` and the count in `drops`, if the full
  list would take more than the time box.
- Do not touch the map. Return `return.csv`, `partners.csv`, `excluded.csv` and `NOTE.md`. Nothing else.

## First ten, returned early without stopping

**Todd Snyder, J.Crew, Noah, Aimé Leon Dore, Barbour, Levi's, Carhartt, Engineered Garments, Stone
Island, Loro Piana** — eight heavy collaborators that will break the schema if anything will, and two
luxury houses to confirm the `NONE` path works.

## Time box

Fifteen minutes a brand; forty-five for the heavy collaborators. Past that, what you have, said so.
