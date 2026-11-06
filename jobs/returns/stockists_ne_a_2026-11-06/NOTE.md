# NOTE — stockists_ne_a_2026-11-06

Returned 6 November 2026. Files: `return.csv` (7 rows) and this note. Nothing else touched; the map was not opened.

## Status by row

| Row | Shop | Status |
|---|---|---|
| 1 | Britches of Concord | Site read. Brand list is a logo carousel I could not read in full → brand fields `NC`. |
| 2 | Charles Men's Shop | Full. Brand list is the 7 lines named on the Menswear page (a floor, not a certain total). |
| 3 | Englunds Apparel | **Skipped** on Sebastian's instruction after a certificate error and the browser extension failing. Mostly `NC`. |
| 4 | Hassis Men's Shop | Full, except owners/ownership `NC` (no statement found). |
| 5 | Mark Thomas Men's Apparel | Full. Albany door's list read in the same pass; see below. |
| 6 | O'Connell's Clothing | Full. |
| 7 | Valentin's Clothiers | Full, except founded/ownership `NC` (not stated on the site). |

Time box: Britches and Englunds ran over or stalled; I did not time the others.

## What was not reached

- **Englunds:** none of the shop's own pages were read. Address in the row is Saint Croix's. Search snippets mention a 1964 founding and Frank Englund; not used because they are not from the shop's pages.
- **Britches brand list:** the Home page carousels show roughly three logos at a time and cross-fade; clicking the arrow did not advance them reliably. Logos glimpsed (not a list): Ballin, 7 Downie St., Edward Armah, Alan Paine, Bresciani, Piccadilly, Meyer, Pantherella (partly legible), Martin Dingman, Scott Barber, turtleson, Torino, Missani, Royal Highnies, Parsley and Sage, Burgess, St-James, Edinburg Knitwear, Elliott Lauren, Hagen of Carmel, NYDJ. These came from half-faded frames and are **not** counted or matched. A person reading the page frame by frame, or a call to the shop, would settle it.
- **Albany door (Mark Thomas):** the site has one Brands page for both doors and no separate Albany list, so the read of the Albany door is the same 16 names. I did not visit the Albany appointment page.
- Other-door searches were limited to what each shop's own site says. "none found" means the site names none, not that a wider search was done.

## What contradicted the record or other sources

- **Charles Men's Shop, Friday hours:** site says 9:30–7; directories (Visit Genesee, Fresh Air Adventures NY) say Friday to 3pm. Site used.
- **Hassis address:** Delco Today (2021) prints 3335 West Chester Pike; the shop's site and Saint Croix both say 3533. Site used.
- **Britches address:** Yelp and MapQuest show "1 Eagle Sq" (Suite 110 on MapQuest); the shop's contact page says One Eagle Square, Suite #103, 100 North Main Street, which matches Saint Croix.
- **Britches phone:** a 'Call us today' link on the Home page reads (603) 224-4184; the Contact page and footer give 603-225-4184. The Contact page number is the one used in searches and listings.

## Reconcile results (`reconcile.py`)

Exact matches written to `matched_brands`: 
- Hassis: Brax, Peter Millar, Raffi, Southern Tide, plus rewrites johnnie-O (shop: Johnnie-O) and Robert Barakett (shop: Robert Barakat). 
- Mark Thomas: Canali, Brioni, Jack Victor, Raffi, plus rewrite Brax (shop: BRAX). 
- O'Connell's: Allen Edmonds, Barbour, Quoddy, Schott NYC, plus Alden (shop: Alden Shoe; **hand-matched**, `reconcile.py` did not flag it). 
- Valentin's: Allen Edmonds. 
- Charles: none.

