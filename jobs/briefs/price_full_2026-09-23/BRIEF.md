# price_full_2026-09-23 — every price, every brand, once

**Issued** 23 September 2026 · **Kind** price · **Pilot** 8 brands first · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This brief supersedes every earlier price brief. It exists because the
September pass read only the garments the map lacked; the five core garments on most brands are
earlier figures nobody has verified. **This pass reads all eight garments for all 203 brands on one
basis, on one set of rules, with the product behind every figure, so the question never has to be
asked again.**

## What you return

`return.csv`, one row per brand, all 203; `NOTE.md`. Nothing else.

Every garment has seven cells: `low`, `low_product`, `low_url`, `high`, `high_product`, `high_url`,
`basis`. **Every figure carries the product name and the product URL it was read from.** That is what
makes a price auditable a year on, and it is not optional. `basis` says what kind of pair the cell is:
`pair` (entry version and elevated version of one staple), `range` (cheapest to dearest of the
category, because the brand sells no such pair), `single` (one style, low = high).

Per brand: `store_used` (the URL of the storefront read), `currency`, `search_url` (the brand's own
site search with the query empty, tested to return results for a garment word the brand uses;
`NONE` for overlay-only search), `sublines_included` (which sub-lines were counted, `-` for none),
`status`, `read_date`, `source`, `note`.

## The rules — all of them, in one place

**Garments.** Tee; polo; dress shirt (woven, collared, button-front; a casual button-down where that is
all the brand makes, said so); jeans; dress pants (or chinos where a brand has no dress trouser, said
so); sweater (the crewneck pullover is the staple; not a sweatshirt); outerwear (jackets and coats;
not blazers, sport coats or shirt-jackets); shoes (own-label footwear; the loafer is the staple).

**Low and high.** Low is the cheapest full-price version of the staple in the current main range.
High is the top of the same staple\u2019s regular range: for sweaters, the dearest crewneck in an elevated
fibre; for outerwear, the same jacket style in an elevated material; for shoes, the dearest regular
loafer. Where no such pair exists, `basis` is `range` and the cells are the cheapest and dearest
regular item in the category. Where the entry version is already the premium fibre, high is the
dearest regular version and a named judgement is fine.

**Elevated** (ruled 18 Sep): majority-cashmere blends; silk, alpaca, mohair, vicuña, superfine wool.
Never fur, never exotic skins. Collaborations, runway, limited editions and capsules are never a high.

**Sub-lines** (ruled 18 Sep): a sub-line sold under the brand\u2019s name in its own store counts (Ghost,
Crown Crafted, Blue Tab, ESSENTIALS, MM6, DRKSHDW). Archive reissues and capsules do not. A sub-line
seated as its own key on the map (RLX, RRL, Purple Label, Veilance) is its own row and never counts
toward the parent; on ralphlauren.com filter by label and say how.

**Own-label shoes.** The brand\u2019s name on the shoe, whoever made it. Stocked footwear \u2014 Dr. Martens
under Margaret Howell, Tricker\u2019s under evan kinori \u2014 is not the brand\u2019s, whatever the vendor field
says. A brand that sells shoes but no loafer is `range`, never `NONE`. `NONE` means it sells none.

**Full price only.** Sale, outlet and markdown prices are not prices; take the regular (compare-at)
price on a marked-down product, and check a second product before trusting a compare-at (Everlane\u2019s
repricing and Joe\u2019s Jeans leave stale ones). Whole dollars, rounded half-up, exact figure in `note`.

**Store and currency.** Use the domain in `worklist.csv`; prefer the store\u2019s US storefront where one
exists; otherwise read the listed store in its own currency and **do not convert**. `USD_landed` for
prices that include duties. The currency test is two feed prices confirmed against the displayed page
on the market path; `Shopify.currency.rate` is a hint only. Record `store_used`.

**Tokens.** `NC` nobody looked. `NONE` the brand sells no such garment. `np` the brand publishes no
price for it. An empty cell is an error.

## Failure classes, every one seen on this map

- A category page shows the nearest N, not all; \u201cShow more\u201d may not load the tail. Read the count.
- The vendor field lies (fifteen houses so far). Judge by the label on the product.
- Two number formats on one site (Cucinelli `$ 1.650,00` and `$1,200.00`); `1 495 USD` at NN07.
- A brand filter that leaks other items and inflates counts (ralphlauren.com); per-label category
  pages are clean.
- A root feed in the base currency while the page shows US prices (Eleventy, Incotex, Aspesi, Ami).
- A round feed total (Todd Snyder\u2019s 3,200).
- Sites that block browsers: Saint Laurent, Gucci, Balenciaga, Bottega Veneta, Celine. Try a fresh
  profile with extensions off, then their listing JSON; a robots-disallowed path is in bounds. If
  still unreadable, `NC` with the exact block in `note`, and say so in `NOTE.md` for a human read.
- No store to read: Comme des Garçons, Junya Watanabe, Charvet, Sugar Cane, Rakho (all `NC`, noted).
  Cesare Attolini\u2019s e-boutique was under maintenance on the 18th; check again.

## Method

Run brands in parallel batches as the September pass did; one written spec for every agent, and
this brief is that spec. Every batch is spot-checked against live pages before it goes into
`return.csv`. **Where the map already holds a figure (`worklist.csv`, `current_prices`), reproduce it
before replacing it**, and where you cannot, say which was filed and why.

Send the pilot first and stop: **Paul & Shark, Levi\u2019s, Peter Millar, Massimo Dutti, Fear of God,
Loro Piana, Wythe, Isaia** \u2014 an inherited-price house the tier pass got wrong, a mass brand, a
sub-line house, a low-price accessible house, a designer house at accessible prices, a house whose
entry is already cashmere, a small DTC house, a non-US-domain house.

## Time box

Twenty minutes on a Shopify house, forty on anything else, seventy-five on a luxury house with a WAF.
Past that, `NC` with a note.
