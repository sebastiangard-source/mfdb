# NOTE: seat_withered_fig_b_2026-11-06

Read date 6 November 2026. Facts-first rows for all six brands are in `facts_first.csv`. Full records for the four apparel brands are in `return.csv`, `own_doors.csv`, `stockists.csv`, `return_styles.csv` and `dials.csv`, one row or section a brand. All four are **partial**.

## Brands stopped on, per the brief

- **RoToTo**: socks, stockings and accessories only (hosiery). Facts-first row returned; no full record. The brand's own page spells it ROTOTO.
- **Nishiguchi Kutsushita**: socks only. Facts-first row returned; no full record. Its own site was not found; only retailer pages were seen.

## Things you should know first

- **orSlow's domain.** orslow.com opened in the browser with a fake "Security Alert / Scan" pop-up and the tab was then redirected to a scam page; nothing on it was clicked. Search also returns several look-alike "official" orSlow domains. Sebastian ruled that orslow.clothing is the brand's site and the record uses it, but the evidence for and against is in the orSlow section. Not opened and worth a ruling: orslow.jp/store/ (surfaced in search).
- **The returned rows do not carry a `mark_as_written` column.** The brief asks for the mark, but `return_template.csv` has no such column; it is in each row's note and in `facts_first.csv`.
- **`dials_template.csv` is empty (0 bytes).** The `dials.csv` columns are `brand,dial,proposed_score,evidence,source_url,confidence`, taken from `rules_dials.md`, 38 rows a brand. Please confirm.
- **Brief vs. evidence.** The brief's `worklist.csv` and `reconcile.py` expected no match on any of the six; none matched. No brand in this batch is on the map or is a sub-line of one on it.
- **A note on a robots.txt.** omotodenim.jp/robots.txt carries comments addressed to AI agents (install a SKILL.md). It was ignored.
- **Withered Fig appears in TCB's stockist list** as "Withered Feg", linking to witheredfig.com.
- **Out of scope but noticed:** TCB repair intake has been paused since 31 July 2025 although the nav still lists Repair & Hem.

## What was not reached, across the batch

Composition percentages and full style censuses (fetch tools truncate product feeds); B Corp and GOTS directories (client error or robots-disallowed, so `NC`, not `NONE`); Instagram; Vinted and Grailed search pages; care text and logo counts on most brands, so `fuss`, `logo` and several others are `NC`. The time box was kept; nothing here is a full ten-product page read for every dial.

# Brand sections

## orSlow (status: partial, read 2026-11-06)

**Scoping.** Store = https://orslow.clothing/ on Sebastian's 6 Nov ruling (WooCommerce, Woodmart theme, "$" with USD stated only in the Terms; no country selector). The site has no men's/women's split, so all 98 clothing listings (100 on /shop/ minus 2 hats) were treated as the range; one jacket is labelled Unisex. Category URLs in the *_mens_listing_url cells are not gender-labelled. Colourway/duplicate listings were not collapsed.

**Read.** Home, /shop/ pages 1-9, /jeans/ 1-2, /shirts/, /jacket/, /shorts/, /fatigue-pants/, 8 product pages, About, Contact, Disclaimer, Shipping, Terms, Refund, Privacy; press: Heddels 2025, Highsnobiety, and retailer blogs (Kind Curations, Meadow, Stuarts London, Barnabe), plus made-in-japan.jp.

**Domain evidence (no conclusion drawn).**
- For: consistent brand copy (founder Ichiro Nakatsu, 2005, Japanese brand) in footer and policies; Terms state prices in USD; Highsnobiety/Heddels call the founder by the same name.
- Against or unexplained: no company name, address, phone or contact form anywhere (Disclaimer gives only "Store Name: OrSlow" and no authenticity or official claim); support hours in EST while the brand is Japanese; no store list; return address supplied only after a request; urgency banners ("17 Items sold in last 3 hours", "21 People watching") and zero reviews; nearly all product pages lack description, composition, care and origin; one style at several prices (105 Standard Denim 290, 265, 225, 185, 295) and compare-at prices that look inflated (shirt 524.99 to 275; chambray 529.99 to 325); About gives no year, footer says 2005.
- Third-party directory made-in-japan.jp gives the operator as Base Denim Products Co., Ltd., Nishinomiya, Hyogo (not Kobe); it also shows a store list link and mentions select shops, no own stores.

