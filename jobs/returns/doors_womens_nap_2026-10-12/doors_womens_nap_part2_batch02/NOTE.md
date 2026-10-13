# doors_womens_nap_2026-10-12 — Part 2 (screen), batch 2

**Part 2 worklist rows 21–40 (Camille Surault → Established). Screened 13 Oct 2026 in Chrome. `reconcile.py`: 20 exact, 0 to rewrite, 0 unmatched. No empty cells.**

## Result

| has_us_own_store | Brands |
|---|---|
| yes | 1 — Danielle Frankel (2 doors) |
| no | 19 |
| NC | 0 |

| Brand | US doors | Source |
|---|---|---|
| Danielle Frankel | New York Atelier, 260 W 39th St, 14th floor, 10018; Los Angeles Boutique, 8475 Melrose Place, 90069 | daniellefrankelstudio.com/pages/appointments |

`return_doors.csv` holds 3 rows: the 2 Danielle Frankel doors, plus one Donde Esteban pop-up that is not counted (point 2).

## Calls to check

1. **Danielle Frankel's two doors are bridal salons, by appointment.** They are counted because the brand publishes both addresses and books retail appointments at both. Drop them if appointment-only salons should not count.
2. **Donde Esteban: Miami pop-up, date unclear.** The page says "La Tiendita Donde Esteban opens November 1 at The Standard Spa, Miami Beach", with no year and no end date. It is recorded as a pop-up with status `NC` and not counted.
3. **Not clothing.**
   - Established is fine jewelry. The brief excludes jewelry, but the row is kept as screened.
   - CHRISTEN is footwear.
   - Déhanche makes belts.
   - Comme Si sells socks and hosiery.
4. **Placeholder pages.** Conner Ives' stockists and contact pages, and ESCVDO's contact page, show theme placeholder text. ESCVDO's shows a fake Albuquerque address. None of it was used.
5. **Own stores abroad only.**
   - Charo Ruiz: 3 in Spain.
   - Cortana: 3 in Spain.
   - DESTREE: 3 in Paris.
   - Clio Peppiatt: London.
   - Carine Gilson: Brussels.
   - Eka: Delhi.

## Wrong or unreachable sites

Three were added to `wrong_sites.csv`:

- Clio Peppiatt: `cliopeppiatt.com` is for sale. The brand's site is `cliopeppiatt.co.uk`.
- Danielle Frankel: `daniellefrankel.com` is a GoDaddy placeholder. The brand's site is `daniellefrankelstudio.com`.
- Donde Esteban: `dondeesteban.com` has no DNS. The brand's site is `dondeesteban.co`.

## Files

- `return_screen.csv`: 20 rows
- `return_doors.csv`: 3 rows
