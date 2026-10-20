# doors_bhj rulings, 16 Oct 2026

- Batch 2 merged; batch 1 replaced by the thread's revised return (with `us_stockists`, Boucheron re-read to 4 boutiques + 4 Saks shops).
- One door per address: two locator entries at the same street and ZIP (Catbird's Williamsburg Wedding Annex, upstairs) are one store. Applied at build.
- Missoma: no own US store (`NONE`); shown on the Brand Set as "no US stores".
- Yellow Rose by Kendra Scott is a sister banner, not counted under Kendra Scott.
- Stores marked opening are listed in the return but not counted until open.
- Venue must come from the locator. Venues inferred from an address (batch 1: Cartier, Bulgari, Van Cleef, Graff, David Yurman) are to be blanked to `street` by the thread.
- visvim craft 5 (Sebastian, 16 Oct): the construction is the product; the Dissertation pages document the brand's own making and name its mills. Men's map v3.58.3.
- Batch 3 merged (fine jewelry, first five home brands). RH held at a slider check (7 of 66 galleries filed; shown as still counting). Aurate has no locator on its own site: NC, still counting.
- Open for ruling: RH Interior Design (Palm Desert) as an own door; Arhaus "The Loft" (9) own-door or outlet.
- Batch 4 merged (rest of home, B&B Italia pulled forward). Poltrona Frau "Branded Space" areas inside dealers' showrooms: concessions, as filed. Design Within Reach's Herman Miller and Knoll partner stores: stockists. RH still held.
- Batch 5 merged (beauty stores and the first fragrance houses). Sephora inside Kohl's: concessions (1,146), not counted. Ulta Beauty inside Target: none on Ulta's directory. Jo Malone London department-store doors under the store's own name: stockists, as ruled in batch 1. Space NK: no US store. Le Labo: locator would not load, NC.
- One store per door at build: rows are merged when they share a street (and ZIP, or city where no ZIP) or a ZIP and phone. Rows with no street and no phone are never merged (Ulta's directory gives neither).
- Batch 6 merged (rest of fragrance; Aesop, Kiehl's, L'Occitane). Penhaligon's Saks and Bloomingdale's doors: stockists, as its locator types them. Stores in outlet centres that the locator files as boutiques (Creed Woodbury, 13 L'Occitane) stay own doors, flagged. Buly: no US store. Le Labo: locator never loaded (three tries), NC.

## Batch 7 and Le Labo (merged 16 October, v0.47)

- **MAC and Charlotte Tilbury counters** ("MAC Cosmetics at Macy's", "CHARLOTTE TILBURY - SEPHORA") are concessions, counted and not returned as rows (MAC 2,978; Charlotte Tilbury 1,266). Own doors: MAC 84, Charlotte Tilbury 2.
- **A hotel spa is not a store**, like a restaurant. Sisley Spa at The Dominick is dropped at merge. Ruled by Sebastian, 16 October.
- La Mer and Augustinus Bader `NONE`; Fresh `NC` (locator returns nothing, script error, no wall).
- Le Labo read after Sebastian's link: 47 own doors.
- **Counters are never rows, department stores included** (ruled by Sebastian, 16 October). A counter or shop-in-shop inside another store, even one the locator names as the brand's, is not returned as a row. Give its count in `us_concessions` only if the locator makes that easy; otherwise `NC`. Applies to doors_bhj and doors_tel from here on.
- Batch 8 merged 20 October (v0.51): NARS 2 own doors (Houston, Paramus Garden State Plaza); Fenty Beauty `NONE`. The worklist is complete; RH held, Le Labo read, Aurate and Fresh `NC`.
- doors_tel batch 1 (travel) merged 20 October (v0.55): Away 14, Monos 5, Rimowa 15, Calpak 1, Briggs & Riley 7 (two dealer-run by Sunsations, two airport stores), Samsonite 2 full-price (Faneuil Hall, Century City) with 77 outlets; Béis and July `NONE`; Tumi held (PerimeterX press-and-hold); Paravel `NC` (site gone, reported shut in 2025; Sebastian to say whether to drop it).
