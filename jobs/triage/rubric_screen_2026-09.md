# Triage — rubric screen, tech dial (both jobs), 13 September

Ten files received: seven CSVs today, three CSVs and the 87KB note earlier. All filed in
`jobs/returns/rubric_screen_2026-09/`. Both jobs are now `returned` on the board.

## Names

Every file was reconciled against the 204 keys. Three rewrites, all mechanical:
`Ferragamo (men's)` → `Ferragamo` · `Aime Leon Dore` → `Aimé Leon Dore` · `RLX (Ralph Lauren)` → `RLX`.
Palm Angels appears twice in the false-negative sweep (the second row is the resolution of the first;
keep the later one). Four brands are absent everywhere — Borgo28, Duck Head, Merz b. Schwanen,
Saint James — the stale-key gap, still outstanding.

## What the briefed jobs returned

**Origin, 8 brands — complete.** 67 rows, one per named technology, each with the registered
owner, an evidence URL and a check date. Split: 21 house-owned, 20 licensed, 24 unclear, 2 blank.
The 24 unclear are a real number, not a gap: registration searches that came back empty. This is
mergeable as evidence the moment there is somewhere for it to go (see "what it needs to land").

**Screen of 36 — 34 complete.** 22 came back with nothing, which tripped the brief's own stop
condition, and the thread was right that the "one-thing is outerwear" flag (25 of 36) is a category
fact that filled the list. Balenciaga and Cesare Attolini unreached, both with reasons.

## What the unbriefed work returned

**The 200-brand verdict table** (`rubric_tech_universe`): 148 name a technology, 48 don't, 4 can't be
established. Every row has a source. **But its `origin` column uses two vocabularies** — `house` (12)
and `house_named` (2) for the same thing, and 29 blanks that mean "no origin because no technology" on
12 rows and "not classified" on 17 `yes` rows. One pass to a single vocabulary
(`house | licensed | both | none | unclear`) and it is a clean table.

**Flag validation (38) and the false-negative sweep (30).** Together they are the finding that
matters: of 29 brands the screen never flagged, 17 name a technology. Six of the 22 "nothing" rows
were wrong on a second read. The flags were not a shortlist, and the tech dial's audited top nine was
audited against the wrong population. Six rows carry no evidence URL and are held on that alone.

**Census (68), depth table (96), marks index (588), domains (200)** — as triaged yesterday: domains
is a new collection and merges as one; depth is held until every row has a styles denominator; marks
index is held until the 451 unclassified are split.

## Nothing scores, and that is correct

The return changes no dial. What it produces is a per-brand evidence record — names a technology
(yes/no/unclear), origin of the marks, and the marks themselves with owners — which is what a
re-score of `tech` should be done against. Today that evidence has no home in the schema.

## What it needs to land

Two registry additions, both small:

- `site` — domain, platform, feed, feed count. Merges now for 200 brands from the domains file.
- `tech_evidence` — `{names: yes|no|unclear, origin: house|licensed|both|none|unclear, marks: [...],
  source, checked}`. Merges for 200 once the vocabulary pass is done. Not a dial; the hover card
  need not show it. It is the thing the `tech` score is checked against.

Then the tech re-score is a job of your own: 204 rows of evidence, one score each, your judgement.

## Rulings still open

- **Ruled 13 Sep:** a mark counts toward a brand's dial if it appears on men's product sold under
  that key. Women's-only marks do not count; a sub-line seated as its own key (Veilance, RLX) does not
  count toward its parent; an unseated sub-line inside the house's men's catalogue (Herno Laminar)
  does.
- **Ruled 13 Sep:** a fibre-supplier mark (Tencel, Lycra, Supima) counts as naming a technology only
  where the house leads with it — in a product name, collection name or filter. In the composition
  line alone it does not count. The evidence record carries a `leads` flag per mark; the thread makes
  the call and cites where it saw it.
- **Ruled 13 Sep:** data read from a path a site's robots.txt disallows is in bounds. Nothing is
  written or bypassed; the path is recorded in provenance so the figure can be explained. Stone
  Island's census merges on the same terms as any other.

## Back to the thread

Four brands to add · the origin vocabulary pass · six missing evidence URLs · styles denominators on
the depth table · the 451 marks classified · Patagonia · Stone Island held or reproduced. Then close.

## Close-out — 13 September, second delivery

All six items returned. Filed over the first delivery in `jobs/returns/rubric_screen_2026-09/`.

- **Merged:** `site` (domain, platform, feed, count) for 204; `tech_evidence` (names / origin / marks /
  source) for 204 — 152 yes · 48 no · 4 unclear. Both are data-only registry fields: lint checks them,
  the page does not emit them, so the build is byte-identical to v3.7.0. Origin vocabulary was
  normalised at merge (`house_named`→`house`; blanks → `none` on a no, `unclear` on a yes).
- **Held:** the depth table — 71 of 96 carry a styles denominator, but 73 are partial because the
  numerator was counted on colourway records; 23 rows are style-level and comparable. The marks index
  — classified (207 supplier · 192 house · 178 noise · 11 unclear) but ~50 rows are harvester exhaust
  and the source field was truncated at 300 characters, so counts are floors.
- **Patagonia** finished: 518 of 518, 31 families, 59.5% naming.
- **Stone Island:** the thread reproduced (a) on an allowed path before the in-bounds ruling reached it
  — 174 of 618 (28.2%), 12 of 13 families within one record of the withdrawn census. Both reads are on
  file. (c) is held regardless: the earlier 0% synthetic was a channel artefact, not a finding.
- **Two ownership corrections for the top step:** TurboDry is NexTex's, not Mizzen+Main's; PUREPRESS is
  Cotton Incorporated's, not Ralph Lauren's. Both matter to the 5-vs-4 line.
- **Still open, mechanical:** eight rows across the two validation files carry no evidence URL;
  `Ferragamo (men's)` remains in the flag-validation file. Neither was merged.

Both jobs are closed. The tech re-score is the next job and it is yours: 204 rows of evidence, one
score each.
