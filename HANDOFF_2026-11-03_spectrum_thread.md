# Handoff: the Spectrum thread, 3 November 2026

This is for the next Spectrum thread, written by the outgoing one when it closed. Everything listed is in the repo. This page says where each thing is and what is still in progress. It replaces `HANDOFF_2026-10-15_spectrum_thread.md`; read that one only for history.

## What this thread is

The Spectrum thread merges and builds the **Menswear Spectrum** (the men's map) and the **Cyprus Brand Explorer** (the women's and brand-set page, formerly the Womenswear Spectrum) with its companion pages. Its jobs:

- write briefs for browser threads;
- file their returns under `jobs/returns/`;
- merge returns into the records;
- build and deploy;
- keep the rulings log.

Browser threads read, Sebastian rules, and this thread proposes and merges.

**Where things live:**

- **Repo:** `github.com/sebastiangard-source/mfdb`, cloned to `/tmp/mfdb`. Clone it fresh if it isn't there, and push to `main`.
- **Commits:**
  - Commit with `git -c user.name=mfdb -c user.email=mfdb@local commit`.
  - End every message with the Co-Authored-By and Claude-Session lines the session gives you.
  - Then run `git push -q origin main`.
- **Men's map:**
  - Currently **v3.67.0, 382 brands**.
  - Artifact `https://claude.ai/artifact/42gtpMsaDfxEcrHDXYx5Cc`.
- **Explorer:**
  - Currently **v0.94**.
  - Artifact `https://claude.ai/artifact/UxiNniK4KZN35xhe4cK4CR`.
  - Publish it with the sub pages in `files`, and keep `capabilities: {downloads: true}`.
  - If the artifact refuses because this conversation hasn't read it, do an Artifact `read` first.
- **Rulings log:** `jobs/briefs/RULINGS_2026-10-12.md`. Append a dated section for each ruling.
- **Doctrine:** `ARCHITECTURE.md`, `audit_protocol.md`, `registers/LOCATIONS_README.md`.

## How Sebastian works

