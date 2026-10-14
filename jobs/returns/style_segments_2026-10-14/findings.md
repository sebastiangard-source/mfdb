# Findings — style segments against stores, price and the Cyprus universe

Base: 370 brands, 6,584 counted doors (nine NC brands excluded). The proposed Cyprus universe is the 216 brands tiered Anchors, Networks, Luxury houses or Circuits & flagships, holding 4,759 doors.

## Cool factor and store count

At the designer and street end, they run opposite. Median doors per brand: Avant-garde 1, Fashion insider 1.5, Hype 2, against Performance 7.5 and Basics 7. A third or more of insider and avant brands have no US store.

Luxury breaks the pattern. Loud luxury (median 26) and Runway houses (19) carry the highest status and the largest fleets, and every brand in both segments has a store. Rock & rebel (14) is also cool and broadly distributed.

Low cool does not mean many stores: Mainstream contemporary, mostly wholesale denim, has a median of 1.

## What the universe covers

- **Well covered:** luxury (Loud and Runway 20 of 20, Quiet 9 of 11), Tailoring & craft (32 in) and Prep, club & course (25 in).
- **Over-weighted by doors:** Prep, Performance and Heritage hold 21% of universe brands but 44% of its doors. Red Wing (478) and Lululemon (382) drive it. By footprint, the universe reads as boots, leggings and polos.
- **Missed:** street and sport culture. Only 2 of 9 are in (Carhartt WIP and Awake NY, 4 doors), because Nike, adidas, Vans and Converse fall out as Basic. Heritage loses Levi's, Carhartt and Timberland the same way. A price rule ends up removing a style segment.
- **Thin where it counts:** 21 of 33 Fashion insider brands are in, but the purest names are wholesale-only and out: Our Legacy, Lemaire, Auralee, Margaret Howell and Norse Projects. Those in hold 97 doors.
- **The hype end:** it is covered by name (18 of 25 in) but not by footprint. Avant, Hype, Street and Insider together make up 25% of universe brands and 7% of its doors, and Golden Goose is a third of Hype's doors.
- **Tiers-file gaps:** Onward Reserve (14 doors), Undefeated (8), Mollusk (3), Lady White Co. (2), Represent (1) and Pilgrim Surf + Supply (1) have doors but are missing from the tiers file. Zadig & Voltaire (20) still awaits a price read.

## Price by segment (median entry price, USD rows only)

| | Dress shirt | Sweater |
|---|---|---|
| Most expensive | Loud luxury $840, Runway $735, Quiet $678, Avant-garde $625 | Quiet and Runway $1,100, Loud $993, Avant-garde $970 |
| Least expensive | Street & sport $80, Heritage and Outdoor $114, Performance $118 | Street & sport $138, Performance $147, Basics $148 |

At entry, Hype ($250 shirt, $275 sweater) costs less than Tailoring ($310, $420) and Fashion insider ($311, $396), so heat is not a price premium. The 15 `USD_landed` brands are excluded, and seven of them are insider brands. Including them lifts insider to $332 and $420 without changing the order. Street's shirt median rests on 8 brands.

## What a second pass should score

1. **Resale heat (1–5).** `resale_grailed` records whether a Grailed page exists, not whether the brand is hot. It flags 78% of Street and 9% of Runway houses. A score built on resale price retention would separate live heat from legacy names.
2. **Drop cadence (1–5), from seasonal to weekly.** Palace had to be moved by hand: it drops weekly, but style 3 kept it out of Hype. With a cadence dial, the Hype rule would not need overrides.
3. **Press and cultural mention (1–5).** Insider and Mainstream are currently split by judgment. Sandro, a 15-door contemporary chain, and Our Legacy, an enthusiast label, both score logo 1 with a high style dial. Editorial and social mention would separate them.
4. **Men's share of the range.** Mango has 62 doors but 17 carry men's, and Jacquemus and Isabel Marant are women-led. Door totals overstate men's reach without this field.
