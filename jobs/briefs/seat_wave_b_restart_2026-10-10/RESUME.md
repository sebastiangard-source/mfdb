# Wave B — restart note, 10 October 2026

Read this before `BRIEF.md`. A previous thread ran this wave and stopped. What it finished is in this
folder; what it did not is the job. **This is a Chrome job**; the first thread's facts-first pass ran
without a browser and a quarter of its store counts came back `NC`.

## Done, do not redo

- **Store counts and addresses for 24 brands**, read in Chrome from each brand's own locator:
  `held_door_counts.csv` (one row per brand) and `own_doors.csv` (1,051 US rows). The 24: Asics,
  Balmain, Church's, Clarks, Columbia, Converse, Fred Perry, G/FORE, Greyson, Helmut Lang, Hoka, John
  Lobb, Kenzo, Lanvin, Lucchese, Maison Kitsuné, Marni, Moose Knuckles, Palace, Sperry, Thursday Boot,
  Timberland, True Classic, Vans. For these, section 4 of the record is complete — carry the counts into
  `return.csv` (`own_doors_us`, `own_doors_world`, `locator_url`, `doors_basis`) and do not re-read
  the locators. Helmut Lang stays `NC` on doors (no locator on its site; HTTP 410).
- **Worklist corrections**, already accepted: Eddie Bauer's stores closed (0), G.H. Bass's closed in
  2020 (0), Human Made's NYC store was a pop-up, Kapital has stockists only, The Kooples has no US
  door, Saturdays NYC's Crosby St appears closed, Veilance's SoHo store was a 2016 concept; Emporio
  Armani's 99 US locations are 92 department-store counters (concessions); Vivienne Westwood's domain
  is viviennewestwood.com.

## Rulings already made (also in RULINGS_2026-10-08.md)

- Bands are set by the Spectrum thread from the full read, by the dress shirt and sweater. Do not
  guess bands.
- Operator- or licensee-run stores under the brand's banner count as own doors, flagged in `note`.
- Marks as the logotype writes them, corporate tails dropped: G.H.BASS, Thursday Boot, Greyson,
  **Schott N.Y.C.** (the header on schottnyc.com writes it so).
- **Outlets judged by location stand as outlets**, with the note saying so: a store in an outlet
  centre is an outlet whatever the locator calls it (Timberland 21 full-price / 54 outlet; Hoka's
  Orlando and Las Vegas rows stay as listed, flagged).
- G/FORE Pebble Beach and Balmain's appointment-only Beverly Hills salon count as own doors, flagged.
- Puerto Rico rows stay: the map is the US, and it already carries San Juan.

## Not done — the job

1. **Section 4 for the other 30 brands**, in Chrome, first: Aether Apparel, Ariat, Belstaff, Bogner, Carhartt WIP, Chubbies, Crockett & Jones, Eddie Bauer, Emporio Armani, Fjällräven, G.H. Bass, Hart Schaffner Marx, Helly Hansen, Human Made, John Elliott, Kapital, Kjus, Koio, Nanamica, On, Rapha, Rowing Blazers, Salomon, Saturdays NYC, Schott NYC, Snow Peak, The Kooples, Turnbull & Asser, Veilance, Vivienne Westwood. One row per door into `own_doors.csv` (append; same columns), one count row each.
2. **Then the full record** for all 54, worklist order, batches of ten: the 132 columns in
   `return_template.csv`, `stockists.csv`, `return_styles.csv`, `NOTE.md`. Stockists read in the
   browser with each batch.
3. The facts-first file from the first thread never reached the Spectrum thread. Do not redo it; the
   full record contains everything it had.

## Returns

`own_doors.csv` (appended), `return_counts.csv` for the 30, then `return.csv` + `stockists.csv` +
`return_styles.csv` + `NOTE.md` in batches of ten. Names must match `canonical_keys.txt`; run
`python3 reconcile.py` before each return.
