# seat_wave_b — batch 6 (True Classic through Vivienne Westwood) · 11 October 2026

This is the last batch of wave B. All 54 brands now have a full record.

## Files

- `return.csv`: 5 rows.
- `return_styles.csv`: 1,079 styles.
- `stockists.csv`: 5 rows.
- `return_counts.csv`: 3 brands.
- `own_doors.csv`: the running master, 1,293 rows.

All brand names match the canonical keys exactly, no cell is empty, and every store count equals its rows.

## Flags for merge

| Brand | Flag | Filed |
|---|---|---|
| True Classic | Each colour has its own handle | Counted by shared article number: 112 styles (about 657 by handle) |
| True Classic | Slippers as shoes | Shoes $20–30 range |
| True Classic | Target and Costco are its only named retailers | Summarised as chains; door counts `NC` |
| Turnbull & Asser | Bury St and Davies St London doors are by appointment only | Counted; world 4 (2 without them) |
| Turnbull & Asser | Marked-down "was" prices ($385, $425) sit below every full-price shirt | Dress-shirt low $455 |
| Turnbull & Asser | 190 made-to-measure fabric listings in the shirts menu | Out of the census, treated as a service |
| Vans | No regular polo and no crewneck sweater | Rugby shirts in the polo slot; knit polo and cardigan in the sweater slot. NONE is the alternative |
| Vans | 90's Big Block snowboard jacket | Regular range, outerwear high $250 (otherwise $130) |
| Veilance | Woven shirts are hidden-snap or camp-collar | Filed as casual wovens; NONE if button-front is required |
| Veilance | 48 US Arc'teryx stores may carry Veilance | Not counted; listed in its NOTE |
| Vivienne Westwood | Guam store | Counted in US own doors, on the Puerto Rico precedent (2 in the 50 states) |
| Vivienne Westwood | Pirate Boot presented as a reimagined 1981 design | Excluded as a reissue; shoe high $960 (otherwise $1,250) |
| Vivienne Westwood | Andreas Kronthaler runway line | Not sold in the US men's navigation, so excluded |

## Things found

- **Turnbull & Asser's** Gloucester shirt factory is evidenced by the brand's own pages, so craft is proposed at 4. The Fayed family are the controlling owners (UK register, 2026).
- **Vivienne Westwood:** Andreas Kronthaler is the only active significant owner on Companies House (25–50%). The "family/estate" description is unconfirmed.
- **Veilance** has no Veilance-banner door anywhere. Every product page names its third-party factory in China or Vietnam, so craft is proposed at 3.
- **Vans** has 569 VF-operated stores per VF's 10-K. That figure is mentioned here only.

---

# Per-brand notes


## True Classic: full record, wave B batch 6 (read 2026-10-11)

**What was checked.** I read the US store at trueclassictees.com. It runs on Shopify, prices in USD, `Shopify.currency.rate` is 1.0, and the country is US.
- **Feed:** I read `/products.json` pages 1 to 7. Page 7 returned zero records. That gave 1,310 products, of which 1,139 carry the `dep_mens` tag. The rest are women's, kids', gift cards and memberships.
- **Compositions:** they come from the feed `body_html`. I checked them against 10 rendered product pages and they matched.
- **Navigation:** the header menu links individual products and five "Shop All" parent collections. The grids are driven by Constructor.io, so the collection JSON is empty.
- **Other pages read:** about-us, our-story, fabrics, the Materials & Fabrics FAQ (which also holds the wholesale FAQ), and the pages sitemap.
- **Off-site:** Retail Brew (16 Jun 2022, interview with Ryan Bartlett), Business Wire (1 May 2025, 1686 Partners investment), Grailed, and a B Lab search.

**Section 4** was not re-read. The counts were carried over: 13 own doors in the US and 13 worldwide, with 0 outlets and 0 non-US. The locator is https://www.trueclassictees.com/pages/stores.

**Stockists and wholesale chains.** The brand lists no independent stockists. The only third-party retailers it names are:
- **Target:** the site has /pages/find-at-target and /pages/true-classic-shop-on-target.
- **Costco:** the site has /pages/true-classic-at-costco.

Both are national chains with far more than 5 US doors. Their door counts are `NC`, because the locator widget was skipped per the section 4 instruction. `/pages/wholesale` is a corporate bulk-order programme (48-piece minimum, resale prohibited), not a stockist list. stockists.csv has a single `NONE` row that says this.

