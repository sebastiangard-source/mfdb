# style_segments_2026-10-11 — segment the Spectrum by style and cool factor

**Issued** 11 October 2026 · **Kind** analysis · **Returns to** Sebastian, who passes it to the Spectrum thread

This brief is self-contained. You are a separate project with no other context; everything you need is
in this folder. Read this file to the end before starting. **You analyze and propose; Sebastian rules.**

## Why

The Menswear Spectrum is a map of 261 menswear brands, each scored by hand on a set of dials and
counted for its full-price, brand-owned US stores. It already segments by price band (Basic, Premium,
Accessible, True Luxury) and by store-count tier. What it lacks is a segmentation by **style and cool
factor**: which brands are hot, which are tasteful but quiet, which are tribal (prep, heritage, outdoor),
which are plain. Cyprus is a card-linked membership program across these brands, and the segments decide
how a brand universe reads to a member and to an investor — "we have the hype end" means something
different from "we have the tailoring end."

A first cut was made on 11 October from rules over the dials (`first_cut_segments.csv`). It is about
90% right and 10% visibly wrong at the edges. This brief asks you to finish it.

## What you are given

**`brand_dials.csv`** — one row per brand, 261 rows, 68 columns. The columns you will use most:

- `band` — basic / premium / accessible / trueLux. Set by a price rule, not by taste.
- `style` 1–5 — how fashion-forward the clothes are. 1 is a plain chino; 5 is runway.
- `tech`, `craft`, `comfort` 1–5 — the brand's focus. Tech is performance fabric and construction;
  craft is make (welted shoes, hand-sewn tailoring, named mills); comfort is softness and ease.
- `logo` 1–5 — how much of the range carries a visible logo. 5 is a box-logo house.
- `whitet` 1–5 — how much the range is built around the basic tee.
- `fuss` −3 to +3 — negative is throw-it-on, positive is dressed and particular.
- **Culture registers**, each 1–5, 1 meaning absent: `street`, `status`, `avant`, `weird`, `prep`,
  `ivy`, `murica`, `ital`, `fren`, `scandi`, `briish`, `golf`, `finbro`, `boat`, `racquet`, `ski`,
  `western`, `rock`, `workwear`, `outdoor`, `surf`. These are the cool-factor ingredients. `status`
  is the luxury-signal register; `street` is streetwear and skate; `avant` is designer/conceptual;
  `weird` is deliberate strangeness; `finbro` is the finance-office uniform; `murica` is Americana.
- `fab_*` — fabric emphasis 1–5 (denim, cashmere, linen, cotton, wool, synth).
- `*_lo`, `*_hi`, `*_ccy` — entry and top price for eight garment slots (tee, polo, dress shirt,
  jeans, pants, sweater, outerwear, shoes), US full price. Empty means the brand does not sell the
  garment. A currency other than USD means the US price could not be read.
- `own_doors` — counted full-price brand-owned US stores. `NC` (two brands) means the locator could not
  be read; it is not zero. `store_tier` is the store-count segmentation already in use:
  No stores · Flagship (1–3) · Coastal circuit (4–12) · Boutique network (13–50) · National chain (51–250)
  · Mass fleet (250+).
- `resale_grailed` — whether the brand has a Grailed designer page on file (a weak resale-heat signal).
- `chan` — channels: O own stores, D department stores, I independents, W web.
- `why` — the one-line description of the brand as the map shows it.

**`first_cut_segments.csv`** — the 11 October rule-based cut: fifteen segments, every brand assigned.
The rules, applied in this order (first match wins):

| # | Segment | Rule |
|---|---|---|
| 1 | Avant / designer | avant ≥4 or weird ≥4 |
| 2 | Hype & drop culture | street ≥4 and (status ≥4 or style ≥4) |
| 3 | Street & sport culture | street ≥4 |
| 4 | Loud luxury | status ≥4 and logo ≥4 |
| 5 | Runway houses | status ≥4, trueLux, logo = 3 |
| 6 | Quiet luxury | status ≥4, trueLux, logo ≤2 |
| 7 | Rock / rebel | rock ≥4 |
| 8 | Performance & athleisure | tech ≥4 and style ≤3 |
| 9 | Tailoring & dress | fuss ≥1, tech ≤2, and (ital/briish/fren ≥3 or finbro ≥3 or ivy ≥3) |
| 10 | Outdoor & coast | outdoor/ski/surf ≥4 |
| 11 | Prep, club & course | golf/racquet/boat/finbro ≥4 or prep/ivy ≥4 |
| 12 | Heritage American | workwear/western/murica ≥4 |
| 13 | Fashion insider | style ≥4 and logo ≤2 |
| 14 | Mainstream contemporary | style ≥3 |
| 15 | Basics & staples | everything else |

