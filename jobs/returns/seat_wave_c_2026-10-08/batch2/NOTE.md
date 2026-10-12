# Wave C full records: batch 2 of 9, 11 October 2026 (revised after the 11 Oct rulings)

Brands: Brain Dead, Budd Shirtmakers, C.P. Company, Carmina, Castaway Nantucket Island, Closed, Danner, Denim Tears, Deus Ex Machina, Dickies.

Files:
- `return.csv`: 10 rows, 132 columns, no empty cells.
- `return_styles.csv`: 1,197 style rows.
- `own_doors.csv`: 85 rows.
- `stockists.csv`: 218 rows.

Reconcile is clean on all four files (10 exact, 0 to rewrite, 0 unmatched). Every site was read in Chrome on 11 October. The workspace still gets a 403 on every brand host.

## What was read
- **Shopify houses** (Brain Dead, Budd, Castaway, Denim Tears, Deus, Dickies):
  - The full `/products.json` feed for each. For Dickies the feed was `/en-us/collections/mens`.
  - Product pages wherever the feed carries no composition.
  - Only in-stock products are counted.
- **Price spot-check.** The picked products were re-read from the product `.js` record (Brain Dead 8, Castaway 10, Denim Tears 10, Deus 5, Dickies 6), and from the displayed page at Budd (2) and Danner (2). Two corrections came out of it:
  - **Dickies charges more for larger sizes** (the Short Sleeve T-Shirt is 14.99, and 17.99 in big sizes). Every Dickies cell is now the base-size regular price.
  - **Castaway's Yachtsman Crewneck** is 145 compare-at on all five colours, not 175.
- **Other platforms:**
  - **C.P. Company** (Salesforce): every Main Collection and Metropolis listing at `?sz=500`, 215 product pages, and the Stores-FindStores endpoint.
  - **Carmina** (Logicommerce): the `data-product` JSON on all 8 loafer pages (156 loafers), and the physical-locations list.
  - **Closed** (commercetools + Global-e):
    - 221 product pages, for composition, country and the factory note.
    - USD read off the listing tiles after Global-e converted them. The HTML carries EUR, and US prices are set per product, not by one rate.
  - **Danner** (Magento + Constructor.io): the browse API for 365 men's footwear records and 136 apparel records, plus 88 apparel product pages.
- **Style method:**
  - SKU or style stem at Brain Dead, Budd, C.P., Castaway, Closed, Deus and Dickies.
  - Title de-duplication at Danner and Denim Tears.
  - Castaway's stem is model + fabric, so embroidery variants collapse (302 listings become 58 styles).

## Exclusions you should know about
- **Collaborations are out of the style layer:**
  - Brain Dead: 81 of 152 in-stock men's clothing listings (69 styles: adidas, Coach, Brooks Brothers California, A.P.C., UD Ibiza, Magic: The Gathering, Disney and others; re-counted 11 Oct, kids, dresses and skirts left out). The own line is 71 listings / 63 styles.
  - Dickies: 17 styles (Harley-Davidson, Thrasher, Budweiser).
  - Deus: AGTZ and Attaquer.
  - C.P.: Alessi.
  - Denim Tears: the Billionaire Boys Club sweater.
  - Danner: Sig Zane.

  This mirrors batch 1's rule for multi-brand stores. At Brain Dead the collaborations are counted in `styles_total` (132 = 63 own + 69 collaboration) but stay out of the fibre figures, as ruled.
- **Budd's outlet products** (130) can only be seen after logging in to a customer account, so they are not counted. Also excluded at Budd:
  - 332 made-to-measure cloth listings.
  - Studs, bib fronts and waistcoat slips.
  - Zimmerli (third-party).
