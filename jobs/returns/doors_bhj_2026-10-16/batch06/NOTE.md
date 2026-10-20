# doors_bhj_2026-10-16 · batch 6 · 16 Oct 2026

Batch 6 covers the rest of fragrance (Creed, Frédéric Malle, Kilian Paris, Penhaligon's, Santa Maria Novella, Officine Universelle Buly, Acqua di Parma) and the first of skin and body (Aesop, Kiehl's, L'Occitane).

`reconcile.py` returned 10 exact matches, 0 rewrites and 0 unmatched. For every brand, the rows match its counts. No cell is empty.

| Brand | Own | Outlet | Concession | Stockists | US locator rows |
|---|---|---|---|---|---|
| Creed | 14 | 0 | 0 | 240 | 254 |
| Frédéric Malle | 5 | 0 | 0 | 12 | 17 |
| Kilian Paris | 2 | 0 | 0 | NC | 2 |
| Penhaligon's | 1 | 0 | 0 | 8 | 11 |
| Santa Maria Novella | 7 | 0 | 0 | 0 | 7 |
| Officine Universelle Buly | **NONE** | 0 | 0 | 0 | 0 |
| Acqua di Parma | 1 | 0 | 0 | NC | 1 |
| Aesop | 72 | 0 | 0 | 4 | 77 |
| Kiehl's | 57 rows (56 stores) | 0 | 0 | 1,172 | 1,238 |
| L'Occitane | 116 | 0 | 0 | 0 | 116 |
| **Total rows** | | | | | 275 |

## Pace and walls

**No bot wall or check box appeared on any site.** Pages were read one at a time. Chrome stopped responding for a while partway through Aesop; once it was back, the work picked up where it stopped.

## Calls made

- **Department-store doors under the store's own name are stockists**, as you ruled. This covers Creed (about 130), Frédéric Malle (12), Kiehl's (about 316) and Aesop's one Saks door.
- **Penhaligon's** names its Saks and Bloomingdale's doors "Penhaligon's Saks …", which looks like a brand-named counter. Its locator types them "Stockist", though, so they're counted as stockists, not concessions. That's the opposite of Byredo, where the locator's own type said "Department Store". Say if you want them moved to concessions.
- **Outlet centres:** Creed Woodbury Common and 13 L'Occitane stores sit in outlet centres, but both locators file them as ordinary boutiques. They're returned as own-door with a note, as with Arhaus The Loft.
- **Kiehl's Mall of America** is listed under the name "Mall of America", but the locator gives it its own Kiehl's store page, as it does for every Kiehl's store and no retailer. So it's an own door.
- **Not returned:**
  - Aesop Seaport, Boston: its locator name is "Permanently Closed".
  - Penhaligon's Rockefeller: status CLOSED.
  - Penhaligon's Arielle Shoshana, Fairfax: type Store, status DISABLED.
- **Status opening:** L'Occitane Plaza Las Americas in Puerto Rico, which is named "¡Muy Pronto - remodelación!".
- **Buly is `NONE`.** Its locator lists no US city.

## Weak spots

- **Kilian and Acqua di Parma stockists are NC.** Their retailers sit behind an address search I couldn't run: Kilian's box wouldn't take typed text, and I didn't try Acqua di Parma's.
- **Aesop's count doesn't match.** Its US page says 78 locations, but its pages yield 77 distinct entries.
- **Aesop's city field is the metro city.** For example, the Venice and Pasadena stores are filed under Los Angeles, with the real locality in the street line.
- **Kiehl's Tysons Corner is listed twice** under two city slugs. Both rows are returned and noted.
- **Missing phones or ZIPs:**
  - Santa Maria Novella: no phones on its list. The state is taken from the city for Boston, Miami, Las Vegas and Costa Mesa.
  - Acqua di Parma: no ZIP for Miami.
- **Typos are kept as the locator gives them, with notes:**
  - L'Occitane: "Cincinnatti", "Charlotteville", and ZIP "6110" for West Hartford.
  - Frédéric Malle: Prince Street phone "+1 329 …".
- **L'Occitane's "View all stores" list returns 116 US stores in one go.** It's a big chain on the brief's list, but the locator returns its whole US list at once, so nothing needed paging.

## Your centres

- **The Street Chestnut Hill:** Kiehl's and L'Occitane (both 199 Boylston St).
- **Wrentham Village Premium Outlets:** L'Occitane.
- **Seaport:** Aesop's locator still lists Aesop Seaport (70 Pier 4 Blvd) but names it "Permanently Closed", so it isn't returned.

## Le Labo (batch 5)

Now read from the link you sent: 47 own doors and 77 stockists. Batch 5's files are updated.
