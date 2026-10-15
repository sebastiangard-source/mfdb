# Batch 01 — womens_dials_2026-10-14, thread 1

Read 14 October 2026, in Chrome, on each brand's own US store. This batch is the pilot (audit protocol §6). Batches 02–05 have not been started. They wait on review of the points below.

`reconcile.py`: 10 names in, 10 exact, 0 to rewrite, 0 unmatched.

## What came back

| brand | status | styles (with comp.) | nat / syn / cell % | spandex | shape | denim·cash·linen·cotton·wool·synth·silk | tech | craft |
|---|---|---|---|---|---|---|---|---|
| Chico's | partial | 80 (80) | 40 / 29 / 31 | 35 | split | 3·2·2·4·1·4·1 | 3 | 1 |
| LOFT | read | 76 (76) | 58 / 30 / 12 | 20 | split | 3·2·3·5·1·4·1 | 2 | 1 |
| Talbots | read | 79 (79) | 67 / 24 / 9 | 34 | one | 3·2·1·5·2·4·1 | 3 | 1 |
| White House Black Market | read | 80 (80) | 22 / 59 / 19 | 60 | split | 3·1·1·4·1·5·1 | 3 | 1 |
| J.Jill | partial | 80 (42) | 31 / 5 / 16 | 20 | one | 2·1·1·4·2·2·1 | 3 | 1 |
| Soma | read | 79 (79) | 32 / 22 / 47 | 58 | one | 1·1·1·4·1·4·1 | 2 | 1 |
| Athleta | partial | 80 (80) | 9 / 74 / 18 | 67 | split | 1·1·1·3·1·5·1 | 4 | 1 |
| Anthropologie | partial | 80 (79) | 56 / 26 / 16 | 28 | split | 3·2·2·5·2·4·1 | 2 | 1 |
| Aerie | partial | 80 (80) | 59 / 38 / 4 | 56 | split | 2·1·1·5·1·4·1 | 4 | 1 |
| Free People | partial | 80 (79) | 69 / 16 / 14 | 19 | one | 3·1·1·5·1·3·2 | 2 | 1 |

In this table, `partial` means at least one cell is `NC`. The `note` column in each row names the cells.

- **Craft is 1 for all ten.** None of these brands names a maker, a mill or a facility on any product page I read. Almost every page says only "Imported". The only made-in lines were 2 of 80 sampled at Anthropologie ("USA") and 4 of 80 at Free People. Chico's (1983, Sanibel Island) and Talbots (1947, Hingham) give a dated, placed founding, but in both cases it is a shop's or a catalogue's founding, not a maker's.
- **Tech:** Athleta and Aerie (OFFLINE By Aerie) are 4. Athleta could be a 5: every fabric block I checked carries a performance claim, but its fabric families (Salutation, Elation, Seasoft…) carry no fabric trademark on the page. Chico's, Talbots, WHBM and J.Jill are 3, for house-named cloths in part of the range (Travelers™, AirKnit, FORME™, Wearever).

## Contradicts the worklist

- **Chico's has no shoes.** The worklist has `shoes_sold = yes`. The only footwear-adjacent node is Jewelry & Accessories (938 items), and it holds no shoes. A site search for "shoes" returns clothing. I filed the cell as `NC`, not `NONE`, so the Spectrum thread can rule.
- **Aerie outerwear:** 11 jacket styles exist (product path `tops/jackets`), but there is no jackets node in the Aerie navigation, so the cell is `NC`.

## Not reached, or read with less than the playbook asks