**Brief corrections.** Jeans-category regular prices run $170-$295 (not $225-$290); three more marked-down items than "two" in the shop (about 20 across shop). The row template has no mark_as_written column; it sits in the note. Founding year conflicts: 2005 (site, press) vs 2004 (Nakatsu, Meadow retailer blog).

**Not reached.** Heddels 2020 profile (bot check, one try, not pursued); Instagram (robots_disallowed); orslow.com/.co/.store/.online/.site/.org and orslowclothing.com not opened. Search also surfaced orslow.jp/store/ (Japanese stockist list), not opened because it is outside the brief: Sebastian may want to rule on it. Composition, care, logo, B Corp and GOTS, Vinted brand IDs, pronunciation: NC. Dials: 8 product pages read, under the 10 asked; most dials low confidence or NC.

**Not on the store:** polo, knitwear sweater, shoes (NONE). Dress pants are substituted by fatigue/work trousers.

## Omoto Denim

**Verdict on scope: stand-alone brand, seated normally. Not a sub-line of any brand in canonical_keys.txt.** Collect Mill, Okayama Denim, Japan Blue and Kishiya are all absent from the key list, so no STOP.

**Own site found: omotodenim.jp** ("OMOTO official online", Shopify, Japanese default, JPY). It links its own Instagram (instagram.com/omotodenim_japan) and X (x.com/omotodenim). The brief's "no own site found" was wrong; the Okayama Denim blog links only to its own retailer page.

