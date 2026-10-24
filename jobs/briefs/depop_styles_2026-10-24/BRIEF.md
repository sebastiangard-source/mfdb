# depop_styles_2026-10-24: how Depop sellers tag each brand's style

**Issued** 24 October 2026 · **Kind** read-only browser read · **431 brands, a pilot and five batches** · **Returns to** the Spectrum thread

This is a Chrome job on depop.com. If you cannot run a browser, say so and stop. **You gather; Sebastian rules.**

## Why

Depop sellers tag each listing with up to three style tags from Depop's own list (for example Y2K, Streetwear, Vintage, Boho, Preppy, Minimalist). Read across a brand's listings, those tags show how resale shoppers see the brand. We want the mix for every brand on the Cyprus Brand Explorer, to set beside our own segments. Read the style tags only. Hashtags are out of scope.

## The worklist

`worklist.csv` holds the 431 Explorer brands, in five batches of about 87. Each row gives the brand, our tier and segment, and its Explorer kind:

- **womens** and **crossover** brands: read the women's page (`/c/womens/`).
- **mens_only** brands (57): read the men's page (`/c/mens/`).

`depop_url_known` comes from our 20 October links read: the brand's Depop women's page, already checked to the right brand.

- **For mens_only rows,** the URL has been switched to `/c/mens/`; confirm it resolves.
- **`NONE`** means the brand wasn't in Depop's Brands A–Z on 20 October. Look once more in the A–Z; if it's still missing, the row is `NONE`.
- **`NC`** means it hasn't been looked up yet (Madewell, American Eagle, Urban Outfitters, Jimmy Choo, Ruti, Amsale, HANRO, Reem Acra, Wacoal). Find it in the Brands A–Z, `/brands/a-z/<letter>/`.

## Part 0: pilot, returned on its own before the batches

Use these five brands: Free People, Lululemon, Gucci, Carhartt WIP and Talbots. Find out how Depop exposes style tags, then return `NOTE_0.md` with what you found and what the full run will cost. Answer these questions:

1. **Facet counts.** On a brand page, does the filter panel have a Style filter? Does it show a count beside each style?
2. **Style list.** What is Depop's full list of style tags? Return it once as `depop_style_list.txt`.
3. **Per-style counts.** If the panel has no counts: when you apply one style filter on the brand page, does the results header (for example "(1.2K results)") give a count for that style?
4. **Listing pages.** Does each listing page show its style tags?
5. **Test the method.** Run the method you'd use (see below) on all five pilot brands. Return their rows in the return format.

**Methods, in order of preference.**

- **A. Facet counts.** The filter panel shows a count per style, so one page per brand gives the whole mix. Use this if it exists.
- **B. Filter counts.** Apply each style filter in turn and read the results header. This costs one page per style per brand, so with about 20 styles it's roughly 8,600 pages.
- **C. Listing sample.** Read the style tags on the first 40 listings in Depop's default order. That's about 17,000 pages.

If only B or C works, say so in `NOTE_0.md` and wait for Sebastian before starting the batches. Either is a long run, and he may want to cut the scope. If A works, carry straight on.

## Part 1: the batches

For each brand, on its women's page (or men's page for mens_only), with no other filter applied:

- **The whole-page count** from the header: Depop's rounded figure, as shown.
- **Every style with its count,** under the method the pilot settled. Include styles with small counts. Leave out styles with none.
- **Untagged listings.** If Depop shows how many listings carry no style tag, give that figure; otherwise `ND`.

Return two files per batch.

**`batch<N>/return_summary.csv`**, one row per brand, with these columns:

- `brand`
- `depop_url`
- `department` (`womens` or `mens`)
- `listings_shown`
- `method` (`A`, `B` or `C`)
- `tagged_total`: the sum of the style counts, or under method C the number of listings read
- `untagged`
- `style_1`, `style_1_n`, `style_1_share`, and the same for `style_2` to `style_5`. Each share is the style's count divided by `tagged_total`, to one decimal place, as a percent.
- `read_date`
- `status` (`read`, `NONE` or `held`)
- `note`

**`batch<N>/return_styles_long.csv`**, one row per brand and style, with these columns: `brand`, `style`, `count`, `share`.

Flag in `note`:

- **Very small brands.** Under 20 listings, the mix means little. Read it anyway.
- **Same-name brands.** Depop's brand tag is typed by sellers, so some pages mix two brands. The 20 October read named these: On, Theory, Reiss, Still Here, CO, Sea, Purple, Represent, Elan, Jordan, Express, Soma, Frame, Camilla, Bode, Palace, Eton, Rains, Vince, Kith, Greyson and Goldwin. Glance at the first screen of listings. If it plainly mixes two brands, say so; don't try to separate them.
- **LoveShackFancy** showed 0 results on 20 October. Check it once more.

## Rules

- **Read only.** Don't sign in. Never like, save, follow, message, offer or buy.
- **Pages only.** Depop's own pages, as a shopper sees them. No API calls. Reading a page inside a hidden frame in the Depop tab is fine, as on 20 October.
- **Pace.** One page at a time, about one every two to five seconds. Don't run pages in parallel.
- **Bot walls.** One plain try. If a check box appears, ask Sebastian once whether he'll clear it himself. Anything else: stop, mark the rest `held`, name the wall, and return what you have.
- **Brand names** are as in `worklist.csv`. Don't rename them.
- **Cell values.** `NC` means nobody looked, `NONE` means Depop has no such brand, `ND` means the page was read and doesn't show it. No empty cells.
- **Counts are as shown,** with K and M as Depop writes them in `listings_shown`. Facet counts can be written as numbers when the page shows them in full.

## Return and time box

1. **Pilot:** `NOTE_0.md`, `depop_style_list.txt` and the five pilot rows. Allow 20 minutes.
2. **Batches 1 to 5:** for each, `return_summary.csv`, `return_styles_long.csv` and a short `NOTE.md` covering misses and flags. Return each batch as it finishes. Under method A, allow about 30 minutes a batch.

Past the box, return what you have and mark the rest `NC`.
