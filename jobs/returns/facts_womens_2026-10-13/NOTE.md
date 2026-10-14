# facts_womens_2026-10-13 — full return, read 13–14 October 2026

All 180 brands are in `return.csv`, in worklist order. `reconcile.py` gives 180 exact, 0 to rewrite, 0 unmatched. No cell is empty. Every quotation is 6–30 words and every `what_it_sells` is under 30 words.

- **Status:** 168 `read`, 12 `partial`.
- **Partial rows:** Brandy Melville, NIC+ZOE, Roller Rabbit, ViX Paula Hermanny, GUEST IN RESIDENCE, Cozy Earth, Roger Vivier, Danielle Frankel, HATCH Collection, PatBO, Diane von Furstenberg and Reem Acra. Most are partial because the owner is unknown.
- **Unknowns:** 16 `NC` cells across the file.
- **Batch notes:** each `facts_womens_batchN/NOTE.md` holds the detail for its ten brands. This note collects what matters for the merge.

## Changes to the record (check before merge)

- **Marc Jacobs.** LVMH sold it. The IP is now in a WHP Global / G-III 50/50 joint venture, and G-III's 8-K of 2026-09-02 reports the deal closed.
- **GUESS.** Taken private on 2026-01-23. Authentic Brands holds 51% of the IP, the Form 15 was filed in February 2026, and there is no ticker now.
- **Stella McCartney.** She bought back LVMH's minority stake in 2025.
- **Roger Vivier.** Its owner, Tod's, was delisted in 2024 after an L Catterton vehicle took control.
- **Gianvito Rossi.** Richemont has held a controlling stake since 2023.
- **Carolina Herrera.** Owned by Puig. Puig–Estée Lauder merger talks were confirmed in March 2026 and no deal was reached as of April. Re-check before merge.
- **HANRO.** Owned by HUBER Holding AG, not Delta Galil.
- **St. John and Wolford.** Both are owned by Lanvin Group.
- **Salt Life.** Iconix bought it out of Delta Apparel's Chapter 11. Press says all 28 stores closed in 2024, and the site lists one new store (Sanibel Island). **The doors register should be checked.**
- **Sanctuary.** Its `O` rests on one store, the Beverly Hills flagship opened in February 2026.
- **O'Neill.** The US licensee exits after Fall/Holiday 2027.

## Certifications

**B Corp (14 yes).** All 14 were confirmed on the brand's B Lab profile:

- Athleta
- Eileen Fisher
- Rip Curl, certified as KMD Brands Limited
- Cotopaxi
- Ganni
- Chloé
- ba&sh
- DÔEN
- FARM Rio, certified via its parent Grupo Azzas 2154
- Camilla
- TOTEME
- Good American
- Another Tomorrow
- RÙADH

The pre-done `pucci` hit was a Costa Rican publisher, so Pucci is `no`.

**Gap: parents of batches 1–5 were not searched.** The 180-name search missed two brands certified under a parent (Rip Curl, FARM Rio). Batches 6–18 searched parent names; batches 1–5 did not. **Rows 1–50 could still have a missed parent certification.**

**GOTS (3 yes):** Aritzia (ARITZIA LP), Maje (MAJE SAS) and TOTEME (TOTEME AB). Lilysilk claims GOTS fabrics on its site, but neither its name nor its operating company's name is in the database, so it is `no`.

## Method changes during the job

- **Vinted.** Vinted's brand API stopped returning data partway through the job (first HTML, then 403). Every id was verified by loading the filtered women's catalogue (`catalog[]=1904`). The pre-done "none" list was often wrong; ids were found for LAPOINTE, Sea, Terez, Toccin, Suzie Kondi and others. **Batches 2–12 relied more on that list.** About 12 brands remain `NONE`, and the ones in early batches are worth a second look.
- **The RealReal.** On 2026-10-14, after Sebastian passed TRR's Press & Hold check in his own browser, every brand's designer URL was opened. A link counts only if the page carries the brand's own title.
  - **Found:** 25 brands that were missing from the 13 Oct index have pages (LOFT, Talbots, Eileen Fisher, Good American, Sam Edelman and others).
  - **Removed:** AFLALO, which had a link from the index; its URL opens no brand page.
  - **`NONE` (27 brands):** the brand's URL guesses opened no brand page. These are mostly mass or mall labels: Chico's, J.Jill, Soma, Athleta, Aerie, Free People, prAna, Jockey, Wacoal, Hurley, NYDJ and others.
- **Mixed Vinted ids.** Some ids also catch unrelated labels: Soma, Camilla, Elan, ARGENT (silver jewelry), Still Here and Róhe. Each `note` says so.

## Rulings needed (collected from all batches)

1. **Lookbooks.** Season-named shopping or "edit" pages, and dated digital catalogs, were counted as lookbooks, following the brief ("a collection page with a season name counts"). About 141 rows are `yes`. Several are judgment calls, and their notes say so:
   - pages with no season name: Veronica de Piante "Collection Eight", Sanderlak "Collection II", Camilla "Paris 2026", ViX "Afterlight";
   - nav-only season labels: Alexander Wang, B SIDES, Ciao Lucia, EB Denim;
   - a monthly collection: M.M.LaFleur.

   If the rule should be editorial or runway pages only, roughly 40 rows flip to `no`.
2. **Owner from the site's terms.** Where no ownership press exists, `owner_today` is the operating company named in the site's terms or legal notice, flagged in `note`. About 75 rows cite site terms in `note`, mostly for this. The alternative is `NC`.
3. **Founding facts from a journalist.** Some founding years and places come from a journalist's own wording rather than a quote from the brand: EDIKTED, Rains, R13, Reem Acra, Róhe, RIXO, Sea, Sanderlak, Veronica de Piante, La Ligne, Danielle Frankel, Altar'd State and others. Keep them, or set them to `np`?
4. **Founding place.** "Based in X" was written as `np`. Launch wording such as "debuted at NYFW" or "LA-based collective" was accepted. Please confirm.
5. **Signature products.** About 25 rows give a line rather than one style (e.g. Wearever, Travelers™, DoubleSoft®, CozyChic®, Fits Everybody). Some signatures are not women's clothing: Cotopaxi's pack, Rip Curl's and O'Neill's wetsuits, Cozy Earth's sheets, Vilebrequin's men's swim trunk.
6. **Pronunciation.** Only brand-sourced pronunciations were entered, plus a few well-known ones flagged "not sourced" (ERES, Khaite). Lhuillier, Aquazzura and Vivier are `NONE`.
7. **Sister banners.** MICHAEL Michael Kors was kept separate from Michael Kors. If it should be merged, the Michael Kors signature becomes the Hamilton bag and Vinted id 981100 is added.
8. **Belong on a women's list?** Kartik Research (its women's collection was empty when read) and Sanderlak (launched as menswear) may not belong on a women's list.
9. **Thin channel evidence:**
   - `D` rests on a single Nordstrom or Saks item for ba&sh and MONSE.
   - `I` rests on one trunk-show entry for Wiederhoeft.
   - Reem Acra's `W` was dropped because its shop shows 0 products and gowns are made to order.

## Not reached

- **LOFT, Sam Edelman and Athleta were re-read on 14 October.** The bot checks had cleared, and all three are now `read`. The Athleta lookbook is "THE LOOKBOOK FALL '26".
- **Owners `NC`:** NIC+ZOE, Roller Rabbit, ViX, GUEST IN RESIDENCE, Cozy Earth, Danielle Frankel, PatBO and Reem Acra.
- **Owner rests on old press:** Diane von Furstenberg (2022), IRO (2016), NYDJ (2013) and Proenza Schouler (2018).
