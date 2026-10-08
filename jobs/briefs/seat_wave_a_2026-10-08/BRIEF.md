# seat_wave_a_2026-10-08 — full records for 36 brands (wave A of three)

**Issued** 8 October 2026 · **Kind** seating evidence · **Facts-first rows returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the `seat_resort` record — the 132 columns in
`return_template.csv` plus `own_doors.csv`, `stockists.csv`, `return_styles.csv` and `NOTE.md` — for
every brand in `worklist.csv`. The rules files in this folder are the standing rules and win over any
shorthand here. **You gather and you propose; Sebastian rules.**

## What changed on 8 October, so you do not re-decide it

Sebastian ruled that **everything on the gap-analysis list seats**: the 171 brands across three waves
(A: 36 a reader would notice first; B: 54 that fill a thin register; C: 81 with few or no US
doors). That settles the five open rulings for this job:

- **No floor for now.** Uniqlo, Abercrombie, Tommy Hilfiger, Gap and the rest are read like any other
  brand; a sub-premium band may follow once their prices are on file. Return the prices.
- **Sportswear giants seat.** Nike, adidas, New Balance and the rest: a full record each. Their store
  locators are large; count own stores and outlets separately and say which the locator mixes.
- **Shoe-only houses seat.** Seven `NONE` price slots and a `range` on shoes is the expected row.
- **Licenses seat under their own name** (Carhartt WIP is its own key, not Carhartt).
- **Sub-lines with their own stores seat as their own key** (Emporio Armani, Veilance, Y-3, Needles,
  Moncler Grenoble), on the RRL and Purple Label precedent; scope every read to the sub-line's own
  pages and say how.
- **No US door is not a reason to stop.** A brand with zero US own stores returns `0` with the
  locator URL and a full record; the map carries it as positive zero.

## Order

**Facts first, for every brand, returned before any full record:** one row per brand in
`facts_first_template.csv` — site, US store, own-store count with its source, what it sells, an entry
and a top price, a band guess, and the brand's mark as it writes it. Fifteen minutes a brand. This lets
the map seat on provisional bands while the full records come in, and surfaces anything that is not a
clothing or footwear house at all (say so in `note`; do not drop it).

Then the full record, in worklist order. Send the return in batches of ten so nothing waits on the
last brand.

## The sections, and the rules file for each

1. Store, currency, search (`rules_prices.md`). US storefront; USD on two displayed prices.
2. Eight garments, prices and men's listing links (`rules_prices.md`, `rules_garment_links.md`). Product
   and URL behind every figure. A shoe house is `NONE` on seven; a shirtmaker on most.
3. Fibre by style (`rules_fibre.md`, `schema_styles.json`). On a house with thousands of styles (Nike,
   Uniqlo, Abercrombie) count the men's clothing feed and say what was paginated; past the time box,
   `partial` with the share read.
4. Own doors, worldwide, US first; outlets, concessions and pop-ups separately.
5. Stockists the brand itself lists.
6. Tech. 7. Craft (`rules_craft.md`, `rubric_craft.txt`): six facts, two URLs, proposed score and
   reasoning — a famous name earns nothing. 8. Origin and ownership from the brand and filings (many of
   these are listed companies; the annual report is the source). 9. Lookbook. 10. Vinted and Grailed.
   11. B Corp and GOTS. 12. One real quotation (`rules_quotes.md`). 13. Signature product; pronunciation.

## Rules

- Names must match `canonical_keys.txt`; run `python3 reconcile.py` before each return. Where the
  brand's own mark differs, say so in `mark_as_written`; Sebastian rules on marks.
- `NC` nobody looked; `NONE` does not sell or do; `np` no price published. No empty cells.
- Full price only. The brand's own statements first, then press that quotes them, then filings.
- Do not touch the map. Do not send working files. Out of scope but noticed: `NOTE.md`.
- A brand you think belongs on this list and is not: a line in `NOTE.md`.

## Time box

Fifteen minutes a brand on facts-first. Forty a brand on sections 1–5 (seventy-five for a house with a
large feed or a WAF), thirty on 6–13. Past the box, what you have, `NC` on the rest, said so.
