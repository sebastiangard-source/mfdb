# Handoff — the Spectrum thread, 15 October 2026

For the next version of this chat (ACTIVE — Menswear Brands VI). Written by the Spectrum thread (Menswear Brands V)
at close. Everything below is in the repo; this page says where, and what is mid-flight.

## What this thread is

The **Spectrum thread** is the merge-and-build seat for The Menswear Spectrum and The Womenswear Spectrum. It writes
briefs for browser threads, files their returns under `jobs/returns/`, merges them into the records, builds and
deploys the maps, and keeps the rulings log. Browser threads read; Sebastian rules; this thread proposes and merges.

- Repo: `github.com/sebastiangard-source/mfdb`, cloned to `/tmp/mfdb` (clone fresh; push to `main`).
- Men's map: **v3.58.1, 373 brands**. Artifact `https://claude.ai/artifact/42gtpMsaDfxEcrHDXYx5Cc`. Deployed by
  `tools/job.py release --deploy`.
- Women's map: **v0.13, 246 brands** (180 women's-only + 66 crossovers). Artifact
  `https://claude.ai/artifact/UxiNniK4KZN35xhe4cK4CR` (published with `capabilities: {downloads: true}` — keep that on
  every republish).
- Rulings log: `jobs/briefs/RULINGS_2026-10-12.md` (append a dated section per ruling).
- Architecture and doctrine: `ARCHITECTURE.md`, `audit_protocol.md`, `registers/LOCATIONS_README.md`.

## Standing doctrine (short form)

Wrong is worse than missing. Counted beats authored. The brand's own locator and site are the only source. Threads
propose, Sebastian rules. Plain language, American spellings, no em-dash tics. `NC` = not counted (never zero),
`NONE` = does not sell/do, `np` = not published, `ND` = page read, nothing stated. Never work around a bot wall
(UGG is held twice for this). Names must match canonical keys; every brief ships `reconcile.py`. Sister banners are
their own names (RRL, Purple Label, MICHAEL Michael Kors, Carhartt WIP). Kids/home/fragrance/watch boutiques are not
doors. Commit as `-c user.name=mfdb -c user.email=mfdb@local`.

## Pipelines

