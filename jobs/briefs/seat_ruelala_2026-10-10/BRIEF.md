# seat_ruelala_2026-10-10 — four men's seats and eleven women's door reads

**Issued** 10 October 2026 · **Kind** seating evidence + locations · **Facts-first for the four, returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. The rules files in this folder are the standing rules and win over any
shorthand here. **You gather and you propose; Sebastian rules.** This is a Chrome job for the store
locators; if you cannot run a browser, say so and stop.

## Why

Rue La La's featured-brands list was checked against every register on 10 October. Of 39 names,
16 are on the men's map, 11 are in the women's registers, and 12 are nowhere. Four of the twelve are
men's business the map should carry; seven are women's brands whose stores the women's register
needs; one, Tommy Bahama, is both. This brief closes all of it in one pass.

## Part 1 — four men's seats (`worklist_seat.csv`)

The `seat_resort` record, exactly as the wave briefs: `facts_first_template.csv` first for all four
(fifteen minutes a brand, returned before anything else), then the 132-column `return_template.csv`,
`own_doors.csv`, `stockists.csv`, `return_styles.csv` (`schema_styles.json`) and `NOTE.md`.

- **Tommy Bahama** is the one that matters. It is a men's clothing house with its own US fleet, and
  it slipped every seating wave. Its locator mixes stores, outlets and the restaurant-bar sites; return
  one row per door with `format` and say in `note` where a store shares an address with a restaurant.
  The women's line is sold in the same stores and on the same site: count the men's range only for
  prices and fibre, and say so.
- **Christian Louboutin, Giuseppe Zanotti, Jimmy Choo** are shoe houses with men's lines, and shoe
  houses seat (ruled 8 October): seven `NONE` price slots and a `pair` or `range` on shoes is the
  expected row. Their locators list women's boutiques, men's boutiques and department-store doors
  together. A boutique that stocks men's shoes is an own door; a women's-only boutique is still the
  house's door and counts; a shop inside Saks or Neiman is a `counter` unless the locator shows a
  branded shop. Say in `doors_basis` how many of the own doors carry men's.

Bands are set at merge by the price rule (tee and dress-shirt entry for Basic; the mean of
dress-shirt and sweater entry above that; a shoe house on its shoe entry). You propose; Sebastian
rules.

## Part 2 — eleven women's door reads (`worklist_womens_doors.csv`)

The `doors_womens_2026-10-10` return, exactly: `return_doors.csv` and `return_counts.csv` in the two
templates here, same columns, same definitions, same rules, so the rows merge into the women's store
register without reconciliation. For every brand: the brand's own US locator in Chrome, every US
location, one row per door, `format` = own-door, outlet, concession or pop-up, `operator` where a
partner runs the door. Tommy Bahama's doors come back with Part 1; do not read them twice.

Two of these are also a question about the department-store index returned on 10 October:
**Escada** and **Hale Bob** are carried by department stores but did not surface in the nine-store
women's index. Open the Nordstrom, Bloomingdale's and Macy's women's clothing brand filters and say
whether the brand is there under another spelling, under a sub-line, or not at all. One line each in
`NOTE.md`.

**Chanel** publishes no wholesale and its locator covers fragrance and beauty counters as well as
boutiques; return only doors the locator types as a fashion boutique (ready-to-wear, bags, shoes),
and say how it labels them.

## Rules (standing; the files win over this list)

- **The brand's own locator is the only source for a door.** Not Google Maps, not a mall directory,
  not press. If the locator cannot be read even in Chrome, `NC` with the exact block in `note`.
- **Own door means the brand's name on the door at full price.** A store in an outlet center is an
  outlet whatever the locator calls it (ruled 10 October). A shop-in-shop with no sign of a branded
  shop is a `counter`, kept in the file and counted nowhere. Operator-run doors under the banner
  count, flagged.
- **Prices:** full price, the brand's own US store, two displayed page prices confirm the currency;
  capsules, collaborations, factory and made-for-outlet styles excluded; shearling excluded from
  highs; licensed lines (team, NFL) excluded.
- **Fibre:** styles not colourways, main fabric line only, composition as the page writes it;
  `styles_total` is the whole men's range even where composition is sampled.
- Names must match `canonical_keys.txt`; run `python3 reconcile.py` before returning.
- `NC` nobody looked; `NONE` looked and found none; an empty cell is an error.
- Do not touch the map. Return the files and `NOTE.md`: what was read, what could not be, and
  where this brief would have produced a confident wrong answer.

## Order and time box

Facts-first for the four seats, returned at once. Then Tommy Bahama in full, then the three shoe
houses, then the women's doors in worklist order. Forty minutes a brand for a full record, fifteen
for a doors-only read; past that, what you have, `NC` on the rest, said so.
