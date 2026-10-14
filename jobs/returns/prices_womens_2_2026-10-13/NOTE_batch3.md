# prices_womens_2 — batch 3 note (13 Oct 2026, evening), and close-out

**Read (9 of 9):** Le Monde Béryl, MAISON MAYLE, Miguelina, RIXO, RÙADH, Sanderlak, The Frankie Shop, Veronica de Piante, Wiederhoeft. All in USD.

**Whole return:** 29 rows. 27 are read, LOFT is `NC` (PerimeterX, see batch 1), and Kartik Research has no women's range on its own store. `reconcile.py`: 29 exact, 0 rewrites, 0 unmatched. No cell is empty, every figure has a product name and an http URL, and low ≤ high everywhere.

**Proposed bands:** 13 True Luxury, 12 Accessible, 2 Premium, plus the two above.

## Where the brief would have produced a confident wrong answer

1. **Shopify feeds are in the base currency, not the US price.** Le Monde Béryl's `products.json` is in GBP (og:price "180 GBP"), but the US page shows "$180". USD happens to use the same numbers there, so the figures stand, but nothing guarantees that for the next UK or EU brand. RIXO's US prices only come out of its `/en-us/` feed. Any feed-based read of a non-US brand needs a page check, which I did for both.
2. **The Frankie Shop is partly a multi-brand store.** About 800 of its 2,846 listings are stocked brands (Le Monde Béryl, Tekla, Coperni and others) or men's. Without filtering on the vendor field, its shoes and several highs would belong to other houses. I priced own label only, and it has no own-label shoes.
3. **"Dress" covers gowns.** RIXO's dearest dress-type item is a $2,175 "Silk Jacquard Gown". I used the top non-bridal day dress (Mirena, $890 regular). Danielle Frankel and Wiederhoeft have no day dress at all, so their dress rows are bridal and evening ranges and are labelled as such in `note`.

## Rule reads wrong — proposals

- **Miguelina** (resort cover-ups, no sweater): the blouse entry alone ($423) would read True Luxury. **I propose Accessible**: tops start at $215 and dresses at $495.
- **Wiederhoeft** (bridal couture, no sweater): **I propose True Luxury** on blouse entry $2,000. Its only tee is an FW24 runway piece; I recorded it as `single` so it isn't lost, but `NONE` is defensible.
- **The Frankie Shop:** the mean is $155, just $5 into Accessible. Flag it as borderline.

## Flags for the merge

- **Miguelina's homepage** redirects to `/Coming-Soon/`, which renders as a 404. Product pages work and 134 items can be bought. The store may be mid-relaunch.
- **Sanderlak** is menswear-led with a 52-piece Women collection (no dresses, no shoes). I priced that collection only. Whether it belongs on the women's map is your call.
- **Spot checks after the feed reads** (live page or `.js` endpoint): Kallmeyer Ornella $1,250, RIXO Clementine $2,175, Frankie Shop Hazel $256, and three Wiederhoeft items. All matched the feed.
- **The leather-outerwear ruling from batch 2 still applies.** For each brand where a leather piece is the high (RÙADH, Sanderlak, The Frankie Shop, Veronica de Piante), the top non-leather piece is named in `note`, so the merge can switch without a re-read.
