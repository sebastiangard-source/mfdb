# craft_second_read_2026-10-04 — the 56 brands the first read could not settle

**Issued** 4 October 2026 · **Kind** evidence + proposal · **No pilot: every row is a known problem** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. Same job as `craft_audit_2026-10-03`, same columns, same rubric
(`rubric_craft.txt`), for the brands that read came back on at low confidence, could not read at
all, or held pending one fact. **You gather, you propose, Sebastian rules.**

## Why these 56

`worklist.csv` has each brand with the first read\u2019s proposal, its confidence, its note and its
reasoning. The notes say what went wrong: a site that refused automated reads (Kering, Moncler product
pages, John Smedley, Peter Millar, Boggi), a JS shell (Massimo Dutti), a fetch budget that ran out,
origin text hidden in a collapsed tab, a sample of one or two product pages. **Read the note first and
go around the obstacle it names** \u2014 a fresh browser profile with extensions off, the site\u2019s own
product JSON, the collapsed tab opened by hand, the annual report fetched as a document rather than
summarised.

Two groups need a particular fact:

- **Dolce&Gabbana, Fendi, Dior**: the first read found no owned making but did not show it absent.
  Each is a group house with leather-goods factories on the record (LVMH, Capri); find whether any
  owned site makes clothing, and name it or say the filings do not.
- **Zegna** (owned garment plants: the 20-F) and **Rubinacci** (where ready-to-wear is made): one
  fact each, and the 5 holds or falls on it.

## What to establish

The same six facts as the first read, each with a URL: owned facility; named makers on product pages;
named mills on product pages; made-in stated, on what share; heritage claim dated and placed or vague;
process documented. Then `proposed_craft` with two or three sentences a reader could check.

## Rules

- Evidence, not reputation. The brand\u2019s own statements first, then press quoting them, then filings.
- Two URLs per brand. `NC` only if the site cannot be read by any route; say which routes were tried.
- Where the first read\u2019s note says a country may be in a hidden tab, open the tab and settle it.
- Names must match `canonical_keys.txt`; run `reconcile.py` before returning.
- Return `return.csv` and `NOTE.md` (what settled, what still could not be read, and why).

## Time box

Thirty minutes a brand; these are the hard ones. Two shared caps bit the first read \u2014 the session search
cap and ~800 fetches an hour \u2014 so budget fetches per brand rather than per batch.
