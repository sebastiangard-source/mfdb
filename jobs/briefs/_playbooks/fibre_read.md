# Reading a brand's own site for fabric composition — the playbook

**15 September 2026.** Written for a thread starting cold. Everything in it was learned on a pass that
counted 68,670 men's styles across 191 brands; every trap named below fired at least once. Read it
end to end before touching a site.

## The question

For one brand, from its own product pages: how does its **men's clothing range** divide by main
fibre (natural / synthetic / cellulosic), how much of it stretches, and is it one cloth story or
two? The answer is a **count of styles**, and every figure has a URL behind it.

## What you return

Six files. `return_styles.csv`, one row **per style**, is the layer everything else is derived
from and the one that must be kept: with it a house can be re-cut on any future rule without a page
being re-read, and every aggregate can be checked against it. Then `return.csv`, one row per brand;
`return_categories.csv`, one row per brand **per product category**; `return_fibres.csv`, one row
per brand **per fibre**; `return_lines.csv`, one row per brand **per named line**; and `NOTE.md` saying what you read, what you could not reach, what contradicted the brief, and
what the brief got wrong. No summaries in place of data, no working files, no rebuilt tools.

The brand row is the roll-up of its category rows: `styles_total` is their sum, the percentages
are computed from them, and `shape`, `synthetic_categories` and `natural_categories` are read off
the category table rather than judged. Build the categories first; the brand row falls out.

**Never invent, never extrapolate, never fill from memory.** A cell nobody looked at is `NC`. An
empty cell is an error. `0` means counted and found none.

## Definitions and rulings — apply to every row

- **Scope: clothing only.** Hats, socks, gloves, scarves, belts, bags, shoes, hard goods and licensed
  headwear are out. Underwear and swim are in the denominator, out of the split verdict.
  Men's only: a path rule that sweeps in boys' or women's styles is wrong (Vineyard Vines 721 → 669).
- **A style, not a colourway, not a listing.** A style is a distinct numeric stem; colourway codes,
  finish variants (Canada Goose 247 → 159), size runs and locale copies (Baracuta 992 entries = 283
  handles × 4 locales) collapse. Report `colourway_ratio` (raw/styles) and `locale_dedup`. A ratio of
  exactly 1.00 on a house with colour options is itself suspicious; say why.
- **Main fibre = the fibre with the highest share in the first composition listed.** Shell over
  lining, shell over filling (down reads the shell). Ties: first-listed wins.
- **natural** = cotton, wool, linen, silk, cashmere, hemp, down, leather. **synthetic** = polyester,
  polyamide/nylon, acrylic, elastane, polypropylene, polyurethane and the like. **cellulosic** =
  rayon, viscose, modal, lyocell/TENCEL, cupro, acetate — a third figure, neither side.
  `natural + synthetic + cellulosic + (no composition) = 100`, of all styles.
