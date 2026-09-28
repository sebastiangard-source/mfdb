# logo_count_2026-09-28 — how visibly the mark appears, counted

**Issued** 28 September 2026 · **Kind** count + proposal · **First eight rows returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a count job with a proposal on the end: **you count, you propose a
score, Sebastian rules.**

## The dial

`rubric_logo.txt`. The short form: 1 no visible branding; 2 a small mark on some pieces; 3 a small mark on
most; 4 a prominent mark on nearly every piece, or large marks on a good share; 5 the logo is the design.
The current scores are seeded from memory and are provisional; Stone Island at 4 (the compass badge on
every piece) is the one ruling so far.

## What to count

For each brand, on its own US store, men\u2019s clothing only, **styles not colourways**:

- `styles_read`: how many styles you looked at. Read the whole men\u2019s clothing range where the site allows
  it; where it does not, the first 100 by category, tees and outerwear first, and say which in
  `sample_basis`.
- For each style, from the **main product photo** (the one on the listing tile), classify the mark:
  `none` (no brand mark visible), `small` (a chest logo, a sleeve badge, a label tab \u2014 under about a
  hand\u2019s width), `large` (a mark bigger than that, a big chest logo, a back print), `allover` (a repeating
  logo, monogram or letterform print). A brand mark is the brand\u2019s own; a collaboration partner\u2019s
  mark is noted, not counted.
- `mark_kind`: what the mark is when present \u2014 wordmark, emblem (the pony, the crocodile), badge (Stone
  Island, Moncler), monogram, label tab.
- `proposed_logo`: the score the counts support, with two sentences of `reasoning`. The mapping is a
  judgment, not a formula; roughly, share under 10% is a 1, a small mark on most pieces is a 3, a
  prominent mark on nearly all is a 4, all-over on a real share is a 5.

## Rules

- Main photo only. Do not open each product to hunt for a label; if the mark is not on the tile, it is
  `none`. The dial measures what a stranger sees.
- Men\u2019s clothing only; footwear and bags out. Sub-lines sold under the brand\u2019s name on its own store
  count (Polo\u2019s big-pony pieces count toward Polo).
- `NC` nobody looked; an empty cell is an error. A store that cannot be read returns the current score as
  proposed, confidence noted in `note`.
- Names must match `canonical_keys.txt`; run `reconcile.py` before returning.
- Do not touch the map. Return `return.csv` and `NOTE.md`, nothing else.

Return these eight rows first, without stopping: **Stone Island, Lacoste, Polo Ralph Lauren, Gucci, The Row,
Carhartt, Kith, Everlane** \u2014 the ruled case, a small emblem on everything, a house with both sizes, an
all-over house, a house with nothing, a workwear label tab, a wordmark streetwear brand, a brand that
says it has no logo.

## Time box

Fifteen minutes a brand. Past that, the sample you have, said so.
