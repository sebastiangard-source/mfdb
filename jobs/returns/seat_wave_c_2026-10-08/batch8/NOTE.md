# Wave C full records: batch 8 of 9, 13 October 2026

Brands (worklist rows 71–80): Tellason, Ten Thousand, UGG, Undefeated, Undercover, Universal Works, Velva Sheen, Y-3, Zadig & Voltaire, Zara.

Files:
- `return.csv`: 10 rows, 132 columns, no empty cells.
- `return_styles.csv`: 1,245 style rows from 9 houses. Y-3 was not read. Zara's rows are a sample. UGG's rows have names only.
- `own_doors.csv`: 241 rows. 157 of them are carried from the 10 Oct counts job: Zara 102, UGG 48, Universal Works 7.
- `stockists.csv`: 48 rows. Velva Sheen has 26 and Undercover 14.

Checks:
- Reconcile is clean on all four files (10 names: 10 exact, 0 to rewrite, 0 unmatched).
- The style table passes `schema_styles.json`.

Every site was read in Chrome on 13 October. Price cells are whole units, with exact figures in `note`. The brand key stays "Zadig & Voltaire", as in the worklist. The mark is written Zadig&Voltaire in `note` and in the door rows' `banner_stated`.

## What was read
- **Shopify, USD:**
  - Ten Thousand, Undefeated and Velva Sheen: full `/products.json`.
  - Universal Works: the US market (`/en-us`, USD presentment at a 1.3522 rate from GBP).
- **Tellason:** a BigCommerce store. The all-products listing has 123 products. Every clothing product page was read for cloth, mill and country.
- **Undercover:** the Japanese store, in JPY, with tax-inclusive list prices (`size_proper`). It tells a US visitor that items "cannot be purchased from your area". Prices are not converted, per ruling. I read the men's all-item listing (213 item codes) and every item page.
- **Zadig & Voltaire:** the US site. Men's view-all has 122 products, read from the page's JSON-LD, plus every product page for composition. The store locator's US city and store pages give 51 locations.
- **Zara (large house):**
  - The men's all-products category feed returned 1,000 listing entries, which are colour-level. That is 639 products, 494 of them clothing. The feed looks capped at 1,000, so 494 is a floor (ruling item 4).
  - The style table is a sample: up to the first 8 entries per clothing family, giving 71 rows. It is not proportional.
  - Composition comes from each sampled product's detail call.
- **UGG (large house):**
  - The men's apparel listing shows 83 tiles on one page. That is 38 clothing styles, all rowed with name and URL.
  - After the listing, ugg.com served a bot check ("Verification Required", a slide puzzle). I did not try to get past it.
  - So UGG has no prices and no composition. Its tee, trousers, sweater, outerwear and shoe cells are NC, with the block named.
- **Y-3:** not read. adidas.com was not retried, per ruling, and www.y-3.com does not resolve. Only the Vinted and Grailed ids are filled.
- **Prices are list prices.** Universal Works has 390 ARCHIVE products (older seasons on sale). Their compare-at list price is filed. Undefeated's one marked-down piece (Stencil Crewneck, 77 against 110) is filed at list.

## Exclusions you should know about
- **Collaborations:**
  - Undercover: Gramicci & nonnative, Dickies, Champion, Twin Peaks, fragment, New Era, Medicom Toy, Vans, Guidi, George Cox, OOFOS and Kijima Takayuki.
  - Undefeated: every "X" piece and the UND X CLC collegiate licensed range.
  - Universal Works: Paraboot, Topologie, Taion and Zardus "for Universal Works".
  - Zadig & Voltaire: Lucien Pellat-Finet.
  - Zara: Aaron Levine X Zara.
  - Tellason: Valsport (its only shoe) and Barnes & Moore (belt).
  - UGG: Willy Chavarria.
  - Ten Thousand: the Aaron Levine capsule.
- **Other brands sold on the store:**
  - Undefeated: only vendor UNDEFEATED clothing counts (106 styles of 1,315 products).
  - Universal Works: F/CE, cableami, Novesta, Paraboot, Mikia and others are out.
- **Undercover's Cindy Sherman pieces:** 26 AW26 mainline styles carry Cindy Sherman artwork, credited "courtesy the artist and Hauser & Wirth". They are kept in the style table but not taken as the outerwear high. See ruling item 6.
- **Licensed lines at Zara:** Ford, Ayrton Senna and Fruit of the Loom pieces are kept in the sample but not taken as highs. This follows Puma.

