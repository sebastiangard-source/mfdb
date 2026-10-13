# Wave C seating job — handoff, 12 October 2026

This file lets a new session continue the wave C full-records job without the old workspace. Everything referenced sits beside it under `wave_c/` in this project.

## What the job is
Read `wave_c/brief/BRIEF.md` and `wave_c/brief/RESUME.md` first, then `wave_c/brief/audit_protocol.md`. The task: return the `seat_resort` record for 81 brands (`wave_c/brief/worklist.csv`), with these files per batch of ten:
- `return.csv`: 132 columns, from `return_template.csv`
- `own_doors.csv`
- `stockists.csv`
- `return_styles.csv`: one row per style
- `NOTE.md`

Brand names must pass `reconcile.py` against `canonical_keys.txt`. Tokens: `NC` = nobody looked, `NONE` = does not sell or do, `np` = no price published. No empty cells.

## Done and delivered
1. **Door counts** for the ten `NC` brands plus a Zara census: `wave_c/out/counts/` (`return_counts.csv`, `own_doors.csv`, `NOTE.md`).
2. **Batch 1 of 9** (Alan Flusser, Anglo-Italian, Asket, Awake NY, Aztech Mountain, Bad Birdie, Beams, Berg & Berg, Birdwell, Blundstone): `wave_c/out/batch1/`. This is the revised version after the rulings below.

3. **Batch 2 of 9** (Brain Dead, Budd Shirtmakers, C.P. Company, Carmina, Castaway Nantucket Island, Closed, Danner, Denim Tears, Deus Ex Machina, Dickies): `wave_c/out/batch2/`. Revised after the 11 Oct rulings below.
4. **Batch 3 of 9** (Eastside Golf, Edward Green, Evan Kinori, Express, Flint and Tinder, Freenote Cloth, Frye, Fusalp, G-Star, Gallery Dept.): `wave_c/out/batch3/`. Merged at v3.54.0 with batches 1–2; its 6 questions were ruled on 12 Oct (`wave_c/brief/RULINGS_wave_c_batch3_2026-10-12.md`).
5. **Batch 4 of 9** (Gap, Goldwin, Golf Wang, Hender Scheme, Hickey Freeman, Holderness & Bourne, Imogene + Willie, Jos. A. Bank, Katin, Kiel James Patrick): `wave_c/out/batch4/`. It also carries the two re-reads asked for on 12 Oct: G-Star's 13 US mono-brand doors with addresses (in its `own_doors.csv`, brand G-Star) and the Blundstone craft proposal (2, in its `NOTE.md`). Its `NOTE.md` ends with 7 questions for ruling, open.

