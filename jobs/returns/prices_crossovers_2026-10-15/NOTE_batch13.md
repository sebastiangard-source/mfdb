# prices_crossovers_2026-10-15 — batch 13

Read 16 October 2026 under the 16 October rulings. `return.csv` is cumulative and now holds 130 rows across batches 1–13. `reconcile.py` result: 10 exact, 0 to rewrite, 0 unmatched.

## Checked

- **`done`, nine brands:** Sunspel, Thursday Boot, Bode, Boggi Milano, Emporio Armani, G/FORE, Jil Sander, Ksubi and Mackage.
- **`held`, one brand:** Salomon.

## Not reached

**Salomon is `held`.** Its women's shoes listing returned an "Access to this page has been denied" bot page on the first plain try. I didn't retry or work around it, so `shoes` is `NC`. Its clothing was read before the wall and is in the row.

## Contradicts the existing record

- **Bode reads Accessible, not the current True Luxury.**
  - The core shirt is the White Smock Shirt at $468.
  - The core sweater is the Solid Front Tie Pullover at $530.
  - Their mean is $499.
  - I excluded Bode's one-of-a-kind and single-size pieces and kept embroidered pieces out of highs. Embroidery is close to a house signature there, so Bode's highs are conservative.
- **Boggi Milano reads Premium, not the current Accessible.**
  - The core shirt is $168 and the core merino crew is $198.
  - Their mean is $183.
- **Three brands can't be banded.** Salomon, Thursday Boot and Mackage have no blouse or sweater and no tee at $35 or under. I proposed their current bands unchanged. These need a ruling, like Cole Haan and On.
- The other six agree with `band_now`:
  - Sunspel, Emporio Armani, G/FORE and Ksubi read Accessible.
  - Jil Sander reads True Luxury.
  - Ksubi's band rests on a cardigan, its only knit.

## Brief or worklist issues

1. **Runway, capsules and limited editions excluded.**
   - Jil Sander and Emporio Armani runway pieces.
   - Emporio Armani's Boteh, Signature and Icon capsules.
   - G/FORE's "LTD Release" and holiday pieces.
   - Bode's one-of-a-kind pieces.
   - Collaborations: Jil Sander & PUMA, and Jil Sander for OTB Foundation.
2. **Sport-only ranges.**
   - Salomon's women's clothing is all running, trail and ski gear.
   - G/FORE's bottoms and dresses are golf pants, skorts and golf dresses, treated as sport as for Malbon, so its trousers and dress are `NONE`.
3. **Brands that are mostly one category.**
   - Thursday Boot's only women's clothing is jackets.
   - Mackage is mostly outerwear. Its "jumpers" are sweatshirts and its "cardigans" are zip hoodies and knit bombers, so its sweater is `NONE`.
   - Sunspel makes no women's jeans, dresses, outerwear or shoes; its only trousers are sweatpants, used as pull-ons.
4. **Jeans called trousers.** Jil Sander sells denim trousers rather than five-pocket jeans; I counted one as the jean.
5. **Product names that are codes.** Mackage names products with codes (TEE-W, NIDYA-Z); I classified them from their descriptions.
6. **Dead or missing starting links.**
   - Jil Sander's `/en-us/women/clothing`, Ksubi's `/us/collections/womens` and Mackage's `/us/en/women/` are 404s.
   - Boggi Milano renders its listing client-side, so I read it in the tab.
   - The paths I used are in `source`.

## Out of scope but noticed

- **Fabric not stated.** Ksubi's $900 Highway Bomber has no fabric in its description; it may be leather.
- **Leather trim.** Thursday Boot's wool Varsity jacket has leather sleeves, so I left it out of the outerwear high.
