# doors_womens_nap_2026-10-12 — Part 2 (screen), batch 1

**Part 2 worklist rows 1–20 (&Daughter → Calle Del Mar). Screened 13 Oct 2026 in Chrome. `reconcile.py`: 20 exact, 0 to rewrite, 0 unmatched. No empty cells.**

## Result

| has_us_own_store | Brands |
|---|---|
| yes | 2 — AFLALO, B SIDES |
| no | 17 |
| NC | 1 — Away That Day |

| Brand | US door | Source |
|---|---|---|
| AFLALO | The Studio, 56 Greene St, 3rd Floor, New York 10012 (walk-ins and appointments) | aflalonyc.com/pages/the-studio |
| B SIDES | Our Store, 445 Warren St, Hudson NY 12534 | bsidesjeans.com/pages/our-store |

Both are in `return_doors.csv`.

## Calls to check

1. **Appointment showrooms are not counted.**
   - Calle Del Mar has a Los Angeles showroom, by appointment only and with no address.
   - Autumn Sonata has a Tribeca showroom, reserved for trade clients.
   - Both are `no`.
   - AFLALO's third-floor studio is counted, because the brand says it is open to walk-ins.
2. **Away That Day is `NC`.** Its site is password-locked for maintenance, so nothing could be checked.
3. **Not clothing.**
   - AMANU sells sandals, bags and belts.
   - By Pariah is a jewellery label.
   - Autumn Sonata is mainly home textiles.
4. **Own stores abroad, none in the US.**
   - BONDI BORN: Bondi Beach and Noosa.
   - BLAZÉ Milano: Milan.
   - CALL IT BY YOUR NAME: seasonal Saint-Tropez shop.
   - BONDI BORN's US list includes We Wear Australian, a multi-brand store in SoHo. It is not a BONDI BORN door.

## Method

Each brand was checked the same way: the home page nav and footer links, the full page sitemap (Shopify), and any store, stockist, showroom, visit or contact page. Every brand's domain had to be found, because `site_domain` is `NC` throughout the worklist. Stockists were not recorded in Part 2, which is a screen only.

## Wrong or unreachable sites

Two were added to `wrong_sites.csv`:

- AARON ESH: `aaronesh.com` has an SSL error. The brand's site is `aaronesh.co.uk`.
- BLAZÉ Milano: `blazemilano.com` is for sale. The brand's site is `blaze-milano.com`.

## Files

- `return_screen.csv`: 20 rows
- `return_doors.csv`: 2 rows
