# seat_farafield_2026-11-06: the full record for Farafield

**Issued** 6 November 2026 · **Kind** seating evidence · **Facts-first row returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the `seat_resort` record for the one brand in `worklist.csv`:

- the 132 columns in `return_template.csv`;
- `own_doors.csv`;
- `stockists.csv`;
- `return_styles.csv`;
- `NOTE.md`.

The rules files in this folder are the standing rules and win over any shorthand here. **You gather and you propose; Sebastian rules.**

## The brand

**Farafield**, farafieldclothing.com. It makes menswear and accessories and calls itself independent, family-run menswear built on close relationships. The site also writes "Far Afield" in places. The home page says it was founded in 2016, names Brighton as its hometown and Mark Scholes as Creative Director, and names one production site, a family-run knitwear workshop in Istanbul. It lists no stores of its own, but a Stockists page and Journal pieces feature shops in Brighton, Toronto, Ottawa, Indonesia and Brooklyn. A first read showed prices in pounds, with a country and currency selector set to the United Kingdom. `worklist.csv` has what we know.

It is not on the men's map or in the Cyprus Brand Explorer today. Use `Farafield` as the brand name. If the brand's own mark differs (Far Afield, FARAFIELD), say so in `mark_as_written`; Sebastian rules on marks.

The standing rulings from the earlier seating briefs hold:

- **Men's range only.** Nothing on the home page suggests a women's range. Confirm that, and say how you scoped the pages.
- **No US door is not a reason to stop.** If the brand has no US store of its own, return `0` with the locator URL or `NONE` and a full record.

Things to settle on the way:

- **Own stores versus stockists.** Read the Stockists page and say whether it is a list or a set of features. The brand appears to have no store of its own, so `own_doors.csv` may be `NONE`, with sample sales or pop-ups counted separately and labeled. Put every stockist the brand names in `stockists.csv`, worldwide, with the shop's city and country. Mark each US shop clearly, because the map seats US stockists first. If a stockist is a department store or a chain, say so.
- **Prices and currency.** Set the country selector to the United States first. If a US storefront with USD exists, use it and confirm USD on two displayed prices. If the site offers only pounds or converts at checkout, record the pound prices, say so in `store_used` and `currency`, and fill `feed_currency_rate` as `rules_prices.md` directs. Use regular prices, not sale prices. The home page shows a sale price on one shirt and 25% off select styles.
- **Where it is made.** The home page names only the Istanbul knitwear workshop. Read Manufacturing & Sustainability and product pages for each garment's country, and for named factories, mills and workshops. Say whether Farafield owns any of them. Those are the main evidence for craft.
- **Founding.** The home page says 2016. Look for the brand's own statement of the founders, the place and the story (About Us). If only press gives it, mark the source as press.
- **Searching secondhand.** Search Vinted and Grailed for "Farafield" and "Far Afield". Ignore listings for unrelated products that share the name.

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
13. **Signature product and pronunciation.** Propose a signature product only if the brand's own pages call something its signature, its standard or its best seller. The Far Afield pages (About Us, Manufacturing & Sustainability) may be the place.

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