- **Send the HTML every time a build changes:** `index.html` (men's) and `explorer.html`, via SendUserFile. He has complained when it was missing.
  - His saved memory says deliverables should be .docx. That applies to documents, not to site builds or browser-thread briefs, which go as zip, csv and md.
- **Writing style:** plain American English, no em dashes in prose. Wrong is worse than missing.
- **Thread messages:** he pastes browser-thread messages and returns into this chat. Give him a reply he can paste back in a quote block, short and decisive.
- **Caching:** when he says he can't see a change, it's usually the cache. Tell him to hard refresh and check the version stamp.

## Standing doctrine (short form)

Counted beats authored. The brand's own locator and site are the only source. Threads propose; Sebastian rules.

- `NC` means not counted, never zero.
- `NONE` means the brand doesn't sell it or do it.
- Never work around a bot wall or a tool permission refusal.
- Briefs are read-only: no buying, signing in, signing up, following or messaging. Keep private account details out of returns.
- Names must match `dist/canonical_keys.txt`, and every brief ships with `reconcile.py`.
- Department stores are recorded but not seated as stockists unless Sebastian rules otherwise.

## Pipelines

### Men's release

1. Add an entry to the top of `data/changelog.json` with a new version. A release with the same version but a changed hash will stop.
2. Run `timeout 590 python3 tools/job.py release --deploy > /tmp/claude-0/relN.txt 2>&1; echo rc=$? >> …`. It lints, builds, validates and runs testpass (367 checks).
3. Copy `dist/index.html` to `/mnt/user-data/outputs/index.html` and to the scratchpad `mens_index.html`.
4. Republish artifact 42gt… from the scratchpad copy.
5. Commit and push.

Things that bite:

- **Lint:** every New York City place needs `h` (a neighborhood, from the existing set). Every brand `region` needs both `o` and `s` keys.
- **Seats** must stay dense. If you remove a brand, renumber the seats above it and reindex the place indices in every region list.
- **Places** are appended to `data/places.json`. `k='o'` is an own store and `k='s'` a stockist. For a stockist, copy the shape of Louie or Alan Bilzerian: `n a c s z k t ub bt v o{s f w ot d u sn c} src2`.
- **Schema and fields:** the field schema is in `schema/fields.json`. Constants are injected through `/*@@NAME@@*/` in `app/template.html`.
- **Derived values:** REACH is computed in `tools/spec.py` with 0–5 steps at 1+, 5+, 13+, 51+ and 250+ stores. `validate.py` checks ranges.
- **Seating new brands:** `tools/seat_from_return.py` together with `authored.py`. Men's price bands: under $150 premium, $150–400 accessible, over $400 true luxury.

### Explorer

1. Run `python3 tools/build_womens.py [--deploy]`. It writes:
   - `dist/womens_spectrum.html`;
   - `app/sub/cards.js` and `cards_data.js`, from `cards.tpl.js` via write_cards;
   - `app/sub/maggies-list.html`, from the .tpl via write_maggie.
2. Deploy copies `womens/brandset/explorer.html` plus the sub pages.
3. Bump the `<b>v0.xx · ` stamp in `app/womens_template.html`.
4. Explorer tests are in `/tmp/claude-0/t.py`, `t2.py` and `t3.py`. They may be gone after a container reset; rebuild them if needed.

### Sub pages

All in `app/sub/`:

| Page | How it's built |
|---|---|
| `overlaps.html` | edited directly |
| `cake-croissant.html` | edited directly |
| `ws-cake-croissant.html` | from `.tpl.html` by `tools/build_ws_venn.py`. Covers the WS centers, CAKE, Croissant and Rakuten+. Drops come from `registers/ws_tenant_drops_2026-10-22.csv` and Rakuten+ from `registers/rakuten_plus_2026-11-02.csv`. Venn fonts are Avenir Next. |
| `maggies-list.html` | 122 brands from `registers/maggies_list_2026-10-22.csv`. It is first in the nav. |
| `cards.js` | the shared brand card. It lazy-loads and falls back to IG/TT links. `tierOf` mirrors the Explorer's re-banding. |

### Tells

`tools/merge_tells.py` reads `jobs/returns/tells_2026-11-01/**/return.csv` plus `master_return.csv`; the master wins, and its OVERRIDE is applied. It writes `registers/tells.csv` and the men's `tell` field, which shows only yes at high or medium confidence. The Explorer reads `tells.csv`.

Of 567 brands, 169 have a tell, 269 have none, 112 are unclear and 17 are NC. 155 tells are shown.

Rulings: the A.P.C. wordmark and other distinctive wordmarks count. Construction details count, so Edward Green is yes. Calvin Klein and the CdG PLAY heart are yes at medium. Crockett & Jones is none.

### Native currency

Price arrays carry `[lo, hi, CUR]`. `FXUSD {JPY:1/150, GBP:1.30, EUR:1.10}` positions the bars, and the figures stay as read. Ten brands are affected: Undercover, Kapital, Needles, Nigel Cabourn, Hender Scheme, Ring Jacket, Sugar Cane, Hackett, Zilli and Stefan Brandt.

## Browser threads out right now

### 1. `stockists_undercover_2026-11-03`: returned and merged

- The return and NOTE are at `jobs/returns/stockists_undercover_2026-11-03/`.
- All 18 shop records are in `registers/shops_undercover_stockists_2026-11-03.csv`. The 8 October read missed four shops because their pages write "United States" instead of "USA".
- v3.67.0 added the four Northeast shops as stockists linked to 77 brands. Places 6770–6773 are Alan Bilzerian, Joan Shepp, Atelier New York (men's door) and Dover Street Market New York.

**Held for Sebastian:**

- **The eight shops outside the Northeast,** pending the national question: DSM Los Angeles, Maxfield, H.Lorenzo, Modern Appealing Clothing, Blake, Ikram, Nakamuraya and Relish.
- **The five Nordstrom doors.** The department-store rule applies; the store pages don't mention Undercover, though nordstrom.com sells it.
- **Kith Manhattan.** It's already a Kith own store.
- **Gender for women's shops.** The thread wrote `womens_only` for Blake, Ikram and Relish, and that value isn't in the schema. Add it, or use `womens_with_mens_tail`? Relish added men's in 2022.

### 2. `stockists_national_2026-11-03`: in progress, batch 1

- The pack is at `jobs/briefs/stockists_national_2026-11-03/`.
- It covers 56 brands that sell through independents but have no Northeast stockist or store. It returns every US shop the brand's own locator lists, flagged Northeast or not, with `country_as_written`.
- Status buckets in `worklist.csv`:

| Status | Brands |
|---|---|
| read | 24 |
| verify | 8 |
| reread | 4 |
| verify_count (Ariat) | 1 |
| second_look | 19 |
| skip (Flint and Tinder) | 1 |

- **First partial return:** Birdwell, Castaway, Edward Green, Evan Kinori and Velva Sheen match the file exactly. Baracuta and Aspesi list only their own stores (`NONE`).
- **Blocked:** the Deus Ex Machina (Stockist.co) data endpoint was refused by the tool's permission layer. The Locally widgets for Eastside Golf, Duck Head, Danner, Quoddy and Stan Ray can't be read as text.
- **Last instructions sent to the thread:**
  - Don't work around the refusal.
  - Try the brand's public page on locally.com, or a city search covering the ten Northeast states' largest cities plus NYC, LA, Chicago, SF, Dallas, Atlanta and Seattle.
  - For Deus, if search stays broken, return one row with `NC` and the marker count.
  - Big lists like Fidelity Denim (about 243) go in chunks, Northeast rows first.
  - Entries with no country that name a US state or ZIP are kept as US, with `country_as_written = blank on page`.
  - About five brands per turn. Returns are cumulative; each replaces the last.
- **Sebastian may clear** the Stockist.co and Locally domains in the Chrome extension's site settings.

**On return:**

1. File the batches under `jobs/returns/stockists_national_2026-11-03/batchN/`.
2. Match the Northeast rows to places (`k='s'`, by normalized name and city). Add new Northeast independents as stockists only after a shop-record pass (the Ellicott and Undercover briefs are the model). Link brands to the existing shops directly.
3. Put the Northeast and national counts in front of Sebastian for the national ruling.

**Quick win, offered but not ruled:** the 8 October registers already hold eight pairs where the shop is on the map but not linked to the brand:

- Castaway at Englunds and at Hassis
- Edward Green at Mr Sid
- Evan Kinori at c'h'c'm
- Human Made at Hirshleifers
- Velva Sheen at Totem Brand Co.
- Deus Ex Machina at Galvanic
- Ariat at Lenny's

Human Made and Lady White are now linked through DSM New York.

The cause: the map links a brand to a stockist only when the shop's own list names it. Brand-side reads in `registers/stockists_wave_{a,b,c}_2026-10-08.csv` were never linked. Also check every brand in that read for the "United States" miss.

### 3. Other packs written but on hold

- **`depop_styles_2026-10-24`:** on hold, because the pilot found no public style tags. A text-mining pilot was offered.
- **`tells_2026-11-01`:** finished. 17 brands are NC, to retry: Allen Edmonds, Ariat, Cesare Attolini, Charvet, Corneliani, Hermès, Junya Watanabe, Rick Owens, Rubinacci, Closed, Rakho, Flint and Tinder, Mango, prAna, Sanctuary, SKIMS and ViX Paula Hermanny. 112 unclear and 14 low still need settling.

## Done this thread (since 15 October; see the changelog and rulings log for detail)

**Explorer:**

- the venn WS set, with multi-brand stores, local boutiques and non-brands cut and Kirna Zabête kept;
- header cleanup;
- brand cards on the companion pages;
- Madewell, American Eagle, Urban Outfitters and Jimmy Choo added;
- unified tier-basis wording (`xbasis()`/`money()`, BASIS_HAND for Cozy Earth, Miguelina and Suzie Kondi);
- the Maggie's list page;
- order chips as a segmented toggle;
- tells on the hover card;
- the 16:9 screenshot view (white, denser pills, header spacing);
- Rakuten+ added (22 brands);
- Avenir Next on the venns.

**Men's map:**

- Ellicott & Co. (Lancaster, PA) added as a stockist, marked visited 24 Oct;
- seven brands seated: American Trench, Bridge & Burn, Soft Goods, Peregrine Clothing, SeaVees, Lems, Nisolo;
- TOPO Designs removed;
- Oliver Spencer craft 4 and style 4;
- Asket durability and fit flexibility 5;
- "has stores" dial above Focus, with slider labels 1+/5+/13+/51+/250+;
- Registers open by default;
- underline fix;
- tells on the detail page and hover card;
- long store-city lists fold by state;
- yen, pound and euro bars;
- Undercover's Northeast stockists.

**Also:** the WS tenants file, sent to Sebastian; the Chico's Tier 2 explanation; and the wool dial, which already exists.

## Open offers and rulings to walk with Sebastian when he asks

1. **National stockists:** add shops outside the Northeast for every brand, or only for designer brands with no own stores?
2. **Nordstrom and department doors** as stockists?
3. **`womens_only` gender value.**
4. **The eight unlinked on-file pairs** listed above.
5. **Retry the 17 NC tells** and settle the unclear ones.
6. **The overlaps page:** rebuild its Cyprus column from live data and fix its stale footnote.
7. **Depop:** the text-mining pilot.
8. **Benched or pending brand work:**
   - Power Goods (benched);
   - split Bulova and Citizen;
   - Lucky Brand Tier 1 check;
   - a women's price read for the brands priced from men's lines.
9. **The fabric dials:** move the wool dial and drop linen?
10. **American Eagle, Madewell and Jimmy Choo:**
    - American Eagle's 46 "Closed" cards;
    - Madewell's men's-only shops;
    - Jimmy Choo's three held shops.
11. **Pound and euro rates:** they're set at rounded figures ($1.30 and $1.10); refresh if Sebastian wants.

The older open list in the 15 October handoff still stands where it isn't covered here.

## Project docs

The Cyprus project holds copies of briefs, returns and rulings under `wave_b/`, `wave_c/`, `spectrum/`, `competitive/` and `zeitgeist/`. This handoff is also at `spectrum/HANDOFF_2026-11-03.md` there.
