# seat_withered_fig_c_2026-11-06: the full record for 6 brands

**Issued** 6 November 2026 · **Kind** seating evidence, batch · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the `seat_resort` record for **each of the 6 brands in `worklist.csv`**, one after another, in order. For each brand:

- the 132 columns in `return_template.csv`, one row a brand in a single `return.csv`;
- `own_doors.csv` and `stockists.csv`, with a `brand` column on every row;
- `return_styles.csv`, with a `brand` column;
- `dials.csv`, with the `brand` column;
- one section a brand in `NOTE.md`.

The rules files in this folder are the standing rules and win over any shorthand here. **You gather and you propose; Sebastian rules.**

## Why these brands

Withered Fig (a shop) stocks all of them and none is on the men's map or in the Cyprus Brand Explorer today. Sebastian wants them seated. Where a brand turns out to be a sub-line, a re-brand or the same company as one already on the map (check `canonical_keys.txt`), stop on that brand, say so in `NOTE.md`, and go to the next.

## The brands

- **3sixteen**
- **Dehen 1920**
- **Gitman Vintage**
- **Viberg**
- **The Rite Stuff**
- **Railcar Fine Goods**

Use the brand name exactly as written above for the `brand` column. If the brand's own mark differs, say so in `mark_as_written`; Sebastian rules on marks.

The standing rulings from the earlier seating briefs hold:

- **Men's range only.** Say how you scoped the pages. A brand that sells only women's or only goods that aren't clothing or footwear (hosiery, accessories): return the facts-first row and stop on that brand.
- **No US door is not a reason to stop.** If the brand has no US store of its own, return `0` with the locator URL or `NONE` and a full record.
- **Own stores versus stockists.** Read the Stockists page and say whether it is a list or a set of features. Count outlets, concessions and pop-ups separately.
- **Prices and currency.** Set the country selector to the United States first. If the site offers only yen, pounds or euros, record those prices, say so in `store_currency`, and don't convert.
- **Where it is made.** Read each garment's country and the named factories, mills and workshops, and say whether the brand owns any of them. This is the main evidence for craft.
- **Founding.** Look for the brand's own statement of the founders, the place and the year. If only press gives it, mark the source as press.

## Pace

Do all 6 facts-first rows first and return them as one file before any full record. Then do the full records in order and return in batches of two brands. A brand that runs past the time box is returned as it stands, with `NC` on the rest.

## Order

1. **Facts first.** Return one row per brand in `facts_first_template.csv`, all 6 together, before any full record:
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
13. **Signature product and pronunciation.** Propose a signature product only if the brand's own pages call something its signature, its standard or its best seller.

14. **Dial evidence** (`rules_dials.md`, `dials_template.csv`): one row for each of the 38 dials, for each brand. Each row carries a proposed score, a quotation or a counted fact from the brand's own pages, the URL and a confidence. Write `NC` where the pages give too little to judge. Read at least ten men's product pages for logo, forgiveness, care and comfort.
15. **Store neighbourhood.** For every own door, name the neighbourhood as the brand or a local guide uses it (West Village, Back Bay), in the `note` column of `own_doors.csv`.

## Rules

- **Name** must match `canonical_keys.txt` where it can. Every brand in this batch is new, so `reconcile.py` will report no match. That is expected.
- **Cell values.** `NC` means nobody looked; `NONE` means it doesn't sell or do it; `np` means no price is published. No empty cells.
- **Full price only.** Use the regular price, not a sale price.
- **Sources.** The brand's own statements first, then press that quotes them. A retailer's prices and descriptions are never the brand's.
- **Bot walls.** One plain try. If a check box appears, ask Sebastian once whether he'll clear it himself.
- **Read only.** Don't sign in, add to cart, sign up or submit anything.
- **Don't touch the map.** Don't send working files. Anything out of scope but noticed goes in `NOTE.md`.

## Time box

- Facts first: about fifteen minutes a brand.
- Full record: about forty minutes a brand.

Past that, return what you have, put `NC` on the rest, and say so.
