# craft_audit_2026-10-03 — verifiable making, brand by brand

**Issued** 3 October 2026 · **Kind** evidence + proposal · **First ten rows returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is an evidence job with a proposal on the end: **you gather, you
propose a score, Sebastian rules.** Nothing you return changes a score until he says so.

## The dial

`rubric_craft.txt`. The short form: **verifiable making** — who makes it, where, and for how long. Owned
factories, named mills, documented process and heritage with dates and places score; a hangtag and a
word like \u201cartisanal\u201d do not. A 5 is a house where the maker and the brand are the same thing. A
4 is real owned or named making that does not cover the whole range. A 3 names its makers or mills
and owns nothing. A 2 states a country and little else. A 1 says nothing checkable.

The current scores were authored before any of this was checked, and the one audit we have done by
accident \u2014 putting each 5\u2019s reason on the page \u2014 found a note on the wrong brand within a day.
`worklist.csv` carries each brand\u2019s current score and its written reason; treat the reason as a claim
to test, not a fact.

## What to establish, per brand

Six facts, each with where you saw it:

1. **Owned facility** \u2014 does the brand own a factory, mill or workshop that makes what it sells? Its
   about page, press, filings, LinkedIn, a factory tour. \u201cOur atelier\u201d is a claim; a named place
   with a photograph or a filing is evidence. Say which.
2. **Named makers** \u2014 do product pages name the factory, workshop or maker? (Todd Snyder names the
   Italian maker on 321 styles; most brands name nobody.)
3. **Named mills** \u2014 do product pages name the cloth or yarn mill (Loro Piana, Albini, Candiani,
   Kaihara, Thomas Mason)? Named on the page counts; a generic \u201cItalian fabric\u201d does not.
4. **Made-in stated** \u2014 on how much of the range does the product page state the country? Read a
   sample across categories and say what share.
5. **Heritage claim** \u2014 is the founding story dated and placed, or vague? \u201cSince 1860, Long Eaton\u201d
   is dated and placed; \u201cgenerations of craftsmanship\u201d is vague.
6. **Process documented** \u2014 does the brand publish specifically how its product is made (loopwheel
   machines, garment dyeing after sewing, hand-attached collars), or only that it is made well?

Then `proposed_craft` with two or three sentences of `reasoning` a reader could check on the brand\u2019s
own site. The mapping is judgment, not arithmetic; the rubric steps above are the guide.

## Rules

- **Evidence, not reputation.** A famous name earns nothing. Kiton\u2019s 5 rests on its Arzano factory
  and tailoring school, which can be shown; Gucci\u2019s 4 rests on nothing anyone has checked.
- **The brand\u2019s own statements first**, then press that quotes them, then filings. A retailer\u2019s
  description of a brand is not evidence about the brand.
- **Two URLs per brand**, the two that carry the most weight.
- `NC` nobody looked; an empty cell is an error. A brand whose site cannot be read returns the current
  score as proposed, confidence in `note`.
- Names must match `canonical_keys.txt`; run `reconcile.py` before returning.
- Do not touch the map. Return `return.csv` and `NOTE.md` (a table of every row where proposed \u2260
  current, largest moves first), nothing else.

## First ten, returned early without stopping

**Proper Cloth, Buck Mason, Gucci, Versace, Todd Snyder, AYR, Sunspel, Kiton, Patagonia, Peserico** \u2014
the brand whose note was wrong, the brand it belonged to, two luxury 4s nobody checked, the named-maker
case, the \u201cheld from 4 until the mills get names\u201d case, a settled 5, a settled 5 of a different
kind, a repair-program house, and a house that names its mills but not its makers.

## Time box

Twenty minutes a brand; thirty-five for a luxury house. Past that, what you have, said so.
