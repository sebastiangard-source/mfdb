# doors_bhj_2026-10-16: every brand-owned US store for 72 beauty, home and jewelry brands

**Issued** 16 October 2026 · **Kind** locations · **Batches of ten, returned as each is done** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the same job as `doors_womens_2026-10-10`, with the same columns,
definitions and rules, so the returns drop into the one store register beside the clothing brands. It is
a Chrome job, because store locators are JavaScript. If you cannot run a browser, say so and stop.

## Why

The Cyprus Brand Set lists every clothing brand with a full-price store of its own in the US. Cyprus
also needs the beauty, home and jewelry houses that sit in the same malls and shopping streets. Their
**store lists** are all that is wanted. No prices, no dials, no tiers.

## The worklist

`worklist_brands.csv` lists 72 brands in seven categories, in batches of ten:

- **High jewelry and watches** (13)
- **Fine to demi-fine jewelry** (12)
- **Home** (16)
- **Beauty retailers** (4)
- **Prestige fragrance** (12)
- **Skin and body** (9)
- **Makeup** (6)

`site_domain` is `NC` throughout. Establish the brand's own US site first and record it.

## What you return

The same two files as the women's doors job. Use the column templates in this pack.

- `return_doors.csv`: one row per door.
  - `format` is `own-door`, `outlet`, `concession` or `pop-up`.
  - `operator` is filled where a partner, dealer or licensee runs the door.
- `return_counts.csv`: one row per brand.
  - Own stores, outlets and concessions are counted separately.
  - Give the total rows the locator showed, and the read method.
- `NOTE.md`, one per batch.

## Rules (unchanged from the clothing doors jobs)

- **The brand's own locator is the only source.** Do not use Google Maps, Yelp, mall directories or press.
  If the locator cannot be read, return `NC` with the block named.
- **An own door has the brand's name on the door.**
  - A counter or shop-in-shop inside a department store or another retailer is a `concession`. It is
    returned, but it is not an own door.
  - Outlets are `outlet`.
  - "Coming soon" is `status` = opening.
- **Sister banners are separate brands.** Read each from its own locator, filtered by banner, and say how.
- Names must match `canonical_keys.txt`. Run `python3 reconcile.py` before each return.
- `NC` means nobody looked, and an empty cell is an error. A locator that lists 500 stores returns 500 rows.
- **Bot walls:** one plain try. If a check box appears, ask Sebastian once whether he will clear it himself.
  Anything else is `held`, with the wall named. Never work around a wall.
- Do not touch the map.

## Category rules (new for this job)

**Jewelry and watches**

- **Boutiques inside department stores are concessions.** This covers Tiffany at Macy's or Nordstrom,
  Cartier and Van Cleef inside Saks or Neiman Marcus, and David Yurman inside Nordstrom.
- **Rolex, Omega and TAG Heuer list hundreds of authorized retailers. These are not doors.**
  - Count only stores branded with the watch brand's name, such as "Rolex Boutique" or "OMEGA Boutique".
    Name the dealer that runs it in `operator`.
  - A jeweler that sells the watches is a stockist. Count stockists in `return_counts.csv` if the locator
    makes that easy, and do not return them as rows.
- **Showrooms count as own doors,** including appointment-only ones. This covers Brilliant Earth, Blue Nile,
  Mejuri studios and Catbird. Flag "by appointment" in `note`.

**Home**

- **Banners in the same group are separate brands.** Williams Sonoma, Pottery Barn and West Elm are one
  group; so are Crate & Barrel and CB2.
  - Read each banner as itself.
  - Do not count kids' and teen banners: Pottery Barn Kids, Pottery Barn Teen, Crate & Kids and
    RH Baby & Child. Give their counts in `NOTE.md`.
- **RH:** galleries, design galleries and RH Outdoor count as own doors. RH Outlets are `outlet`.
  Restaurants and guesthouses are not stores.
- **European design houses work through dealers.** These are Ligne Roset, Roche Bobois, Poltrona Frau and
  B&B Italia.
  - A store that carries the brand's own name counts as an own door, with the dealer in `operator`.
  - A multi-brand furniture shop that stocks the brand is a stockist. Count it, and do not return it as a row.

**Beauty**

- **Department-store counters are concessions,** including Macy's, Nordstrom, Saks and Bloomingdale's.
  This matters most for Kiehl's, MAC, Jo Malone, Bobbi Brown, La Mer, Origins, Fresh, NARS and
  Charlotte Tilbury. Only freestanding, brand-named stores are own doors.
- **Sephora inside Kohl's is a concession,** and so is Ulta Beauty inside Target. Count them separately
  in `return_counts.csv` as concessions. Do not return them as rows unless the locator lists them one by one.
- **Bluemercury and Space NK** are store chains in their own right. Read them as such.
- **A brand with no freestanding US store is `NONE`, not `NC`.** Fenty Beauty and Augustinus Bader may be
  in this case. Say so in the note.

## Known traps

- **The big chains** are Sephora, Ulta Beauty, Kendra Scott, Williams Sonoma, Pottery
  Barn, Crate & Barrel and L'Occitane. Their locators show the nearest N stores. Page by state or set the
  radius to the maximum, and compare the count the locator reports with the rows you return.
- **Watch-brand locators** default to authorized retailers. Filter to boutiques and say how.
- **International houses** (Graff, Boucheron, Penhaligon's, Buly, Santa Maria Novella, Diptyque) list
  worldwide. Scope to the US.

## Order and time box

Work in worklist order and return batch by batch.

- **Fifteen minutes a brand.**
- **Forty minutes for a paged chain:** Sephora, Ulta Beauty, Kendra Scott, Williams Sonoma, Pottery Barn,
  Crate & Barrel and L'Occitane.
- Past the box, return what you have, `NC` the rest, and say so.
