# Vestiaire Collective — NOTE

**Part B, site 2 · checked 20 Oct 2026 · about 10 minutes**

## Method
- Opened https://us.vestiairecollective.com/brands/ once and read the full A–Z: 13,698 brand links, each in the form `/<slug>/`.
- A Cloudflare "performing security verification" page cleared on its own after a few seconds. I took no action on it.
- Declined non-essential cookies.

## Gender and counts
- **No women's page.** VC brand pages are not split by gender. I tried `/women/gucci/` and it returns "can't find this page". So every URL is the unisex brand page, `url_kind=designer_page`.
- **No counts.** The brand-page header caps the count ("Gucci – 999+ items"), and opening 400 pages to read capped numbers wasn't worth it. `listings` is `ND`.

## Result (464 rows)
- 381 `exact`, 29 `alias`, 54 `NONE`.
- `NONE` means the brand is absent from the complete A–Z list.
- VC shows a banner saying it **no longer accepts fast-fashion brands**. Zara, Mango, Uniqlo and Gap are `NONE`.

## Aliases (in `name_on_site`)
- Former brand names: daniella kallmeyer (KALLMEYER), sally lapointe (LAPOINTE), jonathan simkhai (Simkhai).
- Name variants: salvatore ferragamo, g-star raw, maison martin margiela, alexander mcqueen, emilio pucci, valentino garavani (Valentino), bvlgari, moynat paris, on running, purple brand, sea new york, schott, thursday boots, kate spade, lafayette 148 ny, mestiza, nn07 no nationality, boggi, ami (Ami Paris), simon miller.
- RRL → "ralph lauren double rl". It is separate from Polo Ralph Lauren, Ralph Lauren Collection and Ralph Lauren Purple Label, which VC also lists.

## Doubtful, verify before showing
- **AG:** VC splits the brand across "ag adriano goldschmied" and "ag jeans". I linked the full-name entry.
- **Joe's and Joe's Jeans** both point to `/joes/`, the only Joe's entry.
- **Goldwin → "goldwin sport":** the only Goldwin entry; unsure it is the same line.
- **Category not checked:** Aether Apparel → aether, HATCH Collection → hatch, Ami Paris → ami.
- **Near names not matched (all `NONE`):** "bonobo" (not Bonobos), "carmina campus" (not Carmina), "loft designed by" (not LOFT), "pilgrim" (not Pilgrim Surf + Supply). Agua Bendita has only its sister line "agua by agua bendita", which wasn't folded in.
- **Carhartt and Carhartt WIP** are separate VC entries and are mapped separately.
