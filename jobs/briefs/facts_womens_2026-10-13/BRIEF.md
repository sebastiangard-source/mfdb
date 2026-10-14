# facts_womens_2026-10-13 — origin, ownership, lookbook, resale, certifications, a quotation and the signature product for 180 women's brands

**Issued** 13 October 2026 · **Kind** read · **Batches of ten, each returned as done** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first, then `rules_quotes.md`. This is a facts job, not a price job: every
figure and sentence you return is read from the brand's own site, its filings, or named press, and every
row says where. It is a Chrome job. If you cannot run a browser, say so and stop.

## Why

Every men's brand on the Spectrum carries a short set of facts beside its prices and stores: where and when
it was founded and by whom, who owns it today, whether it publishes a lookbook, where it resells, whether it
is a B Corp or GOTS-certified, one real quotation in its own voice, and its signature product. The 180 women's
brands with their own US stores have stores on file and a price pass under way, but none of these facts. This
job gives each of them the same set, so a women's brand page can read like a men's one.

## What you return

`return.csv` in the columns of `return_template.csv`, one row per brand, all 180; `NOTE.md` per batch. The
template's second row is a worked example — delete it. Nothing else.

## The columns

**Description and channels**

- `what_it_sells` — one sentence, under thirty words, in plain words: what the brand makes, at what level, and
  how it mostly sells. Written from the range as it reads on the site today, not from the brand's own blurb.
  No adjectives the brand uses about itself ("effortless", "timeless", "elevated").
- `channels` — the ways the brand sells in the US, as letters joined by `;`: `O` own stores, `D` department
  stores (named on the brand's own stockist page or the department store's site), `I` independent shops,
  `W` its own site. `O` is already established by the doors register — confirm it, do not re-count.

**Origin and ownership** (men's sections 8 and 13, the same words)

- `founded_year`, `founded_place` (city, country), `founders` — from the brand's own about page, then
  filings, then named press that quotes the brand. `np` where the brand does not publish it; do not take a
  Wikipedia year without a source behind it.
- `owner_today` — the entity that owns the brand now: the brand itself if independent, else the parent
  (Tapestry, Capri, URBN, Gap Inc., LVMH, Kering, OTB, Max Mara Fashion Group, a private-equity firm by name).
  Many of these are listed companies: the annual report or 10-K is the source. `ownership_url` is that page.
- `signature_product`, `signature_product_url` — the one product the brand is known for, in the brand's own
  name for it, with the product page. One; if you cannot pick one, the oldest continuous style. `NONE` with a
  note if the brand has none.
- `pronunciation` — only where a reader might get it wrong (Eileen Fisher no; ERES, Akris, Maje, Sézane yes).
  Plain syllables with the stressed one in capitals. `NONE` otherwise.

**Lookbook**

- `lookbook_found` yes/no; `lookbook_season_label` as the brand writes it (Fall 2026, AW26, Holiday 2026);
  `lookbook_womens` yes/no (is the lookbook, or a section of it, women's); `lookbook_url`. A collection page
  with a season name counts; a plain category page does not.

**Resale**

- `vinted_womens_url` — the Vinted catalogue URL filtered to the brand and women's; `vinted_brand_ids` the
  numeric id(s) in that URL. `therealreal_url` — the brand's designer page on The RealReal, where one exists.
  These are the women's twins of the men's Vinted and Grailed links. `NONE` where the brand has no page.

**Certifications**

- `b_corp` yes/no with `b_corp_entity` (the certified company name as the B Lab directory lists it — it is
  often the parent, not the brand). `gots_certified` yes/no with `gots_entity` from the GOTS public database.
  A claim on the brand's site is not a certification: both come from the certifier's directory.

**Quotation** (`rules_quotes.md`, the same rules)

- `quote`, `quote_who`, `quote_source`, `quote_url`, `quote_date`. Verbatim, six to thirty words, in the
  brand's own voice (founder, chief executive, creative director, or the house writing as itself). Never a
  journalist, a retailer, Wikipedia or a reviewer. `NONE` with a note where there is nothing worth quoting.

**Housekeeping**

- `status` is `read`, `partial` (past the time box, said so) or `NC`. `read_date`, `source` (the kinds of
  source used, e.g. "brand site; 10-K 2025; WWD 2024"), `note` for anything the columns cannot carry.

## Rules

- Names must match `canonical_keys.txt`; run `python3 reconcile.py` before each return.
- `NC` nobody looked; `NONE` does not exist or does not apply; `np` the brand does not publish it. No empty
  cells.
- The brand's own statements first, then filings, then press that quotes the brand. A famous name earns
  nothing: an unsourced "founded 1983" is `np`.
- A sister banner with its own stores (G by GUESS, Marciano, MICHAEL Michael Kors) is its own name; facts
  are for the worklist brand only.
- Do not touch the map. Do not send working files. Out of scope but noticed: `NOTE.md`.

## Order and time box

`worklist.csv` is sorted by store count, largest fleet first, with a `batch` number; batches of ten,
returned as each is done. Ten minutes a brand; twenty for a house whose ownership needs a filing read.
Past the box, what you have, `NC` on the rest, said so.
