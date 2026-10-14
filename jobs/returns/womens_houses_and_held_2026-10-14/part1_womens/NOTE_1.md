# womens_houses_and_held_2026-10-14 — Part 1: Chanel and Miu Miu

**Already returned, so I didn't re-read it.** This thread returned this read today as Part B of `womens_crossover_2026-10-14`. The four files here are those files, unchanged: `return_b_counts.csv`, `return_b_doors.csv`, `return_b_prices.csv` and `return_b_facts.csv`. `reconcile.py` against this folder's `canonical_keys.txt`: 2 exact, 0 rewrites, 0 unmatched. The templates have the same columns. Everything else is in `NOTE_b.md` from that return.

## Where the Part 1 spec differs from what was returned

1. **"Fragrance, beauty, eyewear and watch counters are not doors."** The 3 travel-retail fragrance counters are already left out. Chanel's 38 Fragrance & Beauty boutiques and 4 Watches & Fine Jewelry boutiques are a different case. They are standalone, Chanel-run stores with their own store pages, so they're counted as own doors with `banner_stated` saying which kind.
   - If the line is meant to cover them too, Chanel's US own doors drop from 70 to **28** (filter `banner_stated = CHANEL`).
   - One more row sits under concessions with the Watches & Fine Jewelry banner.
   - This needs a one-line ruling.
2. **Outerwear high.** These are already read under the 14 October ruling. Chanel's is a $16,550 coat in mixed fibres and Miu Miu's is an $8,200 cashmere-wool caban. Neither is leather, suede, fur, shearling, exotic, runway or capsule. Miu Miu "From the Runway" pieces were left out of every garment.
3. **Band** is left to the merge. Both blouse-and-sweater means are well above $600 (Chanel $2,675, Miu Miu $1,150).
4. **Channels.** Chanel is O;D (no fashion e-commerce in the US). Miu Miu is O;D. Neither has an I or W channel on its own site.
5. **Founding from the filing.** Not met.
   - Chanel's founding fields are `NC`, because the site gives no citable text.
   - Miu Miu's 1993 / Miuccia Prada comes from the Prada Group brand page. The investors page with the annual report returned "Access Denied".
6. **GOTS** wasn't checked for either. It's `NC`, not `NONE`.
7. **B Corp:** neither is in the bcorporation.net directory.
