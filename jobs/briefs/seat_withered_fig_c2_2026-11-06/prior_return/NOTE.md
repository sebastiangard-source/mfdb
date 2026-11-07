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


## Gitman Vintage

**Status:** partial, read 6 Nov 2026. Seated as its own brand, "Gitman Vintage" (Sebastian's ruling). Nothing gathered for Gitman Bros. beyond the tie below. Not in canonical_keys.txt (expected).

**Tie to Gitman Bros.**
- The brand's own FAQ page metadata says "Gitman Vintage is a division of Gitman Bros." The lookbook page says it "is a division of Gitman Bros." too.
- Shared factory: the Gitman Vintage contact page gives the factory as 700 Freeman Street, Lafayette, TN 37083, and the FAQ says "Our shirt factory is located in Lafayette, TN and our wholesale showroom is located in New York City." HQ/showroom: 197 Grand St, #6S, New York NY. Email is mail@gitman.com.
- Ownership: Individualized Apparel Group (IAG) lists Gitman Bros. among its brands (IAG About page; Wikipedia says the same). IAG's About page also lists "Measure Up Shirt Makers, in Lafayette, Tennessee" as its Tennessee factory. The link from that plant to the Gitman address is inferred from the shared town, not stated by the brand. IAG's page still says Gitman Bros. "operates in Ashland", so it is out of date.
- Who runs it: no Gitman Vintage statement. Press (InsideHook, 10 June 2020) named Chris Olberding as Gitman Brothers president when the Ashland factory's closure was announced; Wikipedia says Ashland production ceased in 2020, moving to a sister Tennessee plant. Not re-verified for today.
- The jackets and Sack Suit are made at a "sister factory"/tailoring house in Rochester, NY (product pages; suit page says founded 1899). Not named further.
- Founding: about page says Max Gitman, Brooklyn shirt-maker, opened the Ashland Shirt & Pajama Company in Ashland, PA in 1932; contract shop until 1978 when Gitman Bros. was created; sons Alfred and Sheldon. Gitman Vintage "Launched in 2008" (About). The lookbook page says "Launched in 2009" - brand contradicts itself; filed 2008.

**Contradictions and flags**
- About says "all our production based in the USA". Two knits (Roll Neck Sweater, Rugby Shirt) say Made in Peru.
- Roll Neck Sweater page lists 70% alpaca / 30% merino in copy but 20% merino in the spec table.
- Prices: dress shirt $235 (Blue/White Oxford) to $320 (Green Canvas Oxford, Winter Madras, tweeds, cords). The $295 "Pinpoint Oxford Dress Shirt" is the only formal dress shirt. Collabs excluded (Girard $320-325, Nicholas Daley $325-350, AGES $425). Rugby Shirt $315 filed as polo by judgement. Sweater $335 is a roll neck. No tees, jeans, dress pants, shoes; Simple Jackets ($565-$840) are sport coats, so outerwear NONE. Many products show as sold out online; prices still displayed; no compare-at price found.
- USD confirmed on Blue Oxford ("$235 USD") and Green Canvas Oxford ("$320.00 USD"). No country selector found.
- Stockists: a list, not features. Page shows 60 entries (27 US, 3 Canada, 1 Mexico, 20 Europe, 9 Asia), 63 locations because Westerlind has four. Several regions carry "Show All" links; I could not expand them, so more may sit behind them. Streets and zips are not shown. "Of The Lion, Minneapolis, MI" is printed that way on the page. Withered Fig is listed (online). Beams and Ships are multi-store retailers, filed as independent from the page alone.
- No own doors found (0 US, 0 world); the ruling "no US door is not a reason to stop" applied.
- Vinted: brand id 6128480 for "Gitman Vintage"; a separate id exists for Gitman Bros., not gathered. Grailed lists items under designer "Gitman Bros. Vintage"; the designer page did not load, so the URL is NC.
- B Corp and GOTS: directories would not load, NC. Quote date and pronunciation NC. Lookbook is Spring / Summer 2026 while the site shows Autumn / Winter 2026; images not readable, so men's flag NC.
- Dials: 38 rows. Boat, sail, racquet, ski, golf are NC because lookbook imagery was unreadable. Tech proposal NC (scale not in the folder).
- Styles: composition read on 14 pages only (all stated, all natural); roll-ups NC. ~248 listings (121 + 112 + 15 across collections/all pp1-3) include ties, hats, add-ons.
- Out of scope noticed: Gitman Bros. has its own site (gitman.com) with a heritage page; its brand merges with Gitman Vintage on Grailed/Vinted listings, which may confuse resale counts.


## Viberg

**Scope.** Footwear and small leather goods only (Sebastian's ruling). Seven clothing garments are NONE. Shoes are priced from the loafer staple: Bristol, $1,275 on all nine colourways, basis `single`. Brand's own site, viberg.com (store selector reads United States, USD $). Not a sub-line or re-brand of anything in `canonical_keys.txt`; the name is new there. Mark as written: VIBERG (wordmark).

**Prices read, boots and shoes.** Entry shoe: 145 Oxford Cuoio Horsebutt $1,145. Top: Service Boot 2030 BCT in Shell Cordovan (Black, Color 8, Dark Cognac) $2,240. Loafer $1,275. Billfold (leather good) $1,200. Collab and preorder items (Outsider II preorder, Garmsville, ACL, Permanent Style) were not used for any price.

**Catalogue caveat.** collections/all gives 5 pages of 28 and page 6 is empty. Pages 3 and 4 repeat several URLs, so the distinct count is below 140. The filter also showed 107 out-of-stock listings that I could not see. The extremes ($1,145 and $2,240) should be treated as medium confidence. Reads were via WebFetch summaries, not a raw feed.

**Own doors.** One: the Viberg Flagship, 262 Mott Street, New York (phone and hours on the brand's stockists page; ZIP not given there; neighbourhood Nolita from the brief, not named by the brand). The stockists page is a plain text list, not features. 35 outlets listed (flagship plus 34 others, 37 city rows in stockists.csv). Stockists are labelled independent from list context only; I did not open their sites. Withered Fig (Vienna, VA) is on the list.

**Victoria factory.** The craftsmanship page says "Located in Victoria, BC, Canada - the Viberg workshop houses some of Canada's best shoemakers and craftspeople". The company is called third-generation family owned and operated. The brand pages never use the words "own", "factory" or "Viberg Boot Mfg", and I found no filing; owned facility is a brand claim by implication. Not read: Sharp Magazine 2016 factory tour, Montecristo 2019, Stitchdown Brett Viberg interview (all turned up in search).

**Brief contradictions.** The brief and Sebastian's note say Goodyear welt, Horween, Shinki, Rocky Mountain. Verified: Goodyear welt (Bristol, Hiker, Outsider II) and Stitchdown (145 Oxford; process page); Horween named in the journal (The Shell Collection) and Shinki in the journal (Service Boot Shinki Horsebutt). Rocky Mountain not found. No tannery is named on any of the 9 product pages read (Chromexcel is only a product-title label).

**Not checked (NC).** search_url and feed rate, lookbook contents, Vinted, Grailed (fetch failed), B Corp, GOTS, pronunciation, logo dial, golffice, bruv, sail. vibergnyc.com did not give address detail; the brand's stockists page did.

**Signature product.** None proposed: the Service Boot is "iconic" and "our foundation", never signature, standard or best seller.

**Out of scope but noticed.** Duplicate catalogue entries and mismatched titles (Engineer says Teacore Vacchetta Lucida and Horsebutt on one page; Bristol Black Kangaroo listed twice). Journal posts carry no dates. Heavy sold-out sizing (single width E) on most boots.


## The Rite Stuff (read 2026-11-06, WebFetch only, own site first)

**Brand and site.** the-rite-stuff.com, Shopify, men's reproduction workwear (1920s-40s American patterns) made in Japan. Not a sub-line or re-brand of any canonical key (no match in `canonical_keys.txt`, expected). Mark: footer "The Rite Stuff"; product titles use "{The Rite Stuff}", tags "rite stuff clothing".

**Store and currency.** Single storefront, no country or currency selector visible; login links carry `region_country=US`. USD confirmed by `og:price:currency` = USD on Daybreak (250), Loopwheel Tee (84), Railhead (208), Oilman (220), Titan (189), Icebreaker (249). Nothing converted. Search URL and `Shopify.currency.rate` not tested (the feed read through WebFetch returned only 5 products, so it was not trusted).

**Scope.** Whole catalogue treated as men's (a "women's" tag exists; no women's product seen). About 72 listings over 4 pages of /collections/all, mostly sold out; vintage/antique, belts, caps, bandanas, scarves, bags, pennant out of scope. 23 men's clothing styles counted (colourways collapsed), 22 with composition, all cotton-led (one 75/25 cotton/linen), no elastane stated. Per the brief's definition "current range" was taken as in stock, regular price, not a collab.

**Prices (full, USD).** Tee 84 (single). Dress shirt = work shirts, 208 Railhead to 249 Icebreaker flannel (range). Dress pants = chino/work pants, 220 Oilman to 289 Arkham Tweeduroy cord (range). Outerwear: Knockabout work jacket lists $0.00 and is sold out, so `np`. Shoes: one collab sneaker 230 (sold out); Sebastian to rule whether a collab counts. Polo, jeans, sweater: NONE (Titan is a sweatshirt; denim pants are sold-out collab or closeout). Sold-out older prices (Atlas 199/229, Heracles 225, Bulldog 240, Uncle Sam 210/220) are in the row note.

**Doors and stockists.** No own store, outlet, concession or pop-up. Stockists page is a LIST of 17 entries (16 distinct; Blue Owl Workshop appears twice): 8 US, 8 abroad (Spain, UK, Japan, Australia, Taiwan, South Korea, Indonesia, China). Streets and ZIPs are not published. Redcast, Those That Know and Withered Fig are online. Per Sebastian's ruling, retailer prices and copy were not used.

**Made where.** Japan on 22 of 23 style pages (Knockabout in meta description only). Named maker: John Lofgren & Co. on about 12 style pages ("made in Japan in collaboration with John Lofgren & Co."). Loopwheel tee fabric knit in Wakayama (own page). No mill named anywhere ("Japanese-milled"); no owned facility. Waterhead Mills (Lowell, MA) and Salant & Salant are historical references only. **Sendai** is not on the brand's product pages; it appears as a blog tag and in the Those That Know interview (retailer-hosted, press only). **Taipei**: press only (same interview: Bryan lived in Taiwan around 2013); not on the brand's own pages. Proposed craft 3.

**Founding.** Own statement: Bryan Shettig, "This is why I founded The Rite Stuff in 2017" (Who We Are, signed Owner). Place not stated on the page, so `founded_place` = NC.

**Not reached.** Vinted, Grailed, B Corp and GOTS directories (WebFetch client error / not tried): NC. Search URL, feed rate, quote date, pronunciation: NC. No lookbook page exists (FW26 blog post is an essay with 8 unlabelled photos). Care wording is absent on nearly all pages, so `fuss` is low confidence.

**Contradictions and oddities.** Titles disagree with URL slugs (Daybreak "11 oz." vs slug "10-oz"; several Deadstock tee slugs point at other designs); Knockabout shows $0.00; the /collections/outerwear listing holds only the two Titan sweatshirts, not the jacket; Uncle Sam chambray page says "organic cotton" 4.69 oz. Sale prices on Bantam, Pacemaker, Daybreak Navy, Heracles, Border Stripe etc. were ignored in favour of the struck-through regular prices. `proposed_tech` 1 assumes 1 = none; the brief gives no tech scale.

**Out of scope noticed.** Shipping Protection by Route add-on appears as a "product" in the feed; a loyalty and an affiliate programme page exist (not read).


## Railcar Fine Goods

**Status: partial.** Full price record, doors, craft and dials done from the brand's own pages (fetch tools only, read-only). Not a sub-line or re-brand; not in canonical_keys.txt (expected). Mark: "Railcar Fine Goods" / "Railcar" / "RFG" (collabs), no difference ruling needed.

**Scope.** Men's range = /collections/shop-mens and sub-collections (tees, tops, bottoms, jackets, shoes). railcarfinegoods.com also stocks Red Wing, Barbour, Brixton, Pendleton, Deus, Danner, Thorogood and more, so Railcar label only; stocked footwear excluded. USD confirmed on two pages ($198.00 USD Kurabo jeans, $425.00 USD wax jacket).

**Prices (regular, whole dollars).** Tees $36-40 (all graphic, no plain tee). Polo NONE. Dress shirt $138-328 (casual button shirts). Jeans $198-338 (Rebels Kurabo non-selvedge to Rebels X134 21 oz selvedge). 2014 press ~$258 MSRP does not match the live range. Dress pants = duck work trousers $198-248. Sweater NONE (the "Crew Neck Sweater" at $70 is a printed cotton sweatshirt). Outerwear pair $298 (Type 2 Kurabo) to $425 (Type 2 wax canvas). Shoes: only a Railcar X Whites 610 collab boot, $715 (made by Whites, Spokane): needs Sebastian's ruling. Sale prices ignored (Type 2 X105/X111/X130 at $338 not $238; Candiani items).

**Doors.** One US own door: 10636 Main St, El Monte CA 91731 (Down Town El Monte), a multi-brand shop that also carries Railcar. Former Monrovia store (2014-2020) recorded as closed. No stockist page or locator found: stockists.csv is NONE-style.

**Making.** Brand states all manufacturing is in-house at its El Monte workshop (about page). Ownership of the building/business is not stated by the brand; owned vs leased unknown (Apparel News 2020 doesn't say either). Denim mills named in product titles: Kurabo, Cone Mills, Candiani, Unshin. Proposed craft 4, 5 if in-house counts as owned.

**Origin.** Founded 2010 by Steven Dang (ex LA Metro mechanic) from his home; Arcadia 2011, Monrovia 2014, El Monte 2020 (brand's about page). The brief's "Tawny" appears only in a Withered Fig interview (May 2018): Tawny Ortiz, Dang's wife, runs bookkeeping/production; not on the brand's own pages.

**Quote** is press (Apparel News, 2020, Dang): "Quality is central. I know what goes into every garment". No suitable quote found on the brand's own pages. Second option: "I think I consider myself more as a maker rather than a designer" (Withered Fig, 2018-05-27).

**Not reached / NC.** Style census and fibre split (products.json returned nothing through the fetch tool; 9 styles read individually, most state no fibre); Grailed (fetch error); B Corp and GOTS directories (fetch error); Vinted brand id (5 listings under "Railcar Fine Goods" on search, no id visible); pronunciation; proposed tech; lookbook men's flag (Look Book page has ten unlabelled photos, no season label); FAQ page failed to load. Polo/sweater NONE rests on category pages and a fuzzy search, not a full crawl.

**Brief notes.** Collection grids loaded inconsistently through the fetch tool (some pages returned 0 tiles), so prices were taken from pages that did load and re-confirmed on 8 product pages. Chore Coat Candiani shows $235 regular vs $238 siblings: possible stale compare-at, not used. Signature product: NONE (no page calls anything its signature or best seller).
