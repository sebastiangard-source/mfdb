# ws_centers_2026-10-22: every tenant at 18 WS Development centers

**Issued** 22 October 2026 · **Kind** read · **Three batches, returned as each is done** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job. If you cannot run a browser, say so and stop.

## Why

The Cyprus Brand Explorer will show which of its brands trade at WS Development's centers. Today that's worked out from the brands' own store addresses, which is good but not certain. Each center's **own directory** is the authority on who is there, and this pass reads it. Nothing here is matched to the Explorer; the Spectrum thread does that from your return.

## The worklist

`worklist.csv` lists 18 centers in three batches.
- **Batch 1:** the five Insider properties (Seaport, Derby Street Shops, The Street Chestnut Hill, MarketStreet Lynnfield, Legacy Place).
- **Batches 2–3:** thirteen more, from The Avenue Viera to The Shops at Farmington Valley.

`city_state_hint` is our best guess at each center's location; confirm it from the center's site. Station Twelve's location is unknown.

## Where to read

1. **Find each center's own website** from WS Development's property page: https://www.wsdevelopment.com/our-properties/. Record it in `center_site`.
2. **Open the center's directory** (often "Directory", "Shop", "Stores" or "Shop & Dine") and read the **whole** list. Use filters only to see everything: clear any category filter, and page through or load more until the count matches the total the site shows.
3. **Seaport** is a district with several directories (shops, dining, and others). Read all of its shopping and services listings, and say which pages you used.
4. **Don't use** mall-directory aggregators, Google Maps or brand store finders. The center's own site is the only source for this pass.

## What you return

**`return_tenants.csv`**, in the columns of `return_tenants_template.csv`, with one row per tenant per center:
- `tenant_name`: exactly as the directory spells it.
- `category_on_site`: the category the directory gives (for example "Women's Apparel" or "Dining"). Use `ND` if it gives none.
- `unit_or_address`: the suite, unit or street address, if the listing shows one. Otherwise `ND`.
- `status`: `open`, or `coming_soon` where the site says "coming soon", "opening" or similar. Return the temporary or pop-up tenants the directory lists, and note them.
- `tenant_url`: the link the directory gives to the tenant's page or the brand's site, if any. Otherwise `ND`.
- **Keep every tenant**, including restaurants, services, fitness, banks and offices. The merge filters them.
- **Don't merge or rename.** If the directory lists "J.Crew" and "J.Crew Men's" separately, return two rows.

**`return_centers.csv`**, in the columns of `return_centers_template.csv`, with one row per center: its site, the directory page, city and state, how many tenants are listed, how many are coming soon, and the read method.

**`NOTE.md`**, one per batch: the pages you read, any directory that seemed incomplete or out of date (for example a tenant listed that the site's own news says has closed), and anything doubtful.

## Rules

- **Bot walls:** one plain try. If a check box appears, ask Sebastian once whether he'll clear it himself. Any other wall makes that center `NC`, with the wall named.
- **Pace:** one page at a time, a few seconds apart.
- Read only what a person browsing would see. If a directory loads its list from the site's own data feed as the page renders, reading that same feed is fine; say so.
- **Cell values:**
  - `NC`: nobody looked.
  - `ND`: the page was read and states nothing.
  - No empty cells.
- Don't touch the map. Anything out of scope but noticed goes in `NOTE.md`.

## Order and time box

Return each batch as it is done. Allow fifteen minutes a center, and forty for Seaport. Past the box, return what you have and say so.
