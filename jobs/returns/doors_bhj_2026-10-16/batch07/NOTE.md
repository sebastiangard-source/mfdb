# doors_bhj_2026-10-16 · batch 7 · 16 Oct 2026

Batch 7 covers the rest of skin and body (Fresh, Malin+Goetz, Origins, Sisley Paris, La Mer, Augustinus Bader) and the first of makeup (MAC Cosmetics, Charlotte Tilbury, Glossier, Bobbi Brown). Following your note, only stores under the brand's own name are own doors.

`reconcile.py` returned 10 exact matches, 0 rewrites and 0 unmatched. For every brand, the rows match the own-door counts. No cell is empty.

| Brand | Own | Concession | Stockists | US locator rows |
|---|---|---|---|---|
| Fresh | **NC** | NC | NC | NC |
| Malin+Goetz | 10 | 0 | 217 | 227 |
| Origins | 4 | 0 | 505 | 509 |
| Sisley Paris | 11 | 0 | 304 | 315 |
| La Mer | **NONE** | 0 | 438 | 438 |
| Augustinus Bader | **NONE** | 0 | 292 | 292 |
| MAC Cosmetics | 84 | 2,978 (not rows) | 0 | 3,062 |
| Charlotte Tilbury | 2 | 1,266 (not rows) | 0 | 1,268 |
| Glossier | 9 | NC | NC | 9 |
| Bobbi Brown | 1 | 0 | 1,924 | 1,925 |
| **Total rows** | | | | 121 |

## Decision needed: MAC and Charlotte Tilbury counters

Both locators list every counter one by one, under the brand's name:

- MAC: "MAC Cosmetics at Macys", "… at Ulta", "… Sephora at Kohl's", and so on.
- Charlotte Tilbury: "CHARLOTTE TILBURY - SEPHORA …", "… ULTA …", and so on.

The brief makes these concessions and says they're returned. Your note for this batch says only stores under the brand's own name count. I've counted them as concessions, with the breakdown in `return_counts.csv`, but **haven't returned them as rows**. That would be about 4,250 rows, the addresses are all on the locators, and it's about two hours of reading. Say if you want them.

- **MAC: 2,978.** Ulta 1,402, Sephora at Kohl's 851, Macy's 329, Dillard's 128, Sephora 118, Nordstrom 86, Belk 46, Bloomingdale's 16, and 2 others.
- **Charlotte Tilbury: 1,266.** Ulta 588, Sephora 547, and the rest in Nordstrom, Bloomingdale's, Saks, Cos Bar and two malls.

Bobbi Brown, La Mer, Origins, Sisley and Augustinus Bader list their counters under the store's own name ("Nordstrom", "ULTA"), so those are stockists, as you ruled.

## Calls made

- **La Mer and Augustinus Bader are `NONE`.** La Mer's US locator has no La Mer store. Augustinus Bader's locator has "Augustinus Bader Store" and "Augustinus Bader Counter" categories, but no US entry carries either.
- **Fresh is `NC`.** Its locator returns nothing for any search, US or abroad, and the page throws a script error while loading. No wall was shown. That may mean the US boutiques have closed, but the locator doesn't say so.
- **Origins:** four doors carry the Origins name.
  - Harvard Square, Cambridge, and Market Common Clarendon, Arlington VA, are typed "Origins". Market Common Clarendon is listed under that name only.
  - Disney Springs is named Origins, with its type left blank.
  - The San Juan airport shop is in the Dufry terminal; operator is Dufry.
- **Sisley Paris:** 11 Sisley-named entries.
  - 8 are "Maison" stores.
  - "SISLEY-PARIS MAISON NEW YORK" is at the same address as "Maison New York". Both are returned and noted.
  - "Sisley-Paris Boutique Las Vegas" is on the same street as Maison Las Vegas.
  - "Sisley Spa at The Dominick" is a hotel spa, not a shop. Say if spas shouldn't count.
- **MAC:** 84 stores, a separate group on its locator, including 8 MAC Pro and 1 in Puerto Rico. The locator returns no detail for 3 of them, so their phones are NC.
- **Charlotte Tilbury:** only the 2 "Beauty Wonderlands" are its own (Aventura Mall and The Grove).
- **Bobbi Brown:** one own store, Bobbi Brown - The Studio in Montclair NJ.
- **Malin+Goetz:** 10 US apothecaries, plus Hong Kong.

## Weak spots

- **Glossier gives no ZIPs or phones** (NC). It also says it's "in all freestanding Sephora stores" without listing them, so its concessions are NC.
- **Sisley Maison Las Vegas has no ZIP.** Three Sisley entries have no phone.

## Your centres

None of your five centres has an own door from this batch. The nearest are MAC Prudential Center and Origins Harvard Square.
