# price_pass_2026-09-18 — full return (rev 3)

## What was checked
- **All 178 rows.** 170 were read live on 18 Sep 2026 from each brand's own store. The 8 pilot rows were carried forward without a re-read and conformed to rev 3 (`-`, `range`, `USD_landed`, URL-only `store_used`); their notes start "Carried from the 18 Sep pilot".
- **Checks run before returning:**
  - `reconcile.py` returned 178 exact, 0 rewrites, 0 unmatched.
  - No blank cells, and every `SKIP` is untouched: the build script refuses to write any cell that isn't `NC`.
  - Every enum value is legal and every row with a finding has a URL `source`.
- **Values filled:**
  - 828 garment price cells.
  - 116 `NONE` cells, each a verified absence with the reason in `note`.
  - 29 of the 37 requested search URLs, with the passing test word named in `note`.
- **Price rules followed:** every figure is a regular or compare-at price. Every row's `note` names the product behind each figure and records any count shortfall ("88 of 89 tiles").
- **How it was run:** ten browser agents, 17 brands each, all working to one written spec of the rev 3 rules. The spec was updated after the first wave; see currency below.
- **Spot check:** I re-read four cells live myself before returning, and all four matched:
  - Drake's: sweater low 345 and high 1065.
  - Tom Ford: sweater low 1190 and high 3750.
- **Rows that start with `range`:** 74. That prefix now lists which garments are ranges, e.g. `range sweater, outerwear | …`. Some agents had put the tag mid-note; 33 notes were re-prefixed mechanically so it always comes first.

## What was not reached (16 rows `partial`, 76 garment cells still `NC`)
- **The browser extension hangs as soon as the site loads.** Saint Laurent, Gucci and Balenciaga (all Kering; McQueen worked) and Bottega Veneta. Needs a manual read or a different browser.
- **Celine:** Akamai "Access Denied" on every URL.
- **No online store at all:**
  - Comme des Garçons and Junya Watanabe: lookbook only. The only shop linked is Dover Street Market, multi-brand though CDG-owned, and I did not use it.
  - Charvet: holding page only.
  - Rakho: WooCommerce catalogue with every price at 0.
- **Temporarily closed:**
  - Madhappy: store password-locked; not signed in, per the rules.
  - Cesare Attolini: e-boutique "under maintenance".
- **Brax:** the US store sells only trousers and jeans. Tee, polo, dress shirt, sweater and outerwear exist only on the EU stores in EUR, so those cells were left `NC` rather than mixing EUR into a USD row.
- **Search URL not found (8 rows):**
  - Indochino and Ferragamo: in-page search overlays with no URL form.
  - Golden Goose: the US search index returns 0 for almost everything, including jeans and denim.
  - Ring Jacket: `/p/search?keyword=` works, but the brand sells no denim.
  - Rakho, CDG, Junya Watanabe and Charvet: no search at all.
- **Search-URL-only rows (16):** `not_a_staple` and `currency_basis` are left `NC`, because nobody assessed their garments and there are no prices.

## What contradicted the existing record (worklist)
- **The listed domain isn't the US store:**
  - J.Lindeberg → `jlindebergusa.com`
  - Isaia → `isaia.us`
  - Kiton → `us.kiton.com`
  - Corneliani → its `/en_us/` path
  - Samsøe Samsøe → its `/en-US` path
  - Hackett: no working US storefront; the US paths serve the UK store in GBP.
  - Sugar Cane: no own store at all; figures come from Toyo Enterprise's multi-brand JP store, in yen.
- **The platform tag is wrong:**
  - Canada Goose and Bonobos are now Shopify.
  - Tecovas, J.McLaughlin, Rhoback, Suitsupply and Les Deux are headless Shopify with no `/products.json`.
  - Vineyard Vines runs a Salesforce PWA with Algolia listings.
- **The vendor field lies in more places than the rev 3 list:** Southern Tide, Faherty, Percival, Kith, Norse Projects, NN07, Alex Mill, Sease and J.Press.
  - At J.Press it's inverted: own-label knits carry the maker as vendor, and only the brand line on the product page tells own label from third party.
  - Ted Baker and Scotch & Soda list licensees as the vendor.

## What this brief got wrong
1. **The schema's integer cap breaks yen rows.** `int [1, 99999]` can't hold Ring Jacket (¥550,000–880,000 outerwear, ¥132,000 sweater high, ¥220,000 shoes high) or Sugar Cane (¥275,000 outerwear high). I returned the true figures, so `validate.py` will reject those 5 cells. They're held anyway as JPY. The fix is to raise the cap or add a currency-scaled column.
2. **The Shopify rate check isn't enough on its own.** Where the rate isn't 1, root `/products.json` can return the base EUR list, not the US list shown on the page. Eleventy's root feed says 775 where the US page shows 1195. The same setup was found at Incotex, Merz, Aspesi, Ami Paris, Boglioli and Casablanca. Casablanca's feed follows the session's geolocated market until the `/en-us` storefront is opened.
   - **Wave 2 (batches 6–10)** was briefed to read the `/en-us/` feeds and check each figure against the displayed price.
   - **Wave 1 (batches 1–5)** wasn't briefed on this. The three wave-1 stores whose notes show a rate ≠ 1 were checked against the displayed page: Finisterre, Baracuta and Eleventy. The other wave-1 Shopify rows either record rate 1.0 or are US-based stores that weren't re-verified one by one.
   - **Proposed rule:** read the market path and confirm two feed prices against the page.
