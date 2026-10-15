# Batch 14: womens_dials_2026-10-14, thread 3

Read on 14 October 2026 in Chrome, on each brand's own US store. There are 10 brand rows and 798 style rows. `reconcile.py` gives 10 exact matches, 0 to rewrite and 0 unmatched. No empty cells, every enum is valid, and every `lead_pct`/`elastane_pct` is ND or 0–100.

## What was checked

| brand | store / platform | styles (site) | sampled | with composition | status |
|---|---|---|---|---|---|
| AFLALO | Shopify | 92 | 80 | 74 | read |
| Alaïa | /en-us · SFCC | 246 | 79 | 76 | read |
| Amsale | Shopify | 344 | 80 | 39 | **partial** |
| Another Tomorrow | Shopify | 195 | 80 | 80 | read |
| B SIDES | Shopify | 128 | 80 | 74 | read |
| Barefoot Dreams® | Shopify | 308 | 80 | 52 (family level) | **partial** |
| Cara Cara | Shopify | 352 | 80 | 79 | read |
| Ciao Lucia | Shopify | 215 | 80 | 79 | read |
| CO | Shopify | 139 | 80 | 80 | read |
| Diane von Furstenberg | Shopify | 368 | 79 | 76 | read |

Every house is a proportional stratified sample of 80 (AFLALO's 92 included). Two came out at 79 because a drawn item was dropped: Alaïa (a denim belt in Skirts) and DVF (a 'DVF Vintage' resale listing typed as a dress). Resale and vintage listings were excluded everywhere: Another Tomorrow's Authenticated Resale and DVF Vintage. B SIDES's reworked vintage Levi's stay in, because they are the brand's own product.

## Headlines

- **Another Tomorrow is the craft standout:** it names its mills and farms (Candiani, Lake Hawea Station, two Uruguayan farms), lists Tier-2 mills on the Open Apparel Registry, and gives a town on each product page. Cut-and-sew makers are withheld by policy, so it gets a 3.
- **Made-in-USA denim and knits:** B SIDES makes 56 of 80 sampled in the USA, NYC or LA, hand-knit in New York or LA. AFLALO denim is made in Los Angeles, its silks in New York and its tailoring in Italy.
- **Silk is a real women's dial again:** AFLALO (fab_silk 4), Ciao Lucia (4) and DVF (3).
- **Viscose leads DVF:** 52% cellulosic-led, from jersey wraps.
- **Most synthetic:** Barefoot Dreams (CozyChic polyester and nylon) and Amsale (polyester gowns) are synthetic-led wherever composition exists.

## What contradicted the record or the brief

1. **Amsale: the worklist says nothing is sold, but the store sells dresses.** It has ready-to-wear evening dresses (/collections/all-ready-to-wear) plus bridal and bridesmaid gowns. As briefed, every link is NONE, and the real dress listing is in `links_kind`. I read the dresses for B and C anyway; **the dress cell should be corrected at merge**.
   - Bridal gown pages are try-in-store pages with no composition, so 41 of 80 are ND and the status is partial.
   - The house says every design is handcrafted in its New York atelier, but every page that names a country says Made in Thailand.
2. **Barefoot Dreams publishes no per-product composition.** Every page carries the same fabrication note (CozyChic = 100% polyester microfiber; Lite = nylon and rayon; Ultra Lite = nylon and viscose). I applied it only where the title and store tag name a single family (52 of 80), flagged in each row. The rest are ND. This is family-level data, so **I'd treat fab_synth as indicative.**
3. **Cara Cara's story page claims "workrooms in the US"**, but none of the 80 sampled pages say USA: 67 are Made in China and 12 Made in India.
4. **Ciao Lucia's worklist `shoes_sold = no` holds.** The store has a Shoes collection, but it is Larroudé and other collaboration footwear sold through Shopify Collective.
5. **House data that doesn't add up, filed as stated:**
   - DVF has a blouse reading '97% Viscose, 3%' with the second fibre missing. Its store tags sometimes differ from the page; the page was used.
   - Ciao Lucia has a cardigan at 77% cotton / 33% nylon.
   - Another Tomorrow has a blouse summing to 105.
   - Amsale has '92% polyethyene' (sic).

## Parser changes (batches 11–13 rebuilt; no figure changed)

- Bare numbers with no % sign ('95 Cotton / 5 Spandex') are read only when they sum to 100.
- Yarn counts and weights (120's, 50s/1, oz, gg, ply) no longer block a named-fibre read.
- New mappings: 'Poly' → polyester, 'MD' → modal, chinchilla and mink → other-natural, and the 'polyethyene' typo.

## Not reached

- I didn't open Alaïa's house-history or atelier pages; none are linked from the US store navigation. The Homo Faber page was the only craft page found.
- Ciao Lucia has no about or story page, so heritage and process are blank by absence, not unread.
- No current craft scores are in the worklist, so there is no moves table.
