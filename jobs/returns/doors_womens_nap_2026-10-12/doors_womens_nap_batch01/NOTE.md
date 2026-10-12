# doors_womens_nap_2026-10-12 — Part 1, batch 1 (pilot, revised)

**Worklist rows 1–10, read 12 Oct 2026 in Chrome. Revised after review. 9 brands returned; Anna Sui is left out by ruling. `reconcile.py`: 9 exact, 0 to rewrite, 0 unmatched.**

## Result

All nine brands return 0 US own doors, 0 outlets and 0 concessions, so `return_doors.csv` is header only. Each row names the page that was read.

| Brand | Brand's own site shows |
|---|---|
| adidas by Stella McCartney | A sub-line page on adidas.com/us. 0, as the brief expected. |
| Aje | 43 own doors, all in Australia and New Zealand. The US entries are stockists, listed in `return_stockists.csv`. |
| Alessandra Rich | No store page. `locator_url` = `none`. |
| Allude | A wholesale finder of about 326 rows with no US entry. Own doors are Kitzbühel and the Munich Cashmere Clinic. |
| Ann Demeulemeester | 3 boutiques: Paris, Milan, Antwerp. |
| Calvin Klein Collection | No door carries the Collection banner. 0, as the brief expected. |
| Cap d’Antibes | No store page. `locator_url` = `none`. |
| Cecilie Bahnsen | Copenhagen only. The US has 17 stockists, names only, in `return_stockists.csv`. |
| Christopher Esber | No store page on the US or AU site. `locator_url` = `none`. |

## Rulings applied from the review

- Anna Sui is left out of this return.
- `locator_url` = `none` where the brand's site has no store page. `read_method` lists every page that was tried.
- Stockists the brand names on its own site are recorded for the main thread in `return_stockists.csv`. That file covers the US only, gives full names and addresses as the brand writes them, and sets `channel` to store, online or NC.
- Sites that turned out to be wrong are listed in `wrong_sites.csv` (outputs root) for review at the end of the job.

## Stockists: points for the main thread

- Aje's own locator wrote one Aria address as "Nothing Bundt Cakes Baton Rouge, 7620 Corporate Blvd". It is kept exactly as written, with a flag.
- Cecilie Bahnsen's stockists page gives names only. Address, city and channel are therefore `NC`, and "Boyds Philadelphia" is marked "coming soon".
- Department stores and online stockists are kept with a flag, because the register rules exclude them and the main thread can drop them.

## Files

- `return_counts.csv`: 9 rows
- `return_doors.csv`: header only
- `return_stockists.csv`: 44 rows (Aje 27, Cecilie Bahnsen 17)
