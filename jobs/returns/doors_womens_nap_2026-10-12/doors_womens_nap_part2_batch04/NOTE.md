# doors_womens_nap_2026-10-12 — Part 2 (screen), batch 4

**Part 2 worklist rows 61–80 (Miguelina → Terry Puesto). Screened 13 Oct 2026 in Chrome. `reconcile.py`: 20 exact, 0 to rewrite, 0 unmatched. No empty cells.**

## Result

| has_us_own_store | Brands |
|---|---|
| yes | 3 — Miguelina (1), RÙADH (1), Suzie Kondi (2) |
| no | 16 |
| NC | 1 — OTZI |

| Brand | US doors | Source |
|---|---|---|
| Miguelina | West Village, 69 8th Ave, NY 10014 | miguelina.com/pages/miguelina-west-village |
| RÙADH | SoHo studio, 160 Mercer St, Floor 2, NY 10012 (private appointments) | ruadh.com/pages/studio |
| Suzie Kondi | 15 Orchard St, NY 10002; 137 Main St, Amagansett NY 11930 | suziekondi.com/pages/our-stores |

All 4 doors are in `return_doors.csv`.

## Calls to check

1. **Appointment studios: the rule used so far.**
   - Counted when the brand publishes an address and books customers in:
     - RÙADH (this batch)
     - Danielle Frankel (batch 2)
     - AFLALO (batch 1)
   - Not counted when there is no address:
     - Sara Cristina ("our New York studio", email only)
     - Calle Del Mar (batch 1)
   - Not counted when the space is for the trade only:
     - Autumn Sonata (batch 1)
   - If appointment-only studios should come out, drop RÙADH, Danielle Frankel and AFLALO.
2. **OTZI is `NC`.** otzi.com is for sale. Net-a-Porter shows the designer as "Coming soon", and searches return only unrelated "Ötzi" results.
3. **Miguelina's home page is broken.** It redirects to a "Coming-Soon" 404 page. The West Village store page was found through the brand's own sitemap.
4. **Not clothing.**
   - SIX THE RESIDENCE is UK furniture (NAP sells its poufs).
   - SENSI STUDIO sells hats and bags.
   - Olympia Le-Tan makes book clutches.
   - RUE de VERNEUIL makes bags.
5. **Own stores abroad only.**
   - SHUSHU/TONG: 3 in China.
   - SKALL: 2 in Copenhagen.
   - Olympia Le-Tan: Paris.
   - RUE de VERNEUIL: Paris.
   - STOULS: Paris.

## Wrong or unreachable sites

Three were added to `wrong_sites.csv`:

- OTZI: `otzi.com` is for sale, and no brand site was found.
- STOULS: `stouls.com` and `stouls.fr` are for sale. The brand's site is `stouls.paris`.
- **Taller Marmo: web search turned up `gettallermarmo.shop`,** a look-alike "Official Boutique" that the brand does not link to. It is likely not genuine and was not opened. The brand's site is `tallermarmo.com`.

## Files

- `return_screen.csv`: 20 rows
- `return_doors.csv`: 4 rows
