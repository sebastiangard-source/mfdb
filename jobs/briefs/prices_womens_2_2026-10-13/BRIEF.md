# prices_womens_2_2026-10-13 — entry and top prices for 29 more women's brands with US stores

**Issued** 13 October 2026, evening · **Kind** price · **Batches of ten, each returned as done** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the second cut of `prices_womens_2026-10-13`, the same job on the
same rules: full price, the product behind every figure, the URL it was read from, eight women's garments.
It is a Chrome job on the brands' own US stores. If you cannot run a browser, say so and stop.

## Who is on it

Twenty-nine brands, in three batches. Four are retries of brands the first pass could not read on 13 October —
**LOFT** (PerimeterX "press and hold"), **TOTEME** (certificate warning), **Sam Edelman** (Cloudflare) and
**prAna** (bot wall). Try each once more, from a fresh tab, and if the wall is still up, try the brand's category
page through a search engine's cached link or a product URL from its sitemap; past ten minutes, `NC` and say what
you saw. The other twenty-five joined the register after the first worklist was cut: the Net-a-Porter additions with
one to five stores — shoe houses (Gianvito Rossi, Manolo Blahnik, Roger Vivier, Aquazzura, Loeffler Randall, Le
Monde Béryl), New York designers (Tibi, KALLMEYER, Wiederhoeft, Lauren Manoogian, Danielle Frankel) and the
rest. A shoe house bands on its flat or loafer entry; say so in `note`. `worklist.csv` carries the reason each
brand is here.

## Why

The women's map is up with 246 brands, and after the first pass 29 of them still show "Pending" for want of a
price read. This job closes the gap so every brand with a store of its own carries a band.

## What you return

`return.csv` in the columns of `return_template.csv`, one row per brand, all 29; `NOTE.md` per batch.
Nothing else.

Eight garments, seven cells each: `low`, `low_product`, `low_url`, `high`, `high_product`, `high_url`,
`basis`. **Every figure carries the product name and the product URL it was read from.** `basis` is
`pair` (entry version and elevated version of one staple), `range` (cheapest to dearest of the category,
because the brand sells no such pair) or `single` (one style, low = high). `NONE` where the brand does
not sell the garment; `np` where it sells it but publishes no price; `NC` where you could not look.
An empty cell is an error.

`band_proposed` is your reading of the rule below; the Spectrum thread sets the band at merge and
Sebastian rules.

## The garments

The three that set the band first, the rest for the record:

- **tee** — the plain short-sleeve cotton (or cotton-blend) t-shirt. Not a tank, not a bodysuit, not a
  graphic collaboration.
- **blouse** — a woven shirt or blouse with sleeves: button-front shirt, silk blouse, poplin shirt. Not a
  knit top, not a camisole. Where the brand makes only button-front shirts, say so; where it makes only
  blouses, say so.
- **sweater** — the crewneck pullover is the staple. Not a sweatshirt, not a cardigan unless that is all
  the brand knits (said so).
- **jeans** — a five-pocket denim jean.
- **trousers** — tailored or dress trousers; a chino or pull-on pant where that is all the brand makes,
  said so. Not leggings.
- **dress** — a day dress: the cheapest and dearest regular dress, `range` basis as standard, because
  no brand makes an "entry" and "elevated" version of one dress.
- **outerwear** — jackets and coats; not blazers, not shirt-jackets.
- **shoes** — own-label footwear; the flat or loafer is the staple, the dearest regular version the high.
  Stocked footwear (another brand's shoe sold on the site) is not the brand's. A brand that sells shoes
  but no flat or loafer is `range`, never `NONE`.

Swim, lingerie, activewear and sleepwear are not among the eight: a brand whose whole range is one of
those (Soma, Aerie, Wacoal, Eberjey, Hanky Panky, Commando, Natori, Jockey, Athleta, Beyond Yoga,
Varley, Sweaty Betty) returns `NONE` on what it does not sell and prices what it does; say in `note`
what the range is. The Spectrum thread will band those by hand.

## The band rule (men's, applied as is)

Basic: **core** tee entry at or under $35 and **core** blouse entry under $80 — the plain, year-round version of
each, not the cheapest item that fits the word (ruled 13 Oct: Aritzia's $28 ribbed baby tee and $58 smocked top
are not its core tee and shirt; its core tee is the $50 Essential, its core shirt $88+). Say in `note` when you
pass over a cheaper item for this reason. Otherwise the mean of the blouse entry and
the sweater entry: under $150 Premium, $150–400 Accessible, over $400 True Luxury. A shoe house (no
blouse, no sweater) bands on its shoe entry on the same cuts. Where the women's staples make the rule
read wrong for a brand (a knit house with no blouse, a dress house with no sweater), say so in `note`
and propose; the rule will be adjusted on the evidence, not guessed around.

## Rules (from the men's pass; the same words)

- **Low and high.** Low is the cheapest full-price version of the staple in the current main range.
  High is the top of the same staple's regular range: for sweaters, the dearest crewneck in an elevated
  fibre; for outerwear, the same style in an elevated material. Where no such pair exists, `basis` =
  `range`. **Elevated**: majority-cashmere blends; silk, alpaca, mohair, vicuña, superfine wool. Never
  fur, never shearling, never exotic skins. Collaborations, runway, limited editions and capsules are
  never a high.
- **Sub-lines** sold under the brand's name in its own store count (say which in `sublines_included`);
  archive reissues and capsules do not. A sister banner with its own stores (G by GUESS, Marciano,
  MICHAEL Michael Kors vs Collection) is its own name: read the worklist brand only and say what you
  excluded.
- **Full price only.** Sale, outlet and markdown prices are not prices; take the regular (compare-at)
  price on a marked-down product and check a second product before trusting a compare-at. Whole
  dollars, rounded half-up, exact figure in `note`. Read the US storefront; where a brand has none,
  read its own store in its own currency and **do not convert** (`USD_landed` where duties are
  included). Two displayed page prices confirm the currency.
- **Women's range only.** Several of these brands also sell men's; price the women's garment.
- Names must match `canonical_keys.txt` (the register spelling, capitals and ® included); run
  `python3 reconcile.py` before returning.
- Do not touch the map. `NOTE.md` per batch: what was read, what could not be, where the brief would
  have produced a confident wrong answer, and any brand that is not womenswear after all.

## Order and time box

`worklist.csv` is sorted by store count, largest fleet first, with a `batch` number; batches of ten,
returned as each is done. Fifteen minutes a brand; forty for LOFT, where a category-stratified read is fine if
you say so. Past the box, what you have, `NC` on the rest, said so.
