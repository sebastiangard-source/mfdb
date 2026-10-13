# doors_womens_nap_2026-10-12 — job summary

**Done, 13 Oct 2026. Part 1: 72 of 73 brands, with Anna Sui left out by your ruling. Part 2: all 88 brands screened. Every batch passed `reconcile.py` with 0 unmatched, and there are no empty cells in any file.**

## Files for the main thread

| File | Rows | What |
|---|---|---|
| `doors_womens_nap_ALL_return_counts.csv` | 72 | Part 1, one row per brand |
| `doors_womens_nap_ALL_return_doors.csv` | 52 | US doors from both parts: 49 own doors, 2 concessions, 1 pop-up (not counted) |
| `doors_womens_nap_ALL_return_stockists.csv` | 1,103 | Part 1 US stockists, full names and addresses where the brand gives them (36 brands) |
| `doors_womens_nap_ALL_return_screen.csv` | 88 | Part 2 screen, one row per brand |
| `wrong_sites.csv` | 23 | Domains that are wrong, parked or unsafe (review below) |

Each batch folder also has its own `NOTE.md`: `doors_womens_nap_batch01`–`08` and `doors_womens_nap_part2_batch01`–`05`.

## Headline numbers

**Part 1: 16 brands have US doors.** In all, 35 own doors and 2 concessions; no brand has a US outlet.

| Brands | US own doors |
|---|---|
| Still Here, Gianvito Rossi (+1 concession) | 5 each |
| Loeffler Randall | 4 |
| Manolo Blahnik, Roger Vivier (+1 concession) | 3 each |
| Sporty & Rich, Tibi, We Norwegians, Aquazzura | 2 each |
| Elie Saab, Extreme Cashmere, Lauren Manoogian, RIXO, Sanderlak, The Frankie Shop, Le Monde Béryl | 1 each |

**Part 2: 11 of 88 brands have a US store, 14 doors in all.**

- Danielle Frankel, KALLMEYER, Suzie Kondi: 2 each.
- AFLALO, B SIDES, Kartik Research, MAISON MAYLE, Miguelina, RÙADH, Veronica de Piante, Wiederhoeft: 1 each.

Nearly all are in New York.

## `NC` rows: nobody could look

| Brand | Part | Why |
|---|---|---|
| Sorel | 1 | Locator sits behind a "Press & Hold" bot check, which was not attempted |
| Sportmax | 1 | Locator links redirect to the home page from the US |
| Posse | 1 | No brand site found |
| LEGRES | 1 | No brand site found |
| Away That Day | 2 | Site password-locked for maintenance |
| OTZI | 2 | No site found; NAP designer page says "Coming soon" |

Sorel is the one most likely to have real US doors.

## Calls the main thread should confirm

1. **Appointment studios and salons.** Five Part 2 counts rest on this:
   - Danielle Frankel (2)
   - RÙADH, Wiederhoeft, AFLALO (1 each)
   They are counted because the brand publishes an address and books customers in. Without them, Part 2 has 9 doors, not 14.
   Not counted:
   - Calle Del Mar and Sara Cristina, because no address is given.
   - Autumn Sonata, because its space is trade-only.
2. **Concessions are kept separate from own doors.** These are brand-run shop-in-shops inside Bloomingdale's 59th St: Gianvito Rossi and Roger Vivier.
3. **One pop-up is not counted.** Donde Esteban's Miami Beach pop-up has no year or end date, so it has status `NC`. lemlem's past NYC pop-up is not counted either.
4. **Worklist "clothing" is often wrong in Part 2.** Several brands are jewelry, which the brief excludes: Established, Joelle Kharrat, Le Sundial, Julietta. Others are:
   - Bags: Liffner, Valesque, Olympia Le-Tan, RUE de VERNEUIL.
   - Footwear: JUDE, CHRISTEN.
   - Belts: Déhanche.
   - Hosiery: Comme Si.
   - Eyewear: Thistles.
   - Hats: SENSI STUDIO.
   - Homeware or furniture: Fourth Street, LOUISE ROE, SIX THE RESIDENCE, The House of Lyria, Autumn Sonata.
   Each is flagged in `note`.

## Wrong-sites list: review

`site_domain` was `NC` for every worklist row, so these are the obvious domains that turned out wrong.

**Unsafe. Do not open:**
- `floreflore.com` (FLORE FLORE): redirects to a fake "Apple Security Center" page.
- `gettallermarmo.shop` (Taller Marmo): a look-alike "Official Boutique" that came up in search. It was not opened.

**Parked or for sale:**
- Paris Texas: `paris-texas.com`
- BLAZÉ Milano: `blazemilano.com`
- Clio Peppiatt: `cliopeppiatt.com`
- STOULS: `stouls.com`, `stouls.fr`
- OTZI: `otzi.com`
- LEGRES: `legres.com`
- Maryam Nassir Zadeh: `mnzstore.com`
- Posse: `posse.co`

**Someone else's site:**
- Paris Texas: `paristexas.com` (Chamber of Commerce)
- ST. AGNI: `stagni.com` (accounting firm)
- Hunting Season: `huntingseason.com`
- Liffner: `liffner.com` (an illustrator)
- LEGRES: `legres.fr` (a town council)
- Danielle Frankel: `daniellefrankel.com` (GoDaddy placeholder)

**Broken:**
- AARON ESH: `aaronesh.com` (SSL error)
- Loretta Caponi: `lorettacaponi.com` (certificate error, not bypassed)
- Donde Esteban: `dondeesteban.com` (no DNS)
- Matteau: `matteau.com` (does not load)
- ROTATE Birger Christensen: `rotate-birger-christensen.com` (does not load)

**From batches 1–2:** Aje, Cap d’Antibes, HIGH SPORT and Haight. Details are in the CSV.

The correct domain for each is in the `correct_domain` column. Posse, LEGRES and OTZI are still `NC`.

## Method

- Every count comes from the brand's own site only, read in Chrome. Sources:
  - store pages
  - the locator's own data feed (stockist.co, Alpine and Demandware data)
  - the brand's own sitemap
- Part 2 was a screen. It covered nav and footer links, the full page sitemap, and any store, stockist, showroom or contact page.
- Stockists were recorded for Part 1 only.