- **J.Jill:** 38 of 80 sampled PDPs state no composition, almost all of them sale handles ending `s-1`. I checked one in the live tab, and the rendered page has no fabric block either. The percentages are of all 80, so every J.Jill share and dial is understated.
- **Aerie:** compositions come from the JSON-LD `material` field. The visible Materials & Care accordion rendered only on the first PDP, where it matched JSON-LD exactly. On later pages it stayed out of the DOM. So this is validated on 1 page, not the 10 the playbook asks for.
- **Heritage was not read** for Athleta, Anthropologie, Aerie or Free People, which is why those craft rows are `partial`. All four still sit at 1 on product-page evidence alone.
- **Anthropologie and Free People are page samples, not full censuses.** I read tiles from two or three pages per category, weighted by each category's own count.
- **The time box is far off for browser-only sites.** I averaged well over 35 minutes a brand, mostly on the bot-walled stores, where every PDP has to be an ordinary page load.

## Bot wall (LOFT)

My first background `fetch` of a LOFT category page returned a PerimeterX "Press & Hold" page, and I did not attempt it. One plain retry later in the ordinary tab loaded normally. After that, LOFT, Anthropologie, Free People and Aerie were read entirely by ordinary page navigation, one page at a time. I did not use the robots.txt ruling.

## Where the brief needs a ruling

1. **Multi-brand stores.** Anthropologie is a stockist: only 28 of 80 sampled styles are its own labels (Maeve, Pilcro, By Anthropologie, Daily Practice, BHLDN). At Free People, 20 of 80 are third-party (MOTHER, AGOLDE, Diesel, Barbour…). The dials here describe the store's assortment. If they should describe the house's own labels only, the style rows let you re-cut without re-reading: own labels and third-party brands are tagged in `lines`.
2. **The category set is the men's set.** For women's tops, I filed knit tops, tees, tanks and camis under `tees-polos`, and woven blouses, shirts and tunics under `shirts`. Skorts are filed as `skirts`, and a house "Activewear" or "Tunics" node is split by garment. Each moved row says so in `note`. A `tops` category (or `blouses`) would be cleaner.
3. **`fab_denim` is not a fibre.** I set it from the share of sampled styles that are denim garments (category `denim`, or "denim" in the title), not from lead fibre.
4. **Sampling and the roll-up.** `styles_total` and every percentage are counts of the style table returned, which is the stratified sample of up to 80. The site's own total is in `sample_basis`. The `shape` test asks for a category with 10 or more styles, which a sample rarely reaches, so I used 5 or more sampled styles.
5. **Scope at the lingerie brands.** At Soma I read only the Apparel node (lounge tops, bottoms, leggings, sweaters, wraps, dresses). At Aerie I read the clothing tree without bras, undies or pajamas. I excluded sleepwear as nightwear. Say if it should be in.
6. **`rules_craft.md` asks for a table of proposed ≠ current, largest moves first.** The worklist carries no current craft score or reason, so I could not build it.
7. **`rules_fibre.md` asks for six files; the brief asks for three.** I returned the brief's three. The category, fibre and line tables can all be derived from `return_styles.csv`.

## Parsing traps found (all fixed before return)

- **Fibres must be summed.** Two parts of the same fibre must be added before choosing the lead: "40% Recycled Cotton, 17% Cotton, 43% Lyocell" leads cotton at 57, not lyocell.
- **Run-together labels.** "Contents95% Cotton, 5% ElastaneOriginImport" (Free People) lost the second fibre until camel-case words were split. I re-read the 12 affected pages.
- **Abbreviated fibres.** One Aerie composition is written "55% Ctn, 35% Rec Poly, 7% Nylon, 3% Elstne".
- **Marketing copy ahead of the real line.** At Soma, "38% TENCEL branded lyocell fibers" sits ahead of "58% Cotton, 38% TENCEL Lyocell, 4% Spandex".
- **LYCRA® T400® is not elastane.** It is filed as elastomultiester and does not count in `spandex_styles`.
- **Compositions that don't sum to 100 are filed as written** and flagged in `note`. There are 10 (e.g. WHBM's High-Rise Flare Jean at 95).

## Out of scope but noticed

- Talbots and LOFT are both Knitwell Group stores and both sell Haven Well Within.
- Chico's, WHBM and Soma run on one platform: the same `/store/category/…/catNNN` and `/store/product/…` patterns, with the composition in a description `<li>`.
