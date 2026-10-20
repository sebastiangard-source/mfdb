# links_brandset_2026-10-20: where to shop and resell each Brand Set brand

**Issued** 20 October 2026 · **Kind** links · **Two threads, one per part, run side by side** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. This is a Chrome job. If you cannot run a browser, say so and stop.

## Why

Each brand card on the Cyprus Brand Set will link out to the places a shopper meets the brand beyond its own stores: the luxury and department-store retailers that carry it, and the resale sites where it trades second-hand. The card shows only links that are right. **A wrong link is worse than no link.**

## The worklist

`worklist.csv` has 464 brands:
- 422 fashion brands, with tier, US store count and the brand's own site.
- 42 jewelry, bag and eyewear brands from the Other brands section.

`vinted_on_file` is a Vinted catalog link already held for 352 brands. Most are **men's** filters (`catalog[]=5`).

## Work by site, not by brand

Almost every site below has a designers A–Z page listing every brand it carries, with a link to each.

1. Open that page **once**.
2. Read the whole list.
3. Match it against the worklist.
4. Open individual brand pages only to settle a doubtful match or to read a listing count.

This is far faster than searching 464 brands one at a time on each site.

**Part A, retail (`THREAD_A.md`), in this order:**
1. SSENSE (women's designers)
2. Net-a-Porter
3. Mytheresa (women)
4. Saks Fifth Avenue
5. Nordstrom
6. Shopbop
7. Farfetch (women)

**Part B, resale (`THREAD_B.md`), in this order:**
1. The RealReal
2. Vestiaire Collective
3. Depop
4. Poshmark (women's brand pages)
5. Vinted (women's)

For **Vinted**:
- Where a brand has a Vinted link on file, swap the men's catalog for the women's one, keeping the same `brand_ids`. Check the swap on five brands before applying it to the rest.
- Where none is on file, find the brand's ID with Vinted's brand filter.

## What you return

One `return.csv` per part, in the columns of `return_template.csv`, with **one row per brand per site**. That's 464 rows for each site you finish.

- `url` is the brand's page on that site.
- `url_kind` says what sort of page it is:
  - `designer_page`: the site's own page for the brand. This is preferred.
  - `brand_filter`: a listing filtered by the site's brand ID, as on Vinted.
  - `search`: a keyword search. Use this only where the site has no brand pages, and say so.
- `match` describes how sure the match is:
  - `exact`: the name on the site is the brand's.
  - `alias`: a different spelling or form of the name. Give it in `name_on_site`.
  - `NONE`: the site doesn't carry the brand.
  - `NC`: not checked, or blocked.
- `listings` is the number of items the page shows, where it shows one; otherwise `ND`. Give `listings_basis`, for example "page header 1,240 items". Counts are wanted because they show how deep each brand is on each site, so take them wherever the page gives them cheaply. Don't scroll to count.
- `NOTE.md` per site: method, the page you read, the time it took, and anything doubtful.

## Matching rules

- **Sister lines are their own names.** On a site that splits them, map each worklist name to its own line only, and never fold one into another.
  - RRL is not Polo Ralph Lauren or Ralph Lauren Collection.
  - Polo Ralph Lauren is not Ralph Lauren Collection.
  - Carhartt WIP is not Carhartt.
  - Black Comme des Garçons and Comme des Garçons Play are not Comme des Garçons. Map Comme des Garçons to the main line only.
  - Emporio Armani is not Giorgio Armani.
  - MM6 is not Maison Margiela.
  - Max Mara's sub-lines (Weekend Max Mara, 'S Max Mara) don't count.
- **Women's side first.** Where a site splits men's and women's designer pages, give the women's page. If the brand is sold only in men's there, give the men's page and say so in `note`.
- **Same name, different brand.** Check the category before matching names like "Reiss", "Rowan", "Elan", "Still Here", "On" and "Theory". "On" on a resale site is usually On Running, but check.
- **The brand's own page on the site, never a sponsored or "similar to" page.**

## Bot walls and pace

- **One plain try per site.** If a check box appears, ask Sebastian once whether he'll clear it himself. Any other wall, such as press-and-hold, slider or "access denied", means the site is `NC` with the wall named in `NOTE.md`, and you move on.
- **Pace:** one page every few seconds. Nordstrom, Saks and Farfetch are known for walls; take them last in Part A.
- Read only what a person browsing would see. Don't use scripts to call a site's private search or catalog services.

## Rules

- **Names** must match `canonical_keys.txt`. Run `python3 reconcile.py` on the brand column before each return.
- **No empty cells.**
- Don't touch the map. Anything out of scope but noticed goes in `NOTE.md`.

## Order and time box

- **Return each site as it's done.** Don't wait for the whole part.
- Allow about forty minutes a site, and an hour for Vinted.
- Past the box, return what you have, put `NC` on the rest, and say so.
