# batch18 — womens_dials_2026-10-14, thread 4

Read 15 October 2026 in Chrome, on each brand's own US store. All ten brands returned `read`. `reconcile.py`: 10 names in, 10 exact, 0 to rewrite, 0 unmatched. Conventions are the same as batches 15–17:
- `styles_total` is the number of styles read; the site total is in `sample_basis`.
- The fab dials use the share of disclosed styles by lead fibre.
- Denim is counted by cloth.

## What was read

| brand | channel | styles read | of site total | with composition |
|---|---|---|---|---|
| Sanctuary | Shopify `body_html` | 80 | 263 | 80 |
| Sea | Shopify `body_html` | 80 | 350 | 80 |
| Simone Rocha | Shopify US store + PDPs | 76 | 93 | 70 |
| Terez | Shopify, style-number tag + PDP "Fabric" block | 80 | 125 | 70 |
| The Frankie Shop | Shopify `/collections/womens-clothing`, own vendor | 80 | 934 | 80 |
| Toccin | Shopify `body_html` + PDPs | 78 | 235 | 73 |
| Veronica de Piante | Shopify + PDP "Product details" | 77 | 94 | 76 |
| Victoria Beckham | Shopify `/en-us` + PDPs | 77 | 194 | 71 |
| Wiederhoeft | Shopify `body_html` | 77 | 117 | 76 |
| Yves Salomon | Shopify US store, women's collections + PDP "Composition" | 80 | 322 | 79 |

## Headline findings

- **Yves Salomon, proposed craft 3.**
  - It is a fur house with a dated four-generation furrier history (Paris since 1920), Loro Piana cloth named on part of the range, and claimed Paris workshops doing made-to-measure.
  - No product page states a country.
- **Fur has no dial.** Yves Salomon is 13 of 79 styles fur-led (mink, fox, rex rabbit) and 21 leather/shearling-led. The build now counts fur as natural.
  - Re-running batches 15–17 with that change altered nothing.
  - Fur trims on wool or technical shells are filed under the shell fibre, with the fur in the style note.
- **Silk-led or silk-heavy:**
  - Veronica de Piante: silk 25%, wool 25%, 100% "Made in Italy".
  - Wiederhoeft: silk 30%.
- **Most synthetic:**
  - The Frankie Shop: 49% synthetic-led, with PU faux-leather outerwear.
  - Wiederhoeft: 43% synthetic-led, from its beaded poly/spandex gowns.
  - Simone Rocha: 39% synthetic-led.
- **Split shape:** Simone Rocha, Terez and Wiederhoeft.
- **Terez, proposed tech 3.** Its own names are TLC, Flex, Hi-Shine, DuoKnit and Action, on about 19% of sampled styles. Most of the house is MLB/NBA/NFL licensed sportswear: 333 of 441 women's listings, kept and noted as for Jordan.
- **Strongest country-of-making disclosure:**
  - Veronica de Piante: Italy on 100%, with the workshop towns named by category (Gallarate knits, Prato, Parma couture).
  - Wiederhoeft: New York on 98%, made to order with a 24-week lead time.
  - The Frankie Shop: 99%, mostly South Korea.
  - Victoria Beckham: 95%, mostly Portugal.
  - None names a maker, so all four are proposed 2.

## What contradicted the existing record (worklist)

- **Simone Rocha trousers `no`.** A women's "Trousers & Shorts" page exists. I kept `NONE`.
- **Terez blouse `no`.** Two rayon button-downs exist. I kept `NONE`.
- **Wiederhoeft:**
  - Shoes `no`, but the store sells mules and pumps. I kept `NONE`.
  - There are no category pages at all: `/collections/dresses`, `/skirts`, `/jackets` and the rest are empty. Garment links point to the two parent listings, In-Stock and Made-to-Order, wherever the garment actually sits.
- **Terez outerwear.** There is no jacket page in the nav. `/collections/bomber-jackets` is live, but its first tiles are "Unisex" licensed bombers. I filed it and flagged it; it needs the unisex ruling.
- **Sea shoes.** There is no shoe page; three flats sit inside Accessories (parent), which is what I filed.

## Scope calls made

- **Other labels on the store excluded:**
  - The Frankie Shop resells about 90 labels.
  - Simone Rocha's adidas and Crocs collab vendors.
  - Toccin's Canfora Capri footwear vendor.
  - Wiederhoeft's menswear collection.
- **Dropped as accessories, lingerie or kids:** snoods, foulards, necklaces, bralettes, a Terez sports bra line, and one Toccin kids' cardigan.
- **Victoria Beckham** feed records under a "Victoria Beckham UK" vendor were kept, since they are the same house.

## Data problems found and fixed

1. **Labels run together with the lining text** were re-read by hand:
   - Veronica de Piante, 5 labels: "100% Goat SkinLining: 100% Cupro" had been read as cupro.
   - The Frankie Shop, 2 labels.
   - Toccin, 1 label.
2. **Wiederhoeft labels with a stray space inside the number** ("7 0%", "8 4%", "1 00%") were read as 70/84/100, and the raw form is in the style note. One label is garbled and filed `ND`.
3. **Terez pages name fibres in order with no percentages** ("Cotton/Nylon"). They are filed as named, with the lead as the first fibre named, so Terez's `spandex_styles` is not meaningful.
4. **Malformed labels filed as found, not guessed:**
   - Simone Rocha dress sums to 110%: `ND`.
   - Veronica de Piante "Luna Polo in Cashmere" reads "100% silk finishing": `ND`.
   - Wiederhoeft lilac corsets sum to 110%: filed as written.
5. **Feed product types were wrong or inconsistent** at Toccin (a cami typed as a skirt) and Victoria Beckham (generic types). Categories come from titles.

## Proposed craft scores, largest first

| brand | proposed_craft | rests on |
|---|---|---|
| Yves Salomon | 3 | dated furrier heritage since 1920; Loro Piana named; Paris workshops claimed, unlocated |
| Veronica de Piante | 2 | Made in Italy 100%; workshop towns named, makers not |
| Wiederhoeft | 2 | Made in New York 98%; made to order; NYC showroom fittings |
| The Frankie Shop | 2 | country on 99% (South Korea 50 of 80) |
| Victoria Beckham | 2 | country on 95% (Portugal 43 of 80) |
| Sanctuary | 1 | founded LA 1997; nothing on making |
| Sea | 1 | founders only |
| Simone Rocha | 1 | US store states nothing on making |
| Terez | 1 | founded 2008; nothing on making |
| Toccin | 1 | about page is an empty template |
