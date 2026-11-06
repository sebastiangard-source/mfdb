# NOTE — seat_withered_fig_d_2026-11-06 (partial return)

**Browser:** the Chrome extension failed for this whole batch (get_page_text and JS errors). Everything below was read with the page fetcher and search only. Every unreached field is `NC`.

## Barnstormer — stopped (ruling 1)
- Withered Fig vendor pages: a Japanese chino and trouser maker. Its collection page says it was founded in 1977 by Ebine Monroe. Product copy says "Made in Japan", 100% cotton.
- Neither the product page nor the collection page names or links a brand site. Drinkwater's search page could not be fetched, so the second route is not done. Search shows other retailers (HAKU, Beams, Frans Boone, Stuf-f, Random Walk) and a ZOZO page that has moved.
- I did not confirm that Drinkwater's "Barnstormer" is the same brand. The Withered Fig line (chinos, shorts, dress fatigue, $255–$330) is not the US aviation company barnstormer-usa.com that I guessed earlier, so that guess is withdrawn.
- Facts-first row stays `NC`. Needs a Drinkwater's product page and a brand site.

## Câbleami, Chup — not closed
Both are hats-only and socks-only on retailer pages only. I did not reach either brand's own site. The ruling needs the brand's own site, so they remain unconfirmed. I'd not write full records for either.

## Dr. Sole — stopped (ruling 3)
The Withered Fig journal interview names no website, only Instagram and Facebook. Brand is Taipei-based, with a shop there and a factory in southern China, founded by Chao-Yung Lin. It makes rubber soles and heels, resoling and custom soles for other brands, and also its own boots (Game Changer, OZ Troopers). Under the ruling's wording the missing site means stop. Scope is arguable, because it does make boots. Sebastian to rule.

## Fitted Underground — partial
- Read collection pages 1–3 of 117. The fetcher summarised pages, and sale and regular prices are unreliable. About a dozen SKUs show $0.00 (probably unpriced).
- Top prices seen: Bespoke Storm Rider Jacket and Bespoke Workpant $995; Bespoke Jeans $895.
- Ready-to-wear top I could confirm: W17 Copperhead Akasabi jeans from $355, sold out. Also STRIDER Sashiko $425.
- **Own door:** the Schedule page gives 108 Bayard St, Williamsburg, Brooklyn, with a fitting "denim bar", repairs and pickup, open weekdays 10–5. I count it as one own US door, format "studio", for Sebastian to rule on. The page's own wording is "denim bar", not "store".
- Not done: eight-garment grid beyond tee and jeans, fibre by style, craft, origin, lookbook, Vinted/Grailed, B Corp/GOTS, quotation, 38 dials.
- Brand writes its name "FITTED Underground" (capital FITTED).

## National Athletic Goods — partial
- Own pages say Vancouver, Canada, made in Canada. The site looks wholesale-led (Stockists, Dealer Login, Shop Archive).
- Stockists page is a list of independent shops in seven countries and names no own stores. Own doors 0.
- Shop Archive could not be fetched, so I cannot yet say whether it sells direct. I left prices as `NC`, not `np`. The $95–$165 Withered Fig figures are retailer figures and are not recorded.
- Not done: everything beyond stores and stockists.

## Not in scope / noticed
- A reader flagged that Withered Fig plans a physical shop in Falls Church, VA (early 2026). I have not checked it.
- 1 of 6 brands has a clear own door; none is on the map.

## Contradicts or brief errors
- The worklist says all six are clothing or footwear: Câbleami (hats) and Chup (socks) probably are not.
- `reconcile.py` not run (no match expected; not executed here).

## Update (browser back)
- **National Athletic Goods:** the site does not sell direct. Pages are About, Stockists, Contact, Collection (season lookbooks, latest spring & summer 2024), Dealer Login. `/archive` says the shop archive is "coming soon". No brand prices are published, so prices are `np` (this replaces the earlier `NC` and the "cannot say whether it sells direct" line above). Lookbook found. The Withered Fig $95–$165 figures remain retailer figures and are not recorded.
- Fitted Underground full record still not done in the browser.

## Fitted Underground — second pass (browser)
- Read the full product feed (117 products), the About page and the Schedule page. About: founded 2014 by "Eric", who sewed jeans alone in a Brooklyn basement for about a decade; Japanese selvedge and organic cotton.
- Prices (regular, USD, US selector): tees $35–$115; jeans $195 (D10 Citizen, on sale $95) to $355 base size, with larger sizes up to about $455; hoodie $165; chore coat $225; STRIDER jackets $395–$425 ready-to-wear. Bespoke jeans $895 and bespoke jacket $995 are made-to-measure and excluded from the ready range. No polos, dress shirts, dress pants or shoes (`NONE`).
- Where made: product copy says Brooklyn (a named artisan), USA tees, Japanese selvedge looms, and five items "Made in China, finished in Brooklyn". Proposed craft 4; Sebastian rules.
- Still `NC`: fibre by style, tech, resale, certifications, ownership today, signature product, and all 38 dials.

## Batch 3 — fills (6 Nov 2026)

