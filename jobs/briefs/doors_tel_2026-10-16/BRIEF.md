# doors_tel_2026-10-16: every brand-owned US store for 28 travel, eyewear and bag brands

**Issued** 16 October 2026 · **Kind** locations · **Batches of ten, returned as each is done** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the same job as `doors_bhj_2026-10-16` (beauty, home and jewelry), with the same columns and rules. It covers three more groups for the Brand Set's Other brands section. It is a Chrome job; if you cannot run a browser, say so and stop.

## Why

The Cyprus Brand Set lists every fashion brand with full-price stores of its own in the US. It also has an Other brands section for the houses that share their malls and shopping streets. Only their **store lists** are wanted: no prices, no dials, no tiers.

## The worklist

`worklist_brands.csv` lists 28 brands in three groups, in batches of ten:

- **Travel** (10): Away, Monos, Rimowa, Tumi, Béis, Calpak, Paravel, Briggs & Riley, Samsonite, July.
- **Eyewear** (8): Warby Parker, Moscot, Oliver Peoples, Garrett Leight, Gentle Monster, Ray-Ban, Persol, Jacques Marie Mage.
- **Bags and leather goods** (10): Coach, Longchamp, Polène, Cuyana, Senreve, Strathberry, Mulberry, Smythson, Goyard, Moynat.

`site_domain` is `NC` throughout. Establish each brand's own US site first.

## What you return

The same files as `doors_bhj`.

- `return_doors.csv`: one row per door.
  - `format` is `own-door`, `outlet`, `concession` or `pop-up`.
  - `operator` is filled where a partner or licensee runs the door.
- `return_counts.csv`: one row per brand.
  - Own stores, outlets, concessions and stockists (`us_stockists`) counted separately.
  - Give the locator's total rows and the read method.
- `NOTE.md`, one per batch.

## Rules (as in doors_bhj, with the rulings made there)

- **The brand's own locator is the only source.** If it can't be read, the brand is `NC` and the block is named.
- **An own door has the brand's name on the door.**
  - A counter or shop-in-shop inside another store is never a row, even inside a department store and even when the locator names it as the brand's. Put its count in `us_concessions` if the locator makes that easy; otherwise `NC`.
  - A department-store or retailer door listed under the store's own name is a stockist, counted only.
  - Outlets are `outlet`.
  - A store marked opening or coming soon gets `status` = opening.
  - Closed stores are not returned.
- **Venue comes only from the locator:** a centre it names, or its store label where that is a centre. Otherwise `street`. Never work it out from the address.
- **Same address, one store.** Return both entries, and say so in `note`.
- **A dealer-run store under the brand's name is an own door,** with the dealer in `operator`.
- **Sister banners are separate brands.** Read the worklist brand only, and say what you left out.
- **Bot walls:** one plain try. If a check box appears, ask Sebastian once. Anything else is `held`, with the wall named.
- **Pace:** one store page at a time, a few seconds apart. Opening pages quickly tripped RH's wall.
- Names must match `canonical_keys.txt`. Run `python3 reconcile.py` before each return. No empty cells.

## Group notes

**Travel**

- Away, Monos, Béis, Calpak and July are mostly online, with a few stores each. A brand with no store of its own in the US is `NONE`, not `NC`.
- **Rimowa and Tumi** have boutiques of their own, plus many retailer and department-store doors. Only the brand-named stores are rows.
- **Samsonite** has many outlet stores. Keep them as `outlet`. "Samsonite Black Label" stores, if listed, are own doors, noted.
- **Briggs & Riley** sells mostly through retailers and may have few or no stores of its own.

**Eyewear**

- **Warby Parker** has 250 or more stores; page by state or read its full list.
- **Ray-Ban and Persol** sit inside EssilorLuxottica's retail network.
  - Count only stores under the Ray-Ban or Persol name.
  - Sunglass Hut, LensCrafters and Target Optical are stockists, counted only.
- **Oliver Peoples, Moscot, Garrett Leight and Jacques Marie Mage** each have a few boutiques plus many optician stockists. Count the opticians only.

**Bags and leather goods**

- **Coach** has hundreds of full-price stores and many outlets: separate them. Coach Outlet is an outlet.
- **Longchamp** has boutiques plus many department-store shops. Only the boutiques are rows; count the shops.
- **Goyard and Moynat** have a few boutiques each. Goyard's US locations may be listed only on a boutiques page.
- **Cuyana, Senreve and Polène** have a few showrooms or stores each.
- **Mulberry, Strathberry and Smythson** are UK houses. Scope to US stores. Shops inside Bloomingdale's, Saks or Nordstrom are not rows; count them.

## Order and time box

Work in worklist order and return batch by batch.

- **Fifteen minutes a brand.**
- **Forty minutes for a big chain:** Warby Parker, Coach and Samsonite.
- Past the box, return what you have, `NC` the rest, and say so.
