# outerwear_high_womens_2026-10-14 — the top non-leather outerwear piece for 46 women's brands

**Issued** 14 October 2026 · **Kind** price · **Four batches of twelve, each returned as done** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a one-column follow-up to the women's price pass. Chrome job on the
brands' own US stores. If you cannot run a browser, say so and stop.

## Why

Sebastian ruled on 14 October that **leather and suede are not elevated materials**: a leather or suede piece is
never an outerwear high, in the same way fur, shearling and exotic skins never were. 46 women's brands
were read with a leather or suede piece as their outerwear high. Their pages now show the outerwear entry alone.
This job supplies the high. Faux leather, faux suede and "suede-effect" are not leather and were left as read.

Nothing turns on the band: the high is for the record and the brand page only.

## What you return

`return.csv` in the columns of `return_template.csv`, one row per brand; `NOTE.md` per batch. Nothing else.
`worklist.csv` carries the store used, the outerwear entry already on file and the leather piece that was read
as the high, so you know what to pass over.

## The rule

The high is the dearest regular, full-price jacket or coat in the brand's current women's range that is **not**
leather, suede, nappa, lambskin, fur, shearling or an exotic skin, and not a collaboration, runway piece,
limited edition or capsule. Not a blazer, not a shirt-jacket. `basis` is `pair` where it is the same style as the
entry in an elevated fibre (majority cashmere, silk, alpaca, mohair, vicuña, superfine wool), else `range`.
Full price only: the regular price on a marked-down piece, checked against a second product. Whole dollars,
rounded half-up; the exact figure in `note`. Where the brand sells no non-leather outerwear at all, `NONE`
with a note.

## Rules

- Names must match `canonical_keys.txt`; run `python3 reconcile.py` before each return.
- `NC` nobody looked; `np` no price published. No empty cells.
- Women's range only; own label only on the multi-brand stores (Anthropologie, Free People, Evereve, Aritzia,
  Reformation, LOFT).
- Do not touch the map. Out of scope but noticed: `NOTE.md`.

## Time box

Five minutes a brand. Past the box, what you have, `NC` on the rest, said so.
