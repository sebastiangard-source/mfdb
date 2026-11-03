# stockists_national_2026-11-03: every US stockist for the 56 brands with no Northeast shop

**Issued** 3 November 2026 · **Kind** locations · **Returns in batches, no stop between them** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. Everything below assumes it. **You gather and propose; Sebastian rules.**

## Why

56 brands on the map are sold through independent shops but have no stockist and no store of their own in the Northeast. The September pass read stockist pages for the Northeast only. The 8 October waves read more widely, but they missed shops that write the country as "United States" instead of "USA", and several reads stopped short. This pass reads each brand's own stockist page again. It returns **every US shop the brand names, in any state**, and flags the Northeast ones.

`worklist.csv` has the 56 brands plus one row (Flint and Tinder) already ruled out and marked `skip`. Its `status` column says what each brand needs:

| status | brands | what to do |
|---|---|---|
| `read` | 24 | **Never read, or not read last time** (client-side widget, broken page, or out of time). Do a full read. |
| `verify` | 8 | **Rows are on file in `on_file.csv`.** Check them against the locator today. Add the shops that are missing, mark the ones that are gone, and don't re-key the rest. |
| `reread` | 4 | **Rows on file are thin** (state or city only, or names only). Read again and return full rows. |
| `verify_count` | 1 | **Ariat.** 2,129 rows are on file. Don't re-key them. Check that the locator still works, and give a count for each of the ten Northeast states in `NOTE.md`. |
| `second_look` | 19 | **On file as publishing no stockist list,** or listing only its own stores. Take one more look, as set out below. |

Do the `read`, `verify` and `reread` brands first and return them as batch 1. Then do the `second_look` brands and Ariat as batch 2.

## What to return

Return one row per brand per shop in `return_template.csv`.

**Columns:**

- `country_as_written`: the country exactly as the page writes it ("USA", "United States", "US", "U.S.A."). This is how the last pass lost rows. **Check every US spelling, and any locator entry that names a US state or a US ZIP code with no country.**
- `shop_kind`:
  - `independent` is what we want.
  - Also return `department` rows (Nordstrom, Saks, Neiman Marcus, Bloomingdale's), `chain` rows (outdoor, golf or ski chains such as REI, Golf Galaxy or Christy Sports), `pro shop` rows (golf or ski clubs), and `brand-owned` rows (the brand's own or a sister brand's store), each marked. They show what the locator counts. Whether they go on the map is ruled on merge.
- `lines`: men's, women's or both, if the page says so. Otherwise `NC`.
- `northeast`: `yes` for Massachusetts, Rhode Island, Connecticut, New Hampshire, Vermont, Maine, New York, New Jersey, Pennsylvania or Delaware. Otherwise `no`.
- `new_to_register`: `no` if the shop name and town match a row in `register_shops.csv`, or `yes` if not. Spelling may differ slightly; use your judgment and say so.
- `on_file`: `yes` if the row was already in `on_file.csv`, `added` if it is new this pass, or `gone` if it is in `on_file.csv` but no longer on the locator.
- Street, city, state and ZIP as the locator gives them. For a shop with no street on the locator, fill in the town and put `street not on locator` in `note`. Don't look up streets elsewhere in this pass.

**Brands with no shops to return:**

- **A brand with a locator but no US shops:** one row with the locator URL and `shop_name = NONE`.
- **A brand that publishes no locator:** one row with `locator_url = NONE`, and say in `note` every place you looked.

## The second look

For each `second_look` brand, try these in order, five minutes each, then stop:

1. The footer and the sitemap (`/sitemap.xml`, `/pages/sitemap`): look for stockists, retailers, where to buy, find a store, or wholesale.
2. **The brand's other sites.** A UK, EU or Japanese home site often has a stockist page that the US site doesn't. Edward Green's North America list is one example.
3. The brand's Instagram highlights and bio links, for a "stockists" highlight or a stockist page. Read only.
4. The brand's own press or about page, for named US shops. If you find shops this way, mark them `source_kind: about page` in `note`. They can count, but they rank below a locator.

A shop named only by a retailer's own site, a press piece or a third-party directory is not a source for this pass. It belongs in `NOTE.md` under the brand as a lead, not in `return.csv`.

## Notes on particular brands

- **Golf brands** (Bad Birdie, Eastside Golf, Holderness & Bourne, Kjus): club pro shops make up most of their locators. Return them marked `pro shop`. The register leaves them out today, but return them anyway.
- **Western and outdoor brands** (Ariat, Lucchese, Danner, Roark): these mostly sell through farm, tack and outdoor chains. Mark each shop with its kind; don't filter.
- **Needles:** Nepenthes New York is the parent company's shop. Mark it `brand-owned` and return any other US shops.
- **Japanese brands** (Kapital, Hender Scheme, Human Made, Needles, Sacai): the Japanese site often lists overseas dealers on a page the US site doesn't link. Look there first.
- **Map widgets** (Danner, Quoddy, Stan Ray, Dickies): if the widget loads client-side, try its data endpoint, which shows in the page's network calls (read only). Otherwise search each state's largest cities.

## Rules

- **The source is the brand's own locator or stockist page.** Not a retailer's site, and not a third-party directory.
- **Names.** Brand names match `canonical_keys.txt` exactly. Write shop names in the shop's own case ("Dover Street Market", not "DOVER STREET MARKET").
- **No empty cells.** `NC` means nobody looked. An empty cell is an error.
- **Bot walls.** Try once, plainly. If a check box appears, ask Sebastian once whether he'll clear it himself.
- **Read only.** Don't sign in, add anything to a cart, sign up, follow or message anyone.
- **Don't touch the map.** Don't rebuild anything. Return `return.csv` and `NOTE.md` per batch, nothing else. `NOTE.md` holds a short section per brand: what you read, the count of US and Northeast shops, and any leads.

## Time box

- Ten minutes per brand for a list page, twenty for a map or ZIP search.
- `verify` brands: ten minutes.
- Second looks: twenty minutes in all per brand.
- Past the limit, return a row with what you have and a note.
