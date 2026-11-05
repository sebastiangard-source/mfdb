# NOTE - stockists_assembly_2026-11-05 (Assembly Showroom, Hingham)

## 1. Shop check (returned first)

- **Shop's own site:** https://assemblyshowroom.com/ - confirmed. Footer, "Locations + Hours":
  - **ASSEMBLY Hers, 88 North St., Hingham, MA 02043** - Mon-Sat 10-5, Sun by chance - 781.741.0262
  - **ASSEMBLY His, 24 North St., Hingham, MA 02043** - Mon-Sat 11-5, Sun by chance - 781.741.0236
- **The brief is wrong on one point:** 88 North St. is the women's door. The men's door is 24 North St. The brand pages' single address is the Hers door. ZIP 02043 comes from the site.
- **other_doors:** 24 North St. (above). The Hingham Anchor (May 2021) also reports Cohasset (3 South Main, opened June 2020) and Duxbury Marketplace (opened May 2021). Neither is on the shop's current site. Status today: **NC**. A Cohasset "Assembly" directory listing (3 S. Main) calls itself a home-furnishings showroom, which may be a different business; unverified. No home or kids shop found.
- The Anchor (July 2026) says holly & olive, a separate homegoods shop, moved in next to Hers at 88 North St. in spring 2026. It is a different business, not a door.
- **Suggest:** a second record for 24 North St. (His). The map currently shows one door.

## 2. Full record
See `return.csv`. Confidence is **Medium**.

- **Brand list source:** the shop's Designers page (/pages/vendors). It shows 18 entries; Citizens of Humanity and Velvet each appear twice (women's and men's), so 16 distinct brands. The page's markup holds 3 more links with no visible text (Marissa Webb, Mikoh, Organic by John Patrick); I left them out as not displayed.
- **Reconcile (Designers list):** 16 in, 7 matched, 1 rewrite (Paige -> PAIGE, applied), 9 no match.
  - Matched: AGOLDE; Citizens of Humanity; Closed; Hiroshi Kato; PAIGE; Rails; Save Khaki United.
  - Unmatched: Bembien; Demylee; Donni.; Frēda Salvador; LNA; Nation LTD.; Saint Art; The Great.; Velvet by Graham & Spencer (Velvet Mens is the same brand).
- **Save Khaki United:** yes (Designers page and store vendor list). **Mollusk:** no, on both. The online store has 349 products, none from Mollusk. This does not overrule Mollusk's own page, but the link may be stale.

### Decision for Sebastian: the Designers page is thin
The About page says "the list is long", and the Designers page is a fraction of it. The online store's vendor field shows 43 vendors (349 products read from /products.json, public, read-only). Following the brief, I used the Designers page. Using the store's list instead would raise the match count from 7 to 17:
AGOLDE; American Trench; Billy Reid; Citizens of Humanity; Closed; Faherty; Hiroshi Kato; Katin; Marine Layer; NN07 (store writes NN.07, rewrite applied); Oliver Spencer; PAIGE; Paul Smith; Rails; Save Khaki United; Taylor Stitch; Theory.
Store-list names with no match (23): Asher; Astr the Label; Bellroy; Bembien; Cuisse de Grenouille; Demylee; Donni; Ela Rae NYC; Forte Forte; Freda Salvador; Fulton & Roark; Jungmaven; LNA; Nat + Noor; Nation LTD; P.F. Candle Co.; Rye51; Sol Angeles; Standard Rec; Saint Art; The Great; Upstate Stock; Velvet by Graham & Spencer.
The store also lists "ASSEMBLY" (own label), left out of all counts. Store vendors reflect products currently listed online, so it is a snapshot, not a brand roster. Your ruling decides which list goes in.

## 3. Contradictions and brief problems
- 88 North St. = Hers only (see above); the brief treats it as the whole shop.
- Hingham Anchor July 2026 says "nearly 10 years" and also "8 year anniversary"; the shop's About page and the Anchor's 2021 piece both say 2018. I used 2018.
- Boston Magazine lists 781-740-1421; the shop's site lists 781.741.0236 / .0262. The site's numbers are used.
- The Anchor piece's byline and page metadata name different authors; the byline is not used anywhere in the record.
- Boston Magazine does not name the owner as such; the Anchor Q&A names Matt Gallagher as owner and Evan (surname Shuman in the July 2026 piece). "Independent" is my reading; no outlet uses the word.
- The brief says Boston Magazine and the Anchor can carry founding facts; Boston Magazine gives none beyond "three South Shore locations".

## 4. Not reached
No bot walls hit. Not checked: Cohasset and Duxbury status today, Instagram (out of scope), Mollusk's and SKU's pages.

## 5. Sources
- https://assemblyshowroom.com/ ; /pages/about-us ; /pages/vendors ; /products.json
- https://www.hinghamanchor.com/from-denim-to-dinner-parties-meet-this-downtown-hingham-boutique-duo-2/
- https://www.hinghamanchor.com/?p=25684
- https://bostonmagazine.com/best-of-boston-archive/2021/assembly-showroom/
