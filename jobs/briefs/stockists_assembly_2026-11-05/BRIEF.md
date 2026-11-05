# stockists_assembly_2026-11-05: the shop record for Assembly Showroom, Hingham

**Issued** 5 November 2026 · **Kind** stockist · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. Everything below assumes it. **You gather and propose; Sebastian rules.**

## Why

Assembly Showroom, 88 North St., Hingham, MA, is a men's-and-women's boutique with a long brand list. Two brands' own pages name it: Save Khaki United (its stockist page gives the street but no ZIP) and Mollusk (its page gives the name and town only). The map shows it as a bare record today, with one brand linked and no history, owner or brand list, so a reader sees one name where the shop carries many. This brief brings Assembly to the standard the Undercover shops and the Northeast shops meet. Then its brand list can link to every brand we already have.

## The job

### 1. Confirm the shop

Find the shop's own website. Confirm that the shop at 88 North St., Hingham is the one you are reading, and take the address, ZIP, hours and phone from the shop's own pages. Search for other doors under the Assembly name (a second Hingham door, a home or kids shop, another town). Put what you find in `other_doors`, or `none found`.

Return this check by itself, before the full record, in the first section of `NOTE.md`.

### 2. The full record

Fill one row of `return_template.csv`, the same columns the Undercover shops used, with these fields:

- **Where it is:** street, city, state and ZIP, from the shop's own site. If the site's address differs from the two brand pages (`88 North St.`), use the site's and say so in `note`.
- **What it is:** `type` and `gender`. Use `womens_with_mens_tail` if the shop is mainly women's with some men's.
- **Who owns it, and since when:** `founded`, `owners` and `ownership` (independent, family-owned, part of a group). The Hingham Anchor ("From Denim to Dinner Parties, Meet this Downtown Hingham Boutique Duo") and Boston Magazine's Best of Boston 2021 both cover the shop. They can carry founding facts, owners and the story. Name the outlet in `note`.
- **The hours it keeps.**
- **Its brand list,** read from its own source: a Designers or Brands page, the shop's vendor filter, or its online store. Name the source in `brand_list_source`, and give the full count in `brand_count`. If the shop publishes no list, say so, then use its online store's brand or vendor filter, and say which you used. Don't build a list from social posts or press.
- **The brands we already have:** run `python3 reconcile.py names.txt` on the full list. Put the exact canonical names that match in `matched_brands`, separated by `;`, and their count in `ub`. A near miss is a rewrite, not a new brand. Keep the whole list, unmatched names included, in `NOTE.md` under the shop's name. Don't sift it.
- **A story** of three to six sentences, in the register of `shop_example.json`: facts, dates and names, with no adjectives the source didn't supply.
- **Whether Save Khaki United and Mollusk are on the shop's own list.** Set `sku_on_shop_site` and `mollusk_on_shop_site` to `yes`, `no` or `NC`. A `no` doesn't overrule the brand pages. It tells us how fresh the link is.

## Rules

- **Names.** Brand names in `matched_brands` match `canonical_keys.txt` exactly. The shop name is written the way the shop writes its own name.
- **No empty cells.** `NC` means nobody looked. An empty cell is an error.
- **One source per row.** Put it in `source`, and use the shop's own page where there is one. A press piece can carry the story or the founding facts.
- **Bot walls.** Give each one a single plain try. If a check box appears, ask Sebastian once whether he'll clear it himself.
- **Read only.** Don't sign in, add to cart, sign up, follow or message anyone.
- **Don't touch the map.** Don't rebuild anything. Return `return.csv` and `NOTE.md`, nothing else.

## Time box

- Ten minutes on the shop check, then return it.
- Thirty minutes for the full record. The brand list is the long part.
- Past the limit, return what you have and write `NC` with a note.
