# Seating note

## 3sixteen

**Identity.** One brand, 3sixteen.com (Shopify, US storefront, USD confirmed on Heavyweight Boxy T-shirt $60 and Country Jacket 3L $485 with the selector at "US-$ USD"). Not in `canonical_keys.txt` (no match expected). Brand writes its mark "3sixteen". No sub-line, re-brand or twin on the map.

**Scope.** 3sixteen labels nothing by gender. I scoped to the whole range: sizes are S-2X and jeans waists 28-40, the FW26 lookbook shows men, and I found no women's section. Not checked: whether any women's pieces sit inside the catalogue. Footwear included.

**Checked.** Collection JSON feeds read page by page (limit 8) for tees, shirts, denim, bottoms, knits, outerwear, footwear; 12 product pages (tee, jeans, Country Jacket, loafer, derby, Driver Knit, Knit Polo, Roll Neck, Big Oxford, Pleated Trouser, Hunting Jacket, Easy Pant); About, Stores, FAQ, Wash Guide, Measuring Guide, News index, FW26 lookbook, "The Future of Feet", NY reopening post. Foreknown facts verified: both stores and the stockists link are right.

**Prices (regular only).** Main-range items often carry sale prices with a compare-at (e.g. Cotton Crewneck Lapis Boucle 185 vs 245; Welding Jacket 410 vs 550); I used the compare-at. Two oddities: Work Pant ~ Black Twill and ~ Umber list price 245 against compare-at 240/245. Excluded: collaborations (Schott Drivers Jacket 1300, CDW down 798/625/550, Self Edge x Samurai, Saucony), vests, shorts, sweats, 2-packs (priced per pack, 98), gift cards. Sale collection not read. The fetch tool truncated the unpaged feed, so counts are from paged reads and are approximate. The fetch tool refused `?sort_by=` URLs as robots-disallowed, so I could not use price sorting to confirm lows and highs; they come from reading every page of each collection (outerwear 8 pages, denim 4, bottoms 5, knits 5, shirts 5, tees 3, footwear 3).
Garment judgements: no dress shirt (casual button-fronts, range 175-285), no dress trouser except the Pleated Trouser (range basis 220-330), only knit polos (both 245), no elevated crewneck pair (sweater range 245-330; baby-alpaca roll neck is 285), loafer is a single style at 495 (shoes category runs 240-550), jeans 250-310.

**Not reached (NC).** Full style census and fibre shares (a 27-style sample with compositions is in `return_styles.csv`; totals NC), swim share, tech (no named performance fabric seen; Active collection not opened), B Corp and GOTS (bcorporation.net and GOTS database fetches failed; a web search found nothing for the brand, which is not a directory check), pronunciation (no source), golffice and sail dials. Vinted and Grailed pages themselves returned client errors; the URLs and Vinted brand id 623847 come from search results and are unverified.

**Craft.** Proposed 3. No owned facility found; the brand names mills (Nihon Menpu, Kuroki, Albano Morgado) and the shoe maker (Sanders & Sanders, Northampton), and every page read states a place. Clothing factories are not named ("partner factory in Peru"). Press says outside factories make the jeans.

**Contradictions and gaps.** Founding: the brand's About page says only "Founded over two decades ago" and "modern history began in 2008" with no founders or place; the 2003 / New York City / Andrew Chen and Johan Lam facts come from press (The Hobbyist, 13 Mar 2025; Wikipedia), so the source is press. The Withered Fig interview (2017) says "nearly 15 years" and focus on denim from 2010, consistent with 2003. Wikipedia names Johan Lam as owner; the Hobbyist calls Johan only "partner". The brand states no ownership. The quote is Andrew Chen in The Hobbyist; the About page has no founder quote (its motto: "3sixteen: the last shall be first").

**Stockists.** The About page's Stockists section is a plain list of 56 entries grouped by region (28 US incl. 3 online, 5 Canada, 1 Mexico, 13 Europe, 6 Asia, 3 Australia/NZ), city only, no street or zip. Withered Fig (this commissioning shop) is on it. Self Edge, Iron Shop Provisions and Rivets are single entries covering several cities. Own doors: 2, no outlets, concessions or pop-ups; the NY shop hosts a private Stephen Kenn furniture showroom, not a concession. NY shop was renovated and reopened September 2026.

**Brief errors.** `dials_template.csv` is empty (0 bytes), so columns were taken from this instruction. `return_template.csv` holds 36 pre-filled other-brand rows under the header, not just a header. `mark_as_written` has no column in the full template, so the mark is in `note`. Style quantity in `schema_styles.json` (ND vs NC) works but `pure` for blends (silk/cotton tie) follows first-listed fibre only by my reading. BRIEF says do facts-first rows before full records; this assignment asked for the full record only, so no facts-first row was returned for 3sixteen.

**Out of scope noticed.** Home collection and a Stephen Kenn showroom; a Quoddy shoe collaboration (mentioned in press); "Sale" collection with many marked-down main-range items; the Hobbyist mentions Johan Lam running retail.


## Dehen 1920 (read 2026-11-06)

