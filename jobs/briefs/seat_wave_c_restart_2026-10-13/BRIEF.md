# seat_wave_c — restart, 13 October 2026: the last 41 brands

**Issued** 13 October 2026 · **Kind** seating evidence · **Batches of ten, each returned as done** · **Returns to** Sebastian, who passes them to the Spectrum thread

You are picking up a job that is half done. Read `audit_protocol.md` first, then this file to the end,
then `HANDOFF_2026-10-12_from_batch4.md`, which the previous session wrote for exactly this purpose: it
has the method that worked, the traps found, and every ruling received. The rules files in this folder
are the standing rules and win over any shorthand. **You gather and propose; Sebastian rules.** This is
a Chrome job; if you cannot run a browser, say so and stop.

## Where the job stands

Wave C is 81 brands (`worklist.csv`). Batches 1–4, rows 1–40 (Alan Flusser through Kiel James Patrick),
are returned and seated on the map at v3.55.0. The door-count job for the ten `NC` brands is done.
**Rows 41–81 remain: 41 brands, `worklist_remaining.csv`, batches 5–9** (batch 9 is one brand, Études).

The batch 5 brands, Lady White Co. through Needles, may have been started by the previous session;
nothing from them was delivered. Start batch 5 from the beginning.

## What you return, per batch of ten

Exactly what batches 1–4 returned, in the same folder shape (`wave_c/out/batchN/`):

- `return.csv` — 132 columns from `return_template.csv`, one row per brand
- `own_doors.csv` — one row per door, every row with street, city, state (`own_doors_template.csv`)
- `stockists.csv` — the brand's own stockist list, US rows, `shop_kind` filled (`stockists_template.csv`)
- `return_styles.csv` — one row per style, `schema_styles.json`
- `NOTE.md` — what was read, what could not be, where this brief would have produced a confident
  wrong answer, and a numbered **For ruling** list at the end

Names must pass `python3 reconcile.py` against `canonical_keys.txt`. Tokens: `NC` nobody looked,
`NONE` does not sell or do, `np` sells it but publishes no price. No empty cells.

## Brands that need a word before you start

- **Large houses** — Lands' End, Mango, Muji, Nautica, Puma, Zara, UGG: a category-stratified style
  sample is allowed (ruled 10 Oct); count the full catalogue and say in `status` that the sample is not
  proportional. **Zara's 102 US doors, UGG's 10 + 36 outlets, Jos. A. Bank's and Danner's are already
  counted and registered from the 10 Oct counts job: do not re-read those locators**; carry the counts
  into `own_doors_us` and say so in `doors_basis`. Universal Works (3 UK + 3 operator-run abroad, 0 US)
  likewise. Outdoor Voices, Rancourt & Co., Birdwell and Frye were read in that job too (see
  `RULINGS_wave_c_facts_2026-10-10.md`); Rancourt's Lewiston factory address is for ruling, not a door.
- **Y-3**: adidas.com is not to be retried (ruled 10 Oct). Read what y-3 publishes elsewhere on
  adidas's own pages only if reachable without the bot check; otherwise `NC` with the block named.
- **Needles**: keep the worklist key `Needles`; Nepenthes New York is its own-door question — raise it,
  don't decide it.
- **Shoe and boot houses** — Meermin, Quoddy, Rancourt & Co., UGG: check for clothing before writing a
  style table; `NO_STYLES` where there is none (Carmina / Edward Green pattern); seven `NONE` price
  slots and a `pair` or `range` on shoes is the expected row.
- **Non-US houses** — Lardini, Pini Parma, Nigel Cabourn, Oliver Spencer, Private White V.C., Studio
  Nicholson, Undercover, Études, Represent, Nudie, Spier & Mackay, Samuelsohn: read the US storefront
  where one exists; otherwise the brand's own store in its own currency, **no conversion**, `USD_landed`
  where duties are included.
- **Worklist notes asking for a "floor ruling"** (Lands' End, Mango, Muji, Nautica): count doors, row
  outlets as outlets, put the floor question in `NOTE.md`.

## Rulings in force (the files have the full text; these are the ones that bite most)

- Collaborations are out of prices and the style layer; a shoe house whose every shoe is a collaboration
  gets shoes = NONE. Capsules, limited editions and licensed lines (team, league) are never a high.
- A licensee's line sold under the brand on the brand's own store is own label (Frye / Moda Piel).
  Sub-lines sold under the brand's name count (G-Star RAW Research, Gap's GapStudio).
- Own door only if the brand's name is on the door. Operator-, licensee- or distributor-run stores count,
  flagged. Women's-only stores count, flagged. A store in an outlet centre is an outlet whatever the
  locator calls it; a store in a regular mall is not an outlet because the locator's tab says so.
  Department-store counters and undated department-store "pop-ups" are concessions, not counted.
  Dated pop-ups are rows, not counted. Posted hours a customer can use make a door; by-appointment
  doors count, flagged.
- Puerto Rico is US; Guam and other territories are listed but not US doors.
- Every own-door row needs street, city and state, or the map seats a count and holds the rows
  (G-Star needed a second read for this).
- The state code `NC` is North Carolina. It is never a token in the state column.
- `proposed_tech` stays `NC`; fill `tech_named_fabrics` fully — the Spectrum thread authors tech from it.
- Marks as the logotype writes them; the worklist key stays in `brand`.
- Elevated fibres: majority-cashmere blends, silk, alpaca, mohair, vicuña, superfine wool. Never fur,
  shearling or exotic skins. Horsehide and cordovan are not exotic.
- Styles, not colourways: count by model or SKU stem; a handle count is a colourway count.

## Order and time box

Batch 5 first, in worklist order; then 6, 7, 8, 9. Forty minutes a brand for a full record, fifteen
for a shoe house; past that, what you have, `NC` on the rest, said so. Return each batch as it is done
with its `NOTE.md`; do not wait for the next. If you write a handoff of your own at the end, keep the
shape of the one in this folder.

## Added 13 October, midday: the previous session's code and inputs

`wave_c/code/` holds every script the earlier session wrote (fibre.py, assemble_b4.py, meta_b4.py,
helpers_b4.js, dump.js and the batch 1–3 versions), `wave_c/raw/` its per-batch inputs and notes, and
`wave_c/out/` the four returned batches and the counts job, so you can see exactly what a finished
batch looks like and reuse the scripts. They are tools, not rules: where a script and a rules file
disagree, the rules file wins. Deliver your batches into `wave_c/out/batch5/` onward, beside these.
