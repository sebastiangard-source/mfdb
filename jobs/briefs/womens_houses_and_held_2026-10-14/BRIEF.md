# womens_houses_and_held_2026-10-14 — Chanel and Miu Miu for the women's map; Kapital, UGG, Y-3 and Sanderlak for the men's

**Issued** 14 October 2026 · **Kind** read · **Two parts, each returned as done** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. Chrome job on the brands' own US sites. If you cannot run a browser, say so and
stop. About an hour: forty minutes for Part 1, twenty to thirty for Part 2. Part 1 duplicates Part B of
`womens_crossover_2026-10-14`; if another thread has already returned that, skip to Part 2 and say so.

## Part 1 — Chanel and Miu Miu, the full women's read (`part1_womens/`)

Both houses sell women's ready-to-wear in their own US stores and appear on no Cyprus register, because they have
no menswear and no department-store floor. Read each as the women's jobs read the other 244 brands. One return of
four files, in the columns of the templates:

1. **Doors** — `return_b_counts.csv` and `return_b_doors.csv`: every US store on the brand's own locator, own-door /
   outlet / concession / pop-up, open or opening, street, city, state, zip, venue, operator. Boutiques inside Saks,
   Neiman Marcus, Bloomingdale's or Nordstrom are concessions, not doors — Chanel has many. Fragrance, beauty, eyewear
   and watch counters are not doors. The rules are those of `rules_doors_reference.md`, unchanged.
2. **Prices** — `return_b_prices.csv`: the eight women's garments (tee, blouse, sweater, jeans, trousers, dress,
   outerwear, shoes), entry and top, product and URL behind every figure, full price, women's range only. Chanel
   publishes ready-to-wear prices on chanel.com; "price on request" is `np`. Leather and suede are never an outerwear
   high (ruled 14 Oct); nor are fur, shearling, exotics, runway-flagged or capsule pieces. The band is set at merge
   (women's cuts $200 / $600 on the blouse-and-sweater mean; both will read True Luxury).
3. **Facts** — `return_b_facts.csv`: what it sells (one plain sentence under thirty words), channels (O/D/I/W),
   founding year, place and founders, owner today with the filing (Chanel Limited is private; Miu Miu is Prada
   S.p.A., listed in Hong Kong — the annual report is the source), signature product, pronunciation, lookbook,
   Vinted women's URL and The RealReal page, B Corp / GOTS from the certifiers' directories, one real quotation
   under `rules_quotes.md`.

`NOTE_1.md` for the pair. Names: `canonical_keys.txt` in the folder.

## Part 2 — four men's brands the map holds (`part2_mens/`)

These sit off the men's map for want of a read. Return `return.csv` in the columns of `return_template.csv` (the wave C
record), one row per brand, plus `own_doors.csv` and `stockists.csv` for Sanderlak, and `NOTE_2.md`. The rules
files are the wave C ones, unchanged.

- **Kapital** — every price `NC` on 12 Oct: kapital.jp gave no US-readable price in the time box, and there is no US
  store. Read the eight men's garments on kapital.jp in **JPY, not converted** (`currency` = JPY; two displayed prices
  confirm it), product and URL behind each. If the site offers a US storefront with USD, use that and say so. Styles
  and fibre as the wave C rules ask, within thirty minutes; past that, `partial`.
- **UGG** — on 13 Oct ugg.com put up a slide-puzzle bot check after the listing, so prices and composition are `NC`.
  Do not solve the check. Load the homepage, click into Men's, and read if it lets you; if the wall is still up after
  one plain reload a few minutes later, `NC` and say what you saw. The door counts (10 own, 36 outlets, 1 concession)
  are carried — do not re-read the locator.
- **Y-3** — not read on 13 Oct: www.y-3.com does not resolve and adidas.com was not retried. The ruling against
  re-reading adidas.com was for adidas's own seat; for Y-3, read **adidas.com/us/y-3** as the brand's US store.
  Eight garments, styles, fibre, doors (Y-3 has no stores of its own in the US; say so and give the count as 0 if
  the locator confirms it), facts.
- **Sanderlak** — ruled 14 Oct onto the men's map (menswear-led; its 52-piece women's collection was read on the
  women's side and is excluded there). A full wave C seat: facts-first row, eight men's garments, styles and fibre,
  own doors worldwide (one US store is on file), stockists it lists, tech, craft, origin and ownership, lookbook,
  Vinted and Grailed, certifications, a quotation, the signature product.

## Rules

- Names must match `canonical_keys.txt` in each part's folder; run `python3 reconcile.py` from inside that folder
  before each return.
- `NC` nobody looked; `NONE` does not sell or do; `np` no price published. No empty cells.
- Full price only; the brand's own site and locator; never a workaround for a bot wall.
- Do not touch either map. Out of scope but noticed: the part's `NOTE`.
