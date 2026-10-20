# Vinted — NOTE

**Part B, site 5 · checked 20 Oct 2026 · about 45 minutes**

## Method
1. **The swap.** For every on-file link I built the women's URL with the same `brand_ids`:
   `https://www.vinted.com/catalog?catalog[]=1904&brand_ids[]=<id>`.
2. **Checked every link, not just five.** The brief asked for the swap to be tested on five brands first. Instead I loaded every one of the 431 brand-ID sets, one every ~2.2 s. On each page I read:
   - the **brand chip** (the name Vinted shows for that ID), which confirms the ID is the right brand;
   - the **"N results"** line;
   - the **Women** catalog chip.
   That covers the five-brand check and the rest.
3. **Brands with nothing on file, or a bad link on file.** I typed each name into the catalog's **Brand filter** box (the ordinary UI) and read the IDs off the result list. That was 122 brands. Each ID found was then checked the same way as in step 2.

No walls on Vinted. I declined non-essential cookies.

## Result (464 rows)
- 408 `exact`, 22 `alias`, 33 `NONE`, 1 `NC`. All links are `url_kind=brand_filter`.
- `listings` is Vinted's results line. It caps at "500+".

## What the record got wrong
- **Not "most are men's".** Of the 352 on-file links, 180 were men's (`catalog[]=5`), 169 were already women's (`1904`), and 3 were in other formats.
- **10 on-file links were keyword searches** (`search_text=`), not brand filters:
  - Vans now has its brand ID (139).
  - Indochino, Mack Weldon, Mizzen+Main, Patrick James, Proper Cloth, RLX, Sid Mashburn and State & Liberty have no Vinted brand. They are `NONE`, and the searches were not kept.
- **Bogner's on-file link** (`/brand/bogner`) opens an unfiltered page of random items. It is replaced with ID 99868 (Bogner, 325 women's results).
- **Sister lines were folded into some on-file IDs.** I took them out, and re-read those pages for counts:
  - Comme des Garçons: had Homme, Homme Plus and Play → main line only (56974).
  - Maison Margiela: had MM6 → 639289 only.
  - Diffusion lines removed: M Missoni, PS Paul Smith, Y's by Yohji Yamamoto, Z Zegna, Versace Collection, Diesel Black Gold.
- **Alternate spellings of one label were kept together**, since the multi-ID filter shows them all: Dior + Christian Dior, Valentino + Valentino Garavani, Bvlgari + Bulgari, Saint Laurent + Yves Saint Laurent, Ferragamo + Salvatore Ferragamo.
- **Brand-family IDs are also kept** as they were on file: Burberry (with Brit, London, Prorsum), Barbour, BOSS, Levi's, Lacoste, Moncler. Prune these too if the card should show the main line only.
- **MAISON MAYLE is `NC`.** The on-file ID resolves to "Mayle", Jane Mayle's earlier label. It was not folded in.

## Flags
- **Luca Faloni:** the women's catalog shows no results; all 6 listings are under Men, so the men's link is given.
- **Palace:** linked to "Palace Skateboards" (222038, 3 results). The generic "Palace" brand (139960, 47 results) probably mixes in other labels and was left out.
- **Women's counts of 5 or under** (mostly menswear houses): Fusalp 1, Merz b. Schwanen 1, Boglioli 1, Turnbull & Asser 1, Cesare Attolini 1, Frescobol Carioca 1, Stefano Ricci 2, RÙADH 2, Meermin 3, Rodd & Gunn 3, Boggi Milano 3, Piaget 3, Drake's 3, Visvim 4, Goldwin 4, Kallmeyer 4, Orlebar Brown 5, Isaia 5, Aztech Mountain 5, Markarian 5.
  - The brief says to give the women's page wherever the women's side has stock, so these stay women's. Switch to `catalog[]=5` if the card should show depth instead.
- **Same-name risk** (category not checked; noted in rows): Rowan, Elan, Theory, Reiss, Still Here, Sea, Purple, Represent, Jordan, Express, Soma, Camilla, Bode, Eton, Rains, Vince, Kith, TWP, Greyson, Graff, ARGENT, MOTHER, Frame, HATCH Collection, Aether Apparel, On.
- **`NONE`** (no match in Vinted's brand filter): AFLALO, Carmina, CO, Danielle Frankel, Evan Kinori, Extreme Cashmere, Freenote Cloth, GRACE LING, Imogene + Willie, Indochino, John Lobb, Kiel James Patrick, Lady White Co., Mack Weldon, Mizzen+Main, Mollusk, Nanamica, Patrick James, Pilgrim Surf + Supply, Proper Cloth, RLX, Sid Mashburn, State & Liberty, Veronica de Piante, Wiederhoeft, Aurate, Blue Nile, Brilliant Earth, Catbird, Gorjana, Harry Winston, Jennifer Fisher, Warby Parker.
