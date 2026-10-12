# Wave B: one brand, full record (agent spec)

You are researching ONE brand for Sebastian's Menswear Spectrum map. You gather and propose; he rules.
All rule files are in `/home/claude/wb/`. Read these before starting, in this order: `audit_protocol.md`, `BRIEF.md`,
`RULINGS_2026-10-08.md`, `seat_wave_b_rulings.md` (10 Oct), then the rules file for each section as you reach it
(`rules_prices.md`, `rules_garment_links.md`, `rules_fibre.md`, `schema_styles.json`, `rules_craft.md`, `rubric_craft.txt`,
`rules_quotes.md`). The column lists are in `schema.json` and `return_template.csv`. Where this spec and a rules file disagree, the
rules file wins, except for the overrides below.

## Overrides and rulings (current as of 10 Oct)

- Outlets: a store in a Premium Outlets, Tanger, Mills or other named outlet centre is an `outlet` unless the brand's own locator
  says otherwise. Say so in `note`. Locator labels that look wrong the other way stay as the locator gives them.
- Operator- or licensee-run stores under the brand's banner are `own-door`, with the operator in `note`. Department-store counters
  are `concession`. Pop-ups are `pop-up`.
- `status` in own_doors.csv: `as listed`, `open`, `opening`, `closed` (record a closed store as a row; do not drop it), `held`
  (inclusion uncertain, e.g. operator unknown at a resort pro shop).
- Puerto Rico rows are kept, coded PR.
- Positive zero: no US own door gives `0` with the locator URL, and the full record still goes ahead. If the worklist `why` claims US stores
  and the locator shows none, add `worklist_conflict: <the claim>` to the note.
- Press and Wikipedia are NOT sources for a door count. Brand's own locator only. If the locator cannot be read, `NC` with the exact block.
- Do not guess bands. There is no `band_guess` column in the full record.
- Count non-US doors in `world_non_us` where it is cheap (locator covers the world); otherwise `NC` with the reason.
- Tokens: `NC` nobody looked; `NONE` the brand does not sell/do this; `np` no price published; `ND` composition not stated (styles
  file). **No empty cells anywhere.** Use `-` only where a rules file says `-` is legal.

## Standing rulings from Sebastian, 11 Oct (apply without asking)

- Shearling is fur-on and is never a high. Neither are fur or exotic skins (croc, alligator, python, ostrich, lizard).
- Capsules, collaborations, reissues, limited editions and runway pieces are never a high. Regular-range pieces are allowed, however expensive.
- Licensed lines (NFL, team or league product, character licences) are out of prices.
- Styles are counted by article number or product code, not by model. The census covers the range in the site's own navigation; archive-sale stock outside navigation stays out.
- A store in an outlet centre is an `outlet` whatever its sign says.
- Held rows stay `held` (not counted, not dropped) until the operator is known.
- A duplicate locator row is one door; drop the duplicate and say so.
- Filings and press are never a door source, even when they give a different number. Mention the figure in NOTE.md only.
- Craft: an unnamed factory is a claim, not evidence. A licensed membrane or fabric is tech, not craft. Propose tech and craft and move on, because the map seats them as proposed.
- Dealer or wholesale chains with 5 or more US doors: summarise them in NOTE.md (name, door count) instead of writing rows.
- A suspicious composition: file it as read and flag it in the style's note.
- `own_doors_us` = own-door format only (not outlets). `own_doors_world` = own doors worldwide incl. US (not outlets) when known, else NC. Put outlets, concessions and pop-ups in `doors_basis`.

## Standing rulings added 11 Oct, after batch 2

- Shearling, fur and hair-on hide (pony hair, calf hair) are fur-on and are never a price.
- A garment the brand sells only as limited editions is `NONE` for that slot. A limited edition is never priced, low or high.
- Styles: count by article number when the number identifies the style. When the brand gives each colour its own article number,
  that number is a colourway, so count by product handle and say which you used.
- An overshirt or shirt-jacket is not a dress shirt. If there is no woven button-front shirt, the dress shirt slot is `NONE`.
  A casual woven button-down is still allowed where it is all the brand makes, and you say so.
- Licensee-made goods sold under the brand's own name in its own store are in. Collegiate, pro-team, league and character-licensed product is out.
- Operator-run doors (including airport concessionaires like Dufry) count as own doors, flagged with the operator in `note`.
- Do not stop for rulings. File what the standing rules say. Flag anything they don't cover in NOTE.md under a heading
  `Flags for merge`. The Spectrum thread rules at merge.

## Browser

