# doors_womens_2_2026-10-12: complete return

All 405 worklist brands are read, plus the 2 brands Sebastian added (DÔEN and Nour Hammour). Captured 12 Oct 2026 in Chrome.
Batches 01–07 were read in the main thread and returned one by one, with rulings applied. The rest were read in parallel: Part 1 batches 08–13 by three readers, and Part 2 screen batches 01–15 by six. All used the same written rules and schema, and each reader worked only in its own tab.

## Files in this folder: merged across every batch

| File | Rows | Contents |
|---|---|---|
| `return_doors.csv` | 1,930 door rows | Part 1 full reads, plus Part 2 brands with yes and ≤ 25 doors |
| `return_counts.csv` | 123 | Part 1 brands, including DÔEN and Nour Hammour |
| `return_screen.csv` | 284 | Part 2 brands |

The per-batch folders (`doors_womens_2_batch01…13`, `doors_womens_2_screen01…15`) hold the same rows, each with its own NOTE.

- **Doors by format and status:** 821 own-door open, 1,047 outlet open, 43 concession, 8 pop-up, 7 closed, 4 opening.
- **`reconcile.py`:** 407 names. 405 are exact matches, 0 need rewriting, and **2 are unmatched by design**: `DÔEN` and `Nour Hammour`. Add both to `canonical_keys.txt` before merging.
- **Validator, all rows:** no empty cells and every state has 2 letters.
  - ZIP is 5 digits except 48 rows marked `NC`, where the brand's site doesn't publish one.
  - Counts equal the open rows by format for every brand.
  - The one non-5-digit exception from the rulings is Elie Tahari (ZIP NC, by ruling).

## Largest fleets found (own / outlet / concession)

GUESS 36/184/0 · Michael Kors 60/150/0 · Under Armour 15/159/0 · Kate Spade 35/130/0 · Lucky Brand 53/75/0 · Steve Madden 43/43/0 · Marc Jacobs 31/43/0 · Jockey 3/58/0 · True Religion 15/43/0 · UGG 10/36/1 · 7 For All Mankind 21/21/0 · Zadig & Voltaire 22/10/18 · KARL LAGERFELD PARIS 0/31/0 · Jenni Kayne 30/0/0 · SKIMS 23/3/0.

**Part 2 brands that turn out to have fleets (findings):**
- **Hurley:** 1 own + 33 outlets. It's a licensing name, yet it runs an outlet fleet. Counts only, because it's over 25.
- **Rip Curl:** 18 + 8, counts only.
- **EDIKTED:** 21 own doors.
- **O'Neill:** 3 + 17.
- **TWP:** 12.
- **Frances Valentine:** 7 (+2 concessions).

Part 2 totals: **54 yes, 200 no, 30 NC.**

## Rulings needed (consolidated)

1. **Pop-ups.** This has been open since batch 1. There are 8 pop-up rows; none are counted. Do you want a pop-up column?
2. **Appointment-only showrooms and ateliers.** Readers handled them differently:
   - Counted as own-door: Sachin & Babi (2), Mestiza New York, Adam Lippes' NYC salon, Lela Rose's NY atelier, LAPOINTE, Markarian, Reem Acra, GRACE LING, PatBO Flatiron.
   - Not counted: Naeem Khan, Shani, Rosie Assoulin's studio, Dress the Population.
   - One rule is needed: are by-appointment showrooms that sell direct to consumers doors?
3. **G by GUESS (54 doors)** is filed as outlet. GUESS's own Factory locator lists it, but most of these doors are in regular malls. Reclassify as own-door if you'd rather.
4. **Concessions now have real data:**
   - UGG at Macy's Herald Square
   - ba&sh × 15 at Bloomingdale's
   - Chloé at Saks
   - Zadig & Voltaire × 18 at Bloomingdale's
   - MARELLA × 9 at Bloomingdale's, including Chestnut Hill
   - Whistles × 3 at Bloomingdale's
   - Giambattista Valli at Bloomingdale's
   - Loulou de Saison at Bloomingdale's
   - Market (Dallas) as host for Cult Gaia
   - DÔEN at Alchemy Works
   - Decide whether the map shows concessions.