**Brand and key.** Not in canonical_keys.txt (expected). Owner of the name: Dehen Knitting Co., Portland OR. Not a sub-line or re-brand of a mapped house. "Dehen x Merz b. Schwanen": Merz b. Schwanen IS a mapped key; the Dehen pilot jacket is a collaboration and was not counted. "Dehen x Gitman" oxford is a collaboration with Gitman (Gitman Vintage is also in this batch); not counted.

**Scope.** Men's only, as ruled. Dehen sells women's too. The all-catalogue listing does not label gender, so scope = men's collection pages (/collections/jackets, /sweaters, /heavy-duty-tees, /overshirts) plus product copy, excluding anything titled "Women's" (about 12 on pages 5-6 and the overshirt page). Currency cell says so. No sale or compare-at price appeared anywhere.

**Checked.** All six pages of /collections/all (USD, "Page 1 of 6"; every price shown with "$" and "USD" on product pages; $68 tee and $1,395 N-1 confirm USD). Collections: jackets (31), sweaters (36), heavy-duty tees (page 1 of 2, 48), overshirts (24). 15 men's product pages for composition, made-in, mills, care and sizing. Factory, History, 1980-2010, Retail Store, Stockists, Size Chart, A/W 2025 lookbook pages. Heddels (press, 17 Dec 2020).

**Top price.** $1,395, N-1 Deck Jacket (4 colourways, waxed canvas shell, mouton lining). Next: All-City Leather Jacket $1,295. Brief's instruction to read all six pages was followed; see tool caveat below.

**Not reached / NC.** No style census (WebFetch only: no feed, no payload), so styles_total, fibre percentages, shape, spandex, colourway ratio are NC; return_styles.csv holds 15 hand-read sample styles only (method manual). Dress shirt NC (see row note: Lounge Shirt $260 collar unstated; Gitman collab $235). Tees collection page 2 of 2 not read. Accessories and Heavy Duty Cotton collections not read as lists. search_url and feed rate untested. Vinted and Grailed returned fetch errors: NC. B Corp / GOTS directories unreachable: NC. Pronunciation, signature product: NC (no brand page calling anything its signature seen; "Most Popular" collection not read). Store neighbourhood: brand names none; local guide not checked. Dial care (fuss) NC: no care lines on any of 15 pages. Lookbook men's/women's NC.

**Craft (key evidence).** "Made in Portland over 100 years" verified as the footer/copyright line ("DEHEN 1920 - MADE IN PORTLAND, ORE. USA FOR OVER 100 YEARS - COPYRIGHT 2026 DEHEN KNITTING CO."); 15 of 15 product pages read state Portland/USA. Owned-factory evidence is claim-level plus press: "knit by us on 1940's knitting machines" (moto-sweater page), trim "knit at Dehen factory" (leather jacket, N-1), history page's Flanders & 10th mill (1960-80), Heddels quoting the president on 1950s flatbed machines. No filing or site photo read; current factory address not stated by the brand. Third-party maker named: Columbia Knit (tees, rugby shirt). Named mills: Abraham Moon & Sons (UK), Halley Stevensons (Scotland). Proposed craft 4, confidence medium; Sebastian rules on 5.

**Contradictions / things that do not reconcile.**
1. Ownership: the brand says family-owned, "well into our fourth generation", no owner named; Heddels (2020) names Jim Artaiz (not a Dehen by name) as president and owner. Left unreconciled in owner_today.
2. Factory page says both that pressure to move manufacturing abroad existed and that goods are made in Portland; history page gives Flanders & 10th as the factory but the retail store is at 1040 NE 44th Ave. Whether the factory moved is unstated.
3. History page calls 2011 a launch of the Dehen 1920 line, not a revival. Quote used is the house's own, from that page, undated.
4. Tool caveat: WebFetch summarises pages with a small model. Its page 4 of /collections/all described itself as "page 4 of 7" and repeated page 3 items, so page 4 is unreliable; the top price was cross-checked against the jackets collection (N-1 4 x $1,395) and the leather jacket pages.
5. Stockists page spells "EDMINTON", "EDMUNDS", "EV AMHEM", "Wisconson": kept as listed with notes.

**Brief errors / observations.** return_template.csv has no band_guess (as you said); the facts-first template does. dials_template.csv is a zero-byte file, so dials.csv columns follow the instruction. The brief mentions "five properties" style Insider scoping nowhere for this job; no conflict. rules_craft.md references worklist current scores, which this batch does not carry.

**Stockists.** A list (84 names, 90 rows once multi-city entries are split; two online-only: Huckberry, Withered Fig). Brand gives name and city only, no street or zip. It names Railcar Fine Goods (El Monte CA), another brand in this batch. "DEHEN JAPAN / TOKYO" is listed as a stockist; unverified whether Dehen-owned, so not counted as an own door.

**Out of scope but noticed.** Dehen sells women's (separate nav, lookbook "Women's A/W 2024", women's cardigans $395 to $445 inconsistently across page 5 and 6 of the all-catalogue, a sign that listings change between reads). Accessories (hats, socks, scarves, watch caps) are out of the clothing count. Heddels says a retail store inside the factory was planned. Gift card links go to dehen1920.myshopify.com.
