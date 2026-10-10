# Wave C — restart note, 10 October 2026

Read this before `BRIEF.md`. A previous thread ran this wave and crashed part-way through the full
records (its last visible work was Dickies' product feed, page 1 of 4). What it finished is in this
folder; what it did not is the job. **This is a Chrome job**: the store section needs a browser.

## Done, do not redo

- **Facts-first for all 81 brands**: `facts_first.csv` — site, US store, own-store count, entry and top
  price with product and URL, band guess, mark. Carry its door counts and prices into `return.csv`
  where they are complete; it saves re-reading them. Its worklist corrections (angloitalian.com,
  badbirdiegolf.com, us.goldwin.global, outerlimits.co.jp for Nigel Cabourn, the Lardini and Universal
  Works .com redirects, the Edward Green / Asket / Aztech Mountain store notes) are accepted.
- **Rulings** on its five questions: `RULINGS_wave_c_facts_2026-10-10.md`. Short form: the brand's name
  on the door or it is not the brand's door (Flint and Tinder, Needles and Castaway are 0 with a stockist
  row; Pilgrim and Undefeated are own doors as multi-brand shops); residencies are pop-ups, Zadig's
  Archive stores are outlets, Oxxford's showroom is its one door; Nautica's "Comp. Value" is the regular
  price; bands are held for the Spectrum thread to set; marks as the logotype writes them (Zadig&Voltaire,
  Études, Alan Flusser, Budd, Closed); non-USD houses stay in their currency; `np` for Hickey Freeman and
  Oxxford.
- Also ruled since: operator- or licensee-run stores under the brand's banner count as own doors,
  flagged; a store in an outlet centre is an outlet whatever the brand calls it; a department-store
  counter with no sign of a branded shop is a `counter`, not a concession, counted nowhere.

## Not done — the job

1. **Section 4 in Chrome first for the ten `NC` door counts**: Birdwell, Danner, Dickies, Frye, Jos. A.
   Bank, Outdoor Voices, Rancourt & Co., UGG, Universal Works, Y-3. Zara's 69 is a floor from a city
   search, not a count — page its locator by state. Y-3: adidas.com puts up a robot check and y-3.com
   would not load for the last thread; try once in Chrome, then `NC` with the block in `note`.
2. **Then the full record for all 81**, worklist order, batches of ten: the 132 columns in
   `return_template.csv`, `own_doors.csv`, `stockists.csv`, `return_styles.csv`, `NOTE.md`. Do not
   write feed dumps into browser tabs; keep working files out of the return.
3. Nothing from the crashed thread's full records reached the Spectrum thread. If any batch of records
   was written before the crash, it is lost; start the records from the top of the worklist.

## Returns

`return_counts.csv` for the ten, then `return.csv` + `own_doors.csv` + `stockists.csv` +
`return_styles.csv` + `NOTE.md` in batches of ten. Names must match `canonical_keys.txt`; run
`python3 reconcile.py` before each return.
