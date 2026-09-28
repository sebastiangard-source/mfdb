# Change requests — logged, not acted on

## CR-1 · 20 Sep 2026 · Drop the "1 =" / "5 =" scale anchors from the dial tooltips
Requested by Sebastian. The rail tooltips currently end with scale anchors ("5 = built on engineered
fabric", "1 = a trace", "5 = the maker and the brand are the same thing"). Remove the numeric anchors
from every dial tooltip; keep the prose definition. Applies to all 35 dials. The anchors can stay in
`rubric.json`, which the brand page and the rubric screens read; only the tooltip text changes.
State: done, v3.22.0 (23 Sep) — anchors removed and every tooltip cut to one or two sentences.

## CR-2 · 23 Sep 2026 · Reach screen
Reach has never been audited: 203 scores, a definition written 21 Sep, 34 brands at 4. The definition
rests on things the map already holds — own US doors, independent stockists on the register,
department-store channel, online-only — so a screen can propose the whole dial mechanically and
Sebastian rules on the exceptions. Queue after the tech re-score. State: closed 28 Sep 2026 — reach replaced by Own stores, derived from the door count; no screen needed.

## CR-3 · 26 Sep 2026 · Cotton dial screen
The cotton dial is authored and unaudited, and its 5s mix two readings: houses built on a named
cotton programme (Sunspel, Merz b. Schwanen, Proper Cloth, Charvet, Stefan Brandt) and houses that
simply sell a lot of cotton (A Bathing Ape, Hackett, Duck Head). The fibre pass now measures the
second reading — share of cotton-led styles, 198 brands — so the dial should mean only the first:
a named fibre or signature cloth the reputation rests on. Screen: take the measured share as the
floor, then a short read for the named-programme step. Queue after reach (CR-2). State: logged.

## CR-4 · 27 Sep 2026 · White-tee read
The white-tee dial is seeded (169 brands at 2 on "sells a tee", 13 at 3, 8 at 4, 6 at 5). A read would
settle steps 2-4 for each brand: is there a plain white tee, is it a named product with its own cloth
or cut, is it a signature. Evidence is on the brand's own tee listing, which garment_links already
holds for 193 brands. Queue with the price_full return, which reads the tee anyway. State: logged.

## CR-5 · 28 Sep 2026 · Logo read
The logo dial is seeded by hand (all 204). A read would count, per brand, the share of men's styles with a
visible mark and the size class of the mark (none / small / large / all-over), from the brand's own product
photos — the fibre pass method applied to branding. Queue AHEAD of the white-tee read (ruled 28 Sep): the logo dial is the one where a wrong score is most visible. State: logged.
