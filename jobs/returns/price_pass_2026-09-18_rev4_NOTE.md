# price_pass_2026-09-18 — rev 4 restatement return

`return.csv` holds **112 rows** after the 19 Sep merge (see the last section): 25 rows from the rev 4 restatement plus the audit restatements, all 24 columns, with `SKIP` in every cell not being restated. Names reconcile: 112 exact, 0 rewrites, 0 unmatched. There are no blank cells, and the enums and integer ranges are legal. The one exception is the `NONE` token in `search_url` (see "What this brief got wrong", item 4).

## What was checked

**1. No fur or exotic skin: the four named rows**

| Row | Cell | Was | Now | Notes |
|---|---|---|---|---|
| Stefano Ricci | outerwear_high | 53,700 | 12,300 | Cashmere and shearling blouson. Re-read today: no fur, no exotic. The $25,800 vicuña-silk blouson has crocodile inserts listed only on its product page, so it's excluded too. |
| Stefano Ricci | shoes_high | 17,550 | 2,100 | Suede loafers. Every dearer loafer is exotic. |
| Loro Piana | outerwear_high | 29,000 | 29,000 | Unchanged. Tyton Bomber is 98% vicuña / 2% cashmere with plongé leather trim, so vicuña as fibre, not fur. |
| Hermès | shoes_high | 5,150 | 1,925 | Icone loafer (calfskin). Re-read live in the follow-up; confirmed. |
| Sid Mashburn | shoes_high | 895 | 595 | Italian Penny/Tassel loafer. Re-read live in the follow-up; confirmed. |

**2. No fur or exotic skin: the same ruling applied to seven rows the brief didn't name**

The earlier notes show fur or exotic figures in these rows too, so I restated them.

| Row | Cell | Was | Now | Notes |
|---|---|---|---|---|
| Zilli | shoes_high | €4,320 | €1,380 | Re-read today. The €1,800 and €1,575 moccasins have caiman trim, so they're excluded as well. |
| Dolce&Gabbana | outerwear_high | 13,500 | 8,445 | Nappa leather bomber, re-read today. The brand names the old piece "Fur bomber", and it's also an FW26 runway piece. |
| Visvim | outerwear_high | 8,400 | 13,875 | Winfield Coat excluded (Visvim calls its collar and liner "Uzbekistan Sheepskin Fur"). The follow-up re-read found Strabler Jkt IT ($13,875, horsehide) filed under a small "IT" category; 6,740 if "IT" pieces don't count. |
| Brioni | outerwear_high | 15,000 | 10,400 | The old high had alligator details; the new high is the same style in nubuck (100% leather). Re-read live; confirmed. |
| Kiton | shoes_high | 2,540 | 2,530 | The old high had crocodile inserts. Re-read live; confirmed. |
| Valentino | shoes_high | 1,350 | 1,190 | The old high was eel skin. Re-read live; confirmed. |
| Ferragamo | shoes_high | 2,900 | 1,590 | The old high was crocodile. Live re-read: the $2,500 Tramezza penny is python and the $1,750 Caspian Lux has alligator; the new high is the Tramezza penny loafer in calfskin, $1,590. |

Checked and left unchanged:

- **Rhude:** the $4,110 "Blue Crocodile Pilot Jacket" is croc-*embossed* leather with a Sherpa collar.
- **Tom Ford:** the high loafer is "Soft *Printed* Alligator", i.e. printed, not exotic. Not re-read today.

**3. Sub-lines**

| Row | What changed | Cells |
|---|---|---|
| Fear of God | Whole row restated with ESSENTIALS included | polo NONE → 115/165; dress shirt 695 → 135 low; sweater low 990 → 175; shoes low 195 → 150; outerwear unchanged; `not_a_staple` Polo → `-` |
| Maison Margiela | MM6 is sold on the US store, so it's included | sweater low 960 → 560; outerwear low 3,100 → 1,425; shoes low 1,450 → 780 |
| Rick Owens | DRKSHDW (305 men's products on the US store) had been excluded; now included. Not named in the brief — found in the sub-line check. | outerwear low 2,090 → 1,875 (DRKSHDW BRAD in canvas; the Brad style's leather high stays 3,225); shoes low 935 → 685 |
| Y.Chroma | Drücken line counted | outerwear low 775 → 399 (Drücken Track Jacket) |

