# Depop — NOTE

**Part B, site 3 · checked 20 Oct 2026 · about 35 minutes (mostly the count pass)**

## Method
1. **Directory.** Read the Brands A–Z on 27 letter pages, `/brands/a-z/a/` through `/z/` plus `/other/`. That gave 21,729 unique brand links of the form `/brands/<slug>/`. I matched the worklist against them, then went through every miss by hand.
2. **Women's page and count.** For each of the 446 brands found, I opened the women's brand page, `/brands/<slug>/c/womens/`, one page at a time at about one every 2–5 seconds. From each I read the header count, e.g. "(40.3K results)", and the H1, e.g. "Women's Gucci". This also confirms that every link resolves to the right brand.
   - No walls on Depop.
   - The pages were loaded in a hidden frame inside the Depop tab and read from the rendered page. No API calls were made.

## Result (464 rows)
- 422 `exact`, 24 `alias`, 18 `NONE`.
- `listings` is Depop's own rounded header figure (K = thousands, M = millions).
- Every matched brand has a women's page with a count, so no row needed a men's-page fallback.
  - Alden (316) and Allen Edmonds (171) are menswear houses but still show women's results. Those are probably seller tagging.

## Flags
- **LoveShackFancy shows 0 results**, on both the women's page and the all-gender page. The brand entry exists but the link leads to an empty page. I recommend not showing it.
- **Missoma:** on the first pass the frame briefly showed Mejuri's page. I re-opened it directly: `/brands/missoma/c/womens/`, 75 results. The row is correct.
- **Joe's and Joe's Jeans** both point to `/brands/joe-s-jeans/`, the only Joe's Jeans entry.
- **AG:** Depop has both "AG Adriano Goldschmied" and "AG Jeans" (`/brands/ag-jeans/`). I linked the first.
- **Saint Laurent → "Saint Laurent Paris".** A separate "Yves Saint Laurent" entry exists and was not merged.
- **Sister lines kept apart:**
  - RRL → "RRL by Ralph Lauren"; RLX → "RLX Ralph Lauren"; neither folded into Polo Ralph Lauren.
  - Carhartt and Carhartt WIP are separate entries.
  - McQueen → Alexander McQueen; McQ not folded in.
  - Lacoste, Lululemon, Patagonia and Reformation also have "-plus" entries. I linked the main entry.
- **Very small counts** (under 20, so possibly mis-tagged listings): Redvanly 2, Cesare Attolini 4, Indochino 4, Patrick James 4, Harry Winston 4, Luca Faloni 7, Brilliant Earth 9, Piaget 9, Freenote Cloth 10, John Lobb 10, Merz b. Schwanen 11, Meermin 15, Sid Mashburn 17, Turnbull & Asser 18, Berluti 19.
- **Same-name brands not checked by category** (Depop brand tags are typed by sellers): On (On Running), Theory, Reiss, Still Here, CO, Sea, Purple (Purple Brand), Represent, Elan, Jordan, Express, Soma, Frame, Camilla, Bode, Palace, Eton, Rains, Vince, Kith, Greyson, Goldwin, Graff.
- **NONE** means the brand is not in the A–Z: AFLALO, Another Tomorrow, ARGENT, Danielle Frankel, Jamie Haller, KALLMEYER, Kiel James Patrick, Markarian, Mestiza New York, Rowan ("Rena Rowan" is a different brand), RÙADH, State & Liberty ("STATE" is a different brand), TWP, Veronica de Piante, Wiederhoeft, Aurate, Blue Nile, Jennifer Fisher.