**Fibre verdict.** 112 men's clothing styles, counted by YGroup article number, from 678 colour handles. The range is split by line:
- **Overall:** 47% natural-led, 36% synthetic-led, 17% cellulosic-led. All 112 styles state a composition. 64 contain elastane, and 40 of those are at 5% or more.
- **Wholly synthetic lines:** Active (25 styles, 22% of the range, polyester/spandex), Commuter (5) and Performance (3).
- **Wholly natural lines:** Fleece French Terry (9, 60/40 cotton/poly), Heavyweight (8) and Pima Cotton Blend (4, the only all-cotton tees). Note that "natural" here is mostly cotton-led 60/40 poly blends. Only Pima, Authentic Denim and Twill Chino are close to pure cotton.
- **Wholly cellulosic lines:** Dressy (polos and sweaters, 62% viscose) and Waffle (modal/cotton).
- **Mixed:** Tall (22 styles).
- **By category:** synthetic leads in Shirts (9 of 13) and Shorts (7 of 14). Natural leads in Tees & Polos (27 of 46), Fleece and Chinos.

**Prices.** All in USD. Regular prices are rounded from the $x.99 figures.

| Garment | Low | High | Basis |
|---|---|---|---|
| Tee | $35 (Classic Crew) | $45 (Pima Cotton Blend Crew) | pair |
| Polo | $40 | $50 (Dressy Polo) | range |
| Dress shirt | $60 (Oxford) | $65 (Performance Dress Shirt) | range |
| Jeans | $80 | $80 | range |
| Dress pants | $60 | $65 | range, chinos |
| Sweater | $50 | $65 | range |
| Outerwear | $60 (Puffer) | $100 (Coaches Jacket) | range |
| Shoes | $20 (Slippers) | $30 (Comfort Slides) | range |

- No garment in the range uses an elevated fibre.
- Packs are not prices.
- A site-wide "Fall Sale" ran on the read date, but the feed's single-item records carry regular prices.

**Craft and tech.**
- **Proposed craft is 1.** No owned facility, maker or mill is named. No country of origin is stated on any of the 1,139 men's records. No process is documented. The "very unique process with the fabrics" in the FAQ is a claim only.
- **Proposed tech is 2.** The fabrics page gives house names for ordinary blends (Classic Jersey, Active Jersey and others). There are UPF and quick-dry claims on Active. No licensed or owned technology is named.

**Mark as written.** `mark_as_written: TRUE CLASSIC`, from the logotype, as accepted on 10 Oct. Key kept.

**Not reached / NC.**
- **Vinted:** not read. Prior batches drew a 403.
- **Shoes listing URL:** there is no footwear category in the navigation.
- **Lookbook:** none found on the site or in the sitemap.

Status is `partial`.

## Flags for merge
- **Style method:** the YGroup tag is shared across colour handles and packs, so I counted by it. A literal handle count (the 11 Oct ruling, for when colours carry their own numbers) would give about 657 single handles. Please rule.
- **Two-tag records:** three groups carry two YGroup tags (4809;4827, 4810;4828, 4801;4819). Each is a "2.0" or length variant that has its own title, so I kept it as a separate style.
- **Glacier Gray Classic Polo:** it has no tag, so I merged it into 4002.
- **Underwear "W/ Fly" lines:** three are sold only in packs (2032, 2033, 2036). They are counted as styles. 2036 and 2032 may be the same boxer brief in an old and a 2025 version.
- **Suspicious composition:** Sandstone Slim Chino Pants 2.0 (4730) reads "99% Cotton / 5% Spandex", which sums to 104%. The straight version reads 95/5. Filed as read.
- **Empty navigation items:** "Swim Trunks", "Heavyweight Curved Hem Henley" and "Short Sleeve Active Mesh Crew" link to `/pages/pdp/...` pages. The swim page rendered no product, and none of the three is in the feed or site search. They may be pre-launch. Swim is counted as 0.
- **Shoes:** the only footwear is own-label slides ($30) and slippers ($20). Whether slippers count as shoes is for the Spectrum thread. The Timberland Pro collaboration boot ($170) is excluded.
- **Category assignment:** the Active Quarter Zip is filed under tees-polos. Active Joggers are filed under trousers and Fleece Joggers under sweats.
- **Natural-led tie:** outerwear (4 natural-led, 4 synthetic-led) and denim (2 natural-led, 2 cellulosic-led) tie. Neither is in the natural top three.

