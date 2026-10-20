# links_trr_2026-10-20 — NOTE

**The RealReal · checked 20 Oct 2026 · about 50 minutes · 178 rows**

## Result
- 42 `exact`, 5 `alias`, 4 `NONE`, 127 `NC`.
- Every linked page except one (Ami Paris) was opened. For each, I confirmed the H1 names the brand and took the item count from the header.

## Pages read
1. **Men directory** (`/designers/men`): 2,775 entries. It loaded with no check.
2. **Fine Jewelry directory** (`/designers/fine-jewelry`): the press-and-hold check appeared. Sebastian cleared it, and I read all 2,803 entries.
3. **Watches directory** (`/designers/watches`): 240 entries.
4. **Kids and Home:** skipped. No worklist brand plainly belongs there.
5. **Brand pages:** 44 opened for counts.
   - That covers 30 brands from the Men directory, 11 from Fine Jewelry, 2 from Watches, and Bulgari.
   - The check reappeared once on Monica Vinader. Sebastian cleared it and the rest were read.
6. **Search for the 134 brands still missing.**
   - I used TRR's own search (`/products?keywords=`), which is what the search box submits to, for 11 brands.
   - The check then returned on the next page load and I stopped there. The rest are `NC`.

## What the brief got wrong
- **The directories are not complete.**
  - `/designers/asics/men` is a real page ("Asics Men", 92 items), yet Asics is in no directory.
  - The same goes for `/designers/brooks-brothers/women` ("Brooks Brothers Women", 1 item).
  - So "not in any directory" does not mean TRR lacks the brand. The 127 `NC` rows should not be turned into `NONE` on directory evidence.
  - A slug that doesn't exist falls back to the generic "Women" page (2.6M items). That makes a direct page check reliable: a real hit has an H1 that starts with the brand name.
- **TRR's search does not return designer pages.** Choosing a suggestion, or pressing Enter, lands on a keyword results page. It shows the designer label on every item, but never links to a designer page.
  - So "look for a designer result" isn't something the search box can do.
  - What it can show is whether items under that label exist. I recorded that in `note`.
- **Ami Paris was missed by the first pass.** The Women directory lists it as "AMI Alexandre Mattiussi" and also as "AMI".
  - Search for "Ami Paris" returned 1,857 items, mostly under those two labels.
  - It's given as an alias, but the page wasn't opened, so verify it first.
- **Nike's main line is in the Men directory only.** The Women directory carries Nike collaborations alone, so the Nike link goes to the men's page.

## Flags
- **Bulgari:** `/designers/bvlgari/women` is confirmed ("Bvlgari Women", 1,128 items).
- **Men's pages given** (listed under Men only), each noted in its row:
  - 120% Lino, Alden, Allen Edmonds, Ariat, Awake NY, Evan Kinori, Freenote Cloth, Frescobol Carioca, G/FORE, Greyson
  - Indochino, John Lobb, Lady White Co., Nanamica, Nike, NN07, Pilgrim Surf + Supply, Proper Cloth, Represent, Roark
  - Sid Mashburn, Suitsupply, Sunspel, Taylor Stitch, Todd Snyder, Undefeated, Persol, plus the three aliases below
- **Aliases:** Malbon → Malbon Golf · Purple → Purple Brand · Palace → Palace Skateboards · Bulgari → Bvlgari · Ami Paris → AMI Alexandre Mattiussi.
- **Same-name checks:**
  - Represent: items are Represent streetwear.
  - Purple: the entry is Purple Brand.
  - Rowan and Elan: unresolved (`NC`).
- **Pages to check before showing:**
  - Asics: the women's page wasn't checked.
  - Brooks Brothers: the women's page has 1 item. Search found 15 Brooks Brothers items, so the men's page probably holds most of them.
- **`NONE` (4):** Aerie and Athleta (search returned 0 items), Altar'd State and Aritzia (search results carried none of their labels).
- **Items exist but no URL** (search-only evidence, `NC` with the evidence in `note`): 7 For All Mankind, Abercrombie & Fitch, adidas, AG (labeled "Adriano Goldschmied"), Anthropologie.

## To finish the 127 `NC` rows
Open `/designers/<slug>/women` for each, falling back to `/men`. That's about 130–260 page loads, and at the rate TRR is challenging now, it means clearing the check every few pages. Best done by hand, or in short sessions spread over time.
