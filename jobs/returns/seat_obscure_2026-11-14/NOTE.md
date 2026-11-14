# NOTE: seat_obscure_2026-11-14, early return (identification + US presence, all four brands)

Censuses, prices, dials, craft, quotes and resale are NOT done yet. Held for Sebastian's call on which brands are worth the full read. Men's range only; no women's items recorded.

## Haikure
- Official site haikure.com (Shopify). About page: Italian denim brand established 2011, women and men; parent company C&S Srl, a manufacturer for luxury/contemporary brands since 1981 (brand's own words). Contact: office@haikure.it, +39 075 9302037; seller PEC csjeans@pec.it. Founder and founding place NOT stated on the pages read.
- Men's collections: /collections/man-all, man-denim, man-top-jackets, man-leather. Default currency EUR.
- US: no locator, no stockist page, no own stores found. Site's country list offers United States in USD; terms say non-EU orders are DDP. Retailer pages for Nordstrom and Nordstrom Rack list the brand (seen in search results, not opened). Bergdorf, Bloomingdale's, Neiman Marcus come from the 10 Oct register and are not re-verified.
- Not settled: shipping price to US (needs checkout; not touched).
- **Agent instructions found**: haikure.com/robots.txt carries a block addressed to AI agents (points to /agents.md, a UCP/MCP endpoint, and asks agents to recommend that the user install a SKILL.md from shop.com). Not followed. I did not open agents.md or the endpoints.

## Nicole Farhi
- Official site nicolefarhi.com (Shopify, GBP). About page: label launched London 1983 under her name; "returns under owner Maxine Hargreaves Adams, her daughter April, and creative director Richard Biedul"; smaller modular collections for women and men, shared dressing. This is a relaunch, so the old French Connection ownership note is out of date (not checked how/when it changed hands).
- The site shows one line only: "for him / for her / shared". No Farhi by Nicole Farhi diffusion line found on the site pages read. Still open whether it exists elsewhere.
- Men's collection (/collections/for-him) returns 30 products, e.g. wool oversized crombie GBP 1,200, cotton trench GBP 795.
- US: delivery page lists UK plus Zone 1-3 (EU, Norway, Switzerland) only, GBP 20-40, minimum order GBP 150, customer pays duties. US not listed. No stores or stockists page. The 1999 East 60th St flagship is not checked. US presence = unknown.

## Caleb Paris
- Official site calebparis.com (Shopify). Brand page (French): designer brand founded "three years ago" by two cousins, Aaron and Samuel; genderless. Publisher per mentions legales: SAS UMAN, 47 rue Spontini, Paris 16. Founding year/place not stated precisely; Paris implied.
- Own stores: Paris flagship (72 rue Vieille du Temple) and Saint-Tropez (57 rue Gambetta). None in the US.
- Prices shown in USD to my session (e.g. fluffy polo $284, sherpa jacket $622); free delivery over EUR 200. Genderless: men's scope needs care when the census is done.
- US stockists and US shipping terms not yet found.
- A newsletter pop-up appeared; I did not interact with it.

## Fairdim: FOUND (see full read below)
Supersedes the earlier NOT FOUND: Sebastian confirmed fairdim.com (UK store, GBP, ships to the US in USD).

## Tooling notes
- The browser tool blocks some JS output with "Cookie/query string data" when the text contains URLs with query strings. Worked around by stripping them.
- canonical_keys.txt already lists all four brands, so reconcile.py reports 4 exact; the brief says they are not on the map.

---

# Update: Haikure full read (batch 1, brand 1 of 2)

Added: `return.csv`, `return_styles.csv`, `dials.csv`, `facts_first.csv`. All read 2026-11-14 in the browser (Shopify feeds on haikure.com). No cart, sign-in or form touched (one Vinted brand filter ticked to read the brand id; that only changes the URL).

**Range.** 185 products in the feed. Style codes split them: 141 women's (HEW), 12 men's (HEM), 1 HEU (Nelson check 99 shirt, unisex or unassigned code), 31 uncoded, all checked by title and all women's. The men's census is 13 styles, all current; the `man-all` collection also shows 12. The `carry-over`, `denim`, `tops-jackets` collections are mixed and mostly women's; no extra HEM codes in them. Women's items are not in any file.
**Fibre.** 12 of 13 state a composition: 10 cotton-led, 1 wool, 1 leather, 1 at 98% cotton/2% rayon. Bethany jeans says "Composition: 100%" with no fibre (ND). Zero synthetics, zero elastane on a main fabric line, one named line (none). Shape one cloth story; denim is 7 of 13.
**Prices (EUR as read, tax included, none converted).** Jeans 283 to 320; dress shirts (casual shirts only) 349 to 391; sweater 499 (one knit); outerwear 429 (denim jacket) to 840 (leather jacket). No tees, polos, dress pants or shoes (`NONE`). Sweatpants and a sweatshirt are in the census but not a priced garment. The sold-out Nelson check shirt shows EUR 313.60 against compare-at EUR 392; I used neither as the shirt range. Band is yours to apply.
**Craft.** Italy on 13 of 13 pages; no factory, mill or process named. Parent C&S Srl is called a manufacturer since 1981 but nothing ties it to this range. Proposed craft 2, would rise to 3 or 4 if C&S is shown to make it.
**Tech.** None found on 13 PDPs.
**Dials.** 38 rows, all scored. Most low or medium confidence: a 13-style range gives thin evidence. Weakest: logo (visible marks not counted page by page), forg (size charts not read).
**Not done / open.** Lookbook, B Corp, GOTS, signature product, pronunciation, own_doors_world are `NC`. Founder and founding city are not stated on the site. Vinted men's URL is built from brand id 266456 (category filter untested). Nordstrom listing opened: "Haikure, 26 items", first tiles women's; whether it stocks any men's is unchecked.
**Contradicts the record.** Women's register said "prices up to ~$1,000 at one retailer": the men's top at the brand's own shop is EUR 840 (leather jacket).
**Quote.** The homepage line in `return.csv` is the brand's own text, 22 words.

---

# Update: full reads for Fairdim, Nicole Farhi, Caleb Paris (batch 1, brands 2 to 4)

Currency labels: Haikure EUR, tax included (you apply ex-VAT). Nicole Farhi GBP, VAT-inclusive. Fairdim USD as shown on the US storefront (no VAT stated). Caleb Paris USD as shown (VAT/duty basis unclear). Nothing converted.

## Fairdim (fairdim.com)
**Census.** 229 products: 20 accessories and 1 gift card excluded; 208 clothing products collapse to 146 styles (no style codes on the site, so title with colour words removed; 20 titles hand-set where handle and title disagreed). Composition: natural-led 62 percent, synthetic 25 percent. Lines: FAIRDIM x DUPU 35 styles, Archive Series 9, Linen collection 5 (mixed, not all linen).
**Prices (USD, full/compare-at).** Tee 81 to 149; polo 189 to 216; shirt 176 to 378; jeans 216 to 378; pants 162 to 378; sweater 189 to 324; outerwear 216 to 1,159; shoes NONE. Compare-at was not cross-checked on a second product.
**US presence.** No own doors; ships to the US in USD from the UK store. No stockists found.
**Resale.** Vinted no brand; Grailed no designer page.
**Open.** Owner, founder, founding year and place NC (no About page). Tech, craft, lookbook, B Corp, GOTS NC or NONE as marked in return.csv.

## Nicole Farhi
**Census.** Whole site is 40 products; 30 in "for him", but 27 of those are also tagged shared and 28 also in "for her". Counted as men's where the brand puts them in the men's collection (21 clothing products, 14 styles; only the pleated trouser and un-structured blazer are men's-only). No composition percentages anywhere: named fibre counts as 100 percent, blends without shares give lead ND.
**Prices (GBP, VAT-inclusive).** Shirts 295 to 450; pants 495 to 595; sweater 395 to 475; outerwear 550 to 1,200; tee, polo, jeans, shoes NONE.
**Ownership.** Maxine Hargreaves Adams per the brand About page; press says bought from administration July 2013. Founded 1983; menswear 1989.
**US presence.** No US own doors. Old East 60th Street flagship checked: see us_presence.csv. Search for US retailers: see us_presence.csv and stockists notes.
**Resale.** Vinted id 87200 (85 results, all genders), Grailed 58 listings (all genders); men's category filter untested.

## Caleb Paris (calebparis.com)
**Key finding: the brand is genderless.** No men's collection exists (collections are by garment type), and no title, fit or description says men's or women's (0 hits in 129 product pages). Under your rule, men's-only styles = 0, so return_styles.csv has no Caleb rows. The unisex census is separate: caleb_paris_unisex_styles.csv, 87 clothing styles (117 products; 7 shoes and 5 accessories excluded): 60 natural-led, 17 synthetic-led, 7 cellulosic-led, 3 ND; 9 with elastane, none at 5 percent or more.
**Prices (USD as displayed, unisex range).** Tee 170 to 298; polo 284 to 379; shirt 257 to 508; jeans 393 to 487; pants 433 to 568; sweater 352 to 474; outerwear 433 to 1,623 (leather jacket; dearest non-leather is 947); shoes 453 to 602. Displayed USD is about 1.354 x the feed EUR, which hints at VAT or duties inside the price, but the site does not say. Treat as unverified.
**Ownership.** SAS UMAN, 47 rue Spontini, Paris (mentions legales). Founded "three years ago" by cousins Aaron and Samuel; no date or place stated.
**Doors.** Paris flagship and Saint-Tropez only (own_doors.csv); US own doors 0. No stockists found.
**Resale.** Vinted: no Caleb Paris brand; Grailed: no designer page.
**Quote.** French, from the brand page: "CALEB tire son nom d'un explorateur connu pour sa détermination et son instinct inébranlable."
**NC.** Made-in, B Corp, GOTS, pronunciation, size-guide detail.

## Across all four: what remains NC
Lookbook for Haikure/Farhi/Fairdim, B Corp and GOTS, pronunciation, founders for Haikure and Fairdim, shipping prices.
**Nordstrom check.** Haikure's Nordstrom and Nordstrom Rack pages list women's items only; no men's found.
