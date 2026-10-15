# followup_2026-10-15: what the crossover and dials passes left open (6 brands)

**Issued** 15 October 2026 · **Kind** read · **One thread, two parts** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job on the brands' own US sites. If you cannot run a browser, say so and stop.

## Why

Crossover Part A (187 men's-map brands, "do your US stores sell women's clothing?") and the women's dials pass
(180 brands) are merged. Six brands could not be settled from what came back: two were stopped by bot walls, one
was cut short by one, two have own sites that do not show what their stores sell, and one answered from the
wrong country's site. This pack settles them.

## Start with Allen Edmonds

Allen Edmonds is first because it is the only brand never read at all. The last thread met a Cloudflare
"verify you are human" page on allenedmonds.com and stopped, rightly.

- Open allenedmonds.com once, in a normal tab, at a normal pace.
- **If the page loads**, read it as in Part 1.
- **If the Cloudflare check appears**, stop and ask Sebastian, in one line, whether he will tick the box himself in
  that tab. A person passing a visible check in their own browser is ordinary browsing. Everything else is
  working around the wall, and that is never done: scripts, retries in a loop, caches, mirrors, other country
  sites, third-party retailers.
  - If he ticks it and the site loads, read it.
  - If he says no, or does not answer, file the row `NC`, note `held: Cloudflare check`, and move on.

The same rule holds for every brand in this pack: one plain try; a visible check box goes to Sebastian; any other
wall is `held`.

## Part 1: crossover re-reads (5 brands, `worklist_crossover.csv`)

Return `return_a.csv` in the columns of `return_a_template.csv`, with the definitions unchanged from Part A:

- `womens_clothing`:
  - `yes`: a women's clothing range under the brand's own name (tops, knitwear, trousers, dresses or outerwear).
  - `partial`: thin, made to order only, unisex sizing only, or sold in some stores and not others.
  - `no`: none.
- `where`: `all stores`, `some stores`, `online only` or `NONE`. Fill it only when the locator lists departments
  or a store page says "Women". Otherwise `NC`, and the evidence line says why. Do not infer `all stores` from a
  Women tab on the site.
- `womens_url`, `evidence` (one line: what you saw), `read_date`, `note`.

The column `what_to_settle` says what each row needs:

1. **Allen Edmonds:** as above. If a women's range exists, apply Part A's footwear rule. A women's range that is
   footwear only is `no`, with the note "women's footwear only".
2. **Timberland:** a bot wall cut the last read off after 72 tiles of the unisex Clothing listing, with 3 women's
   pieces seen. Count the women's clothing styles on the US site, then say `yes` or `partial` with the count. If
   the wall returns, `held`.
3. **Comme des Garçons:** comme-des-garcons.com sells nothing. Look for the brand's own US door pages on a CDG-owned
   domain and see whether they say the store sells women's. Dover Street Market is CDG's own retail company, so its
   New York pages may be read. Say whether the evidence came from a CDG door or from Dover Street Market; the
   Spectrum thread decides whether Dover Street Market counts. Say which domain you used. If nothing on a CDG-owned page says it,
   `NC`.
4. **Chrome Hearts:** the own site sells only scents, intimates and small goods, but its stores sell clothing.
   Read the brand's own US store pages for whether women's clothing is sold there. Intimates alone are not
   clothing. If the pages do not say, `NC`.
5. **Paul Smith:** the last read was `yes`, but paulsmith.com/us redirected to the UK site in pounds. Settle
   whether a US web store exists. If it does, give its women's URL and re-confirm `yes`. If it does not, keep
   `yes` and set `womens_url` to the UK women's page, with the note "no US web store; UK site".

## Part 2: True Religion women's dials (1 brand, `worklist_dials.csv`)

True Religion was held at a PerimeterX ("px-captcha") wall in the dials pass. Its jeans link was filed before the
wall. Everything else is `NC`.

- Read the rules in `rules_garment_links.md`, `rules_fibre.md`, `rules_craft.md` and
  `rubric_craft.txt`, and return `return.csv` and `return_styles.csv` in the template columns.
- The read: the seven other listing links, an 80-style women's sample with composition, fabric dials, proposed
  tech and proposed craft.
- The standing defaults from the dials pass apply:
  - Own labels only.
  - Lyocell kept as its own fibre.
  - `fab_silk` read.
  - Unisex listings counted and flagged.
  - Sleepwear and swim excluded.
- PerimeterX shows a "press and hold" check, not a box. Treat it like the Cloudflare box: one plain try. If it
  appears, ask Sebastian once whether he will clear it himself. Otherwise `held`.

## Return

- `part1/return_a.csv` and `part1/NOTE.md`.
- `part2/return.csv`, `part2/return_styles.csv` and `part2/NOTE.md`.
- Run `python3 reconcile.py` on the names before each return. `canonical_keys.txt` holds the six names.
- No empty cells: `NC` nobody looked, `NONE` does not exist, `np` not published, `ND` page read and nothing stated.
- Anything out of scope but noticed goes in a `NOTE.md`, not in the rows.
- Do not touch the maps.

Part 1 matters first: Allen Edmonds, then the other four. Return Part 1 when it is done, then Part 2.
