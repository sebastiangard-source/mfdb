# sift_candidates_2026-10-08 — ninety brands the map may be missing: the sift

**Issued** 8 October 2026 · **Kind** sift · **Tier A returned first, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is the Stage 1 sift from `seat_boyds_2026-10-07`, run on a list
chosen by asking what a knowledgeable reader would look for on the map and not find. `worklist.csv`
holds 90 brands with the gap each fills and a one-line reason; `tier` A is the 36 a reader would
notice first, B the 54 that fill a thin register. **You gather and you propose; Sebastian rules.**

## The job

One row per brand in `sift_template.csv`, from the brand's own site, fifteen minutes at most:

- `site_domain`; `us_store` yes/no/none; `mens_clothing_or_footwear` yes/no
- `us_own_stores`: how many stores of its own the brand runs in the US, counted from its locator
  (`0` is a finding; `NC` only if there is no locator and no store page); `us_own_stores_source` URL.
  Outlets and concessions are not own stores; say in `note` if the locator mixes them.
- `what_it_sells` in plain words under twelve
- `price_tee_or_entry` and `price_outerwear_or_top`: one entry price and one top-of-range price, full
  price, currency stated (`rules_prices.md`); `np` if none published
- `band_guess`: premium ($80–300 basics) / accessible ($150–800) / trueLux ($800+) by the price pair
- `sift_verdict`: **seat** (men's clothing or footwear house, readable US site, at least a few US stores
  of its own), **bench** (real but something blocks it: no US own stores, a license, a sub-line, a range
  below the map's floor), **reject** (not a clothing or footwear house)
- `reason`, one checkable sentence; `source` URL

## Things the list already knows, so you do not have to decide them

- The **floor** is not ruled. Uniqlo, Abercrombie & Fitch, Tommy Hilfiger, Calvin Klein, UNTUCKit:
  return the prices and the door count and write `bench — floor ruling` as the verdict. Sebastian rules.
- **Shoe-only houses** (Alden, Allen Edmonds, Johnston & Murphy, Birkenstock, Dr. Martens and the
  rest): `mens_clothing_or_footwear` yes; verdict by the door count like anyone else.
- **Sportswear giants** (Nike, adidas, New Balance, Converse, Vans, Asics, Hoka, On): same — count the
  doors, guess the band, verdict `seat` if the bar is met; the class ruling is Sebastian's.
- **Carhartt WIP** is a license with its own stores; verdict `bench — license ruling`.
- **Emporio Armani, Veilance**: sub-lines of seated houses with their own stores; verdict
  `bench — sub-line ruling`, with the door count.
- **Gant**: the bench already says it is the Ivy canon member that matters; the question is only its
  US own-store count today.

## Rules

- Names must match `canonical_keys.txt` exactly; run `python3 reconcile.py` before returning. Where the
  brand's own mark differs (accents, capitals, "G.H. Bass" vs "Bass"), say so in `note`.
- `NC` nobody looked; an empty cell is an error.
- The brand's own site only. No press, no Wikipedia, no retailer.
- Do not touch the map. Return `sift.csv` and `NOTE_sift.md`. Nothing else.
- Out of scope but noticed — a brand you think belongs on this list and is not — goes in `NOTE_sift.md`
  with a line of reason.

## Order and time box

Tier A first, returned as soon as the 36 are done, then Tier B. Fifteen minutes a brand; past that,
what you have, said so.
