# seat_kotn_eot_2026-10-07 — everything needed to seat Kotn and Every Other Thursday

**Issued** 7 October 2026 · **Kind** seating evidence · **Two brands, no pilot** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the `seat_resort` record for two brands. The rules files in this
folder are the standing rules and win over any shorthand here. **You gather and you propose; Sebastian
rules.** Nothing you return seats a brand or sets a score until he says so.

## The two brands, and the one question each carries

**Kotn** — Toronto, founded 2015, Egyptian cotton basics and the clothes around them, a B Corp, with its
own stores in Canada and at least one in the US. The question for Kotn is **cotton as evidence**: the
brand's whole story is a direct supply chain to Nile Delta farms and schools it has built there. The
craft section (7) tests that story the way the craft audit tests every other — named farms or mills,
on how many product pages, with what documentation — and does not take the sustainability page's word
for it. Also read the US storefront carefully: kotn.com may serve CAD by default; the currency test is
two displayed page prices on the US market path.

**Every Other Thursday** — Ethan Glenn's menswear label, grown out of his TikTok following from 2021,
selling direct online at roughly $150–300 with occasional leather pieces above $1,000. The question here
is **doors**: as far as anyone has established the brand has no store of its own and no stockists, and
the map's bar, with few exceptions, is a few US stores. Section 4 is therefore the first thing to
settle and the first thing to return: own stores (`0` is the finding), pop-ups with dates, stockists
if any. Sebastian rules on whether it is an exception. Everything else in the record is still wanted,
because a bench with a full record seats in one step when the doors arrive.

## What you return

`return.csv` (the 132 columns in `return_template.csv`, both rows, every cell filled), `own_doors.csv`,
`stockists.csv`, `return_styles.csv` (`schema_styles.json`), and `NOTE.md`. Nothing else.

## Sections, and the rules file for each

1. **Store, currency, search** (`rules_prices.md`). US storefront, USD confirmed on two displayed prices.
2. **Eight garments** (`rules_prices.md`, `rules_garment_links.md`). Kotn's tee is the staple and will
   have a real low/high pair; say which. Every Other Thursday's leather jacket is a legitimate
   outerwear high only if it is a regular item, not a drop. Product and URL behind every figure.
3. **Fibre by style** (`rules_fibre.md`). Kotn should read as a one-cloth cotton house; if it does not,
   say what else leads. Count styles, not colourways.
4. **Own doors**, worldwide, US first; concessions and pop-ups as the enum says, with dates for pop-ups.
5. **Stockists** the brand itself lists.
6. **Tech**: expect `none`; say so from the pages.
7. **Craft** (`rules_craft.md`, `rubric_craft.txt`): six facts, two URLs, proposed score, reasoning.
8. **Origin and ownership**: as the brand states, with a filing where one exists (Kotn is a Canadian
   corporation; a federal or Ontario registry record will do).
9. Lookbook. 10. Vinted men's filter and Grailed. 11. B Corp (Kotn's certified entity name from the B
   Lab directory) and GOTS. 12. One real quotation (`rules_quotes.md`) — both founders are interviewed
   often; prefer their own words from the brand's site or a named publication. 13. Signature product
   and pronunciation (Kotn: how the brand says its name, from the site if stated).

## Rules

- Names must match `canonical_keys.txt`; run `python3 reconcile.py`.
- `NC` nobody looked; `NONE` does not sell or do; `np` checked, no price published. No empty cells.
- Full price only. The brand's own statements first, then press that quotes them.
- Do not touch the map. Do not send working files. Out of scope but noticed: `NOTE.md`.

## Order and time box

Every Other Thursday's doors first, returned early without stopping; then both records in full. Forty
minutes a brand for sections 1–5, thirty for 6–13. Past that, what you have, `NC` on the rest, said so.
