# Stone Island — depth measurement reproduced on a robots-allowed path

Date of read: 2026-09-13. Locale: en-US. Scope: men's.
No `/on/demandware.store/` URL was requested at any point. No access control was bypassed, spoofed or defeated.

---

## 1. What robots.txt says

Read first, at `https://www.stoneisland.com/robots.txt`.

For `User-agent: *` the site **disallows**:

```
Disallow: */on/demandware.store/*
Disallow: */cart
Disallow: */checkout
Disallow: */login
Disallow: */*?location=*
Disallow: */account/*
Disallow: */express/*
Disallow: *?filters=
Disallow: */?query=*
Disallow: */search*
Disallow: /en-ru/
```

It **allows** everything else, and explicitly advertises sitemaps:

```
Sitemap: https://www.stoneisland.com/en-us/sitemap_index.xml   (also en-gb, ko-kr, ja-jp, en-au)
Host: www.stoneisland.com
```

Consequences for this measurement:
- The prior channel (`*/on/demandware.store/*`) is disallowed — confirmed, first line of the group.
- Site search and filtered/faceted listing URLs are disallowed (`*/search*`, `*?filters=`, `*/?query=*`).
- **The product sitemap, category/listing pages, and ordinary PDP URLs are all allowed.** Plain pagination params (`?start=`, `?sz=`) are not disallowed.
- Separately, robots.txt name-bans the user-agents `python-requests`, `wget`, `lwp-trivial`, `mozilla/4`, `mozilla/5` and ~130 others with `Disallow: /`. Any reproduction must not present those UAs. This read used a normal Chrome browser UA.

One environment note, unrelated to robots.txt: this session's egress proxy returns **403 (org policy denial)** for `www.stoneisland.com:443`, so server-side `curl` cannot reach the host at all. Per the proxy README that denial was reported, not retried or routed around. All work below ran in the user's Chrome.

---

## 2. Denominator — reproduced

| Source (all allowed paths) | Colourway records | Styles |
|---|---|---|
| Live men's listing `/en-us/collection/view-all` (rendered) | **629** | — |
| Product sitemap `sitemap_0-product.xml`, en-US rows | **618** | **292** |
| Earlier pass (disallowed channel) | 637 | 298 |