**Men's release:** `python3 tools/lint.py` → `python3 tools/build.py` → `cd dist && python3 ../validate.py
menswear_spectrum.html && timeout 580 python3 ../testpass.py` (367 checks) → bump `data/changelog.json` →
`timeout 580 python3 tools/job.py release --deploy` → `cp dist/index.html /mnt/user-data/outputs/index.html` →
commit, push → republish artifact 42gt… from `dist/index.html`.

**Women's:** `python3 tools/clean_fibre.py` → `python3 tools/womens_records.py` (writes `data/brands_womens/*.json`
from the returns) → `python3 tools/build_womens.py` (writes `dist/womens_spectrum.html` from
`app/womens_template.html`) → copy to outputs → commit, push → republish artifact UxiN….

Women's record shape = men's record shape (name, band, band_note, why, origin, chan, say, onething, prices[8],
garments, price_evidence, doors, site, ownership, season, opview/quote, resale, certs, focus{tech,craft,comfort,style},
fabric{denim,cashmere,linen,cotton,wool,synth,silk}, fibre{…, ly_pct, cv_pct, clean_pct…}, garment_links, notes).
Women's garments: T-shirt, Blouse, Sweater, Jeans, Trousers, Dress, Outerwear, Shoes.

## Rules that are ruled (do not re-litigate)

- Women's band cuts **$200 / $600** on mean of blouse + sweater entry; men's stay $150 / $400. Basic = tee ≤$35 and
  blouse <$80 (or tee ≤$35, no blouse, another slot priced). HAND overrides in `tools/womens_records.py`.
- Crossovers re-banded at the women's cuts on their men's shirt+sweater mean; movable by the band sliders.
- Leather/suede/nappa/lambskin/calf hair/ponyhair never the women's outerwear high; faux is fine.
- `fab_silk` is a seventh fabric dial (women's). Lyocell shown apart from other cellulosics. No fabric dials for shoe,
  swim, underwear/sleepwear and loungewear houses (`NO_FABRIC` list in `womens_records.py`); Monique Lhuillier held.
- "Natural or lyocell" dial (`clean`): every fibre natural or lyocell/TENCEL, elastane ≤5%, lead fibre irrelevant,
  Tencel Modal excluded, ≥20 judged styles; cuts 99.95/95/85/70 like the natural dial. Source:
  `registers/clean_fibre.csv` from `tools/clean_fibre.py`.
- Style segments (men's): 15 segments, `seg` field on every record, filter on primary only. Rescores applied
  14 Oct. Queued, not done: boat 4–5 on the Italian tailors, racquet 4 on Sunspel, street 4 on Wales Bonner,
  style 3 on Palace.
- Chanel 29 fashion boutiques (fragrance/watch boutiques excluded), Miu Miu 9. Kapital seated by hand, craft 4
  pending. Y-3 doors NC. Sanderlak True Luxury, one store. Kartik Research and Sanderlak are not women's.

## Browser threads out right now

1. **`brief_womens_dials_2026-10-14_thread1_batches4-5.zip`** — reissue of women's dials thread 1, batches 4–5
   (20 brands: SKIMS … Splendid; Anine Bing … STAUD). Pack at `jobs/briefs/womens_dials_2026-10-14/thread1_rebrief/`.
   Batches 1–3 and 6–18 are merged. On return: file under `jobs/returns/womens_dials_2026-10-14/batch04`, `batch05`
   (return.csv, return_styles.csv, NOTE.md), run the women's pipeline, author comfort/style for the 20 into
   `registers/womens_focus_authored.json` (provisional, say so), bump women's version, republish. Ruling to ask for:
   anything the NOTE proposes for craft ≥3, and any `_sold` flag it reports wrong.
2. **`brief_womens_crossover_a_2026-10-15.zip`** — Part A reissue: 187 men's-map brands, yes/partial/no on women's
   clothing in their US stores, 8 batches of 25 by store count. Pack at `jobs/briefs/womens_crossover_a_2026-10-15/`.
   Part B (Chanel, Miu Miu) is done. On return: file under `jobs/returns/womens_crossover_a_2026-10-15/batchN/`; the
   `yes` rows join the women's universe as crossovers (add to `registers/own_doors_womens_2026-10-10.csv` or the
   universe list `build_womens.py` reads — check how `build_womens.py` decides a men's brand is a crossover and extend
   that); `partial` goes to Sebastian for a ruling, with the evidence line. Nothing in this pass changes the men's map.

Dropped for now by Sebastian's ruling (15 Oct): geocoding, Rue La La.

## Not yet written (queued)

- National stockist pass for 172 men's brands with no own stores (brief outline exists in the summary of this
  thread; Wave B/C stockist rules in `jobs/briefs/seat_wave_c_restart_2026-10-13/`).
- Women's stockists pass.
- Style-count / lyocell-finder pass (~100 thread-hours sized). Sebastian is weighing a separate lyocell product; see
  project memory `areas/lyocell-finder.md`. Prototype outputs: `clean_fibre_styles_2026-10-15.csv` (10,523 styles),
  `lyocell_natural_styles_2026-10-15.csv`.
- Add the parent-page rule to `rules_garment_links.md` (a category parent page is acceptable when the garment has
  no page of its own; say `links_kind`).

## Open rulings to walk with Sebastian when he asks

Unisex listings (Extreme Cashmere, Lauren Manoogian, Terez, Industry of All Nations, Pendleton, Yohji, Lady White Co.);
Elie Saab craft 3; Miguelina caftans as dresses; stale `_sold` flags in the dials worklist; Anthropologie / Free
People own-label re-cut (Beams rule); Kapital craft 4 vs 5; Gabriela Hearst $18k coat as outerwear high; HSM /
Hickey Freeman / Oxxford / Samuelsohn seating; UGG (held, bot wall); Rapha; Guam; men's True Luxury cut at $600 (would
move 36 brands — Sebastian said skip the re-read for now); B Corp parent search on facts rows 1–50; 12 Vinted `NONE`
rows; Carolina Herrera owner if the Estée Lauder talks close.

## Women's page features (so you don't rebuild them)

Side rail (search, store-tier multi-select chips, Northeast, crossovers, band-cut sliders, focus/fabric/natural/clean
threshold sliders with hover tips, Publish block); hash state `#v=`; publish → inline standalone page with back /
copy / copy as rich text / save (downloads capability) / open in new tab / email draft; user-renamable bands; dense
brand list; per-dial explanations on the brand panel. Men's page: segment chips, certs, dials, clear-all.

## Project docs

The Cyprus project holds copies of briefs, returns and rulings under `wave_b/`, `wave_c/`, `spectrum/`,
`competitive/`, `zeitgeist/`. This handoff is at `spectrum/HANDOFF_2026-10-15.md` there. Keep writing durable
rulings and findings to the project as well as the repo.