3. **"Elevated fibre" and "elevated material" are undefined, and they move the highs a lot.**
   - **Blends:** agents required majority cashmere and put the dearer blend in the note. Examples: Herno 870 vs 970, Paul & Shark 795 vs 1,095, Hermès 2,825 vs 3,125. Moncler has no majority-cashmere crew, so its high is a 10% blend.
   - **Other fibres:** silk, ultra-fine wool, alpaca and mohair were counted as elevated, with the cashmere-only figure in the note. Dior's high is 5,400 with silk and 2,700 without; Zegna's is 3,990 vs 3,250.
   - **Fur and exotic skins** were included; the figure without them is in each note:
     - Stefano Ricci mink blouson 53,700
     - Loro Piana vicuña bomber 29,000
     - Hermès alligator loafer 5,150
     - Stefano Ricci crocodile loafer 17,550
     - Sid Mashburn sharkskin loafer 895
   - **Needs a ruling:** fibre list, blend threshold, and whether fur and exotics count.
4. **"Same style" for outerwear has two readings: the exact model or the garment type.** Luxury houses rarely sell one model in two materials, so batches 7–10 paired by type (nylon blouson vs leather blouson) and gave the exact-model pair in the note. Big swings: Missoni coat 2,220/6,440 by type vs bomber 4,460/4,790 by model. Corneliani field jacket 1,795/1,850 vs coat 2,550/4,395.
5. **Sub-lines need a ruling, one at a time:**
   - Stone Island's S.I. Ghost holds every cashmere crew and the only leather jacket. Included; without it the sweater high is 800.
   - Peter Millar Crown Crafted: sweater high 998 with it, 358 without.
   - Kith &Kin: included.
   - Levi's Blue Tab: included; it sets the 295 sweater high.
   - Banana Republic's Archive Reissue capsule: excluded.
   - Fear of God ESSENTIALS: excluded, which makes polo `NONE`; with it, 115–125. Caution: I told that agent "main collection only", which overrode the spec's default of including sub-lines.
6. **`range` now covers 74 of 178 rows, so the staple rule is the exception, not the default.** Loafers and suede/shearling pairs are rare below the luxury tier. The Spectrum should show `range` cells differently from staple pairs, or it will compare unlike things.
7. **Other rule gaps, each decided conservatively with the alternative in the note:**
   - moccasins, lace-up "loafers" and slippers
   - part-leather jackets, e.g. wool body with leather sleeves
   - maker collaborations on own items (Sunspel × Cheaney loafers)
   - sold-out and last-season items still listed (Rick Owens, Filson, Tecovas Last Call)
   - whether a track jacket counts as outerwear (Y.Chroma)
   - a cashmere "sweatshirt" (Aimé Leon Dore)
   - flip-flops in the shoe range fallback (Vineyard Vines)
8. **The search test has no case for brands that sell no denim** (Ring Jacket, Indochino, Easy Mondays). In the other direction, some searches "pass" on unrelated fuzzy matches: Valstar's `jeans` search returns 17 items and none are jeans.
9. **Landed and tax-inclusive prices:**
   - `USD_landed`: Auralee, Reiss ("Duties Paid"), Officine Générale, Rick Owens and Husbands.
   - Our Legacy ships duty-paid but excludes US sales tax, and is recorded `USD_landed`; confirm the label.
   - Wales Bonner (GBP) and Zilli (EUR) have no USD list.
   - Rubinacci's USD is exactly 1.2× its GBP list and may not be a true US price.
10. **Compare-at prices aren't always real full prices.**
    - Everlane's "Better prices" repricing leaves old list prices in compare-at.
    - Joe's Jeans' almost entirely marked-down catalogue: compare-at ($248 vs $69) may be an inflated reference.
    - Brooks Brothers tiles show markdowns only as a range.
    - J.Press shows a "SALE PRICE" label at full price.

## Out of scope but noticed
- **Stores and ranges that are changing:**
  - Everlane launches a loafer collection on 23 Sep, so its shoe cells will go stale.
  - Club Monaco's live men's range is very thin; the feed returns 19 knitwear items against a stated 142.
  - Southern Tide and Taylor Stitch ranges are seasonal and thin right now.
- **Feeds that don't match the live store:** Duck Head's feed carries about 219 untyped "SALE" copies with no compare-at. Les Deux, PAIGE and Finisterre feeds list products that 404 on the live US store.
- **Price formats that break parsing:** NN07 prints "1 495 USD" and Cucinelli prints "$ 1.650,00".
- **Tooling:**
  - Cross-origin fetches (Banana Republic → api.gap.com) hung the extension for about 30 minutes.
  - The extension blocks any tool output that contains a query string.
- **Useful data endpoints, recorded in the row notes:** Moncler, Burberry, BOSS, Massimo Dutti and Loewe (paged `?page=N`, 16 per page).
