# NOTE: seat_farafield_2026-11-06 (Farafield)

Read 6 November 2026 from the US storefront of farafieldclothing.com. Read only: I signed in nowhere, added nothing to a cart and submitted nothing. You rule on every score and every mark.

## What I checked

- **Store and currency.** The tab opened on a US market with USD active. The cart currency is USD, United States is selectable, and product pages say "Ships from the US, no import charges". The feed price equals the displayed price on all 155 live pages (0 mismatches), so USD is confirmed on far more than two prices (for example Shaggy Station Cardigan $240.00 and Nepalese Sunset Buckley Cardigan $225.00). `feed_currency_rate` is 1.365423 (`Shopify.currency.rate`), a hint only. The pound read in the brief was a geolocated UK market.
- **Scope.** Menswear only. About says "independent, family-run menswear brand"; no women's collection or nav exists. I scoped to the 327 products in `/products.json`, then to the 155 whose product page loads.
- **Feed versus live range.** 172 of 327 feed products return 404 (unpublished or sold out: AW26 and SS26 drops, Fundamentals colours, some collaborations). Everything below uses the 155 live pages, which are **120 styles**. A style is the title before " - colour", within a category (`title_dedup`). The earlier facts-first row quoted $88.75 and $390 from the full feed; the entry price comes from a page that no longer loads. The live entry tee is $95.
- **Prices.** 79 of 155 live pages are marked down, many by about 70 percent, so every figure is the compare-at (regular) price. I checked a second product before trusting it: Edmund T-Shirt and Everything is Great T-Shirt both carry a 95 compare-at. All figures are whole dollars with no rounding. Every garment is `range`: the brand has no entry-and-elevated pair of one staple. "Dress shirt" is the casual woven shirt (all the brand makes). "Dress pants" are casual trousers. The brand makes no jeans and no footwear (`NONE`). Collaboration capsules (Capo, POP, Rose Wong) were not used as a high; Fundamentals is a house line and is counted.
- **Fibre.** 118 of 120 styles state a composition; natural-led 90%, synthetic-led 7%, cellulosic-led 2%, no elastane anywhere. Shape is `one`: the only synthetic-led category is swim (2 styles, one with no composition); outerwear is natural-led (12 of 14). Lines: Fundamentals (permanent), Capo Collection, POP and Rose Wong capsules are named; I did not measure them separately (the capsules are all 100% cotton; Fundamentals is mostly cotton with one cotton-lyocell shirt). Two styles state none (the Fundamentals Station Jacket, and the Yami Floral Swim Short). Jacket compositions give a shell line plus lining; I read the shell only. I inserted `;` between sections that the page runs together.
- **Stockists page** is a list, not a set of features: 158 rows (148 distinct shops, 72 in the US, 9 online-only) worldwide, grouped by region. Several shops list more than one address and get a row each. None is a department store; Allen Edmonds (a shoemaker with its own stores) and the online retailers are labelled. No door-one or door-two test was run: that is for you.
- **Own doors.** None. One brand-run **Design Studio & Sample Store in Porto** is counted separately in `own_doors.csv`. A Journal post mentions a one-off sample sale at Combi Coffee in Porto (event, not a store).
- **Craft.** No owned facility and no named factory or mill. Making countries stated: Sri Lanka, India, Turkey, Portugal, UK (Manufacturing & Sustainability). The knitwear partner is an unnamed family-run Istanbul workshop, "honing their craft since 1989", second generation, partnered "for over a decade" (Journal, 4 April 2025). Proposed craft 2.
- **Origin and ownership.** About: founded 2016 by brothers Mark Scholes (Creative Director) and Chris Scholes (Wholesale Director), "based between Brighton and Porto". Endole, a third-party aggregator of Companies House data: Far Afield Ltd, 08090708, incorporated 31 May 2012, directors Mark Scholes, Christopher John Scholes, Hayley Evans and Thomas Anthony Wands; persons with significant control Mark Scholes and Thomas Anthony Wands.
- **Lookbook.** AW26 "Collection #20, Upper Mustang, Nepal" (Journal); the Lookbook Archive page lists 13 seasons back to AW19.
- **Secondhand.** Vinted: 500+ results for "far afield", item cards labelled "Brand: Far Afield". Grailed: designer page "Far Afield", 67 listings.
- **Dials.** 38 rows in `dials.csv`. Copy was scanned by script across all 155 live pages and about ten were inspected by eye; photographs were not judged (so `logo` is a floor).

## What I could not reach

- **Vinted brand ID:** `NC`. The brand link is not in the page source without clicking through the filter.
- **B Corp:** `NC`. The directory's search is semantic and returned unrelated entries; none contained "afield" in the loaded text, but I could not exhaust the pages. The brand's own pages claim no B Corp status.
- **GOTS:** `NC`. The certifier's database URLs I tried were dead or unreachable. The brand says it uses "GOTS-certified organic cotton" and the Journal says its knitwear is knitted "using Global Organic Textile Standard certified organic cotton", which is a supplier claim, not a listing for Farafield. Needs a human look at the GOTS database for "Far Afield" and the Istanbul workshop.
- **`western` and `golffice` dials:** `NC`.
- **Care guides by fibre** (cotton, TENCEL, wool, linen) and the FAQ were not read.
- **Quote date.** The About page is undated, so `quote_date` is `NC`. A dated alternative, from the Journal (4 April 2025, house voice): "It's not about scale or speed - it's about doing things properly, and building something lasting."

## What contradicted the existing record

- Prices are USD on the US market, not pounds.
- The Stockists page lists UK, Japan, Europe, Canada, the US and Oceania. I found no Indonesian shop. Brooklyn is Alter, Toronto is MUDDY GEORGE, SYDNEY'S and UNCLE OTIS, and Ottawa is STOMPING GROUND.
- The Manufacturing page names five countries, not only the Istanbul workshop.
- The company was incorporated in 2012, but the brand says it was founded in 2016. The aggregator's contact address is a Newhaven business park, not the Brighton hometown.
- The feed holds 327 products but only 155 are live.

## What the brief got wrong or left open

- "Brand's own mark": the site title, About page and Journal all write **Far Afield**; the domain and store are `farafieldclothing.com`. Canonical key `Farafield` is not in `canonical_keys.txt` (reconcile reports 1 unmatched, as expected).
- `own_doors.csv` has no legal format for a sample store; I used `outlet` and labelled it.
- The size run is numeric (0 to 5, with XS to XXL beside it), which the `forg` dial's S/M/L language does not quite cover.
- **Signature product: `NONE`.** The brand calls the Station Jacket its "long-standing chore jacket" and the Zigger knit shirt "a staple silhouette, revisited each season", but nothing calls either its signature or best seller. Candidates for you to rule on.
- `scandi` (0), `denim` (1), `golf` (1) and `ski` (0) all rest on "none found"; the scale's floor is a judgement for you.

## Tabs

I worked in your Farafield tab and opened one extra tab for the Journal, Vinted, Grailed and the certifier sites. I'll close it.
