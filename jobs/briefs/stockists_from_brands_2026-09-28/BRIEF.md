# stockists_from_brands_2026-09-28 — the other direction of the match

**Issued** 28 September 2026 · **Kind** locations · **Priority-1 rows returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first.

## The job

The stockist register was built one way: each shop\u2019s own brand list, read from its website, matched to
the map. A brand therefore appears against a shop only if that shop lists it online. Many small menswear
stores list nothing, and 18 brands the map says are sold through independents have no stockist on file
at all. **Read the brand\u2019s own stockist page, and return every independent shop it names in the ten
Northeast states** \u2014 Massachusetts, Rhode Island, Connecticut, New Hampshire, Vermont, Maine, New York,
New Jersey, Pennsylvania, Delaware.

`worklist.csv` has all 204 brands; **priority 1** is the 18 with no stockist on file, priority 2 the rest.
Do priority 1 first and return it, then continue. `register_shops.csv` is every shop the register holds
today, so you can say whether a shop is new.

## What to return

One row per brand per shop in `return_template.csv`. For a brand with a locator and no Northeast
independents, one row with the locator URL and `shop_name = NONE`. For a brand that publishes no locator,
one row with `locator_url = NONE` and where you looked in `note`.

- `locator_kind`: `list` (a page listing shops), `map` (a store-locator map; read it by state or by
  searching each state\u2019s largest cities), `search` (a zip search; run the ten states\u2019 main zips), `none`.
- `shop_kind`: `independent` is what we want; return `department` (Nordstrom, Saks) and `brand-owned`
  rows too, marked, so we know what the locator counts, but they will not be seated as stockists.
- Street, city, state, zip as the locator gives them. A shop with no street on the locator gets the
  town and `note: street not on locator`.
- `new_to_register`: `no` if the shop name and town match a row in `register_shops.csv` (spelling may
  differ slightly \u2014 use judgment and say so), else `yes`.

## Before you start

Location Thread II (August 2026) captured stockists as a by-product of reading own-store locators, for
the brands whose locators mix the two \u2014 Ksubi (52 Northeast rows), Marine Layer and a few others \u2014
into a **Wholesale Network** tab of `brand_tracking_*.xlsx`. Ask for that tab; where a brand is in it,
verify the rows against the locator today rather than re-reading from nothing. Its leading-zero ZIP fault
was fixed there; check for it again on any zip search.

## Rules

- The brand\u2019s own locator is the source. Not a retailer\u2019s site, not a third-party directory.
- A locator that shows only own stores counts as `locator_kind = list` with `shop_name = NONE` and the
  note \u201cown stores only\u201d.
- Do not seat, judge or filter shops; that is done on merge.
- Names must match `canonical_keys.txt`; run `reconcile.py` before returning.
- Return `return.csv` and `NOTE.md`, nothing else.

## Time box

Ten minutes a brand for a list, twenty for a map or zip search. Past that, a row with what you have and a
note.