**Contradictions with the worklist or record.** The worklist reads "DTC tee house opening US stores". That is consistent with the carried 13 doors. The range is much wider than tees: it includes chinos, jeans, a blazer, jackets and dress shirts. Press (Retail Brew 2022) says the brand uses 10 contract plants in Egypt, Turkey, China and Bangladesh. This is a press figure and is not used as evidence.

**Out of scope but noticed.**
- A women's line of about 82 records and a kids' line of about 79 records.
- Socks, caps, belts, a leather backpack and sunglasses.
- A Spanish locale at `/es/`.
- A paid "Insiders Club" membership.


## Turnbull & Asser: full record, wave B (read 11 Oct 2026)

**What I checked:** turnbullandasser.com in Chrome. It is a Shopify US store (title "Turnbull & Asser US", USD, currency rate 1.0). I read:
- `/products.json`: 4,012 products over 17 pages. Page 18 returned 0 products.
- 31 navigation collections via `/collections/<handle>/products.json`
- 107 PDPs, one at a time about 3 s apart, with no blocks. I used them to validate the feed's `Material:` tags, read the 41 styles that have no tag, and sample `Country Of Origin`.
- /pages/stores, /newyork, /jermyn, /bury, about-us, understanding-our-shirts, about-sustainability, royal-warrant, the Off the Cuff blog index and the Menichetti interview
- off-site: turnbullandasser.co.uk/pages/our-people, the Companies House PSC register (01066321), The Manufacturer (2013) and Punchline Gloucester (2019), both on the factory
- I could not curl the site from the shell (the egress proxy refused it), so every read went through the browser.

**Section 4 (own doors): 1 US own door, 0 outlets, 0 concessions, 0 pop-ups, 3 non-US. own_doors_world = 4.**
- /pages/stores ("Find a Store") lists four stores.
- US: 50 East 57th Street, New York NY 10022 (the "New York Townhouse"). Lat 40.761728, lon -73.971446, taken from the brand's own map data in the page source.
- London: 71-72 Jermyn Street (the flagship), 23 Bury Street (Bespoke) and 4 Davies Street ("The Room", a craft concept; bespoke and ready to wear by appointment).
- The worklist claim "NYC store" is confirmed.

**Prices (USD, full price):**

| Garment | Basis | Low | High |
|---|---|---|---|
| Tee | range | $245 | $330 |
| Polo | range | $265 | $355 |
| Dress shirt | pair | $455 Light Blue Mayfair, cotton | $855 Navy Silk Chelsea |
| Jeans | single | $595 Navy Denim Trousers | $595 |
| Dress pants | range | $650 Jonathan, wool/linen | $1,275 Edward/Rupert, 95% wool 5% cashmere |
| Sweater | pair | $495 merino crew | $795 cashmere crew |
| Outerwear | range | $995 Albi Harrington | $4,455 Joseph cashmere overcoat |
| Shoes | NONE | | |

- That is 7 of 8 slots priced. Shoes are `NONE`: the 4,012-product feed has no footwear.
- James Bond (licensed) and Churchill pieces are excluded from prices.

**Fibre census:**
- 587 styles from 1,282 colourway handles. A style is the product code's model plus fabric; the third segment is the colourway.
- Composition stated on 586/587.
- Split: 99.1% natural, 0.7% synthetic, 0% cellulosic.
- 30 styles have elastane, 10 of them at 5% or more.
- Shape `one`.
- Shirts make up 353 styles (60%), and every one is natural-led (cotton, linen, silk, cotton-cashmere).
- The only synthetic-led styles are 4 quilted pieces (polyamide gilets, quilted blazer/jacket).
- Line verdicts, all all-natural: The Linen Collection (32), Sea Island Collection (13), Black Tie Collection (10), The James Bond Collection (8). No line of 5 or more is mixed.

**Stockists:** none listed (I filed one `none` row).

**Craft 4 / Tech 1 (proposed).**
- **Gloucester factory: evidence, not just a claim.** The brand names "our factory just outside of Gloucester" and "our Gloucester workrooms". Its our-people page names staff who have worked at the Gloucester factory since 1964 and shows workroom photos. Press places the factory at Quedgeley with about 100 staff (The Manufacturer, 22 Feb 2013). Punchline Gloucester (21 Oct 2019) reports the filings. The brand site gives no street address.
- **Why 4, not 5:** the PDPs state Italy for most tailoring, trousers, outerwear and knits (63 of 87 PDPs that give a country), and no mill is named.
- **Tech:** three licensed treatments (Storm System, Cordura, Basolan) appear on about 4 styles.