- **A named fibre with no percentage counts as a composition** ("100% lambskin", "REAL LEATHER",
  John Smedley's named materials). A cloth name does not ("Bedford cord", "seersucker").
- **Stretch is two counts, on the main fabric line only.** `spandex_styles` = any elastane there;
  `spandex_high_styles` = 5% or more. Neck tape, rib edges, plackets, pocket bags do not count
  (Lacoste puts 133 styles' elastane in trims). "Exclusive of elastic" = excluded. "100% cotton with
  mechanical stretch" = no elastane. Named stretch with no percentage ("5% Stretch") counts in the
  first cell, never the second. Elastolefin (XLANCE) counts as elastane.
- **shape** = `one` or `split`; `synthetic_categories` = categories where synthetic leads;
  `natural_categories` = top three natural-led. JSON lists; `[]` for a one-cloth house.
- **status** = `complete`, or `partial` when under ~60% of styles state a composition after a
  payload read, or when a cell is `NC`. Return the numbers either way and say why.

## Method, in order

### 1. Find the real store before counting anything

- **The apex domain may not be the US store.** `isabelmarant.com` is the EMEA store; the US range is
  `us.isabelmarant.com`, a different catalogue. `saint-james.com` 302s to the French store. Fifteen
  domains in circulation are wrong, dead or someone else's (`sease.com` is a private homepage,
  `rhude.com` a photographer). Confirm you are on the house's own US-facing store and say which.
- **Assert `location.host` inside the page before every capture and inside every loop.** A shared
  tab drifted origin mid-run once and filed Norse Projects as Y.Chroma; `drakes.com` geo-redirects a
  beat after it has answered fetches.
- **Identify the platform.** `window.Shopify` → Shopify. `__PRELOADED_STATE__` / `/on/demandware.store/`
  → Salesforce Commerce Cloud. `__NEXT_DATA__` → Next.js. VTEX, Magento, BigCommerce each have a
  feed. This decides the cheapest channel.
- **Record `Shopify.currency.rate`.** If it is not 1.0 with USD active, `/products.json` is in the
  shop currency, not dollars. Free while you are there.

### 2. Census the catalogue — get the denominator right first

Reconcile at least two of feed, sitemap and the house's own listing count before trusting any.

- **Shopify:** `/products.json?limit=250&page=N` until a page returns **zero or a non-OK status**,
  de-duplicating on product id. A short page is not the end (State & Liberty page 1 = 249, pages 2–3 =
  250). Kith returns 250 on pages 1–100 then HTTP 400 — a 25,000 cap that never yields a zero page.
  A headless store usually still has its feed: `rhone.com` 404s `/products.json` but
  `window.Shopify.shop` names `rhone.myshopify.com`, which serves it. Try the myshopify origin
  before accepting a crawl.
- **Feeds lie in both directions.** Wax London's feed is a superset of the live range by 208 dead
  PDPs; Scotch & Soda's is 2,329 of 3,898 dead. Vollebak's sitemap is short 68 live products.
  Sandro's sitemap is 164 men's styles short of its own category tree. Sample both sides for a 200
  and `available: true`.
- **Pagination has failed in six shapes.** Re-serving page one (John Smedley, Burberry, Hermès at
  page 3); a short first page; a four-tile server-rendered grid (BOSS); silently ignored params
  (Prada, Palm Angels); **cumulative** paging where page 2 contains page 1 (Givenchy, Margiela, Jil
  Sander); a hard cap that 400s. The test is that the id set grows by exactly the page size — not
  that pages are disjoint — and that a recommendation grid past the end is not a page.
- **A product sitemap can be a 1,000-item cap.** Saint Laurent's contains two men's ready-to-wear
  products; the true 320 came from the PLP data route.
- **Read the record count the widget itself states** and reconcile to it. Patagonia gives 518 on
  the grid, 562 on the counter (518 + 25 colourway tiles + 18 third-party goods + 1 book), 702 in
  the sitemap. 518 is the answer; the note says why.
- **Concurrency, not volume, trips WAFs.** ~1,600 requests at concurrency 5 with 130 ms spacing drew
  nothing at Ralph Lauren; concurrency 10 drew a block. Canada Goose 429s above ~8 concurrent.
  Lululemon's Akamai wall (`400 GE401001`) took 33 pages at 200 ms and did not lift for hours.
  Go slow from the start. Reading a robots-disallowed path is in bounds; record the path.
- **The vendor field is not the boundary.** Arpenteur's 17 shoes are Paraboot and Veja under its own
  vendor string. Judge third-party goods by product code, name and collection.
- **A product type is not a fibre.** J.Press's "College Silks" are 102 glass paperweights.
- **Merchandising tiles arrive in a feed as products.** Tibi's `/products.json` carries 122
  "Content Block" and "PDW" records, 24 of them with real category tags, so a category filter alone
  does not remove them; catch them on title. Patagonia's colourway tiles are the same trap.
- **Unbounded substring scope filters delete garments.** `/glove/` removed the "Gloverall Monty
  Duffle Coat"; `/tie/` a "Tie-Dye" shirt; `/bag/` two garments in colour "Shopping Bag Brown".
  Match on category, not on substrings of titles.

### 3. Find where the composition actually lives

**Payload before DOM.** Composition frequently never enters `document.body.innerText`. Canada Goose
read as 39% undisclosed and Bonobos as 46% from rendered text; both are near-complete in the page
payload. **Do not call a row partial before reading the payload.** Where it has been found:

| where | houses |
|---|---|
| `properties.fabric` in `__NEXT_DATA__` | Bonobos |
| `c_materialComposition` in `__PRELOADED_STATE__` | Canada Goose (and nowhere else on Salesforce — the field is the house's, not the platform's) |
| `apparel.material` in `__LSCO_INITIAL_STATE__` | Levi's |
| `page.data.customAttributes` in `window.__INITIAL_STATE__` | NN07 |
| `_next/data/<buildId>/…json` route | Next.js houses |
| a product **tag** `contentdesc-96% Cotton, 4% Elastane` — Shopify splits tags on commas, so read the `contentdesc-` tag alone | James Perse |
| `pdp_accords.fabric`, now an object not a string | Buck Mason |
| JSON-LD `material` — **often wrong**, see step 4 | many |
| the second `<p>` of DETAILS, while an accordion literally named MATERIALS holds a fibre essay | Brunello Cucinelli |
| ad copy ("Made from 100% natural silk"), no structured field at all | Rubinacci |
| parentheses inside the description | Hermès |
| an unlabelled first bullet of `featuresAndDetails` (labelled `Composition:` only on denim) | Rag & Bone |
| one fibre per `<li>` with parts that sum to 200 | Theory |
| behind a dialog wired to a controller, not in the DOM at all | Stone Island (composition unreachable; state it) |

Some houses publish none through any first-party channel (Sugar Cane, Junya Watanabe, Charvet,
Cesare Attolini — whose Shopify backend has twenty empty collections). Confirm that four ways and
return the denominator with the rest `NC`; that is a finding.

### 4. Parse — and distrust anything that parses cleanly

- **Validate the candidate field by hand against the rendered product detail on ten varied pages**
  before trusting it: multi-part garments, shell/lining/insulation, camel-joined labels.
- **A field that looks like the composition is the most dangerous thing on the page.** Canali's
  "Composition" holds names with no percentages; Etro's JSON-LD `material` is one family word on 293
  of 548 (`LINEN` where the truth is 56/44 linen/viscose); Fendi's is truncated to the first
  component so spandex reads 0; Brioni's is a whole-garment average across shell and lining;
  Brioni's `compliantComposition` is the literal string `"$undefined"` on 158 of 840 — truthy, and it
  silently defeats a `||` fallback. Saint Laurent's `compliantComposition` has names without
  percentages on 123 of 320; the same field at McQueen, same platform, is correct. Validate per house.
- **Percentage order varies.** Luca Faloni and Lacoste write `Silk (30%)` — percent after fibre.
  Detect the order per house and parse once; running both orders double-counts.
- **Fibres are not always words.** Aspesi uses EU codes: `80%PL 20%PA`, `WS 100%`, `50%WY 50%WO`.
- **Accents and misspellings are a coverage hole:** `élastane`, `ELASTHANE`, `Elastine`, `POLIAMYDE`,
  `casmere`, `Cashere`, `Vicuña` (which handed a 97% vicuña knit to silk). Match accent-folded; keep a list.
- **Pre-strip fabric grades** — `Super 140's Wool` parses to the fibre "Super". But `100% SUPER
  GEELONG WOOL` is a wool type; take the fibre class by keyword inside the percentage chunk.
- **Element boundaries split fields silently.** A `<br>` inside Boggi's field returned 984 of 989 as
  single fibres and elastane 4 times; the truth was 217. One `<span>` per fibre at Boglioli; a `<br>`
  inside `54% Polyester 44% Wool / 2% Spandex` at Dolce&Gabbana. Part labels need the Italian set
  and an optional trailing number (`TESSUTO 2:`); separators may be an en dash.
- **Labels vary inside one house.** Balenciaga: "Main material:", "Main material 1:", "Material 1:",
  "Fabric 1:", and bare lines.
- **Special characters kill regexes silently.** `brrr° recycled polyester` dropped the leading
  fibre on five styles; a `(100% recycled)` parenthetical lost three styles' 16/12/12% elastane.
- **A composition can sum to 100 and contain no cloth.** `ACCESSOIRES 100%NICKEL`, `100%PEARL`
  (Kiton). Scope should have removed these; check.
- **An unterminated `<ul>`** produces no string at all, so the sum check cannot see it (Dries Van
  Noten). Count styles whose parser returned nothing and open five by hand.

### 5. Validate before computing

- **Sum every composition to 100 ± 1.** Outside that is a parse failure, not a finding. This is the
  check that caught the degree sign, the `<br>`, the en dash and the 200% Theory rows.
- **Any extractor returning the same value on 100% of rows is reading page furniture.** Balenciaga
  mentions Tencel on 338 of 338 pages (the shopping bag) and has it in zero compositions. Check the
  string on a page with no product.
- **Furniture need not be constant.** Ralph Lauren's construction bullets return different plausible
  wrong values ("Button-down collar" → down; "Leather patch at the back waist" → leather).
- **A PDP can server-render other products.** NN07's PDP renders eight featured products
  byte-identical on every page; a whole-page regex returns the same eight compositions 235 times.
- **Never key on product names.** John Smedley is all knitwear and scores 6 of 107 on a knit word
  count; its products are called Lundy and Bradrick.
- **Reproduce before you restate.** If an earlier figure exists, reproduce it on its own basis first;
  where you cannot, record both and say which is filed.

### 6. Categories — the breakdown the map wants

Count every figure **per product category** and return one row per brand per category. Use the
house's own category label as it appears in its navigation or feed (`category_house`) and map each
to one of the standard set (`category`):

`tees-polos` · `shirts` · `knitwear` · `sweats` · `trousers` · `denim` · `shorts` · `tailoring`
(suits, sport coats, blazers, waistcoats) · `outerwear` · `underwear-swim` · `dresses` · `skirts` ·
`jumpsuits` · `other` (say what). The last three exist for houses outside the men's map; on a men's
row they are empty.

One style, one category. Where the house's taxonomy overlaps (Stone Island lists anoraks under
shirts and coats; Zegna has an `underwear-socks` node), assign by the garment, not by the first
menu it appears in, and say so in `note`. Where a house has no categories (a flat feed), assign
from product type or title and set `category_house` to `derived`. A category with fewer than
five styles still gets a row; the count is the finding.

