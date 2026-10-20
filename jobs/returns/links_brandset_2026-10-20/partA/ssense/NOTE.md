# SSENSE (women's) — Part A, links_brandset_2026-10-20

- **Method:** opened https://www.ssense.com/en-us/women/designers once; read the designer links present on the page (303 brands, 3.1 Phillip Lim ... Yves Salomon) and matched them to the worklist by name with accents/punctuation folded. Spot-opened On, Still Here, Róhe and Comme des Garçons pages. No scripts called site services. Time: ~25 min.
- **Matched:** 91 of 464 (89 exact, 2 alias: A Bathing Ape = BAPE, Carhartt WIP = Carhartt Work In Progress). Remaining 373 are NONE = not on the A-Z list as read.
- **Listings:** brand pages show no item count in the header, so every row is ND (no scrolling to count).
- **Doubtful:**
  - The A-Z list is what the page rendered; I could not confirm it is the site's full roster. NONE rows therefore mean "not on that list", not a per-brand search. Prada, Miu Miu: only Eyewear lines appear, not mapped.
  - "Still Here": page is a denim/tops label; category not verified against the worklist brand.
  - "On" is On Running (sneakers), confirmed.
  - adidas (adidas Originals only), Calvin Klein (Collection only), Carhartt (WIP only), Camilla (CAMILLA AND MARC) not mapped, per sister-line rule.
  - Slug quirks: TOTEME = totme, Róhe = randoacutehe, Ami Paris = ami-alexandre-mattiussi, Ferragamo = salvatore-ferragamo, Guizio = danielle-guizio, McQueen = alexander-mcqueen.
- **Format:** `-` in name_on_site means exact name; `n/a - brand not listed on site` in url for NONE rows. reconcile.py: 464 exact, 0 rewrites.
- **Brief note:** `url` has no legal "none" value for NONE rows; I used a text placeholder.
