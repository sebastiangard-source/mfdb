# prices_crossovers_2026-10-15 — batch 21 (retry of the seven held brands)

Read 20 October 2026, at the user's request. `return.csv` is cumulative, still 191 rows. No empty cells. Each brand got a plain retry at a slow pace. Wherever a check appeared I stopped and did not work around it.

## Result by brand

| Brand | Was | Now | What happened |
|---|---|---|---|
| Massimo Dutti | held | `done` | No wall this time. All ten listings read. |
| Hermès | held | `done` | No slider check. All seven listings read, using the Load-more button. |
| Polo Ralph Lauren | held | `partial` | Pages loaded, but only the first 12 Polo tiles per listing could be read. A scripted fetch for more brought back a px-captcha page, so I stopped. |
| Salomon | held | `partial` | The shoes listing was read. The sneakers page returned 'Press & Hold'. |
| The North Face | held | `partial` | The T-shirts listing was read. The next page returned 'Press & Hold'. Tee row only. |
| Vans | held | `held` | Clothing listing loaded (48 of 84 items). The next page returned 'Press & Hold'. Nothing filled. |
| Columbia | held | `held` | Listing again shows grey placeholder tiles and no products. Nothing filled. |

## Needs a ruling

**Massimo Dutti reads Premium, not the Accessible I proposed on 16 Oct.** Core blouse $100 and core sweater $100 give a mean of $100. Tee low is $60, so Basic does not apply.

- The url cells point to the listing page, not the product page.
- Listings show 53–66 tiles each, so dress highs could sit further in.

**Hermès reads True Luxury.** Blouse $2,275 and sweater $1,500 give a mean of about $1,888.

- Every Hermès tee is printed or embroidered. The cheapest is $820 and the plain one is $1,000.
- The dress high of $15,600 ('Dress with laced back') is unverified for fibre. Hermès tiles name leather explicitly, and this one doesn't.
- Outerwear low is a $2,425 Ferronnerie Remix varsity jacket. I counted that seasonal print series as regular range.
- Shoes were read with the site's 'Available online' toggle on. The high of $5,700 comes from filtering to smooth leather, suede and textile, which excludes exotic skins.

**Polo Ralph Lauren is a sample, not the range.** Blouse $148 and sweater $228 give a mean of $188 (Premium), only $12 under the Accessible line. Treat the band as unconfirmed until the full range is read. Dress, outerwear and shoes were not read.

**Salomon shoes are running and trail only.** Women-coded range is $140–$170. Lifestyle sneakers (XT-6 and others) sit on the blocked page, so the high may be understated.

## Why the walls matter

Vans, The North Face and Salomon all let the first page through and then showed the same Press & Hold check on the next page. Columbia never loads products. These look pace- or session-triggered. A fresh session, or a person browsing the categories by hand, may get further. I would not push these through automation.

## Second retry, 20 October (user asked to try the Press & Hold ones again)

- **Salomon sneakers:** still the same Press & Hold page (same reference ID), so not read. Salomon stays `partial`.
- **The North Face:** the casual-tops, pants, jackets-and-vests and footwear listings all loaded on a plain try. Filled: blouse, sweater and jeans `NONE` (casual tops are fleece and sweatshirts); trousers $65–$180; outerwear $110–$490; shoes $70–$290; band Basic. Still `partial`: dress is NC, and only 53 of 126 jackets and 30 of 67 shoes loaded.
- **Vans:** the clothing listing loaded and I slow-scrolled about 51 of 84 items. Filled tee $30–$50, blouse $55, sweater $90, jeans $70–$75, trousers $70–$75, outerwear $110–$150; band Basic. Dress and shoes NC. Now `partial`.
- **Columbia:** not retried; it never shows products.

I did not press and hold on anything. That check is a bot test, so I only reload pages and leave it if it shows.

## Third pass, 20 October (user watching for the check; none appeared)

- **Salomon:** now `done`. Lifestyle and clog pages load but every shoe there is unisex-coded, so the women-coded shoes cell stays $140–$170. With unisex counted it would be $100–$280.
- **Vans:** now `done`. The listing paginates; all 84 items read. Sweater $80–$90, dress $65 (single), shoes $60–$180 from about 16 shoes (the shoe grid recycles tiles, so some styles may be missed).
- **The North Face:** still `partial`. Dress is NONE (no dresses sold). Only 48 of 126 jackets and 30 of 67 shoes ever appear, even after View More.
- **Columbia:** still `held`; it shows no products.