**reconcile.py** on all six names: 6 names in, 0 exact, 0 to rewrite, 6 unmatched (Fitted Underground, National Athletic Goods, Barnstormer, Câbleami, Chup, Dr. Sole). Expected: all new.

### Fitted Underground
- `return_styles.csv`: 40 styles from 57 men's clothing products (all 117 products read from the feed; the other 60 are hats, totes, belts, wallets, scarves, beanies, 21 fabric-library SKUs, services, gift card, event). 32 state a composition (all cotton-led, 80.0% natural, 0% synthetic, 0% cellulosic); 8 state none (FLATIRON, STRIDER, STRIDER Sashiko, 5 bespoke pieces). Three styles carry elastane (D10 97/3, D13 Standard Issue 99/1, D13 Gunmetal 99/1). Colourway ratio 1.43 (57 products to 40 styles). The hoodie is a named fibre ("cotton fleece") with no percentage, so lead_pct is ND.
- Bespoke pieces are in the style count, flagged made-to-measure; they are out of the ready-to-wear price range as ruled.
- Entry price stays $195 for jeans (D10 Citizen regular; sale $95 not used). Founder recorded as "Eric (surname not stated)".
- Craft 4 reasoning is in `craft_reasoning` (Brooklyn making, named artisan, USA tees, Japanese selvedge, repair program; against: five "Made in China, finished in Brooklyn" items, no owned mill proved).
- `dials.csv`: 38 rows. 8 are `NC`/`NONE` (golffice, sail, rock, surf `NC`; linen, shoes `NONE`). Logo is low confidence: I counted mentions in product text (21 of 57), not marks on photos, so the ten-page visual read is not done.
- Tech `NONE` (no named technical fabrics). Signature product: PFT 220 Japanese Ring-Spun Cotton Tee (copy says "our bestselling"). Quotation: the About line already filed. Vinted: one listing (W30, $80) seen by the fetcher. Grailed: no Fitted Underground entry in the designer index. B Corp: directory search returned unrelated results, so `NC`. GOTS database not reached, `NC`. Lookbook not read, `NC`. Pronunciation `NC`.

### National Athletic Goods
- No product pages exist on the brand's site, and the season lookbooks (latest spring & summer 2024) sit behind the dealer login, which I did not touch. So styles, fibre, tech and almost all dials are `NC`; `return_styles.csv` holds one NC row. 0 product pages read. Only murica is scored (3, low, from the About page).
- The site says wholesale inquiries go to contact@nationalathleticgoods.com and consumers should use the stockists link.
- Grailed lists a National Athletic Goods designer page (count not read). Vinted, B Corp and GOTS not checked. Founder, year and ownership are not stated on any page I read.

### Câbleami — stopped, accessories
- Own site is cableami.jp (cableami.com does not resolve). Menu: Home, About, Company, Collections, Store List, Contact, Instagram. The Collections page shows hats only. Mark: "câbleami®" in lowercase. Facts-first row updated. No full record.

### Chup — not reached
- chup.jp is blocked to the page fetcher by robots.txt; in the browser the tab loaded but the extension would not return the page. Row stays `NC` (hosiery only per retailer pages). Not confirmed on the brand's own site.

