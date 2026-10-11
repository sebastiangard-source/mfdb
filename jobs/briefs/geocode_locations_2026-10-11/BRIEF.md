# geocode_locations_2026-10-11 — latitude and longitude for 9,061 brand-owned US stores

**Issued** 11 October 2026 · **Kind** geocoding · **Returns to** Sebastian, who passes it to the Spectrum thread

This brief is self-contained. You are a separate project with no other context; everything you need
is in this folder. Read this file to the end before starting.

## What you are given

`locations_db_v1.csv` — 9,061 rows, one per door. Every row is a **full-price, brand-owned US store**
(no outlets, concessions, department-store counters, pop-ups or stockists) for 233 menswear and
womenswear brands, with the address as the brand's own store locator writes it. Columns:

`door_id, brand, map, store_name, banner, street, city, state, zip, country, phone, venue, operator,
neighbourhood, source, captured_on, lat, lon, geo_source, geo_match`

- `door_id` is the key. Return it unchanged; never retype it.
- `street`, `city`, `state`, `zip` are the address. 70 rows have no ZIP; the street and city are still
  there. `venue` is the mall or center name where the locator gave one, which helps when a street is
  a mall address ("6010 Mall Walk, Suite 8080").
- `lat`, `lon`, `geo_source`, `geo_match` are empty. They are what you fill.

## What you return

`return.csv` with the columns of `return_template.csv`:

`door_id, lat, lon, geo_source, geo_match, matched_address, geo_note`

**One row for every door_id in the input, 9,061 rows, no empty cells.** A door you could not place
is a row too, with `NC` in `lat`, `lon`, `geo_source`, `geo_match` and `matched_address` and the
reason in `geo_note`. An empty cell is an error; `NC` means nobody could place it.

- `lat`, `lon`: decimal degrees, WGS84, at least four decimal places (four decimals is about 11 m).
- `geo_source`: which service gave the point — `census`, `nominatim`, `google`, `locator` (the
  brand's own store page or locator feed states the coordinates) or another named service.
- `geo_match`: the precision the service reported, mapped to one of `rooftop` (the building),
  `street` (interpolated along the block), `range` (address range), `locator` (the brand's own
  coordinates), or `NC`. **Never return a ZIP centroid, a city centroid or a state centroid as a
  point.** If the best a service can do is a centroid, the row is `NC` and the note says so.
- `matched_address`: the address the service matched, as it returned it, so a bad match can be seen.
- `geo_note`: anything a reader needs: ZIP supplied by the geocoder, a street cleaned to get a match,
  a second service used after the first failed, a disagreement between services.

Run `python3 validate_return.py locations_db_v1.csv return.csv` before returning. It checks every
door_id is present once, no cell is empty, every point is inside its state, and every `geo_match`
is from the list. Return only when it passes.

## Method, in order

1. **The U.S. Census Bureau batch geocoder** first — free, no key, built for exactly this
   (`https://geocoding.geo.census.gov/geocoder/locations/addressbatch`, benchmark
   `Public_AR_Current`, up to 10,000 addresses per POST as a CSV of `id, street, city, state, zip`).
   Use `door_id` as the id. It returns the matched address, a match indicator (Exact / Non_Exact /
   Tie / No_Match) and coordinates. File Exact as `rooftop`, Non_Exact as `street`, Tie and
   No_Match as unmatched for step 2.
2. **Nominatim (OpenStreetMap)** for what Census could not match — one request per second, a
   descriptive User-Agent, the structured query (`street`, `city`, `state`, `postalcode`,
   `country=US`). Accept only results whose `addresstype` is `building`, `shop`, `house` or similar
   and whose returned house number matches; a result typed `postcode`, `city` or `suburb` is a
   centroid and is `NC`.
3. **Any other service** you have a key for (Google, Mapbox, HERE) is fine for the remainder, with
   the same precision rule and `geo_source` naming it.
4. **Clean, don't invent.** Strip suite, unit and floor from `street` before geocoding; fix
   obvious casing; use `venue` to disambiguate a mall address. Never change the city or state to get
   a match — a row whose city is wrong is a finding for `geo_note`, not something to correct.

## Rules

- `NC` nobody could place it; never a centroid, never a guess. Wrong is worse than missing.
- Every point carries the service and the precision it reported. A point without provenance is not
  a point.
- Do not touch the input file. Do not add, drop or re-order rows. Do not retype door_ids.
- Where two services disagree by more than 200 m, say so in `geo_note` and return the higher
  precision.
- Return in two parts if it helps: `return_part1.csv` (Census) as soon as it is done, then the
  full `return.csv`.

## What good looks like

9,061 rows; 95% or more at `rooftop` or `street`; every `NC` with a reason a reader could act on;
the validator passing. Mall addresses and suite numbers are where this usually goes wrong; the
`venue` column is there for them.

## Time box

The Census batch is minutes. Nominatim for the remainder is about an hour per 3,000 rows at one
request a second. If a service is down or refusing, say which, return what you have, and stop.