**Please rule on two judgment calls:** Robert Barakat → Robert Barakett (spelling differs on the shop's page), and Alden Shoe → Alden. Both are counted in `ub`. Drop them if you disagree and adjust `ub` by 1 in each row.

Names that matched nothing are kept below, unsifted, as the brief asks. Some are probably the same brand under a different spelling or sub-line; I did not guess.

## Full brand lists, per shop (as the shop writes them)

### Britches of Concord
Not captured.

### Charles Men's Shop (7)
34 Heritage; Bench Craft; Ballin Slacks; Grand River; Enro; Robert Graham; Wigens Caps

### Englunds Apparel
Not read.

### Hassis Men's Shop (40) — site Collections page
Alan Paine; Arnau of Spain; Barocci; Brax; Bresciani; Bugatchi; Calder of Carmel; Cardinal of Canada; Emanuel Berg; Fish Hippie; Hagan Shirts; Halsey; Jack of Spades; Johnnie-O; J. Z. Richards; Marbas; Martin Dingman; Meyer/Germany; Mirto; Pacific Silk; Nicoby; Olukai; Peter Millar; Raffi; Remy Leathers; Robert Barakat; Robert Graham; Robert Jensen; Scott Barber; Smathers and Branson; Southern Tide; St. Croix; Tailor Red; Tailor Vintage; Tasc Performance; Tommy Bahama; Toes on the Nose; True Grit; Turtleson; Zelli

(The list includes **St. Croix**, which is the brand Saint Croix. Not matched to any canonical key.)

### Mark Thomas Men's Apparel (16) — both doors
Canali; Brioni; Jack Victor; Stenstroms; Magnanni; AG Jeans; Robert Graham; David Donahue; Paul Betenly; BRAX; Torino; BALLIN; DOLCEPUNTA; GIMO'S; JOE'S; Raffi

### O'Connell's Clothing (34)
Albert Thurston; Alden Shoe; Allen Edmonds; Armin Oehler Shoes; Atkinsons; Barbour; Bills Khakis; Bresciani; Chester Jefferies; Chrysalis; Draper of Glastonbury; Geo. Trumper; Gottmann Caps; H. Freeman & Son; Jill McGowan; Kal Rieman; Kent Brush; Lesley Evers; Mackintosh Ireland; Marcoliani; Quoddy; Robert Jensen; Robert Talbott; Rochester Tailored Clothing; Royall Fragrances; Schneiders of Salzburg; Schott NYC; Seaward & Stearn; Shinola; Smathers & Branson; Southwick Clothing; St. John's Bay Rum; Viyella; Wigens

### Valentin's Clothiers (14) — Suppliers page (names from logo alt text)
Hickey Freeman; Prive; Bresciani; Baroni; Geoff Nicholson; Trafalgar; Stetson; Allen Edmonds; Max Davoli; Sartoria Tosi; Punto; 7 Downie St.; Chiari; Maceoo

## What the brief got wrong or left unclear

1. **Schema vs template.** `schema.json` lists `sku_on_shop_site` and `mollusk_on_shop_site`; `return_template.csv` omits them. I followed the template. Both can be added as `NC`.
2. **Type values differ.** The brief says menswear specialist, boutique, outfitter, department store; `schema.json` says menswear specialist, boutique, department-like, other. Every row here is "menswear specialist", which is in both.
3. **`NC` has two meanings.** The brief says `NC` means nobody looked, and also tells me to write `NC` when a shop publishes no list. Those are different findings. I used `NC` for both and put which one applies in `note`. Consider a separate value such as `NONE_PUBLISHED`.
4. **`ub`/`matched_brands` when nothing matches.** Charles has `ub` 0 and `matched_brands` "none", since empty cells are errors. A validator may read "none" as a brand name.
5. **Logo-only brand lists.** Britches publishes its list as image carousels, which this kind of read can't capture. The brief only offers a text list, vendor filter or a "no list" fallback. A fourth case is worth naming.
6. **"Read only. Don't sign in…"** fits, but the browser's certificate error on Englunds is the sort of thing the brief doesn't cover (I did not click through the warning).
7. **Mark Thomas "Albany door's brand list in the same pass":** the site shares one list across both doors, so the extra read produced no new information.
8. The `source` column wants "one source per row"; I gave the page the brand list or key facts came from, and put other pages in `note`.
