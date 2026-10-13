# Wave C full records: batch 6 of 9, 13 October 2026

Brands (worklist rows 51–60): Nigel Cabourn, Nudie Jeans, Oliver Spencer, Onward Reserve, Outdoor Voices, Oxxford, Pact, Perfect Moment, Pilgrim Surf + Supply, Pini Parma.

Files:
- `return.csv`: 10 rows, 132 columns, no empty cells.
- `return_styles.csv`: 1,140 style rows (9 houses; Oxxford has no shop, so it has no style table).
- `own_doors.csv`: 39 rows.
- `stockists.csv`: 88 rows (Oxxford 75).

Reconcile is clean on all four files (10 names: 10 exact, 0 to rewrite, 0 unmatched). The style table passes `schema_styles.json`. Every site was read in Chrome on 13 October.

As in batch 5, price cells are whole units, and exact figures are given in `note` (see that batch's ruling item on rounding).

## What was read
- **Shopify houses:**
  - Oliver Spencer: US market path, USD. Feed and `.js` prices agree.
  - Onward Reserve, Outdoor Voices, Pilgrim Surf + Supply: USD.
  - Pini Parma: USD on the US market (selected through the store's localization form; duties not included). The full `/products.json` feed was read, with composition from each PDP. The base currency is EUR, about 1.6x lower.
- **Nigel Cabourn:** cabourn.com is a brand site whose feed holds only styling posts. Its US page sends shoppers to the **Outer Limits Online Store** (outerlimits.co.jp), and that store is what was read.
  - Prices are in JPY, filed tax-inclusive as displayed (feed × 1.1, checked on two products), and not converted.
  - Composition (素材) and country (生産国) were read from every men's PDP.
- **Nudie Jeans:** a Centra store. The selection pages and every men's product page were read from the page data.
  - Each product carries a composition, a country and a **named supplier** (garment maker).
- **Pact:** the product API behind the men's pages (26 records). Composition comes from the tag list.
- **Perfect Moment:** men's category pages and every PDP.
  - 40 product links were reachable; the men's page says 51 products.
- **Oxxford:** no shop. The site pages were read, plus the retail-partner list.
- **Price spot-check:** re-read live via `.js` after the browser came back: Pini Parma 16, Oliver Spencer 12, Onward Reserve 14, Pilgrim 11 and Outdoor Voices 6 picks. All matched but one: Pilgrim's trouser high (Alpine Fatigue Pant, 385) was a compare-at on a marked-down colour while the same pant lists at 265 in its other colour; the high is now the Barnes Back Satin Fatigue Pant at 295. Nudie, Pact, Perfect Moment and Nigel Cabourn picks were read once.

## Exclusions you should know about
- **Collaborations:**
  - Nigel Cabourn: Lee x Nigel Cabourn OX'ed Silver, Mammut, RMFC, Sunspel, and the Viberg Aspley. That makes Nigel Cabourn's shoes NONE.
  - Oliver Spencer: Le Tings, and the Solovair x Oliver Spencer shoes (all its footwear). Shoes are NONE.
  - Onward Reserve: Coca-Cola and Waffle House co-branded pieces.
  - Pilgrim: Extra Vitamins + Pilgrim and Rivian.
- **Licensed team lines (Onward Reserve):**
  - Out of the style count: Collegiate, MLB, NFL, custom and youth lines.
  - Also out: collegiate "Vintage Script" shorts, and an SMU sweatshirt.
- **Lybro (Nigel Cabourn):** the heritage workwear label is "now part of Nigel Cabourn" but is sold under its own name. It is in the style table (lines = Lybro) but not used for prices. See ruling item 1.
- **Limited editions:**
  - Nigel Cabourn: the numbered LE5 pieces and the memorial "Spirit" tee.
  - Pini Parma: Limited Edition trousers.
  - None of these are taken as highs.
- **Suit bundles (Oliver Spencer):** combined suit products are bundles of the jacket and trouser already listed. They are left out of the style table.
- **Footwear:** Onward Reserve and Pini Parma shoes are priced but kept out of the style table, as for Lardini in batch 5.

## Prices: things to know
- **Nigel Cabourn (JPY):**
  - The tee is 9,350 to 17,600.
  - Shirts top out with an OX'ed Silver linen shirt at 44,000.
  - The outerwear high is the Everest Parka, ¥682,000. It has a coyote-fur hood trim and is filed as a `range` high, not an elevated pair. See ruling item 2.
- **Pini Parma (USD, US market):**
  - Sweater pair: wool-and-silk crewneck 318 against a 100% 2-ply cashmere crewneck 606.
  - Shoes pair: penny loafer 398 against tassel loafer 446.
  - Outerwear: fur-collared coats (2,316) and fur-trimmed cashmere bombers are not taken. The high is a 99% wool reversible coat at 2,316.
- **Pilgrim tee pair:** cotton Team Tee 55 against a Super 140's wool jersey tee 135. Super 140's is superfine wool, so this counts as elevated.
- **Onward Reserve:**
  - Shoes pair: Penny Driver and Bit Loafer, both 198.
  - Sweater: there is no cashmere crewneck, so the cashmere V-neck (295) is a `range` high.
- **Pact:** prices are MSRP. Most items were selling below it on 13 Oct (pants 29 against 98).
- **Oxxford:** dress shirt, dress pants and outerwear are `np`, as ruled. The other slots are NC.
- **Perfect Moment:** ski pants stand in for trousers. There are no tees, polos, shirts, jeans or shoes (NONE).

## Fibre: the headline per house
- **Pact:** 100% natural (organic cotton).
- **Nudie Jeans:** 98% natural.
- **Oliver Spencer:** 97% natural.
- **Pini Parma:** 94% natural.
- **Nigel Cabourn:** 93% natural.
- **Pilgrim:** 71% natural; outerwear is synthetic-led.
- **Onward Reserve:** split, 50% natural / 44% synthetic. The performance polos, shirts, quarter-zips and jackets are synthetic-led; the sport coats are natural.
- **Perfect Moment:** 55% synthetic (ski shells); the merino knits are natural.
- **Outdoor Voices:** 81% synthetic.
- **Partial compositions:** 38 rows carry a "sums to" flag. Most are Oliver Spencer and Outdoor Voices pages that give only part of the line.

## Doors
- **Onward Reserve: 14 US.** Each has a store page with address and posted hours. Charlotte and Raleigh are in North Carolina (state NC).
- **Nudie Jeans: 3 US / 38 world.** All are "Nudie Jeans Repair Shops".
  - US: Bedford (Brooklyn), Bowery (Manhattan), La Brea (LA).
  - Only the 3 US shops are rowed.
- **Pilgrim Surf + Supply: 1 US / 3 world.**
  - The US door is 33 Grand St, Brooklyn: a multi-brand shop under the brand's name (ruled).
  - Tokyo and Kyoto are run through the Beams partnership and are flagged.
- **Oxxford: 1.** The Chicago factory showroom (ruled). The footer prints 6535 South Archer Ave; the factory and contact pages say 5635.
- **Nigel Cabourn: 0 US / 9 world, all Japan.**
  - Women's-only Nakameguro is flagged.
  - Lucua Osaka is flagged.
  - Hankyu Men's is a concession.
  - No UK store is listed.
- **Oliver Spencer: 0 US / 4 world.** All four are in London.
- **Pini Parma: 0 US / 9 world.** Addresses load client-side, so no rows (one placeholder row). The operator is not stated.
- **Outdoor Voices: 0.** Carried from the counts job and not re-read; low confidence.
- **Pact: 0.** Online only.
- **Perfect Moment: NC.** The "Stores & Popups" page renders nothing.

## Stockists rowed
- **Oxxford:** 75 US retail partners with full addresses, 7 of them Neiman Marcus (department store).
- **Pilgrim:** 5 US names, no addresses.
- **Not read (NC):**
  - Nigel Cabourn: the stockist tabs render empty.
  - Nudie and Onward Reserve: client-side locators.
  - Oliver Spencer, Pini Parma and Perfect Moment.
- **NONE:** Pact and Outdoor Voices.

## Sections 6–13
- **Craft proposals:**
  - Oxxford 5: own Chicago workrooms, 14,000 hand stitches, 30 hours of handwork.
  - Nudie Jeans 4: the garment maker is named on every product, plus own repair shops.
  - Nigel Cabourn 3, Oliver Spencer 3, Pini Parma 3.
  - Onward Reserve 2, Pact 2, Pilgrim 2.
  - Outdoor Voices 1, Perfect Moment 1.
- **Named mills:**
  - Pini Parma: Loro Piana, Albini, Thomas Mason, Candiani, Canclini, Albiate, Fratelli Tallia di Delfino, in compositions.
  - Onward Reserve: Barberis, Reda, Guabello, Di Pray, E. Thomas, Barbera, in sport-coat titles.
- **GOTS:** Pact's sustainability page shows "Certified by Control Union 832196" beside its GOTS link, so gots_certified is yes. B Corp is NC for all.
- **Founding:**
  - Oxxford 1916, Chicago, Louis and Jacob Weinberg.
  - Perfect Moment 1984, Chamonix, Thierry Donard; owned since 2010 by Jane and Max Gottschalk.
  - Nudie Jeans 2001, Gothenburg.
  - Oliver Spencer 2002, London.
  - Pilgrim 2012, Williamsburg, Chris and Erin Gentile.
  - Onward Reserve: founder TJ Callaway, no year given.
  - Nigel Cabourn: no year given (first brand Cricket, launched in his final year at Northumbria, 1967–71).
- **Quotes:** Nigel Cabourn, Oliver Spencer, Onward Reserve (TJ Callaway), Oxxford, Pact and Pilgrim.
- **Vinted:**
  - No brand entry for Onward Reserve, Oxxford, Pilgrim or Pini Parma.
  - Pact's entry may be another "pact".
- **Grailed:** no page for Onward Reserve or Pact.

## What contradicted the record
- **Nigel Cabourn's shop is Japanese.** cabourn.com has no products; the shop is Outer Limits Co., Ltd. in JPY, and the store list is all Japan.
- **Oxxford's address.** The site gives two street numbers for the showroom (5635 and 6535 South Archer Avenue).

## For ruling
1. **Lybro (Nigel Cabourn).** "Established in 1927 … now part of Nigel Cabourn", and sold under the Lybro name. It is in the style table but kept out of prices. Is it a sub-line, or a separate label?
2. **Fur-trimmed highs.** Nigel Cabourn's Everest Parka (coyote-fur hood trim) is filed as the outerwear `range` high, at ¥682,000. For Pini Parma, the mink-collar coats were skipped and a wool coat at the same price was taken. Should trimmed garments be excluded from range highs too, as they are from elevated highs?
3. **Nigel Cabourn's store and currency.** Is reading the Outer Limits store in JPY right for a British-founded house whose only shop is now Japanese?
4. **Pini Parma currency (resolved, for information).** The store serves EUR by default (visitor country FR) but has a US market: with US selected, the feed, `.js` and the page all show USD (duties not included). The batch was read on the US market, so USD is filed. Confirm USD over EUR.
5. **Pini Parma doors.** There are 9 named stores, but addresses load only in a client-side map, and the site has a franchising page. Count 9, or hold until the addresses and operators are read?
6. **Pilgrim's Japanese shops.** Tokyo and Kyoto opened through a partnership with Beams. They are counted, flagged, as operator-run doors (the Universal Works pattern). Confirm.
7. **Nudie Jeans' world doors.** All 38 Repair Shops are counted. The operators (for example in Indonesia and Australia) are not stated. Confirm.
8. **Perfect Moment doors.** NC: the stores page renders empty.
9. **Oxxford's showroom address.** The site prints 5635 and 6535 South Archer Avenue. 5635 is rowed, from the factory and contact pages.
10. **Onward Reserve's licensed lines.** The collegiate, MLB and NFL ranges are about 80% of the feed and were excluded as licensed lines. Confirm.
11. **Pilgrim scope.** Only Pilgrim-label items in the store's mens collection are counted (55 styles), so this is a floor. Should older stock that is in neither collection be added?
