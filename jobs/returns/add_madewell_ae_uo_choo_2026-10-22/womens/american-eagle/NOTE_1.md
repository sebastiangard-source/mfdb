# NOTE_1: American Eagle, Part 1 (women's read), 22-23 Oct 2026

I hold `add_madewell_ae_uo_choo_2026-10-22`. American Eagle Part 1: dials, 79-style sample, facts, socials. Prices are in `womens/return_prices.csv` (already returned).

## Social (read only; nothing followed, liked or messaged)

| Platform | Handle, linked from ae.com footer | Followers shown |
|---|---|---|
| Instagram | https://www.instagram.com/americaneagle | 3.8M |
| TikTok | https://www.tiktok.com/@americaneagle | 785.7K |

The footer also links Facebook and Pinterest (not read). These are the main US American Eagle accounts, not Aerie.

## For you to rule

- **Shape is split.** Cotton leads 58% of the sample (jeans, sweats, graphic tees) and synthetic leads 32% (knitwear, tanks, outerwear, dresses, mostly recycled polyester), so `fab_cotton` 5 and `fab_synth` 4 at once.
- **proposed_tech = 3, proposed_craft = 1.** Tech rests on own-named denim (Next Level Stretch, Dreamy Drape), not a performance fabric, so 3 is generous; 2 is arguable. Craft is 1: 10-K says no owned factories and every sampled page says only "Imported".
- **Sample bias.** Each category page serves about 30 tiles, so I read three views per category (featured, price ascending, price descending): 520 style codes. The 79 sampled are proportional to the site's own category counts. Shares are indicative, not exact. The site's counts sum to 1,246 (categories overlap).
- **Founding.** Place is the first store (Novi, Michigan, 1977); founders are NC. The timeline names Silverman's Menswear, not people.
- **Signature product** is NC. Jeans are the signature category ($1 billion in jean sales, 2018) but I did not pick one product.
- **Lookbook:** no seasonal lookbook on ae.com; only a customer Style Gallery.

## Method and limits

- Composition comes from the material field in each product page's HTML; style URLs are built from the style, slug and colour and the slug rule was checked against the real URL for all 80 pages read.
- Elastane (incl. spandex) in the main fabric on 32 of 79. One pyjama-set pant was dropped as sleepwear.
- Lyocell or TENCEL appears in 9 of 79 (3 labelled TENCEL; Lenzing, licensed). "Real Good" is AE's own badge for more sustainable items.
- Ownership: public (NYSE: AEO). 10-K for fiscal 2025 read via a text extract; the extract gave no filing date.
- The RealReal page loaded after a short interstitial (no check box). The Vinted catalogue API was not called directly; the brand id came from the site's Brand filter.
