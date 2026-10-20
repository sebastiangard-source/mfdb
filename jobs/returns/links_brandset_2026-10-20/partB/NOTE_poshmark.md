# Poshmark — NOTE

**Part B, site 4 · checked 20 Oct 2026 · about 25 minutes**

## Method
1. **Directory.** Opened https://poshmark.com/brands once. It is a single page holding all 29,893 brand links in the form `/brand/<Name>`. I matched the worklist against it and went through the misses by hand.
2. **Women's pages.** Every brand URL is built as `/brand/<Name exactly as linked>-Women`. Poshmark is strict about the name:
   - `Adam_Lippes-Women` shows "No listings found".
   - `Adam%20Lippes-Women`, the name exactly as the directory links it, has listings.
   - So every slug is copied verbatim from the directory link, including its case, spaces, `.`, `&`, `+` and the curly apostrophe in `Joe’S`.
3. **Listings check.** Loaded each of the 452 women's pages (one every ~2 s, page HTML only, stopped reading once the result was known) and checked whether it shows listings or "No listings found". No walls.
   - 16 menswear brands had no women's listings. For those I checked `-Men`; all 16 have listings, so the **men's page is given**, with a note: J.Press, Merz b. Schwanen, State & Liberty, Awake NY, Boggi Milano, Carmina, Cesare Attolini, Freenote Cloth, Frescobol Carioca, John Lobb, Meermin, Mizzen+Main, Nanamica, Sid Mashburn, Turnbull & Asser, Visvim.

## Result (464 rows)
- 434 `exact`, 18 `alias`, 11 `NONE`, 1 `NC`.
- `listings` is `ND` throughout: Poshmark brand pages show no item count.

## Flags
- **RÙADH:** in the directory as "RUADH", but both the women's and all-gender pages show "No listings found". `listings=0`; I recommend not showing it.
- **AFLALO is `NC`:** only "YaYa Aflalo" is listed. It may be the designer's earlier label but I couldn't confirm that.
- **MAISON MAYLE is `NONE`:** only "Mayle" (Jane Mayle's earlier label) is listed, and it wasn't folded in.
- **Sister lines kept apart:**
  - RRL → "Ralph Lauren Double RL"; RLX → "RLX Ralph Lauren"; neither folded into Polo Ralph Lauren.
  - Maison Margiela → "Maison Martin Margiela"; MM6 is separate.
  - McQueen → Alexander McQueen; McQ is separate.
- **Other aliases:** Frame → "Frame Denim" (there is no plain FRAME entry) · Lululemon → "lululemon athletica" · Kate Spade New York → "kate spade" · Lafayette 148 → "Lafayette 148 New York" · AG → "Ag Adriano Goldschmied" · Bulgari → BVLGARI · On → "On Running".
- **Duplicate entries:** where the directory has two spellings, I took the one matching the brand's own styling: CHANEL, J._McLaughlin, Lilysilk, NN07, R13, Suitsupply, Tod's, White_House_Black_Market.
- **Joe's and Joe's Jeans** are separate Poshmark entries ("Joe’S" and "Joe's Jeans") and map one each.
- **Same-name risk:** Poshmark brand tags are entered by sellers, so generic names will mix in other labels. Flagged in `note`: Theory, Reiss, Still Here, CO, Sea, Purple, Represent, Elan, Rowan, Jordan, Express, Soma, Camilla, Bode, Palace, Eton, Rains, Vince, Kith, TWP, Greyson, Graff, ARGENT, Toccin, Terez.
- **`NONE`** (not in the 29,893-brand list): Aztech Mountain ("Aztec" is different), Deus Ex Machina, Evan Kinori, Goldwin, GRACE LING, Lady White Co., MAISON MAYLE, Pilgrim Surf + Supply ("Pilgrim" is different), Suzie Kondi, Veronica de Piante, Wiederhoeft.
