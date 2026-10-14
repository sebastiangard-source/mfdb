# doors_womens_2_2026-10-12 — brand-owned US stores for the rest of the women's universe

**Issued** 12 October 2026 · **Kind** locations · **Two parts, batches of ten** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the second women's doors job. The first (`doors_womens_2026-10-10`)
read 36 chains and came back clean: 3,656 stores, counts matching rows. **Same returns, same columns, same
definitions, same rules**, so the rows merge into the same register without reconciliation. It is a
Chrome job: store locators are JavaScript. If you cannot run a browser, say so and stop.

## Why

The women's universe is 523 brands, built from the women's clothing brand lists of nine department
stores. Thirty-six have had their own locators read; forty-nine more sit on the men's map and come with
it. That leaves **407 brands with no store count at all** — not zero, unknown. Most will own no US
store. Some own fleets (Michael Kors, Kate Spade, Steve Madden, Lucky Brand, UGG). Nobody knows which,
and the locations database cannot carry a women's map until somebody looks.

## One worklist, two parts

`worklist.csv` — 407 brands, `part` 1 or 2, with how many of the nine department stores carry each
(`dept_stores_carrying`, a measure of wholesale reach, not of stores). `site_domain` is `NC`
throughout: establish the brand's own US site first and record it. DÔEN and Nour Hammour carry `0` department
stores: they were added from Net-a-Porter's featured list, not the department-store index.

**Part 1 — 125 brands, full read.** Brands that, by name, are likely to own US stores. For every one:
the brand's own US store locator in Chrome, every US location, **one row per door** in `return_doors.csv`
(`format` = own-door, outlet, concession or pop-up; `operator` where a partner runs the door), and one
row per brand in `return_counts.csv`. Exactly the first job.

**Part 2 — 282 brands, screen.** One row per brand in `return_screen.csv`
(`return_screen_template.csv`): does the brand's own US site publish any store of its own? `has_us_own_store`
= yes / no / NC. **Where yes and the count is 25 or under, return the rows too**, in `return_doors.csv`,
same as Part 1 — you are on the locator already. Where yes and more than 25, return the count and
leave the rows for a follow-up. Where no, say in `note` what you checked (footer, sitemap, a /stores
or /locations path, the contact page). Five minutes a brand; the point is to find the handful that own
stores, not to prove the rest don't.

A Part 2 brand that turns out to have a fleet is a finding; say so in `NOTE.md`. A Part 1 brand with
no store is normal; `0` with the basis.

## Rules

- **The brand's own locator is the only source for a door.** Not Google Maps, not Yelp, not a mall
  directory, not press. If the locator cannot be read even in Chrome, `NC` with the exact block in
  `note`. `NC` means nobody could look; `0` means the brand's own site shows no store; an empty cell is
  an error.
- **Own door means the brand's name on the door at full price.** A shop-in-shop at Nordstrom or
  Bloomingdale's is a concession. A store in an outlet center is an outlet whatever the locator calls
  it. "Coming soon" is `status` = opening, with the date. Operator- or licensee-run doors under the
  banner count, flagged in `operator`. Department-store counters are not doors.
- **Women's-only stores count** (ruled 11 Oct). A brand that also sells men's is still a women's-universe
  brand here; count every door under its name.
- **Sister banners and sub-lines.** MICHAEL Michael Kors and Michael Kors Collection are Michael Kors;
  Lauren and Collection are Ralph Lauren (already on the men's map, skip); DKNY and Donna Karan are
  separate; BCBG and BCBGMAXAZRIA are one; Weekend and Studio are Max Mara (done, skip). Where a locator
  is shared across banners, filter by banner and say how.
- **Licensed names.** Several on the list are licensing brands with no store of their own (Jones New
  York, Anne Klein, London Fog, Halston, Herve Leger, BCBG under Marquee, Hurley). `0` with the basis,
  and name the licensor in `note` if the site says.
- **Footwear and underwear houses** on the list (Steve Madden, Sam Edelman, UGG, Hunter, Wacoal, Natori,
  Hanky Panky, Commando, Spanx, Skims) are in scope: a store is a store.
- Names must match `canonical_keys.txt` (the worklist spelling, department-store capitals and ® marks
  included); run `python3 reconcile.py` before returning. Where the brand's own mark differs, say so in
  `note`.
- Street addresses as the locator writes them, ZIP five digits, state two letters. NYC rows with the ZIP
  so the neighbourhood can be derived. Puerto Rico counts as US; Guam and other territories listed but
  flagged.
- Locators that cap at 50 or 100 results silently: compare the count shown with the rows returned.
- Do not touch the map. Return the files and `NOTE.md` per batch: what was read, what could not be, and
  anything the worklist got wrong (a brand that is really a line of another, a brand that is menswear,
  a brand that has closed).

## Order and time box

Part 1 in worklist order, batches of ten, each batch returned as it is done. Then Part 2, batches of
twenty. Fifteen minutes a brand for a Shopify locator, forty for a paged chain (Michael Kors, Steve
Madden, Lucky Brand, UGG, GUESS, Under Armour, Champion will be large and outlet-heavy; separate
the outlets). Five minutes a Part 2 brand. Past the box, what you have, `NC` on the rest, said so.
