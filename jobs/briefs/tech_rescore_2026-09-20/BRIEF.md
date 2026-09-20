# tech_rescore_2026-09-20 — proposed tech scores for 204 brands, from evidence

**Issued** 20 September 2026 · **Kind** rescore proposal · **Pilot** 10 brands first · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a proposal job: **you propose, Sebastian rules.** Nothing you
return changes a score until he says so, row by row. What you return has to be checkable by him in a
minute per brand.

## The dial

`rubric_tech.json` is the definition. The short form: **how technical the clothes are, scored on
depth of technical product; ownership decides only the top step.** A 5 is reserved for a house that
developed what it sells. A 4 is a range as technical, bought in — licensed membranes, or commodity
performance cloth under house names. A 3 is a real but partial technical business. A 1 is a trace.
The old scores were guesses; four of the top nine were wrong when checked.

## What you have

- `tech_evidence.csv` — one row per brand: the current score and its note, whether the house names a
  technology (yes/no/unclear, 204 rows, read 12–13 Sep), the origin of its marks (house / licensed /
  both / none), the marks themselves, the store domain and platform, and the fibre pass's measured
  synthetic share and style count.
- `depth_table_HELD.csv` — share of the range naming a technology for 96 brands. **Held** because 73
  rows were counted on colourways, not styles; 23 are style-level. Use it where `pct_basis` is styles;
  restate the rest.
- `marks_index_HELD.csv` — 588 named fabrics and technologies with owner and kind. Classified but
  dirty: ~50 rows are harvester exhaust, counts are floors.

## Rulings that bind every row

- A mark counts toward the dial only if it appears on **men's product sold under this key**. Women's-
  only marks do not count. A sub-line seated as its own key (Veilance, RLX, RRL) does not count toward
  its parent; an unseated sub-line in the house's men's catalogue (Herno Laminar, Prada Linea Rossa,
  Peter Millar Crown Sport) does.
- A **fibre-supplier mark** (Tencel, Lycra, Supima, Coolmax) counts only where the house **leads with
  it** — in a product name, collection name or filter. In the composition line alone it does not.
  Mark each counted mark `(leads)` or not.
- **Ownership is what the trademark register says**, not what the brand implies. TurboDry is NexTex's,
  not Mizzen+Main's; PUREPRESS is Cotton Incorporated's, not Ralph Lauren's. A house whose only
  registered marks belong to suppliers cannot take a 5.
- **Depth is counted on styles, men's clothing only** (the fibre pass's scope rule). A colourway count
  is not a depth. Say the basis.
- **Naming regime is not substance.** Redvanly's thirty house-named fabrics are ordinary cloths; Vollebak
  names nothing and takes a 5. Judge what the technology does, not how many names it has.

## What to return

One row per brand in `return_template.csv`: the proposed score, the current one, the rubric step it
rests on, ownership, depth and its basis, the marks counted (with owner and `(leads)`), the marks seen
and excluded (with why), one evidence URL, confidence, and **two or three sentences of reasoning a
reader could check on the brand's own site**. Then `NOTE.md`: what moved and why, in a table of every
row where proposed ≠ current, sorted by the size of the move.

Where the evidence on file is thin — the four `unclear` origins, the 33 partial depth rows, the marks
that need a register lookup — **go and read**: the house's own site for what it sells and names, the
USPTO/EUIPO register for who owns a mark. Record the path. A robots-disallowed path is in bounds.

## Rules

- `NC` means nobody looked; an empty cell is an error. A brand you could not reach returns its
  current score as proposed, confidence L, and the block in `note`.
- Names must match `canonical_keys.txt`; run `reconcile.py` before returning.
- Do not touch the map. Return `return.csv` and `NOTE.md`, nothing else.
- Send the pilot first and stop: **Peter Millar, Mack Weldon, Vuori, Sease, Redvanly, Vollebak, Todd
  Snyder, Loro Piana, Stone Island, Palm Angels** — the top of the dial, the two extremes of naming,
  a licensed house, a natural-fibre technical house, and one that should be a 1.

## Time box

Fifteen minutes a brand where the evidence on file suffices; forty where a read is needed.
