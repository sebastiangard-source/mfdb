# NOTE — womens_brands_dept_stores_2026-10-10 (full return)

Captured 10 Oct 2026 in Chrome. This return replaces the earlier Nordstrom + Saks pilot. Those two stores were rebuilt from the same captures, so their rows have not changed.

The files are:

- **`return_brands_by_store.csv`**: 16,602 rows, one per brand per store, with no empty cells.
- **`return_brands.csv`**: 2,930 distinct women's-clothing brands. 153 of them are sold only at off-price stores.

## Method

Every list was read from the live page in Chrome and printed back as page text, and the CSVs were built from that text by script. No brand name was retyped by hand.

For each store I read two lists. The **brand index** gives one row per brand. The **brand filter on that store's Women's Clothing listing** decides `womens_clothing` and, where the store shows them, the item counts. A brand that is in the index but has no women's clothing gets `womens_clothing` = `no` and stays in the file. A brand that is in the clothing filter but missing from the index gets a row whose `listed_under` says so.

**Lingerie-only rule.** A brand is `womens_clothing` = `no` when the store files all of its women's clothing under lingerie, bras, panties, shapewear, hosiery or socks. Sleepwear, loungewear, robes, swim and activewear count as clothing. Each `no` row says why in its `note`.

## Per store

| Store | Index read | Index size | Women's clothing brands | Counts? | Tier labels found |
|---|---|---|---|---|---|
| Nordstrom | `/brands-list/women`, plus the Women > Clothing index | 4,563 / 1,905 | 1,829 yes, after 76 lingerie-only | 23 only (site throttled per-brand pages) | `Designer` (Designer > Women > Clothing filter, 158) |
| Saks Fifth Avenue | `/designers` (store-wide; no women-only A–Z exists) | 1,173 | 438 of the 447 in the clothing filter (9 lingerie-only) | yes, all; filter adds up to the page total (29,885) | none exist |
| Bloomingdale's | `/shop/all-designers` (store-wide) | 2,502 | 568 (47 with only lingerie or non-apparel items) | yes, all | `The Designer Boutique` (74) |
| Neiman Marcus | `/c/designers-cat000730` (store-wide) | 1,060 | 415; filter adds up to the page total (25,453) | yes, all | `Designer Collections` (87), see below |
| Bergdorf Goodman | Designer Collections > All Designers (women) | 251 | 246; filter adds up to the page total (9,172) | yes, all | none |
| Macy's | Women > All Brands | 1,537 | 769 (87 with only lingerie or non-apparel items) | yes, all | none found |
| Dillard's | `/c/shopbybrand` (store-wide) | 1,174 | 327 (none lingerie-only) | no; the filter shows none | `Contemporary` (60), `European Designers` (5), `The Coterie Shop` (6) |
| Von Maur | `/Brands.aspx` (store-wide) | 1,559 | 301 of 319 (18 intimates-only) | no; the filter shows none | `Contemporary` (47) |
| Nordstrom Rack | `/brands` (store-wide) | 2,574 | 720 of 742 (22 intimates-only) | no; the filter shows none | `Designer` (82) |
| Saks OFF 5TH | **not reachable** | – | – | – | – |

**Paging.** Every index was a single A–Z page with no paging and no lazy loading. Row counts were checked again after scrolling to the end, except at Bloomingdale's and Macy's, whose filters come from the page's own data.

## What could not be reached

**Saks OFF 5TH.** saksoff5th.com now shows only "SaksOFF5TH.com is Shutting Down", whatever path is requested, so there is no index online to read. The store has one row, all `NC`, with this explained in its `note`. Offline coverage would need another source.

## Indexes that look incomplete, or numbers to treat with care

- **Bloomingdale's and Macy's: brand filters fall short of the page totals.** Bloomingdale's filter adds up to 51,993 items against a page total of 53,084. Macy's adds up to 82,009 against 83,041. The gap is about 2%, either unbranded items or a small cut-off in the filter. The other stores' filters add up exactly.
- **Possible caps on single subcategory filters, used only for the lingerie check.** Nordstrom's Dresses filter returned exactly 1,000 brands. Dillard's Dresses and Tops filters returned exactly 210 each. If those are caps, a brand that sells only dresses plus lingerie could be misjudged. At Dillard's it made no difference, because every brand turned up in some clothing subcategory.
- **Nordstrom's Clothing index changed while I was reading it.** It went from 1,904 to 1,905 entries between reads: `&Daughter` appeared.
- **Nordstrom item counts: 23 captured.** The rest are `NC`, because the site stopped returning product data after about 20 brand pages.
- **The Bloomingdale's index lists six pages twice under two spellings.** For example, `/buy/alc` appears as both "A.L.C." and "ALC". The first spelling is used and the second is in the `note`.

## Results that may look wrong but are what the stores show

