# craft_audit_2026-10-03 — NOTE

`return.csv` has 204 rows, one per canonical key. `reconcile.py` reports 204 exact names, 0 rewrites and 0 unmatched. The schema check (`validate_return.py`, written for this pass against `schema.json`) reports 0 errors. Nothing here changes a score until Sebastian rules. `proposed_craft` is a proposal only.

**Headline:**

- 199 of 204 rows carry a proposal.
- 119 proposed scores differ from current: 97 down, 22 up.
- 80 match the current score. Ten of those were held at low confidence and are **not** confirmations (listed below).
- 5 rows are `NC`: nobody could read the evidence.

Most moves are downward, and most are one step. Two patterns drive them:

- **Scores that assume a stated country.** Many 2s and 3s assumed a country of make, but the product pages say "Imported" or nothing.
- **5s resting on heritage.** Many 5s rest on heritage, a single owned site, or a process story, not on owned making across the range.

## What was checked

For each brand, the research covered:

- the brand's own about, factories and sustainability pages;
- a sample of product pages, usually 4 to 10, spread across categories;
- filings or annual reports for listed groups (Levi's, Hugo Boss, Moncler, Ferragamo, Canada Goose, Capri, Prada, Christian Dior, Hermès, Cucinelli, Burberry, Armani, Valentino).

Every row's `source` column says what was read and where. Its `note` column gives a confidence level and any contradiction with the worklist.

## What was not reached, or is weak

- **`NC`, not researched:**
  - **Massimo Dutti:** JS shell; inditex.com refused.
  - **Vineyard Vines:** pages unreadable.
  - **Peter Millar:** firewall.
  - **RLX:** no RLX product page reachable on ralphlauren.com.
  - **Brax:** fetch cap hit before the origin text. Start at company.brax.com/en/sustainability.
- **Held at the current score, low confidence, *not* confirmations:**
  - **Site blocked or unreadable** (the brief's rule): Paul Smith, Boggi Milano, John Smedley (homepage only), Bottega Veneta (Kering and brand site blocked).
  - **Thin sample:** 120% Lino, Aspesi, Y.Chroma, Acne Studios (origin in hidden tabs), Comme des Garçons and Junya Watanabe (no product pages on the brand site).
- **Moves resting on thin evidence:**
  - **Dries Van Noten 4→1:** only 2 womenswear product pages, out of 11 products in the store.
  - **Dolce&Gabbana, Fendi and Dior 4→2:** owned making is not established at a primary source, which is not the same as shown absent. A confirmed leather-goods factory would support a 4.
  - **Etro 5→2:** low; only 1 product page read.
  - **Sacai 3→1:** its own pages are silent. Dover Street Market labels say Made in Japan, which would make it a 2 if retailer label data counts.
- **Hidden origin text.** Several fetches could not open collapsed product-page tabs. Where an agent suspected that, `made_in_stated` is NC rather than `none`, and the note says so. A handful of 1s (PAIGE, Diesel, Polo Ralph Lauren) would be 2s if the hidden tab states a country.
- **Repair column.** Coverage of `repair_or_care_program` is uneven. Some rows are NC because the fetch budget ran out.

## What contradicted the existing record

The worklist's `current_reason` was blank for most brands; where it existed, these failed or were overstated:

- **Overstated 5s:**
  - **Levi's:** the 10-K says nearly all product comes from contract makers. Its one company plant is in Epping, South Africa.
  - **Brooks Brothers:** the US factories closed in 2020, and no current owned making was found.
  - **Sunspel:** Long Eaton makes T-shirts only; the rest comes from partners, mostly in Portugal.
  - **Filson:** Seattle makes "core heritage styles" only; many product pages say Imported.
  - **Barbour:** South Shields is one of about 136 finished-goods factories.
  - **Merz b. Schwanen:** a Portuguese partner makes much of the range, and "32 loopwheelers" wasn't found.
  - **Drake's:** owned making is ties (London) and shirts (Chard) only.
  - **Ring Jacket:** the Napoli line is Italian-made by unnamed makers.
  - **Burberry:** Castleford and Keighley cover the signature outerwear and cloth only.
- **Unsupported 5s:**
  - **Sugar Cane:** no sugar-cane fibre on the pages read, and no owned mill.
  - **Visvim:** owns no making; dyeing and kasuri are done by outside workshops.
  - **JiyongKim:** fabrics are new, not "reconstructed vintage", and no maker is named.
  - **Etro:** heritage only; no owned making found after the L Catterton sale.
- **Partly supported 5s:**
  - **Cucinelli:** about 400 independent workshops; Solomeo is design and samples.
  - **Hermès:** owned sites are leather, silk and textiles; owned ready-to-wear making not shown.
  - **Zegna:** owns a mill chain; owned garment plants not confirmed because the 20-F was unreachable.
  - **Brioni:** Penne makes "a large proportion", not all.
  - **Berluti:** the Paris workshops aren't evidenced; Gaibanella (Ferrara) is.
  - **Rubinacci:** the bespoke atelier is shown, but not where ready-to-wear is made.
- **Wrong details in reasons:**
  - **Wax London:** "Portuguese make" appears on 0 of 7 product pages.
  - **Valstar:** made in Veneto and Tuscany, not Milan.
  - **Proper Cloth:** names mills, not makers; it is Vietnam and Thailand by country.
  - **Buck Mason:** Mohnton makes the tees, not all knits.
  - **AYR:** factories are described but never named.
  - **Golden Goose:** about 100 steps, not 16.
  - **Hackett:** the Savile Row bespoke service is not evidence of making.
  - **RRL:** its reason describes design accuracy, not making.
  - **Bode:** one-of-one cutting covers a sub-line only.
  - **Greg Lauren:** owned studio unverified.
  - **Luca Faloni:** product pages give regions but no mill names.
- **Upward finds:**
  - **Canada Goose 3→5:** seven owned Canadian factories; about 75% of volume made in Canada.
  - **Son of a Tailor 2→4:** it owns SON Supply in Santo Tirso, which makes "the majority"; product pages name each maker.
  - **BOSS 2→4:** five owned sites make 17% of volume (Izmir alone 15%).
  - **Lacoste 2→4:** the Troyes factories, about 500 staff.
  - **Rothy's 2→4:** its own Dongguan factory.
  - **Others:** Citizens of Humanity and AGOLDE (company-owned LA and Turkey facilities), Carhartt (four owned US plants for the USA line), Rick Owens (bought its Concordia factory), Celine and Saint Laurent (owned leather workshops only; see rulings).
- **Founding facts.** Several founding details in the worklist's `origin_line` differ from the brands' own sites: Raffi, The Row, Boglioli, 120% Lino, Stefan Brandt (Quito, not Germany), Alex Mill (designer name), Rodd & Gunn, Paul & Shark, Eton.

**I verified directly:**

- Patagonia does not own factories.
- Sunspel's Long Eaton factory makes T-shirts only.
- Son of a Tailor owns SON Supply.
- BOSS's 17% own-production share.
- Lacoste's Troyes factories.
- Dries Van Noten's biography page is silent on making.

The rest rests on agent reads, cited in each row.

## What the brief got wrong, and rulings needed

1. **The swapped note.** No reason in the Proper Cloth / Buck Mason pair was written about the other brand. If the swap was fixed before issue, close this.
2. **Todd Snyder** names mills, not makers. "Names the Italian maker on 321 styles" doesn't match the site or the current reason.
3. **Ruling: leather-goods-only owned making.** Agents treated it as owned making for part of the range, capped at 4. This decides Celine 4, Saint Laurent 4, Gucci 4, Balenciaga 3 and Bottega Veneta 4.
4. **Ruling: factory directories off the product page.** These include supplier lists, Open Supply Hub entries and impact reports (Patagonia, Sunspel, Taylor Stitch, Everlane, Reiss, NN07). They are recorded as `named_makers = some`. Should a directory count toward a 3? Taylor Stitch would go 2→3 if it does.
5. **Ruling: a group-owned retailer's labels.** Dover Street Market is owned by the Comme des Garçons group. Do its labels count as the brand's own statement? This decides CDG, Junya and Sacai.
6. **Ruling: brand-site lists of making countries.** A FAQ or brand-level list of countries, not per product, was scored 2 for Mack Weldon and Our Legacy. Under a stricter reading, Mack Weldon keeps 1.
7. **Ruling: repair run through a partner.** Johnstons (Cashmere Circle) and Tecovas (NuShoe) — should these count as `yes`? This pass used repair, resale and take-back, and excluded care guides alone.
8. **Unnamed but claimed ownership.** Canali (70% in its "own workshops", towns unnamed), Valstar and Incotex (one CEO quote) were proposed 4 with `owned_facility = unclear`.

## How the pass ran

The pass was briefed out in batches. It hit two shared caps:

- **Search:** the session's 200-search cap, which is now exhausted.
- **Fetch:** about 800 page fetches an hour, shared by all agents.

The first wave left 83 brands unread. Those brands were re-run in budgeted waves using page fetches only. Rows from the re-run replace the placeholders, and no placeholder survives as a score: any row with no evidence carries `proposed_craft = NC`.

Some brand and corporate sites refused automated reads: Kering, Gucci, Moncler product pages, John Smedley, Peter Millar and Boggi. Some agents also tried direct report-PDF downloads, which the proxy refused. Those PDFs were read only through fetch summaries, and the affected rows say so.

## Every row where proposed ≠ current, largest moves first

| Brand | Current | Proposed | Move | Confidence | Basis (from `reasoning`) |
|---|---|---|---|---|---|
| Sugar Cane | 5 | 2 | -3 | medium | Sugar Cane documents its denim process in a dated article series (cotton blending, spinning tension, dyeing, weaving on old Toyoda shuttle looms at 29-inch width), but never names a mill or factory, and parent Toyo Enterprise n… |
| Etro | 5 | 2 | -3 | low | Etro's own about page claims a textile origin ('began as a creator of exquisite fabrics', 1968) but names no mill, print works or factory that the house owns today. |
| Visvim | 5 | 2 | -3 | medium | visvim owns no making that its site shows: its dye work is done by an outside workshop in Ome City and its kasuri by Tomihisa Orimono, a named independent weaver. |
| Dries Van Noten | 4 | 1 | -3 | low-medium | The DVN site states no country of make on the PDPs read, and names no workshop, maker or mill. |
| JiyongKim | 5 | 2 | -3 | medium | JiyongKim's product pages say 'Made in Korea' and that each sun-bleached item 'carries a unique imprint of nature and time', but name no maker, workshop or mill. |
| Levi's | 5 | 3 | -2 | medium-high | Levi Strauss & Co.'s FY2024 10-K says it sources 'nearly all' products from independent contract manufacturers in about 28 countries; its only own plant is a manufacturing and finishing plant in South Africa. |
| Taylor Stitch | 4 | 2 | -2 | medium | PDPs give a country of make (mostly China, denim in Vietnam) and construction specs, but no factory or mill. |
| Hiroshi Kato | 4 | 2 | -2 | medium | Kato states all garments are cut, sewn, washed and finished in the USA and the jeans PDP says 'Made In: USA' with Japanese selvedge, but no factory, contractor or mill is named and nothing is owned. |
| Wythe | 4 | 2 | -2 | medium-high | PDPs state country and often the process stage ('knit, cut, sewn and dyed in Portugal'; 'woven in a family owned mill in India'; 'Made in China in a WRAP Gold certified facility'), but no factory or mill is ever named and nothi… |
| RRL | 4 | 2 | -2 | low-medium | RRL PDPs on ralphlauren.com describe vintage-inspired design and trim (corozo buttons, leather zip stoppers, garment dyeing, French corduroy) but the readable ones give origin only as 'Imported'. |
| A Bathing Ape | 3 | 1 | -2 | medium | BAPE's US site gives a founding year and Harajuku origin but names no factory, maker or mill and states no country of make on any sampled product, including in the raw product data. |
| Diesel | 3 | 1 | -2 | low-medium | Diesel's own pages name no factory, maker or mill and the sampled jeans pages show no country of make. |
| Hackett | 4 | 2 | -2 | medium | Hackett PDPs name the cloth's weaving country (England or Italy) and, on premium suits, the mill Loro Piana, but none states where the garment is made or who makes it. |
| Rakho | 3 | 1 | -2 | medium | Rakho's site names no factory, maker, mill or country of make, and does not mention Thames Apparel or China. |
| Brooks Brothers | 5 | 3 | -2 | medium-high | Brooks Brothers proposed closing its three US factories (Garland shirts, Haverhill suits, Long Island City ties) in 2020, was sold out of bankruptcy to Authentic Brands/Simon, and names no factory of its own on its site today. |
| Sid Mashburn | 4 | 2 | -2 | medium-high | Sid Mashburn is a designer-retailer: its about page says it uses luxury brands' mills and makers but names none, and its stores' tailoring shops do alterations, not manufacturing. |
| Billy Reid | 4 | 2 | -2 | high | Billy Reid states a country on every product page sampled: Turkey, Peru, Italy, China. |
| Luca Faloni | 4 | 2 | -2 | medium | Every Luca Faloni product page sampled says the piece is made or knitted in Northern Italy (one names Iseo), but none names a mill or a workshop. |
| Boglioli | 4 | 2 | -2 | low-medium | Boglioli's site places the family and the company in Gambara and speaks of 'our artisans' and signature garment dyeing, but names no factory and never says it owns one. |
| Raffi | 3 | 1 | -2 | medium-high | Raffi's site names no factory or mill and owns none, and its product pages give fibre composition but no country of make. |
| Sease | 4 | 2 | -2 | medium-high | Every PDP sampled says 'Made in Italy' and gives composition plus construction notes (gauge 12 cashmere, yarn-dyed WISH wool, 3-layer heat-taped membrane), but no product names a maker or mill. |
| Ferragamo | 4 | 2 | -2 | medium | Ferragamo's 2024 annual report says production is outsourced entirely to a network of Italian manufacturers, with only product development, industrialisation and quality control kept in-house; its owned Sesto Fiorentino site is… |
| Versace | 4 | 2 | -2 | medium-high | Versace's own former parent described its production as handled by independent third-party contractors, with materials going through a Novara warehouse. |
| Dolce&Gabbana | 4 | 2 | -2 | low-medium | Every men's PDP sampled (shirt, jeans, boots, sneakers) states 'Made in Italy' with composition, and none names a factory, workshop, mill or tannery. |
| Fendi | 4 | 2 | -2 | low-medium | Fendi's men's ready-to-wear PDPs state 'Made in Italy' and composition, and name no maker or mill. |
| McQueen | 4 | 2 | -2 | medium | Every McQueen product page sampled (tailoring, leather, shirts, knit, shoes) says 'Made in Italy' and names no maker, mill or atelier. |
| Sacai | 3 | 1 | -2 | medium | Sacai's own site gives fibre composition on product pages but no country of make, no factory and no mill, and its About page is design philosophy only (Tokyo, 1999). |
| Dior | 4 | 2 | -2 | low-medium | Christian Dior SE's own 2025 annual report (p.14) says Dior sources ready-to-wear and jewelry mainly from outside companies and supplements its leather-goods manufacturing with third-party subcontractors, without naming any own… |
| Golden Goose | 4 | 2 | -2 | medium | Every PDP read (sneaker, suede jacket, jeans) says 'Made in Italy' and names no maker, tannery or mill. |
| Bode | 4 | 2 | -2 | medium-high | Every Bode PDP states a country of make: the main collection is made in India, Peru, Romania and Portugal, with no maker or mill named. |
| Greg Lauren | 4 | 2 | -2 | medium | Every apparel PDP says 'Constructed in Los Angeles', and the brand overview PDF describes the process: vintage garments and army tents are deconstructed, and scraps are pieced into 'Scrapwork' yardage. |
| Ralph Lauren Purple Label | 4 | 2 | -2 | medium | All 6 Purple Label PDPs sampled say Made in Italy, and the tailoring PDPs say 'hand-tailored' with construction detail. |
| Lacoste | 2 | 4 | +2 | medium | Lacoste's savoir-faire page describes its Troyes factories, with 500 staff assembling the polo, and its Made in France pieces say 'Made in France' or 'Made in Troyes' on the product page. |
| Son of a Tailor | 2 | 4 | +2 | high | Son of a Tailor says it owns SON Supply, a factory in Santo Tirso, Portugal, that makes over 55% of its garments, and each product page names the factory: SON Supply for tees and sweatshirts, and named Portuguese partners (Mind… |
| Rothy's | 2 | 4 | +2 | high | Rothy's says on its own blog that it owns and operates its factory in Dongguan, China, and documents the knit-to-shape, outsole moulding and hand strobel steps made there. |
| Canada Goose | 3 | 5 | +2 | medium-high | Canada Goose's own FY25 Modern Slavery Act report says its core down jackets are made in seven owned and operated factories in Winnipeg, Toronto, Scarborough and Montreal, and that 75% of products by volume are made in Canada; … |
| BOSS | 2 | 4 | +2 | high | HUGO BOSS's 2025 annual report says 17% of volume is made in five owned facilities, with Izmir making formalwear and casualwear and Metzingen making Made to Measure suits. |
| Mott & Bow | 3 | 2 | -1 | medium | Mott & Bow's about page says its jeans are made in the Honduras factory the founder's family set up in 1982, but never names that factory or its town, and says the denim itself comes from unnamed Japanese and US mills. |
| J.Crew | 3 | 2 | -1 | low-medium | J.Crew owns no making and names no factories or mills on the responsibility, fabrics or about pages; its 2025 impact report speaks only of suppliers and says roughly 46% of production is in Vietnam. |
| Industry of All Nations | 4 | 3 | -1 | medium | PDPs state the place of make for every item, with a stage-by-stage origin table. |
| Southern Tide | 2 | 1 | -1 | medium | Southern Tide's product pages give fibre content and care but no country of make, factory or mill, and the about page says nothing about making. |
| Criquet | 3 | 2 | -1 | low-medium | Criquet's product copy says 'Designed in Austin, TX' and almost always just 'Imported'; only the Quilted Hoodie names a country (Peru), and no factory or mill is named anywhere I read. |
| Patagonia | 4 | 3 | -1 | high | Patagonia says on its own site that it does not own any factories. |
| Faherty | 3 | 2 | -1 | medium-high | Faherty publishes a list of 13 tier-1 supplier countries, and its product pages carry a country of origin (e.g. |
| johnnie-O | 2 | 1 | -1 | medium-high | Product pages say only 'Imported' with fibre content; no country, factory or mill is named. |
| Percival | 3 | 2 | -1 | high | Every PDP sampled states a country of make (mostly China, also Turkey and Portugal) but names no factory or mill. |
| Wax London | 3 | 2 | -1 | high | PDPs state a country of make (China, Tunisia, Morocco) and composition; only one product names a mill (Deveaux, France). |
| Duck Head | 3 | 2 | -1 | medium | Product pages say 'Imported' or nothing; no country, factory or owned plant is named. |
| Alex Mill | 2 | 1 | -1 | medium | Product pages give composition and sometimes a fabric country ('Portuguese cotton fabric') but no country of make, factory or mill. |
| Robert Barakett | 2 | 1 | -1 | medium | Barakett product pages state composition only, with no country, factory or mill. |
| Easy Mondays | 3 | 2 | -1 | medium-high | Every Easy Mondays product page sampled says 'Handmade in Portugal' in 'GOTS Certified Factories', and the about page says it works with small, family-run Portuguese factories, but no factory, town or mill is named anywhere. |
| Tecovas | 4 | 3 | -1 | medium | Tecovas says its boots are handmade in León, Mexico (over 200 steps, Goodyear welt, hand-laid cording) but never names the workshop or claims to own it. |
| Patrick James | 3 | 2 | -1 | medium-high | Patrick James is a retailer whose own about page says it began as a private-label store and sources from nine countries; it names no factory or mill. |
| Barbour | 5 | 4 | -1 | high | Barbour does own its South Shields factory: its history page says the Bedale and Beaufort wax jackets are still made there by hand, and rewaxing and repairs are done there. |
| Baracuta | 3 | 2 | -1 | medium | Baracuta says its G9 in Baracuta Cloth is still made in the UK, 'now in London', but names no factory and no cloth mill. |
| Filson | 5 | 4 | -1 | high | Filson still runs its own Washington sewing floors (the SoDo flagship and Kent), and some products are labelled 'Made in USA'/'Made at Filson', including the Mackinaw Cruiser. |
| James Perse | 2 | 1 | -1 | low | The brand's own pages say nothing checkable about where clothes are made: PDPs give fabric origin (USA cotton, Italian corduroy) but no country of make, and the only manufacturing text refers to inspected outside 'Suppliers'. |
| Kith | 2 | 1 | -1 | medium | Kith's own-label product pages give composition and fabric weight but, for apparel, no country of make ('See garment tag'); in a sample of seven only a leather card holder said 'Made in Italy'. |
| Aimé Leon Dore | 3 | 2 | -1 | medium-high | Aimé Leon Dore's product pages give a country of make on under half the items sampled (China, Portugal, Italy, USA) and 'Imported' on the rest; fabric copy is generic ('Italian cotton denim') with no mill named. |
| Polo Ralph Lauren | 2 | 1 | -1 | medium | The Polo Ralph Lauren PDPs whose details could be read say only 'Imported' with fibre and care, naming no country, maker or mill. |
| J.McLaughlin | 2 | 1 | -1 | medium-high | Every men's PDP sampled says only 'Imported.' with fibre and care; no country, maker or mill is named. |
| Ted Baker | 2 | 1 | -1 | medium | Five Ted Baker PDPs list fibre content and care but no country of manufacture and no mill. |
| Rails | 2 | 1 | -1 | high | Every Rails product checked says only 'Imported' with fibre content - no country, factory or mill. |
| PAIGE | 2 | 1 | -1 | low | PAIGE says it partners with wash houses and factories 'all around the world' but names none and owns none. |
| Ksubi | 2 | 1 | -1 | medium | Ksubi's FAQ only says its denim comes from unnamed mills in Portugal, Turkey and China. |
| Purple | 2 | 1 | -1 | medium | Purple's about page and FAQ say nothing about where or by whom its clothes are made. |
| Fidelity Denim | 3 | 2 | -1 | medium | Fidelity says it cuts, sews and washes its jeans in Los Angeles and every sampled jean page says Made in the USA, but it names no factory and does not claim to own one. |
| Joe's Jeans | 2 | 1 | -1 | medium | Joe's Jeans' about page gives a founding date and city (2001, Los Angeles) but nothing about who makes the clothes or where; none of the four product pages read states a country of make, a factory or a mill. |
| Eton | 3 | 2 | -1 | medium | Eton's own 2025 sustainability report says all manufacturing is outsourced; the Gånghester site keeps a sample atelier, not production. |
| Eleventy | 3 | 2 | -1 | medium | Eleventy's product pages say Made in Italy on every item sampled and one jacket names its Zegna cloth, but no page names a factory, workshop or mill beyond that, and the site has no about or production page. |
| Borgo28 | 3 | 2 | -1 | high | Borgo28's about page says it works with 'select Italian and Portuguese factories' but names none, and its product pages name neither maker nor mill. |
| J.Press | 4 | 3 | -1 | medium | J.Press says many products are made in America (New York, Massachusetts, Connecticut, Georgia) and elsewhere, but names no factory it owns. |
| Sunspel | 5 | 4 | -1 | high | Sunspel genuinely owns and documents its Long Eaton factory (since 1937), and the Classic T-shirt PDP says it is made there. |
| Merz b. Schwanen | 5 | 4 | -1 | medium-high | Merz b. |
| Isabel Marant | 2 | 1 | -1 | medium | Isabel Marant's men's product pages give composition only: no country of make, factory or mill on any of 6 sampled. |
| Rag & Bone | 2 | 1 | -1 | medium | Rag & Bone's product pages say only 'Imported': no country, mill or factory on any of the 4 sampled (jeans, two shirts, a jacket). |
| A.P.C. | 3 | 2 | -1 | medium | A.P.C. |
| Officine Générale | 3 | 2 | -1 | medium-high | Product pages state a country of make (mostly Portugal; China for a merino knit, Spain for leather) and the fabric's country of origin, but name no factory and no mill. |
| Auralee | 3 | 2 | -1 | medium | Auralee documents its fabrics in detail (fibre grade, weave, finishing, and sourcing regions such as Ichinomiya and Mongolia in its Material Matters stories), but it names no mill or factory, owns none, and its product pages do… |
| Ring Jacket | 5 | 4 | -1 | medium | Ring Jacket's tailoring is made in its own Kaizuka (Osaka) factory, and its jacket PDPs say Made in Japan. |
| Drake's | 5 | 4 | -1 | high | Drake's own pages say its ties are handmade in its East London workshop and its shirts in 'our own shirt factory in Chard, Somerset', and shirt PDPs read 'Made in Our Factory in Somerset'. |
| Thom Browne | 3 | 2 | -1 | medium | Every sampled product states a country of make (mostly Italy, with Ireland and Japan), but no maker, mill or owned facility is named. |
| Burberry | 5 | 4 | -1 | high | Burberry really does own its making for its signature product. |
| Paul & Shark | 3 | 2 | -1 | low | The site dates the Dini family's knitting origin to Maglificio Dacò (1920s) and mentions 'in-house weaving machinery' from the start. |
| Givenchy | 3 | 2 | -1 | low-medium | Givenchy PDPs state origin on every item checked (Italy for trousers, knit shorts and a leather bag; Portugal for a polo), with a traceability block naming countries of weaving and dyeing, but never a maker or mill. |
| Maison Margiela | 3 | 2 | -1 | low-medium | Maison Margiela's men's PDPs state 'Made in Italy' (5/5) and composition, naming no maker or mill. |
| Yohji Yamamoto | 3 | 2 | -1 | medium-high | Every sampled product page on the official shop states a country of make (mostly Japan, but knitwear made in China and one tailored jacket made in Vietnam) and nothing more: no factory, no mill. |
| Amiri | 3 | 2 | -1 | medium-high | Amiri states a country of make on every product checked (USA jeans, Tunisia knitwear, Italy shirts, Vietnam sneakers, China bags) but names no maker or mill. |
| Rhude | 2 | 1 | -1 | medium | Rhude's PDPs give fibre content and care only. |
| Fear of God | 3 | 2 | -1 | medium | Fear of God's mainline product copy states only a country ('crafted in the USA', 'crafted in Italy') and names no factory, maker or mill; the Essentials product data states no origin at all. |
| Zegna | 5 | 4 | -1 | medium | The Zegna Group owns its wool mill in Trivero and a chain of Italian textile and yarn makers (Filiera page names each with acquisition date). |
| Berluti | 5 | 4 | -1 | medium | Berluti PDPs state Made in Italy for shoes and clothing alike but name no maker. |
| Husbands | 3 | 2 | -1 | medium | Every Husbands PDP sampled states a country of make (Italy, Poland, Portugal) and the fabric's country of origin, but none names a maker or mill. |
| Brioni | 5 | 4 | -1 | medium | Brioni says its Penne atelier, opened 1959, still makes 'a large proportion of our production', and press puts about 1,000 tailors across Penne, Montebello di Bertona and Civitella Casanova. |
| The Row | 3 | 2 | -1 | medium-high | The Row's men's PDPs state a country of make on every item sampled (Italy for cashmere jacket, sweater and loafer; Japan for denim and corduroy shirt) with careful fabric descriptions, but name no maker, mill or tannery. |
| Lemaire | 3 | 2 | -1 | medium-high | Lemaire owns no making and names no factories or mills; its about page refers only to unnamed partners in Europe and the Mediterranean. |
| Jil Sander | 3 | 2 | -1 | medium | Every Jil Sander product page checked says 'made in Italy' and nothing more: no factory, maker or mill is named. |
| Wales Bonner | 3 | 2 | -1 | medium | Wales Bonner states a country of make on only some products (the Italian tailoring and loafers). |
| Brunello Cucinelli | 5 | 4 | -1 | medium-high | Cucinelli's own investor site says production 'is entrusted to approximately 400 independent highly-specialised artisan workshops', mostly in Umbria, with design and sampling done at Solomeo by its own team and over 100 tailors. |
| Fedeli | 4 | 3 | -1 | medium | Fedeli's about page dates the family firm to Monza in 1934 and says every stage of production is overseen in Monza. |
| Hermès | 5 | 4 | -1 | medium | Hermès's 2025 Universal Registration Document reports 79 owned production sites and 55% of output from in-house and exclusive workshops, centred on leather goods, tanneries, silk/textiles and other métiers. |
| Rubinacci | 5 | 4 | -1 | low-medium | A 2016 Bloomberg feature describes Rubinacci's own atelier above its Naples store, where about 20 people cut and make bespoke suits. |
| Carhartt | 3 | 4 | +1 | medium | Carhartt's own about page says four Carhartt sewing and cutting facilities in Kentucky and Tennessee make its Made in the USA line, with union workers. |
| Mack Weldon | 1 | 2 | +1 | medium | Mack Weldon names no factory, mill or owned facility; its FAQ states it manufactures in WRAP-certified factories in Thailand, Peru, China, Egypt and Vietnam. |
| Everlane | 2 | 3 | +1 | medium | Everlane owns no factories but publishes a factory directory naming partners with city and country, and some product pages name the factory ('Made at TAL in Vietnam'). |
| Marine Layer | 1 | 2 | +1 | high | Every Marine Layer product page sampled states a country of make ('Made responsibly in China' or 'in Cambodia') plus fibre content, but none names a factory or mill. |
| Bonobos | 1 | 2 | +1 | medium | Bonobos product pages give fibre content and 'Imported' with no country, but a few tailoring items name the cloth mill (Abraham Moon on the Alma Mater blazer, Marzotto on a stretch Italian wool tuxedo). |
| Outerknown | 2 | 3 | +1 | medium | Every rendered PDP states country and region of make (Indonesia, Sri Lanka), denim names Candiani as the mill, and the sustainability page points to a full supplier list on the Open Apparel Registry. |
| Indochino | 2 | 3 | +1 | medium | The /production page names the one factory that makes every garment (Dayang, Dalian, China) and walks through the made-to-measure process (pattern from measurements, laser cutting, sewing, pressing, QC). |
| Madhappy | 1 | 2 | +1 | medium-high | Madhappy's product pages state a country or city of make on most items (core fleece 'Made In Los Angeles', midweight hoodie Canada, knits China), and its fabric guide says where each fabric is knit and garment-dyed (Los Angeles… |
| Norse Projects | 2 | 3 | +1 | medium-high | Norse Projects owns no factory, but product pages name the maker with a short profile: Fontoli (Portugal) for the Oxford shirt, Blupuro Maglierie in Carpi for lambswool knits, Triwool (Portugal) for tees, and state country on m… |
| Vollebak | 2 | 3 | +1 | high | Every Vollebak product page sampled states where the garment was constructed (Romania, Portugal, UK, China, Vietnam) and where the material came from, and several name the mill or material maker (Schoeller, Sesia, Brunello, Alp… |
| AG | 3 | 4 | +1 | low-medium | AG's own sustainability page refers to 'our LA factory and headquarters' and to water-filtration systems in 'our Los Angeles and Mexico factories', and its story page calls it the first vertically operated denim maker on the We… |
| Citizens of Humanity | 3 | 4 | +1 | medium-high | Citizens of Humanity's how-we-are-made page says its jeans are made in company-owned sewing and laundry facilities in Los Angeles (and Turkey), and its denim, trouser, sweatshirt and denim-jacket pages say Made in USA. |
| AGOLDE | 3 | 4 | +1 | medium | AGOLDE's sustainability page says most of its product is made in Los Angeles and Turkey 'at facilities that are owned by us' and describes its own laundry machinery; its jeans, shirt, tee and denim-jacket pages say Made in USA. |
| Ami Paris | 1 | 2 | +1 | medium-high | Ami's product data states a country of make on most items (Romania for tailoring and outerwear, Turkey for leather, Portugal for knits and shirts, Italy for accessories, plus Bulgaria, Spain, Morocco and China). |
| Saint Laurent | 3 | 4 | +1 | low-medium | Trade press reports a Saint Laurent-run leather-goods atelier in Scandicci with more than 500 artisans; this is the brand's own making, inside Kering. |
| Celine | 3 | 4 | +1 | medium | Celine owns two leather goods workshops in Tuscany, at Strada in Chianti (acquired 1994) and Radda in Chianti (opened 2019), run as Celine Production. |
| Rick Owens | 3 | 4 | +1 | medium-high | Owens says the company bought its Concordia sulla Secchia factory, where it has worked with the same people for decades (032c, 2022). |