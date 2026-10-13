# doors_womens_nap_2026-10-12 — Part 1, batch 3

**Worklist rows 21–30. Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. No empty cells in any of the three files.**

## Result

Lauren Manoogian is the only brand in this batch with a US door of its own:

| Brand | US door | Source |
|---|---|---|
| Lauren Manoogian | 407 Broome Street, New York 10013 | laurenmanoogian.com/pages/store |

The other nine brands come back 0. No brand in this batch has a US outlet or concession.

| Brand | Own doors on the brand's site | US stockists recorded |
|---|---|---|
| Hunting Season | none | 11 names, no addresses (mostly online) |
| Joseph | 29 JOSEPH-named points abroad; none in the US | 5 (all Neiman Marcus) |
| Lauren Manoogian | 1, New York | none published |
| Le Kasha | 1, Paris (by appointment) | 7 |
| Les Vacances D’Irina | 2, both Bucharest | 5 |
| Lido | none | 10 |
| Mad | none (not a clothing brand; see below) | none |
| Magda Butrym | 1, Warsaw | 17 |
| Marrakshi Life | 1, Marrakech (store and atelier) | 10 |
| Mary Katrantzou | none | 12 |

## Where the worklist was wrong

1. **Mad is a watch brand.** Net-a-Porter's "Mad" is MAD Paris, which customises luxury watches. Its one NAP US product is a $103,000 Audemars Piguet Royal Oak, and madparis.com is a contact form only. It belongs with the jewelry and watch names the brief already excluded. It is recorded here as 0 with that note.
2. **Not clothing, or not likely to own a US store:**
   - Hunting Season is a handbag label.
   - Lido is Italian swimwear.
   - Les Vacances D’Irina is a Romanian resort label whose only stores are in Bucharest.
   - None of them looks like a "likely to own a US store" brand.
3. **Joseph has no US store, despite its name.** Its locator lists 60 points worldwide. The 29 JOSEPH-named ones are all outside the US, including branded concessions at Harrods, Harvey Nichols and Bon Marché. Its 5 US rows are Neiman Marcus, named as Neiman Marcus and not flagged as JOSEPH concessions, so they are recorded as stockists.

## How data was read

- **Joseph's** locator is a stockist.co map (the same widget as Elie Saab in batch 2). All 60 rows were read from the widget's own feed, which is the data the map displays.
- **Magda Butrym's** US stockists sit behind North America › USA tabs, which were clicked open.
- **Mary Katrantzou's** list sits in country accordions, which were read from the page's markup.
- **Every other brand** was read from its own stores, boutique or stockists page, found from the site navigation.

## Stockist quality: points for the main thread

- **Names and places only.** Hunting Season, Le Kasha, Les Vacances D’Irina, Lido and Marrakshi Life publish no street addresses, so street and ZIP are `NC`.
- **Joseph** puts the state in the city field on four of its five US rows. Each is corrected and flagged.
- **Marrakshi Life's** list may be out of date: it still names "Barney's New York, Naples FL" and spells Neiman Marcus "Nieman".
- **Lines that cover several cities.** Lido lists elysewalker (NY/LA/Newport Beach) and Goop (Mauna Lani/Sag Harbor) on one line each. The Webster appears the same way for Marrakshi Life. Each line was split into one row per city and flagged.

## Wrong or unreachable sites

One was added to `wrong_sites.csv`:

- Hunting Season: `huntingseason.com` is an unrelated hunting-dates site, and `huntingseason.co` is parked. The brand's site is `hunting-season.com`.

Lido's site, `lido-lido.com`, was found through a brand directory listing. Le Kasha, Les Vacances D’Irina, Magda Butrym, Marrakshi Life and Mary Katrantzou are on the domains you would guess.

## Files

- `return_counts.csv`: 10 rows
- `return_doors.csv`: 1 row
- `return_stockists.csv`: 77 rows
