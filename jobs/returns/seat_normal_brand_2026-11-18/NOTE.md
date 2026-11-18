# The Normal Brand — first seating evidence (read 18 Nov 2026)

Seat: `seat_normal_brand_2026-11-18`. I gather and propose; Sebastian rules. Men's range only. Band is not computed here. `reconcile.py`: "The Normal Brand" matches a canonical key exactly.

## 1. What it is (ownership and origin, first)
- **Brand's own words** (https://thenormalbrand.com/pages/our-story): "BUILT BY BROTHERS… We aren't designers. We're brothers who make clothes. Headquartered in St. Louis." Home page: "Family-Owned - St. Louis Based."
- **Founded 2015, St. Louis, Missouri.** Jimmy worked in finance, quit and moved into his parents' basement to work on the first Normal shirt; Lan joined summer 2015; Conrad full-time in 2016 after law school. First store 2019. 2025 added a Legacy Collection (premium line).
- **Which family:** Sansone — from the brand's press page ("Jimmy Sansone, brother and co-owner") and press (St. Louis Magazine, Kansas City Magazine, KSDK) naming Jimmy, Lan and Conrad Sansone as running it. The story page itself does not give the surname.
- **Which company:** Normal Brand, LLC, 911 Washington, Suite 814, St. Louis MO 63101, owner of USPTO marks THE NORMAL BRAND and PUREMESO (reg. 5287278, 12 Sep 2017). This is from trademark directories, **not the brand's own pages**. A Glossy podcast summary (press) says it has no outside funding; early grant money reported (Arch Grant 2015, about $50K).
- **Men's range:** 165 casual, comfort-first styles — Puremeso and Comfort Terry jersey/terry tees, polos, button-ups, flannels, knits, jackets, shorts, a few leather/wool pieces. No shoes (none among 719 products). Not closed.

## 2. US presence
- **11 own stores** (live Our Stores page, each with a 200 store page): Denver CO, Indianapolis IN, West Des Moines IA, Kansas City, Des Peres, Springfield, Clayton, Kirkwood MO, Nashville and Franklin TN, Southlake TX. No partner shops or concessions stated. See `own_doors.csv`.
- **Not settled:** the story page's opening list adds up to 13. The Retailer Locator also holds own-brand rows for **Mall of America (Bloomington MN)** and **Birmingham AL (The Summit)**, neither on the live Our Stores page. A press article says MOA will close "next month" (date unconfirmed); Birmingham opened June 2023 and a search snippet still showed it, so it is probably closed or delisted. Neither is counted; both are in `own_doors.csv` marked unverified. A phone call settles it. The Clayton store reportedly started as a pop-up; it is listed as permanent now.
- **Retailer Locator** (Secomapp widget, data read from the page): 946 rows = 11 own-brand + 935 retailers (897 US across 49 states, no HI or DC, about 751 distinct names; 36 Canada; 2 elsewhere). Rows carry no product data, so men's items are not shown. Only the **first 25 are in `stockists.csv`** (truncated, as the brief allows); `shop_kind` not checked (NC). The locator's "Dillards" rows are junk (PO Box HQ and an all-zero row) and are not stores.
- Department stores Dillard's and Nordstrom (men's brand pages) and Target Plus were seen only as search results; pages not opened (retailer evidence, low). Von Maur is press-only.
- **Shipping:** free over $150 on US orders; the cost below that is not published (checkout only; nothing added to cart). Ships to Canada, Australia and the UK, buyer pays duties, 8-20 business days. Store is own US site, USD.

## 3. Census, prices, tech/craft, dials
- **Census:** 165 men's styles (420 colourway listings), method title_dedup. Scope = `/collections/mens` plus products carrying clean men's tags; 138 are in the men's collection and 27 are tagged men's only (flagged in each row's note, with available/sold-out). Tags are contaminated (some women's items carry men's tags), hence the collection check. Lead-fibre split of 162 with composition: natural 130 (80%), synthetic 25 (15%), cellulosic 7 (4%); 3 ND (Everyday Canvas Chore Coat, Button Front Trunk, Apollo Trunk). Shape: one. Two named lines of 5+ styles: Puremeso 13, Comfort Terry 11 (no `return_lines.csv` requested in this brief).
- **Prices** (full price, USD, all `range`): tee $38-$78; polo $68-$128; dress shirt (casual button-ups only) $88-$128; jeans $128-$148; dress pants (casual pants/chinos) $128-$148; sweater $78-$248; outerwear $158-$698; shoes NONE. Excluded: Robles Knit Jacquard Polo (clearance; compare-at $138 vs $118 inconsistent; now $79).
- **Tech/craft:** named fabrics Puremeso (owned, trademarked), Comfort Terry, COOLMAX (licensed), Seawool, Texstretch, Comfortech, Tencel. No owned facility, named maker, named mill or made-in statement found. Proposed craft 1 (reasoning in `return.csv`). `proposed_tech` is NC: the package has no tech scale.
- **Dials:** 38 rows. Many are scored from the garments at low confidence; shoes 0, boat 0, racquet 0, sail NA. Keyword counts in the evidence are counts on product-page text, not hand-verified. Dry-clean mentions (60) were not split into "dry clean only" vs "do not dry clean".
- **Quote:** from the brand's own story page, "Life in the middle" block.
- **Resale:** Vinted has no brand entry (Brand filter "not found" twice on 2026-11-18); free-text search gives 500+ results (link in `return.csv`); brand id NONE. Grailed: `/designers/the-normal-brand` redirects to the index and the A-Z list has no entry: NONE.
- **Lookbook:** `/pages/lookbook` and variants are 404 (NONE). B Corp / GOTS: no evidence found (NONE).

## 4. Could not settle / doesn't belong
- Mall of America and Birmingham status (above).
- Founding year: the brand says 2015; an Olin blog post says 2014. 2015 used.
- `return.csv` has one data row (the brief says "header only" for the missing mark column; I read it as the template's columns minus `mark_as_written`).
- Men's listing URLs were checked for women's tags, not tile by tile; `/collections/bottoms` is a parent category (includes shorts). The site search also shows women's items.
- Not read: women's lines (out of scope). Retailer pages for Dillard's, Nordstrom, Target.
- **Agent-directed instructions:** none found on the pages read.
- **Tool notes:** one direct Vinted API fetch was refused by the tool's permission check; I did not work around it and used the visible Brand filter instead. The shell could not reach the brand site; everything was read in the browser. No pop-ups, security alerts or redirects to report beyond the Grailed designer redirect.