**Owner:**
- Fayed family. The Companies House PSC register lists James Allie Fayed and Liam Fayed, both notified in 2026, replacing a "no registrable person" statement that dated from 2016.
- Founders, as the brand gives them: John Arthur Turnbull and Ernest Asser, 1885. Wikipedia says "Reginald" Turnbull; the brand's version is filed.

**Quote:** Roberto Menichetti (Creative Director), from the brand's own journal (2026).

**mark_as_written:** Turnbull & Asser.

## Flags for merge
- **Two own doors are by appointment.** Bury Street (Bespoke department) and Davies Street "The Room" are by appointment. I counted them as own doors because the brand lists them as stores with their own addresses. Without them, world own doors = 2.
- **Shirts with compare-at prices below the range.** Two shirts carry compare-at prices of $385 and $425. Both are marked down and sold out, and both are below every full-price shirt ($455 and up), so I did not use them. If the compare-at rule is applied literally, the dress-shirt low would be $385.
- **Navy Davey Cotton T-Shirt.** It is $120, an older-season code, sold out in all sizes, and not in the t-shirts collection. I did not use it as the tee low.
- **Fairway Ash Grey Driving Jacket.** The feed tag says 79/16/5 cotton/polyamide/elastane, the PDP says 58/36/6. I filed the PDP. Henley blazer: the tag says 6% polyester, the PDP says 6% polyamide; I filed the PDP.
- **"100% wv".** The PDP for the Greenwich knitted overshirt says "100% wv" while the tag says 100% Wool, so I read it as wool.
- **"Bright Yellow Merino V-neck Jumper".** Its handle says "cashmere"; the composition is merino. Filed as merino.
- **Made-to-measure fabric listings.** 190 MTM fabric listings sit inside the see-all-shirts navigation. I excluded them as a service, not a style. If they were counted, the shirt count would rise sharply, all cotton.

Out of scope, noticed:
- The brand also makes ties in Sidcup, Kent.
- The sustainability page says some mills hold GOTS, RWS, European Flax and OEKO-TEX certifications. None is named, and the brand itself is not certified.


## Vans: full record, read 2026-10-11 (status partial: lookbook, B Corp, GOTS, Vinted id not reached)

**Mark as written:** VANS. This mark was accepted on 10 Oct. Page titles write "Vans®". The note carries `mark_as_written: VANS`.

## Access
- vans.com runs the same VF Nuxt front end as Timberland.
- It served all 8 pages of the men's clothing listing and all 243 product pages without a challenge.
- I moved between pages by navigation only, one product page about every 5 seconds, and used no `fetch()`.
- I hit no PerimeterX block.

## Prices (sections 1–2), USD, list prices
- **Tee:** $30–40 (pair: New Left Chest vs Premium Loose Fit).
- **Polo:** $70–90, collared rugby knits.
  - Vans has no short-sleeve pique polo outside the Vans X Rowan collaboration.
- **Dress shirt:** $60–70 (range). Casual woven button-ups are all Vans makes.
- **Jeans:** $70–90, Check-5 denim.
- **Dress pants:** $65–80, Authentic Chino. There is no dress trouser.
- **Sweater:** $70–98 (range: Feldman Polo Sweater to Harmon Cardigan). There is no crewneck pullover sweater.
- **Outerwear:** $70–250, from the Torrey Coaches Jacket to the 90's Big Block 2L snowboard jacket.
- **Shoes:** $85–120 (pair: Skate Loafer vs Premium Harris Tweed Loafer 53).
- **Excluded from prices:** collaborations (Vans X Atiba, Rowan, Travis Barker, Odyssey; OTW by Vans X Julian Klincewicz and TDC); licensed music tees (Black Sabbath, Sex Pistols, Queens of the Stone Age, De La Soul); Waffle Shop pieces.
- **Listing links:**
  - The men's nav has only four clothing nodes: Hoodies & Jackets, Shirts, Pants, Shorts. Tees, polos and shirts therefore share the Shirts parent.
  - Sweater uses the men's clothing parent.
  - The men's clothing listing also carries a handful of unisex styles under women's breadcrumbs (Ronnie track set, Drill Chore, Range Cargo shorts, OTW field pants, Waffle Shop).

## Fibre (section 3): census complete on the men's clothing navigation
- **Coverage:** 369 colourway tiles collapse to 243 styles (8-character style stem). 153 of the 243 (63%) state a composition in the PDP Details list.
  - The 90 that state none are mostly graphic tees (67 of the 129 tees and tops).
