# NOTE: stockist_ellicott_2026-10-24

Returns: `return_shop.csv` (1 row) and `return_brands.csv` (10 rows). Scope per Sebastian: the ten photo brands only. I added no extra names from the shop's full list.

## What was checked
- Shop record read from ellicott.co (About, Brands page, footer) on 24 Oct 2026, plus three press pieces on owners and opening.
- Brands page lists **104 entries (103 distinct; Penguin Random House appears twice)**. Most are not clothing (books, candles, food, barware, tobacco, games).
- All six map brands confirmed on the shop's own list: Red Wing Shoes, Taylor Stitch, Marine Layer, Nudie Jeans Co, Pendleton, Filson.
- Each of the ten brands was read on its own site, except Power Goods (no own site found).

## Verdicts
Seat: SeaVees, Soft Goods, TOPO Designs, Nisolo, Peregrine Clothing, American Trench, Bridge & Burn, Lems (footwear: SeaVees, Nisolo, Lems). Bench: Power Goods. Reject: Ellicott & Co. (house label).

## Contradicted the existing record
- **TOPO Designs** has four own stores on its own locator (Denver flagship, Fort Collins, Denver Base Camp, San Francisco Hayes Valley), not just Denver and Fort Collins.
- **American Trench**: the brand's current stockists page lists Ellicott, Franklin & Poe and Weitzenkorns, but not Vestis and not Ardmore. I did not check the Imogene + Willie page.

## Not reached or unresolved
- **Power Goods:** powergoods.com is a parked domain; powergoods.co.uk would not load. No brand-owned site, so it is benched. I could not open Ellicott's own Power Goods product, so the namesake check against the shop's product is not done.
- **Peregrine:** the namesake check against Ellicott's product was also not done. The site found is the UK knitwear house.
- **Nisolo** founding year (2011) rests on press, not its own site; a Nashville store is mentioned by Entrepreneur but nisolo.com has no store locator.
- **Soft Goods** stockists page could not be read; own stores unconfirmed.
- **Lems:** the company's origin city before Boulder (moved 2016) is not given.
- Ellicott's opening month: 2016 comes from a 2022 Lancaster Online piece; the 2016 opening article would not load.
- `gender_at_shop` is `mens` for all brands because the shop calls itself a men's shop; I did not check each brand's product by gender on the shop's site (`both` for TOPO reflects its own lines).

## What the brief got wrong
- `reconcile.py` does not match "Red Wing Shoes" to the map's "Red Wing" (similarity falls below its 0.85 cutoff), though the brief says it does.
- `reconcile.py` wrongly proposes THEORY11 (a playing-card maker) -> "Theory". Do not accept that rewrite.
- The brief's `own_store` asks for a count; `schema_brands.json` says URL or NONE. I gave a count plus the locator URL, or NONE.
- The shop's brand pages are not at /pages/brands/<name> (they return the generic Brands page), so shop-side product checks needed another route.
- About 87 other names on the shop's list are not on the map, mostly non-clothing. They were left unsifted per Sebastian.