## Style counts: how a style was drawn
- **Universal Works:** 610 styles from 984 products. A style is the house style code (SKU prefix), which is model × cloth with colours joined. Grouping by model alone would give about 270, but the model names are not clean.
- **Tellason:** 82 styles. Each fit-and-cloth product is a style; jeans come in four or five denims. Colour-only products of one model are joined.
- **Zadig & Voltaire:** 90 styles. Style code is the SKU without its 3-digit colour code.
- **Undercover:** 125 styles by item code.
- **Velva Sheen:** 72 styles, from 379 colour products joined by title.

## Prices: things to know
- **Undercover (JPY):**
  - Tee: 12,400–55,800.
  - Knit polo: 83,700.
  - Outerwear high: 356,500 (silk down track jacket). The Cindy Sherman Loro Piana cashmere track jacket is 465,000.
  - Shoe: the Shepherd UNDERCOVER sneaker, 68,200. It is the only own shoe.
- **Zara sweater pair:** a viscose-blend basic sweater at 49.90 against a 100% cashmere jumper at 179. The outerwear high is a suede jacket, 359.
- **Universal Works:**
  - The sweater cell is a range. The cheapest full-price knit is already majority alpaca (55%): Lyon Crew 251, up to a David Cardigan at 460.
  - There are no five-pocket jeans. Denim trousers stand in, 212–337.
- **Zadig & Voltaire:** the cheapest knit (328) is a cashmere sweater, so the sweater cell is a range up to 898 (cashmere). Shoes: a single sneaker at 358.
- **Tellason:**
  - Core selvedge jeans are 275 in every fit and weight; the Tellason Stock line is 149.
  - Outerwear runs to the Drizzler waxed jacket, 499 (Halley Stevensons cloth, made in Italy).
- **Velva Sheen:** tees and sweats only. Tee 60–180; the high is a brushed thermal henley, made in Japan. Every other slot is NONE.
- **Ten Thousand and Undefeated:** no polo, dress shirt or own shoe. Casual and training pants stand in for dress pants.

## Fibre: the headline per house
- **Zadig & Voltaire:** 97% natural; cashmere-heavy knitwear and leather jackets.
- **Universal Works:** 89% natural.
- **Tellason:** 84% natural (71 of 82 state a composition).
- **Undercover:** 84% natural.
- **Undefeated:** split, 77% natural / 19% synthetic. Outerwear and shorts are synthetic-led.
- **Zara (sample):** 65% natural / 25% synthetic. Trousers are synthetic-led.
- **Ten Thousand:** split, 20% natural / 51% synthetic. 14 of 51 styles state no composition.
- **Velva Sheen:** only 21 of 72 styles give percentages. 29 name cotton ("US Cotton") without figures and 22 state no fibre; all 51 are ND, with a note saying which.
- **UGG:** NC (not read).

## Doors
- **Zara:** 102 US, carried from the counts job and rowed.
- **UGG:** 10 own + 36 outlets + 1 concession, carried and rowed. The counts job's Williamsburg "coming soon" row is also carried; it is not counted.
- **Universal Works:** 0 US / 6 world, carried. That is 3 UK stores and 3 operator-run Partnership Stores (Lyon, Toulouse, Berlin), flagged. The Tokyo shop in Hankyu Men's is a concession.
- **Zadig & Voltaire:** 51 US locations, all rowed:
  - 20 own doors.
  - 13 outlets: 11 named "Outlet" in outlet centres, plus 515 Archive and Tribeca Archive, which are outlets by ruling.
  - 18 Bloomingdale's shops, counted as concessions.
  - World total not counted.
- **Undefeated: 8 US / 13 world.**
  - US: seven UNDEFEATED shops (Los Angeles ×2, Santa Monica, Glendale, Las Vegas, Phoenix, New York) and "UACTP #001" in Los Angeles, the sub-line's shop (flagged).
  - Abroad: Tokyo, Osaka, Shanghai ×2 and Guangzhou. Operators are not stated (flagged).
