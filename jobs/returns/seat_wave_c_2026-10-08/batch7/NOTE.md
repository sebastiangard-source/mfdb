# Wave C full records: batch 7 of 9, 13 October 2026

Brands (worklist rows 61–70): Private White V.C., Puma, Quoddy, Rancourt & Co., Represent, RVCA, Samuelsohn, Spier & Mackay, Stan Ray, Studio Nicholson.

Files:
- `return.csv`: 10 rows, 132 columns, no empty cells.
- `return_styles.csv`: 1,495 style rows (9 houses; Rancourt sells no clothing). Puma's rows are a sample.
- `own_doors.csv`: 139 rows (Puma 113).
- `stockists.csv`: 244 rows (Samuelsohn 235).

Reconcile is clean on all four files (10 names: 10 exact, 0 to rewrite, 0 unmatched). The style table passes `schema_styles.json`. Every site was read in Chrome on 13 October. As in batches 5 and 6, price cells are whole units, and exact figures are in `note`.

## What was read
- **Shopify, US market, USD:** Private White V.C., Quoddy, Rancourt & Co., Represent ("Official US Store"), RVCA, Stan Ray (global store, US market) and Studio Nicholson. Full `/products.json` feeds; composition from the description or each product page.
- **Samuelsohn:** a headless Shopify storefront ("US and Canada"). Every full-price product page was read; prices are USD (`currencyCode USD`).
- **Spier & Mackay:** a custom storefront showing USD to a US visitor. Collection pages show at most 40 cards, so all sub-collections were read too (1,441 cards), then each style's product page for composition.
- **Puma:** large house. The men's clothing listing gives the full count (637 products). The style table is a sample: the first page of each men's clothing category (91 rows after collaborations are removed). It is not proportional.
- **Prices are list prices.** Represent, Stan Ray, RVCA and parts of Studio Nicholson were heavily marked down on 13 Oct; where a product shows a compare-at price, that list price is filed.
- **Prices were not re-read separately** after the feed reads (all picks come from the same-day feeds and pages).

## Exclusions you should know about
- **Collaborations:**
  - Private White V.C.: Permanent Style (vendor "Permanent Style"), PWVC x Schofield's Bar, and the Royal Hospital Chelsea (RHC) pieces.
  - Represent: Belstaff, PUMA, Guns N' Roses, Metallica, Oasis, Iron Maiden, Beach Boys, Viper Room, Mels Diner, and NFL and MLB team pieces.
  - RVCA: Tapout, RVCA X Clay, RVCA X Dani Miller.
  - Puma: every "PUMA x" item (Street Fighter, Le Père, HYROX, Saysky, LaMelo Ball, Arnold Palmer, Aston Martin, Schomburg).
  - Stan Ray: Karhu x Stan Ray (its only shoe). Studio Nicholson: SN x Perfumer H.
- **Studio Nicholson "OFFLINE" products:** 91 men's products carry vendor "OFFLINE" (tag NOT-AVAILABLE-ONLINE-STORE). Left out; the count is what is sold online.
- **Samuelsohn Factory Direct:** the outlet collection is left out; 33 full-price products in 21 styles.
- **Puma licensed lines:** Ferrari, BMW, McLaren, Porsche and club and national football kit stay in the sample but are not taken as price highs. See ruling item 3.
- **Footwear** is priced but kept out of the style table (Represent, Studio Nicholson, Spier & Mackay, Puma).

## Prices: things to know
- **Private White V.C.:** all knitwear is cashmere (720–865), so the sweater cell is a range. Outerwear runs to the Shadow Parka (Ventile) at 2,900.
- **Spier & Mackay polo pair:** cotton pique Classic Polo 55 against a 55% silk / 45% linen knit polo 115. No cashmere crewneck, so the sweater high is a cashmere shawl cardigan (598), filed as `range`.
- **Studio Nicholson sweater pair:** Arda Knit (cotton) 420 against Haddan Knit (100% cashmere) 850.
- **Represent outerwear high:** Cowhide Trucker Jacket, 1,930 (list; 965 on sale).
- **Samuelsohn** sells tailoring only: suits 1,695–1,995 and blazers 1,295–1,495 (not a slot). Only dress trousers are priced (395–450); the other slots are NONE.
- **Quoddy:** one clothing product, a branded tee "Stitched In Maine" (39.99). See ruling item 4.
- **Rancourt:** shoes only, 228 (Dirigo Camp-Moc) to 748 (shell cordovan Bartlett Oxford). An alligator penny loafer at 3,000 (sold out) is not taken.
- **Spier & Mackay shoes** were read from listing cards; the URLs are the shoe listing.

## Fibre: the headline per house
- **Samuelsohn:** 100% natural (all wool).
- **Private White V.C.:** 98% natural.
- **Spier & Mackay:** 90% natural.
- **Studio Nicholson:** 86% natural.
- **Stan Ray:** 66% natural (130 of 178 styles state a composition).
- **Represent:** split, 59% natural / 22% synthetic. The 247 performance line is synthetic-led.
- **RVCA:** split, 57% natural / 21% synthetic. Shorts and outerwear are synthetic-led; swim is 11% of the range.
- **Puma (sample):** 44% natural / 56% synthetic.
- **Quoddy:** the tee states no composition (NC).