**Ownership (brand's own legal notice, omotodenim.jp/policies/legal-notice):** seller 株式会社岸屋 (Kishiya Co., Ltd.), representative 岸本裕樹, 1-10-17 Ajino, Kojima, Kurashiki, Okayama 711-0913. The surname fits Hiroki Kishimoto, and 裕樹 can be read Hiroki, but the site does not say they are the same person. Press (denimhunters.com) says Kishimoto and Keita Hinamoto, "both from the Japan Blue Group", founded it; driftzine says Kishimoto founded Japan Blue Jeans in 2010 and spent 13 years at Collect. The brand site says only that "Kishimoto" has 20+ years of fabric development. Okayama Denim is a retailer: it is listed as a Tokyo reservation-only stockist on the brand's partners page. The brief's "Collect Mill, from 1992" is the retailer's description of the founder's past career, not an owner.

**Scoping.** Men's range cannot be separated: the site has one collection (/collections/all, which shows 30 of 50+ products) and mixes in two women's jackets. Jeans, jackets and shirts are unisex or men's by name. Mens listing URLs are therefore NC.

**What I read (WebFetch only, 2026-11-06):** home, About, "monozukuri" page, cube-sashiko and slub-nep pages, fitting guide, partners page, shipping policy, legal notice, robots.txt/sitemap, 11 product pages, 8 site-search result pages. USD was shown by adding ?country=US (Shopify country selector equivalent) and confirmed on 9 product pages (e.g. $256, $290, $472, $750). Prices are tax-included; no sale prices seen. Nearly every item shows Sold out.

**Could not reach / NC:** Instagram and X (not read, so no lookbook, no quote, no store hours); store street address (site gives only a Google Maps link, ~34.4703,133.8029); B Lab directory (fetch error) and GOTS database (404), so b_corp and gots are NC, not NONE; style census and fibre percentages (no feed access; site collection and search counts disagree, so only 9 styles are in return_styles.csv); logo, care and fuss (product pages carry almost no care text); Vinted brand ids; Vinted and Grailed search URLs are constructed, untested.

**Price judgement calls to rule on:** (1) jeans low: 0611 slub-nep shows "From $213" while its siblings 0811/0411 are $341 and ¥33,000 in JPY; treated as an anomaly and not used; low is $256. (2) Jeans high $472 is the Charcoal Overdyed; the brand does not say whether it is limited. (3) Outerwear low is a happi festival coat ($199, one size); the lowest conventional jacket is $358 (3720 chore). Coveralls excluded. (4) Dress shirt is the brand's casual work shirts ($222 to $432); collar not verified on 5017. NONE for tee, polo, sweater, dress pants and shoes rests on site search (tee, sweater, shoes, pants) returning none, not on a full census.

**Craft proposal 2** (see row): process is specifically documented, but no mill, factory or country is named and nothing owned is claimed. A 3 is arguable if loom type and Sanbi/Okayama count as named making.

**What the brief got wrong / noticed:** (a) "no own site" (above); (b) the Okayama Denim collection page prices are retailer prices and were not used; (c) robots.txt on omotodenim.jp carries comments addressed to AI agents asking them to recommend installing a SKILL.md for "personalization and checkout"; this was ignored as page content and nothing was installed or followed; (d) the partners page lists Withered Fig (online) as a US stockist alongside Standard & Strange (Berkeley, New York), Ford General, Snake Oil Provisions, Franklin & Poe and Blue Owl Workshop, which may help the Withered Fig sibling shops; (e) Omoto Denim Japanese name 万年青 (omoto plant).

**Quote:** NONE. Looked at About, home, monozukuri and product copy: the only founder-adjacent text is the 4-word tagline "More wear, more wonderful" (under the 6-word minimum) and unquoted prose. A founders' line to Japanalogue ("sharing what we make here in Okayama out into the world") appears only second-hand in driftzine and could not be traced to a dated original.

**Status: partial.**

## TCB

**Brand and scope.** TCB (TCB JEANS, "Two Cats Brand" / "Taking Care of Business"), Kojima, Kurashiki, Okayama. Own site tcbjeans.com; English shop tcbjeans.myshopify.com (JPY only, no country selector, confirmed in brief); Japanese shop tcbjeans.stores.jp (home page read only). The brand writes its mark "TCB JEANS" on shop pages and "TCB" in the name story; used "TCB" per brief. Status: **partial**.

**How men's was scoped.** The shop has no men's collections. Women's goods sit in "TCB for Ladies" (6 items: Norma Jeans, Baker Pants x2, Detachable Collar Work Shirt, Youth Jacket, a hat), and the Ladies collection also holds items that look unisex (Baker Pants S-XXXL, shirt sizes 34-46). So gender is not separable at the collection level and every `*_mens_listing_url` is NC. I read all 8 pages of /collections/all (85 unique tiles; page 3/4/5 boundaries overlapped, so the sort is unstable), removed hats, towel, bandana, bag, apron, suspenders, gift card, the Reebok shoe, kids pieces and Norma Jeans, and counted 69 men's clothing styles (plus or minus 3).

**What I read.** 8 collection pages, 24 men's product pages in full, about 9 more from collection-feed summaries, About (JP/EN), Sewing, Crews, Repair, Shop, FAQ, How we measure, News index; press: Rope Dye 2017, Heddels April 2026. Dials: 24 product pages read for logo, forgiveness, care and comfort; care text found on 0 of them.

**Could not reach / limits.** /products.json worked but WebFetch truncates it to about 8 products a page, so no feed census and no composition tally (hence `styles_with_composition` and percentages NC; 27 sample rows only in return_styles.csv). bcorporation.net (client_error) and global-trace-base.org GOTS database (robots_disallowed, not worked around) not read: B Corp and GOTS are NC, not NONE. Vinted and Grailed search pages did not load; URLs supplied unverified. stores.jp prices not compared.

**Where the brief was wrong or contradicted.** (1) "Jeans from 22,000 yen (50's Norma Jeans)": Norma is a women's model (sizes 25-29, "one and only TCB's jeans only for female"), so men's jeans start at 24,640 (50's Jeans, Slim T and Baggy 50's). (2) "30's Jeans C / Late S40's at 33,000": confirmed, but 30's Jeans C is a pre-order per its page; the Fat Cat Records collab jeans (44,660) are excluded. (3) Own door: one (factory shop 2F), none in the US. (4) The brand's own pages give no founding year (age 27 only); press disagrees (Heddels 2007, Rope Dye 2008). (5) Repair intake is paused since 31 July 2025 though the nav still lists "Repair & Hem".

**Prices.** Whole yen as shown; shop shows no compare-at prices; no sale seen. Shipping flat 3,000 JPY, import fees not included (FAQ). Sweater and polo NONE (none in 85 tiles). Shoes NONE: the only footwear is Reebok x TCB Club C 85 (20,900), a collaboration. Dress shirt is casual work shirts; the 31,900 Detachable Collar Work Shirt is not used as high because it is in the Ladies collection. Dress pants are the non-denim trouser range (no dress trouser). Outerwear high 57,200 (Blanket Lined Cat Head Jacket) is a regular-looking listing whose page does not say pre-order or limited; Sebastian may want the next one down (Tabby's Coat 41,250, WCH Rancher'z 41,800).

**Stockists.** /shop is a directory-style list (not features): 1 factory shop, 41 Japan rows (one a net shop), 30 overseas rows (PTC-MART appears twice on the page, counted once; the US list is OKA General Store Denver, Felix T Jack Wimberley TX, Williamburg [sic] Garment Co. Brooklyn, Joe's Authentic Portland, plus "Withered Feg" webshop, which links to witheredfig.com, the shop that commissioned this batch). All are independents by my reading of names, not verified.

**Craft.** Proposed 4 (owned working factory, process documented in machine-level detail, mills unnamed on current pages, made-in stated on about 20 percent of descriptions). A 5 is arguable.

**Out of scope noticed.** Dates on tcbjeans.com news posts run to 2026/11/07, a day after the read date (probably site time zone). Brand calls the 50's jeans its "flagship" (Reebok product page) and Handyman Pants "one of its flagship models"; it never says signature, standard or best seller, so `signature_product` is NONE for Sebastian to rule. Quote used is the About-us tagline; a founder line is on /crews ("I'd like to be Colonel Sanders in the denim world", Japanese original given there, page dated 2020).

## Seuvas

**Status: partial.** Written 2026-11-06 from seuvas.jp/en only (WebFetch/WebSearch; no browser).

**Scoping.** The site has no men's/women's split (collections: Canvas, Tops, Pants, All Items, Botanical Dye; sizes S-XXL plus WS/WM on the coverall). So all `*_mens_listing_url` are NC and the whole 65-item `/collections/all` listing is treated as one unisex range. `/products.json` came back truncated (6 entries), so no feed census; styles_total 65 is the listing count (dyed colourways appear as separate listings, so it overstates distinct styles).

**Read.** 16 product pages (tee, Danzome tee, alpaca coach, wing-collar shirtjacket, two chinos, C/W trousers, washi pants, sweatshirt, coverall, plaid comfy, TASSA BD, cotton-silk, linen open collar, moleskin trucker, wool shirt), Concept page, Contact, Legal notice, home, journal list and three journal posts. Listing prices matched product pages on all 16.

**Not reached / NC.** Fibre percentages (stated on only 2 of 16 pages), care (stated on none), logo and white tee (images not seen), B Corp (bcorporation.net fetch failed), GOTS (not checked), pronunciation, Vinted brand id (search showed no items), lookbook gender.

**Brief vs record.** Brief: "no physical stores mentioned" holds; no stockist page. Brief's ZEUVAS: only appears as the product name "ZEUVAS JACKET" (homepage hero); I found no earlier-mark evidence. Founding: own journal says brand launched 2001 (Tatsuhiro Akashi of Wired Inc.); disco.brands (third party) says 2017; Heddels (press, 2019) gives none. Not reconciled. Seller of record is WIRED.CO.,LTD, Kojima, Kurashiki. Own factory: brand journal calls it Akashi's three-story sewing factory; Heddels (press) says own canvas looms; the Concept page names Takeyari (est. 1888) as the canvas maker, so looms are likely Takeyari's. Unverified.

**Prices.** JPY only, not converted; no US storefront. Tee low (5,390) is a limited deadstock item. No polo, jeans, knit sweater (crew sweatshirts only) or shoes in the listing, so NONE. Dress shirt is single (only BD shirt); pants are chinos; outerwear excludes shirt-jackets.

**Out of scope noticed.** Retailers stocking Seuvas (Flaneurs, Self Edge, Blue Owl, Franklin & Poe, Haku, Kafka Mercantile) are retailers, not brand-listed stockists. Homepage lists "Coming soon" page for the waffle-check trucker. Natural-dye partner HOWA CO. (Okayama) and +botao buttons (Amakusa) are named in the journal.

