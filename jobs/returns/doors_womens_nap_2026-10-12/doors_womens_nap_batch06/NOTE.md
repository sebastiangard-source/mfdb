# doors_womens_nap_2026-10-12 — Part 1, batch 6

**Worklist rows 51–60. Read 13 Oct 2026 in Chrome. `reconcile.py`: 10 exact, 0 to rewrite, 0 unmatched. No empty cells in any of the three files.**

## Result

Three brands have US doors, 10 rows in all:

| Brand | US own doors | US concessions | Source |
|---|---|---|---|
| We Norwegians | 2: Park City UT; Aspen CO | 0 | wenorwegians.us/pages/contact |
| Aquazzura | 2: 939 Madison Ave, New York; Bal Harbour FL | 0 | aquazzura.com/us_en/storelocator |
| Gianvito Rossi | 5: South Coast Plaza, NorthPark, Crystal Shops, Bal Harbour, Madison Ave | 1: Bloomingdale's NYC | gianvitorossi.com/us_en/boutiques/ |

The other seven brands come back 0. No US outlets.

| Brand | Own doors on the brand's site | US stockists recorded |
|---|---|---|
| WARDROBE.NYC | none | none published |
| Willy Chavarria | 1 concession, Galeries Lafayette Paris | none published |
| Aeyde | none | 21 |
| Amina Muaddi | 6–8, Paris, London, Milan, Gulf | 60 (incl. 1 Puerto Rico) |
| Ancient Greek Sandals | 2, Athens | 66 |
| Autry | 6, Europe and a Tokyo pop-up | none published |
| Emme Parsons | none | 21 (12 store, 9 online) |

## Where the brief would give a confident wrong answer

1. **Gianvito Rossi's Bloomingdale's is a concession, not a door.** It is listed among "Our Boutiques" with its own Gianvito Rossi shop email, so it is counted as a concession and kept out of `us_own_stores`. Take the boutique list at face value and you get 6 doors, not 5.
2. **Aquazzura New York shows "Seasonally Closed".** It is counted as open and flagged, because the brand still lists it as a flagship. Check by hand if a closed store should come out of the count.
3. **Autry has no US store, despite its domain.** The site is autry-usa.com, but the locator and its country list are Europe and Asia only.
4. **We Norwegians runs a separate US site.** The global site lists only Voss and Park City. The Aspen store and the US stockist list exist only on wenorwegians.us.
5. **Ancient Greek Sandals' USA tab is not all US.** It holds 116 entries, but many stores repeat under two or three city/state headings. Barbados, Bahamas, Greece, Canada and 16 non-US online shops are also in it. After those are removed, 66 unique US rows remain.

## Stockist quality: points for the main thread

- **We Norwegians** and **Amina Muaddi**: full addresses from their stockist.co feeds.
  - Amina Muaddi's feed drops leading zeros from New England and New Jersey ZIPs. They were restored and flagged.
  - Its Puerto Rico ZIP ("1400") is not valid, so it is `NC`.
  - It misspells Coral Gables and McLean.
- **We Norwegians**: "The Nordic Shop, Rochester NY" carries a Minnesota ZIP. It is kept as written and flagged.
- **Aeyde**: gives the city and country, so the state is filled in from the city. One Clairvaux row gives "Kansas" only, so its city is `NC`.
- **Ancient Greek Sandals**: addresses are free text, split by hand. One row names Mauna Lani but gives a Ritz-Carlton Maui address.
- **Emme Parsons**: names and cities only.

## Wrong or unreachable sites

None. All ten worklist rows had `site_domain` `NC`, and each brand's site was on the domain you would guess. Autry's site ran an automatic browser check that passed on its own; nothing was clicked.

## Files

- `return_counts.csv`: 10 rows
- `return_doors.csv`: 10 rows (9 own doors, 1 concession)
- `return_stockists.csv`: 203 rows