## Doors
- **Puma: 3 US own doors + 110 outlets.** The locator lists 113 US locations (110 in the states, 3 in Puerto Rico), all rowed. Store codes split them: 3 "usrf" (retail flagship: 609 Fifth Avenue NYC, Las Vegas Strip, Miami Dadeland) and 110 "usro" (retail outlet). Street text comes from the store-page URL. World total not looked for.
- **Represent: 1 US / 5 world.** Los Angeles (461 North Robertson Blvd), London (Wardour Street), Manchester (New Cathedral Street). The retail page also lists "247 Bondi" and "South Africa"; not opened, flagged.
- **Studio Nicholson: 0 US / 8 world.** 3 London, Tokyo Aoyama and Shibuya Parco, Kyoto, Beijing, Shanghai. Harrods and four Seoul department stores are concessions, not counted.
- **Samuelsohn: 1 US (flagged) / 1 world.** "Samuelsohn Custom NYC", 501 Madison Avenue, Suite 204, is on the brand locator under the brand's name. The Toronto store is an outlet ("Premium Outlet Store"); a Montreal outlet is named only.
- **Private White V.C.: 0 US / 1 world.** The flagship at the front of its own Salford factory.
- **Spier & Mackay: 0 US / 1 world.** Heartland Town Centre showroom, Mississauga.
- **Stan Ray: 0.** Rancourt & Co.: 0 (factory for ruling, as before).
- **Quoddy and RVCA: NC.** Quoddy's store pages render empty; RVCA's site has no store page.

## Stockists rowed
- **Samuelsohn:** 235 US stockists from the brand locator, with addresses and the label each carries (Samuelsohn, Heritage Gold, or both). Nordstrom and Neiman Marcus doors are marked department store.
- **Not read (NC):** Represent, Stan Ray and Quoddy (client-side finders), Private White V.C., RVCA, Studio Nicholson (no list). Puma's third-party retail not rowed (large house).
- **NONE:** Rancourt & Co. and Spier & Mackay.

## Sections 6–13
- **Craft proposals:**
  - Private White V.C. 5: own Manchester factory, nothing outsourced, makers named.
  - Rancourt & Co. 5: all footwear made in its own Lewiston factory, handsewn.
  - Quoddy 4: own Lewiston workshop, but in-stock shoes are also made elsewhere.
  - Samuelsohn 3, Spier & Mackay 3, Stan Ray 3.
  - Studio Nicholson 2. Represent 1, RVCA 1, Puma 1.
- **Named mills:** Samuelsohn (Reda, Carlo Barbera); Spier & Mackay (Reda, Hardy Minnis, Zignone, Marling & Evans and about 30 on its showroom page); RVCA (Cone Denim in jeans).
- **Founding:**
  - Private White V.C.: 1853, the house's date for the Manchester factory. See ruling item 6.
  - Samuelsohn 1923, Lesser Samuelsohn.
  - Stan Ray 1972, Crockett, Texas, Earl Beard; still run by his family.
  - Rancourt & Co. 2009, Lewiston, Michael and Kyle Rancourt.
  - Studio Nicholson 2010, Nick Wakeman; menswear from 2017.
  - Represent 2011, Manchester, George and Mike Heaton.
  - Quoddy: owners Kirsten and Kevin Shorey; no year read. Puma, RVCA and Spier & Mackay: not looked for.
- **Owner stated:** RVCA's footer is "Boardriders IP Holdings, LLC"; Stan Ray, the Beard family; Quoddy, the Shoreys.
- **Vinted:** no brand entry for Quoddy, Rancourt, Samuelsohn or Spier & Mackay.

## What contradicted the record
- **Quoddy "own store"** (worklist): no store found; only the Lewiston workshop on the contact page.
- **RVCA "own stores"** (worklist): the site carries no store page.
- **Samuelsohn "no own store"** (worklist): the brand locator lists "Samuelsohn Custom NYC" at 501 Madison Avenue.
- **Represent "LA store":** confirmed, plus London and Manchester.

## For ruling
1. **Puma's doors.** 3 flagship-coded stores counted as own doors; the 110 outlet-coded stores (3 in Puerto Rico) counted as outlets by store code. Confirm, and say whether Puerto Rico counts as US.
2. **Puma's sample.** The style table is the first page of each men's clothing category (91 rows), against a full count of 637. Confirm this is enough, as for Muji and Lands' End.
3. **Licensed lines at Puma.** Team and motorsport replicas are kept in the style table but not taken as price highs (an authentic Dortmund jersey is 160). Should they be excluded entirely, as Onward Reserve's licensed lines were?
4. **Quoddy's tee.** Its only clothing is a branded tee. Is that clothing (1 style, tee 39.99) or merch (NO_STYLES, tee NONE)?
5. **Samuelsohn Custom NYC.** A suite at 501 Madison Avenue under the brand's name, on the brand's locator. Own door, or a showroom not to be counted?
6. **Private White V.C.'s founding year.** The house dates the factory to 1853; the brand is named after Jack White V.C., owner from 1937. File 1853, or hold for a brand date?
7. **Represent's "247 Bondi" and "South Africa".** Counted in the world total (5) without being opened. Count, or hold until read?
8. **Studio Nicholson's Asian stores.** Five stores in Japan and China are counted as own doors with operators not stated. Confirm, or treat as operator-run (flagged)?
9. **Studio Nicholson "OFFLINE" products.** 91 men's products not sold online are left out of the style count. Confirm.
10. **Quoddy and RVCA doors.** Both NC: Quoddy's finder renders empty, RVCA has no store page. Leave NC, or carry a count from elsewhere?
11. **Spier & Mackay style count.** Each card is a colourway; 279 styles come from stripping colour and cloth words from card names, so the count is approximate. Accept, or count by card (1,233)?