- **Undercover: 0 US / 9 world.**
  - Own doors: Aoyama Mens, Aoyama Womens (women's-only, flagged), Sendai, Nagoya, Kyoto, Noise Lab Shibuya PARCO, Shinsaibashi PARCO, Repulse Bay (Hong Kong) and Taipei. Operators of the last two are not stated (flagged).
  - Seven department-store shops are concessions: Isetan ×2, Hankyu ×3, Iwataya and The Hyundai Seoul.
- **Tellason and Ten Thousand: 0 (low confidence).** Neither site publishes a store page.
- **Velva Sheen: 0.** The where-to-buy page lists stockists only.
- **Y-3: NC.**

## Stockists rowed
- **Velva Sheen:** 26 US stockists from the where-to-buy page; 15 more abroad are not rowed. The page's handle is "where-to-buy-test", but it is linked in the site footer.
- **Undercover:** 14 US stockists from its stockist page, including Dover Street Market LA and NY, Maxfield, Kith and five Nordstroms. Women's-only accounts are marked.
- **Not read (NC):** Tellason (no list), Ten Thousand (wholesale form only), UGG (large house), Universal Works, Zadig & Voltaire (own locator only) and Y-3. Undefeated is a retailer and publishes no stockists.
- **NONE:** Zara.

## Sections 6–13
- **Craft proposals:**
  - Tellason 3: cut and sewn in San Francisco from named mills (Kaihara, Cone Mills White Oak). Other pants and jackets are made in Italy. No owned facility, no maker named.
  - Undercover 2, Universal Works 2, Velva Sheen 2.
  - Ten Thousand 1, Undefeated 1, Zadig & Voltaire 1, Zara 1, UGG 1 (default).
  - Y-3 NC.
- **Named mills:**
  - Tellason: Kaihara, Cone Mills, Halley Stevensons, Kindermann.
  - Undercover: Thomas Mason, Loro Piana.
  - Universal Works: Kaihara and Harris Tweed, in titles.
- **Founding:**
  - Velva Sheen 1932, Cincinnati.
  - Undercover 1990, Jun Takahashi with a friend (house timeline).
  - Zadig & Voltaire 1997, Paris.
  - Tellason: founders appear only as "Pete & Tony"; no year read.
  - Others: not read or not published.
- **Owner stated:** Velva Sheen's footer reads "Operated by TOPWIN LA CORPORATION", Torrance CA.
- **Vinted:** no brand entry for Tellason or Velva Sheen.

## What contradicted the record
- **Undercover "no US store"** (worklist): confirmed. There are no own US doors, but 14 US stockists.
- **Universal Works:** the worklist domain is universalworks.co.uk; the US storefront is universalworks.com/en-us.
- **Velva Sheen "no own store; trade":** confirmed.
- **Y-3 "US stores?":** still not read.

## For ruling
1. **UGG blocked.** ugg.com served a bot check after the men's apparel listing. The 38 clothing styles are rowed by name with composition "not read". Every price cell for tee, trousers, sweater, outerwear and shoes is NC. Leave NC for a later pass, or carry prices from elsewhere?
2. **Tellason and Ten Thousand doors.** Neither publishes a store, and both are filed as a low-confidence 0. The worklist says "SF" for Tellason. Confirm 0, or NC?
3. **Universal Works style unit.** Is 610 house style codes (model × cloth) the style count? Or should cloths be joined into models (about 270, approximate)? Spier & Mackay was counted by model.
4. **Zara's count.** The feed returned exactly 1,000 colour entries (494 clothing products), which looks like a cap. Is "at least 494" enough, or is the count NC?
5. **Zara's sample.** 71 rows: the first 8 per clothing family. Confirm, as for Puma.
6. **Undercover's Cindy Sherman pieces** (26 styles, artist's artwork credited to Hauser & Wirth). Are these mainline (kept, as filed) or collaborations (excluded)? They also hold the outerwear top (465,000) and the only jean.
7. **Undercover JPY prices.** Prices are tax-inclusive list prices from a store that will not sell to the US. Confirm JPY as filed.
8. **Undefeated's UACTP #001.** The jiu-jitsu sub-line's Los Angeles shop is counted as an own door. Confirm, or exclude it as a different banner?
9. **Undefeated's and Undercover's Asian stores.** Operators are not stated; they are counted as own doors and flagged. Treat them as operator-run?
10. **Zadig & Voltaire's Bloomingdale's shops.** 18 are counted as concessions. Confirm.
11. **Velva Sheen compositions.** 29 of 72 styles say "US Cotton" without percentages and are filed ND. Should a stated single fibre count as 100%?
12. **Universal Works ARCHIVE.** 390 older-season products on sale are counted, at list price. Count them, or treat them as outlet stock and leave them out?
