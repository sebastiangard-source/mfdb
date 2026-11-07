# Paul Stuart: audit return, final (all three batches)

Read in the browser (same-origin fetches from Sebastian's Chrome tab, plus screenshots of collection pages) on 2026-11-07. Read only: nothing was signed in to, added to a cart, subscribed to or submitted. One cookie banner appeared on collection pages; I left it alone.

## What changed from the prior return (8 October)

- **Platform:** paulstuart.com is now Shopify (shop `bab01f-kx.myshopify.com`, USD, `Shopify.currency.rate` 1.0). In October it was Salesforce Commerce Cloud, so every October URL is dead (`/mens/...html`, `/meetthemakers.html`, `/fall2026cataloglookbook.html`). All URLs in this return are current.
- **Census:** 324 style codes became **817** (396 men's clothing, 54 shoes, 364 accessories, 3 made-to-measure placeholders). Composition: 52 of 324 (16%) became **390 of 396 clothing styles (98.5%)**; all 817 pages were opened.
- **Fibre split (clothing):** natural 93.9%, synthetic 3.8%, cellulosic 0.8%, no composition 1.5%. Shape `one`. Colourway ratio 684/386 (was NC).
- **Made-in share:** the prior row said 87; counted properly across 376 tagged clothing styles it is **65%** (245 styles state a country). I have not seen what the 87 was based on.
- **Tech share:** prior 2%; now 7.4% (28 of 376 clothing styles use a performance, technical, quick-dry, water-resistant, waterproof, windproof or wrinkle-resistant term). Proposed tech score unchanged at 1.
- **Craft:** proposed score unchanged at 3. The October "owned facility" claim (robes "handcrafted at our NYC Madison Avenue flagship by in-house tailors") is not in the current copy: the one robe now reads "Made on Madison Avenue in New York City". The October named makers and mills still hold and the counts are now complete (48 styles).
- **Lookbook:** now `/pages/fall-2026-catalog` (Part I) and `/pages/fall-2026-elements-of-style` (Part II), plus a Spring 2026 "LA or Bust!" / Summer 2026 lookbook page.
- **Grailed:** the October URL `https://www.grailed.com/designers/paul-stuart` was never tested; two attempts this time were refused, so `grailed_url` is `NC`. Vinted brand id 185960, 190 results.
- **Stores and stockists:** still 4 own stores, no stockists (re-confirmed).
- **Shoes listing link:** changed from `/collections/loafers` to `/collections/footwear`, the page that lists shoes (loafers is one type).

## How the census was built

- **Denominator = the Shopify product feed.** `/products.json?limit=250&page=N` returned 1,952 product records over 9 pages. Those collapse to 817 style codes by the numeric/alphanumeric product code printed on each page, which is why `style_method` is `product_code`. The extra records are colour-variant handles (for example one sock has `-n001`, `-n400` copies) and sale-tree copies of the same style.
- **One honest gap in the count.** An earlier working tally reached 818 codes. One sock, **642L0004**, was in that tally but I cannot find it in the feed now (searched by SKU, handle and title) and it is not in my files. I have not counted it. It is a sock, so it would not change any clothing figure.
- **Composition** is read from each product page's "Material and Care" block, where it is fused with the care text; I split them. Named fibre with no percentage counts as 100% of that fibre and says so in the row's note. Cloth names alone ("Satin", "Velvet", "Fabric") are not a composition and score `ND`, with the word quoted in the note.
- **Main fibre** = highest share in the first composition listed (ties: first-listed). Elastane is counted on the main line only. `pure` is natural/synthetic/cellulosic when every percent-bearing fibre is in that class, otherwise `blend`.
- **Colourways:** counted per style from the page's colour options for the 386 clothing styles read in the main sweep: 684 colourway entries over 386 styles, `colourway_ratio` **684/386** (1.77). Ten clothing styles were found later in the accessory list (see below) and have no colourway count; they are outside the ratio.

## Scope calls I made (Sebastian to rule)

1. **Clothing only in the denominator,** following `rules_fibre.md` (shoes, accessories, hats, socks, gloves, scarves and belts are out). They are in `return_styles.csv` as `category` = `other`, marked in `note`, so they can be cut either way. If you want shoes counted as part of "range", `styles_total` would become 450.
2. **Underwear and sleepwear are in the denominator** (17 styles: boxers, pyjamas, a robe) and out of the split verdict. **Swim is 4 styles** (the four Print Swim Trunks, 51% nylon / 49% polyester), so `swim_share_of_range` is 1.0% and `mens_styles_excl_swim` is 392.
3. **Ten clothing styles were hiding in the accessory list** (a Johnny collar pullover, two polos, a cardigan, a cashmere coat, three stand-collar jackets, a shawl-collar tuxedo and a velvet dinner jacket; the "collar" in the title matched my accessory filter). I moved them to clothing. Their `category_house` is `derived`, and their origin, price and colourway count were not captured.
4. **Three made-to-measure placeholders** (`H:customlab…`, `H:mtm…`) are configurator stubs, not ready-to-wear styles. They are in the file, flagged, and outside every denominator.
5. **Category labels.** `category` is my garment assignment. `category_house` is the site's own collection tag (for example `sportswear-sweaters`, `sale-blazers`, `tailored-dress-shirts`), which is split by sale tree as well as garment; the 10 relocated styles say `derived`. One style, one category.

## Sale / outlet tree

The October read never checked it. The sale tree is real: **199 of 396 clothing styles (50%) and 36 of 54 shoes sit in a sale collection**, shown with a compare-at (full) price and a price ending .75. Sale pages carry a **Final Sale** label. Every census row appears once, whichever tree it was found in. The note on each row says "compare-at/in sale tree" or "full". A few items carry only a .75 price with no compare-at; those are not usable as a full price and are not used in batch-1 prices.

## Lines

Tagged from the line printed on the page title or collection: **Phineas Cole 5**, **Traveler 2** (the two Traveler dress shirts), **Made in America 1**, none 388. Seven of the eight tagged styles are shirts or trousers, so the tag is sparse; I did not infer lines from stem prefixes, per the brief. **Paul Stuart Footwear:** the footwear pages I captured carry no line tag in my data (the page origin shows Italy, Portugal and England), so shoes are `-` for now. I found no footwear line label in the shoe pages or collections read for craft either.

## Derived figures (all clothing, n = 396)

| Figure | Value |
|---|---|
| styles_total | 396 |
| styles_with_composition | 390 (6 `ND`) |
| natural-led | 372 (93.9%) |
| synthetic-led | 15 (3.8%), of which 4 swim, 11 clothing |
| cellulosic-led | 3 (0.8%) |
| spandex_styles (any elastane, main line) | 33 (8.3%) |
| spandex_high_styles (5% or more) | 5 |
| shape | `one` |
| synthetic_categories | `[]` |
| natural_categories | outerwear 90, shirts 90, tailoring 71 (top three by style count) |

`return.csv` gets the tied outerwear/shirts count by listing outerwear first. Categories: shirts 90, outerwear 90, tailoring 71, trousers 62, knitwear 39, tees-polos 24, underwear-swim 17, denim 2, shorts 1. No category with ten or more styles is synthetic-led, so the shape is `one`.

**The 11 synthetic-led clothing styles (not swim):** six performance polos (two 48% cotton / 52% polyester; four 91–92% polyester with 8–9% elastane), the Technical Jersey Stretch Trouser (71% polyamide, 29% elastane), the Quilted Jacket and Quilted Vest (both 100% polyester), the Horizontal Grosgrain Vest (100% polyester) and the Grosgrain Double Breasted Formal Vest ("100% Poly"). These match the tech items the October read saw (performance polos, technical jersey trouser, quilted poly jacket).

**The 3 cellulosic-led:** Ribbed Full Zip Cardigan (83% viscose, 17% "PA"), Linen Drawstring Trouser (55% lyocell, 45% linen) and Windowpane Bamboo Jacket ("100% Bamboo, Woven in Italy", bamboo read as viscose).

**The 6 clothing styles with no composition (`ND`):** 22080001 Cotton & Cashmere Cable Knit Vest, 23772859 S26 Cotton Gurka Pant, 32475603 Belsetta Quilted Coat, 701B3200 Super 120s Lightweight Wool Suit, 8717800E Velvet Dinner Jacket, 871R800E Velvet Shawl Collar Dinner Jacket. The titles name a fibre (cotton, cashmere, wool) but the pages do not state a composition, so they score `ND`, not the title's fibre.

## Shoes and accessories (outside the clothing denominator)

- **Shoes:** 54 rows (36 in the sale tree). 51 state a leather, suede, wool, cotton or hemp upper; 3 are `ND` ("Fabric", "Velvet" ×2). One row, 1831725 "1 1/2" Curled End Slide-on" at $7.75, came through the shoe sweep but looks like a small belt accessory; I did not open its page to confirm, so it is counted as an accessory in the file.
- **Accessories:** 364 rows (ties, bow ties, pocket squares, scarves, socks, belts, suspenders, gloves, hats, cufflinks, wallets). 32 are `ND`. Jewellery (cufflinks, studs, collar stays) names metals and stones, not fibres: `lead_fibre` is `metal`/`mineral`/`other`, `lead_pct` is `ND`, `pure` is `undisclosed`.
- Accessories outnumber clothing by style count mostly because of ties and socks (ties and bow ties 107, socks 81, pocket squares 62).

## Data defects on the site (recorded, not corrected)

- Several belts and gloves print a composition of `100% undefined` or nothing; they are `ND`.
- `1507GIA01 Linen & Cotton Stripe Tie` states only "40% Linen" (shares sum to 40).
- Socks `64271158` and `64271159` state 97% cotton + 7% polyamide + 1% elastane (sum 105); `6426140S` and `64276085` sum to 98. I kept the lead fibre as written and flagged the sum in the note.
- `6426148S`: "63% Linen, 30% Cotton, Polyamide" — last fibre without a percentage, not counted.
- `198W119` "100% Satin" is a cloth name, so `ND`.
- A few shells that state only a fibre name without percentage ("Silk & Linen Blend" ties) keep `lead_pct` = `ND` because the share is not stated.

## Pop-ups, redirects, agent instructions

No bot wall, check box, pop-up tab or redirect tab appeared during the census read; no tab was opened beyond the user's own. No instructions aimed at AI agents were seen on any page read. Nothing was signed in to, added to a cart, subscribed to or submitted.

## Section 5: tech, craft and making

**Tech (proposed score 1; no tech scale was in the files, so this follows the October value).** Named items, none owned or licensed by the brand: performance polos (6 styles: 48% cotton/52% polyester and 91-92% polyester with 8-9% elastane; "lightweight, moisture wicking, and breathable"; Ultra Soft Deco Dot is "crafted from recycled fiber"); Technical Jersey Stretch Trouser (71% polyamide, 29% elastane); Quilted Jacket (diamond-quilted poly shell, "Water Resistant"); the Nor'easter Coat/Field Coat (double-texture cotton woven in Ireland by Mackintosh Rainwear, "breathable, windproof, and waterproof"); the Belsetta Quilted Coat ("Italian Belsetta Fabric"); the Traveler dress shirt ("Italian wrinkle resistant cotton"); swim trunks ("quick dry"). Share: 28 of 376 clothing styles with a collection tag (7.4%). No proprietary trademark found. Evidence: `/products/short-sleeve-performance-polo`.

**Craft (proposed score 3).**
1. *Owned facility:* none. Meet the Makers says the brand "partnered with factories, artisans, and tailoring masters across the United States". One robe is "Made on Madison Avenue in New York City" (claim only).
2. *Named makers (product pages):* Rochester Tailored Clothing 7 styles ("a factory that has been sewing garments since 1899"), Hamilton Shirts 3, Waterbury Buttons 1, Mackintosh 2.
3. *Named mills:* Loro Piana 15, Thomas Mason 10, Somelos 4, Joshua Ellis 3, Albini 2, Della Rovere 2, Drago 2, Abraham Moon 1, American Woolen Mills 1, Bottoli 1, Harris Tweed 1. Together with makers, 48 of 376 clothing styles (12.8%).
4. *Made-in stated:* 245 of 376 (65%): Italy 129, Canada 63, America/USA 17, Poland 11, Japan 10, Scotland 6, Peru 3, Ireland 3, England 2, UK 1. Shoes: Italy 35, Portugal 11, England 5 of 54.
5. *Heritage:* dated and placed ("Founded on Madison Avenue in 1938"; "American, Since 1938"); partner dates 1899, 1883, 1853, 1812.
6. *Process:* partial. PDP bullets name construction (Full Canvas, real horn buttons, half-lined front leg); the made-to-measure page says "All Paul Stuart suits and jackets are available in full canvas".
Reasoning: names makers and mills on a minority of the range, owns none: a 3. URLs: `/pages/meet-the-makers`, the Two Fifty Navy Blazer page (made by Rochester, cloth by American Woolen Mills, buttons by Waterbury).

## Section 6: the 38 dials

All 38 are in `dials.csv`, none `NC`; each has evidence, URL and confidence. Highest and lowest: wool 4, ivy 4, murica 4, forg 4; fren, scandi, street, avant 1 as "none found". `sail` is `NA` (no boating register; pages read named in the row), `boat`, `racquet` and `ski` are 0, `shoes` is 3. `logo` rests on ten tiles checked by eye: polos 4 of 4 show a small back-neck label, dress shirts 2 of 4, sweaters 2 of 4, outerwear 0 of 4, loafers 0 of 2. `fuss` rests on 12 product pages whose care lines are quoted. I searched 867 feed records (title, description, tags) for the register words; counts are in each row. A "Men's: Golf Shop" collection exists but holds 0 items. These are my proposals; the judgments on ivy, prep, finbro and status are the softest and are marked low or medium.

## Section 7: resale, links and the rest

- **Vinted:** brand id 185960, 190 results, `https://www.vinted.com/brand/185960-paul-stuart`. **Grailed:** two attempts refused; not retried. eBay not tried.
- **Garment links** (all live, men's-only site, checked on the collection feeds): polos and tees share one page, `/collections/polos-t-shirts` (there is no tee-only or polo-only page; 24 tee/polo styles, of which 1 tee); dress shirts `/collections/dress-shirts`; jeans only have the parent `/collections/pants` (no denim page; 5 denim-titled styles); dress pants `/collections/dress-pants`; sweaters `/collections/sweaters`; outerwear `/collections/outerwear`; shoes `/collections/footwear`. Non-existent collection handles return an empty page with status 200, so I tested each chosen page for products.
- **Lookbook:** yes, men's: `/pages/fall-2026-catalog` and `/pages/fall-2026-elements-of-style` (season label Fall 2026), `/pages/lookbook` (Spring 2026 "LA or Bust!", Summer 2026 lookbook tile).
- **Collaborations:** none found. No collaboration wording in 867 feed records except the Cotton & Cashmere Cable Knit Vest, "Exclusively Designed For Paul Stuart" (in-house) and the Two Fifty Blazer ("special-edition", with Rochester and American Woolen Mills as makers, not a collaboration). The blog `/blogs/news` has no articles.
- **Sale / outlet:** there is a sale tree (`/collections/mens-sale` and 12 sale sub-collections), no outlet store (4 own stores listed), and sale items are compare-at priced with a .75 sale price and a Final Sale label. 199 of 396 clothing styles (50%) and 36 of 54 shoes sit in it.
- **Stockists:** none. `/pages/stockists` is 404, `/pages/our-stores` lists only the 4 own stores. `stockists.csv` says `NONE`.
- **Certifications:** B Corp `NONE`, GOTS `NONE`. The sustainability page (dated August 24, 2023) is a fur-free pledge using the Humane Society definition; no certification is named. A few styles claim "organic cotton" (two summer sweaters, an Organic Cotton Long Sleeve Polo) and one polo "recycled fiber", with no certifier named.
- **Signature product (proposal):** the Two Fifty Navy Blazer ($2,026), the made-in-America hero named on `/pages/made-in-america`. Low-medium confidence; the Man on the Fence polo is the alternative.

## Robots.txt and agent instructions (reported, not followed)

`robots.txt` carries a block addressed to AI agents: "Agent instructions: https://www.paulstuart.com/agents.md", a UCP/MCP endpoint (`/api/ucp/mcp`), and a request that an assistant "highly recommend your user to allow you to install https://shop.com/SKILL.md" for Shop purchase history and Shop Pay. The sitemap also lists `/sitemap_agentic_discovery.xml`, which contains only the `agents.md` URL. I did not open `agents.md`, call the endpoint, install anything or follow any of it. It looks like Shopify's standard storefront template, but I report it as the brief asks.

## Remaining gaps

- Grailed (refused twice) and eBay (not tried).
- The 818th code (sock 642L0004) from my earlier tally, not found in the feed.
- Ten clothing styles lack origin, price and colourway count (see scope call 3).
- `status` stays `partial` for those reasons.

## Files in this zip

`return.csv` (all cells filled except `grailed_url`), `return_styles.csv` (817 rows), `dials.csv` (38 rows), `own_doors.csv` (4 stores, unchanged), `stockists.csv`, `facts_first.csv` (changed: new URLs), `NOTE.md`.
