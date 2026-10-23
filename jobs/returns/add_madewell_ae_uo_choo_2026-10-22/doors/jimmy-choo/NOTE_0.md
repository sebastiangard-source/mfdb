# NOTE_0 — Jimmy Choo stores (Part 0)

Captured 22 Oct 2026 from us.jimmychoo.com/en/store-locator. Name matches `canonical_keys.txt`.

**Result.** 31 rows, all US, all `open`: 18 `own-door` (incl. The Mall of San Juan, PR) and 13 `outlet`. One search, country United States, 35 results; city searches (New York, Miami) returned only subsets of the same 35, so I take 35 as the full US list.

**Not rows**
- **Counter:** "Jimmy Choo at Bloomingdale's", Chestnut Hill MA (225 Boylston St), locator type Department. A shop inside a department store, so counted in `us_concessions`=1. This is the one Jimmy Choo presence at a WS property (Chestnut Hill); no Jimmy Choo at Legacy Place, Derby Street, Lynnfield or Seaport.
- **Held for your ruling (`held_not_returned.csv`, 3 rows):** The Forum Shops at Caesars, The Shoppes at the Palazzo (both Las Vegas) and Jimmy Choo Americana Manhasset. The locator types them Department, but each address is a mall or shopping centre, not a department store. If you count them as boutiques, own-door becomes 21 and rows 34.

**Abroad is `NC`.** This locator belongs to the US region. Canada, Mexico and France return "no stores", and the UK returns one counter (Harvey Nichols, Edinburgh). The country list has 49 entries, but their boutiques sit on the other regional sites, which I could not reach (the site sends me to the US one). Switching region with the site's footer selector is possible; I did not do it without asking.

**Judgement calls.** Types are the locator's. Two outlets (Camarillo, Houston Outlet) and two own-door stores (Somerset Collection, Miami Design District) have no type on the locator; outlet there rests on "Outlet" in the name, own-door on the name having no outlet or department wording. `venue` is the named centre from the locator, else `street`. Several city fields differ from the address line (Palm Beach Gardens, Houston/Cypress, Seattle/Tulalip, Livermore under "San Francisco", Orlando for Vineland); returned as the locator gives them with a note. Troy MI, Las Vegas North and Vineland have no state on the locator: `ND`.

**Pace.** I read the 35 results from one page and ran six extra searches (Canada, UK, Mexico, France, New York, Miami); no wall, no deviation.

Not touched: the map, any account, any form.
