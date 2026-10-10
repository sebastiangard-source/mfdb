# doors_womens_2026-10-10 — every brand-owned US store for 36 women's brands, with a full address

**Issued** 10 October 2026 · **Kind** locations · **No pilot; return in batches of ten** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the women's twin of `doors_recapture_2026-10-10`, issued the
same morning: **the same returns, the same columns, the same definitions, the same rules**, so the two
files merge into one store register without reconciliation. It is a Chrome job: store locators are
JavaScript. If you cannot run a browser, say so and stop.

## Why

A women's version of the map is coming, and before it starts we need one complete list of every
brand-owned store in the US, men's and women's together. The men's brief covers the 206 brands on the
men's map. This one covers 36 brands that are women's only, or essentially so, and are not on the
men's map. Isabel Marant was on the list and is skipped: it is seated on the men's map and its stores
come back with the men's job.

## One worklist, two returns

`worklist_brands.csv`: 36 brands with a note on the line (women's only; essentially women's with a
small men's line; luxury women's). `site_domain` is `NC` throughout — establish the brand's own US
site first and record it.

For every brand: open the brand's own US store locator in Chrome, make it list every US location (set
the radius to the maximum, or page through states, or read the locator's JSON — say which in
`read_method`), and return **one row per door** in `return_doors.csv`, with `format` = own-door,
outlet, concession or pop-up and `operator` where a store is run by a licensee or partner (operator-run
doors under the brand's banner count as the brand's, flagged). Then one row per brand in
`return_counts.csv`: own stores, outlets and concessions counted separately, the total rows the
locator showed, and the method.

## Rules

- **The brand's own locator is the only source for a door.** Not Google Maps, not Yelp, not a mall
  directory, not press. If the locator cannot be read even in Chrome, `NC` for the brand with the exact
  block in `note`.
- **Own door means the brand's name on the door.** A shop-in-shop at Nordstrom or Bloomingdale's is a
  concession. An outlet is an outlet (Talbots, LOFT, Chico's, J.Jill and Tory Burch have large outlet
  estates; keep them separate). A "coming soon" is `status` = opening, with the date if given.
- Department-store counters are not doors.
- **Sister banners are separate brands.** Anthropologie and Free People (URBN), LOFT (Ann Inc.), Soma
  and White House Black Market (Chico's FAS), Aerie (American Eagle), Athleta (Gap): each returns under
  its own name from its own locator, and a shared locator is filtered by banner, said how. An Aerie
  shop inside an American Eagle store is a concession under Aerie, not an Aerie door.
- Names must match `canonical_keys.txt`; run `python3 reconcile.py` before returning. Where the
  brand's own mark differs from the key (J.Jill vs J. Jill, STAUD, Altar'd State), say so in `note`.
- `NC` nobody looked; an empty cell is an error. A locator that lists 500 stores returns 500 rows.
- Street addresses as the locator writes them, ZIP five digits, state two letters, NYC rows with the
  five-digit ZIP so the neighbourhood can be derived.
- Do not touch the map. Return the two files and `NOTE.md`: what was read, what could not be, and
  anything the worklist got wrong (a brand with no US stores, a brand that is really a line of another).

## Known traps

- **The mall chains are big.** Talbots, LOFT, Chico's, White House Black Market, J.Jill, Soma, Athleta,
  Aerie, Anthropologie and Free People each run from a hundred to several hundred US doors; their
  locators show the nearest N and need paging by state or a radius set to the maximum. Read the count
  the locator reports before trusting the list, and compare it with the rows returned.
- **Outlet-heavy banners** (Talbots, Chico's, Tory Burch, Lilly Pulitzer) mix outlet and full-price in
  one locator; filter and say how.
- **Brandy Melville** publishes a store list rather than a locator; read it as the source.
- **Wolford, Max Mara, Zimmermann, Maje** have US locators on international sites; scope to US and watch
  for concessions in Saks, Neiman Marcus and Bloomingdale's listed as if they were stores.
- Locators that cap at 50 or 100 results silently; compare the count shown with the rows returned.

## Order and time box

Worklist order, returned in batches of ten. Fifteen minutes a brand for a Shopify locator, forty for a
paged chain; past that, what you have, `NC` on the rest, said so.
