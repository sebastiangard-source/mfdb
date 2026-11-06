# Seating note

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
