# Batch 03 — womens_dials_2026-10-14, thread 1

Read 15 October 2026, in Chrome, on each brand's own US store. I used the same defaults as batch 02:

- **Own labels only.** Stocked brands at Jenni Kayne (AGOLDE, RE/DONE) were dropped. Co-branded collabs sold under the brand's own vendor name are kept and tagged in `lines`. These are LoveShackFancy's collabs and Marc Jacobs' Heaven line.
- **Unchanged from batch 01:** the category mapping, denim as garments, sleepwear and swim excluded, and the 80-style sample.

`reconcile.py`: 10 names in, 10 exact, 0 to rewrite, 0 unmatched.

## What came back

| brand | status | styles (with comp.) | nat / syn / cell % | spandex | shape | denim·cash·linen·cotton·wool·synth·silk | tech | craft |
|---|---|---|---|---|---|---|---|---|
| Veronica Beard | read | 80 (80) | 64 / 19 / 18 | 36 | one | 3·2·1·4·2·3·2 | 2 | 2 |
| Steve Madden | partial | 80 (79) | 36 / 54 / 9 | 32 | split | 3·1·1·4·1·5·1 | 2 | 1 |
| GUESS | partial | 80 (40) | 18 / 21 / 11 | 17 | one | 3·1·1·3·2·4·1 | 2 | 1 |
| Kate Spade New York | partial | 73 (57) | 41 / 18 / 19 | 6 | one | 2·1·1·4·3·3·1 | 1 | 1 |
| Alice + Olivia | read | 80 (79) | 48 / 32 / 19 | 37 | split | 3·2·2·4·3·4·2 | 1 | 1 |
| Marc Jacobs | read | 79 (50) | 41 / 16 / 6 | 9 | split | 3·1·1·4·2·3·2 | 1 | 1 |
| Zimmermann | read | 80 (79) | 60 / 14 / 25 | 11 | one | 3·1·3·4·3·3·3 | 1 | 1 |
| Jenni Kayne | partial | 74 (72) | 80 / 5 / 12 | 5 | one | 2·3·2·4·4·2·1 | 1 | 2 |
| Chanel | partial | 80 (65) | 80 / 1 / 0 | 0 | one | 2·3·1·3·4·2·3 | 1 | 4 |
| LoveShackFancy | read | 80 (77) | 68 / 22 / 6 | 7 | one | 2·1·2·5·2·4·3 | 1 | 1 |

`partial` means at least one cell is `NC`; the `note` column names the cells. Shares are of all styles in the table, including those with no composition, so brands with many ND rows are understated (GUESS, Marc Jacobs, Kate Spade, Chanel).

### Craft

- **Chanel — 4.** Chanel owns and names its Métiers d'art houses: Lesage (embroidery and tweed), Lemarié, Goossens, Massaro, Atelier Montex and Maison Michel, gathered at le19M in Paris. Its savoir-faire page documents process (Lunéville crochet hook, the Cornely machine). Product pages name no maker or country, and the owned making covers embellishment and some tweeds, not the range. So this is a 4, not a 5.
- **Veronica Beard — 2.** 15 of 80 pages say "Made in the USA" or "Made in LA", mostly denim and tailoring. The denim pages name the fabric's country (Italian, Japanese or Turkish denim), but no mill.
- **Jenni Kayne — 2.** 73 of 74 pages state a country. Many also name a fibre origin (Italian fabric, Mongolian cashmere, Peruvian alpaca), but no maker or mill.
- **The other seven are 1.**
  - Steve Madden, Kate Spade and Alice + Olivia say "Imported" on every page.
  - GUESS, Marc Jacobs and Zimmermann state no country at all.
  - LoveShackFancy states one on 2 of 80 pages.
  - Zimmermann's sustainability page mentions "partnerships with our factories" but names none.

### Tech

No brand in this batch names a technical fabric. Veronica Beard, Steve Madden and GUESS are 2 on stretch-denim and stretch claims. The other seven are 1.

## Contradicts the worklist

The cells below are filed `NONE` per the brief, although the store sells the item:

| brand | worklist | what the store shows |
|---|---|---|
| Steve Madden | tees and blouses not sold | Tops & Shirts holds 79 products, mostly woven and knit tops |
| Jenni Kayne | jeans not sold | its own jeans (Topanga, Ojai, Fran, Ollie, 90s Jean) in a Denim collection |
| LoveShackFancy | shoes not sold | a Shoes collection with 8 products typed Shoes |

Two more points:

- **Chanel ready-to-wear is shown with prices but not sold online** ("Contact Us"). There is one curated RTW page with no garment sub-categories, so every garment link cell points to it.
- **Jenni Kayne is partly a stockist.** It sells AGOLDE and RE/DONE alongside its own label (vendor field in its product feed).

## Not reached, or read with less than the playbook asks

- **Composition missing on the page:**
  - **GUESS: 40 of 80.** The "Composition & Care" field is empty on nearly every current-season style, and the rendered page shows none either.
  - **Marc Jacobs: 29 of 79,** nearly all Heaven styles, many of them older listings still live.
  - **Kate Spade: 16 of 73.** These name only a fabric ("Crispy poplin", "Organza", "Denim", "Neoprene").
- **Fibres named without percentages:**
  - **Chanel** gives material names only ("Wool & Silk", "Cotton, Silk & Mixed Fibers"). Filed as the first-named fibre, percentage ND. "Mixed Fibers", "Tweed", "Denim" and "Jersey" are ND (15 of 80).
  - **Kate Spade** often does the same ("Cotton", "Alpaca, polyamide, wool").
- **Heritage was not read** (`NC`) for Steve Madden and GUESS (no history page), Kate Spade (about pages return 410), Jenni Kayne (the about page has no founding text) and Chanel (its about pages render in script; not opened in the browser).
- **A bot wall at GUESS.** A burst of background category fetches got 403s on 6 nodes. I stopped and redid the census by ordinary page navigation, paced, clicking "Show more" to the end. I made no retries against the 403s.
- **Strata from product names.** At Kate Spade, Marc Jacobs, Zimmermann and Chanel the grid does not carry a sub-category, so strata come from the product name. At Michael Kors in batch 02, the filter could not be fetched.
- **Lines not read:**
  - Zimmermann's Swim & Resort clothing line.
  - Steve Madden's swim.
  - Marc Jacobs' kids line.
- **Kate Spade is a full census, not a sample:** 73 clothing styles after removing swim, sleepwear and cover-ups.

## Parsing traps found (all fixed before return)

- **Part-labelled compositions.** LoveShackFancy writes "SHELL: … / SELF: … / LINING: …", and 31 pages were missed until the label was allowed. Zimmermann writes "Main: … ; slip: … ; pocketing: …". The shell or main part is filed.
- **House typos read as intended:** "POLYIMIDE", "SELL:" (LoveShackFancy), "polymide", "Vicose" (Kate Spade), "Polyacrylic" (Veronica Beard), "Fuax Fur" (Marc Jacobs).
- **Leather written without the word "leather"** ("100% lamb leather", "100% LAMB") was missed until re-read: 4 pages at Alice + Olivia and LoveShackFancy.
- **Marketing copy instead of a composition.** Veronica Beard gives composition only in description copy on 3 pages ("Made from 100% cotton for a soft…"). It is filed as stated and flagged.

## Out of scope but noticed

- Steve Madden's `/collections/bottoms` holds 120 products but is not in the menu. It is used as the trousers link.
- Each Zimmermann print is its own product name, so the style count slightly overstates garments.
- Each GUESS wash or fabric is its own product code, so 2,232 codes overstates garments.
