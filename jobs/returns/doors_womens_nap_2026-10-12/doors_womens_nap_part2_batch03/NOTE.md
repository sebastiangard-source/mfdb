# doors_womens_nap_2026-10-12 — Part 2 (screen), batch 3

**Part 2 worklist rows 41–60 (FANE → MFPEN). Screened 13 Oct 2026 in Chrome. `reconcile.py`: 20 exact, 0 to rewrite, 0 unmatched. No empty cells.**

## Result

| has_us_own_store | Brands |
|---|---|
| yes | 3 — KALLMEYER (2), Kartik Research (1), MAISON MAYLE (1) |
| no | 17 |
| NC | 0 |

| Brand | US doors | Source |
|---|---|---|
| KALLMEYER | Flagship, 83 Orchard St, New York; Madison Avenue, 1022 Madison Ave, NY 10075 | kallmeyer.nyc/pages/stockists; /pages/contact-sub-store-info |
| Kartik Research | KARTIK RESEARCH, NEW YORK, 61 Orchard St, NY 10002 | kartikresearch.com/pages/stockists |
| MAISON MAYLE | 33 Great Jones St, New York (Tue–Fri 12–6, else by appointment) | maisonmayle.com/pages/store |

All 4 doors are in `return_doors.csv`. Two have ZIP `NC`, because the page gives none: KALLMEYER Orchard St and MAISON MAYLE.

## Calls to check

1. **Many brands in this batch are not clothing.**
   - Jewelry, which the brief excludes: Joelle Kharrat, Le Sundial.
   - Jewelry and accessories, per its own terms page: Julietta.
   - Footwear: JUDE (NAP sells boots and pumps).
   - Bags: Liffner.
   - Homeware: Fourth Street and LOUISE ROE (Danish design objects).
2. **lemlem only had a pop-up.** 199 Mulberry St, New York, ran 11–16 June 2026 and has ended. It is not counted.
3. **Brand names shared with other businesses.**
   - JUDE was matched to thejude.com by the NAP products.
   - LOUISE ROE is the Copenhagen design brand at louise-roe.com, not the presenter's "Front Roe" label.
4. **Own stores abroad only.**
   - Loretta Caponi: Florence and Forte dei Marmi.
   - LIÉ STUDIO: Copenhagen.
   - MFPEN: Copenhagen.
   - Maygel Coronel: Cartagena.
   - Ilkyaz Ozel: Istanbul.

## Wrong or unreachable sites

Three were added to `wrong_sites.csv`:

- **FLORE FLORE: `floreflore.com` redirects to a fake "Apple Security Center" scam page.** Nothing on that page was touched. The brand's site is `flore-flore.com`. Do not open the bad domain.
- Liffner: `liffner.com` is an unrelated illustrator's site. The brand's site is `liffner.co`.
- Loretta Caponi: `lorettacaponi.com` gives a certificate error, which was not bypassed. The brand's site is `lorettacaponi.it`.

## Files

- `return_screen.csv`: 20 rows
- `return_doors.csv`: 4 rows