- **Castaway:**
  - The MENS OUTLET product types are excluded.
  - So are third-party vendors on the store (Murray's Toggery, Smathers & Branson, Holebrook and others).

## Prices: things to know
- **Markdown houses:** Brain Dead, Castaway, Deus and Dickies. The compare-at is filed as the regular price, and the sale price is in the product cell.
- **Budd** sells in USD on its UK store (Shopify Markets, rate 1.35). Feed and page agree on 2 products.
- **Closed is `USD_landed`** (duties included through Global-e).
  - A few models show different USD by colour: Doubleface coat 1340 / 940, Cooper True jeans 425 / 330.
  - No strikethrough was found on the tiles.
- **Shoe cells that are all collaborations are NONE** (ruled 11 Oct):
  - Brain Dead: adidas, Crocs, Coach, Andersson Bell.
  - C.P. Company: ASICS, Moonstar.
- **Shoe-only house.** Carmina is filed like Alan Flusser: seven NONE garment slots and no style table. Its loafers run 475 to 1125. Alligator loafers (3090–3990) are excluded as exotic skin.
- **Danner has no loafer.** Its shoe range runs from a 75 slide to the 540 Danner Light Revival.
- **No footwear sold:** Budd, Castaway, Closed, Denim Tears, Deus (the footwear collection is empty) and Dickies US (the 1,741-product store feed has no shoes).

## Fibre: the headline per house
- **C.P. Company is split.**
  - Synthetic: the jackets and coats (Chrome-R, D.D. Shell, Shell-R, nylon throughout), the tennis kit, and most of the Metropolis Series.
  - Natural: knitwear, tees and polos, sweatshirts, trousers.
  - Overall 65% natural, 35% synthetic, with elastane on 41 styles. Composition was read on 212 of 212.
- **Closed:**
  - 90% natural across 121 styles, 26 with elastane (mostly jeans and stretch trousers).
  - The synthetic-led styles are puffers, track pieces and the fleece-knit sweaters.
  - Every product page states a country.
- **Budd:**
  - Cotton shirting, cashmere knitwear, cotton and silk nightwear.
  - No synthetic-led style.
  - Most compositions name a fibre in prose without a percentage ("2-fold cotton poplin"). 29 of 102 styles name no fibre at all, so coverage is 72%.
- **Denim Tears:**
  - 84% natural (cotton tees, fleece and USA-made denim).
  - The synthetic-led styles are the nylon and polyester jackets, track pieces and fleece.
- **Castaway:** 90% natural. Cotton twill, madras and seersucker, with 2–3% stretch in the twill pants. The house writes "98/2 Cotton/Stretch", and "Stretch" is filed as elastane.
- **Brain Dead** (own line): 79% natural, mostly cotton tees, denim and fleece. The synthetic-led styles are the nylon "Equipment" and ripstop pieces.
- **Dickies:**
  - 69% natural and 21% synthetic.
  - The core work pant and shirt are 65/35 polyester-cotton (874, work shirts).
  - Duck, denim and the newer heavyweight pieces are cotton.
  - 43 styles carry elastane (the FLEX line).
- **Danner** (apparel only): 57% natural (USA-made cotton flannels, duck pants, heavyweight tees) and 43% synthetic (GORE-TEX and fleece jackets, Cordura trail pieces).
- **Deus:**
  - Composition on only 135 of 246 styles (55%).
  - 111 carry-over and markdown listings stated no fibre on two separate reads, so the row is `partial`.
  - Of the styles that do state one: cotton tees and fleece, with synthetic jackets and moto jerseys.

## Doors
- **Brain Dead: 5 US, 7 world.** This counts the Long Beach door, which the brand lists as "BRAIN DEAD @ LONG BEACH RISING". It meets the 10 Oct test (the brand's name is on the listing), but the 6am–10pm weekday hours suggest a shop inside the Long Beach Rising site, so it is flagged. As ruled 11 Oct it stays an own door until something names another operator.
- **C.P. Company: 0 US.** The locator, queried worldwide, returns 23 stores:
  - 19 own doors.
  - 1 outlet (Gotemba Premium Outlets).
  - 3 doors inside department stores (Réel Shanghai, Hankyu Mens Osaka, Osaka Takashimaya), not counted.
- **Carmina: 2 US** (New York, San Francisco) and **9 world**. The Inca store is the brand's own "Carmina Outlet", not counted.
- **Closed: 0 US, 30 world.**
  - 7 of the 30 are women's-only stores, counted and flagged `womens-only` (ruled 11 Oct).
  - Münster and both Zürich stores use operator e-mail domains (viehoff.com, bollag.net), so they are flagged as operator-run.
- **Danner:** 6 US, carried from the counts return. World NC.
- **Denim Tears:** 1 US (Spring Street). The Atlanta residency is filed as a pop-up as ruled; the stores page gives no dates.
- **Deus:** 1 US (Venice) and 6 world. São Paulo uses a deusbr.com e-mail, flagged as operator-run. Canggu has no address on the site.
- **Dickies:** NC as ruled (the locator iframe returns 404).
- **Castaway: 0.** Murray's Toggery is a stockist row, as ruled.

## Stockists rowed
- **Castaway:** 139 shops after duplicates, from its store-locator endpoint.
- **Deus:** the 66 US and Puerto Rico rows of 365 on its stockist.co list. Not rowed: France 136, Indonesia 52, UK 51, Canada 46, and others.
- **Denim Tears:** the 4 Dover Street Market stores.
- **Carmina:** 3 US stockists.

Not rowed:
- Closed: not looked for.
- Danner: about 6,200 Locally markers.
- Dickies: the locator is broken.

Brain Dead, Budd and C.P. publish no stockist list.

## Sections 6–13
- **Craft proposals:**
  - Budd 4: its own Andover workshop is named, with the staff who run it, and product pages name mills (Alumo, Thomas Mason, Loro Piana).
  - Carmina 4: family manufacture on Mallorca since 1866 and a 190-step process, though the factory is claimed rather than shown.
  - Danner 4: an owned USA factory with a factory-tour page, and a country on every apparel style.
  - C.P. Company 3: the garment-dyeing process is documented, and a weaving / dyeing / sewing passport appears on 193 of 212 styles.
  - Closed 3: 188 of 221 product pages name the factory (Pan-Ko, Income, Esvap, Aten, Mundicorte and others). It owns no facility on the evidence read and names no mills.
  - Brain Dead 2, Denim Tears 2.
  - Castaway 1, Deus 1, Dickies 1.
- **Ownership:**
  - C.P. Company: Tristate International S.A., Lugano, from the brand's corporate-information page.
  - Dickies: Bluestar Alliance, from press. The brand's site does not say.
  - Closed: the impressum names only the operating company, Closed Direct GmbH.
  - Danner: not stated on the site.
- **Quotes:** found for 8 of 10.
  - Closed has no about page, so its quote is NONE.
  - Deus's about pages were not reached, so its quote is NC.
- **Vinted:** no brand entry for Budd, Carmina or Castaway.
- **Grailed:** no page for Budd or Castaway.
- **B Corp, GOTS and pronunciation:** NC for all ten, as in batch 1.

## What contradicted the record
- **Carmina's entry loafer is now 475, not 500.** It is the Penny Loafer 80160 Xim. Facts-first saw only 24 of 156 loafers.
- **Budd has an owned workshop** (Andover), which facts-first did not record.
- **Denim Tears' worklist note** says "NYC store", and that holds (Spring Street). The stores page also names Dover Street Market as its only authorised retail.
- **C.P. Company's door list** in facts-first named 10 European stores. The worldwide query returns 23, including Seoul and six in China.

## Rulings applied (11 Oct)
1. **Collaboration-only shoe cells are NONE** at Brain Dead and C.P. Company. The collaboration shoes are listed in the shoe note.
2. **Brain Dead's style layer is own-line only.**
   - `styles_total` is 132: 63 own-line styles plus 69 collaboration styles (81 listings), so collaborations are 52% of the clothing.
   - The fibre figures cover the 63 own-line styles only. The split is stated in `note`.
3. **Brain Dead Long Beach stays an own door**, flagged in `own_doors.csv`.
4. **Budd outerwear is NONE.** The two Safari Jackets and the Chore Jacket are named in `note` so the slot can be revisited.
5. **Closed's 7 women's-only stores count** in the 30. Each is flagged `womens-only` in `own_doors.csv`.

## What the brief got wrong / method notes
- **The Chrome route is now practical for full catalogues.** Rendering the data into the page and reading it with `get_page_text` returns about 40k characters a call, against about 1k in batch 1.
- **One Chrome tab stopped responding** to the extension mid-run. Work continued in a second tab (Brain Dead → Dickies).
- **Dickies product pages break `get_page_text`.** The workaround was to stage the data in sessionStorage and read it from `/robots.txt` on the same origin.
- **Search URLs not tested:** Carmina, Closed and Danner. Closed's search renders client-side. Castaway's search page returns no tiles in the server HTML.
