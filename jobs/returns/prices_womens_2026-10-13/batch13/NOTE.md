# prices_womens_2026-10-13 — batch 13

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Barefoot Dreams® | $78 / $98 / $115 | **hand-band** (loungewear; rule reads Premium) | complete |
| NYDJ | $49 / $79 / $99 | Premium | full price only |
| Johanna Ortiz | none / $595 / $1,950 | True Luxury | complete |
| MOTHER | $90 / $198 / $278 | Accessible | own label only |
| Retrofête | none / $248 / none | **hand-band** (partywear; rule can't read) | own label only |
| Sanctuary | $39 / $89 / $89 | Premium (missed Basic by $4 on the tee) | complete |
| Simone Rocha | $285 / $650 / $760 | True Luxury | complete |
| Victoria Beckham | $150 / $590 / $464 | True Luxury | complete |
| Alaïa | $750 / $1,550 / $1,950 | True Luxury | complete |
| Lilysilk | none / $139 / $119 | Premium (sleepwear share; hand-band check) | complete |

## Where the brief would give a confident wrong answer

1. **Multi-brand sites.** These own sites sell other brands too, and only the brand's own label was read:
   - **MOTHER:** 261 stocked-brand products (Alix of Bohemia, XiRENA, SABLYN and others) plus Merci x MOTHER.
   - **Retrofête:** its sister label SEROYA (388) and others, which outnumber Retrofête.
   - **Barefoot Dreams:** stocked plush toys and licensed Disney pieces.
2. **Most stock is on sale.** NYDJ tags full price as `price_reg` (793 of 1,335). Every in-stock NYDJ shoe is older-season sale stock, so shoes were read at their compare-at prices and flagged. Retrofête and MOTHER sale and archive-sale tags were excluded.
3. **Sanctuary nearly reads Basic.** Its tee entry is $39, just over the $35 cut, and its blouse is $89. Small changes in which tee counts would flip it to Basic.
4. **Silk and knit houses versus the cotton-tee rule.** Lilysilk's tees are all silk jersey ($68–129), so tee is `NONE`. Its Liberty-fabric blouses ($369–499) were treated as a collaboration.
5. **More hand-band candidates:**
   - Barefoot Dreams is loungewear and blankets.
   - Retrofête is partywear with no tee or sweater, so the rule can't read.
   - Lilysilk has a large sleepwear business.
6. **Fur, shearling and hair-on leather at the top end.** Excluded from highs:
   - Retrofête: a real-fur jacket ($1,898) and faux-fur coats.
   - Johanna Ortiz: a Tibetan-shearling jacket ($6,500) and a shearling-trimmed coat.
   - Victoria Beckham: a shearling-collar aviator ($4,690).
   - Simone Rocha: a sheepskin coat ($5,780).
   - Alaïa: pony-hair calfskin coats.

## How prices were read

| Site | Method |
|---|---|
| Barefoot Dreams, NYDJ, Johanna Ortiz, MOTHER, Retrofête, Sanctuary, Simone Rocha (US store) | Shopify `/products.json` feed, in stock only |
| Victoria Beckham | Shopify feed on the /en-us market, tagged `full-price` |
| Alaïa | server-rendered category listings on /en-us |
| Lilysilk | category pages scrolled until every product had loaded |

Barefoot Dreams and NYDJ product types are blank or SKU codes, so garments were read by title. MOTHER used the site's own "sub class" tags.

## Garment notes

- **Embellishment as house style.** At Simone Rocha nearly every piece has pearls, bows or embroidery, so embellished pieces were kept.
- **Tee:**
  - MOTHER's tees are mostly graphic.
  - Johanna Ortiz's T-shirts are polyester or viscose, so `NONE`.
- **Trousers:**
  - Simone Rocha sells only knit "long johns", so `NONE`.
  - Barefoot Dreams is pull-on only.
- **Dress:** Johanna Ortiz's maxi dresses ($950–6,950) were not read; only midi, mini, tunic and shirt dresses were.
- **Shoes without a flat or loafer:** NYDJ and Retrofête, so both are `range`.
- **`NONE` because the brand doesn't sell it:**
  - Barefoot Dreams: jeans, shoes.
  - Johanna Ortiz: tee, jeans.
  - MOTHER: shoes (socks only).
  - Retrofête: tee, sweater.
  - Simone Rocha: jeans, trousers.
  - Lilysilk: tee, jeans.

## Files

- `return.csv`: 10 rows
