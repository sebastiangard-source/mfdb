# prices_womens_2 — follow-up pass (14 Oct 2026)

This pass replaces `return.csv` in full: still 29 rows, and `reconcile.py` matches all 29 exactly. 28 brands are now read, and Kartik Research is unchanged (no women's range on its own store).

## LOFT: read (was `NC`)

- **How it opened.** I loaded the homepage normally and clicked the visible "Sweaters" chip. There was no challenge and no press-and-hold, and I didn't use a cache, sitemap or any other workaround. After that, category URLs loaded directly.
- **Read.** Category-stratified, as the brief allows: price-sorted listings, plus product pages for the key figures.
- **Band: Basic.** The core tee is the Everyday Crew Tee at $29.95 and the core shirt is the Everyday Dolman Shirt at $59.95 (woven, 100% cotton). Both are under the cuts.
- **Prices.** Nearly every LOFT product shows "50% OFF! PRICE AS MARKED" or final sale, so every figure is the struck-through regular price. The exact figure is in the product cell, rounded half-up.
- **The core shirt may rotate out.** The Everyday Dolman Shirt is final sale. The next woven shirts are $54.95–$59.95, so the band holds either way.
- **Where the brief would have produced a confident wrong answer.** loft.com is partly a marketplace. Taken at face value, these would have come from other brands:
  - the sweater high: Haven Well Within cashmere, up to $398
  - the dress high: Rebecca Taylor, up to $495
  - the tees: Junk Food and Wild Collective
  - the shoes: Sorel and Sperry

  I excluded those and kept Rivete (LOFT denim), LOFT Versa and Lately as sub-lines.
- **Trousers** come from the Palmer fit category ($84.95–$99.95), because the low end of the full Pants listing is shorts.
- **Dress high** is from the Lately occasion line. I couldn't isolate LOFT's own top day dress from the marketplace listings.

## Flags resolved

- **RIXO.**
  - Blouse high is now Moss (100% silk crepe de chine, $315), replacing the bridal-edit Adeline ($570).
  - Sweater is now crewnecks only, from product pages: Emerson $345 to Anderson $415. Both are wool blends, so the basis is range.
  - Band mean is now $285. Still Accessible.
- **KALLMEYER.** The "Cashmere Wool" Nina crew is 70% merino, so it isn't majority cashmere and the sweater basis changes from pair to range. None of its knits are majority cashmere. Band unchanged.
- **MAISON MAYLE.** The only tee is the brand's own graphic slogan print. There's no plain tee.
- **Sanderlak.** The alpaca share of the Split Crewneck isn't published ("Italian wool-and-alpaca melange"), so it stays range.
- **Still open: Sam Edelman Croc Jacket material.** Cloudflare challenged the product page on both tries today, so I left it. The note already names the faux-fur and faux-shearling alternatives.

## Verification

I checked every Shopify-sourced figure in the return against its live product endpoint (`/products/<handle>.js`): 260 URLs across 21 brands. All return 200, and the regular price matches the cell at whole-dollar rounding. The only item that can't be bought is the Suzie Kondi Kyma Coat, which the row already flags as sold out. Currency was USD on every store, including Le Monde Béryl and RIXO's US market.

The seven non-Shopify brands (LOFT, Gianvito Rossi, Manolo Blahnik, Roger Vivier, Aquazzura, prAna, Sam Edelman) were read from their live pages in the first place.

## Second follow-up (14 Oct, later)

- **Sam Edelman Croc Jacket: resolved.** The product page source (fetched from the store after the homepage loaded) gives "Shell Face Polyurethane, Shell Back 73% Viscose". It's faux croc, not an exotic skin, so it stays as the outerwear high.
- **LOFT dress high: replaced.** I removed the marketplace brands and the Lately occasion line from the high-to-low dress listing. The top LOFT day dress is the Poplin Bustier Midi Pocket Dress at $110 regular. That replaces Lately at $150, and the band is unchanged (Basic).
- **prAna blouse low: corrected.** The Cambria Cove Button Up Top ($58) turns out to be a ribbed cotton-stretch knit, not a woven shirt. The low is now the Mountain Maven Denim Shirt ($78). The mean becomes $83, still Premium.
- **prAna's bot wall is back.** PerimeterX turned on during that check ("Access to this page has been denied"), so I stopped there. The Railay button-down ($78) couldn't be opened, and the figure above comes from the category listing read on 13 Oct.

Nothing is left unread. The remaining items are rulings for the Spectrum thread, all set out in the notes:

- leather outerwear as a high
- Gianvito Rossi Rania vs Yuna
- the Wiederhoeft runway tee
- whether Sanderlak and Kartik Research belong on the women's map
- the four proposed bands (Suzie Kondi, We Norwegians, Miguelina, Wiederhoeft)