The brand row's `shape` is `split` when at least one category with ten or more styles is
synthetic-led while another is natural-led; `synthetic_categories` lists the synthetic-led
categories by their house label; `natural_categories` the top three natural-led by style count.
Underwear and swim are excluded from that verdict but present in the table.

### 7. Fibres — what the buckets are made of

You already parse every fibre in every composition to find the leader. Keep the by-product. For
each brand, one row per fibre that appears anywhere on a main fabric line, with:

- `fibre` from the standard list below; `fibre_house` as the house writes it (`ELASTHANE`, `PL`,
  `Cashere`, `TENCEL™ Lyocell`) so the mapping can be audited.
- `styles_leading` — styles where this fibre has the highest share.
- `styles_any` — styles where it appears at all on the main line.
- `median_pct` — its median share across the styles where it appears.
- `styles_with_composition` on the brand, so the two counts can be read as shares.

Standard fibre list. **Do not collapse cellulosics into viscose**: modal and lyocell are different
fibres with different provenance and hand, and the whole point of this file is to tell them apart.

| class | fibres |
|---|---|
| natural | cotton · wool · linen · silk · cashmere · hemp · alpaca · mohair · camel · vicuña · yak · leather · down · other-natural (say what) |
| cellulosic | viscose (incl. rayon, EcoVero) · modal · lyocell (incl. TENCEL) · cupro · acetate · triacetate · other-cellulosic |
| synthetic | polyester · polyamide (nylon) · elastane (spandex, Lycra) · acrylic · polypropylene · polyurethane · elastolefin (XLANCE) · elastomultiester · other-synthetic (say what) |
| other | metal · glass · mineral · other (say what) — should be scope leaks; report them |

