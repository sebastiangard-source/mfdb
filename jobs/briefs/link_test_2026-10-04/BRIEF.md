# link_test_2026-10-04 — every outbound link on the map, opened

**Issued** 4 October 2026 · **Kind** link test · **First 200 rows returned early, no stop** · **Returns to** the Spectrum thread

Read `audit_protocol.md` first.

## The job

`links.csv` is every URL the page or the record points at: 5033 links. Open each one in a real
browser, as a US visitor with no login, and say what it shows. When the garment-links pass looked at
the site-search links in September, a sixth were dead or served the wrong country; nothing has checked
the rest.

By kind: price 2784, garment 1267, site 204, vinted 203, onething 195, search 183, season 114, shop-site 83.

## What to return

One row per link in `return_template.csv`: the HTTP status after redirects, the final URL, a verdict,
a replacement where you found one, and a note.

`what_it_should_show` says what counts as right:

- **site** \u2014 the brand\u2019s store, US storefront, not a splash page or a region picker that strands you.
- **search** \u2014 results for the word polo (or the brand\u2019s own word for it); a page that says
  \u201cno results\u201d for a brand that sells polos is `wrong-page`.
- **garment** \u2014 a men\u2019s listing for that garment with product on it. Women\u2019s product in the first
  two rows is `wrong-page`; a listing with no tiles is `empty`.
- **onething** \u2014 the named product, or a search that surfaces it in the first row.
- **vinted** \u2014 men\u2019s listings under the brand; a page of women\u2019s or another brand is `wrong-page`.
- **season** \u2014 a lookbook or campaign page with images, not a category grid.
- **price** \u2014 the product page behind a price figure; still the same product, still on sale at full
  price or sold out (sold out is `ok`; a different product at the URL is `wrong-page`).
- **shop-site** \u2014 the shop\u2019s own site, live.

## Rules

- A real browser, fresh profile, US exit, no login. A 200 with a bot wall is `blocked`, not ok.
- Follow redirects and record where you land; a redirect to the right page is `redirected-ok`.
- `replacement_url` only when you found the right page on the same site; never a guess.
- Do not fix anything on the map. Return `return.csv` and `NOTE.md` (patterns: which stores moved,
  which block, which redirect US visitors elsewhere).
- Two agents per shared browser at most; the September pass found the extension hangs above that.

## Time box

Fifteen seconds a link once the browser is warm; the whole file is a day for two agents. Return the
first 200 rows early so the format can be checked, and keep going.
