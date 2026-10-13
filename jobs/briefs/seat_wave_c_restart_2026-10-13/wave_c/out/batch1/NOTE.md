# Wave C full records: batch 1 of 9, 10 October 2026 (revised after rulings)

Brands: Alan Flusser, Anglo-Italian, Asket, Awake NY, Aztech Mountain, Bad Birdie, Beams, Berg & Berg, Birdwell, Blundstone. All read in Chrome on 10 October.

Files: `return.csv` (10 rows, 132 columns, no empty cells), `return_styles.csv`, `own_doors.csv` and `stockists.csv`. Reconcile is clean.

## What was read
- **Sections 1–5 (prices, men's listing links, fibre by style, doors, stockists):** read from each brand's own store, one request at a time.
  - Shopify houses: the full `/products.json` feed, plus the product pages wherever composition is not in the feed. That was Aztech's "Fiber content", Bad Birdie's "Materials + Care" and Berg & Berg's "Details Materials".
  - Asket (not Shopify): read from the server-rendered state of its men's listing pages and each product page.
  - Beams: re-read on beams-america.com (ruling 10 Oct), replacing the beams.co.jp attempt. Beams America is multi-brand, so only vendor BEAMS and the BEAMS T sub-line count: 140 of 381 men's products, 74 SKU stems, 67 clothing styles. NEEDLES, TEATORA, Hender Scheme, Buzz Rickson's and the others are excluded. Composition comes from each product page's "Composition & Care".
- **Style method:**
  - SKU stem where the SKU carries one: Bad Birdie (`BBMP001` = the core printed polo, 37 prints in 1 style), Birdwell (`2BS1-1275`) and Beams (first 11 digits of the item number).
  - Asket: its own parent SKU.
  - Anglo-Italian, Awake and Berg & Berg: title de-duplication.
  - Aztech: one handle per style.
- **Sections 6–13:** each brand's about, store and fabric pages; Grailed designer pages; Vinted's brand API (men's catalogue URL built on the brand id).

## What was not reached
- **B Corp and GOTS: `NC` for all ten.** B Lab's directory ignored its search query in Chrome (it showed "all 339 B Corps" whatever was typed). Profile URLs could not be used as a test either, because the control slug `patagonia` also returned 404. The GOTS database was not attempted. Both need another route.
- **Pronunciation: `NC` everywhere.** No brand states one.
- **Tech:** `proposed_tech` is `NC` everywhere because the brief gives no tech rubric. The evidence columns are filled.
- **Stockists not rowed:**
  - Blundstone's retailer locator renders client-side.
  - Asket's stockists were not looked for.
  - Awake's 51 non-North-American stockists are named on its page but not rowed.

## Prices: things to know
- **Awake NY is a markdown house.** Most live product is at 50% off with a compare-at, and every figure is the compare-at.
- **Berg & Berg prices are duties-paid** (currency `USD_landed`).
- **Anglo-Italian is filed at the displayed US price, not the feed.** The spot-check found the feed (`products.json` / `.js`, USD presentment) running 1.48% above the displayed page on all 14 products checked (polo: feed 232.77, page $229.33). The prices are taken from the server-rendered page instead. Facts-first's "feed = displayed" held on 8 Oct and no longer does, so Shopify Markets houses need this check every time.
- **Berg & Berg checked the same way:** page and feed agree on four products.
- **Shoes:**
  - Bad Birdie's only shoe, a Payntr collaboration, is kept as ruled.
  - Anglo-Italian's loafers are Crockett & Jones (stocked), so its shoe cells use its own boots.
  - Beams' only own-label shoe on the US store is a BEAMS JAPAN wooden geta sandal (125).
- **Alan Flusser is custom only.** The one published from-price fills the dress shirt; trousers and outerwear are `np`.

## Fibre: the headline per house
- **Berg & Berg:** 24 of 24 styles natural-led.
- **Anglo-Italian:** 86 of the 89 styles with a composition are natural-led; the three synthetic ones are the Rain Parka, the Featherweight Keepers Chore and the Keepers Fleece.
- **Bad Birdie:** a synthetic house, 24 of 30 synthetic-led, with elastane on the main line in 17. The six natural-led styles are the four tees, the cotton-majority Jacquard Polo and the French Terry Crewneck.
- **Aztech Mountain:** synthetic shells (ski jackets, pants, fleece) beside natural knits and shirts. The split categories are each under 10 styles, so the rule returns `one`.
- **Birdwell:** SurfNyl® is now filed as nylon, as ruled. That makes 19 styles polyamide-led, and jackets join UV shirts as a synthetic-led category. The 11 SurfStretch® boardshorts stay undisclosed: the site states no fibre and the ruling named SurfNyl only. Coverage is 88 of 99. The 21 boardshorts count as swim.
- **Beams:** 48 of the 59 styles with a composition are natural-led (cotton nearly throughout), and 11 synthetic-led: check shirts in polyester-rayon or polyester-cotton, three polyester boxer shorts, a nylon jacket, the Renewool jacket, the wool-blend slacks and the cargo shorts. The washi knit leads with paper yarn (35%), filed as other-natural. Japanese labels write "polyurethane" for stretch; it is filed as written, so `spandex_styles` undercounts stretch at Beams.
- **Asket:** composition read on 33 of 47 styles. The site renders other products' material blocks on every product page, so only the product's own record was used.
- **Awake NY:** composition on 22 of 39; most name a fibre without a percentage ("washed cotton").

## What contradicted the record
- **Asket's origin claim.** Its about page says garments are made "exclusively in Italy and Portugal", but its own product data gives Romania as country of origin for several knits and the wool coat.
- **Aztech's Aspen door.** No Aspen door appears on the brand's locations page; Aspen appears only as its home.
- **Bad Birdie's domain.** The domain on file (badbirdie.com) redirects to badbirdiegolf.com.
- **Beams' US door: 1, not 0.** Facts-first said none. Beams America's locations page lists BEAMS MALIBU, 23710 Malibu Rd, Malibu CA 90265; it is in `own_doors.csv` and `return.csv`.

## Parser fix in this revision
Labelled part breaks inside a composition ("Contrast fabric:", "Rib part:", "Waist Part:") are now cut, so only the main fabric is read. Before the fix, a 70/30 cotton-polyester chino with a polyester contrast panel read as polyester-led. Every house was re-run; only Beams' numbers moved.

## Rulings applied (10 Oct)
1. Large houses: the style layer may be a category-stratified sample. Not needed in this batch.
2. Beams is read on beams-america.com.
3. Bad Birdie's collaboration shoe stays in the shoes cells.
4. SurfNyl® is filed as nylon (polyamide), and each affected style row says so in `note`.

## For ruling
1. **SurfStretch® (11 Birdwell boardshorts):** the ruling named SurfNyl only. Should SurfStretch also be filed as nylon, or stay undisclosed?
2. **Craft proposals** (no current scores were on the worklist to compare against):
   - Alan Flusser 4
   - Asket 3
   - Aztech 3
   - Anglo-Italian 2
   - Berg & Berg 2
   - Birdwell 2
   - Awake 1
   - Bad Birdie 1
   - Beams 1 (on the US store's evidence only)
   - Blundstone not proposed

## What the brief got wrong
- **Time.** The 70-minute time box per brand is not compatible with moving data out of the browser. The workspace cannot reach brand sites (org egress policy), so every row passes through the Chrome tool, which returns about 1,000 characters per call. Large houses (Nike, Uniqlo, Zara, Gap) will use the ruled category-stratified sample.
- **Schema gaps.** `return_counts.csv` and the tech section have no rubric or schema in the brief. I used what is described in the counts note and left `proposed_tech` as `NC`.