- **Split:** 52% natural, 10% synthetic, 0% cellulosic (1 viscose camp shirt), of all 243 styles.
- **Stretch:** 11 styles carry elastane. 4 have 5% or more, all swim.
- **Shape:** `one`. No category of ten or more styles is synthetic-led once swim is set aside.
  - Outerwear is close: 6 natural-led vs 5 synthetic-led of 11 disclosed.
  - Knitwear (2 styles) is synthetic-led.
- **Line verdicts (lines of 5+ styles):**
  - All-natural (on disclosed styles): Premium (9 of 9), Check-5 (8 of 8), OTW by Vans (5 of 5), Skate by Atiba Jefferson (5 of 5), the Vans X collaborations (14 of 14), Stretch Logo (4 of 10 disclosed).
  - Mixed: Authentic Chino (4 natural, 4 recycled-polyester-led; 6 of 8 carry 2% elastane).
- **Flagged composition:** OTW X Julian Klincewicz Collared Fleece is "100% French terry cotton blend". I filed it as read (cotton 100) and flagged it.

## Doors (section 4)
- Carried as given: 299 own doors and 99 outlets (US); world NC.
- I did not re-read the locator.
- VF's FY2026 10-K cites "569 VF-operated stores" for Vans. That is a filing, so it is noted here only and is not a door source.

## Stockists (section 5)
- One `none` row. locations.vans.com has a single store-type filter ("Vans Store"), and no stockist or dealer page was found.
- No dealer chains are listed by Vans, so there is nothing to summarise. The 10-K mentions "specialty, chain stores" without names.

## Sections 6–13
- **Owner:** VF Corporation (10-K for the fiscal year ended 28 March 2026). Vans is the largest brand in the Active segment.
- **Craft: proposed 2.**
  - Heritage is dated and placed: Van Doren Rubber Company, Anaheim, 16 March 1966.
  - Making: VF sources from about 216 independent contractor factories and owns no plants.
  - Product pages: 0 of 243 name a maker or mill, or state a country.
- **Tech: proposed 2.** Vans owns footwear technologies (WaffleCup, PopCush, Duracap) and uses licensed GORE-TEX on shoes. Men's clothing names no fabric technology, only generic DWR and 2-layer snow shells.
- **Quote:** Paul Van Doren, on vfc.com/brands/vans.
- **Signature product:** the Old Skool (1977).
- **Grailed:** 14.7k listings.
- **Vinted:** the URL is a keyword search; the brand id was not found.
- **Not reached:** lookbook, B Corp, GOTS.

## Flags for merge
- **Polo slot = rugby shirts.** Vans makes no regular-range short-sleeve polo. File `range` on rugbies, or `NONE`?
- **Sweater slot:** the only items are a knit polo sweater (composition not stated) and a nylon/polyester cardigan. There is no crewneck pullover. File the range, or `NONE`?
- **Outerwear high:** the $250 "90's Big Block Hooded 2L Snowboarding Jacket" is a regular snow piece. I read "90's" as a design name, not a reissue. If it is ruled a reissue, the next high is $130 (Hillgate Hooded Puffer / Nico Cropped Chore Canvas Jacket).
- **Lawson Solid Oxford Long Sleeve Shirt:** its byline calls it an "overshirt", but its bullets describe a button-up shirt. It is not used as a price.
- **OTW by Vans:** the sub-line sells five-pocket and field trousers at $150–170 in the men's listing. It counts under the sub-line rule but sits outside the chino slot. A dress-pants high of $150–170 would be possible if those count.
- **Waffle Shop:** these are upcycled secondhand garments with Vans archive graphics, and the pages say composition "may vary". They are in the census as undisclosed and out of prices.
- **Licensed music tees** are in the census, out of prices.


## Veilance: full record, wave B batch 6 (read 2026-10-11)

**Scope.** I read Veilance pages only. `veilance.com` redirects to `arcteryx.com/us/en/lp/veilance`, so the US Veilance store is the Veilance collection on arcteryx.com.
- The census comes from the men's Veilance category, `arcteryx.com/us/en/c/mens/veilance`. Its listing API (`/api/catalog.getProductListingPage`, slug `mens/veilance`) returns 70 items, with `totalCount` 70 and `hasMore` false.
- Every PDP carries `collection: veilance` and the breadcrumb Veilance > Men's.
- Composition, factory and origin come from each PDP's Next.js data route, read one at a time at 1.6 s spacing (70 PDPs, no blocks).
- No Arc'teryx mainline product was read or counted.

