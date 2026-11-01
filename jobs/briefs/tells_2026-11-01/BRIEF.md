# tells_2026-11-01: the "tell" for every brand

**Issued** 1 November 2026 · **Kind** research read (browser and web) · **567 brands, a pilot and six batches** · **Returns to** the Spectrum thread

Read only. You gather and propose; Sebastian rules.

## What a tell is

A tell is the detail that lets someone who knows clothes recognize the brand on the street without reading a name. Examples:

- Stone Island's compass badge on the left sleeve.
- Maison Margiela's four white stitches on the back of the neck.
- Levi's red tab on the back right pocket.
- Thom Browne's red, white and blue grosgrain stripe.
- Burberry's check.
- Moncler's felt cockerel badge on the sleeve.

It is a mark, detail or pattern **on the garment**. It is not the signature product: that's a separate field we already hold, given in `worklist.csv` as `signature_product_known` so you can see the difference. The Barbour Bedale is a product; the tartan lining and corduroy collar are tells.

Many brands have no tell, especially basics and mainstream brands that rely on a printed name. That is a real answer: return `none`. **A wrong tell is worse than a missing one.**

## The worklist

`worklist.csv` holds 567 brands: everything on the men's map and The Cyprus Brand Explorer. For each brand it gives:

- the maps it is on;
- its band or tier;
- the men's logo score where we have one (1 is no visible branding, 5 is the logo as the design);
- the signature product we already hold;
- its site.

Brands come in a pilot of ten, then batches 1 to 6 of about 100.

## For each brand

Return one row in `return.csv`, with the columns of `return_template.csv`; the example row is Stone Island. Fill these:

- **`has_tell`:** `yes`, `none` (the brand has no recognized tell beyond printing its name) or `unclear` (sources disagree, or it is too new to say).
- **`tell`:** a short name, eight words at most. For example "The compass badge" or "Four white stitches".
- **`description`:** one plain sentence on what it is and where it sits.
- **`kind`:** one of:
  - `badge_or_patch`
  - `stitching`
  - `label_or_tab`
  - `pattern_or_print`
  - `color`
  - `hardware` (buttons, zips, buckles)
  - `logo_mark` (a symbol, not the written name: the Polo pony, the Lacoste crocodile)
  - `construction` (a cut or build detail, like a collar or a pocket shape)
  - `other`
- **`placement`:** where on the garment, such as left chest, back neck, sleeve, lining, or all-over.
- **`visibility`:**
  - `overt`: anyone notices it.
  - `subtle`: you notice it if you look.
  - `insider`: only people who know the brand recognize it.
- **`since`:** the year it began, if a source states it; otherwise `ND`.
- **`source_url`** (required for every `yes`), plus **`source_url_2`** if you have it. Use the brand's own pages first (a heritage or about page, a product description), then reputable press: GQ, Esquire, Highsnobiety, Hypebeast, Mr Porter's Journal, Permanent Style, Put This On, The Rake, Business of Fashion, Vogue. A forum, a reseller listing or a blog alone is not enough; it can support a press or brand source.
- **`example_product_url`:** a current product on the brand's own site where the tell can be seen. `NC` if none is easy to find.
- **`confidence`:**
  - `high`: the brand or two good sources name it.
  - `medium`: one good source.
  - `low`: well known, but thinly sourced. Say why in `note`.

## Rules

- **One tell per brand:** the most recognized one. A strong second goes in `note`, such as "also: the gold horsebit hardware".
- **Logos.** A written wordmark is not a tell, unless its form or placement is the identity, like Off-White's quotation marks. A symbol (the pony, the crocodile, the swoosh) can be one.
- **Sub-lines** are read on their own record. RRL's tell is not Polo's. Carhartt WIP is not Carhartt.
- **Women's and crossover brands.** On the Explorer the tell may sit on women's clothes or accessories, like the Chanel quilting or the Tory Burch double-T. That counts.
- **Discontinued tells.** If the tell is no longer on current product, say so in `note` and give `since` as the span, such as "1990-2015". Prefer a current tell where there is one.
- **No adjectives the source didn't supply.**
- **Cell values.** `NC` means nobody looked; `ND` means the source doesn't state it. No empty cells.
- **Read only.** Don't sign in. Never buy, sign up, follow, like or message.
- **Pace.** One page at a time, at a human pace.
- **Bot walls.** One plain try. If a check box appears, ask Sebastian once. Anything else: move on, mark the row `NC`, and name the wall in `note`.

## Order, return and time box

1. **Pilot (ten brands):** Stone Island, Maison Margiela, Levi's, Burberry, Thom Browne, Moncler, Polo Ralph Lauren, Acne Studios, Asket and Uniqlo. Return `pilot/return.csv` and `pilot/NOTE.md`, then stop and wait for Sebastian's word. The last two are there to test `none`.
2. **Batches 1 to 6:** `batch<N>/return.csv` and `batch<N>/NOTE.md`, each returned as it finishes. List the low-confidence and `unclear` rows at the top of each note.

Allow about three minutes a brand. Well-known houses go fast and obscure ones quickly come back `none`, so a batch is about five hours. Past the box, return what you have and put `NC` on the rest.
