# stockist_great_put_on_2026-09-18 — The Great Put On: shop record and brand sift

**Issued** 18 September 2026 · **Kind** stockist · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. Everything below assumes it.

## The job

Two things, in order.

**1. The shop.** The Great Put On is a stockist not yet in the register. Establish it: where it is,
what it is, who owns it, since when, what hours it keeps, and its own brand list read from its own
source (a Brands menu, a collections feed, or the floor — say which). Return one row in
`return_shop_template.csv` and a story of three to six sentences in the register the examples in
`shop_example.json` use: facts, dates and names, no adjectives the source did not supply. Golden
Goose is on the map and is carried; confirm that on the shop's own list. If the shop turns out to be
womenswear with a men's tail, say so in `gender` — that is a finding, not a failure.

**2. The brands.** Twelve names were read off the shop's list and are in `return_brands_template.csv`.
Golden Goose is seated. For each of the other eleven, run the sift:

- **Reconcile first.** `python3 reconcile.py names.txt` against `canonical_keys.txt`. A near-miss is a
  rewrite, not a new brand.
- **Check the bench.** `menswear_bench.md` holds brands already looked at and not seated, with the
  reasoning. Autumn Cashmere is there (trades heavily through off-price). Do not redo a bench entry;
  confirm or contradict it in `note`.
- **Verdict.** `seat` if the brand is a real menswear house with a first-party store, an origin, and
  a staple price that can be read; `bench` if it is real but cannot be seated yet (no own store, no
  prices anywhere, a stockist's markup is the only figure, off-price-led) — say what would change
  it; `reject` if it is a shop's own label with no independent existence, a womenswear house with no
  men's line, or not a clothing brand at all. William Henry is knives and pens; say so and reject.
- **For every seat or bench**: origin, founding, own US store or `NONE`, the price basis, one staple
  price, and one sentence of what the brand is in its own words.

## Rules

- Names must match `canonical_keys.txt` exactly where a match exists; elsewhere the brand's own
  mark, as it writes itself.
- `NC` means nobody looked; an empty cell is an error.
- **A stockist's price never becomes a brand's price.** If the only figure is The Great Put On's,
  label the basis as such; it can bench a brand but it cannot seat one.
- **A search result carrying the brand's name is not the brand** until product, price band and
  country agree with what the shop is selling. seyagarments.com was a live Shopify store that was not
  seya. Check the referring shop's product against the site you find.
- **The vendor field is not the boundary.** Judge by product and by what the house says it makes.
- **Do not touch `menswear_spectrum.html`. Do not rebuild anything. Return the two CSVs and
  `NOTE.md`, nothing else.**

## Time box

Twenty minutes on the shop. Fifteen minutes per brand; past that, `NC` with a note. Return the shop
row first and stop, before the brands.