A fibre a house names by trademark — TENCEL, EcoVero, Lycra, Coolmax, Sorona — maps to its class
fibre, with the trademark kept in `fibre_house`. A brand-named cloth ("Tropical Wool") is not a fibre
and does not get a row; its composition does.

### 8. Lines — the parts of a house that are all one thing

A category cut misses the way houses actually organise cloth: Peter Millar's Crown Sport is
synthetic and its Crown Crafted is natural, and both run across polos, trousers and outerwear.
Find the house's **named lines** and measure each one.

A line is anything the house itself names and groups product under: a sub-line or sub-brand
(Laminar, Linea Rossa, Veilance if unseated), a collection or series (Crown Sport, Summer Comfort,
Tropical Wool, Heater Series), a fabric family it sells as a line (DreamKnit, Tour-fit), or a fit
family that carries its own cloth. Read them from the navigation, collection handles, product-line
tags and series names in titles. **A line the house has not named is not a line** — do not invent
groupings from compositions.

For each line with **five or more styles**: styles, coverage, the three shares, both stretch
counts, and a `verdict`: `all-natural` when 90% or more of disclosed styles are natural-led;
`all-synthetic` when 90% or more are synthetic-led; `all-cellulosic` likewise; otherwise `mixed`.
A style can sit in more than one line (Crown Sport and Polos); the line table is not a partition
and does not need to sum to the range. Say in the note how lines were identified and how many
styles sit in none.

Report the verdicts in `NOTE.md` as the headline: **which lines in this house are wholly natural,
which wholly synthetic, and how much of the range they account for.** That, not the brand average,
is what a reader planning to walk in wants to know.

### 9. Styles — keep the layer underneath

