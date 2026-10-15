# mens_links — batch 3 (thread 4)

Read 15 October 2026 in Chrome on each brand's own store. One `NC` cell per brand; only those were touched. `reconcile.py`: 25 names in, 25 exact.

**Result:** 25 cells → 16 filled, 9 left `NC`.

## Rule applied for parents
A parent page was used only when the garment is a real part of it. Examples:
- Officine Générale Knitwear: 8 knitted polos of 39, two in the first rows.
- Joe's Jeans Tops: 29 polos of 204.

When the parent held only one or two pieces of the garment, the cell was left `NC` with the count in the note:
- Lemaire, Margaret Howell, Our Legacy and Maison Margiela (polo).
- Norse Projects and Marine Layer (jeans).
- Ksubi (dress pants).
- Malbon (dress shirt).

## Left NC
| brand | cell | reason |
|---|---|---|
| Ksubi | dress_pants | Pants is track/cargo; 2 chinos of 34 |
| Lemaire | polo | 2 of 49 Tops |
| Maison Margiela | polo | /polos returns 410; "Polos" is only a filter on T-shirts, holding a V-neck tee and a knit top |
| Malbon | dress_shirt | no shirt page; 2 camp shirts |
| Margaret Howell | polo | 2 MHL woven polos of 43 |
| Marine Layer | jeans | Pants holds chinos, cords, joggers; no jeans |
| Norse Projects | jeans | 2 denim styles of 45 Trousers |
| Our Legacy | polo | one knitted polo in Knitwear |
| Pendleton | shoes | the only footwear page is unisex Shoes & Slippers, with women's slippers in the first rows. Needs the unisex ruling; URL in note |

## Flags
- **Ring Jacket shoes:** the store is the brand's own (JPY, menswear only), but the first tiles mix imported labels (Gaziano & Girling, Saint Crispin's, Baudoin & Lange) with its own sneakers.
- **Pages that are live but not in the nav:**
  - Luca Faloni /shop/sneakers.
  - PAIGE /collection/men-shoes, reached from the breadcrumb Men > Shoes.
- **Small shoe pages:**
  - Purple: one sneaker in 4 colours.
  - Rhude: Strada Runner.
- **Officine Générale:** `/collections/og-homme-polos` exists but is unlinked and holds only t-shirts, so it was not used.
- **Rhoback dress shirt:** Tailwind Performance Sport Shirts, which are knit button-downs.
- **Merz b. Schwanen dress shirt:** the Shirts page, which holds woven button shirts.
