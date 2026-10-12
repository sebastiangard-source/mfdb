# doors_womens_nap_2026-10-12 — Part 1, batch 2

**Worklist rows 11–20. Read 12 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. No empty cells in any of the three files.**

## Result

Two brands have a US door of their own:

| Brand | US door | Source |
|---|---|---|
| Elie Saab | 860 Madison Avenue, New York 10021 (flagship) | eliesaab.com boutique finder |
| Extreme Cashmere | 152 Mercer St, New York 10012 (SoHo) | extreme-cashmere.com "our stores" |

The other eight brands come back 0. No brand in this batch has a US outlet or concession.

| Brand | World doors on the brand's site | US stockists recorded |
|---|---|---|
| Deiji Studios | 2, both AU | 52 |
| Elie Saab | 19 entries named ELIE SAAB | 27 |
| Emilia Wickstead | 1, London | 19 |
| Extreme Cashmere | 3 (Amsterdam, New York, St. Moritz) | none published |
| Galvan | 1, London Loft (by appointment) | 21 |
| Giuliva Heritage | 0 | 7 |
| God’s True Cashmere | 0. The LA address is a mailbox suite | none published |
| Goldbergh | no locator (`none`) | none published |
| Haight | 7, all in Brazil | none |
| HIGH SPORT | 0. The Hamptons event was a past pop-up | 38 |

## How data was read

- **Elie Saab.** The boutique finder renders from a stockist.co widget. All 177 rows were read from the widget's own feed, which is the data the page displays, rather than by searching city by city. That turns up 28 US rows: the flagship and 27 resellers.
- **Bridal salons are not concessions.** Elie Saab's feed tags Bergdorf Goodman and Neiman Marcus bridal salons as "Resellers/Bridal", so they are recorded as stockists, not concessions.
- **HIGH SPORT.** The page has 22 region tabs that do not switch on a scripted click, so the panels were read straight from the rendered page. All 51 rows were captured.

## Stockist quality: points for the main thread

- **Deiji Studios.** The brand writes several addresses incompletely or wrongly, and every one is kept as written and flagged:
  - "307 e. ojai avenue #100, ca" gives no city.
  - "kansas city ka" uses a code that is not a state.
  - "bethesda ma" and "beverly hills la" have the wrong state.
  - "mangesset" is the brand's spelling of Manhasset.
- **Emilia Wickstead and Galvan** give name and city only, so street and ZIP are `NC`. Galvan files Bergdorf Goodman under "LONGVIEW", which looks like an error on the brand's page.
- **Elie Saab** files four NY kids' shops with city "New York" and the real town (Monroe, Chappaqua, Cedarhurst, Brooklyn) in the street line. They are kept as written and flagged.
- **One Deiji stockist is in a WS property.** Onyx Boutique, 27 Boylston St, Chestnut Hill MA, is at The Street Chestnut Hill.

## Wrong or unreachable sites

Two were added to `wrong_sites.csv`:

- HIGH SPORT: `highsport.net` does not exist. The brand's site is `high-sport.com`.
- Haight: `haight.com` is unreachable. The brand's site is `haight.com.br`.

## Where the worklist was wrong

- **Haight is a Brazilian label** with no US presence at all on its own site, so it may not belong in "likely to own a US store".
- **Giuliva Heritage and HIGH SPORT** each publish a "stores" page that is wholesale only. Read quickly, either page could be mistaken for a door list.

## Files

- `return_counts.csv`: 10 rows
- `return_doors.csv`: 2 rows
- `return_stockists.csv`: 164 rows
