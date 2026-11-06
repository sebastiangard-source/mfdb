# seat_inkerman_2026-11-06: the full record for Inkerman

**Issued** 6 November 2026 · **Kind** seating evidence · **Facts-first row returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the `seat_resort` record for the one brand in `worklist.csv`:

- the 132 columns in `return_template.csv`;
- `own_doors.csv`;
- `stockists.csv`;
- `return_styles.csv`;
- `NOTE.md`.

The rules files in this folder are the standing rules and win over any shorthand here. **You gather and you propose; Sebastian rules.**

## The brand

**Inkerman**, inkermannyc.com. It sells footwear (loafers, boots, sneakers) and clothing (knitwear, shirts and polos, tees, jackets, blazers, bottoms, socks and hats), and calls itself inspired by the spirit and heritage of New England. The domain suggests New York. The home page shows prices, with Pre-Order buttons, and links "Store Locations", "The Inkerman Standard" and "The Journal". It states no founding year or place and no place of manufacture. `worklist.csv` has what we know.

It is not on the men's map or in the Cyprus Brand Explorer today. Use `Inkerman` as the brand name. If the brand's own mark differs (INKERMAN, Inkerman NYC), say so in `mark_as_written`; Sebastian rules on marks.

The standing rulings from the earlier seating briefs hold:

- **Men's range only.** Women have their own section, and the other categories carry no gender label. Treat everything outside the Women section as the men's range, say how you scoped it, and note any item that is clearly women's or unisex.
- **No US door is not a reason to stop.** If the brand has no US store of its own, return `0` with the locator URL or `NONE` and a full record.

Things to settle on the way:

- **Own stores versus stockists.** Read the "Store Locations" page. Count only stores the brand runs itself, and name each city. Pop-ups, shops inside another retailer and partner shops are counted separately, with what each is. Anything the brand sells through goes in `stockists.csv`.
- **Prices.** Confirm the US storefront and USD on two displayed prices. Items carry Pre-Order buttons. Record the displayed price and say in `note` which items were pre-order. A price shown only after sign-in is `np`.
- **Where it is made.** The home page says nothing. Check product pages and The Inkerman Standard for made-in lines, named factories, tanneries or mills, and any owned facility. Those are the main evidence for craft. For footwear, record the construction if the brand states one.
- **Founding.** Look for the brand's own statement of the year, place and founders (an About, Standard or Journal page). If only press gives it, mark the source as press.
- **Searching secondhand.** Search Vinted and Grailed for "Inkerman" and "Inkerman NYC". Ignore listings for unrelated products that share the name.

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
13. **Signature product and pronunciation.** Propose a signature product only if the brand's own pages call something its signature, its standard or its best seller. The Inkerman Standard page may be the place.

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
