# seat_resort_2026-10-07 — everything needed to seat Frescobol Carioca and Orlebar Brown

**Issued** 7 October 2026 · **Kind** seating evidence · **Two brands, no pilot** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This brief gathers, in one pass, every fact the map holds for a seated
brand, for two brands that are not on it yet. The rules are not new: each section points at the
standing rules file in this folder, and those files win over any shorthand here. **You gather and you
propose; Sebastian rules.** Nothing you return seats a brand or sets a score until he says so.

The two brands are resort houses whose range may be mostly swim. The map scores clothing, so the swim
question has to be answered before the dials can be: how much of each men's range is swimwear, and
what is left when it is excluded. Count it; do not guess it.

## What you return

Four files and a note, nothing else:

1. `return.csv` — one row per brand, the 132 columns in `return_template.csv`, every cell filled.
2. `own_doors.csv` — one row per brand-owned store, worldwide, US rows first (`own_doors_template.csv`).
3. `stockists.csv` — one row per third-party stockist the brand itself lists (`stockists_template.csv`).
4. `return_styles.csv` — one row per men's style read for the fibre count (`schema_styles.json`).
5. `NOTE.md` — what was read, what could not be reached, what the brief got wrong, and anything out of
   scope worth keeping.

Names must match `canonical_keys.txt` exactly (`Frescobol Carioca`, `Orlebar Brown`). Run
`python3 reconcile.py` before returning. `NC` nobody looked; `NONE` the brand sells or does no such
thing; `np` checked, no price published. An empty cell is an error.

## Sections of the row, and the rules file for each

**1. Store, currency, search** (`rules_prices.md`, "Store and currency"). The US storefront where one
exists (`orlebarbrown.com` and `frescobolcarioca.com` both ship to the US; find the US market path and
record it in `store_used`). Currency confirmed by two displayed page prices, not the feed.
`search_url` is the brand's own site search with the query empty, tested to return results for a
garment word the brand uses; `NONE` for overlay-only search.

**2. Eight garments, prices and links** (`rules_prices.md` for low/high/basis/elevated/full-price;
`rules_garment_links.md` for the men's listing URL). Tee, polo, dress shirt, jeans, dress pants,
sweater, outerwear, shoes. Seven price cells plus one listing link per garment. Every figure carries
the product name and the product URL it was read from. Linen shirts count as the dress shirt only if
the brand makes no woven collared shirt otherwise, said so in `note`. Trousers in linen or cotton drill
are the dress-pants cell with `note` saying chinos. Shoes are own-label only; espadrilles and sandals
under the brand's name count as `range`, never as a loafer pair. Swim shorts are not a garment on the
card: do not put them in any cell; they go in section 3.

**3. Fibre and swim** (`rules_fibre.md`, read end to end). Count men's styles, main fibre from the first
composition listed, spandex count, one cloth story or two. Then three cells this pass adds:
`swim_styles` (men's swim styles counted), `swim_share_of_range` (swim styles over styles_total, as a
percentage), `mens_styles_excl_swim`. Swim is in the denominator and out of the split verdict, as the
playbook says. Both houses sell a lot of polyester and polyamide swim; if the natural share of the
range looks high, check that swim was actually counted.

**4. Own doors** (`own_doors.csv`). Every store the brand itself operates, from the brand's locator, one
row each, worldwide. US rows first. `format` is `own-door`, `concession`, `outlet` or `pop-up`; a shop
inside a department store or hotel is a concession, not an own door, and the two are counted
separately on the map. `own_doors_us` and `own_doors_world` in the brand row count own-doors only.
`doors_basis` says what you counted from (locator URL, date). Orlebar Brown's locator mixes own stores
and stockists; read the labels.

**5. Stockists** (`stockists.csv`). Only what the brand itself lists; a retailer saying it stocks the
brand is not evidence here. `locator_kind` says where the list came from. Department stores are rows
with `shop_kind` department store; they are kept separately from independents.

**6. Tech** (`data/rubric.json` text is reproduced below). `tech_named_fabrics`: the fabric names the
brand gives its technical cloth (quick-dry, UPF, four-way stretch, recycled polyamide), semicolon
separated, with `tech_evidence_url`. `tech_owned_or_licensed`: `owned` if the brand says it developed
the material, `licensed` if a named supplier's (Econyl, Repreve, Sorona), `commodity` if unnamed
performance cloth, `none`. `tech_share_of_range`: share of men's styles (swim included) whose product
page makes a performance claim, as a percentage. `proposed_tech` 1–5 with the reason in `note`.

> Tech: how technical the clothes are. Depth of technical product drives the scale; who owns the
> technology decides only whether a house can reach the top. 5 is reserved for a house that developed
> what it sells. 4 is a range as technical, bought in. 3 is a real but partial technical business.
> 1 is a trace.

**7. Craft** (`rules_craft.md`, `rubric_craft.txt`). The six facts, two URLs, `proposed_craft` and two
or three sentences of `craft_reasoning` a reader could check on the brand's own site. Frescobol Carioca
makes a point of where it makes things; test the claim the way the craft audit did, not by repeating it.

**8. Origin and ownership.** `founded_year`, `founded_place`, `founders` as the brand states them, with
the URL. `owner_today`: the parent or holding company if any (Orlebar Brown has had a corporate owner
since 2018; name it from a filing or the owner's own site, not from press memory), `independent` if
none, with `ownership_url`.

**9. Lookbook** (same columns as `registers/lookbooks_fall2026`). Is there a current-season men's
lookbook or campaign page on the brand's site: `yes`/`no`/`not verified`, the season label as the brand
writes it, whether it is men's, the URL.

**10. Resale.** `vinted_mens_url`: Vinted men's catalog filtered to the brand's brand id(s), ids listed in
`vinted_brand_ids`, as `registers/vinted_mens_search` does (catalog 5 is men's). `grailed_url`: the
brand's designer page on Grailed, or `NONE`.

**11. Certifications.** B Corp directory and the GOTS public database, nothing else. `yes`/`no`, and
the certified entity name where yes.

**12. In their words** (`rules_quotes.md`). One real quotation, verbatim, six to thirty words, founder or
house, with who said it, where, the URL and the date. `NONE` with a note if nothing is worth quoting.

**13. Signature product.** The one product the brand is known for, its own name for it, and its URL
(Orlebar Brown's is obvious; find what Frescobol Carioca itself puts first). `pronunciation`: how the
brand says its own name, if it says anywhere; otherwise `NC`.

## Rules that apply to the whole row

- Full price only; sale and outlet prices are not prices.
- The brand's own statements first, then press that quotes them, then filings. A retailer's
  description is not evidence.
- Where a locator or listing caps or paginates, read the count before capturing (`rules_fibre.md`,
  paginated feeds).
- Do not touch the map. Do not rebuild anything. Do not send working files.
- Out of scope but noticed: record it in `NOTE.md`, do not discard it.

## Order and time box

Do both brands in parallel if you can. Within a brand: store and currency, then fibre (it decides the
swim question everything else hangs on), then prices and links, then doors and stockists, then the rest.

Forty minutes a brand for sections 1–5; thirty for 6–13. Past that, what you have, `NC` on the rest,
and say so in `NOTE.md`.
