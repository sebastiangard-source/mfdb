# Delta, 12 October 2026 — 883 doors added, 2 removed

`delta_2026-10-12.csv` holds 883 doors that were not in `locations_db_v1.csv` as issued on 11 October: same
columns, same rules. Geocode them exactly as the brief says and return them in a second file,
`return_delta_2026-10-12.csv`, in the return template's columns. Do not re-run the original rows.

Where they come from:
- 165 are North Carolina stores (132 women's, 33 men's) that the 11 October build dropped by mistake: the
  state code NC was read as "not counted". Fixed on 12 October.
- The rest are new reads since the file was issued: Express (220), Jos. A. Bank (174), Zara (101), The North Face (58), Nike (40), Fjällräven (21), On (19), UGG (10), and smaller fleets.

Two door_ids from the 11 October file no longer exist (366189d77678, fca3adb216bf); omit them or return them
as NC with the note "removed on 12 Oct" — either is fine.
