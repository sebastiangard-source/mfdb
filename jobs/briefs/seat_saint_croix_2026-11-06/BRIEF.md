# seat_saint_croix_2026-11-06: the full record for Saint Croix

**Issued** 6 November 2026 · **Kind** seating evidence · **Facts-first row returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the `seat_resort` record for the one brand in `worklist.csv`:

- the 132 columns in `return_template.csv`;
- `own_doors.csv`;
- `stockists.csv`;
- `return_styles.csv`;
- `NOTE.md`.

The rules files in this folder are the standing rules and win over any shorthand here. **You gather and you propose; Sebastian rules.**

## The brand

**Saint Croix**, saintcroix.com. It makes knitwear, ready-to-wear clothing and accessories for men and women, and says its clothes are handcrafted in Winona, MN and are "American-made Luxury." It cites more than 65 years of experience but states no founding year, founder or place on the home page. Its About menu has Story, Sourcing & Technique and Stores, and its Collections menu runs from Luxury Fall 2026 to Classics, Performance and Limited Release. A first read of the home page found no prices and no currency selector. `worklist.csv` has what we know.

It is not on the men's map or in the Cyprus Brand Explorer today. Use `Saint Croix` as the brand name. If the brand's own mark differs (Saint Croix Knitwear, SAINT CROIX), say so in `mark_as_written`; Sebastian rules on marks.

The standing rulings from the earlier seating briefs hold:

- **Men's range only.** The brand also sells women's. Read the men's pages only, and say how you scoped them.
- **No US door is not a reason to stop.** If the brand has no US store of its own, return `0` with the locator URL or `NONE` and a full record.

Things to settle on the way:

- **Own stores versus stockists.** Read the Stores page. Count only stores the brand runs itself (a factory store or outlet counts separately, with what it is), and name each city. Anything the brand sells through goes in `stockists.csv`.
- **Prices.** The home page showed none. Check the men's collection pages and product pages. Confirm the US storefront and USD on two displayed prices. A price shown only after sign-in is `np`. The Archive Sale shows reduced prices, so use regular prices from current collection pages only. If prices still don't display, say what you did and stop on that section.
- **Made in the USA.** The brand says Winona, MN. Check it product by product on the men's pages, and record where the yarn comes from if the brand says. Read Sourcing & Technique closely. Name every mill, factory or owned facility the brand names, and say whether it owns the Winona production. Those are the main evidence for craft.
- **Founding.** Look for the brand's own statement of the year, place and founders (the Story page). If only press gives it, mark the source as press.
- **Searching secondhand.** Search Vinted and Grailed for "Saint Croix" and "Saint Croix Knitwear". Ignore listings for unrelated products that share the name, such as fishing rods.

## Order

1. **Facts first.** Return one row in `facts_first_template.csv` before any full record:
   - site and US storefront;
   - own-store count, with its source;
   - what it sells;
   - an entry price and a top price;
   - a band guess;
   - the brand's mark as it writes it.

   Allow fifteen minutes.
2. **Then the full record.** Allow about forty minutes.

## The sections, and the rules file for each

1. **Store, currency, search** (`rules_prices.md`): the US storefront, with USD confirmed on two displayed prices.
2. **Eight garments** (`rules_prices.md`, `rules_garment_links.md`): prices and men's listing links. Put the product and URL behind every figure.
3. **Fiber by style** (`rules_fibre.md`, `schema_styles.json`): men's clothing styles.
4. **Own doors**, worldwide, US first. Count outlets, concessions and pop-ups separately.
5. **Stockists**: those the brand itself lists.
6. **Tech.**
7. **Craft** (`rules_craft.md`, `rubric_craft.txt`): six facts, two URLs, a proposed score and the reasoning. Made-in claims, named factories and owned facilities matter most here.
8. **Origin and ownership**, from the brand's own statements first.
9. **Lookbook.**
10. **Vinted and Grailed.**
11. **B Corp and GOTS**, from the certifiers' own directories.
12. **One real quotation** (`rules_quotes.md`).
13. **Signature product and pronunciation.** Propose a signature product only if the brand's own pages call something its signature, its standard or its best seller. The About pages (Story, Sourcing & Technique) may be the place.

## Rules

- **Name** must match `canonical_keys.txt` where it can. Save Khaki United is new, so `reconcile.py` will report no match. That is expected.
- **Cell values.** `NC` means nobody looked; `NONE` means it doesn't sell or do it; `np` means no price is published. No empty cells.
- **Full price only.** Use the regular price, not a sale price.
- **Sources.** The brand's own statements first, then press that quotes them. A retailer's prices and descriptions are never the brand's.
- **Bot walls.** One plain try. If a check box appears, ask Sebastian once whether he'll clear it himself.
- **Read only.** Don't sign in, add to cart, sign up or submit anything.
- **Don't touch the map.** Don't send working files. Anything out of scope but noticed goes in `NOTE.md`.

## Time box

- Facts first: about fifteen minutes.
- Full record: about forty minutes.

Past that, return what you have, put `NC` on the rest, and say so.