**Section 4 (own doors): positive zero, `0` US, `0` world.**
- Arc'teryx's "Find a store" page embeds a Locally locator (company_id 31).
- I read its `conversion_data` feed in-page at a whole-map radius: 2,778 markers in 37 countries (US 920). None has "Veilance" in its name, address or any other field.
- The locator's Store Type filter offers only Brand Store and Factory Outlet. There is no Veilance type.
- `worklist_conflict: NYC store`. The accepted correction stands: the SoHo Veilance store was a 2016 concept and is not on the locator.
- `own_doors.csv` is header only.

**Arc'teryx-banner US stores that may carry Veilance.** These are not Veilance doors and are not counted. There are 48 Arc'teryx-named US markers; the locator does not say which stock Veilance (a UPC query for a Veilance style returned 0 stocking stores).
- **New York, NY:** Flatiron (149 5th Ave), Upper West Side (158 Columbus Ave), Brookfield Place (250 Vesey St), SoHo (580 Broadway), Rockefeller Center (600 5th Ave)
- **Other New York state:** Manhasset; Woodbury Outlet (Central Valley)
- **New Jersey:** Garden State Plaza (Paramus), Short Hills
- **Massachusetts:** Newbury (Boston), MarketStreet Lynnfield, Chestnut Hill, Wrentham Village Premium Outlets
- **Washington, DC:** DC CityCenter, Georgetown
- **Maryland and Virginia:** Westfield Montgomery (Bethesda), Tysons Corner
- **Illinois:** Chicago Rush Street, Chicago Southport, Oakbrook Center, Old Orchard (Skokie), Fashion Outlets at Rosemont
- **Minnesota:** Mall of America, Southdale Center (Edina)
- **Colorado:** Denver Cherry Creek, Denver RiNo, Boulder Downtown, Aspen, Castle Rock Outlet
- **Utah:** City Creek Center (Salt Lake City), Park City, Arc'teryx Salomon Ogden Outlet
- **California:**
  - Los Angeles area: Old Pasadena, Los Angeles La Brea, Los Angeles Brentwood, Venice Abbot Kinney, Fashion Island (Newport Beach)
  - Bay Area: Stanford Center (Palo Alto), Burlingame Ave, Valley Fair (Santa Clara)
  - Outlets: Desert Hills Premium Outlets (Cabazon), San Francisco Premium Outlets (Livermore)
- **Oregon:** Portland 23rd Avenue, Washington Square (Portland), Woodburn Premium Outlets
- **Washington:** Seattle Pike St, Seattle Premium Outlets (Tulalip)
- **Nevada:** Las Vegas North Premium Outlets

**Stockists.** None filed. Veilance publishes no stockist list. The only locator is Arc'teryx's, and its 920 US markers are Arc'teryx dealers and stores with no Veilance tag. That list belongs to the parent, so I wrote one `none` row.

**Prices (USD, full price; no markdowns on any of the 67).**

| Garment | Low | High | Basis |
|---|---|---|---|
| Tee | $150 | $250 | range |
| Polo | $200 | $300 | range |
| Dress shirt | $250 | $400 | range |
| Jeans | NONE | NONE | |
| Dress pants | $350 | $500 | pair |
| Sweater | $300 | $350 | range |
| Outerwear | $450 | $2,200 | range |
| Shoes | NONE | NONE | |

- **Dress shirt:** the shirts are casual snap-front or camp-collar wovens (see Flags).
- **Dress pants:** Voronoi Pant (nylon) and Voronoi Wool Pant.
- **Sweater:** Conic Wool Midlayer and Conic Wool Half Zip Neck. No crewneck is named.
- **Outerwear:** the Sorin Down Parka is the high.
- `search_url` is NC because the site search rendered no tiles.

**Fibre verdict.** The census is 67 men's clothing styles, all with a stated composition.
- **Synthetic-led overall:** 18% natural, 81% synthetic, 1% cellulosic (paper yarn). Shape is `split`.
- **Elastane:** 27 styles carry elastane; 21 of those have 5% or more.
- **Only Fleece leads natural:** the two Conic knits, 55% wool. Shell Jackets, Insulated Jackets, Shirts and Tops, Pants and Shorts all lead synthetic.
- **Wool:** all 12 wool-led styles are wool blends (54–87% wool). No style is 100% natural.
- **Lines with 5 or more styles are all-synthetic:** GORE-TEX (14), Burly (7), Spere (7), Diode (6), TerraTex (6) and MX (6). 10 styles sit in no named line.

