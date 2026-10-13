# doors_womens_nap_2026-10-12 — Part 1, batch 4

**Worklist rows 31–40. Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. No empty cells in any of the three files.**

## Result

Two brands have a US door of their own:

| Brand | US door | Source |
|---|---|---|
| RIXO | 19 Prince St, New York 10012 (Nolita) | rixolondon.com/en-us/pages/stores |
| Sanderlak | 2 E Broadway, New York 10038 (flagship) | sanderlak.com/pages/nyc-store |

Seven brands come back 0. Posse is `NC`: its site could not be found (point 1). No brand in this batch has a US outlet or concession.

| Brand | Own doors on the brand's site | US stockists recorded |
|---|---|---|
| Maryam Nassir Zadeh | 1, Paris. NY now listed as "Online" | none published |
| Maticevski | 0 | 1 (Forty Five Ten; the rest are online) |
| Matteau | 1, Noosa Heads, Australia | 27 |
| Olivia von Halle | 2 branded concessions (Harrods, Bon Marché) | 13 |
| Posse | `NC` | — |
| Rivage | 0 | none published |
| RIXO | 8 (4 London stores, NY, Liberty takeover, Bicester and Kildare villages) | none published |
| Rodarte | 0 | 15 |
| ROTATE Birger Christensen | 1, Copenhagen | locator disabled |
| Sanderlak | 1, New York | none published |

## Where the brief would give a confident wrong answer

1. **Posse's site could not be found.** posse.com.au, the domain press links to, now redirects to an unrelated lifestyle-article site, so the domain may have lapsed or been taken over. posse.co is for sale, and posseofficial.com does not load. The row is `NC`. Checking the brand's Instagram bio link by hand is the quickest fix.
2. **Maryam Nassir Zadeh's New York shop is no longer listed.** The contact page now gives New York store hours as "Online" and the address as the website. The only physical store named is MNZ Paris (97 rue La Fayette), so US is 0. The Lower East Side shop is well known and may still be on older registers.
3. **ROTATE's store locator is switched off.** /store-locator returns "Store Locator is currently disabled". The flagship page gives one store, Copenhagen. US own doors are 0, but no stockist list could be read.
4. **Swimwear and sleepwear, not ready-to-wear.** Rivage is swim. Olivia von Halle is silk nightwear. Matteau is swim and resort. None looks like a "likely to own a US store" brand.

## How data was read

- Each brand was read from its own store, stockist or contact page, found from the site navigation. Matteau's US list sits behind an "America" tab, which was clicked open. Maticevski's sitemap was read in full to confirm it has no store page.
- **Stockist addresses:**
  - Matteau and Olivia von Halle give full addresses.
  - Rodarte gives name and city only, grouped by state.
  - Maticevski gives names only.
- **Address errors kept as written and flagged:**
  - Matteau writes one Southampton elysewalker as "New York NY 11968", spells "San Franciso" and "Sag Harbour", and puts Grand Cayman and Vancouver in its US list. Those two were left out.
  - Olivia von Halle's Nashville entry carries a stray "CO 81657".

## Wrong or unreachable sites

Four were added to `wrong_sites.csv`:

- Maryam Nassir Zadeh: `mnzstore.com` redirects to a domain auction. The brand's site is `maryamnassirzadeh.com`.
- Matteau: `matteau.com` does not load. The brand's site is `matteau-store.com`.
- Posse: the brand's site was not found (point 1).
- ROTATE Birger Christensen: `rotate-birger-christensen.com` does not load. The brand's site is `rotatebirgerchristensen.com`.

Rivage was found through a Vogue Scandinavia article (`rivageswimwear.com`). Rodarte's `rodarte.net` redirects to `shoprodarte.com`, and RIXO's `rixo.co.uk` redirects to `rixolondon.com`. Both are the brands' own sites.

## Files

- `return_counts.csv`: 10 rows
- `return_doors.csv`: 2 rows
- `return_stockists.csv`: 56 rows
