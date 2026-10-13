# Wave C seating job: handoff, 13 October 2026 (after batch 9)

This continues `HANDOFF_2026-10-13_from_batch6.md`. Batches 5–9 (worklist rows 41–81) are all returned. Nothing is left to gather; what remains is rulings.

## Delivered
| Batch | Rows | Brands | Items for ruling |
|---|---|---|---|
| 7 | 61–70 | Private White V.C. … Studio Nicholson | 11 |
| 8 | 71–80 | Tellason, Ten Thousand, UGG, Undefeated, Undercover, Universal Works, Velva Sheen, Y-3, Zadig & Voltaire, Zara | 12 |
| 9 | 81 | Études | 4 |

Each batch is in `wave_c/out/batchN/`, zipped as `wave_c_batchN.zip`. Reconcile is exact and the style schema is clean for every batch.

## Still open (reasons named in each NOTE)
- **UGG:** prices and composition are NC. ugg.com served a bot check after the men's apparel listing, and it was not bypassed. The 38 clothing styles are rowed by name.
- **Y-3:** NC throughout. adidas.com was not retried, per ruling.
- **Zara:** the men's feed returned exactly 1,000 colour entries, which looks capped. The 494 clothing products are a floor.

## Pipeline additions in batches 8–9 (in `wave_c/code/`)
- **Scripts:** `build_b8.py` / `build_b9.py`, `meta_b8.py` / `meta_b9.py` and `doors_stock_b8.py` / `doors_stock_b9.py`. `assemble_b6.py` is unchanged; run it with `BATCH=8` or `BATCH=9`.
- **`build_b8.py` new note types:**
  - `_notread`: composition blocked.
  - `_nopct`: fibre named without percentages.
- **`doors_stock_b8.py`:** `carry()` copies a brand's door rows from `out/counts/own_doors.csv`, with a "carried" note.
- **Site tricks:**
  - Tellason (BigCommerce): the description sits in a script literal, `const fullDescription = \`…\``.
  - Undercover: item pages carry `size_proper` (the list price, JPY, tax-inclusive) and `product["name"]`. Item paths differ by line (`1_1_` UC, `1_10_` UB, `1_11_` UP, `1_6_` US); `raw/batch8_inputs/uc_paths.txt` maps them.
  - Zadig & Voltaire: listing and product pages carry JSON-LD (`data-nuxt-schema-org`). The store locator lives on storelocator.zadig-et-voltaire.com, with US city pages linking to the store pages.
  - Zara: the category id comes from the page's `"category":{"id":…}` (men's all-products = 2458839). Use `/us/en/category/<id>/products?ajax=true`, and `/us/en/product/<id>/extra-detail?ajax=true` for composition.
  - Études: composition is in a `metafield-rich_text_field` div or the first `<p>NN% …</p>`. Fastmag codes in the tags (`FM-…-<colour>`) give the style reference.