- **Rack lingerie rule produced some surprises.** Komarov and Wrangler come out as intimates-only at Nordstrom Rack. That is what the rule gives, flagged "rule-derived". Treat both as worth checking.
- **Wolford (register) differs by store.** It is `yes` at Saks, Neiman Marcus and Bergdorf, and `no` at Nordstrom, Bloomingdale's, Dillard's and Rack, which file it as hosiery or lingerie.
- **Ganni (register)** is `no` at Nordstrom, which has shoes and bags only, and `yes` at five other stores.
- **Tory Burch (register)** has women's clothing only at Nordstrom. At the other seven stores it is shoes, bags or accessories.
- **"Loft"** is on the register and matched a Nordstrom Rack listing called "Loft". I have not checked that it is the Ann Taylor LOFT label.
- **Pre-owned listings (Macy's).** 37 "Pre-Owned <brand>" listings at Macy's have women's clothing. They stay in the by-store file and are left out of `return_brands.csv`, because they are resale, not brands the store buys.

## Merges in `return_brands.csv`

- **Spelling merges.** Names were merged when they differ only in case, accents, punctuation, ®/™, or &/+/and.
- **17 groups go beyond spelling, and each is flagged** "name-variant merge … check" in its `note`:
  - AG / AG Jeans / AG Adriano Goldschmied
  - Joe's / Joe's Jeans
  - Gottex / Gottex Swimwear
  - ViX Paula Hermanny / ViX by Paula Hermanny / Vix
  - Mer St Barth variants
  - Temperley / Temperly
  - La DoubleJ / La DubleJ
  - MM6 Maison Margiela / MM6 Maison Martin Margiela
  - MM by Max Mara / MM Max Mara
  - Rabanne / Paco Rabanne
  - Rene Ruiz / Rene Ruiz Collection
  - Bronx Banco / Bronx and Banco
  - ATM / ATM Anthony Thomas Melillo
  - Isabel Marant Étoile / Etoile Isabel Marant
  - Teri Jon by Rickie Freeman / Rickie Freeman for Teri Jon
  - Kay Unger / Kay Unger New York
  - Elliatt / Elliat
- **Kept separate on purpose.** These pairs are listed as separate brands by the retailers, so they stay apart:
  - DVF and Diane von Furstenberg
  - Valentino and Valentino Garavani
  - Saint Laurent and Yves Saint Laurent
  - McQueen and Alexander McQueen
  - Michael Kors and Michael Kors Collection
  - St. John and St. John Collection
- **`mark_as_written` = `NC` in 348 rows**, where the stores spell a brand differently. I did not check the brands' own sites. The `note` lists each spelling.
- **`brand_site_domain` = `NC` throughout.** No retailer links out to brand sites, and I did not look them up.
- **Sorting.** The file is sorted by `full_price_stores`, then by total stores.
- **Register.** 23 of the 36 register brands have women's clothing at one or more stores. The 13 absent from all of them all run their own chains (Anthropologie, Aritzia, Talbots and others).

## Where each `private_label` value comes from

Every `private_label` = `yes` row carries a `private_label source:` entry in its `note`. None of them now rests on general knowledge.

- **Macy's and Bloomingdale's: Macy's, Inc. Form 10-K** for the fiscal year ended 31 Jan 2026, Item 1 (sec.gov/Archives/edgar/data/794367/000162828026021721/m-20260131.htm). It lists 29 private-label brands for the whole company and does not say which store each belongs to. Matching was exact on the name: Ideology is marked, but Macy's "ID Ideology" is not, and its note says why.
  - "Macy's", and at Bloomingdale's "C by Bloomingdale's Cashmere" and the other "Bloomingdale's"-named labels, are not on the 10-K list. They are marked from the store name only.
- **Nordstrom and Nordstrom Rack:** the Nordstrom Made page.
- **Dillard's:** its Exclusive page, which also includes licensed exclusives. Badgley Mischka is left `no`, because the page lists only the sub-line Belle by Badgley Mischka.
- **Saks, Neiman Marcus, Bergdorf and Von Maur:** the store's name appears in the brand name; nothing more.
- **Saks OFF 5TH:** closed online. The site was read on 10 Oct 2026 and showed only the shutdown notice. This belongs in the register as closed, with that date.

## Where the brief is wrong, or will produce confident wrong answers

1. **Saks has no "Advanced Designer" or "Contemporary" tiers, and Neiman Marcus has no "Designer" tier.** Neiman's nearest equivalent is the "Designer Collections" edit: 87 brands and about 1,460 items. It is a curated edit, not a department, so it is recorded with that warning in each row's `note`. The tiers that do exist are recorded as written: Nordstrom `Designer`, Bloomingdale's `The Designer Boutique`, Dillard's `Contemporary` / `European Designers` / `The Coterie Shop`, Von Maur `Contemporary`, Rack `Designer`.
2. **Most stores have no women-only brand index.** Only Nordstrom, Macy's and Bergdorf do. Elsewhere the A–Z covers the whole store, and the women's clothing brand filter is the real source.
3. **Per-brand item counts.** These are free where the store's filter shows them: Saks, Bloomingdale's, Neiman Marcus, Bergdorf and Macy's. Elsewhere they cost about one page load per brand, and Nordstrom throttled after about 20. They are `NC` at Dillard's, Von Maur and Rack.
4. **The "lingerie-only" rule needs a ruling.** I treated sleepwear, loungewear and swim as clothing, and socks and hosiery as not clothing. Several register-relevant results depend on that, Wolford above all.
5. **Saks OFF 5TH is in the worklist but can no longer be read online.**
