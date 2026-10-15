# batch16 — womens_dials_2026-10-14, thread 4

Read 15 October 2026 in Chrome, on each brand's own US store. All ten brands returned: 8 `read`, 2 `partial` (Mestiza New York and Miss Circle, both for low disclosure). `reconcile.py`: 10 names in, 10 exact, 0 to rewrite, 0 unmatched. Same rulings and conventions as batch 15:
- `styles_total` is the number of styles read, the same set the percentages come from.
- The fab dials use the share of disclosed styles by lead fibre.
- Denim is counted by cloth.

## What was read

| brand | channel | styles read | of site total | with composition |
|---|---|---|---|---|
| Kiyonna | Shopify feed + PDPs | 76 (sample) | 210 | 74 |
| LAPOINTE | Shopify `body_html` + PDPs | 80 | 184 | 66 |
| Lauren Manoogian | Shopify + PDP "CONTENT /" line | 80 | 169 | 77 |
| Le Monde Béryl | Shopify | 0 | footwear only | — |
| Lilysilk | US product sitemap + PDPs at 5 s crawl-delay | 81 | ~1,030 handles (includes retired) | 79 |
| MAISON MAYLE | Shopify `body_html` + PDPs | 80 | 106 | 75 |
| Markarian | Shopify `body_html` | 82 | 157 | 78 |
| Mestiza New York | Shopify + PDP "Fabrication:" line | 79 | 234 | 42 |
| Miguelina | Shopify `body_html` | 57 (all) | 57 | 57 |
| Miss Circle | Shopify + PDPs | 80 | ~496 | 19 |

## Headline findings

- **Silk houses**: Lilysilk (silk leads 59% of disclosed styles), MAISON MAYLE (60%) and Markarian (29%) are added to the silk-led group from batch 15.
- **Lauren Manoogian** is 92% natural-led and 0% synthetic-led. Its wool dial reads 5 but is mostly alpaca: 25 alpaca-led styles against 7 wool-led. If alpaca should be its own dial or kept apart from wool, this is the house that shows it.
- **Kiyonna** is the most synthetic house so far: 91% synthetic-led, with spandex in 60 of 74 disclosed styles.
- **Miguelina, proposed craft 3.** A named mill appears on product pages ("woven in Tuscany by Busatti", the Miguelina x Busatti capsule), and handmade filé lace from Brazil is credited.
- **The strongest "made in" signals** are all New York or the USA, but every one is a city or country with no named maker:
  - Markarian: "Made in the USA" on 95% of sampled pages.
  - Lauren Manoogian: Peru or Japan on 83%.
  - MAISON MAYLE: "Made in New York" on 78%.
  - Kiyonna: "Made in the USA" on 50%.

## What contradicted the existing record (worklist)

- **Markarian** is marked as selling no sweaters, trousers or shoes. The site has a Knitwear page, a trouser, and Larroudé x Markarian shoes. I kept `NONE` as the worklist says.
- **Le Monde Béryl**: the worklist is right that it sells only shoes, so every fibre cell is `NONE`. The craft score (2) is read from the shoes: "Made in Italy" on 179 of 180 products.

## Scope calls made

- **Third-party goods resold under a house's own vendor name were excluded:**
  - Kiyonna: NYDJ jeans, plus SPANX, Skinnytees and Vikki Vi basics.
  - Markarian: the Larroudé shoes.
- **Miguelina caftans and cover-ups** (33 records, the house's signature category) were left out as swim cover-ups. If they count as dresses, the house's dress share rises; this needs a ruling.
- **Lilysilk** sleepwear, pajama sets and camisole sets were excluded as sleepwear.
- **Lauren Manoogian** is partly unisex: 41 of the 69 styles in its MEN collection also sit in the women's pages. The range read is the women's pages.

## Disclosure problems (data, not effort)

- **Miss Circle**: only 19 of 80 sampled styles state a composition, and they are nearly all the cotton day pieces. The satin, sequin, velvet and mesh eveningwear that makes up most of the range states nothing. Read its fab dials as "what is disclosed", not as the range.
- **Mestiza New York**: 42 of 79 styles disclose a fibre, 24 of them only through a "Fabrication:" line that names the fibre without percentages. The other 37 give a cloth name only (chiffon, crepe, taffeta, moiré), filed `ND` with the cloth in the note.
- **Lauren Manoogian** writes compositions without % signs ("62 SUPER BABY ALPACA/ 27 CASHMERE / 11 LYCRA"). They are filed exactly as written.

## What the brief got wrong or left open

1. **Lilysilk is not on Shopify**, and its listing pages are client-rendered with no feed. The census came from the product sitemap, which still lists retired styles: 4 of 95 sampled handles returned 404. Its site total overstates the live range.
2. **Style grouping on colour-in-title stores**: Miss Circle (and partly Kiyonna) list each colour as a separate product, with the colour inside the title. I grouped styles by the style name, approximately; `style_method` and `sample_basis` say so.
3. **Proposed craft scores**, largest first. There are no current scores to compare against.

| brand | proposed_craft | rests on |
|---|---|---|
| Miguelina | 3 | Busatti named on the capsule; filé lace from Brazil; country stated on 56% |
| Lauren Manoogian | 2 | Peru/Japan on 83%; New York–Peru operation claimed, not shown |
| Markarian | 2 | "Made in the USA" on 95%; NYC Garment Center; made to order |
| MAISON MAYLE | 2 | "Made in New York" on 78% |
| Kiyonna | 2 | "Made in the USA" on 50% |
| Lilysilk | 2 | own factory since 2015 is claimed but not located |
| Le Monde Béryl | 2 | "Made in Italy" on 99% (shoes) |
| LAPOINTE | 1 | founding date and place only |
| Mestiza New York | 1 | founding date and place only |
| Miss Circle | 1 | founding date and place only |
