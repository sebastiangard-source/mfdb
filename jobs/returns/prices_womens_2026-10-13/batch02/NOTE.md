# prices_womens_2026-10-13 — batch 2

**Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. Validator: no empty cells; every priced figure has a product name and URL; no low above its high.**

## Result

| Brand | Tee / blouse / sweater entry | Proposed band | Status |
|---|---|---|---|
| Altar'd State | $44 / $58 / $58 | Premium | shoes `NC` |
| Lilly Pulitzer | $64 / $128 / $108 | Premium | complete |
| Evereve | $38 / $78 / $88 | Premium | own label only |
| Aritzia | $28 / $58 / $68 | **Basic by the rule; flagged** | jeans high `NC` |
| Tory Burch | $160 / $395 / $330 | Accessible | complete |
| Reformation | $48 / $128 / $128 | Premium | complete |
| Brandy Melville | $16 / $20 / $28 | Basic | complete |
| Michael Kors | none / $120 / $150 | Premium | thin assortment |
| Lucky Brand | $40 / $70 / $80 | **Premium, or Basic: see point 2** | complete |
| Eileen Fisher | $78 / $148 / $268 | Accessible | complete |

## Where the brief would give a confident wrong answer

1. **Aritzia reads Basic.** Its cheapest ribbed tee is $28 and a short-sleeve smocked top is $58, so it passes the Basic test. But its core shirts and knits sit at $88–148 and its outerwear goes up to $898. The Basic test only looks at the two cheapest pieces, so it catches seasonal entry items. I'd band Aritzia by hand (Premium on the mean).
2. **Lucky Brand's struck price is a "Comp. Value", not an original price.** Nearly every style sells at about 30% under it. The row uses the struck figure, as the brief says, and reads Premium. On the everyday selling prices (tee $27.65, blouse about $48.65) Lucky reads **Basic**. This needs a ruling on which figure counts as Lucky's full price.
3. **"MICHAEL Michael Kors vs Collection" no longer exists on the site.** michaelkors.com now labels every women's product "MICHAEL KORS". The row is the whole women's offer, and the main thread should decide which name the 60 register doors carry. The US apparel range is small: no pants or jeans category (read via search), and no plain tee (only charity graphic tees, so tee = `NONE`).
4. **More multi-brand stores.**
   - Evereve: only about 23% of its catalogue is its own EVEREVE label; the rest is AGOLDE, Mother, Paige, Z Supply and others.
   - Aritzia: now stocks AGOLDE and Citizens of Humanity.
   - Reformation: sells Veda leather and Patagonia.
   - All of these were excluded. Evereve's own label was isolated via the Shopify `vendor` field.
5. **Wrong prices from loose reads.** On Reformation's outerwear page, a loose tile read attached a $2,448 price to the wrong product. All Reformation prices were re-read, only from blocks holding a single product. At Tory Burch, one trouser shows $990 on its tile and $549 on its product page. That trouser was not used.

## How prices were read

| Site | Method |
|---|---|
| Altar'd State, Lilly Pulitzer, Lucky, Eileen Fisher, Michael Kors | full listings with `?sz=`; struck list price where shown |
| Evereve, Brandy Melville | Shopify `/products.json` feed (vendor, product_type, compare_at) |
| Aritzia | the site's own price sort, first 24 tiles each way; infinite scroll stalls on sorted pages, so highs are less certain |
| Tory Burch | each priced product re-checked on its product page |
| Reformation | scroll-captured tiles |

## Other notes

- **Altar'd State shoes are `NC`.** The shoe category mixes stocked brands (Schutz) with vendor styles, and I couldn't tell own label from the site.
- **Eileen Fisher shoes are all on clearance.** The shoe page redirects to "40% Off Sale Items". The struck list prices are used, but the category may be closing.
- **Brandy Melville's $100 Martha Sweater** is an outlier against three $38 Martha sweaters, and is worth a product-page check.
- **`NONE` because the brand doesn't sell it:**
  - Evereve: shoes (all stocked).
  - Aritzia: shoes.
  - Brandy Melville: shoes.
  - Lucky Brand: shoes (footwear is licensed out).
  - Michael Kors: tee.
- **The rule doesn't fit knit-house naming.** Aritzia and Eileen Fisher name most sweaters "Top", so the "crewneck pullover" staple has to be found by fabric, not by name.

## Files

- `return.csv`: 10 rows
