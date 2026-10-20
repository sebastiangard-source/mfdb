# prices_crossovers_2026-10-15 — batch 20 (last)

Read 16 October 2026. `return.csv` is cumulative and complete: 191 rows (187 crossovers + 4 Pending brands).

## Checks on the full return

| Check | Result |
|---|---|
| `reconcile.py` on all 191 names | all match canonical keys |
| Rows against the worklist | none missing, none extra, no duplicates |
| Empty cells | none |

## Checked

**Reem Acra (Pending) is `done`, but has no prices.**

- The US store lists 1,250 products, almost all runway 'Look' entries, gowns and dresses.
- Their price is $0, so no price is published.
- Only nine products are priced: eight headpieces ($200–$1,600) and one gown at $9,995.
- **Garments.** Every garment is `np`. Tee, jeans and shoes could equally be `NONE`.
- **Band.** True Luxury is a placeholder, based on the one priced gown.

## Status across the whole run

| Status | Rows |
|---|---|
| `done` | 183 |
| `held` | 7 |
| `partial` | 1 |

The seven `held` rows are all bot walls, each named in `note`:

- Vans
- The North Face
- Polo Ralph Lauren
- Hermès
- Columbia
- Salomon (shoes only)
- Massimo Dutti (everything after tees)

## Rulings needed

### The four Pending brands

HANRO, Wacoal, Amsale and Reem Acra don't fit the garment rule (lingerie, loungewear, bridal and evening), so their proposed bands are placeholders.

- **HANRO:** its own store is in EUR, with no US store.

### Brands with too little to band

No blouse or sweater, and no tee at $35 or under:

- **Batches 7–13:** On, Cole Haan, Hoka, Salomon, Thursday Boot and Mackage.
- **Batch 14:** Moose Knuckles, Rapha and Bad Birdie.
- **Batch 16:** Fusalp.
- **Batch 19:** Represent.

### Brands near or across a line

- **Core tee just over $35 (would read Basic with a cheaper logo tee):** Tommy Hilfiger and Calvin Klein.
- **Very close to a band line:** Peserico, Dries Van Noten and Vivienne Westwood.

### Brands where only a weak garment reads (current band proposed unchanged)

- **Vivienne Westwood:** no crewneck sweater.
- **Bally:** capsules excluded.
- **Comme des Garçons:** only the unisex Black CDG line is sold.
- **Off-White:** the only shirts are pajama shirts.
- **Yohji Yamamoto:** its basics read Accessible, while the rest of the range sits at True Luxury.

### Unisex-only women's ranges

- Nanamica
- Black CDG
- Snow Peak (outside its 18 women's pieces)

### Sport-only brands

Golf, ski, running and cycling gear was treated as sport and left out, so several cells are `NONE`. Each `note` gives the values if sport pieces should count.