Other sub-lines I checked were already included: Ghost, Crown Crafted, &Kin, Blue Tab, BOSS Camel, Herno Resort, Tramezza, MHL, s/SACAI CLASSICS.

Polo Ralph Lauren's Purple Label loafers remain excluded. "Ralph Lauren Purple Label" is its own canonical key, so it isn't a Polo sub-line.

**4. Fibre ruling**

Moncler sweater high 1,085 → 1,195, and the row becomes `range sweater`. Its only cashmere crews are 10% blends, which no longer count. The new high is the Grenoble Moose sweater at 43% alpaca, which is not a majority either.

**5. Fedeli**

Re-read on the US storefront (`/en-usd/`); two feed prices matched the displayed page. Sweater 420/1,752 and outerwear 3,005/4,328, all USD.

The small moves from 18 Sep (1,750 → 1,752 and so on) come only from Shopify's exchange rate, which went from 1.170348 to 1.1712558. Most US prices are automatic conversions of the EUR list, rounded up to the dollar: €1,495 shows as $1,752. The permanent "iconic colors" items instead have a fixed USD price ($420 vs €390). **These cells will drift by a few dollars on every pass.**

**6. The five blocked houses**

- **Celine** was read through the web-fetch tool: sweater 1,050/1,950, outerwear 1,500/8,700 (teddy jacket, fleece → calfskin), shoes 950/1,300. **Method caveat:** that tool returns page text through a summariser that was asked to quote verbatim. It is not a direct page read. The knitwear page was read twice with identical results.
- **Saint Laurent, Gucci, Balenciaga and Bottega Veneta** are still `NC` (status partial). The exact blocks are in each note:
  - the browser extension dies as soon as the page loads;
  - web-fetch returns `SITE_BLOCKED`;
  - the sandbox's egress proxy blocks direct requests.

  A fresh browser profile with the extension off isn't available to this thread. The listing JSON sits on the same blocked domains.

**7. Search URLs**

- **Ring Jacket:** `https://www.ringjacket.co.jp/p/search?keyword=` is filled.
- **Indochino and Ferragamo:** `NONE`, because each has overlay-only search with no URL form.
- **Golden Goose:** still `NC`. Every garment word returns "NO RESULTS (0)", including sneakers, jacket, jeans, denim, t-shirt, hoodie and shoes. "super-star" works only because it redirects to a category page.

**8. Wave-1 currency spot-check**

I checked ten US-based Shopify rows, two figures each. Each time I read the feed and the displayed product page (og/ld price). **Nothing moved.** All ten stores report USD at rate 1.0.

- **Held cleanly:** Rothy's 125/185, Alo 188/298, Taylor Stitch 178/1248, Outerknown 178/348, Faherty 278/1500, AYR 595/1400, Alex Mill 178/358.
- **Held under the compare-at rule only:**
  - **Everlane 98:** the No-Sweat Sweater sells at $29 in every colour, and the $98 compare-at predates Everlane's repricing.
  - **Southern Tide 158/178:** both products are marked down (to $99.50 and $79.50).
  - **Industry of All Nations:** the page shows $280, the lowest variant, against the filed 300 (the max-variant rule). The Andes Coat is on sale at $495 against its $745 regular price.

## What was not reached

- **Four houses:** Saint Laurent, Gucci, Balenciaga and Bottega Veneta. See section 6 for the blocks.
- **Golden Goose search URL.**
- **Not re-read:** none; the six note-derived figures were re-read live in the follow-up.

## What contradicted the existing record

- **Rick Owens** had excluded DRKSHDW, a second sub-line case beyond Fear of God.
- **Seven rows had fur or exotic highs that the brief didn't list** (the table in section 2).
- **Zilli's loafer listing** now shows 24 unique products; it showed 20 on 18 Sep.

## What this brief got wrong

1. **The fibre ruling reaches well beyond the named rows.** "Elevated" now includes alpaca, mohair, silk and superfine wool, and only majority-cashmere blends count. So every row filed under the old reading needs another look:
   - The 33 `range sweater` rows, which were ranges because they had "no cashmere crew": Southern Tide, Rhoback, Taylor Stitch, Outerknown, Finisterre, Faherty, Carhartt, Lacoste, Lululemon, J.Lindeberg, johnnie-O, RLX, Tecovas, Baracuta, Filson, Y.Chroma, Kith, Aimé Leon Dore, RRL, Scotch & Soda, PAIGE, AG, Ksubi, Maison Margiela, Yohji Yamamoto, Sacai, McQueen, JW Anderson, Fear of God, Palm Angels, Lemaire, Dries Van Noten, Wales Bonner.
   - Rows whose high is a minority-cashmere blend: A.P.C. (wool-cashmere, 650) and Alo (Wool Cashmere New Class, 298; cashmere share not confirmed today).
   - Loewe's cotton-silk crew ($1,650), which was excluded.

   Only Moncler was restated. **This needs a scope decision** before anyone re-reads 35+ rows.
