# seat_save_khaki_2026-11-05: the full record for Save Khaki United

**Issued** 5 November 2026 · **Kind** seating evidence · **Facts-first row returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the `seat_resort` record for the one brand in `worklist.csv`:

- the 132 columns in `return_template.csv`;
- `own_doors.csv`;
- `stockists.csv`;
- `return_styles.csv`;
- `NOTE.md`.

The rules files in this folder are the standing rules and win over any shorthand here. **You gather and you propose; Sebastian rules.**

## The brand

**Save Khaki United**, savekhaki.com. Sebastian calls it SKU, and the brand abbreviates itself that way too. It makes chinos and casual clothing for men and women, and says its clothes are made in the USA. Its site says you can shop online or in New York and Los Angeles, and it links "All SKU Stores" and "Where to Buy". A first read of the home page found no prices and no founding year. `worklist.csv` has what we know.

It is not on the men's map or in the Cyprus Brand Explorer today. Use `Save Khaki United` as the brand name. If the brand's own mark differs, say so in `mark_as_written`; Sebastian rules on marks.

The standing rulings from the earlier seating briefs hold:

- **Men's range only.** The brand also sells women's. Read the men's pages only, and say how you scoped them.
- **No US door is not a reason to stop.** If the brand has no US store of its own, return `0` with the locator URL or `NONE` and a full record.

Things to settle on the way:

- **Own stores versus stockists.** "All SKU Stores" and "Where to Buy" may be two different lists. Count from the brand's own store list only the stores it runs itself, and name each city. Anything it sells through belongs in `stockists.csv`. If a store is a pop-up, a shop inside another retailer or a partner's shop, count it separately and say what it is.
- **Prices.** Confirm the US storefront and USD on two displayed prices. The site has a currency selector, so set it to the United States first. If prices still don't display, say what you did and stop on that section.
- **Made in USA.** Check the claim product by product on the men's pages. The brand says its chinos are cut in Los Angeles from imported fabric. Record where the fabric comes from if the brand says. Name any factory, mill or owned facility it names. Those are the main evidence for craft.
- **Founding.** Look for the brand's own statement of the year and place (the "Who We Are" page, or the "20 Years of Save Khaki" article). If only press gives it, mark the source as press.
- **Searching secondhand.** Search Vinted and Grailed for "Save Khaki United" and "Save Khaki". Do not search "SKU", which is also the retail term for a product code.

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
13. **Signature product and pronunciation.** The Original Chino is a candidate for the signature product; propose it only if the brand's own pages support it.

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
