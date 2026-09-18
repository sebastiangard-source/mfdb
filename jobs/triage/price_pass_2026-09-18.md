# Triage — price pass, full return, 18 September

178 rows · 170 read live in one day by ten parallel browser agents · reconcile clean · no blank cells.

**Merged:** 128 brands' new price cells (414 prices, 58 verified absences) and 28 search URLs.
**Held:** Sugar Cane, Ring Jacket (JPY); Zilli (EUR); Wales Bonner (GBP); Auralee, Reiss, Officine
Générale, Our Legacy, Rick Owens, Husbands, Acne Studios (USD_landed); Stefano Ricci, Loro Piana,
Hermès, Sid Mashburn (fur or exotic skin counted as the high, against rev 3's own definition —
restate without); Fear of God's polo (the agent excluded ESSENTIALS against the default).
**Not readable:** Saint Laurent, Gucci, Balenciaga, Bottega Veneta, Celine (browser blocked);
Comme des Garçons, Junya Watanabe, Charvet, Rakho (no store); Madhappy, Cesare Attolini (closed).

`price_range_only` recorded on 74 brands: their [low, high] is the category's plain range, not the
staple pair. Data-only until the page marks it.

## Rulings — recommendations

1. **Elevated fibre.** Majority cashmere; silk, alpaca, mohair and superfine wool count; fur and
   exotic skins never do (rev 3 already said so). The four held rows restate on that.
2. **Same style, outerwear.** By exact model where the house sells one; by garment type where it
   does not (luxury houses rarely sell one model in two cloths). Record which in the note. Accept.
3. **Sub-lines.** Include a sub-line sold in the main store under the brand's name (Ghost, Crown
   Crafted, Blue Tab, ESSENTIALS); exclude capsules and archive reissues. Fear of God restates.
4. **Currency.** The test is two feed prices confirmed against the displayed US page on the market
   path; the Shopify rate is a hint. Wave 1's US-based Shopify rows were not re-verified one by one;
   accept, and spot-check ten on the next pass.
5. **Landed prices.** `USD_landed` stays held, with the non-USD figures, pending the axis decision
   that has been open since 13 September. Eight brands now wait on it; it is time to take it.
6. **Range rows.** The page should mark a range cell as such. One UI change.
7. **Schema.** Integer cap raised to 9,999,999 for future returns.

## Corrections to the store record
J.Lindeberg → jlindebergusa.com; Isaia → isaia.us; Kiton → us.kiton.com; Corneliani /en_us/;
Samsøe Samsøe /en-US; Hackett has no US storefront; Sugar Cane has no own store. Canada Goose and
Bonobos are Shopify; Tecovas, J.McLaughlin, Rhoback, Suitsupply, Les Deux are headless Shopify;
Vineyard Vines is Salesforce PWA. To apply to `site` on the next pass.
