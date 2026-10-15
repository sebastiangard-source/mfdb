# Batch 1 — womens_crossover_a_2026-10-15 (25 brands, Red Wing → Allen Edmonds)

Read 15 Oct 2026 in Chrome on each brand's own US site. `reconcile.py`: 25 exact, 0 rewrites, 0 unmatched.

## What was checked
- `womens_clothing`: 24 of 25 read from each brand's own US site (women's nav, category pages, product counts where shown).
- Result: 21 yes · 1 partial (Red Wing) · 1 no (Jos. A. Bank) · 1 NC (Allen Edmonds).

## What was not reached
- **Allen Edmonds**: the site shows a Cloudflare "verify you are human" page. I don't get past bot checks, so every column is `NC`.
- **`where`**: settled for only two brands. Lululemon is `some stores` because its US store directory lists a "Vail Village Men's Pop Up". Jos. A. Bank is `NONE`. The other 22 are `NC`. These locators give names and addresses, not departments. J.Crew's 114-store directory has no department data, and UNTUCKit's /pages/stores returns 404. Rather than guess `all stores` from a site-level Women tab, I left these as not checked. See the brief point below.

## What contradicted the existing record
- **Tecovas is not footwear only.** The brief lists it with the shoe houses. /shop/apparel/womens has 53 results, including suede and embroidered jackets, blouses and tees. Read as `yes`.
- **Red Wing is not quite footwear only either.** /apparel/womens has 8 results: 6 women's logo tees and hoodies (2 web exclusive) and 2 unisex tees. Under the brief's definition (a few styles counts as thin), that is `partial`. If the intent is that logo merch doesn't count, flip it to `no`. Your call, not mine.
- **Johnston & Murphy** (a shoe house) has a real women's apparel range: 110 products with coats, blazers, pants and dresses (the count includes socks and accessories).

## What the brief got wrong, or should look at
1. **`where` can't be answered from most locators in five minutes.** Women's at site level is quick to establish. Whether every door carries it usually isn't, because store pages rarely list departments. If `all stores` is meant to follow from "the site sells women's and no men's-only door is visible", say so and I'll apply that rule with that wording in `evidence`. Otherwise expect `where` to be mostly `NC`. Lululemon shows the risk: a men's-only door exists in an otherwise mixed fleet.
2. The brief points at `canonical_keys_a.txt` / `canonical_keys_b.txt`. The pack ships only `canonical_keys.txt`, which holds the 187 Part A names exactly (checked against `worklist_a.csv`). I used that file.
3. BOSS is read off hugoboss.com/us, which sells BOSS and HUGO together. The women's clothing there is clearly mostly BOSS-labelled, but I did not split it by label.

## Out of scope but noticed
- None this batch.
