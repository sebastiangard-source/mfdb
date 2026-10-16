# prices_crossovers_2026-10-15: women's prices for the 187 crossovers and the 4 Pending brands

**Issued** 15 October 2026 · **Kind** price · **Batches of ten, returned as each is done** · **Runs overnight, unattended** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job on the brands' own US stores. If you cannot run a browser, say so
and stop.

## Why

The Cyprus Brand Set bands every brand on the women's price rule. 187 of its brands are crossovers: men's-map
brands whose stores also sell women's. Each crossover is banded today on its **men's** shirt-and-sweater prices
at the women's cuts. A women's blouse and sweater can sit well away from the same house's men's shirt and
sweater, so those bands are the least certain on the map.

This pass reads the women's prices so the crossovers band on what they charge women. It also prices the four
brands that never got a price read and are hidden for it: Amsale, HANRO, Reem Acra and Wacoal.

## You are unattended

Sebastian is asleep while this runs. So:

- **Bot walls.** One plain try per site. If a check box, a press-and-hold check or any other wall appears, do
  not wait for anyone and do not work around it. File the row `held` in `status`, name the wall in `note`, and
  move on to the next brand.
- **Browser trouble.** If Claude in Chrome stops responding, stop there. Write `NOTE.md` for the batch you are on,
  saying which brands are done and which are not, so the work can resume.
- **Pace.** Read at a human pace: one product page at a time, no bursts of requests. A wall caused by speed
  costs the whole brand.
- **Rulings.** None can be asked for tonight. Where the brief does not settle something, take the reading that
  is easiest to undo, say so in `note`, and carry on.

## What you return

`return.csv` in the columns of `return_template.csv`, one row per brand; `NOTE.md` per batch, in `batch01/` …
`batch20/`. Nothing else.

Eight garments, seven cells each: `low`, `low_product`, `low_url`, `high`, `high_product`, `high_url` and
`basis`. **Every figure carries the product name and the product URL it was read from.**

- `basis` is one of three values:
  - `pair`: entry and elevated versions of one staple.
  - `range`: cheapest to dearest of the category.
  - `single`: one style, low equals high.
- Use `NONE` where the brand does not sell the garment for women, `np` where it sells it but publishes no
  price, and `NC` where you could not look. An empty cell is an error.

`band_proposed` is your reading of the rule below. The Spectrum thread bands at merge and Sebastian rules.

## The garments: women's, from the women's section only

The three that set the band come first:

- **tee:** the plain short-sleeve cotton or cotton-blend t-shirt. Not a tank, not a bodysuit, not a graphic
  collaboration.
- **blouse:** a woven shirt or blouse with sleeves (button-front shirt, silk blouse, poplin shirt). Not a knit
  top, not a camisole.
- **sweater:** the crewneck pullover. Not a sweatshirt; not a cardigan unless that is all the brand knits, and
  say so.

The other five are for the record:

- **jeans:** a five-pocket denim jean.
- **trousers:** tailored or dress trousers. A chino or pull-on pant where that is all the brand makes, said so.
  Not leggings.
- **dress:** the cheapest and the dearest regular day dress, on `range` basis.
- **outerwear:** jackets and coats; not blazers, not shirt-jackets. **Leather, suede, nappa, lambskin, calf
  hair and ponyhair are never the high.** Take the top non-leather piece; faux is fine.
- **shoes:** own-label women's footwear. The flat or loafer is the staple; the dearest regular version is the
  high.

**Unisex.** Where the women's section lists a unisex piece and it is the only version of the garment, price it
and flag `unisex` in `note`. Where the women's section is a thin edit of the men's range (a few tees and
hoodies), price what is there and say how thin it is.

**Shoe and athletic houses** (New Balance, Hoka, Asics, Salomon, Converse, Puma, Tecovas, Lucchese, Ariat,
Danner, Thursday Boot, Johnston & Murphy) price their women's clothing where it exists. Return `NONE` on what
they do not sell, and say in `note` what the women's clothing range is.

## The band rule (women's cuts, ruled 13–14 October)

- **Basic:** a core tee entry at or under $35, and a core blouse entry under $80. "Core" means the plain,
  year-round version of each, not the cheapest item that fits the word. Where there is no blouse, a core tee at
  or under $35 with another slot priced counts.
- **Otherwise**, take the mean of the blouse entry and the sweater entry: **under $200 Premium, $200–600
  Accessible, over $600 True Luxury.**
- Where the women's staples make the rule read wrong for a brand (a knit house with no blouse, a dress house
  with no sweater), say so in `note` and propose a band.

## Rules (the same as the women's price pass)

- **Low** is the cheapest full-price version of the staple in the current main range. **High** is the top of
  the same staple's regular range.
  - **Elevated** means majority-cashmere blends, silk, alpaca, mohair, vicuña or superfine wool. Never fur,
    shearling or exotic skins.
  - Collaborations, runway pieces, limited editions and capsules are never a high.
- **Sub-lines** sold under the brand's name in its own store count; say which in `sublines_included`.
- **Sister banners are their own names:** RRL is not Ralph Lauren, Carhartt WIP is not Carhartt, RLX is read as
  itself. Read the worklist brand only.
- **Full price only.** Take the regular (compare-at) price on a marked-down product, and check a second product
  before trusting a compare-at.
- Prices are whole dollars, rounded half-up, with the exact figure in `note`.
- **Currency:** read the US storefront. Where there is none, read the brand's own store in its own currency and
  do not convert. Paul Smith's US store is at the root path (`paulsmith.com/womens/clothing`); `/us/` sends you
  to the UK store.
- `womens_url_hint` in the worklist is the women's page the crossover pass found. Use it as a starting point,
  not as gospel.
- Names must match `canonical_keys.txt`. Run `python3 reconcile.py` before each return.
- Do not touch the map. Anything out of scope but noticed goes in `NOTE.md`.

## Order and time box

`worklist.csv` is sorted by store count, largest fleet first, in 20 batches of ten (the last is one brand).

- Work in batch order and return each batch as it is done.
- **Eight minutes a brand.** Fifteen for a very large house (Lululemon, Gap, J.Crew, Banana Republic, Zara,
  Uniqlo, Abercrombie & Fitch, Express).
- Past the box, return what you have, `NC` the rest, and say so.
- Expect to get through about half tonight. Wherever you stop, the batches already returned are worth more than
  a half-finished one.
