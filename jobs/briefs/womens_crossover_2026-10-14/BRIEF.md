# womens_crossover_2026-10-14 — which men's-map brands sell women's clothing in their US stores (187), and two houses the registers missed (Chanel, Miu Miu)

**Issued** 14 October 2026 · **Kind** read · **Part A in batches of 25, Part B as one return** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. Chrome job on the brands' own US sites. If you cannot run a browser, say so and stop.

## Why

The women's map shows a men's-map brand as a crossover only when the women's universe file lists it, and that
file was built from department-store floors. So Louis Vuitton, Hermès, Gucci, Dior, Fendi, Celine and The Row —
houses that sell women's in every store they have — are missing from the women's map, and so are Lululemon,
Gap, J.Crew, Zara and Uniqlo. Part A settles, for every men's-map brand with a US store that the women's
universe does not list, whether its stores sell women's clothing. Part B reads two houses that are on no
register at all because they have no menswear and no department-store floor: Chanel and Miu Miu.

## Part A — 187 brands, one question each

`worklist_a.csv`, batches of 25, sorted by store count. Return `return_a.csv` in the columns of
`return_a_template.csv` (delete the two example rows); `NOTE.md` per batch.

- `womens_clothing` — `yes`, `no` or `partial`. **Yes** means the brand sells a women's clothing range under
  its own name on its own US site: tops, knitwear, trousers, dresses or outerwear, not only shoes, bags,
  accessories or fragrance. **Partial** means a women's range exists but is thin (a handful of styles, a
  capsule, unisex sizing only) or is sold in some stores and not others. **No** means none.
- `where` — `all stores`, `some stores` (name how you know: the locator lists departments, or store pages say
  "Women"), `online only`, or `NONE`.
- `womens_url` — the women's landing page on the brand's own site, `NONE` if none.
- `evidence` — one line: what you saw. A Women tab with categories; a locator entry listing departments; a
  product count.
- A shoe or boot house whose women's range is footwear (Red Wing, Allen Edmonds, Alden, Blundstone,
  Birkenstock, Rothy's, Tecovas, Lucchese, Dr. Martens) is `no` with the note "women's footwear only". The
  women's map covers clothing.
- Sister banners are their own names: RRL and Ralph Lauren Purple Label are read as themselves; RLX likewise.
  Carhartt WIP is not Carhartt.
- Five minutes a brand; most take one. Past the box, `NC`, said so.

## Part B — Chanel and Miu Miu, the full women's read

Both houses sell women's ready-to-wear in their own US stores and appear nowhere in Cyprus's registers. Read
each as the women's jobs read the others, in one return of four files:

1. **Doors** — `return_b_counts.csv` and `return_b_doors.csv` in the columns of their templates: every US
   store on the brand's own locator, own-door / outlet / concession / pop-up, open or opening, street, city,
   state, zip, venue, operator. Department-store counters and boutiques inside Saks, Neiman Marcus,
   Bloomingdale's or Nordstrom are concessions, not doors — Chanel in particular has many. Fragrance and
   beauty counters are not doors. Forty minutes a house. The rules are those of `rules_doors_reference.md`
   (the women's doors brief), unchanged.
2. **Prices** — `return_b_prices.csv` in the columns of its template: the eight women's garments, entry and
   top, product and URL behind every figure, full price only, women's range only. Chanel publishes prices on
   chanel.com for ready-to-wear; where a piece is "price on request", `np`. The band rule is the men's: mean
   of blouse and sweater entry, $150 / $400 cuts (both will read True Luxury; the figures are for the record).
3. **Facts** — `return_b_facts.csv` in the columns of its template: what it sells, channels, founding,
   owner today (Chanel Limited is private; Miu Miu is Prada S.p.A., listed in Hong Kong — the annual report
   is the source), signature product, lookbook, resale (Vinted women's, The RealReal), B Corp / GOTS, one real
   quotation under `rules_quotes.md`, pronunciation.

`canonical_keys_b.txt` has the two names. One `NOTE_b.md` for the pair.

## Rules

- Names must match the canonical keys (`canonical_keys_a.txt`, `canonical_keys_b.txt`); run
  `python3 reconcile.py` against the right file before each return.
- `NC` nobody looked; `NONE` does not exist or does not apply; `np` not published. No empty cells.
- The brand's own site and locator only. Do not touch the map. Out of scope but noticed: `NOTE.md`.
- Nensi Dojaka and ASHLYN (seen on The RealReal's emerging list) are not on this worklist: neither has a US
  store of its own. If you see otherwise, a line in `NOTE.md`.
