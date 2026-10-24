# seat_ellicott_eight_2026-10-24: full records for eight brands found at Ellicott & Co.

**Issued** 24 October 2026 · **Kind** seating evidence · **Facts-first rows returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the `seat_resort` record for every brand in `worklist.csv`:

- the 132 columns in `return_template.csv`;
- `own_doors.csv`;
- `stockists.csv`;
- `return_styles.csv`;
- `NOTE.md`.

The rules files in this folder are the standing rules and win over any shorthand here. **You gather and you propose; Sebastian rules.**

## The brands

Sebastian found these eight at Ellicott & Co., a men's shop in Lancaster, PA. A sift on 24 October found each to be a real house with its own site and prices. `worklist.csv` has what we know about each.

Five clothing houses:

- American Trench
- Bridge & Burn
- TOPO Designs
- Soft Goods
- Peregrine Clothing

Three shoe houses:

- SeaVees
- Lems
- Nisolo

The standing rulings from the wave A brief hold:

- **Shoe-only houses seat.** Seven `NONE` price slots and a `range` on shoes is the expected row.
- **No US door is not a reason to stop.** A brand with no US store of its own returns `0`, with the locator URL or `NONE` and a full record. The map carries it as a positive zero.
- **Men's range only.** Bridge & Burn, TOPO Designs, Lems and Nisolo also sell women's. Read men's pages only, and say how you scoped them.

Brand by brand:

- **TOPO Designs.** Seat or bench is still open, because it is mostly packs and gear. Read its men's clothing only: tees, shirts, pants, sweaters and jackets. In `NOTE.md`, give the share of its men's catalog that is clothing rather than bags and gear, so Sebastian can rule. Its own locator lists four stores (Denver flagship, Fort Collins, Denver Base Camp, Hayes Valley San Francisco). Count them from the locator.
- **Peregrine Clothing.** Before anything else, open Ellicott & Co.'s own Peregrine product pages (ellicott.co, brand page or search). Confirm the knitwear there is the UK house at peregrineclothing.co.uk. If it isn't, stop on Peregrine and say so. Read its US/USD storefront. Origin is Wigston Magna, Leicestershire, 1796. Its knitwear factory is in Manchester, so check made-in claims product by product. Selfridges spaces and pop-ups are not own doors.
- **Soft Goods** sold private-label for others before opening its own shop in 2025. Read only the Soft Goods-branded range, not anything it made for other labels. It runs its own factory in Corktown, Detroit; this is the craft section's main evidence. Its stockists page wouldn't load on 24 October; try once more.
- **American Trench** lists its stockists on americantrench.com/pages/stockists-1. Return them in `stockists.csv`. Its founding year (2012) so far comes from press; find the brand's own statement if there is one.
- **Nisolo.** Its own site gives no founding city or year, so mark the press source if that is all there is. Press mentions a Nashville store. Confirm it on nisolo.com, or return `0`.
- **Lems.** Its store locator is a retailer finder (Locally), not a list of its own stores. Return `0` unless the brand names a store of its own. It moved to Boulder in 2016; give the original city if the brand states it.
- **SeaVees.** The Santa Barbara flagship (24 E Mason St) is the only store on its stores page. Count it from the page.

## Order

1. **Facts first, for every brand, before any full record.** Return one row per brand in `facts_first_template.csv`:
   - site and US storefront;
   - own-store count, with its source;
   - what it sells;
   - an entry price and a top price;
   - a band guess;
   - the brand's mark as it writes it.

   Allow ten minutes a brand.
2. **Then the full record,** in worklist order. Return it in two batches: the five clothing houses, then the three shoe houses.

## The sections, and the rules file for each

1. **Store, currency, search** (`rules_prices.md`): the US storefront, with USD confirmed on two displayed prices.
2. **Eight garments** (`rules_prices.md`, `rules_garment_links.md`): prices and men's listing links. Put the product and URL behind every figure. A shoe house is `NONE` on seven.
3. **Fiber by style** (`rules_fibre.md`, `schema_styles.json`): men's clothing styles. For shoe houses, give the upper materials in `note`; no style file.
4. **Own doors**, worldwide, US first. Count outlets, concessions and pop-ups separately.
5. **Stockists**: those the brand itself lists.
6. **Tech.**
7. **Craft** (`rules_craft.md`, `rubric_craft.txt`): six facts, two URLs, a proposed score and the reasoning. Made-in claims, named factories and owned facilities matter most here. Several of these brands make a point of them.
8. **Origin and ownership**, from the brand's own statements first.
9. **Lookbook.**
10. **Vinted and Grailed.**
11. **B Corp and GOTS**, from the certifiers' own directories.
12. **One real quotation** (`rules_quotes.md`).
13. **Signature product and pronunciation.**

## Rules

- **Names** must match `canonical_keys.txt`. Run `python3 reconcile.py` before each return. Where the brand's own mark differs, say so in `mark_as_written`; Sebastian rules on marks. TOPO Designs may write itself "Topo Designs".
- **Cell values.** `NC` means nobody looked; `NONE` means it doesn't sell or do it; `np` means no price is published. No empty cells.
- **Full price only.** Several of these sites run sitewide promotions; use the regular price.
- **Sources.** The brand's own statements first, then press that quotes them. Ellicott & Co.'s prices and descriptions are never the brand's.
- **Bot walls.** One plain try. If a check box appears, ask Sebastian once whether he'll clear it himself.
- **Read only.** Don't sign in, add to cart, sign up or submit anything.
- **Don't touch the map.** Don't send working files. Anything out of scope but noticed goes in `NOTE.md`.

## Time box

- Facts first: about ninety minutes for all eight.
- Full records: forty minutes per clothing house, twenty-five per shoe house.

Past that, return what you have, put `NC` on the rest, and say so.
