# seat_boyds_2026-10-07 — sift and seat: Boyds' unmapped brands, Noah, Engineered Garments

**Issued** 7 October 2026 · **Kind** seating evidence, two stages · **Stage 1 returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This brief is the `seat_resort` brief run at scale: 59 brands instead of
two, with a sift in front so the full read is spent only where a seat is plausible. The rules files in
this folder are the standing rules and win over any shorthand here. **You gather and you propose;
Sebastian rules.** Nothing you return seats a brand or sets a score until he says so.

## Where the list comes from

Boyds, the Philadelphia menswear store, names 84 brands on its men's designers page; 18 are on the map.
`worklist.csv` holds the 57 that are not and are clothing or footwear (the accessory, fragrance and
collaboration names are in `set_aside.txt`), plus **Noah** and **Engineered Garments**, two New York houses
Sebastian wants seated regardless. Many of the Boyds names are small Italian shirt and knit makers sold
almost only through specialty stores; some will have no US store and no published price, and the sift
is how we find out cheaply.

## Stage 1 — the sift (all 59, returned first, without stopping)

One row per brand in `sift_template.csv`, from the brand's own site and nothing else, fifteen minutes
at most:

- `site_domain`; `us_store` yes/no/none (no site at all); `mens_clothing_or_footwear` yes/no
- `what_it_sells` in plain words under twelve ("Neapolitan shirts, made to order and ready to wear")
- `price_tee_or_entry` and `price_outerwear_or_top`: one entry price and one top-of-range price, currency
  stated, so the band can be guessed; `np` if the site publishes none
- `band_guess`: premium / accessible / trueLux by the price pair, against `rules_prices.md` bands
  ($80–300 · $150–800 · $800+)
- `sift_verdict`: **seat** (a men's clothing or footwear house with a readable site), **bench** (real
  but something blocks a full record now: no US store and no prices, a retailer's private label, a
  sub-line better folded into a seated parent), **reject** (not a clothing house: accessories, a
  fabric mill, a collaboration, defunct)
- `reason`, one sentence a reader could check; `source` URL

Sub-lines: Comme des Garçons Homme Deux and Sartorio (Kiton) each need a stated recommendation — own key
on the RRL/Purple Label precedent, or fold into the parent. Gerald is Boyds' own label: record it, propose
bench. Marco Pescarolo was sifted on 13 September and publishes no prices; confirm and carry the `np`.

Send the sift as soon as it is complete and go straight on to Stage 2 for every **seat** verdict. If
Sebastian strikes names from the seat list you will hear within the day; otherwise the verdicts stand.

## Stage 2 — the full record (every seat verdict; Noah and Engineered Garments first)

Exactly the `seat_resort` record: the 132 columns in `return_template.csv`, plus `own_doors.csv`,
`stockists.csv` and `return_styles.csv`. The sections and their rules files, briefly — the resort brief's
section notes apply in full:

1. Store, currency, search (`rules_prices.md`). US storefront where one exists; otherwise the listed
   store in its own currency, never converted (Maurizio Baldassari is EUR list, ruled 13 Sep).
2. Eight garments, prices and men's listing links (`rules_prices.md`, `rules_garment_links.md`). Product
   and URL behind every figure. Shirtmakers will be `NONE` on most slots; that is the finding.
3. Fibre by style (`rules_fibre.md`, `schema_styles.json`). Swim cells stay in the template; most of
   these houses will return 0.
4. Own doors, worldwide, US first. Concessions and outlets separately.
5. Stockists the brand itself lists. Boyds will appear on many; file it as Boyds, Philadelphia.
6. Tech: named fabrics, owned/licensed/commodity, share of range, proposed score.
7. Craft (`rules_craft.md`, `rubric_craft.txt`): the six facts, two URLs, proposed score and reasoning.
   These Italian makers are where owned making is likeliest on the whole map; test the claim, do not
   repeat it. A named factory with a town is evidence; "our artisans" is not.
8. Origin and ownership, from the brand and filings (Companies House, the Italian Registro Imprese,
   state filings), not press memory.
9. Lookbook. 10. Vinted men's filter and Grailed page. 11. B Corp and GOTS. 12. One real quotation
   (`rules_quotes.md`). 13. Signature product and pronunciation.

Engineered Garments is sold through Nepenthes New York and its own site; read the Nepenthes NY store for
the US price and the brand's own pages for everything else, and say which was which. Noah's doors are
its own (New York, Tokyo, and others); its Mercer Street shop is the US door to record.

## Rules that apply to everything

- Names must match `canonical_keys.txt` exactly; run `python3 reconcile.py` before each return. If a
  brand's own mark differs from the key (accents, capitals), say so in `note` — Sebastian rules on marks.
- `NC` nobody looked; `NONE` does not sell or do; `np` checked, no price published. An empty cell is an
  error.
- Full price only. The brand's own statements first, then press that quotes them, then filings. A
  retailer's description — Boyds' included — is not evidence about the brand.
- Do not touch the map. Do not rebuild anything. Do not send working files.
- Out of scope but noticed: `NOTE.md`, do not discard.

## Returns

Two returns. **First:** `sift.csv` for all 59 and a short `NOTE_sift.md`. **Second:** `return.csv`,
`own_doors.csv`, `stockists.csv`, `return_styles.csv`, `NOTE.md`, for every seat verdict. If the second
is large, send Noah and Engineered Garments ahead of the rest.

## Time box

Fifteen minutes a brand on the sift. Forty a brand on Stage 2 sections 1–5, thirty on 6–13; small
shirtmakers with a dozen styles will take far less. Past the box, what you have, `NC` on the rest, said so.