Known misfiles in the first cut, so you can see the kind of error the rules make: J.Crew and Southern
Tide in Tailoring (the fuss dial pulled them); Zegna in Prep (finbro); Alo in Fashion insider; The North
Face, Arc'teryx and Fjällräven in Performance rather than Outdoor; Buck Mason in Heritage American; Alden
in Prep rather than Tailoring/craft; Lemaire and Margaret Howell in Tailoring rather than Fashion insider.
Expect about twenty such moves.

**`cyprus_universe_proposed_2026-10-11.xlsx`** — the proposed Cyprus brand universe (304 rows: the
existing v11 list plus every seated brand with more than three stores). Sheet "Proposed universe",
column A is the brand name as the map writes it. Not every row is a seated brand; the ones that are
match `brand_dials.csv` by name.

**`return_template.csv`** — the columns of your main return.

## What you return

1. **`segments.csv`** in the template's columns, one row for every brand in `brand_dials.csv`
   (261 rows, none missing, none added):
   - `segment` — your final segment, from your taxonomy.
   - `secondary_segment` — a second segment where the brand sits on a border (Amiri is Hype and Loud
     luxury; Golden Goose is Hype and Status), else empty.
   - `confidence` — `high` the dials and the brand's own description agree; `medium` the dials point
     one way and judgment another; `low` the dials are thin or contradictory and a ruling is needed.
   - `rule_or_reason` — the rule that placed it, or a one-line reason where you overrode a rule.
   - `moved_from_first_cut` — the first-cut segment if you moved it, else empty.
   - `note` — anything a reader needs.

2. **`taxonomy.md`** — the final segment list, each with a one-line definition a member would
   understand, the rule that produces it from the dials, the number of brands, and five example brands.
   Keep it to 12–16 segments. Merge any segment under four brands into its neighbor or justify it
   (Runway houses at three brands is a candidate for merging into Loud or Quiet luxury).

3. **`crosstab.csv`** — segment × store tier, counts of brands and total doors in each cell. Then
   segment × band. These two tables are what Sebastian will use.

4. **`findings.md`** — what the segmentation shows, in plain language, under 600 words. Specifically:
   where cool factor and store count run opposite (and where they don't); which segments the proposed
   Cyprus universe covers well and which it misses or over-weights; which segments are most and least
   expensive by dress-shirt and sweater entry; and anything the dials cannot see that a second pass
   should score (a resale-heat dial, a drop-cadence dial, a press-mention dial — say what and why).

5. **`NOTE.md`** — what you did, what you could not, and where this brief would have produced a
   confident wrong answer.

## Rules

- **The dials are the evidence.** Every placement must be traceable to columns in `brand_dials.csv`,
  with the `why` line and the price columns as tie-breakers. You may use what you know of a brand to
  override a rule, but say so in `rule_or_reason` and mark the row `medium` or `low`. You may not
  rescore a dial; if a dial looks wrong, say which in `NOTE.md` and place the brand on the rest.
- **Rule order is a design choice, and you may change it.** A brand that is both Hype and True Luxury
  (Amiri) files where the taxonomy says it files; the other goes in `secondary_segment`.
- **Wrong is worse than missing.** A `low` confidence row with a clear reason beats a confident guess.
  Never leave a cell empty; the word for "nothing" is `-`.
- **Names must match `brand_dials.csv` exactly**, including accents and punctuation (Stüssy, Dolce&Gabbana,
  Aimé Leon Dore, L.L.Bean). Do not retype them; copy them.
- **No web research is needed or wanted.** This is an analysis of the data in the folder. Do not look
  up store counts or prices; the folder's numbers are the ruled numbers, and `NC` means not counted,
  never zero.
- Plain language, American spelling, no hedging phrases. Segment names should be two to four words a
  member would recognize.
- Do not touch the input files.

## Order and time box

Read `brand_dials.csv` and `first_cut_segments.csv` in full. Settle the taxonomy first and write it
down before placing a single brand. Then place all 261, hardest last. Then the cross-tabs, then the
findings. Two hours; past that, return what you have with the gaps marked `low`.