### Not done
- Barnstormer (needs a brand site or Drinkwater's page) and Dr. Sole (no site) remain as stopped.
- Nothing sent to the map. Grailed, B Corp and GOTS directory results are partial as noted.

## Batch 4 — open items settled (6 Nov 2026)

### Fitted Underground
- Ten men's product pages read for logo, fuss and comfort (D10 Citizen, D13 Standard Issue, W13 BK Kibata, PFT 220 tee, Brooklyn Dragon Logo tee, CHELSEA workshirt, Heavyweight Hoodie, STRIDER Sashiko, OG 718 Fatigue Pant, NOLITA overshirt). I read text, not photos, so logo stays medium confidence and says so.
- Logo 2: 3 jeans pages describe a leather "Brooklyn Dragon" patch and a "Brooklyn Sunrise" waistband button, 1 tee has a hand-screenprinted gold Dragon, 6 of 10 describe no mark. Fuss +1: 7 of 10 pages quote "Wash as infrequently as loved ones permit... Always hang dry." Comfort 3: 8 of 10 carry a comfort or softness line.
- Closed: golffice 0 (from the garments), sail NA (no boating register; pages listed), rock 1 and surf 1 (none found, pages read), linen 1, shoes 0. Forg moved from 5 to 4 (custom size and bespoke exist, but ready sizes are waist-only with no inseam options). Status stays 2, now stated as scored from marks and price.
- ND styles: 8 styles state no composition (FLATIRON, STRIDER, STRIDER Sashiko, plus the 5 made-to-measure pieces: Bespoke Work Shirt, Western Shirt, Storm Rider Jacket, Workpant, Jeans). All 8 are `ND` in `return_styles.csv`, with the reason in the note column. The 5 bespoke pieces are in the style count and out of the ready-to-wear price range.

### National Athletic Goods
- **The brand publishes no catalogue.** Its site has About, Stockists, Contact, Collection and Archive; the lookbooks are behind the dealer login, which I did not enter, and /archive says "coming soon". There is no brand product page, so nothing on the brand's own site gives a price, composition or garment.
- Pages used instead (retailer evidence, low confidence): Withered Fig collection page and six product pages (basic tee, long-sleeve gym tee, pocket tee, pullover parka sweatshirt, raglan warm-up, single-V warm-up); stuf-f collection page and three product pages (1/4 zip parka, athletic tee "natnl", pocket gym tee l-s); Gravity Pope collection page (one line, sale price, no product detail). The brand About page for wording.
- `return_styles.csv`: 9 styles from 22 listings. All state 100% cotton (7 organic), 0 elastane. 6oz to 7oz jersey tees and 10oz to 11oz terry sweats, all made in Canada from Japanese fabric.
- Prices stay `np`: the brand publishes none. Withered Fig ($95 to $165 USD) and stuf-f (EUR 50 to 119, sale) are retailer prices and are not recorded as the brand's.
- All 38 dials scored, low confidence, with sail `NA` and the pages read. Where the brand shows none (denim, cashmere, linen, wool, synth, western, rock, workwear, surf) the score is 1 with "none found". Whitet is 1: no plain white tee found (black, choco and taupe at Withered Fig; a white heather long-sleeve and a marled tee at stuf-f). Murica moved from 3 to 4 on the "NATNL" print and the About wording.
- Craft proposed 3, low confidence. No founder, year or owner on any page read, so those cells stay `NC` with the reason. Vinted: search showed 5 unrelated results, no NAG listings. Grailed: designer page exists, count not read. B Corp and GOTS left alone per ruling.

### Chup — closed as hosiery
- chup.jp does not resolve. The brand's own store is chupsocks.com ("Official CHUP Socks online store", run by Glen Clyde Inc.). Navigation shows socks collections and one Knit Hat; no clothing or footwear. Facts-first row updated as hosiery. Mark written "CHUP". English-domain fallback tried: chup.jp/en (DNS fail), chupsocks.com (loaded).

### Barnstormer — stopped with what I found
- Withered Fig vendor pages and collection page: Japanese chino brand, founded 1977 by Ebine Monroe, made in Japan, 100% cotton. stuf-f's page says the same and calls it the first Japanese brand to make American khaki chinos in Japan. Neither links a brand site, a Japanese-language search found none, and a Drinkwater's page could not be fetched. It is a clothing brand, so it would qualify for a full record if a site is found. Needs the Drinkwater's page or the brand's own URL.

### Dr. Sole — stopped
- Read the Withered Fig journal interview: it names no website (only Instagram dr_sole_originals and a Facebook page). It makes rubber soles and heels, resoling and custom soles, plus in-house boots. No site, so the facts-first row stands. Not a full record.

### Left alone
- B Corp and GOTS (no further lookups), Câbleami (closed as hats only).

## Batch 5 — Barnstormer full record (6 Nov 2026)
- Site supplied by Sebastian: barnstormer.tokyo, the brand's own Japanese-only Shopify store (company 株式会社アパレルビレッジ / Apparel Village Co., representative Ebine Monroe, Koto-ku, Tokyo). Prices are in yen; the site's currency rate is 1.0 and I did not convert.
- Read in the browser: product feed (65 products, 61 clothing, 51 styles after collapsing), Story, About Us, Size Guide, Stockists, Kakurega pages.
- **Own door:** one, the official shop KAKUREGA (隠れ家) at Tokiwa 1-4-10-A, Koto-ku, Tokyo (Kiyosumi-Shirakawa), closed Mon and Tue. None in the US. **Stockists:** a LIST of about 35 Japanese shops plus 8 overseas (FR, DE, GB, TW, KR, TH, SG, AU); none in the US. The Japan names were not all captured.
- **Prices (JPY, regular):** pants ¥24,200 to ¥48,400; Cuba shirts ¥17,600 to ¥29,700; denim trousers ¥30,800 to ¥47,300; jackets and blazers ¥49,500 to ¥132,000 (the MacArthur2 jacket's ¥41,580 is a Black Friday sale price; regular ¥59,400). No tees, polos, sweaters or shoes.
- **Fibre:** 51 styles, 26 with a composition (9 cotton, 17 wool; 20 by percentage and 6 named wool), 25 none in the text I scanned. The Japanese copy was scanned by pattern, not read line by line, so some of the 25 `ND` rows may name a fibre in prose. Stated stretch: none.
- **Heritage and ownership:** the story says the predecessor was founded in 1977; the founder is not named there. Ebine Monroe appears as the company's representative.
- Craft proposed 4; quote and signature (1002P Dress Chinos, called "バーンストーマーの定番") from the brand's own pages. All 38 dials scored from the garments and story, low to medium confidence, with sail `NA`.
- Not done: Vinted fetch failed, so `NC`; Grailed designer index has no Barnstormer. B Corp and GOTS left alone. Photos not inspected for logo.
- Dr. Sole and Chup stay stopped as before. Nothing sent to the map.
