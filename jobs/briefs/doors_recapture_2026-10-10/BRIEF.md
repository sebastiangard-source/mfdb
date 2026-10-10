# doors_recapture_2026-10-10 — every brand-owned US store, with a full address, once

**Issued** 10 October 2026 · **Kind** locations · **Priority A returned first, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job: store locators are JavaScript, and the one pass
that tried them without a browser returned `NC` on a quarter of its brands. If you cannot run a
browser, say so and stop.

## Why

The map claims 3,482 brand-owned US stores across 206 brands and has 3,050 addressed rows. The gap is
mostly a handful of chains whose count was inherited from an August master and whose locator was never
read: Alo claims 144 stores and has no address on file; Levi's 97 and 14; J.Crew 112 and 32; BOSS 59
and 8. Beyond those, 95 brands carry a count that nobody has checked since August, 138 rows have a
street but no ZIP, and 33 shops in the stockist register have no street at all. This brief closes all
of it in one pass, so the question never has to be asked again.

## Three worklists, three returns

**1. `worklist_brands.csv` → `return_doors.csv` + `return_counts.csv`.** 140 brands, by priority.

- **A (13)** — count and rows disagree by five or more, or there are no rows at all. Alo, Levi's,
  J.Crew, BOSS, Dior, Diesel, Sandro, Mizzen+Main, Malbon, Carhartt (68 rows against a count of 61 —
  the count is stale the other way), Reiss, Joe's Jeans, Purple. **Return these first.**
- **B (95)** — the count was inherited from the master and never recaptured. Read the locator, return
  every US door, and the count falls out.
- **C (32)** — recaptured in September; confirm the count still holds and fill the missing ZIPs.

For every brand: open the brand's own US store locator in Chrome, make it list every US location (set
the radius to the maximum, or page through states, or read the locator's JSON — say which in
`read_method`), and return **one row per door** in `return_doors.csv`, with `format` = own-door,
outlet, concession or pop-up and `operator` where a store is run by a licensee or partner (ruled 8
October: operator-run doors under the brand's banner count as the brand's, flagged). Then one row per
brand in `return_counts.csv`: own stores, outlets and concessions counted separately, the total rows
the locator showed, and the method.

**2. `worklist_shops.csv` → `return_shops.csv`.** 33 shops in the stockist register with a town and
no street — mostly the Mid-Atlantic register rows (Hans Clothier in Far Hills, and the like). Street,
ZIP and website from the shop's own site or its Google listing; if the shop has closed, say so in
`note` with the source, do not invent an address.

**3. `worklist_zips.csv` → fold into `return_doors.csv`.** 138 own-door rows with a street and no
ZIP. These will mostly be covered by the locator reads in part 1; any that are not, look up the ZIP
for the street and return the row.

## Rules

- **The brand's own locator is the only source for a door.** Not Google Maps, not Yelp, not a mall
  directory, not press. If the locator cannot be read even in Chrome, `NC` for the brand with the exact
  block in `note`, and the count stays as it was.
- **Own door means the brand's name on the door.** A shop-in-shop at Nordstrom is a concession. An
  outlet is an outlet. A "coming soon" is `status` = opening, with the date if given.
- Department-store counters are not doors (Emporio Armani's 92 counters, ruled 8 October).
- Names must match `canonical_keys.txt`; run `python3 reconcile.py` before returning.
- `NC` nobody looked; an empty cell is an error. A locator that lists 144 stores returns 144 rows.
- Street addresses as the locator writes them, ZIP five digits, state two letters, NYC rows with the
  five-digit ZIP so the neighbourhood can be derived.
- Do not touch the map. Return the three files and `NOTE.md`: what was read, what could not be, which
  counts moved by more than two and why.

## Known traps

- **Lululemon, Alo, Levi's, J.Crew, BOSS** have locators that show the nearest N and need paging by
  state or a radius set to the maximum; the September recapture found Lululemon at 379 and J.McLaughlin
  at 164 only by paging. Read the count the locator reports before trusting the list.
- **Levi's and Carhartt** locators mix own stores with dealers; filter to the brand's own stores and
  say how. Carhartt's 68 rows against a count of 61 is probably this.
- **Ralph Lauren** lines (Polo, RRL, RLX, Purple Label) share one locator; filter by label.
- **Nike-style outlet naming** ("Factory Store", "Outlet", "Clearance") is `format` = outlet whatever
  the locator calls it.
- Locators that cap at 50 or 100 results silently; compare the count shown with the rows returned.

## Order and time box

Priority A first, returned without stopping — Alo alone is 144 rows and the biggest single hole on the
map. Then B in worklist order, then C and the shops. Fifteen minutes a brand for a Shopify locator,
forty for a paged one; past that, what you have, `NC` on the rest, said so.
