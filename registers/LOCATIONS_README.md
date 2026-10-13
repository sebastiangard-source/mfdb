# Cyprus locations database — 13 October 2026

Three tables. Every address in them was read from the brand's own store locator or stockist list, by a
reading thread working to written rules, and nothing was taken from Google, Yelp, mall directories or
press. Where a brand's locator could not be read, the brand is absent or marked, never guessed.

## 1. own_stores.csv — 10,923 rows, 392 brands

One row per **full-price, brand-owned US store**. No outlets, factory or clearance stores, concessions,
department-store counters, pop-ups or stockists. Puerto Rico is included; Guam and other territories
are not. Operator- or licensee-run stores under the brand's name are included, with the operator named.

| Column | Meaning |
|---|---|
| `door_id` | Stable 12-character id, from brand + normalized street + ZIP. Never retyped; the geocoding return keys on it. |
| `brand` | The brand's name as the map writes it (the "canonical key"). |
| `map` | `men` — a brand seated on the Menswear Spectrum (6,450 rows, 236 brands); `women` — a brand from the women's universe not on the men's map (4,473 rows, 156 brands). A brand that sells both is `men` once, not twice. |
| `store_name`, `banner` | The store's name and the banner on the door as the locator gives them (e.g. "Michael Kors Collection", "GUESS Jeans", "Gap"). |
| `street`, `city`, `state`, `zip` | The address as the locator writes it; ZIP is five digits, empty (115 rows) where the locator publishes none. State is a two-letter code — NC is North Carolina. |
| `country` | US throughout (PR rows carry PR in `state`). |
| `phone` | As published; empty for about half the rows (many locators give none). |
| `venue` | The mall, center or building the locator names, where it names one (2,800 rows). Not derived from the address. |
| `operator` | A partner, licensee or resort retailer that runs the door, where the locator says so. |
| `neighbourhood` | New York City rows only: the neighbourhood from the ZIP (SoHo, Upper East Side …), for the map. |
| `source` | The reading job that produced the row: `recapture-2026-10-10` (the original 206 men's brands, re-read in full on 10 Oct), `seat_wave_a/b/c_2026-10-08` (brands seated in waves A–C), `own_doors_womens_2026-10-10.csv` (every women's doors job), `own_doors_wave_c_2026-10-08.csv` (wave C brands counted but not yet seated: Zara, Jos. A. Bank, UGG). |
| `captured_on` | The date the locator was read, where the job recorded one. |
| `lat`, `lon`, `geo_source`, `geo_match` | Empty. Filled by the geocoding job, which has this file. |

Rows de-duplicate on brand + street (suite and unit stripped) + ZIP, so a store listed twice by one
locator is one row; a store two brands share (DKNY and Karl Lagerfeld Paris in the same G-III outlet) is
one row per brand, flagged in the source register.

**What is not here, by rule:** outlets and factory stores (counted separately in the registers — about
3,400 rows); concessions and shop-in-shops (Bloomingdale's shops for ba&sh, Zadig, Marella; Macy's
Herald Square for UGG); pop-ups; stores marked opening or closed; stores the thread could not confirm.

## 2. stockists_by_brand.csv — 1,990 rows, 136 brands

One row per **brand × independent stockist**, for the men's brands banded Premium, Accessible or True
Luxury, read from each brand's own stockist locator. Department stores, online-only retailers and other
brands' stores are excluded; running-shoe houses' lists (Hoka, On — run-specialty shops) are excluded by
ruling. Same address columns as above, plus `kind` (always `stockist` here), `shop_name` and `shop_kind`
(`independent` or `golf club or pro shop`; a finer taxonomy is on the list). `source` says which read:
the wave A/B/C stockist files are US-wide reads from the brand's locator; `ne_shop_register` is the
Northeast specialty-shop register built for the map's region feature.

**Coverage is partial and uneven.** Only the 136 brands read in waves A–C have a national stockist list;
the other 172 Premium-and-above men's brands have at most the Northeast register. Women's brands have
stockists only for the 19 Net-a-Porter brands read so far (in a separate file in the registers, not
yet merged here). This table is the practice run for the stockist layer, not the finished layer.

## 3. stockist_shops.csv — 1,425 rows

The same stockists as **one row per physical shop**, with `brands_on_file` (how many of our brands list
it) and `brands` (which). Sorted by brands carried: Richards (Greenwich, 24), Mitchells (Westport, 22),
Boyds (Philadelphia, 18), Louie, Giblees, Puritan Cape Cod, Weitzenkorn's, Raggs, Larrimor's, Moda.

## Provenance and rules

Every row traces to a reading job whose brief, rules and return (with the thread's NOTE on what it could
not read) are in the Spectrum repository under `jobs/briefs` and `jobs/returns`. The rulings that shaped
the data — what counts as an own door, what is an outlet, concessions, pop-ups, operator-run doors,
territories, shared doors, the stockist exclusions — are collected in `jobs/briefs/RULINGS_*.md`. The
build scripts (`tools/doors_db.py`, `tools/locations_db_v2.py`) rebuild all three tables from the
registers in seconds, so a refresh is a re-read, not a re-build.

## Still to come

Wave C batches 5–9 (41 men's brands, Mango and Zara among them); the Net-a-Porter women's job (142
brands); the Rue La La brief (11 women's reads); coordinates from the geocoding job; a national
stockist read for the 172 unread men's brands; the women's price pass, which bands the women's brands
so the Premium-and-above filter applies to both sides.
