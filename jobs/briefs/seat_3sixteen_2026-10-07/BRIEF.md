# seat_3sixteen_2026-10-07 — everything needed to seat 3sixteen

**Issued** 7 October 2026 · **Kind** seating evidence · **One brand, no pilot** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the `seat_resort` record for one brand. The rules files in this
folder are the standing rules and win over any shorthand here. **You gather and you propose; Sebastian
rules.** Nothing you return seats the brand or sets a score until he says so.

## The brand

3sixteen, the New York denim house founded in 2003 by Andrew Chen and Johan Lam, selling raw selvedge
denim and the clothes around it from its own store and a list of specialty stockists. It turns up on
three Mid-Atlantic shop lists already in the register (City Workshop, Franklin & Poe, Totem Brand Co.
among them — check against `registers/trade_brands.csv` and say which). Expect a small range, a long
denim story, Japanese mills by name, and a US store or two.

## What you return

`return.csv` (the 132 columns in `return_template.csv`, every cell filled), `own_doors.csv`,
`stockists.csv`, `return_styles.csv` (`schema_styles.json`), and `NOTE.md`. Nothing else.

## Sections, and the rules file for each

1. **Store, currency, search** (`rules_prices.md`). 3sixteen.com is the US store; confirm USD on two
   displayed prices; `search_url` with the query empty, tested.
2. **Eight garments** (`rules_prices.md`, `rules_garment_links.md`). Jeans is the house's reason to exist:
   low is the cheapest full-price jean in the current main range, high the dearest regular jean (a
   heavier or special-loom denim is a legitimate high; a collaboration or a one-off is not). Say in
   `note` which denims the pair is. Tee, shirt, trousers, sweater, outerwear as the rules say; polo and
   shoes are probably `NONE` — confirm, do not assume. Product and URL behind every figure.
3. **Fibre by style** (`rules_fibre.md`). Count styles, not colourways; denim weights are not styles.
   Swim cells will be 0.
4. **Own doors**, worldwide, US first. The Lower East Side store and anything else the brand runs; a shop
   inside a store is a concession.
5. **Stockists** the brand itself lists, one row each, `shop_kind` as the enum says.
6. **Tech**: almost certainly `none` or `commodity`; say so from the pages, not from the category.
7. **Craft** (`rules_craft.md`, `rubric_craft.txt`). This is the section that matters. 3sixteen names
   its mills (Kuroki is the one most quoted) and says where it sews; test each claim on the brand's
   own pages: which mill, named where, on how many product pages; made-in stated on what share; any
   owned facility (expect no); process documented (sanforization, loom, dye) where. Two URLs,
   `proposed_craft`, two or three sentences of reasoning a reader could check.
8. **Origin and ownership**: founders and year as the brand states them; `independent` unless a filing
   says otherwise, with the URL.
9. Lookbook. 10. Vinted men's filter and Grailed designer page (Grailed will be busy; the page URL is
   enough). 11. B Corp and GOTS. 12. One real quotation (`rules_quotes.md`); Andrew Chen is widely
   interviewed, so prefer his own words from the brand's journal or a named publication. 13. Signature
   product (the house will tell you) and pronunciation ("three-sixteen" — confirm the brand says so).

## Rules

- The name is `3sixteen`, lower case s; run `python3 reconcile.py`.
- `NC` nobody looked; `NONE` does not sell or do; `np` checked, no price published. No empty cells.
- Full price only. The brand's own statements first, then press that quotes them. A stockist's
  description of the brand is not evidence about the brand.
- Do not touch the map. Do not send working files. Out of scope but noticed: `NOTE.md`.

## Time box

Forty minutes for sections 1–5, thirty for 6–13. Past that, what you have, `NC` on the rest, said so.
