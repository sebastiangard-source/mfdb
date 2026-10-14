# Taxonomy — style and cool-factor segments

Fifteen segments, 370 brands. Rules run in the order shown (R1 to R17), and the first match wins. Hand overrides are listed by name in `segments.csv`, and every one is marked `medium` or `low`. Example brands are high-confidence placements, largest door counts first.

| # | Segment | What a member would understand | Rule from the dials | Brands | Five examples |
|---|---|---|---|---|---|
| 1 | Avant-garde designers | Conceptual designer clothes: odd shapes, deliberate strangeness | R1: avant ≥4 or weird ≥4. Exception: street 5 with avant ≤3 drops through to Hype | 20 | Prada, Balenciaga, Loewe, Maison Margiela, Rick Owens |
| 2 | Hype & drop culture | Streetwear with heat: limited drops, lines, resale | R2: street ≥4 and (status ≥4 or style ≥4) | 25 | Golden Goose, Amiri, Kith, Supreme, Stüssy |
| 3 | Street & sport culture | Sneakers, skate and sportswear worn as street clothes | R3: street ≥4, unless workwear or golf scores higher than street | 9 | Nike, adidas, Vans, Converse, Carhartt WIP |
| 4 | Loud luxury | Luxury you can recognize across a room: logos, monograms | R4: status ≥4 and logo ≥4 | 9 | Louis Vuitton, Gucci, Moncler, Dolce&Gabbana, Versace |
| 5 | Runway houses | The big fashion houses that show each season, logo used sparingly | R5: status ≥4, trueLux, and logo 3 or style 5 | 11 | Saint Laurent, Burberry, Dior, Celine, Valentino |
| 6 | Quiet luxury | Top-end make with nothing on it: cashmere, leather, welted shoes | R6: status ≥4, trueLux, logo ≤2, style ≤4 (ski ≥5 with tech ≥3 drops through to Outdoor) | 11 | Hermès, Brunello Cucinelli, Loro Piana, Tod's, John Lobb |
| 7 | Rock & rebel | Leather jackets, boots, dark denim with a band-poster attitude | R7: rock ≥4 | 8 | Dr. Martens, AllSaints, Zadig & Voltaire, John Varvatos, Schott NYC |
| 8 | Performance & athleisure | Technical fabric for the gym, the run and the commute | R8: tech ≥4, style ≤3, no outdoor/ski/surf ≥4 and no golf/racquet/boat ≥5 | 16 | Lululemon, Vuori, New Balance, On, Rhone |
| 9 | Tailoring & craft | Suits, shirts, welted shoes and mill knitwear, the dressed and particular end | R12: tech ≤3, logo ≤2, street ≤2, golf <4, no workwear/western/outdoor/ski/surf ≥4; fuss ≥2, or fuss 1 with finbro ≥3; plus ital/briish/fren ≥3, finbro ≥3, ivy ≥3 or craft ≥4 | 54 | Zegna, Suitsupply, Allen Edmonds, Kiton, Drake's |
| 10 | Outdoor & coast | Mountain, trail, ski and surf, and the coastal casual built on them | R9: outdoor/ski/surf ≥4 and at or above the prep registers (ties go here when tech ≥4) | 33 | The North Face, Arc'teryx, Patagonia, Faherty, Canada Goose |
| 11 | Prep, club & course | Ivy, country club, golf course and yacht club | R10: prep/ivy/golf/racquet/boat ≥4 and at or above the outdoor registers | 36 | Polo Ralph Lauren, J.Crew, Vineyard Vines, Brooks Brothers, Peter Millar |
| 12 | Heritage & workwear | American and British work, western and denim heritage | R11: workwear or western ≥4 and above both other families; R14: murica 5, or murica 4 with workwear/western ≥3 or craft ≥4 | 27 | Red Wing, Levi's, Filson, Tecovas, RRL |
| 13 | Fashion insider | Designer-led but quiet clothes that menswear enthusiasts know | R15: style ≥4, logo ≤2, and some culture register ≥3 | 33 | A.P.C., Acne Studios, Our Legacy, Lemaire, COS |
| 14 | Mainstream contemporary | Current, well-cut, unremarkable: denim houses, mall and high street | R16: style ≥3 | 41 | Banana Republic, Abercrombie & Fitch, Rag & Bone, Bonobos, PAIGE |
| 15 | Basics & essentials | The tee, the chino, the everyday shoe, from mass to elevated | R13: whitet 5, or whitet 4 with style ≤3 or comfort ≥4 (runs before R14); R17: everything else | 37 | Gap, Buck Mason, James Perse, Clarks, UNTUCKit |

R9 to R11 are a single step: the culture family with the highest score of 4 or more wins. R12 (Tailoring) runs before that step, so Italian tailors with high boat scores (Kiton, Isaia, Zegna) stay in Tailoring. In the table, Tailoring sits at row 9 and the R9 to R11 segments at rows 10 to 12.

## Changes from the 11 October cut

- **Runway houses was redefined rather than merged.** The old rule (status ≥4, trueLux, logo = 3) caught only four houses. The new rule adds style-5 houses with logo ≤2 (Saint Laurent, Celine, Valentino, Tom Ford), which the old cut called Quiet luxury. That gives 11 brands. A member would not call Saint Laurent "quiet," and merging those houses into Quiet luxury would make Quiet luxury mean "expensive." With the change, Quiet luxury keeps its real meaning: Hermès, Loro Piana, Brunello, and the Northampton shoemakers.
- **Heritage American is now Heritage & workwear.** The register is workwear and western, not nationality. Nigel Cabourn, Universal Works and Barbour belong here, and the old name had no place for them.
- **Tailoring & dress is now Tailoring & craft.** It holds welted shoes, shirtmakers and mill knitwear (Alden, Charvet, Johnstons of Elgin) as well as suits. The fuss threshold rose from 1 to 2 (fuss 1 still counts with finbro ≥3), and logo ≤2 is now required. Those two changes removed J.Crew, Southern Tide and the Paris and London designers.
- **Basics & staples is now Basics & essentials.** It gained a tee rule (R13) that catches elevated basics (Buck Mason, Lady White Co., James Perse) before the Heritage and Insider rules can claim them. Band separates mass from elevated in the crosstab.
- **Fashion insider now requires a culture register ≥3.** Without one, a style-4 jean house (Frame, AGOLDE, Rag & Bone) reads as Mainstream.
- **Outdoor and golf now win over Performance.** A technical brand with outdoor/ski/surf ≥4 files as Outdoor, and one with golf ≥5 files as Prep, club & course. Performance keeps the gym, run and commute brands.
- **Every segment has eight or more brands.** None needed merging.
