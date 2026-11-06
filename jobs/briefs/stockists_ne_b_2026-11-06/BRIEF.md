# stockists_ne_b_2026-11-06: shop records for 10 Northeast stockists of Farafield

**Issued** 6 November 2026 · **Kind** stockist · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. Everything below assumes it. **You gather and propose; Sebastian rules.**

## Why

Farafield list these shops on their own stockist pages. The map holds a shop only with a record: what it is, who owns it, its story and the brands it carries that we already have. Today none of these 10 shops is on the map. This brief brings each to the standard Assembly Showroom met, so its brands can link to the brands we already have.

## The job, once for each row of `worklist.csv`

1. **Find the shop's own website.** Confirm the shop at the listed address is the one you are reading, and take address, ZIP, hours and phone from the shop's own pages. Look for other doors under the same name (another town, a second shop), and put what you find in `other_doors`, or `none found`. If the shop has closed or has no site, say so and fill what you can.
2. **Fill one row of `return_template.csv`.**
   - **Where it is:** street, city, state and ZIP, from the shop's own site. If the site differs from the brand's page, use the site's and say so in `note`.
   - **What it is:** `type` (menswear specialist, boutique, outfitter, department store) and `gender`. Use `womens_with_mens_tail` if mainly women's.
   - **Who owns it, and since when:** `founded`, `owners` and `ownership` (independent, family-owned, part of a group). Local press and the shop's About page carry these. Name the outlet in `note`.
   - **The hours it keeps.**
   - **Its brand list,** read from its own source: a Designers or Brands page, the vendor filter on its online store, or its own listing of lines it carries. Name the source in `brand_list_source` and give the full count in `brand_count`. If the shop publishes no list, say so and write `NC`. Don't build a list from social posts or press.
   - **The brands we already have:** run `python3 reconcile.py names.txt` on the full list. Put the exact canonical names that match in `matched_brands`, separated by `;`, and their count in `ub`. A near miss is a rewrite, not a new brand. Keep the whole list, unmatched names included, in `NOTE.md` under the shop's name. Don't sift it.
   - **A story** of three to six sentences, in the register of `shop_example.json`: facts, dates and names, with no adjectives the source didn't supply.

## Rules

- **Names.** Brand names in `matched_brands` match `canonical_keys.txt` exactly. The shop name is written the way the shop writes its own name.
- **No empty cells.** `NC` means nobody looked. An empty cell is an error.
- **One source per row.** The shop's own page where there is one.
- **Bot walls.** One plain try. If a check box appears, ask Sebastian once whether he'll clear it himself.
- **Read only.** Don't sign in, add to cart, sign up, follow or message anyone.
- **Don't touch the map.** Return `return.csv` and `NOTE.md`, nothing else.

## Time box

About fifteen minutes per shop. Past the limit, return what you have with `NC` on the rest, and say so. Return in batches of three or four shops if that suits you.
