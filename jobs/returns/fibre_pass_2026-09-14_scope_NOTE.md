# fibre pass — scope restatement, 15 September

Rulings applied: **scope is clothing only**, **named fibre with no percentage counts as stating a
composition**, **"exclusive of elastic" excluded**, **down reads the shell**, **ties stay
first-listed**, and `synthetic_categories` harmonised onto one reading.

**68 of 197 rows changed.** 197 rows, 193 with a split, 4 held. Reconcile clean.
Full-file sweep: **zero sanity failures** — every identity within 1 of 100, no `spandex > total`,
no `high > any`, no `wc > total`, every JSON list parses. Schema clean on 196 of 197 (Rothy's
counted zero, as before). The measured range falls from **73,908 styles to 68,670** — 5,238 hats,
socks, belts, bags, shoes and hard goods out.

Spandex stays as **counts** in this file; the merge converts.

---

## Read this before merging: I did not send the restatement you asked for

Your triage said the thread "has both numbers already". That was true of the fibre percentages and
**false of the spandex counts**. Every batch wrote its clothing-only alternate as a denominator plus
a fibre split and **not one recounted elastane on that basis**.

Because the page renders stretch as a percentage of the range, filing the restatement as-held would
have published a number that is too high on **50 rows** — the denominator falls, the numerator
doesn't. Lululemon would have read **"stretch in 92%"** against a true 74%. Vuori 78% against 60%.
Malbon, TravisMathew and Duck Head all over ten points out.

So I recounted elastane on the clothing-only denominator for all 50 before sending anything. 49 came
back with figures, one is held. **36 of the 50 cells moved.** That is the difference between a
restatement and a corrupted dial, and it is why this took a second round rather than one pass.

---

## Two rows were wrong before scope touched them

Both are ruling errors the recount exposed, not scope effects. They would have been wrong at any
denominator.

**Lacoste — the filed pair was never on the main fabric line.** Filed 278/168. The recount's main
line on the *old* denominator is 249/151, and the filed high of 168 **exceeds even the
anywhere-in-string high of 164** on that basis, so the filed figure cannot have been read on the main
line at all. Lacoste puts 133 clothing styles' elastane in a Rib Edge, Lining, Yoke, Placket or
Collar Rib Border. Anywhere-in-string is 349/160. The cell is now **216/148**, a genuine ruling-2
correction. Its percentages also survived a separate near-miss: Lacoste writes the percentage
**after** the fibre in parentheses, so a percent-first regex returns a literal zero on 948 of 948
rows, and only the sum check caught it.

**Charles Tyrwhitt — 48 styles were counted as stretch that carry no elastane.** Filed 183. Of those,
48 read "100% cotton with natural/mechanical stretch" — a complete composition with no elastane,
which ruling 3's own last sentence excludes. The cell is now **106/19**. On the old convention it
would be 154/19; both are in the notes.

---

## Lululemon is held, and it is the top of the stretch league table

`spandex_styles` and `spandex_high_styles` are **NC**. The fibre split and denominator stand.

The channel still works — sitemap, the `"gender":["Men"]` field and the materials drawer were all
re-verified on 33 live PDPs. What stopped it is an Akamai edge control returning `400 GE401001` on
every dynamic path, homepage included. It fired after 33 pages at a 200 ms gap and **did not lift in
over two and a half hours**; fresh tabs, cleared cookies and the www host made no difference.
Measured refill is four to eight requests per five minutes of silence, against 431 style keys
remaining — six hours-plus of waiting. No challenge was engaged with.

What is known: of 33 of the 184 removed socks, hats, gloves and scarves, **24 carry elastane on the
body line and 14 are at 5% or more** (socks alone 16 of 23, 11 at 5%+). Both cells will fall
materially. 33 of 184 is a sample, not a count, so the cells are `NC` rather than a scaled guess.
The notes carry a step-by-step recipe for the retry.

This is the one row where the page will now show a coverage caveat on its headline house. I would
rather that than publish 92%.

---

## What moved most