Use ONLY the Chrome tab id you were given (mcp__claude-in-chrome__* tools; prefer browser_batch, javascript_tool and
get_page_text over screenshots). Do not open other tabs. Assert `location.host` before every capture. Go slow on feeds (concurrency
<= 3, ~150 ms spacing). Decline any non-essential cookies; never log in, create accounts, buy, submit forms or accept terms. If a
site blocks you, record the exact block and move on. `fetch()` from inside the brand's own page is fine for its own JSON
endpoints (Shopify `/products.json`, locator APIs, etc.). Never put a secret or API key in any output.

## Avoiding blocks (learned in batch 3: Hoka hit DataDome, Kapital's store IP-banned the browser)

- Read listing pages first and take everything they carry (price, composition in the tile/JSON) before opening product pages.
- Paginate only up to the count the site states. Never loop until a page comes back empty; some sites re-serve page 1 forever.
- Product pages one at a time, at least 1.5 s apart. Prefer the platform's JSON (Shopify `.js`/`.json`, SFCC `Product-Variation`,
  Next.js data routes) over full page loads.
- At the first 403, captcha or "access restricted" response, stop that site for the rest of the run. Record the exact block, `NC` what is
  left, and move to other sections. Never attempt a captcha.

## Order of work and time box

1. **Section 4, own doors**: ONLY if your prompt says the brand still needs it. Otherwise copy the given counts into `return.csv`
   and do not re-read the locator.
2. **Prices + men's listing links** (sections 1–2), 40 min. **Fibre census** (section 3): 25 min Shopify / 45 other / 75 big feed.
   If the feed is huge (thousands of styles), census the men's clothing feed; past the box mark it `partial` and say what share you read.
3. **Stockists** (section 5): the brand's own stockist / store-locator list of OTHER shops, US only, in the browser.
4. Sections 6–13, about 30 min in total.
Past any box: return what you have, `NC` the rest, and say so.

## Output: write these files into `/home/claude/wb/<BATCH>/<SLUG>/ (the batch folder is given in your prompt)` (create the folder)

- `return.csv`: header exactly as line 1 of `/home/claude/wb/return_template.csv` (132 columns), ONE row for the brand. `brand` must
  equal the canonical key exactly. `own_doors_us` = US own-door count (number); `own_doors_world` = all own doors worldwide incl. US
  when known, else `NC`; `doors_basis` = e.g. `locator: 21 own-door + 142 outlet (US); world NC, locator US only`.
  `proposed_tech`: integer 1–5 or NC; explain briefly in `note`. `proposed_craft`: 1–5 per the rubric, with `craft_reasoning`.
  `status` = `complete` or `partial`; `read_date` = the date you actually read the pages (run `date -I`); `source` = main URLs read.
- `return_styles.csv`: header from schema_styles.json column names, one row per men's clothing style in scope.
- `stockists.csv`: header = `brand,locator_url,locator_kind,shop_name,street,city,state,zip,country,shop_kind,source,note`.
  `locator_kind` in {stockist page, store locator, none, press/other}; `shop_kind` in {independent, department store, other brand
  own door, online only}. If the brand lists none, write one row with `locator_kind`=`none` and the rest `NONE`, saying where you looked.
- If section 4 was yours: `own_doors.csv` (header exactly
  `brand,store_name,banner_stated,format,status,street,city,state,zip,country,phone,venue,lat,lon,source_url,captured_on,note`,
  US rows only, captured_on = the date you read the locator). Fill `lat` and `lon` with the brand's own coordinates wherever the
  locator feed or page carries them (JSON locators usually do; also check JSON-LD `geo` and map embeds). Use `NC` where the
  locator gives none. Never geocode an address yourself. and `counts.csv` (header exactly
  `brand,us_own_doors,us_outlets,us_concessions,us_popups,world_non_us,locator_url,read_how,status,prior_facts_first,note`; one row,
  `prior_facts_first` = `NC`). The counts must equal the row counts by format, excluding `held` and `closed` rows.
- `NOTE.md`: short. Covers what was checked, what was not reached, what contradicted the worklist/record, anything the brief got wrong, the
  mark as written (put it in `note` of return.csv too, as `mark_as_written: X`), the fibre line verdicts in one or two lines,
  and anything out of scope but noticed.

Before finishing, run a check in Python: correct headers, no empty cells, brand key exact (`cd /home/claude/wb && python3 reconcile.py <file of names>`),
counts equal rows. Your final message to me: 5–10 lines covering the counts, price coverage, styles counted and status, stockists count,
proposed craft/tech, and anything that needs Sebastian's ruling. Do not paste the data.