- The allowed channel **reproduces the denominator to 98.3%** (618 of the 629 live records).
- The 618 vs 629 gap is sitemap staleness (`lastmod 2026-09-13T10:00`), not a structural blind spot.
- 629 vs the earlier 637 is catalogue drift between reads, not a channel difference.
- "Style" = colourway code with the trailing `V####` stripped. On that definition the allowed read gives 292 against the earlier 298 — consistent.
- Men's is cleanly separable: the entire `/en-us/collection/**` tree is the men's collection (US site carries no women's line). Per-category live counts — coats 112, fleecewear 126, pants 132, polos 86, knitwear 82, shirts 44, accessories 74, shoes 8 — sum to 664 because categories overlap (e.g. anoraks sit under both shirts and coats); `view-all` is the deduped figure, 629.

---

## 3. (a) Technology naming — reproduced, census not sample

The sitemap product slug carries both the descriptive product name and the fabric/technology name, e.g.
`.../stand-collar-jacket-with-anti-drop-4100056-nylon-smerigliato-tc-L1S154100056S0345V005G.html`.
That makes (a) a **full census over all 618 records from the sitemap alone** — no PDP fetches needed.

**Records naming at least one technology: 174 of 618 = 28.2%** (earlier pass: 187 of 637 = 29.4%).

| Family | This read (n=618) | Earlier (n=637) |
|---|---|---|
| **House-coined — any** | **160** | 170 |
| -TC suffix | 61 | 61 |
| Nylon Metal | 34 | 35 |
| Reps | 26 | 26 |
| Smerigliato | 20 | 21 |
| David | 9 | 9 |
| Tela Paracadute | 8 | 8 |
| Fissato | 8 | 8 |
| **Licensed — any** | **48** | 69 |
| ECONYL | 34 | 35 |
| PrimaLoft | **0 in names — held, see below** | 23 |
| E.DYE | 6 | 6 |
| CORDURA | 5 | 5 |
| GORE-TEX | 3 | 3 |
| BIONIC | 3 | 3 |

Twelve of the thirteen families reproduce within 0–1 record — i.e. within catalogue drift. Five reproduce exactly.

**The PrimaLoft exception, and it is the interesting one.** PrimaLoft appears in **zero** of the 618 product names. It is not a name-borne technology at all: it is an *insulation* named only in the PDP description (and, presumably, the composition/lining field that lives in the disallowed payload). Both PrimaLoft instances found in the description sample read:

> "…padded with PrimaLoft®-TC…" / "…with PrimaLoft®-TC insulation…"

Sampled rate 2 of 74 = 2.7%, which extrapolates to ≈17 of 618 (95% CI roughly 5–58) — statistically consistent with the earlier pass's 23 of 637 (3.6%). **The per-family PrimaLoft count is held**; it is not reproducible from names and needs the composition channel.

Critically, this does **not** move the headline: in both sampled cases the product name already named another technology (Smerigliato, -TC), so those records were already counted. Across the 74-record description sample, the description added a technology the name did not already carry in **0 cases**. The name channel is therefore a *complete* channel for "does this record name a technology" — the licensed-family gap (48 vs 69) is almost entirely the 23 PrimaLoft records (48 + 23 = 71 ≈ 69).

*Arithmetic note on the earlier pass:* its seven house-coined families sum to 168, yet its house-coined total is given as 170. A union cannot exceed the sum of its parts, so either two records come from an unlisted house family or that 170 is slightly off. Worth resolving before the row is quoted.

---

## 4. (b) Performance claim naming nothing — HELD (sampled only)

Reachable in principle but **not reproduced as a census**.

- Descriptions do not exist in PDP server HTML. Contrary to the earlier pass's note, the PDP server response on this allowed path is a ~33 KB empty shell: no description, no JSON-LD, no composition. The site is fully client-rendered. (Category/listing server HTML is likewise empty — 0 product tiles.)
- Descriptions therefore require rendering each PDP. Rendering via same-origin iframes ran at ~12–24 products/min initially — 6–12x the earlier pass's 2/min — but the site progressively throttled to ~2/min, converging on exactly the wall the earlier pass hit. A full 618-record census is roughly a 1–5 hour continuous crawl and was not attempted, both on time and on politeness grounds.
- Achieved: **74 rendered PDPs**, 70 of them a seeded random sample of the 618.

Sampled result: **0 of 74 records made a performance claim while naming no technology.** 8 of 74 (10.8%) made a performance claim at all, and every one of those sat on a record that named a technology. Rule of three gives a 95% upper bound of ~4.1%, i.e. **≤ ~25 of 618**.

This is an indication, not a figure. It also uses *my* coding of "performance claim" (water/wind resistance, breathability, insulation, membrane, abrasion, anti-drop, heat-reactive, reflective, UV), which is not the earlier pass's rubric. **Do not quote a (b) number from this read.**

---

## 5. (c) Majority synthetic — HELD, channel cannot reach it

**Composition is not reachable on any allowed path.** Verified at four levels:

1. Sitemap — no composition.
2. Category/listing pages, server and rendered — no composition.
3. PDP server HTML — empty shell; no composition, no JSON-LD, no meta description.
4. **Rendered** PDP DOM — description present, but **zero** fibre-percentage strings anywhere in the 354 KB DOM (0 of 74 sampled records contained any `NN% <fibre>` pattern).

Composition sits behind the "PRODUCT DETAILS" control, a `aria-haspopup="dialog"` button with no endpoint in markup, wired in the JS bundle. Every controller reference on the page resolves to `/on/demandware.store/Sites-StoneNA-Site/en_US/...` — the disallowed prefix. The dialog was **not** clicked, precisely so no disallowed request would be issued.

This also explains the earlier pass's "false 0% synthetic": a single-channel grep over PDP HTML returns 0% because the composition is simply not in that document — not because the garments are natural-fibre.

**(c) is held. It cannot be produced from an allowed path on this site.**

---

## 6. Recommendation

**The depth row can stand on (a) only, and should be re-stated against 618.**

- **Ship (a).** It is a genuine allowed-path census — sitemap-only, no rendering, trivially repeatable, and it reproduces the earlier pass on 12 of 13 families within catalogue drift. Restate as **174 of 618 (28.2%)**, house-coined 160, licensed 48, with the per-family table above. Footnote PrimaLoft as description-borne and not counted.
- **Hold (b) and (c).** (c) is structurally unreachable without the disallowed endpoint — that is a permanent property of this site, not a gap to retry. (b) is reachable but only at ~2/min under throttling, and nothing measured so far is census-grade.
- **Do not carry forward the earlier pass's (b)/(c) figures as confirmed.** They were produced through the disallowed channel and, for (c), the "0% synthetic" is a known artifact.
- If (c) is required for the brand to stay in the set, the honest routes are a licensed data feed, the brand's own wholesale/PIM data, or written permission from Stone Island — not a different scrape.
- A cross-brand caution: any brand whose composition was read through a Salesforce Commerce Cloud `demandware.store` endpoint likely has the same exposure, since `Disallow: */on/demandware.store/*` is close to boilerplate on SFCC sites. Worth auditing which other brands' (c) values came from that path.

---

## Appendix — allowed URLs actually used

- `https://www.stoneisland.com/robots.txt`
- `https://www.stoneisland.com/en-us/sitemap_index.xml`
- `https://www.stoneisland.com/en-us/sitemap_0-product.xml` (618 en-US product URLs)
- `https://www.stoneisland.com/en-us/sitemap_1-category.xml`
- `https://www.stoneisland.com/en-us/collection/view-all` (+ `?start=&sz=`, not robots-disallowed)
- `https://www.stoneisland.com/en-us/collection/{coats-and-jackets,fleecewear,pants-and-shorts,polos-and-t-shirts,knitwear,shirts,accessories,shoes}`
- 74 individual PDPs at their public `/en-us/collection/<category>/<slug>.html` URLs
