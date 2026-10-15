# Batch 13: womens_dials_2026-10-14, thread 3

Read on 14 October 2026 in Chrome, on each brand's own US store. There are 10 brand rows and 724 style rows. `reconcile.py` gives 10 exact matches, 0 to rewrite and 0 unmatched. No empty cells, every enum is valid, and every `lead_pct`/`elastane_pct` is ND or 0–100.

## What was checked

| brand | store / platform | styles (site) | sampled | with composition | status |
|---|---|---|---|---|---|
| Proenza Schouler | Shopify | 249 | 80 | 79 | read |
| SACHIN BABI | Shopify | 382 | 80 | 79 | read |
| SILVIA TCHERASSI | Shopify | 669 | 79 | 73 | read |
| SIMONMILLER | simonmillerusa.com · Shopify | 237 | 80 | 79 | read |
| Sporty & Rich | Shopify | 86 models | 79 | 79 | read |
| Suzie Kondi | Shopify | 226 | 80 | 79 | read |
| Tanya Taylor | Shopify | 350 | 80 | 79 | read |
| Tibi | Shopify (/collections/view-all) | 276 | 80 | 80 | read |
| Wacoal | Shopify | 7 (sleep/lounge) | 7 | 7 | read |
| We Norwegians | Shopify | 118 | 79 | 79 | read |

Every house over 80 is a proportional stratified sample of 80, with the basis in `sample_basis`. Three came out at 79 because a drawn item was dropped: Tcherassi (a bag typed Bridal), Sporty & Rich (cashmere socks) and We Norwegians (a men's base layer typed women's). Wacoal is all 7 of its own clothing styles.

For Sporty & Rich, Suzie Kondi, Tanya Taylor and Wacoal the feed carries no composition, so each sampled product page was opened and its Details / Materials block read.

## Headlines

- **Split houses:** SIMONMILLER, Sporty & Rich (SportyCore 82/18 activewear and tennis against cotton fleece and tees), Tibi (synthetic skirts, dresses and coats against wool and cotton tops, pants and knits) and We Norwegians (polyester and nylon skiwear against merino knitwear, which leads 49% of the sample, so fab_wool is 5).
- **Most synthetic:** SACHIN BABI, at 82% synthetic-led (polyester gowns).
- **Most natural:** Suzie Kondi, at 96% (velour and terry tracksuits in 80/20 cotton-poly, cashmere, silk and poplin).
- **Named fabric programmes** (proposed_tech 2–3): Sporty & Rich's Fabric Guide (LuxeFleece, UltraSoft Jersey, SportyCore, Cashmere, with weights and finishes) gets a 3. Tibi's 'Product Grouping' fabric families and We Norwegians' Südwolle and Creora base layers get 2s.
- **Craft:** SACHIN BABI is the only 3 (an owned, family-run Mumbai factory is claimed but not shown). We Norwegians names a yarn mill (Südwolle) on one line. Sporty & Rich credits an unnamed 52-year-old Portuguese mill, and Suzie Kondi places making in LA and NYC. All three are 2s.

## What contradicted the record or the brief

1. **SIMONMILLER's worklist `site_domain` reads "footer links: "**, a scrape fragment. The store is simonmillerusa.com. Its `jeans_sold = yes` rests on one printed jean.
2. **Wacoal is a lingerie house.** Its clothing is a 7-style sleep and lounge capsule. Bras, panties and shapewear were not read. The store also sells **Splendid**-branded loungewear (Winslow, Haven), which I left out as another brand. The fab_* dials rest on 7 styles, so **I'd hold them**.
3. **Tanya Taylor hides its countries.** They appear only in store tags (China 52, India 10, Portugal 8 of 80), never on the page, so made-in is 0%, as with 3.1 Phillip Lim in batch 11.
4. **Tibi's full feed is 3,521 records**, including archive, sample sale and non-product content blocks. I used the store's own current range (/collections/view-all, 578 listings).
5. **Worklist rows to recheck:** We Norwegians `dress_sold = yes` is one SS25 dress that sits in no women's collection, so the link is /collections/all. Suzie Kondi's Denim collection is denim-cloth shirts, skirts and shorts, with no five-pocket jean.
6. **House data that doesn't add up, filed as stated:** Tcherassi has '17% / Lining' with no fibre named. Tanya Taylor's Milla Coat is 15% wool / 49% polyester, and its Annika skirt is 95% cotton / 1% elastane. Sporty & Rich has a jacket at 65% polyester / 37% cotton.

## Parser changes (batches 11 and 12 rebuilt)

- **Main fabric only:** the parser now stops at the first secondary label (Lining, Combo, Collar, Piping, Doublure, Trim, Pocket lining, T2, Skirt, Rib, Fill). Before, an incomplete shell sum ran on into the lining.
  - This fixes one delivered row in batch 12. **ARGENT HL24-0804** had `lead_pct` 134; it is now 34. `batch12/return_styles.csv` is re-sent with that one cell changed, and `return.csv` is unchanged.
  - Batch 11 did not change.
- **Membranes ignored:** "PU/TPU membrane" on skiwear is now skipped, so the face fabric leads.
- **New mappings:** Creora → elastane, CoolMax → polyester.
- **New check:** `check.py` now rejects a `lead_pct` or `elastane_pct` outside 0–100.

## Not reached

- No current craft scores are in the worklist, so there is no moves table.
- I opened no SACHIN BABI factory imagery beyond the about page.