Every aggregate above is computed from a per-style table you already hold. Return it. One row per
style, in scope, with: the house's style code; the title as written; the canonical product URL;
the standard category and the house's label; the named lines it belongs to (`;`-joined, blank if
none); the composition string exactly as the house wrote it; the parsed leading fibre and its
share; the elastane share on the main line (0 if none); a `pure` flag — `natural` when every fibre
on the main line is natural, `synthetic` or `cellulosic` likewise, `blend` otherwise; and
`single_fibre` — the fibre name when the main line is 100% one fibre, else blank. Colourway
records collapse to one row; the URL is the first colourway's.

This file answers the questions the aggregates cannot: which garments are 100% cotton, which are
all-natural at any blend, what sits behind a line or a category, and where to buy the thing.

### 10. Compute and record

Percentages are of **all** styles in scope, undisclosed included; `styles_with_composition` carries
coverage. Count the numerator and denominator on the **same style set** — Vuori's underwear moved
between them and the cells were filed on the set they were counted on, with the discrepancy noted.
Every figure in the note carries the URL and the date it was read; a channel can change in a day
(NN07's `resolve-slug` API vanished; johnnie-O's `/products.json` began 404ing).

## Time and stopping

25 minutes on a Shopify house, 45 on anything else, 75 on a luxury house with a WAF. Past that, `NC`
with a note. Stop and say so when the brief is mis-aimed: a third of a pilot returning nothing usable,
or an instruction that would produce a confident wrong answer. Send the first eight rows before doing
the rest.

## The schema

**`return_categories.csv`** — one row per brand per category:
`brand` · `category` (standard set above) · `category_house` (the house's own label, or `derived`) ·
`styles` · `styles_with_composition` · `natural_pct` · `synthetic_pct` · `cellulosic_pct` (of
`styles`) · `spandex_styles` · `spandex_high_styles` · `source` · `note`.

A worked block, Peter Millar: `tees-polos | Polos & shirts | 188 | 188 | 31 | 69 | 0 | 121 | 114`,
`knitwear | Sweaters | 61 | 61 | 92 | 8 | 0 | 4 | 0`, `tailoring | Sport coats & suits | 27 | 27 |
96 | 4 | 0 | 6 | 0` — three rows that say more than "46% natural, split" ever did.

**`return_fibres.csv`** — one row per brand per fibre:
`brand` · `fibre` (standard list) · `fibre_house` (as written; `;`-joined if several spellings) ·
`styles_leading` · `styles_any` · `median_pct` · `source` · `note`.

A worked block, Tibi (from the thread's own asides, to be replaced by the return): `polyester |
Polyester | 349 | … `, `viscose | Viscose; Rayon | … | 65 | …`, `acetate | … | 59`, `lyocell |
Lyocell; TENCEL™ | … | 27`.

**`return_styles.csv`** — one row per style in scope:
`brand` · `style_code` · `title` · `url` · `category` · `category_house` · `lines` · `composition`
(as written) · `lead_fibre` (standard list) · `lead_pct` · `elastane_pct` · `pure`
(`natural|synthetic|cellulosic|blend`) · `single_fibre` (standard fibre or blank) · `note`.

**`return_lines.csv`** — one row per brand per named line with five or more styles:
`brand` · `line` (the house's name for it) · `line_kind` (`sub-line|collection|fabric-family|fit-family`) ·
`how_identified` (`navigation|collection-handle|tag|title-series`) · `styles` · `styles_with_composition` ·
`natural_pct` · `synthetic_pct` · `cellulosic_pct` · `spandex_styles` · `spandex_high_styles` ·
`verdict` (`all-natural|all-synthetic|all-cellulosic|mixed`) · `source` · `note`.

**`return.csv`** — one row per brand, the roll-up:
`brand` (exactly as in `canonical_keys.txt`; run `reconcile.py` before returning) · `styles_total` ·
`styles_with_composition` · `natural_pct` · `synthetic_pct` · `cellulosic_pct` · `spandex_styles` ·
`spandex_high_styles` · `shape` (`one|split`) · `synthetic_categories` (JSON) · `natural_categories`
(JSON) · `style_method` (`product_code|title_dedup|handle|manual`) · `colourway_ratio` (`1726/396`) ·
`locale_dedup` · `feed_currency_rate` (`1.0`, `1.183`, `not shopify`) · `status` (`complete|partial`) ·
`source` (URL, what was read, date) · `note`.

A worked row, Levi's: `396 · 380 · 88 · 8 · 0 · 41 · 3 · one · [] · ["Shirts & Tees","Outerwear","Jeans"]
· product_code · 1726/396 · per-locale sitemaps; US/en_US only · not shopify · complete`.
