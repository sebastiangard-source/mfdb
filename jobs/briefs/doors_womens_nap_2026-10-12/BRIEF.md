# doors_womens_nap_2026-10-12 — brand-owned US stores for 161 Net-a-Porter brands

**Issued** 12 October 2026 · **Kind** locations · **Two parts, batches of ten** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the third women's doors job and runs in parallel with
`doors_womens_2_2026-10-12`, which covers a different list. **Same returns, same columns, same
definitions, same rules** as the first job (`doors_womens_2026-10-10`, 36 chains, 3,656 stores,
counts matching rows), so everything merges into one register. It is a Chrome job: store locators are
JavaScript. If you cannot run a browser, say so and stop.

## Why

The women's universe was built from nine department stores' brand lists. Net-a-Porter is a different
filter: it carries the runway, resort and designer-shoe end that Nordstrom, Bloomingdale's and Saks
don't. On 12 October its US designer index (469 names) was checked against every register: 139 are
jewelry, eyewear, watches, home, beauty or vintage and out of scope; 169 clothing, shoe and bag brands
are already on a register; **161 are on none**. Nobody knows which of the 161 own a US store. This job
finds out.

## One worklist, two parts

`worklist.csv` — 161 brands, `part` 1 or 2, `kind` clothing or shoes. `site_domain` is `NC`
throughout: establish the brand's own US site first and record it.

**Part 1 — 73 brands, full read.** Brands that, by name, are likely to own a US store: The Frankie
Shop, Tibi, Sporty & Rich, Wardrobe.NYC, Willy Chavarria, Rodarte, Magda Butrym, Elie Saab, Joseph,
Sportmax, and the shoe houses (Manolo Blahnik, Aquazzura, Gianvito Rossi, Roger Vivier, Amina Muaddi,
Loeffler Randall, Sorel, Autry, Moon Boot…). For every one: the brand's own US store locator in
Chrome, every US location, **one row per door** in `return_doors.csv` (`format` = own-door, outlet,
concession or pop-up; `operator` where a partner runs the door), and one row per brand in
`return_counts.csv`.

**Part 2 — 88 brands, screen.** One row per brand in `return_screen.csv` (`return_screen_template.csv`):
does the brand's own US site publish any store of its own? `has_us_own_store` = yes / no / NC. **Where
yes and the count is 25 or under, return the rows too** in `return_doors.csv`. Where no, say in `note`
what you checked (footer, sitemap, a /stores or /locations path, the contact page). Five minutes a
brand. Most of these are swim, resort and newly launched labels with no store anywhere; the point is
to find the few that have one.

## Rules

- **The brand's own locator is the only source for a door.** Not Google Maps, not Yelp, not a mall
  directory, not press, not Net-a-Porter. If the locator cannot be read even in Chrome, `NC` with the
  exact block in `note`. `NC` means nobody could look; `0` means the brand's own site shows no store;
  an empty cell is an error.
- **Own door means the brand's name on the door at full price.** A shop-in-shop at Saks, Neiman Marcus
  or Bergdorf is a concession — several of the shoe houses have them, listed as if they were stores.
  A store in an outlet center is an outlet. "Coming soon" is `status` = opening, with the date.
  Operator- or licensee-run doors under the banner count, flagged. Department-store counters are not
  doors.
- **Women's-only stores count.** A brand that also sells men's is still counted here under its name.
- **Non-US houses.** Many of these are London, Paris, Milan, Sydney or Copenhagen labels whose
  locators cover the world. Scope to the US; put the world count in `note` if the locator gives it.
  A US flagship run by a distributor counts, flagged.
- **Sub-lines and sister names.** adidas by Stella McCartney is a line sold in adidas and Stella
  McCartney stores: `0` own doors, say so. Calvin Klein Collection is sold in Calvin Klein stores,
  which are on the men's map: `0`, say so. Nike SKIMS, Marant Étoile and the Comme des Garçons lines
  are not on this list for the same reason.
- Names must match `canonical_keys.txt` (the Net-a-Porter spelling, capitals included); run
  `python3 reconcile.py` before returning. Where the brand's own mark differs, say so in `note`.
- Street addresses as the locator writes them, ZIP five digits, state two letters. NYC rows with the
  ZIP so the neighbourhood can be derived. Puerto Rico counts as US; territories listed but flagged.
- Do not touch the map. Return the files and `NOTE.md` per batch: what was read, what could not be,
  and anything the worklist got wrong (a brand that is really a line of another, a menswear brand, a
  brand that has closed, a brand that is jewelry after all).

## Order and time box

Part 1 in worklist order, batches of ten, each returned as it is done. Then Part 2, batches of twenty.
Fifteen minutes a Part 1 brand, five minutes a Part 2 brand. Past the box, what you have, `NC` on the
rest, said so.
