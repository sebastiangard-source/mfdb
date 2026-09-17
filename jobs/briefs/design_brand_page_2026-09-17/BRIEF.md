# Design brief — the brand detail page

**17 September 2026** · for a design thread starting cold · returns a page design, not data

## The job

Design the brand detail page for **The Menswear Spectrum** (projcypr.us/mfdb), a map of 204
menswear brands arranged by what each one leads with rather than what it costs. The page exists
today (screenshots in this folder) and was built as a diagnostic view: every dial, every score,
every note, in the order the data arrived. It is complete and it is not a page a reader wants.

Design the page a reader wants. Seven brands are in `brands.json` with every field the map
holds on them — Todd Snyder, Rag & Bone, Theory, James Perse, Vince, Faherty, Marine Layer. They
were chosen because they are fully populated and because they differ: a tailoring-led house, a
denim house, a workwear-adjacent one, three jersey houses, a coastal one. A design that works for
all seven works for the map.

## What comes back

- The page as a self-contained HTML file rendering `brands.json` — one file, no build step, no
  external scripts beyond Google Fonts, working on a phone and a desktop, light and dark.
- A short note: what you designed for, what you left out and why, and what the data made hard.

Not a mockup image, not a Figma. The map is one HTML file and the page has to become part of it.

## The material

`brands.json` — one record per brand. `fields.json` says what every field is and what its absence
means; `rubric.json` is the definition of each dial. In brief:

| field | what it is |
|---|---|
| `band` | Premium · Accessible Luxury · True Luxury. Price sets only this. |
| `focus` | tech, comfort, craft, style — 1 to 5. What the house leads with. |
| `fabric` | denim, cashmere, linen, cotton, wool, synth — 1 to 5. What it is made of. |
| `dials` | cultural registers (golf, ivy, ital, fren, street, avant, prep, boat, racquet, ski, scandi, briish) 0–5 where 0 = not represented; scales (reach, dur, forg) 1–5; bipolar dials (fuss, golffice, bruv, sail) −3 to +3 where 0 is the centre; `shoes` 0–5. A dial **absent** from the record was never assessed and must not render as zero. |
| `natural_dial_derived` | 1–5, computed from the fibre count; absent = not assessed |
| `why` · `origin` · `opview` · `say` | why it is on the map; where it comes from; the house in its own words; how to say the name |
| `onething` | the one garment to buy: `p` product, `u` link, `n` note. `p` null with a note = checked, no signature garment. |
| `prices` | eight slots — T-shirt, Polo, Dress shirt, Jeans, Dress pants, Sweater, Outerwear, Shoes — each `[low, high]` in USD, `null` = does not make it, `"?"` = not assessed |
| `price_checked` | true when all eight were opened and read on the brand's own site |
| `fibre` | measured on the brand's own product pages: `t` styles, `w` stating a composition, `n/s/c` % natural / synthetic / cellulosic, `x` % with elastane, `xh` % at 5%+, `sp` one-cloth or split, `sc`/`nc` category lists, `st` complete or partial |
| `doors` | US own stores: coverage `full` with `n` count and `cities` [city, state, count] |
| `own_stores_northeast` · `stockists_northeast` | resolved shop records in the ten-state register: name, address, city, state, zip, type, `v` multigender, `ub` how many map brands it carries |
| `chan` | channels: O own store, D department store, I independent, W wholesale, X online only |
| `conf` · `forgc` · `forgv` | confidence in the record; forgiveness components and verdict |
| `notes` | one paragraph per dial explaining the score, keyed by dial name |
| `tech_evidence` | names a technology yes/no, origin of the marks, the marks themselves. Not a dial; evidence. |
| `site` | the brand's own store: domain, platform, feed |

Two held files are included because they are interesting and **must be marked as held if shown**:
`tech_depth_HELD.csv` (share of the range naming a technology — counted on colourways for some
rows, so not comparable across brands) and `tech_marks_HELD.csv` (the named fabrics and
technologies, with owner and kind — counts are floors).

## Doctrine the page must respect

1. **A checked absence and an unasked question must never look alike.** A dial that is absent is
   "not assessed"; a `0` is "not represented"; a price `null` is "does not make it"; a price `"?"`
   is "not assessed"; a one-thing with `p: null` and a note is "checked, no signature garment".
   Every one of these is a different fact and the page says which. Never render an absence as a
   zero, a blank, or a dash without a word.
2. **The map makes no negative judgements.** Seating is the endorsement. A low register score
   means the register is not represented, never that the brand is lesser. No "weak", no "poor", no
   red. Language and colour follow that.
3. **Every figure has a source.** Prices were read off the brand's site; fibre was counted on
   its product pages; doors were verified against its locator. The page can say so in a line, and
   should say when it can't (fibre `st: partial`, `price_checked` false).
4. **Words before numbers.** `why`, `origin`, `opview` are written, not scraped, and they are the
   reason a reader came. Dials and scores are evidence behind the words. The current page was
   recently reordered to lead with the words; keep that.
5. **Where to buy is a first-class answer.** Own stores and independent stockists in the
   Northeast, with a way to the shop.

## What the page has to do

- Open from a link (`#brand=Todd%20Snyder`) and from the map's hover card.
- Carry previous / next along the map order (the seven can stand in for that).
- Show the one thing, the prices, the range (fibre), and where to buy without making the reader
  scroll past thirty dials to reach them.
- Make the dials legible as a shape, not a list: what this house leads with, at a glance.
- Handle a house with no stockists (Todd Snyder: ten own stores, none independent) and one with
  thirty-seven (Faherty) with the same component.
- Work at 390px wide.

## Constraints from the existing page

- Palette: linen `#F5EFE4`, ink `#1F1D1A`, forest `#123B2B` and `#2E5F45`, the three bands have
  tints (Premium light, Accessible Luxury a warm mid, True Luxury deep green with light text).
  You may propose a change; say why.
- Typefaces on the site: a serif for names and headings, a sans for everything else. Google
  Fonts only.
- The page is inline in a single 870KB HTML file today. Your file is a standalone proposal; keep
  CSS and JS self-contained so it can be lifted in.

## What not to do

Do not invent data. If a field you want is missing for a brand, show its absence the way rule 1
says, and put the wish in your note. Do not add photography — the map carries none and has no
rights to any. Do not rank the seven against each other.
