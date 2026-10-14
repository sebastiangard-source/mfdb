# prices_womens_2 — batch 1 note (13 Oct 2026, evening)

**Read (9 of 10):** Gianvito Rossi, Still Here, TOTEME, Loeffler Randall, prAna, Sam Edelman, Manolo Blahnik, Roger Vivier, Aquazzura. Every figure has its product name and the US product URL it came from. USD throughout.

**Not read: LOFT, all `NC`.** I tried once in this session. The homepage shell loaded, but the first category request (Tees) got PerimeterX's "Access to this page has been denied … automation tools" page (ref cea65a40-c76c-11f1-8278-d3d9dd429dcb). I didn't press-and-hold, and I didn't use the search-cache or sitemap routes the brief suggests. Both are ways round a bot wall, and this session won't do that. LOFT needs a person to read it in a normal browser.

**Retries that went through:**

- TOTEME: no certificate warning this time.
- prAna: no bot wall.
- Sam Edelman: the apparel page showed a Cloudflare "Performing security verification" interstitial once. A plain reload a few minutes later loaded normally, and I didn't touch the challenge.

## Where the brief would have given a confident wrong answer

1. **Shopify `products.json` is not the US storefront.** TOTEME's feed lists ~1,500 products, including items that 404 on `/en-us/` (a $359 jersey shirtdress would have been the dress low). Marked-down items there carry no compare-at, so they look like full price. I checked every TOTEME figure on its live US product page. Any future pass that reads Shopify feeds needs the same check.
2. **Loeffler Randall and Sam Edelman are "shoe houses" that sell RTW.** Loeffler Randall has a full women's range (tees to coats), and Sam Edelman has a ~46-piece apparel line. I priced all eight garments. For both, the shoe band and the blouse/sweater band agree (LR Accessible, SE Premium), so the rule doesn't fork here.
3. **prAna's core tee is $38.** That's $3 over the Basic cut, and there's no cheaper plain tee. It bands Premium (mean $73). Flag it if the map expects an outdoor brand like prAna to read Basic.
4. **"Shoe house bands on flat entry" pushes Sam Edelman's low to a $65 jelly Mary Jane.** Its core leather ballet (Felicia) is $120. Both are under $150, so the band is the same either way.

## Judgement calls the merge should see

- **Gianvito Rossi:** the high is the Rania Loafer at $2,995 (silk organza and suede), a named FW26 family that isn't marked limited. If the merge treats it as a capsule, the high is the Yuna Loafer at $1,395.
- **Still Here:** there's no crewneck sweater and no elevated fibre (all cotton), so the sweater basis is `range`. Leather and suede versions of the jean styles ($995–$1,095) are excluded as not denim. The outerwear high is the same Car Jacket in leather. Leather isn't on the elevated list, so I marked it `range`, not `pair`.
- **TOTEME:** I passed over a $1,600 wool-silk crew (wool-majority) as the sweater high and used the Cashmere crew at $770. Pony-hair coats and ballerinas are excluded as fur. Garderob is listed as a sub-line.
- **Sam Edelman:** the outerwear high is the Croc Jacket at $248. The listing doesn't confirm it's croc-effect rather than real croc, so check it before merge. I passed over a faux-fur coat and a faux-shearling jacket at $240.

## Not womenswear after all

None. All nine read brands sell women's product on their own US store.