## Next: batch 5 (worklist rows 41–50)
Lady White Co., Lands' End, Lardini, Ledbury, Mango, Meermin, Mollusk, Muji, Nautica, Needles.
- Lands' End, Mango, Muji and Nautica are large houses: a category-stratified sample is allowed; count the full catalogue and say the sample is not proportional (batch 4 Gap / Jos. A. Bank pattern, `FULL` overrides in `assemble_b4.py`).
- Read each worklist note: several ask for a "floor ruling" (Lands' End, Mango, Muji, Nautica) or a channel ruling (Nautica, mostly outlets). Count doors, row outlets as outlets, and put the floor question in NOTE.md rather than deciding it.
- Needles: the worklist asks "one key or two" (Nepenthes NY). Keep the worklist key `Needles` and raise the question.
- Lardini (Italian) stays in its own currency unless the US store shows USD; Meermin is a shoe house (check for clothing before writing a style table).
- Guam, USVI and other territories are listed but are not US doors; Puerto Rico is.

## Rulings of 12 Oct (batch 3 answers; keep applying)
- A licensee's line sold under the brand on the brand's own store is own label (Frye / Moda Piel).
- Sub-lines like G-Star RAW Research and E stand; their highs stand.
- Undated department-store "pop-ups" are `concession`, not counted (Fusalp Korea).
- Posted hours a customer can use make a door (Freenote San Juan Capistrano, counted, flagged).
- Gallery Dept.: Chateau Josué and Art That Kills excluded (confirmed). Express Boca Raton counted under the women's-only ruling (confirmed).
- `proposed_tech` stays NC; fill `tech_named_fabrics` fully. Every own-door row needs street, city and state.

## Rulings of 11 Oct (keep applying)
- Collaborations are out of prices and the style layer. A shoe house whose every shoe is a collaboration gets shoes = NONE; Bad Birdie's Payntr exception does not generalise.
- Own door only if the brand's name is on the door. Operator- or licensee-run stores count, flagged. Women's-only stores count, flagged `womens-only`. Pop-ups get dates.
- A store in an outlet centre is an outlet. Department-store counters are concessions, not counted.
- Marks as the logotype writes them; keep the worklist key in `brand`. Non-USD houses stay in their own currency; `USD_landed` when duties are included.
- Sub-lines sold under the brand's name count; capsules are never a high.
- Elevated fibres: majority-cashmere blends, silk, alpaca, mohair, vicuña, superfine wool. Never fur or exotic skins. Horsehide and cordovan are not exotic.
- Stocked third-party footwear is not own label. A jacket sold as a shirt is a shirt (Budd).

## All rulings received from Sebastian (keep applying)
Earlier rulings are in `wave_c/brief/RULINGS_*.md`. From this session, 10 Oct:
1. **Large houses** (Nike, Uniqlo, Zara, Gap, …): `return_styles.csv` may be a category-stratified sample. Say so in `status` and `NOTE.md`.
2. **Beams** is read on **beams-america.com**: vendor BEAMS plus the BEAMS T sub-line only; the other brands that store sells are excluded.
3. **Bad Birdie's Payntr collaboration shoe** stays in the shoes cells.
4. **SurfNyl®** (Birdwell) is filed as nylon (polyamide). SurfStretch® is still undisclosed; it was asked about and has no ruling yet.

## Method that worked (and traps found)
- **Shopify houses:**
  - Read `/products.json?limit=250&page=N`, plus each nav collection's `products.json` for categories.
  - Composition is often only on the product page. Labels seen: "Fiber content:" (Aztech), "Materials + Care" (Bad Birdie), "Details Materials" (Berg & Berg), "Composition & Care" (Beams America).
- **Style grouping:** use the SKU stem where the SKU carries one (Bad Birdie `BBMP001`; Birdwell first two segments; Beams first 11 digits). Otherwise de-duplicate by title, stripping colour words.
- **Prices: check the displayed page price against the feed.** Anglo-Italian's feed (USD presentment) ran 1.48% above the displayed page, so prices were taken from the server-rendered page. Berg & Berg matched.
- **Markdown houses:** use compare-at as the regular price (Awake NY).
- **Exclusions:**
  - Third-party and collaboration goods on multi-brand stores: filter by vendor or title.
  - Archive feeds: count only available products.
- **Parser:** `wave_c/code/fibre.py`.
  - Main fabric line only; labelled parts ("Contrast fabric:", "Rib part:", "Lining:") are cut.
  - Japanese labels handled (コットン, 毛, キュプラ, 表地/裏地). Japanese "polyurethane" is filed as written.
  - A fibre named without a % counts as a composition.
  - Trademark fabric with no stated fibre → undisclosed.
- **Builders:** `wave_c/code/build_b1.py`, `meta_b1.py`, `assemble.py` and `doors_stock.py` produce the batch files. Copy and adapt them per batch (`meta_bN.py` holds the hand-judged price picks, craft fields and quotes).
- **Browser helpers:** `wave_c/code/helpers.js` holds the JavaScript used inside Chrome when the workspace cannot fetch directly.
- **Vinted:** `/api/v2/brands?keyword=` on vinted.com works from a browser tab. The men's URL is `https://www.vinted.com/catalog?brand_ids[]=ID&catalog[]=5`.
- **Grailed:** `/designers/<slug>`. A generic "Designer Clothing" title means no page.
- **Not reachable so far:**
  - B Corp: the B Lab directory search ignored its query in Chrome.
  - GOTS: not attempted.
  - `proposed_tech` stays `NC`: no rubric in the brief.

## Batch 2 method (Chrome only; the workspace still got 403 on every brand host)
- **Extraction:** build the data in JS, render it into `<pre id=o>`, then read it with `get_page_text`. This returns about 40k characters per call.
  - Dickies pages break `get_page_text`. Stash the data in sessionStorage and render it on `/robots.txt`.
- **Platform recipes** are in `raw/batch2_inputs/notes.md`:
  - Salesforce: `?sz=500` plus Stores-FindStores.
  - Logicommerce: `form[data-product]`.
  - Global-e: USD read off the listing tiles.
  - Constructor.io browse API.
  - stockist.co API.
  - Shopify store-locator app.
- **Size upcharges:** some Shopify houses charge more for big sizes (Dickies). Take the base-size price from `/products/<handle>.js`.
- **Vinted API:** needs an `accept: application/json` header.
- **Builders:** `code/build_b2.py`, `meta_b2.py`, `assemble_b2.py`, `doors_stock_b2.py`. `fibre.py` now handles German labels (Baumwolle, Wolle, Elasthan, ...).

## Batch 3 method notes
- **Builders:** `code/build_b3.py`, `meta_b3.py`, `assemble_b3.py`, `doors_stock_b3.py`; raw inputs and per-brand notes in `raw/batch3_inputs/` (`notes.md` has every pick with URL).
- **Spot-check every pick against `/products/<handle>.js`.** A SKU-stem style can join colours priced differently (Freenote): the handle stored for a style is not always the one carrying its low or high price.
- **Large custom sites:** use the site's own client. Express: `window.__APOLLO_CLIENT__` (plain fetch to /graphql gets an Akamai 400). G-Star: its Algolia index with the public key in the page. Huckberry: `/api/pages/tiles`.
- **Long scripts:** run as a background async job that sets a flag, then poll; long single calls time out the extension.

## Batch 4 method notes
- **Builders:** `code/build_b4.py`, `meta_b4.py`, `assemble_b4.py`, `doors_stock_b4.py`; raw inputs and per-brand notes in `raw/batch4_inputs/` (`notes.md`). `code/helpers_b4.js` is the Shopify DUMP/RECON helper; paste it fresh per page load.
- **Blocked outputs:** the extension blocks returned text containing `?`, `&` or `=`. Render into `<pre id=o>` and read with `get_page_text`, or strip those characters before rendering.
- **Gap:** product-search API `api.gap.com/v2/product_search_cc_aggregations/v2` (cid 1127944, department 75); PDP fabric bullets in the page JSON (`"id":"fabric"`). Stores: `/stores` → state → city → store pages; address in ld+json, format in the markerData `store_type` (a text match on "Gap Factory" is useless: it is in the nav).
- **Jos. A. Bank:** HCL Commerce search `/sr/search/resources/store/13452/productview/byCategory/<id>?catalogId=14052&responseFormat=json` and `/productview/<partNumber>`; `buyable=true` = live; `/p/<title-slug>` works for most products but some need the part-number suffix (`-5BHB`).
- **G-Star stores:** `/en_us/find-a-store/getstores?country_iso=US&output_details=1` with headers `X-Requested-With: XMLHttpRequest` and a JSON accept.
- **Check listing URLs:** guessed `/collections/mens` 404'd on four houses; fetch each listing and page URL for status before writing it.
- **North Carolina:** `state` = NC on own-door rows is the state, not the token; say so in NOTE.md.

## First thing in the new session
1. Run `curl -sS -o /dev/null -w "%{http_code}" https://www.landsend.com/`.
   - If it returns 200, fetch directly with Python.
   - Otherwise use Claude in Chrome with the batch 2 method above.
2. Batch 2 took about four hours through Chrome.
