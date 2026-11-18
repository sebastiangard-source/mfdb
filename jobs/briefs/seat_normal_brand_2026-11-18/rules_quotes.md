# quotes_2026-09-27 — one real quotation per brand

**Issued** 27 September 2026 · **Kind** read · **First ten rows returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first.

## The job

Each brand page has a line called **In their words**. It may hold only a real quotation — something the
brand or its founder actually said, verbatim — and today only seven brands have one. Find one for each
of the other 197, or establish that there is nothing worth quoting.

## What counts

- **Verbatim.** The words as written or spoken, inside quotation marks in the source or plainly attributed.
  Six to thirty words. You may shorten with an ellipsis; you may not paraphrase, tidy, or stitch two
  sentences from different places into one.
- **In their own voice.** The founder, the current chief executive or creative director, or the house
  writing as itself (an about page, a letter to customers, a mission statement the brand publishes).
  Never a journalist\u2019s description, a retailer\u2019s blurb, a Wikipedia line, or a reviewer.
- **Says something.** A sentence a reader learns from \u2014 what the brand thinks it is, why it makes
  what it makes, a stated rule. A tagline counts only if it is the brand\u2019s own stated line and it
  says something ("We\u2019re in business to save our home planet" yes; "Quality you can trust" no).
- **Sourced.** The page or publication, the URL, the date, and who said it, every row. A quotation
  you cannot point to is `NONE` with a note.

## Where to look, in order

1. The brand\u2019s own site: about, our story, philosophy, founder\u2019s letter, sustainability page.
2. Founder or executive interviews in named publications (trade press, newspapers, the brand\u2019s own
   journal). Record the publication.
3. Company filings and annual reports (the listed houses).
4. Video transcripts only if the line is clear and the video is the brand\u2019s own.

## Rules

- `NC` nobody looked; `NONE` looked and found nothing worth quoting, with the note saying where you
  looked. An empty cell is an error.
- One quotation per brand. If two are good, put the better in `quote` and the other in `note`.
- Prefer the founder over the house, and the house over a hired executive, unless the executive line is
  the better sentence.
- Names must match `canonical_keys.txt`; run `reconcile.py` before returning.
- Do not touch the map. Return `return.csv` and `NOTE.md`, nothing else.

Return these ten rows first, without stopping: **Sunspel, Todd Snyder, Brunello Cucinelli, Vuori, Drake\u2019s,
Mizzen+Main, Hermès, Buck Mason, Aspesi, Stefan Brandt** \u2014 a heritage house, a founder-led American brand,
a philosopher-founder, a performance brand, a revived house, a single-idea company, a house that speaks
only as itself, a DTC brand, a famously silent Italian house, and a physicist.

## Time box

Ten minutes a brand. Past that, `NONE` with where you looked.
