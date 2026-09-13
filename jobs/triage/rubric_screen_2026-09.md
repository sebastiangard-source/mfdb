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
- Fibre-supplier marks (Tencel on 35 brands) as "names a technology" (recommend: only where the house
  leads with it — which makes it a judgement the evidence record should carry, not a count).
- Disallowed endpoints (recommend: out of bounds; Stone Island's census held until reproduced).

## Back to the thread

Four brands to add · the origin vocabulary pass · six missing evidence URLs · styles denominators on
the depth table · the 451 marks classified · Patagonia · Stone Island held or reproduced. Then close.