| brand | stretch share, filed → final |
|---|---|
| Lululemon | 74% → **held** |
| Malbon | 27% → 38% |
| Charles Tyrwhitt | 32% → **22%** |
| Vuori | 60% → 67% |
| Duck Head | 36% → 30% |
| TravisMathew | 26% → 31% |
| Lacoste | 28% → **24%** |
| Wythe | 4% → **0%** |
| Hiroshi Kato | 64% → 60% |
| Percival | 10% → 8% |

Note the direction is not uniform: where accessories were elastane-rich the share **rises** once they
leave a smaller denominator can't offset them (Malbon, Vuori, TravisMathew); where the accessories
were the stretch (socks) it **falls** (Duck Head, Wythe, Charles Tyrwhitt).

**The headline finding of the recount is socks.** At six houses the removed styles are dominated by
socks and socks are nearly always elastane. Taylor Stitch's only two styles at 5%+ in its entire
men's range are The Camp Sock and The Waffle Sock — so its high cell goes 1 → 0. Wax London's ten
removed elastane styles are all socks. Duck Head's eight socks are eight of its twelve removed
elastane styles. Wythe's filed 5 becomes **0**.

**And scope is not monotone on the fibre dial either**, in both directions and for a simple reason —
whether a house's accessories are silk and cashmere or licensed polyester caps. Carhartt 17% → 62%
natural; Sease 87 → 92; Etro 85 → 89. Against: J.Press 94 → 90; Reiss 66 → 64; Baracuta 78 → 73;
Barbour 76 → 73; Club Monaco 85 → 83; Husbands 94 → 92, because its non-clothing is all leather
shoes and belts.

**Carhartt is the biggest single move in the file** — 1,472 styles at 27% coverage to **361 at 90%**,
17/10/0 to **62/27/1**, and partial to complete. 793 of the 1,111 dropped styles are one block of
licensed '47 caps that state no composition anywhere. Two agents restated it independently from
different notes and **agreed cell for cell**.

---

## Corrections, disagreements and three things I decided

**Two arithmetic errors in our own notes**, both caught by the sum check: `notes_b4d.txt` prints
J.Press's garments-only alternate as 90/3/0/6, which sums to 99 (correct: 90/4/0/6). `notes_b6a.txt`
says Boglioli's clothing-only cut is "the same 98/0/2"; it is **97/1/2**, so that dial does move —
the opposite of what the batch concluded.

**Carhartt's two alternates disagree and the disagreement is on the record**: `notes_b1a.txt` gives
367 styles / 62-28-1-9 / spandex 100-20; the later `notes_unisex_restate.txt` re-measure gives 361 /
62-27-1-10 / 134-19. The later figure is filed.

**Marine Layer's own clothing-only alternate was wrong under the ruling** — it drops Intimates, which
the ruling keeps — so that cut was rebuilt rather than copied.

**Vuori's denominator is one garment short and I did not paper over it.** The scope cut dropped the
Lifestyle Boxer Brief 5" (93% Modal Rayon / 7% Elastane) as "Accessories 1"; underwear is in. The
recount offered 191/140 on a corrected 287 basis. I filed **190/139 on the 285 basis** so numerator
and denominator sit on the same style set, and flagged that `styles_total` should be 287 next time
this row is touched. Same shape at Percival and Levi's, where a trunk and a boxer-brief 3-pack left
with the accessories; each numerator is on its own denominator's style set.

**Three cells rose and none is new stretch.** Malbon's high 85 → 89 (four styles carry ≥5%
polyurethane as a minority on the main cloth, and three adidas styles the old parser lost to a
"(100% recycled)" parenthetical actually state 16/12/12% elastane). Outerknown 12 → 13 (the old
main-line 12 was an undercount; like-for-like it falls 15 → 13). Marine Layer's any cell 93 → 95 is
**unreconciled** — no parse fault found, the high cell reproduces the filed 15 exactly, and the
likely cause is coverage; treat that one cell as soft. Scotch & Soda's high 7 → 8 sits inside a
style-key difference.

---

## What I did not do

**Two rows need a re-measure to satisfy the scope ruling and were left exactly as filed**, because
the alternate in the notes is the wrong denominator rather than a partial one:

- **Zegna** — its ready-to-wear tree holds an `underwear-socks` node of 12 styles mixing underwear
  (in) with socks (out), and the only alternate removes all 12. Its notes also claim the removal
  "moves no percentage cell", which is arithmetically false: both of the house's cellulosic styles
  are the modal underwear in that node.
- **Proper Cloth** — "Socks & Underwear" is one combined category of 68, and the split moves
  `natural_pct` between 93 and 94. Scotch & Soda and Brooks Brothers have smaller versions of the
  same problem. **The ruling has no case for a combined category** — it asks for a line those houses'
  own taxonomies do not draw.

**`synthetic_categories` is now truthful but not complete.** 21 rows changed. I rewrote cells that
are *false* under the harmonised rule — `[]` while a category leads, or a swim/underwear leak — and
left cells that are merely *incomplete*, because re-cutting those is a second rule you have not
stated. Thirteen rows name some but not all of their synthetic-led categories; Lululemon is the worst
(six of eighteen). The list is in `notes_categories.txt` and it is a one-edit fix if you want the
column fully recoverable rather than merely truthful. Seven rows your brief listed as "contrast" turn
out to have no synthetic-led category at all, so their `[]` is a measured finding — 82 rows are in
that position and they are enumerated.

**`colourway_ratio` is stale on 44 of the restated rows.** Only Carhartt's notes give a listing count
for the clothing-only cut. It is flagged per row.

---

## Two rulings still want a sentence

**"Named fibre with no percentage" needs the word *fibre* defended.** Your examples all name a
material — leather, deerskin, lambskin, wool. The live cases are **cloth names**: AG's "Robechetto
Rigid Selvage Denim", Wythe's "bedford cord", Percival's "Seersucker". I did not apply the ruling
there, because the spec says in terms that a product type is not a fibre and a fabric name is not a
composition — but applying it would move AG 92 → 95 natural. "Italian lambskin" and "Bedford cord"
need separating.

**120% Lino triggers both halves of that ruling at once** and I left it. Its Composition panel is
present and **empty** on 8 of 35 styles, and on 6 of those the body prose says "Made from linen" — so
it hits the prose rule and the empty-field carve-out simultaneously. I applied the carve-out; the
other reading is 94/0/0/6, a 17-point move.

Also unsettled and now material: **TravisMathew has 138 clothing styles that name elastane with no
percentage** ("Polyester / Cotton / Elastane Blend" and 36 other strings). Under the widest reading of
ruling 3 its first cell is 578 rather than 440; the high cell is 385 either way. This is
register-wide, not TravisMathew-specific, and the strict figure is filed for comparability.

---

## Field notes worth keeping

- **Unbounded substring matching deletes garments.** `/glove/` removes Buck Mason's "**Glover**all
  Monty Duffle Coat"; `/tie/` removes Les Deux's "**Tie**-Dye AOP SS Shirt"; `/bag/` removes two
  garments whose *colour name* is "Shopping **Bag** Brown". All three carry elastane.
- **Three channels changed in a day.** NN07's `resolve-slug` API is gone (the product is now in
  `window.__INITIAL_STATE__` at `page.data.customAttributes`, camel-cased). johnnie-O's
  `/products.json` now 404s with no `window.Shopify`. Brioni's `compliantComposition` is the literal
  string `"$undefined"` on 158 of 840 styles — truthy, and it silently defeats a `||` fallback.
- **Baracuta's composition is not in its feed at all** — not one of 306 records contains the word
  elastane, so a feed-only read returns 0 for the house, silently.
- **Buck Mason's `pdp_accords.fabric` is now an object**, not a flat string; a pass written for the
  old shape matches 0 of 197 and files the row wholly undisclosed.
- Every recount was calibrated by first reproducing the count on the **old** denominator before
  applying the cut. Eight houses reproduced the filed figure exactly; where they did not — Rhone's
  census reads 548 against 529, Les Deux's 68/33 against 75/30 — the cell was taken on the filed
  basis by subtraction and both figures recorded rather than silently replaced.

`menswear_spectrum.html` untouched. No scoring anywhere.
