# stockist_ellicott_2026-10-24: Ellicott & Co. (Lancaster, PA), shop record and brand sift

**Issued** 24 October 2026 · **Kind** stockist · **Returns to** the Spectrum thread

Read `audit_protocol.md` first. Everything below assumes it. **You gather and propose; Sebastian rules.**

## The job

Two things, in order. Return the shop first, then the brands.

### 1. The shop

Ellicott & Co. is a men's shop in Lancaster, Pennsylvania (ellicott.co). Sebastian visited it on 24 October 2026. It is not yet in our shop register. Establish:

- where it is: street, city, state and ZIP;
- what it is: type and gender (`gender`);
- who owns it, and since when;
- the hours it keeps;
- its full brand list, read from its own source: a Brands page, the collections or vendor menu, or the shop's footer. Say which in `brand_list_source`, and give the count in `brand_count`.

Return one row in `return_shop_template.csv`. Add a story of three to six sentences in the register `shop_example.json` uses: facts, dates and names, with no adjectives the source did not supply.

Ellicott & Co. appears in its own brand list. Find out whether that is a house label (made for the shop, or by it) or just the shop's name, and say which.

### 2. The brands

`return_brands_template.csv` holds the ten names from Sebastian's photo of the shop's list that are not on the map:

- Ellicott & Co.
- Power Goods
- SeaVees
- Soft Goods
- TOPO Designs
- Nisolo
- Peregrine Clothing
- American Trench
- Bridge & Burn
- Lems

Six other names on that list are already on the map: Red Wing (listed by the shop as Red Wing Shoes), Taylor Stitch, Marine Layer, Nudie Jeans (listed as Nudie Jeans Co), Pendleton and Filson. Confirm each on the shop's own list. Don't sift them.

**If the shop's full list has more brands than the photo,** reconcile every name against `canonical_keys.txt`. Add a row for each one that isn't on the map and sift it the same way.

**What we already know,** to confirm or contradict in `note`:

- **American Trench** is on three other Pennsylvania shop lists in our register: Franklin & Poe, Vestis and Weitzenkorn's. Its stockist at 15 E. Lancaster Ave., Ardmore, PA appears on Imogene + Willie's stockist page. It is marked "add, check stockists" but was never seated.
- **TOPO Designs** was seen once before, at Trail Creek Outfitters. Snow Peak's locator lists TOPO Designs flagship stores in Denver and Fort Collins.

**The sift, for each brand:**

- **Reconcile first.** Run `python3 reconcile.py names.txt` against `canonical_keys.txt`. A near-miss is a rewrite, not a new brand. For example, "Red Wing Shoes" is the map's "Red Wing".
- **Check the bench.** `menswear_bench.md` holds brands already looked at and not seated, with the reasoning. Don't redo a bench entry; confirm or contradict it in `note`.
- **Verdict:**
  - `seat`: a real menswear house with a first-party store (its own website counts), an origin, and a staple price that can be read.
  - `bench`: real, but it can't be seated yet. For example, it has no men's clothing, has no prices anywhere, or the only price is a stockist's markup. Say what would change it.
  - `reject`: a shop's own label with no life of its own, a womenswear house with no men's line, or not a clothing or footwear brand at all.
  - Footwear houses can be seated, as Red Wing is. Say `footwear` in `note`.
- **For every seat or bench,** fill in:
  - origin;
  - founding;
  - own US stores: a count from the brand's own store locator, or `NONE`;
  - the price basis;
  - one staple price (a tee or knit, or the core shoe for a footwear house);
  - one sentence on what the brand is, in its own words.

## Rules

- **Names.** Match `canonical_keys.txt` exactly where a match exists. Otherwise use the brand's own mark, written as it writes it.
- **No empty cells.** `NC` means nobody looked; an empty cell is an error.
- **A stockist's price never becomes a brand's price.** If the only figure is Ellicott & Co.'s, label the basis as such. That can bench a brand but can't seat it.
- **A search result carrying the brand's name is not the brand** until product, price band and country agree with what the shop sells. Check the shop's product against the site you find. Watch the generic names: Power Goods, Soft Goods and Peregrine all have namesakes.
- **Bot walls.** One plain try. If a check box appears, ask Sebastian once whether he'll clear it himself.
- **Read only.** Don't sign in, add to cart or sign up for anything.
- **Don't touch the map.** Don't rebuild anything. Return the two CSVs and `NOTE.md`, nothing else.

## Time box

Twenty minutes on the shop, then return the shop row and stop before the brands. After that, fifteen minutes per brand; past that, mark it `NC` with a note.