2. **The fibre rule still has gaps:**
   - Is the majority test for cashmere only? Moncler's 43% alpaca was treated as not elevated.
   - Does "extra fine wool" count as superfine wool? Moncler's $1,055 sweater uses it.
   - Is silk counted as a majority or as any blend?
3. **Fear of God's ESSENTIALS polos have elbow-length sleeves,** and two are called "3/4 sleeve". If only true short-sleeve polos count, polo is 125/125.
4. **`NONE` in `search_url` breaks the column's `url` type in `schema.json`.** I followed the brief, so `validate.py` will reject those 2 cells until the schema allows the token.
5. **The "any garment word" search test passes Ring Jacket trivially.** "jacket" matches the brand name in every product title (215 hits, mostly shirts and ties). "coat" returns 2 relevant coats, which is the better evidence.
6. **The fresh-profile route in item 4 isn't available to an audit thread.** The four houses need a human read or a different browser.
7. **MM6's $1,425 "Hooded bomber jacket" is described as a nylon puffer.** If puffers don't count as the bomber style, the MM6 outerwear low is $1,655.
8. **"Shearling allowed unless named fur" needs a rule.** Rhude's Sherpa collar and D&G's "fur-making" lambskin show the line depends on the brand's own naming.

## Follow-up (same day): live re-reads, Golden Goose, manual-read workbook

- **Every figure previously taken from an earlier note has now been read live:**
  - **Confirmed, no change:** Hermès shoes 1,100/1,925; Sid Mashburn 595; Brioni 10,400 (100% leather nubuck, no exotic trim); Kiton 2,530; Valentino 1,190.
  - **Ferragamo shoes_high 2,500 → 1,590.** The $2,500 Tramezza penny loafer is python. The $1,750 fallback (Caspian Lux) is calfskin and alligator, and the $2,200 Gancini moccasins are crocodile. The new high is the Tramezza penny loafer in calfskin at $1,590.
  - **Visvim outerwear_high 6,740 → 13,875.** The earlier read missed two leather jackets that the store files under a small "IT" category rather than Outerwear. The new high is Strabler Jkt IT, $13,875 (horsehide, water-buffalo buttons). Mahon Jkt Suede IT is $10,017. If the "IT" pieces shouldn't count, the high is back to 6,740.
