# batch17 — womens_dials_2026-10-14, thread 4

Read 15 October 2026 in Chrome, on each brand's own US store. All ten brands returned `read`. `reconcile.py`: 10 names in, 10 exact, 0 to rewrite, 0 unmatched. Conventions are the same as batches 15–16:
- `styles_total` is the number of styles read, the same set the percentages come from; the site total is in `sample_basis`.
- The fab dials use the share of disclosed styles by lead fibre.
- Denim is counted by cloth.

## What was read

| brand | channel | styles read | of site total | with composition |
|---|---|---|---|---|
| MONSE | Shopify + PDPs | 80 | 141 | 66 |
| MOTHER | Shopify (own vendor, `Division: Womens` tag) + PDPs | 79 | 281 | 76 |
| NYDJ | Shopify + PDPs | 80 | 218 | 76 |
| R13 | Shopify `body_html`, product tags, PDPs | 80 | 214 | 80 |
| Reem Acra | Shopify | 0 | nothing sold online | — |
| Retrofête | Shopify `body_html` (own vendor only) | 79 | 2,459 (incl. sold-out archive) | 76 |
| RIXO | Shopify `/en-us` + PDPs | 81 | 383 | 80 |
| Róhe | Shopify `body_html` + PDPs | 80 | 208 | 77 |
| RÙADH | Shopify + PDP "Sustainability" text | 70 (all) | 70 | 69 |
| Salt Life | Shopify `/collections/womens` + PDPs | 77 | 110 | 72 |

## Headline findings

- **RÙADH, proposed craft 4: the strongest making disclosure in thread 4 so far.**
  - Every product page names the factory and the country: SAITEX (USA), Texmade (Portugal), So.Pam (Italy), a Hawick knitter.
  - Most pages also name the mill: Lanificio Luigi Ricceri, Canclini, Cariaggi.
  - It stops at 4 because the house owns none of these makers.
- **MOTHER, proposed craft 3.**
  - It owns a sewing unit, MOTHER Maker, an LA contractor bought in 2023 that does about 20% of the sewing.
  - 72% of sampled pages say "Made in Los Angeles", and the house claims over 90% of its production is in LA.
  - Mills and wash houses go unnamed. The case for 4 is in `craft_reasoning`.
- **Reem Acra, proposed craft 3.** It has a located atelier (501 Fifth Ave) and every order is made to order in NYC. It sells nothing online, so every link and fibre cell is `NONE`.
- **NYDJ, proposed tech 4.**
  - The house is built on Lift Tuck®, a patented tummy-panel construction rather than a fabric. It appears on about 55% of sampled styles.
  - Other names: Sculpt-Her, Sure Stretch and Re-New, plus licensed Coolmax, Lycra and ISKO Reform.
  - I filed 4 rather than 5 because the brief's 5 is for a house built on its own performance *fabric*.
- **Salt Life, proposed tech 3.** Its SLX performance line (UPF 50, quick-dry) is about 23% of sampled styles.
- **Fibre profile:**
  - Denim-led: MOTHER (denim cloth 56%) and NYDJ (42%).
  - Wool-led: Róhe (44%) and MONSE (39%).
  - Natural-led: R13 (94%) and RÙADH (96%).
  - Viscose print-dress house: RIXO (viscose 44%).
  - Most synthetic: Retrofête (43% synthetic-led).

## What contradicted the existing record (worklist)

- **NYDJ shoes `yes`.** There is no shoe page in the nav, and `/collections/shoes`, `/womens-shoes` and `/footwear` are all empty. The feed still holds 39 footwear records from the 2022–24 seasons. I filed `NC` and think the worklist is stale.
- **Salt Life dress and outerwear `yes`.** There is no dress or jacket page in the nav; three dresses and three jackets exist. I filed the parent All Women's page for dress and the live (unlinked) `/collections/womens-jackets` for outerwear.
- **Retrofête tee and sweater `no`.** The site has a few sweaters and cotton tops. I kept `NONE` per the worklist.
- **Reem Acra (all `no`): confirmed.** The `Look NN` products are $0.00 lookbook pages with "Make an appointment".

## Scope calls made

- **Third-party stock excluded:**
  - MOTHER resells Alix of Bohemia, Eterne, XiRENA, SPRWMN and others.
  - Retrofête resells SEROYA (the founder's second label, 1,788 records), Charo Ruiz, Hemant & Nandita and others.
  - NYDJ's Gibsonlook collab vendor.
- **R13's feed vendor "RATT"** carries the same tags as "R13" and is the house's own; it was kept.
- **Excluded as out of scope:** Salt Life's Aquatrunks (swim) and a cover-up shirt; one Retrofête embellished bra.

## Data problems found and fixed

1. **RÙADH:** the generic parse read the line "Labels made in Italy in 100% Viscose" on 15 pages as the garment composition. All 15 were re-read by hand from the Sustainability text and corrected. Several denim pages name the cotton ("Japanese Better Cotton") with no %; these are filed as named, lead cotton.
2. **R13:** labels are written without commas ("59% VIRGIN WOOL 18% POLYAMIDE … 2% AF"). They are filed with commas, and the raw label is in the style note.
3. **Malformed labels filed as found, not guessed:**
   - Retrofête Regina Dress sums to 40% (filed `ND`).
   - Retrofête Jazlyn Dress lists two parts.
   - R13 Boyfriend Cardigan sums to 130%.
   - Róhe has three single-fibre labels below 100% ("90% merino", "53% polyester").
4. **R13 country of making** sits only in hidden feed tags (China 42, US 17, Italy 15 of 80), never on the page. `made_in_stated_share` is 0% and the tag split is in the cell.

## Proposed craft scores, largest first

| brand | proposed_craft | rests on |
|---|---|---|
| RÙADH | 4 | maker and country named on ~100% of pages; named mills; nothing owned |
| MOTHER | 3 | owned MOTHER Maker sewing unit (~20%); Made in LA on 72% |
| Reem Acra | 3 | located NYC atelier; made to order in NYC (nothing sold online) |
| MONSE | 2 | country on 95% (USA/China); unlocated in-house atelier claim |
| NYDJ | 2 | one named mill (ISKO) on one denim line |
| Retrofête | 2 | country on ~100% (China/India) |
| Róhe | 2 | Amsterdam design atelier (pattern making, not production); European makers unnamed |
| R13 | 1 | no making stated on the page |
| RIXO | 1 | no making stated; one anecdotal London factory in the founding story |
| Salt Life | 1 | nothing stated |