**Craft and tech.** I propose craft **3** and tech **5**.
- **Craft:** every PDP names its factory, all third-party plants in China or Vietnam, each with a partner page. No mill is named, there is no owned facility, and Veilance's own pages carry no dated history.
- **Tech:** 41 of 67 styles name a technical fabric or insulation. 14 are GORE-TEX, which is licensed and counted as tech.

**Ownership.** Amer Sports, Inc. (Form 20-F FY2025), through Arc'teryx. The part of the 20-F I read does not mention Veilance.

**Mark as written.** `mark_as_written: VEILANCE`. The logotype and headings are in capitals; product copy writes "Veilance".

**Not reached or unverified.**
- **Quote:** the Kasuga quote was read through a page-fetch summariser. Check it verbatim before it is used.
- **Founding:** the 2009 launch and Errolson Hugh's role come from press (Hypebeast 2019), not the brand's own pages.
- **Signature product and pronunciation:** NC.
- **B Corp and GOTS:** not checked against the directories.
- **Grailed:** the URL came from search results and was not opened.

## Flags for merge
1. **Dress shirt slot.** Veilance's woven collared shirts close with hidden snaps (Field LS/SS, Demlo SS) or have a camp collar (Cusec). None is clearly button-front. I filed them as casual wovens, because they are all the brand makes. The standing rules do not cover snap-fronts; if a button-front is required, the slot becomes NONE.
2. **Two names reused under separate article numbers:** Voronoi Wool Jacket (X000011088 FW26, X000009959 FW25) and Diode Insulated Jacket (X000010948 FW26, X000009108 FW24). Both are counted as two styles each, by article number.
3. **Older seasons still in navigation.** Several styles date to S23 or FW23 (e.g. Sorin Down Parka, the Frame and Dromos tops). They are counted because they are in the site's navigation at full price.
4. **Categories assigned by garment:**
   - Three softshell blazers (house label Shell Jackets) are in `tailoring`.
   - The Conic knits (house label Fleece) are in `knitwear`.
   - Demlo Hoody appears under both Shirts and Tops and Jackets; I counted it once, as outerwear.
5. **Composition anomalies filed as read:**
   - Voronoi Wool Pant and Monitor Coat name a facility in China but state "Origin of Manufacture: VIETNAM".
   - Five PDPs have no origin-of-manufacture line.

Out of scope but noticed: Arc'teryx's PDPs name the maker on every product. That is a parent-wide practice, worth checking when the Arc'teryx key is re-read.


## Vivienne Westwood: full record, wave B batch 6 (read 2026-10-11)

**What I checked.** I read `viviennewestwood.com/en-us/`, the US store (Salesforce Commerce Cloud, `Sites-viviennewestwood-na-Site`, USD), in Chrome. The worklist domain typo (`viennewestwood.com`) was already corrected in the prompt.

I read the following:
- the store locator's full data model and the four US-flag store pages
- the men's Clothing listing: 84 tiles, which matches the stated "84 Items"
- all 70 clothing PDPs: the Composition accordion, JSON-LD, and the details bullets
- the men's Shoes listing: 13 items, plus four shoe PDPs
- the sustainability and craftsmanship pages
- the Companies House PSC register for company 02682271
- Grailed, Vinted and the B Corp directory

I hit no blocks. I declined optional cookies ("Continue without accepting").

**Section 4 (own doors).** The locator embeds all 109 stores worldwide. "Load 0 More" confirms there are no more pages, and the en-gb locator returns the same 109, so the list is global rather than scoped to the US site.

| US door | Format | Note |
|---|---|---|
| New York, 14 E. 55th St | own-door | Flagship. This is the worklist's "NYC store", confirmed. |
| Los Angeles, 8320 Melrose Ave | own-door | Flagship |
| Tumon, Guam (The Plaza Shopping Center) | own-door | US territory. Kept like the PR rows. |
| Belmont, NY (2501 Hempstead Tpke) | outlet | The locator itself names it "Outlet". It gives no lat/lon, so those are NC. |

- **Counts:** `us_own_doors` 3, or 2 in the 50 states; `us_outlets` 1.
- **`world_non_us` 105.** The locator has no format field, so I filed `own_doors_world` as NC.
  - Reading the store names alone, roughly 48 are boutiques, 12 outlets, 38 department-store or mall counters (Korea, Japan, Taiwan), 6 travel-retail doors and 1 pop-up.
  - Store names are not a reliable format field.