- **Celine:** the browser is still blocked (Akamai Access Denied, ref #18.ec7dd17.1789764020.33c9ec9). The row is now marked partial and "NOT VERIFIED LIVE", and it's in the manual-read workbook.
- **Golden Goose:** search_url stays NC. The URL Sebastian supplied is a category listing (men's shirts, 19 products), not a search page, so a garment word can't be appended to it. Every search route tested returns 0 results: the search page, Salesforce's Search-Show endpoint, and `?q=` on a category page. The clean category URL, with tracking stripped, is recorded in the row's note.
- **`manual_read_blocked_houses.xlsx`:** a fill-in workbook for Saint Laurent, Gucci, Balenciaga, Bottega Veneta and a Celine check. It has instructions, a worked example row (Loro Piana) and a self-checking status column.

## Fibre re-check (proposed; `fibre_recheck.csv`, not merged into return.csv)

36 sweater rows were re-read live under the rev 4 fibre rule. These were the 33 filed as `range sweater`, plus A.P.C., Alo and Loewe. **13 change and 23 hold.** Every note records the composition percentages and which test was applied.

- **Now elevated under the new rule:**
  - Finisterre: high 205 → 165. The Mora crewneck is 100% extrafine merino.
  - PAIGE: 259 → 249. The Matsuda crewneck is 95% extrafine merino.
  - A.P.C.: 650 → 420. The Striped Alpaca crewneck is 35% mohair and 35% alpaca, so it qualifies only on a combined-fibres test.
- **Lost their elevated high:**
  - Loewe: 1,500 → 1,650, now a range. The cotton-cashmere crewneck is only 44.6% cashmere.
  - Alo stays at 298 but is now a range. The New Class crewneck is 18% cashmere.
- **Held at the same figure, but the high now qualifies as elevated:** Lemaire (75% alpaca) and Dries Van Noten (55% alpaca).
- **The earlier pass got the staple wrong in these rows.** These are errors in the original read, not effects of the new fibre rule:
  - Baracuta 400 → 225: the old high was a mock neck.
  - Filson 699 → 259: it was a cardigan.
  - RRL 1,800 → 395: it was a cardigan or workshirt.
  - Aimé Leon Dore 575 → 400: it was a quarter-zip.
  - Scotch & Soda 238 → 198: it was a half-zip from the outlet section.
  - Kith 150/395 → 175/175: the old low was a sweatshirt and the high a turtleneck.
  - Ksubi 240 → 340/360: the old figure was a women's item.
  - Tecovas → NONE: its only sweaters are in Last Call.
  
  **This suggests other rows outside this set may carry the same kind of error.**

**Rulings needed before merging:**

1. **Combined test.** Does a blend of elevated fibres count when no single fibre is over 50%? This decides A.P.C.: 420 if yes, back to a 350/650 range if no.
2. **Brands with no crewneck at all:** Rhoback, Y.Chroma, Ksubi, Tecovas and Wales Bonner (half-zip only). Should these be NONE, or the category range? They're currently mixed.
3. **"Sweatshirt" names on real knits:**
   - The ALD Pavilion is 56% cashmere but named a crewneck sweatshirt. If accepted, the ALD high is 550.
   - AG's Beck Crew is described as a "sweatshirt" in its copy.
4. **Outlet / final-sale items still on the brand site:** the Outerknown Tomales crewneck is 75% cashmere at $298 regular. If accepted, the Outerknown high is 298.
5. **Superfine claims in generic copy:** Lacoste's merino crew mentions "Extra-fine" only in a shared editorial block. If accepted, the Lacoste high is 160.

## Sweater staple audit, remaining rows (proposed; `sweater_staple_audit.csv`, not merged)

I re-read the other 96 rows that had sweater figures live, under the crewneck staple and the rev 4 fibre rule. That covers every sweater row outside the 36 above, Moncler and Fedeli, and excludes the four blocked houses and Celine. **24 change and 72 hold.** Where a ruling is still open, the cells carry the stricter reading and the note gives the alternative figure.

- **The staple or item was wrong in the earlier read:**
  - Todd Snyder low 198 → 248: the $198 crews are sale or final-sale items.
  - The Elder Statesman low 490 → 1,050: the Daily Crewneck is no longer in the men's range.
  - Isaia high 2,495 → 2,295: the "Cashmere Crewneck" is actually 81% wool.
  - Boglioli low 500 → 675: its low is now only in private sales.
  - Club Monaco → NONE: both crews are sold out everywhere and unlisted.
  - Purple 495 → 395: final sale and a cardigan.
- **Minority-cashmere or other blends no longer count (strict single-fibre, >50% reading):**
  - Rails 248 → 268, Diesel 495 → 550, Givenchy 1,450 → 1,700, Visvim 1,490 → 2,670: these become plain crewneck ranges.
  - Jacquemus 1,150 → 850 and Isabel Marant 945 → 880: an alpaca or mohair crew takes over the high.
  - Ring Jacket ¥132,000 → ¥99,000: the new high is a 14.5-micron wool crew.
  - Boggi 368 → 268: yak isn't on the list.
  - Officine Générale 495 → 695: under the combined-fibres reading it would stay 495.
- **New elevated highs:**
  - Vince 398 → 448 (80% extrafine merino)
  - Giorgio Armani 2,195 → 4,195 (100% silk; the neckline is read from the photo)
  - Dolce&Gabbana 2,045 → 7,045 (100% silk; embellished, but no runway tag)
  - Zilli €1,320 → €1,860 (a new 100% cashmere listing)
  - Brunello Cucinelli 1,350/4,000 → 1,300/4,600
- **Final-sale and outlet items excluded:**
  - Bonobos 250 → 99
  - Vineyard Vines 328 → 108
  - Ted Baker 450 → 295
  - Joe's Jeans 178/358 → 278/278
- **Currency basis:** Percival and NN07 both state "duties & taxes included". The note proposes USD → USD_landed for both.

**Additional rulings surfaced:**
- Does "extra-fine" wording count as superfine wool without a micron figure?
  - Vince, Boggi, Canada Goose, Our Legacy and Zegna's Vellus Aureum.
  - Boggi's own page says 19.5 micron, which is above the ≤18.5 threshold used in the spec.
- Is exactly 50% "a majority"?
  - Suitsupply, Isabel Marant's Leonard, Our Legacy's True Roundneck and Ami Paris's alpaca crew.
- Does llama count like alpaca? It decides Paul & Shark: 975 if yes, 795 if no.
- Are embellished statement pieces in scope?
  - D&G's 7,045 and Armani's 4,195 highs.
- Necklines read only from photos:
  - Armani, Missoni, Fendi, Valentino, Amiri and Burberry.
- Possible runway pieces with no tag:
  - Acne's "RW-" style code (1,300; 1,050 if excluded).
- Mock neck vs crew:
  - AYR Fancy Boy: the page title says "Mock Neck". If it's a mock, the high is 395.
- Pages with no percentage composition:
  - Eleventy.

## Shoe staple audit (proposed; `shoes_staple_audit.csv`, not merged)

I re-read all 108 rows with shoe figures live, excluding the blocked houses. **16 change and 92 hold.** The cells take the stricter reading; the alternatives are in each note.

Two agent results were corrected by me:
- **Fear of God:** the agent excluded ESSENTIALS, against the rev 4 ruling, so the low is restored to 150.
- **Rick Owens:** the agent read mainline only, so the low is kept at 685 (DRKSHDW).

**Changes:**
- **Not a loafer:**
  - Diesel high 595 → 495: a hidden-eyelet lace-up, plus a runway loafer.
  - Brooks Brothers low 150 → 199: a slip-on sneaker, plus clearance items.
  - Isabel Marant 785/945 → 880/880: a lace-up moccasin.
  - Maison Margiela low 780 → 1,450: MM6 ballet flats.
  - Casablanca → range 315/595: its "loafer" is a mule.
  - JW Anderson low 590 → 910: a mule.
  - Ferragamo low 750 → 850: an espadrille.
  - Zilli €870/1,380 → €1,050/1,320: moccasins and an espadrille hybrid.
- **Fur, including hair-on and long-hair goat:**
  - Rick Owens high 4,725 → 3,290
  - Lemaire 990 → 970
  - Ami Paris 810 → 730
  - Isabel Marant (as above)
- **Final sale:** Theory → range 295/395.
- **New or changed listings:**
  - Yohji Yamamoto low 880 → 640: a new flip-flop, currently marked down.
  - Visvim low 765 → 750: a new sandal.
  - Polo Ralph Lauren low 178 → 168: the Anders driver at full price.
- **Driving moccasin counted as a driving loafer:** Sid Mashburn low 350 → 295.

**Rulings surfaced:**
- Is hair-on "pony" calf or goat hair fur?
- Do mules, backless loafers, moccasins, espadrille loafers and driving moccasins count as loafers?
- For no-loafer brands, which footwear counts in the plain range: sandals, slides, flip-flops, slippers, wellies? Barbour, Visvim and Palm Angels are currently treated inconsistently.
- Is an item that first appeared in a runway show, but is now sold as main line, runway? This applies to Todd Snyder's Venetian and Rick Owens's Taquito.
- Clearance items that aren't marked final sale: the Brooks Brothers alternative low is 195.
- Everlane has a new Collegium × Everlane loafer capsule, excluded as a collaboration.

## Consolidated proposals and where the work stopped

- **`proposed_restatements.csv`** gathers every proposed change from the three audits into the return schema. That's now 72 rows (outerwear added 19 Sep), with `SKIP` in every cell not being restated, and names reconcile 72/72. It covers:
  - fibre re-check: 13 changes
  - sweater staple audit: 24 changes, plus 2 currency-basis corrections (Percival and NN07 → USD_landed)
  - shoe staple audit: 16 changes

  Nothing is merged into `return.csv` until the rulings above are made; some rows change depending on the answer.
- **Outerwear staple audit: run on 19 Sep; see the next section.**

## Outerwear staple audit, 19 Sep (proposed; `outerwear_staple_audit.csv`, merged into `proposed_restatements.csv`)

I re-read all 143 rows with outerwear figures live on 19 Sep, excluding the blocked houses. That includes 26 rows an interrupted run had read on 18 Sep, which I read again. **42 change and 101 hold.** The cells take the stricter reading; the alternatives are in `ruling_flags` and the notes.

I corrected one agent result myself:
- **Ami Paris high:** the agent dropped the croc-*embossed* cowhide jacket. Rev 4 says embossed leather is ordinary leather, so the high is restored to 2,650.

**Changes:**
- **The pair wasn't the same style:**
  - Missoni 2,220/6,440 → 4,460/4,790, now an exact-model bomber in wool and cashmere
  - Herno 1,060/2,835 → 995/1,685
  - Prada 8,900 → 7,900
  - Givenchy 1,700/6,950 → 1,650/4,900
  - Rubinacci 4,740 → 3,120
  - Yohji Yamamoto 980/5,470 → 1,790/5,190
  - Peter Millar 178/1,295 → 278/1,398 (the old pair were knit chore coats)
  - Fendi and Jacquemus become plain ranges
- **Fur, including removable collars:**
  - Paul & Shark 3,165 → 1,595 (rabbit-fur undercollar)
  - Isabel Marant 3,980 → 1,990 (runway wording, and fur collars)
- **Final sale, outlet, "Last Call" or archive:**
  - Everlane, Industry of All Nations, Lacoste, Bonobos, Tecovas, Joe's Jeans, Frame, Theory, Aspesi (private sale)
- **Sub-lines and new listings:**
  - Maison Margiela low 1,425 → 695 (MM6 denim jacket paired with the waxed shearling trucker)
  - Officine Générale 995/1,890 → 595/1,495 (DLC line)
  - Ring Jacket ¥550,000/880,000 → ¥385,000/440,000 (new Napoli field jackets)
  - Dolce&Gabbana 2,045/8,445 → 1,995/2,845 (Essential line)
  - Boglioli, Corneliani, Thom Browne, Amiri, Casablanca, Levi's (shearling trucker 1,200)
- **Silk counted as elevated:**
  - Visvim 705/13,875 → 1,372/2,230: an exact-model Somer Swing Top in cotton and in 64% silk. Visvim's "IT" pieces are sold under the visvim name; they don't set this pair.
- **Camel hair not on the list:** Husbands 2,450 → 490, now a range.
- **Price drift and stock changes:**
  - Fedeli, Margaret Howell, Norse Projects, Club Monaco, Purple, Massimo Dutti, Vineyard Vines, Scotch & Soda, Filson

**Rulings surfaced:**
1. Pairs: is an exact model required, or is the same silhouette enough? And does the brand calling everything "blouson" count as one style?
2. Are chore jackets shirt-jackets? This affects Bonobos, Percival, Tecovas and Todd Snyder.
3. Do "Last Call", archive and private-sale sections count as outlet?
4. Do these count as elevated: camel hair, suede-front-only pieces, and knit bombers (Fedeli's Davos, 7,843)?
5. Pre-order and "not available online" pieces:
   - Versace's 13,490 high is pre-order; 6,890 without.
   - Armani's 19,500 blouson is not available online and is excluded.
6. Do track jackets typed as knitwear or "après sport" count? This decides Casablanca.
7. Currency: Yohji Yamamoto's US pages say "Import duties included", so the row may be USD_landed.

## Final outerwear rulings applied (Sebastian, 19 Sep)

**Rulings:**
1. The same silhouette is enough for a pair.
2. Chore jackets are not outerwear.
3. Last Call, archive and private-sale sections count as outlet.
4. Camel hair and knit bombers count as elevated.
5. Pre-order pieces are excluded.
6. Yohji Yamamoto is `USD_landed`.

**Effect on the proposals:**
- **Chore-jacket rows, re-read live:**
  - Percival 255/795 → 255/730: western trucker pair.
  - Alex Mill 225/275 → 250/275.
  - Tecovas → 295/295.
  - J.McLaughlin 348/998 → 898/998.
  - Norse Projects unchanged at 395/1,600.
  - Sid Mashburn 425/795 → 395/1,395: military jacket vs suede work jacket.
  - Billy Reid 398/1,198 → 598/1,598: Harrington pair.
  - Drake's 755/1,995 → 985/2,525: blouson pair.
- **Pre-order:**
  - Versace high 13,490 → 6,890.
  - Jil Sander shoes 1,150/1,490 → 1,490/1,490. Its $1,150 loafer showed "Preorder", which wasn't re-verified.
  - Missoni: re-read shows its "pre-order" flag was a hidden page block. The bombers can be bought, so the pair becomes the silhouette pair 2,450/4,790.
  - Maison Margiela: both pieces confirmed buyable; unchanged.
- **Camel hair:** Husbands goes back to 2,450/3,480, so it's no longer a change.
- **Knit bombers:** Fedeli high 4,329 → 7,843.
- **Yohji Yamamoto:** `currency_basis` → `USD_landed`.

`proposed_restatements.csv` has been rebuilt with these.

## Final sweater and shoe rulings applied (Sebastian, 19 Sep)

**Rulings:**
- **S1:** combined elevated fibres count, and exactly 50% counts.
- **S2:** "extra-fine", "ultra-fine" or "superfine" wording on the product page counts as superfine wool.
- **S3:** driving moccasins, moccasins, mules and espadrille loafers count as loafers. Hair-on pony or goat leather is fur.
- **S4:** final sale, clearance, outlet and pre-order are excluded.
- **S5:** a brand with no men's crewneck gets sweater NONE; a brand with no own loafer gets shoes NONE. This replaces the `range` fallback for those two garments. A brand that sells crewnecks but none in an elevated fibre keeps its plain crewneck range.

**How it was applied:**
- **From recorded evidence:** 52 cells, applied from product names, prices and compositions already recorded in the audit notes, with no guessing.
- **Live look-ups:** 10 cells were read live on 19 Sep.

**Result:**
- **S5, shoes → NONE:** 26 brands. This includes Barbour: its only mule is sold as a slipper.
- **S5, sweater → NONE:** Rhoback, Carhartt, Y.Chroma, Ksubi, Wales Bonner, plus Southern Tide, whose only crewnecks are final sale.
- **Wythe shoes → NONE:** the only mocs are made with Easymoc, named in the description as co-creator. If they count as plain Wythe product, the answer is 388/388.
- **S3, 19 shoe rows move.** Examples: Todd Snyder low 248, JW Anderson 590/910, Peter Millar 250/395, Versace 795/1,425, Ferragamo 750/1,590, Zilli €870/1,380, Casablanca 515/545. Dolce&Gabbana's drivers bring its low to 845.
- **S1:**
  - Rodd & Gunn 128/178
  - Officine Générale 495/495
  - Ami Paris 430/690
  - A.P.C. 350/420 (combined fibres)
- **Lacoste sweater:** 98/350 → 98/240. The extra-fine wording is generic womenswear copy. The old 350 high was a polo-collar sweater, not a crewneck.
- **`not_a_staple`:** updated for 32 rows, adding Sweater or Shoes wherever a cell became NONE.
- **`proposed_restatements.csv`:** now 98 rows. Names reconcile 98/98. It passes the schema check except Ring Jacket's yen values above 99,999, which you've already accepted.

**Caveat on S5:** `NONE` was defined as "the brand does not sell this garment". After S5, shoes `NONE` also covers brands that sell sneakers or boots but no loafer. So Shoes in `not_a_staple` now means "no loafer", not "no footwear". If the Spectrum shows NONE as "doesn't sell shoes", that label needs changing.

## Merge into return.csv (19 Sep, on Sebastian's instruction)

`proposed_restatements.csv` (98 rows) is merged into `return.csv`, which now has **112 rows**. 11 brands were in both files. For those, the audit value replaced the rev 4 value wherever the audit restated a cell. Notes and sources are concatenated. A `partial` status stays partial (Celine and the four blocked houses).

**Cells where the audit replaced a rev 4 figure:**
- Visvim outerwear_high 13,875 → 2,230: silk pair.
- Fear of God shoes 150/1,250 → NONE/NONE: no loafer (S5). `not_a_staple` → Shoes.
- Maison Margiela:
  - outerwear 1,425/6,120 → 695/6,590 (MM6 denim / waxed shearling trucker)
  - shoes_low 780 → 1,450 (ballet flats aren't loafers)
- Rick Owens shoes → NONE (no loafer).
- Fedeli outerwear_high 4,328 → 7,843: knit bomber.
- Dolce&Gabbana outerwear_high 8,445 → 2,845: Essential-line pair.

**Checks after the merge:**
- Names reconcile 112/112.
- No blank cells.
- No low above its high.
- NONE always appears in pairs.
- The only schema exceptions are Ring Jacket's yen values above 99,999, and `NONE` in `search_url` (Indochino and Ferragamo), which is parked.

Some rows carry a single restated cell with the other left as `SKIP`, e.g. Hermès shoes_high. That's deliberate: only that cell changed.

The pre-merge file is kept in the scratchpad.
