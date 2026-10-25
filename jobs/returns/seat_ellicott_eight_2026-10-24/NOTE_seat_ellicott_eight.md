# NOTE: seat_ellicott_eight_2026-10-24

Files: `return.csv` (8 rows x 132 columns, validated: header matches template, no empty cells, all names exact on `reconcile.py`), `own_doors.csv` (9 rows), `stockists.csv` (404 rows), `return_styles.csv` (313 rows), plus `facts_first.csv` sent earlier. All read 24 Oct 2026, read-only, men's range only. Each brand was read by a separate research thread; I spot-checked the American Trench Ardmore store and the Peregrine/Ellicott match myself. Per-brand notes with sources are in the working folder and can be sent on request.

## Rulings needed from Sebastian
| Brand | Proposed craft | Open question |
|---|---|---|
| TOPO Designs | 2 | Seat or bench: men's clothing is 86 of 263 styles in the whole catalog (32.7%), but 79 of 87 (90.8%) of its men's pages (bags are unisex and sit outside them). |
| Peregrine Clothing | 4 | Owns the Manchester knitwear factory (own claim plus press; no filing seen). |
| Soft Goods | 4 | Own Detroit factory, backed by American Manufacturing (20 Aug 2026), CFDA directory and MEDC 2023; building ownership unproven; knitting and dyeing outsourced, no mill named. |
| American Trench | 3 | Many mills named; no owned facility. |
| Bridge & Burn | 2 (arguably 3) | British Millerain named on two jackets; graphic tees say USA yarn-to-finish. |
| SeaVees | 2 | Made in Vietnam, factories unnamed. |
| Lems | 2 | Assembled in China (press adds Cambodia); no factory named. |
| Nisolo | 2 | See ownership below. |

Also for you: American Trench founding year (2013 vs 2012); the band guesses in `facts_first.csv` (no band definition was supplied); Topo mark ("Topo Designs" as the site writes it vs "TOPO Designs"); and whether Lems' $25 unisex tee, sold alongside its shoes, should fill the tee slot (left NONE per the standing shoe ruling).

## Contradicted the brief or my earlier return
- **American Trench has an own store** (15 E. Lancaster Ave, Ardmore, PA 19003, called its "flagship storefront"; opened mid-Nov 2023 per Main Line Today). My earlier `own_store` of NONE was wrong; `return_brands.csv` is corrected. Its page hours conflict with its footer. Founding: About page gives none; trench coat introduced 2013; Philadelphia Citizen and Main Line Today say 2013 (Kickstarter); only FashionUnited says 2012. Entered 2013. Vestis and Ardmore are not on its stockists list; Ellicott, Franklin & Poe, Weitzenkorns and Soft Goods (Detroit) are. 310 stockists, no street addresses.
- **Nisolo has changed hands and lost its Peru factory.** Nisolo LLC defaulted and went into foreclosure in Jan 2025; nisolo.com's FAQ says Project Bound Inc. bought it, Modern Retail (1 Dec 2025) says IRL Ventures did (both recorded; you rule). The Trujillo factory was closed by Jan 2025 per Eco-Stylist; now made in Mexico, Brazil and Europe via certified partners. B Lab told Eco-Stylist (30 Sep 2025) it is no longer B Corp certified; directory search returned 0. No store on nisolo.com (/pages/stores now redirects to a 404); a 2023 FashionUnited article lists Nashville, Boston, DC and NYC, unconfirmed. My earlier "owned facility" reading from press was out of date. Founding (Nashville, 2011) is press-only.
- **SeaVees:** the About page says the brand closed in 1971 (not 1972) and the vintage pair was found in a Tokyo secondhand store in 2005 (relaunch 2008). The agent could not find a city for 1964; I did see "launched in California in 1964" on seavees.com's homepage, so that line is the brand's own, city unstated. Shoes basis is a `pair` of loafers: Carmel $120 and Hayward $140, both marked-down lines (the alternative is a range of $80 to $225). Pentland Brands invested in 2017; share unknown; Steven Tiller founder/CEO. Made in Vietnam per help.seavees.com (one product page checked).
- **Lems:** original city is Farrell, Pennsylvania (brand's own "We're moving!" post); Boulder from Jan 2016. The post says it "began back in 2010"; Our Story says first product Sept 2011 (used 2011). Own stores 0: the "Pedestrian Shops" image is an independent retailer. Shoes are a `range` $105 (Drifter) to $235 (Tactical Pro Tall Boot) as there is no loafer.
- **Soft Goods:** own stores 0. The Topo Designs x Soft Goods label tee was not in its feed on 24 Oct, so it is excluded. Internal conflicts: dyeing in South Carolina (Factory page) vs NYC (hoodie page); address 1927 Rosa Parks Blvd (brand) vs 1314 Holden St (CFDA); Classic Tee 190 GSM vs 305 GSM; two months vs 100+ days to perfect the tee. It is unisex (no men's split), 14 branded clothing styles; tee pair $78/$88; sweater is NONE (sweatshirts only); the $248 item is the French Terry Hooded Robe.
- **Peregrine Clothing:** confirmed the UK house (Ellicott's Bexley Jacket is $440 and so is peregrineclothing.co.uk's). All prices are `range`, USD storefront (confirmed on Bexley $440, Scout Coat $632, Classic Tee $72). Made-in is stated on every men's page: 54 UK, 10 Portugal, 5 Spain styles, which conflicts with "all our clothing is made right here in the UK" and Tom Glover's "100% in England" in press. Own doors 0 US; a Regent Street store from 2021 press is unconfirmed; one Selfridges shop-in-shop counted as a concession, not an own door.
- **TOPO Designs:** four own stores confirmed with addresses (Denver Flagship opened Nov 2013), not two. Collection counts on its site are inflated (mens-tee-shirts says 114, serves 30). Gart Capital Partners invested in March 2023. Men's sweaters, polo, jeans and shoes are NONE.
- **Bridge & Burn:** the story page's 2009 is the hoodie idea, not the tee line; 2010 launch confirmed. Own doors: Portland and Bend (the LA store is gone). 45 stockists including Ellicott. Third-party items excluded (Jungmaven, Corridor, American Trench, Hiroshi Kato selvedge jeans $238 to $258).

## NC or thin across the batch
- **GOTS:** the global-standard.org database would not load for most brands (NC). B Corp is NONE for TOPO, Bridge & Burn, Soft Goods and Peregrine on fuzzy name searches (thin evidence).
- **proposed_tech** is NC everywhere: the folder has no tech rubric.
- Vinted brand ids mostly NC (SeaVees id 934507 read from filter state, unconfirmed). Pronunciation NC for most.
- Lookbooks: Bridge & Burn and TOPO NONE (not found); American Trench newest is O.E. FW23.
- Quotations: several are from undated pages, so the read date is used.
- Press details for Soft Goods came from fetched summaries, not raw page reads.

## What the brief got wrong
- It gave no definition of "band", no tech rubric, and its sweater/tee/dress-shirt garment list does not fit TOPO, Soft Goods or the shoe houses; stand-ins (casual button-ups for dress shirts, casual pants for dress pants) are labelled in each row.
- Its own-store premise for American Trench, Nisolo and Lems was off in three different directions (see above).