**Stockists.** None. The locator lists only the house's own doors, and the US site has no stockist or wholesale list. I wrote one `none` row.

**Prices (USD, full price; no sale flags on any tile).**

| Garment | Low | High | Basis |
|---|---|---|---|
| Tee | $240 | $410 | range |
| Polo | $280 | $460 | range |
| Dress shirt | $375 | $820 | range |
| Jeans | $685 | $820 | range |
| Dress pants | $830 | $1,620 | range |
| Sweater | $540 | $555 | pair |
| Outerwear | $830 | $1,800 | range |
| Shoes | $375 | $960 | range |

- **Dress shirt:** the low is the Krall shirt and the high is the Chaos Shirt in wool tartan.
- **Sweater:** the entry crewneck is already 90/10 wool-cashmere. The high is the dearest jumper whose page states a crew neck; no majority-cashmere crew exists.
- **Shoes:** there is no loafer, so this is a range. I excluded the Pirate Boot ($1,250) from the high because its page presents it as the AW1981 "Pirate" design reimagined. The high is the Parachute Boot.

**Andreas Kronthaler for Vivienne Westwood.** I treated it as the runway line and excluded it.
- It is not sold as a line in the US men's navigation. A site search for "kronthaler" returns no products, and AKVW appears only on catwalk, lookbook and bridal pages.
- Two mainline pieces cite AKVW shows in their copy (Checkmate Jumper, Francis Monk Shoe). I kept both in the census as regular range. Neither is a high.

**Fibre verdict.** I counted 70 styles by article number: model plus fabric code, with colour as the suffix (84 colour tiles / 70). Composition is stated on all 70.
- **Natural-led overall:** 91% natural, 9% cellulosic, 0% synthetic-led. Shape is `one`.
- **Elastane:** on 6 styles; 5% or more on 2 (viscose jerseys).
- **Categories:**
  - Knitwear (13), outerwear (4), denim (2) and sweats (3) are wholly natural-led.
  - Tees (3 of 24), shirts (1 of 10), trousers (1 of 9) and tailoring (1 of 5) each carry one to three viscose-led styles.
- **Lines:** the only named line in the men's navigation is Worlds End, at 3 styles, all natural.

**Craft and tech.** I propose craft **3** (low to medium confidence) and tech **1**.
- **Owned facility:** none named. The supply-chain page describes in-house sourcing management since 2019 and audited external suppliers (10 direct, 31 sub-suppliers in 2025).
- **Named mills:** Lochcarron of Scotland and Harris Tweed are named on brand pages, not on PDPs.
- **Made-in:** "Made in Italy" appears on 32 of 70 PDPs.
- **Heritage:** dated and placed: 1971, 430 King's Road.

**Ownership.** The prompt said "private (Westwood family/estate)". That is only partly verified.
- **Private: yes.** Vivienne Westwood Limited is UK company 02682271.
- **Andreas Kronthaler:** the only active person with significant control, holding 25–50% of shares and votes.
- **Vivienne Westwood:** her 25–50% entry ceased on 29 Dec 2022.
- The register does not say who holds the rest (estate, heirs or others). I did not attribute it.

**Mark as written.** `mark_as_written: Vivienne Westwood`

**Not reached.**
- **Vinted:** a generic "Items" page, so NC.
- **Lookbook men's content:** the AW26/27 lookbook is a video, so NC.

## Flags for merge
1. **Guam.** I counted the Tumon store as a US own door (3 rather than 2), on the PR precedent. The en-us locator codes it GU and the en-gb locator codes it US.
2. **Pirate Boot.** I excluded it as a reissue: an AW1981 design that is still in the regular range. If the thread rules it regular range, the shoes high becomes $1,250.
3. **Unisex styles.** 15 styles in the men's Clothing navigation are filed under women's or Worlds End categories. They are counted in the census per the navigation rule.
4. **Belmont outlet address.** The locator writes the city as "New York" with "Belmont" as address2; ZIP 11003 is Elmont, Nassau County. I filed it as listed.
5. **World formats.** The 105 non-US rows include many department-store counters. A format split would need a per-store read; it is not inferred here.

Out of scope but noticed: the locator includes the London "AKVW & Bridal – 6 Davies Street" store, and Worlds End pieces are made from leftover production fabrics.
