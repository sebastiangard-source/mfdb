# Batch 8 — womens_crossover_a_2026-10-15 (12 brands, Massimo Dutti → Yohji Yamamoto), and the whole return

Read 15 Oct 2026 in Chrome on each brand's own US site.

## Batch 8
- Result: 9 yes · 3 no.
  - NN07 and Turnbull & Asser: men's only.
  - Sperry: women's footwear only.
- `where`: `NC` throughout, locator not read.
- **Pilgrim Surf + Supply** is a multi-label shop. The `yes` rests on about 12 Pilgrim-branded women's pieces across four categories. It's close to the line.
- **Yohji Yamamoto**: the store lists women's by line. The `url` points to the mainline "Yohji Yamamoto" women's collection. Y's, S'YTE, Ground Y and LIMI feu are separate lines on the same store.

## The whole file
- `return_a.csv`: 187 rows in worklist order. `reconcile.py` gives 187 exact, 0 rewrites, 0 unmatched. No empty cells. All values are legal, and every `no` row has `where`/`url` set to `NONE`.
- `womens_clothing`: **120 yes · 8 partial · 56 no · 3 NC**.
- `where`: 2 `some stores` (Lululemon, Buck Mason), 56 `NONE`, 129 `NC`.

### Still NC
- **Allen Edmonds**: Cloudflare human check, retried at the end and still blocked.
- **Chrome Hearts**: the site isn't a catalogue; no ready-to-wear is sold online for either sex.
- **Comme des Garçons**: the site has no shop and its store list is Japan only.

### Rulings collected from the notes, each easy to find in `note`
1. **Ungendered sites → `no`**, tagged `UNGENDERED SITE` (10 rows): Supreme, Brain Dead, Stüssy, Golf Wang, Palace, Awake NY, Denim Tears, Evan Kinori, Lady White Co., Freenote Cloth. Flip them together if ungendered should count as `partial`.
2. **Unisex named on the site → `partial`**: Industry of All Nations, Gallery Dept.
3. **Made-to-order women's only → `partial`**: Billy Reid, Alan Flusser.
4. **Sister banners**:
   - Sid Mashburn → `no`, because women's is sold as Ann Mashburn, a separate name.
   - visvim WMV and Officine Générale's OG Femme → `yes`, because both carry the house name on the house's own store.
5. **Footwear houses with women's clothing** (the brief's list was wrong for these):
   - Tecovas, Lucchese, Johnston & Murphy, Danner and Thursday Boot → `yes`.
   - Red Wing and Clarks → `partial`.
   - Timberland → `partial`, but provisional because a bot wall cut the read short.
6. **Small ranges read as `yes`** that could be `partial`: Aimé Leon Dore, Snow Peak, Pilgrim Surf + Supply.

### Rows changed after they were first returned
- Supreme, Brain Dead, Stüssy, Golf Wang: `partial` → `no` (rule 1 above; see batch 7 note).
- Ralph Lauren Purple Label: `NC` → `no` (re-read once the block cleared).
- Paul Smith: `url` corrected to the page actually loaded (paulsmith.com/us redirects to /uk).
