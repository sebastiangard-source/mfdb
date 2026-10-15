# batch15 — womens_dials_2026-10-14, thread 4

Read 14 October 2026 in Chrome, on each brand's own US store. All ten brands returned: 8 `read`, 2 `partial` (GRACE LING, Hurley — low disclosure, not time). `reconcile.py`: 10 names in, 10 exact, 0 to rewrite, 0 unmatched.

## What was read

| brand | platform / channel | styles read | of site total | with composition |
|---|---|---|---|---|
| EB Denim | Shopify `/products.json` | 60 (all) | 60 | 60 |
| Elan | Shopify feed + PDP "Fabric" accordion | 80 sample | 205 | 73 |
| Elie Saab | Shopify (Swiss store, US/USD) + PDP details list | 80 sample | 442 | 78 |
| Extreme Cashmere | Shopify feed + PDPs | 80 sample | 129 | 80 |
| Generation Love | Shopify `body_html` (10 PDPs checked, all match) | 80 sample | 363 | 80 |
| GRACE LING | Shopify `body_html` + PDPs | 80 sample | 127 | 41 |
| Hurley | Shopify `/collections/womens` + PDPs | 80 sample | 132 | 38 |
| Jamie Haller | Shopify `body_html` + PDPs | 67 (all) | 67 | 65 |
| Johanna Ortiz | Shopify `body_html` (8 PDPs checked) | 80 sample | 372 | 77 |
| Jordan | nike.com product-wall API + PDP `productDetails` | 79 sample | 224 | 79 |

Samples are stratified by category in proportion to the census, systematic within each category. **`styles_total` is the number of styles read — the same set as the percentages — not the site total.** The site total is in `sample_basis`. If the Spectrum thread wants `styles_total` to carry the site total, swap it from `sample_basis`. The percentages should still come from the sample.

## Rulings applied (from Sebastian, this thread)

- **fab_\* basis**: fibre dials use lead fibre over the styles that state a composition. `fab_denim` uses denim-cloth styles over all styles read: the jeans category plus any denim jacket, shirt, skirt or short identified by name or shared wash name. Wool dial = wool + alpaca + mohair + camel + yak. Synth dial = every synthetic-class lead. `fab_basis` gives the shares.
- Batch run straight through, with no pilot stop.

## Headline findings

- **Johanna Ortiz, proposed craft 5.** The house says over 90% of production is in its own atelier in Cali, with an on-site sewing and embroidery school since 2016. 89% of sampled PDPs say "Made in Colombia". This is the strongest craft case in the batch. The case for 4 is in `craft_reasoning`.
- **Elie Saab, craft 3, needs a ruling.** An owned Beirut atelier is on record (WIPO case study), but it makes couture, not the ready-to-wear sold on the US store. That ready-to-wear names no maker and says "Made in Italy" on 22% of pages. Question: does couture making count on an RTW row?
- **Silk-led houses:** Elie Saab (silk 35% of disclosed leads) and Johanna Ortiz (30%) both score `fab_silk` 4. GRACE LING also scores 4 on a thin base. This supports making silk a dial.
- **Extreme Cashmere** is 100% natural-led and cashmere-led on 62% of styles. 28 of 80 styles still carry 1–2% elastane in the main line.

## What contradicted the existing record (worklist)

- **Hurley `outerwear_sold = no`**, but `/collections/womens-jackets-and-outerwear` lists 2 styles (Nomad Shacket, Pit Stop Polar Fleece Jacket). Kept `NONE` per the worklist and flagged here.
- **Elan and Generation Love `tee_sold = no`**, but both Tops pages carry tees and tanks. Kept `NONE` per the worklist.
- **Jordan shoes:** the women's Jordan shoe wall shows "Men's Shoes" tiles in its first rows (unisex sizing). Returned `NC`, URL in `links_kind`.
- **Extreme Cashmere** is a unisex, one-size house. No women's-only listing exists, and its category pages carry the same styles as its "men's classics" collection. Links are filed, but this needs the Lady White Co. ruling.
- **Elie Saab** names fibres in titles that its compositions do not carry. "Printed Cotton Midi Dress", "Cotton Embroidered" dress, skirt and bralette are all 100% polyester, and the "Embellished Crepe Wool Jacket" contains no wool. Filed as the composition line states; per-style notes say so.

## What was not reached / low disclosure

- **GRACE LING:** 39 of 80 sampled PDPs state no composition (jersey pieces say "high stretch jersey"). Status `partial`. `shape = split` rests on 5 disclosed tops, so treat it with care.
- **Hurley:** 42 of 80 sampled PDPs (tees, tanks, dresses, shorts) carry only marketing copy. Checked in the HTML, not just the feed. Status `partial`.
- Elan: 7 PDPs with an empty Fabric accordion. Elie Saab: 2 ND. Johanna Ortiz: 3 ND.

## Scope calls made

- Swim, cover-ups, pareos, kimonos (resort line), boardshorts, rashguards, wetsuits, socks, sports bras, pajamas, slippers, kids' styles ("Girl's …", Mommy & Me) and the Johanna Ortiz Home line were excluded.
- **Hurley's owned Phantom cloth** sits only on women's boardshorts, which this scope puts with swim. `proposed_tech` is 3 on Phantom; it is 1 if the dial reads clothing only.
- **Jordan:** 33 of 224 styles are licensed college/NBA product in the women's Jordan wall. Kept and noted per style.

## What the brief got wrong or left open

1. **`styles_total` under sampling**: see above.
2. **The fibre playbook asks for six files; this brief asks for three.** Returned three. Lines are in the `lines` column where the house names them (Extreme Cashmere's cotton cashmere / light cashmere / double-faced / wool cashmere; Jordan's Sport / Brooklyn / Flight and Dri-FIT).
3. **Unisex houses** need a links ruling (Extreme Cashmere here; Lady White Co. on the men's side).
4. **`proposed_tech` on Jordan**: Nike labels some 100% cotton graphic tees "Dri-FIT", so a share counted on the name overstates the technical share. 20% of styles name a Nike tech cloth; filed as 4.
5. **No current craft scores exist for the women's brands**, so the "proposed ≠ current" table from the craft brief has nothing to compare against. Proposals, largest first:

| brand | proposed_craft | rests on |
|---|---|---|
| Johanna Ortiz | 5 | own Cali atelier (>90% in-house), school since 2016, Made in Colombia on 89% |
| Elie Saab | 3 | owned Beirut couture atelier (third-party record); RTW Made in Italy on 22% |
| EB Denim | 2 | "MADE IN LA" on ~55% |
| Extreme Cashmere | 2 | China production + own team on location; Inner Mongolia fibre |
| GRACE LING | 2 | "Made in New York" on ~4%; 3D-printing method described |
| Jamie Haller | 2 | ~25% state place; factories described, never named |
| Elan | 1 | founding year only |
| Generation Love | 1 | founding year only |
| Hurley | 1 | founding year and region only |
| Jordan | 1 | "Imported" only |

## Out of scope but noticed

- Extreme Cashmere's Shopify feed is priced in the shop currency (`Shopify.currency.rate` 1.1196), not dollars.
- Elie Saab's US store is the Swiss Shopify (`elie-saab-switzerland.myshopify.com`), serving US/USD.
- Most GRACE LING product is pre-order (SS25/FW25/SS26 handles).