5. **Shared G-III doors.** DKNY and Karl Lagerfeld Paris list identical suites at Camarillo and Orlando International. These are probably one door each, listed by both brands.
6. **Hotel and resort boutiques** (Vilebrequin × 3, Lela Rose at Bowie House) are counted as own-door.
7. **Address conflicts between brands' own sites:**
   - 1015 Madison Ave is listed by both Camilla and A.L.C.
   - Palisades Village: A.L.C. lists its store open, TOTEME says temporarily closed.
   - 1515 Sheridan Rd, Wilmette is shared by DÔEN and Oscar de la Renta "Chicago". It's a centre address, so this is fine.
8. **Earlier open items:** Tadashi Shoji is NC (its site claims US boutiques but lists none). BCBG's Marquee Company Store is held.

## NC: needs another look (Part 2, 30 brands)

- **Most important:**
  - **Cynthia Rowley:** the site mentions "our boutiques", but its Where to Buy page is empty.
  - **Adrianna Papell:** the locator back end throws an error on every query.
- **Unreadable in Chrome** (certificate or access errors): Smythe, WEAR by Erin Andrews, Flora Nikrooz, Julia Jordan, Midnight Bakery.
- **No official site found, or domain parked or for sale:** Brandon Maxwell, Lyla Grant, SLVRLAKE, AFRM, CeCe, Hutch, Line & Dot, The Good Journey, A.REN, Central Park West, CISSA, Cordova (password page), Gallery, HARSHMAN, In Bloom by Jonquil, LAYERED WITH LOVE, Libertine, LIKELY, MOON RIVER, SECRET MISSION, Super Natural by Secret Mission, Siena, WAYF.
- Several of these look dormant. The worklist's source may hold the right domains.
- Chrome stopped responding at the very end, so I didn't run the final recheck of Cynthia Rowley.

## Zeros worth a second look

- **Spanx:** the help centre wouldn't render.
- **Hudson Jeans:** only the first 25 locator rows were read.
- **Fabiana Filippi:** the store API needs a token; I relied on a radius search.
- **Volcom:** the old locator now returns 404.
- **Silver Jeans Co.:** the finder returns 0 everywhere.
- **Roxy and Sweaty Betty:** no US locator.
- **Kenneth Cole:** the site's legal text still mentions company-owned stores, but it has no locator.
- **Steve Madden:** 7 dead locator entries.

## Worklist corrections

- **Licensing / no store, with the owner named on site:**
  - London Fog: © Iconix
  - Champion: ABG
  - Billabong: Boardriders IP
  - Donna Karan New York: G-III
  - SONIA RYKIEL: G-III
  - Jessica Howard: G-III
  - Kensie: BR Brand Holding
  - HALSTON: © G-III
- **Not womenswear:**
  - Jordan (Nike; one World of Flight door, Philadelphia)
  - Antigua (golf and fan apparel)
  - FANATICS (a retailer, with no locator)
  - Motette (mostly kidswear)
  - Peanuts (a licensing property)
- **Sub-lines or sister labels:**
  - Aidan Mattox is sold on adriannapapell.com.
  - Magicsuit® is sold on miraclesuit.com.
  - Donna Morgan is sold on maggylondon.com.
  - Sunshine 79 redirects to La Blanca.
  - Lauren Ralph Lauren is already on the men's map.
- **Closed or relaunching:**
  - NASTY GAL's site is a "coming soon" holding page.
  - One33 Social's site is a password page.
  - Warehouse is online-only in the UK.
- **Domains differ from the name.** Each brand's `site_domain` or note has the real one. Examples:
  - nicandzoe.com
  - lisa-yang.com
  - lalignenyc.com
  - twpclothing.com
  - danielleguiziony.com
  - locations.truereligion.com
- **Ambiguous worklist entries:** "Marion" was read as MARION Maternity; "BEACH HOUSE" was read as the Beach House swim line; "Gallery" and "Siena" could not be resolved.

## For WS properties

- **Seaport:** Beyond Yoga (70 Seaport Blvd).
- **Derby Street:** NIC+ZOE (94 Derby St).
- **The Street Chestnut Hill:** Splendid (43 Boylston St).
- **Chestnut Hill Bloomingdale's concessions** (225 Boylston, not WS): ba&sh and MARELLA.
- Search `return_doors.csv` for Hingham, Chestnut Hill, Dedham, Lynnfield and Boston for the full list.
