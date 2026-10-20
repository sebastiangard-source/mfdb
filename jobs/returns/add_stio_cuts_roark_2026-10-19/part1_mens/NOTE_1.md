# NOTE_1 — add_stio_cuts_roark_2026-10-19, Part 1 (men's record)

Read 19 Oct 2026 in Chrome, on the brands' own US stores (both Shopify, USD active, `Shopify.currency.rate` 1.0). `reconcile.py`: 2 names, 2 exact. Files: `return.csv` (Stio, Roark), `return_styles.csv` (205 rows), `stockists.csv` (350 rows).

## Headline

| | Stio | Roark |
|---|---|---|
| Men's clothing styles | 99 (all with composition) | 106 (all with composition), 6 swim |
| Natural / synthetic / cellulosic | 26 / 74 / 0 | 64 / 36 / 0 |
| Stretch (any elastane) | 31 styles | 29 styles |
| Shape | split | split |
| Synthetic-led categories | trousers, sweats, outerwear, shorts | shorts, other (tights) |
| Tie | shirts 5/5 | outerwear 6/6 |
| Made-in on PDP | 99/99 | 0/106 |
| Proposed tech / craft | 4 / 3 | 2 / 1 |

Stio is a synthetic technical house with a natural side: flannels, the Rivet canvas, cord and jean, PeakWool base layers, and the unisex graphic tees. Roark is mostly cotton tees and cotton/TENCEL wovens, with a synthetic run-and-swim side (Run Amok, boardshorts, Bless Up nylon shirts).

## Checked, and how

- **Stio:** I read `/collections/mens/products.json` (181 items: 99 clothing styles in scope). For each one I fetched the PDP and read its server-rendered "Materials and Care" block. Rollick Rain Pant has no such block, so I read it from Features. Colours are variants inside one product, which is why `colourway_ratio` is 99/99. Unisex tees (5) and hoodies (4) in the men's collection are counted and flagged.
- **Roark:** I read `/collections/shop-all-mens/products.json` (300 colourway products). Each colour is its own product. I collapsed them on the `style:` tag into 121 styles; 106 are clothing, after removing 3 bags, 2 beanies and 10 hats. Composition is the `product.materials` metafield in each PDP's payload, matched to the PDP's own handle. I checked it against the rendered "Materials:" line on the Axeman Parka.
- **Both:** I parsed compositions and checked they sum to 100. The main line is shell over lining and fill. Roark's "Coton" and "Recyceld" typos are mapped. Stio's Alpin polo is a 42.5/42.5 wool/TENCEL tie; first-listed wins, so wool.
- **Stockists:** Stio's locator lists every retailer in the DOM, giving 349 rows. Roark's retailer search is a Stockist.co widget that shows only the 10 nearest, so it's a single `NC` row with the reason.
- **Certifications:** B Corp directory (search "Stio", "Roark"): neither found. GOTS database: no Stio or Roark entity (three fuzzy hits, none theirs).
- **Resale sites:** Vinted brand IDs came from item pages: Stio 3790461, Roark 600960. The men's catalogue URLs load with 158 and 500+ results. Grailed has designer pages for both (Stio 523 listings, Roark 1.3k).

## Not reached / held

- **Stio ownership filing:** the Wyoming SOS business search hung at "Loading…" after one plain submit. I held it and didn't retry.
- **Owner today:** `ND` for both. Roark: La Jolla Group took an equity stake in Dec 2015 (OCBJ). A 2017 OluKai investment shows in search results but I didn't open it.
- **`lookbook_mens` and `pronunciation`:** `NC` for both. Stio's `lines` is also `NC`, because I didn't read its named lines. Roark's lines come from its own `franchise:` tags and the Run Amok tag.
- **Roark stockists:** not enumerated (see above).

## For Sebastian to rule

1. **Stio price gaps.** Stio sells no plain year-round men's tee at full price (the tee low is a unisex logo tee) and no knit sweater (`NONE`). Its only full-price polo is the $129 merino long-sleeve.
2. **Clearance off the men's collection.** Stio's 26 clearance men's styles (Coburn, CFS, Eddy Coast, Divide…) are in the feed but not in `/collections/mens`. I read them as off the main range. If they count, polo low becomes $59 (Divide Polo compare-at) and tee low $49 (Divide Tee).
3. **Craft scores.** Stio's 3 rests on its Open Supply Hub factory list (brand level, not on product pages). Roark's 1 rests on no country, maker or mill anywhere on its site, and an unverifiable "Fair Trade partners" claim.
4. **Tech scale.** No tech rubric was in the folder. I assumed 1–5 and proposed Stio 4 (own PeakProof membrane family plus GORE-TEX PRO, Pertex, Polartec) and Roark 2 (licensed TENCEL, PrimaLoft, REPREVE, Tactel, and an unattributed HOLEYTECH on 19 of 106 styles).

## Contradicts the brief / record

- Stio's men's map would sit on a synthetic house with 14 own stores. The brief's "a few stores of its own" undersells it (see NOTE_0).
- Roark's About page doesn't date or place the founding. The 2009 date comes from the founder in a 2013 trade interview.
- **Stockists file:** the locator writes street and city as one string, so `city` is `ND`, not split. `shop_kind` is `ND`: the locator doesn't say, and the enum has no value for chains like REI, Scheels and Dick's House of Sport. Those rows are flagged as chains by name in `note`. The register rules would exclude department stores; Charles Department Store is flagged.
- **Stockist duplicates:** one exact duplicate (Footloose Sports, Mammoth Lakes) and several near-duplicates (The Backpacker ×3 pairs, REI Rockville, Boot Doctors Telluride, Mountain Sports Arlington). All are kept as listed.

## Cuts Clothing (doors only)

I didn't re-read prices. In passing on today's site search, the AO Curve-Hem Tee shows "Comp. value" $54 against a $38 sale price, during a sitewide "up to 50% off" Fall Sale. The record's $48 tee low may be stale, but a sale-period "comp. value" isn't proof of the regular price. I'd call it worth a re-read, not clearly wrong.
