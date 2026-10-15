# womens_crossover_a_2026-10-15 — which men's-map brands sell women's clothing in their US stores (187)

**Reissue of Part A of womens_crossover_2026-10-14.** The original thread was lost before any Part A batch came back. Part B (Chanel, Miu Miu) is already returned and merged — it is not in this pack.

**Issued** 15 October 2026 · **Kind** read · **batches of 25** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. Chrome job on the brands' own US sites. If you cannot run a browser, say so and stop.

## Why

The women's map shows a men's-map brand as a crossover only when the women's universe file lists it, and that
file was built from department-store floors. So Louis Vuitton, Hermès, Gucci, Dior, Fendi, Celine and The Row —
houses that sell women's in every store they have — are missing from the women's map, and so are Lululemon,
Gap, J.Crew, Zara and Uniqlo. Part A settles, for every men's-map brand with a US store that the women's
universe does not list, whether its stores sell women's clothing.

## Part A — 187 brands, one question each

`worklist_a.csv`, 8 batches of 25 (the last of 12), sorted by store count. Return `return_a.csv` in the columns of
`return_a_template.csv` (delete the two example rows); `NOTE.md` per batch, in `batch1/` … `batch8/`. Return batch by batch — batch 1 holds the brands that change the women's map most, so it matters first.

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

## Rules

- Names must match the canonical keys (`canonical_keys_a.txt`, `canonical_keys_b.txt`); run
  `python3 reconcile.py` against the right file before each return.
- `NC` nobody looked; `NONE` does not exist or does not apply; `np` not published. No empty cells.
- The brand's own site and locator only. Do not touch the map. Out of scope but noticed: `NOTE.md`.
- Nensi Dojaka and ASHLYN (seen on The RealReal's emerging list) are not on this worklist: neither has a US
  store of its own. If you see otherwise, a line in `NOTE.md`.
