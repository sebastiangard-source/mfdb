# Wave C seating job — handoff, 13 October 2026 (after batch 6)

This continues `HANDOFF_2026-10-12_from_batch4.md`; read that first for the job, tokens and the earlier rulings. Everything referenced sits under `wave_c/`.

## Done and delivered this session
- **Batch 5** (rows 41–50: Lady White Co., Lands' End, Lardini, Ledbury, Mango, Meermin, Mollusk, Muji, Nautica, Needles): `wave_c/out/batch5/`. NOTE.md has 15 items for ruling.
- **Batch 6** (rows 51–60: Nigel Cabourn, Nudie Jeans, Oliver Spencer, Onward Reserve, Outdoor Voices, Oxxford, Pact, Perfect Moment, Pilgrim Surf + Supply, Pini Parma): `wave_c/out/batch6/`. NOTE.md has 11 items for ruling.
- **Not live re-checked:** batch 6 picks were not re-read live. The Chrome extension stopped responding at the end of the batch.

## Next: batch 7 (rows 61–70), then 8 (71–80), then 9 (81, Études only)
**Batch 7:** Private White V.C., Puma, Quoddy, Rancourt & Co., Represent, RVCA, Samuelsohn, Spier & Mackay, Stan Ray, Studio Nicholson.
- **Puma** is a large house: a stratified sample is allowed. Count the full men's catalogue.
- **Quoddy and Rancourt** are shoe houses. Check for clothing, and use NO_STYLES if there is none.
  - Rancourt's doors were counted on 10 Oct as 0. The Lewiston factory address is for ruling, not a door.
- **Non-US houses** (Private White, Represent, Samuelsohn, Spier & Mackay, Studio Nicholson): read the US storefront if one exists. Otherwise use the own currency, with no conversion.

**Batch 8:** Tellason, Ten Thousand, UGG, Undefeated, Undercover, Universal Works, Velva Sheen, Y-3, Zadig & Voltaire, Zara.
- **UGG and Zara** are large houses.
  - Do not re-read their locators. Carry the counts: UGG 10 + 36 outlets + 1 concession; Zara 102.
- **Universal Works:** 3 UK + 3 operator-run, 0 US. Carry from the counts job.
- **Y-3:** do not retry adidas.com. NC with the block named.
- **Zadig & Voltaire:** the NYC "Archive" stores are outlets. Mark as the house writes it: Zadig&Voltaire.
- **Undefeated:** multi-brand shop under its own name, so own door.

**Batch 9:** Études (mark "Études", not "Études Studio").

## Pipeline (batch 6 is the template)
- **Raw captures:** `wave_c/raw/batch6_inputs/*_styles.txt`, `~`-separated.
- **`code/build_b6.py`:**
  - Generic `cat_generic` categoriser.
  - `prep()` cuts Japanese main lines (`jp_main`), strips "Shell:"/lining parts and "Super 1xx's", and maps Alcantara to polyester.
  - It reads `BATCH` from the environment, so copy it to `build_b7.py`, swap the brand loaders, and run with BATCH=7.
- **`code/meta_b6.py`:**
  - One dict per brand, using the helpers in `meta_b5` (G, NONE_, NCG, NP, NOLOOK, NC_STYLES, NO_STYLES).
  - Placeholders take the form `TECH_XX`, `TECHSHARE_XX`, `MADEIN_XX`, `VIN_XX`, `VINID_XX` and `GRAILED_XX`, where XX is any two letters.
  - `TECH` and `LOGO` dicts sit at the end.
- **`code/assemble_b6.py`:**
  - Generic: imports `meta_b{BATCH}` and `build_b{BATCH}`.
  - Rounds prices to whole units, with exact figures in `note`.
  - Fills the placeholders from `vinted_grailed_b5to9.json`. That file already holds ids for every batch 5–9 brand.
- **`code/doors_stock_b6.py`:** door and stockist rows. Use `PH()` for a placeholder row when no door can be addressed.
- **Final checks:**
  - Run `reconcile.py` on all four files.
  - Check the style table against `schema_styles.json`.
  - Zip `out/batchN` and deliver.

## Method notes and traps (batches 5–6)
- **Browser output:** a returned string containing `?`, `&` or `=` is blocked. Write it into `<pre id=o>` and read it with get_page_text. Calls over about 45 s time out, so run long jobs async, save to sessionStorage, and poll. Re-inject helpers after every navigation.
- **Pages that include other products' data:**
  - Nudie: take the first `pr_composition` after the product's own `"uri"`.
  - Pini Parma: use the `Composition:` line.
  - A generic % regex grabs a recommended product's fibres.
- **Prices:**
  - Japanese stores show tax-inclusive prices. Outer Limits' feed is ex-tax (×1.1), while Nepenthes' feed matched the page.
  - Centra (Nudie) and Magento-like (Perfect Moment) stores need page data or the PDP price.
  - Pact's API gives MSRP and sale prices; file the MSRP.
- **Gender filters:**
  - Outdoor Voices: `m-`/`u-` handles and mens/unisex tags.
  - Pilgrim: the `/collections/mens` membership.
  - Onward Reserve: licensed team lines are about 80% of its feed and are excluded.
- **Store locators that render client-side:** Nudie (page data has the 38 storefronts), Perfect Moment (nothing), Pini Parma (names only), Onward Reserve's Stockist app. Lands' End has an XML feed at `/pp/StoreLocator?lat=&lng=&radius=`.
- **Rounding:** batches 5 and 6 round to whole units per `rules_prices.md`; batches 1–4 kept cents. This is raised for ruling.
