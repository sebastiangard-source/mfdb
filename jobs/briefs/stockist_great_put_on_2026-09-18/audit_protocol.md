# Working protocol — audits briefed out, design and QA held here

Written 18 August 2026, after the locations pass. It exists because that pass came back good
and still could not be merged: the schema validated, and most of the file was unusable anyway.
Everything below is drawn from what went wrong there.

## The split

**This thread holds** the file, the design decisions, the validator, and the merge. Nothing enters
`menswear_spectrum.html` without passing through here.

**An audit thread holds** one bounded research job, and returns flat data. It does not touch the
HTML, does not design the feature its data will feed, and does not decide what the map does with
what it finds.

The reason is not territorial. Research threads optimise for coverage — the natural instinct is to
fill every row. The merge has to optimise for the opposite: **for this project, wrong is worse than
missing.** Those two pressures should not live in the same head.

---

## What every brief must specify

**1. The canonical key list.** Brand names must match `canonical_keys.txt` exactly. Two dozen of the 204
carry punctuation or accents another thread renders differently — `J.McLaughlin`, `Dolce&Gabbana`,
`Arc'teryx`, `Hermès`, `A.P.C.`. A mismatch does not error. It writes a row that displays nowhere.
Run `reconcile.py` before returning anything.

**2. A flat schema, one row per finding**, with every column named and its legal values listed.
CSV or JSON array. Never prose, never a document to be parsed back out.

**3. A required provenance column.** (Added 13 Sep 2026, Sebastian's ruling: reading a path a
site's robots.txt disallows is in bounds; record the path, as with any other source.) Not optional, not backfillable later. What was looked at, and
where. `N/A` is not provenance; `N/A — ported from an earlier pass` at least says which. A URL is
better than either.

**4. An explicit not-checked value.** Every schema needs a way to say *nobody looked*, distinct
from *looked and found nothing*. This is the single most common failure. In the locations pass, 26
brands carried an identical boilerplate note asserting zero US stores; two of them were wrong, and
one of those had a well-known flagship. The finding and the assumption were rendering identically.

**5. What is out of scope, and what to do when the boundary is hit.** Record it anyway, in a
separate column or file. The locations brief excluded shop-in-shops; Paul & Shark turned out to
have twenty of them and no standalone doors. Discarding that would have lost the whole finding.

**6. A pilot.** Five to ten items, returned and reviewed before the rest is attempted. Format
errors caught at ten items cost minutes. Caught at 2,500 they cost the pass.

---

## What comes back

Two files and nothing else:

- **The data**, in the briefed schema.
- **A short note** covering: what was checked, what was not reached, what contradicted the existing
  record, and anything the brief got wrong. That last one has been the most valuable part of every
  return so far.

**Do not send a summary in place of data.** Do not send the working files. Do not send a rebuilt
version of the tool — one thread, unable to find `menswear_spectrum.html`, helpfully built a
parallel HTML page from scratch, and it is now a second copy of the same numbers that will drift.

---

## What happens here on return

In order, every time:

1. `reconcile.py` on the brand names. Zero rewrites, zero unmatched, or it goes back.
2. Triage against completeness and provenance. Anything that cannot be told apart from a guess is
   held, not merged.
3. Merge the part that survives.
4. `validate.py`.
5. Render in a headless browser and **read the output**. Every session so far has caught something
   here that the data alone did not show: a phrase printed twice, a row reading `381 of 381
   verified — incomplete`, a bar drawn at 119% of its track.
6. Log what was merged and what was held, in the changelog.

**Held is normal.** In the first locations return, 21 brands of 186 merged. Nobody had done bad
work; the file simply could not tell good rows from unsourced ones. One round of provenance
backfill took it to 171.

---

## What an audit thread should push back on

Briefs from here have been wrong twice, and both times the audit thread was right to say so.

- The first locations brief asked for door counts plus flagships for large fleets. That produced a
  clean flagship map and a dataset that asserted Levi's has one US store.
- The same brief excluded shop-in-shops, which for several brands is their entire American
  distribution.

If a brief asks for something that will produce a confident wrong answer, say so before doing it.
