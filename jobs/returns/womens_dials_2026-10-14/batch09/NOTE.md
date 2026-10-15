# Batch 09 — womens_dials_2026-10-14, thread 2

Read on 14 October 2026 in Chrome, on each brand's own US store. All 10 brands are `read`, giving 757 style rows. `reconcile.py`: 10 exact, 0 rewrites, 0 unmatched. The method is the same as in batch 06. Percentages are of sampled styles; `fab_*` figures are of sampled styles that have a composition.

## What was read

| brand | channel | styles (census) | sampled | with composition |
|---|---|---|---|---|
| Cinq à Sept | Shopify feed descriptions | 1,097 | 83 | 77 |
| ERES | SFCC grids + PDP 'Composition' panel | 209 (resort, lounge, active) | 78 | 74 |
| Fleur Du Mal | Shopify feed descriptions ('Body: …') | 237 (RTW only) | 81 | 81 |
| Good American | Shopify feed descriptions | 573 | 82 | 76 |
| GUEST IN RESIDENCE | Shopify feed descriptions | 102 (women's) | 73 | 71 |
| Loeffler Randall | Shopify feed + PDP 'Materials' | 119 (apparel) | 80 | 79 |
| prAna | SFCC women's grid + PDP 'Fabric details' | ~184 | 77 | 76 |
| Rains | Shopify feed + PDP 'Composition:' | 75 (women's) | 76 | 76 |
| Sam Edelman | client-rendered grid + embedded PDP description | 46 (census) | 46 | 40 |
| Simkhai | Shopify RTW collections + PDP 'More Details' | 399 | 81 | 77 |

## Headlines

### Natural-led houses

- **GUEST IN RESIDENCE** is 96% natural and 61% cashmere-led.
- **Loeffler Randall** is 91% natural: cotton, linen, ramie, wool and silk.
- **ERES** resortwear is linen, cotton and silk, but its activewear is 59–77% polyamide with elastane.

### Synthetic-led houses

- **Rains** is 80% synthetic: coated polyester, with no coating stated.
- **Sam Edelman** apparel is polyester and acrylic knits, satin and faux fur.
- **prAna** is split: recycled nylon and polyester performance pieces against organic and regenerative cotton.
- **Cinq à Sept** is split: its house 'Drapey Crepe' (triacetate/polyester) and polyester dresses against cotton-stretch denim.

### Tech

- **prAna is the only 4 in thread 2 so far.** It has a family of named house fabrics with stated performance:
  - Stretch Zion™: recycled nylon/elastane with DWR and UPF 50+
  - Luxara™
  - Heavana™
  - Sculpt™
- **Good American gets 2.** Soft Tech and Compression denim are named but cover only about 7% of styles.
- **ERES gets 2.** Peau Douce is used on a couple of resort styles.
- **Rains gets 2.** It publishes a 5,000 mm water column on its rain range but names no fabric.

### Craft

**ERES (3).** It has its own Paris pattern and prototype studio at 19M. Its long-standing French lace, embroidery and silk suppliers are described by place and founding date but not named.

**GUEST IN RESIDENCE (3).** It names the factory that makes most of its range: Draper HK's Dongguan Cason Knitted Company, China. Over half of its pages say 'manufactured in China'.

**prAna (2).** It has a dated timeline: Fair Labor Association 2010, first Fair Trade Certified™ apparel 2011, published supplier list 2019. Every page still says only 'Imported'.

**Sam Edelman (2).** 'Made in China' appears on 32 of 46 apparel pages.

**The rest get 1.**

## Not reached / partial

**Sam Edelman.** A Cloudflare "verify you are human" wall appeared on the first visit and on the apparel grid. I did not interact with it. A plain retry a few minutes later loaded normally.

- The grid says "76 products" but renders 46 style tiles; the paging button did not load more. The 46 styles were read as a census.
- 6 outerwear and dress pages carry no composition.

**Heritage `NC`.** Good American (no about page on the US store), Rains (no date or place on /pages/company) and Cinq à Sept (/pages/about is a mood statement).

## Contradicts the record / for the map

- **GUEST IN RESIDENCE sells tees.** The worklist says no tee or blouse, but the store has a 'Tees' collection of cashmere and cotton-cashmere tees. I left the links NONE per the worklist.
  - The store is unisex: 66 of 291 women's products are shared with men's.
  - Seven sampled styles not in the women's collection were dropped.
- **Rains is unisex.** Each style exists as a '-male' and a '-female' product. The women's product was used.
- **Simkhai's product types are internal workflow labels** ('ready', 'need flat', 'no ecom images'). The RTW collections were used as strata instead.
- **Parent links:**
  - Fleur Du Mal: tee and blouse → Tops.
  - Loeffler Randall: tee and blouse → Tops; trousers → Bottoms.
  - Rains: blouse → All clothing.
  - GIR: jeans → the 'Denim World' landing page (no denim collection).
  - ERES: shoes → resort Accessories (mules among bags and hats).

## What the brief got wrong (adds to batches 06–08)

1. **Unisex stores.** Rains and GIR list one style as separate men's and women's products, and their women's collections omit some unisex styles. The brief assumes a women's catalogue exists to sample; for unisex houses it should say whether 'women's' means the women's collection or everything a woman can buy.
2. **Coatings are invisible in compositions.** Rains' rain range is PU-coated polyester but reads '100% PES'. Sam Edelman's 'Alternative Leather' gives percentages only for the 73% viscose backing, so it files as viscose-led. A ruling is needed on whether to file what is written or the face fabric. I filed what is written and flagged it.
3. **Lingerie and swim houses with real ready-to-wear** (ERES, Fleur Du Mal) were read on their clothing only: resort, lounge, active and RTW. I filed sleep nightshirts and kimonos as `other`.

## Method notes

Parser changes this batch. I re-ran batches 06–08 after the changes: 0 style rows changed, and the brand rows are identical.

- Compositions written fibre-first ('Cotton 98% Elastane 2%', Cinq à Sept, prAna) are now read in that order.
- Glued words are split ('DenimCotton', 'ElastaneDry').
- 'Faux Fur 100% Polyester' reads as polyester.
- New codes and spellings: OC (organic cotton), T400 (elastomultiester), 'élasthanne', 'soie', 'Elastaine', 'Spndex', 'Elastic' as a fibre, polyethylene (other synthetic).
- Triacetate is filed cellulosic, with acetate.
