# womens_dials_2026-10-14 — listing links, fibre, fabric, tech and craft for the 180 women's brands (and the men's listing-link gaps)

**Issued** 14 October 2026 · **Kind** read · **Built to run in parallel: batches of ten, any thread takes any batch** ·
**Returns to** the Spectrum thread

Read `audit_protocol.md` first, then `rules_garment_links.md`, `rules_fibre.md`, `rules_craft.md` and `rubric_craft.txt`.
Chrome job on the brands' own US stores. If you cannot run a browser, say so and stop.

## Why

The women's map has stores, prices, facts and a band for every brand, and no dials. The men's map's focus dials
(tech, comfort, craft, style) and fabric dials (denim, cashmere, linen, cotton, wool, synthetic) rest on evidence
read from each brand's site: named technical fabrics, the craft facts, and a count of styles by main fibre. This
job reads the same evidence for the women's brands so the same dials can be set — and, while on each site,
takes the listing link for each of the eight garments, which the women's price pass never asked for.

## Running in parallel

`worklist.csv` is sorted by store count with a `batch` number, ten brands each, 18 batches. Threads do not need
to coordinate beyond picking a batch nobody has taken: say in your first line which batch you hold. Each batch
returns on its own as `batch<NN>/return.csv`, `batch<NN>/return_styles.csv` and `batch<NN>/NOTE.md`. The Spectrum
thread merges batches in any order. Work the batches in number order unless told otherwise — the big fleets
first.

`mens_links/` is a separate, smaller job for a thread with time left: 92 men's brands missing a listing link for
one or more garments they sell (four batches of 25, three minutes a brand). Same link rules; the template is
`mens_links/return_template_mens.csv` and the keys `mens_links/canonical_keys_mens.txt`.

## What you return, per brand (`return_template.csv`, one row)

**A. Listing links** (`rules_garment_links.md`, read "women's" for "men's"). The URL of the brand's own women's
listing for each garment it sells — tee, blouse (shirts and blouses), sweater (knitwear), jeans, trousers, dress,
outerwear, shoes. A navigation category page first; a collection page; a parent category; a women's-filtered
search last. Women's only on the first two rows of tiles; stable; live; the brand's own store. `NONE` where the
worklist says the garment is not sold (`<garment>_sold = no`). `links_kind` says which kind you mostly used.
Three minutes.

**B. Fibre by style** (`rules_fibre.md`, `schema_styles.json`). One row per style in `return_styles.csv` —
composition, lead fibre, lead percentage, elastane, pure/blend, the women's clothing category — and the roll-up
in the brand row: `styles_total`, `styles_with_composition`, the natural / synthetic / cellulosic split, spandex
count, `shape` (one cloth story or two), the natural and synthetic categories. **Sampling is allowed on this
job**: read every style up to 80; above that, a stratified sample of 80 across the categories, said so in
`sample_basis` with the total the site shows. Women's clothing only — not bags, jewelry, swim, lingerie,
beauty, kids. Fifteen minutes; thirty for a house with a large feed.

**C. Fabric emphasis** — six to seven figures, 1–5, read off the style table you just built, not judged:
`fab_denim`, `fab_cashmere`, `fab_linen`, `fab_cotton`, `fab_wool`, `fab_synth`, and `fab_silk` (women's ranges
run on silk in a way men's do not; the Spectrum thread decides whether it becomes a dial). The scale: 5 the fibre
leads the range (over 40% of styles by lead fibre), 4 a pillar (20–40%), 3 present (8–20%), 2 a few styles
(under 8%), 1 none. `fab_basis` gives the share behind each figure in one line.

**D. Tech** — `tech_named_fabrics` (the brand's own trademarked or named technical cloths, `NONE` if none),
`tech_owned_or_licensed`, `tech_share_of_range` (the share of styles that carry a named technical fabric),
`tech_evidence_url`, and `proposed_tech` 1–5: 5 the house is built on its own performance fabric (Lululemon,
Vuori), 4 a performance line with named fabrics is a pillar, 3 named technical cloths in part of the range, 2
a stretch or water-resistant claim without a named fabric, 1 none. Five minutes.

**E. Craft** (`rules_craft.md`, `rubric_craft.txt`) — the six facts (owned facility, named makers, named mills,
made-in share, heritage claim, process documented), two URLs, `proposed_craft` and the reasoning. A famous name
earns nothing. Ten minutes.

`status` is `read`, `partial` (past the box, said what was skipped) or `NC`. `note` carries anything the columns
cannot.

## Rules

- Names must match `canonical_keys.txt`; run `python3 reconcile.py` before each batch return.
- `NC` nobody looked; `NONE` does not sell or do; `ND` a page read that states no composition. No empty cells.
- Women's range only on brands that also sell men's.
- Never a workaround for a bot wall: one plain retry a few minutes later, then `NC` and what you saw.
- Do not touch either map. Out of scope but noticed: the batch `NOTE.md`.

## Time box

About thirty-five minutes a brand, so a batch is five to six hours of thread time; four threads on four batches
clear the top forty brands in an afternoon. Past the box on a brand, return what you have with `partial` and move
on — a batch with ten partial rows beats a batch that never returns.
