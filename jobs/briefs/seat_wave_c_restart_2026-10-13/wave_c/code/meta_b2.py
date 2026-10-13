D = '2026-10-11'
NC = 'NC'

def G(low, lp, lu, high, hp, hu, basis, listing, note=''):
    return dict(low=low, low_product=lp, low_url=lu, high=high, high_product=hp, high_url=hu, basis=basis, mens_listing_url=listing, _note=note)

def NONE_(listing='NONE', note=''):
    return dict(low='NONE', low_product='NONE', low_url='NONE', high='NONE', high_product='NONE', high_url='NONE', basis='NONE', mens_listing_url=listing, _note=note)

def NCG(listing='NC', note=''):
    return dict(low=NC, low_product=NC, low_url=NC, high=NC, high_product=NC, high_url=NC, basis=NC, mens_listing_url=listing, _note=note)

BD = 'https://wearebraindead.com'
BU = 'https://www.buddshirts.co.uk'
CP = 'https://www.cpcompany.com/en-us'
CA = 'https://www.carminashoemaker.com/us/en'
CW = 'https://www.castawayclothing.com'
CL = 'https://www.closed.com'
DN = 'https://www.danner.com'
DT = 'https://denimtears.com'
DE = 'https://deuscustoms.com'
DK = 'https://www.dickies.com/en-us'

COMMON = dict(b_corp=NC, b_corp_entity=NC, gots_certified=NC, gots_entity=NC, pronunciation=NC, read_date=D)
NO_STYLES = dict(styles_total=0, styles_with_composition=0, natural_pct=NC, synthetic_pct=NC, cellulosic_pct=NC, spandex_styles=0, shape=NC,
                 natural_categories='[]', synthetic_categories='[]', colourway_ratio='0/0', style_method='manual', swim_styles=0, swim_share_of_range=NC, mens_styles_excl_swim=0)
M = {}

# ------------------------------------------------------------------------------------------------ Brain Dead
M['Brain Dead'] = dict(
    site_domain='wearebraindead.com', store_used=BD, currency='USD', search_url=BD + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(54, 'Brain Dead Fantasy Fest T-shirt - Black', BD + '/products/brain-dead-fantasy-fest-t-shirt-black', 95, 'Looped Stripe T-shirt - Green Multi (compare-at 95; on sale 47.50)',
              BD + '/products/looped-stripe-t-shirt-green-multi', 'range', BD + '/collections/t-shirt', 'unisex house: /collections/t-shirt is not men-only; several own-line tees sit at 54'),
        polo=G(145, 'Dyed Short Sleeve Boxed Pique Polo - Terracotta (compare-at 145; on sale 72.50)', BD + '/products/dyed-short-sleeve-boxed-pique-polo-terracotta', 145,
               'Dyed Short Sleeve Boxed Pique Polo - Terracotta (compare-at 145)', BD + '/products/dyed-short-sleeve-boxed-pique-polo-terracotta', 'single', BD + '/collections/shirt',
               'only own-line polo in stock; listed under shirts (parent category)'),
        dress_shirt=G(240, 'Nylon Western Shirt - Black (compare-at 240)', BD + '/products/nylon-western-shirt-black', 325, 'Cropped Nylon Button Up Shirt - Army (compare-at 325)',
                      BD + '/products/cropped-nylon-button-up-shirt-army', 'range', BD + '/collections/shirt', 'casual button-fronts only; no dress shirt'),
        jeans=G(265, 'Type 00 15oz Selvedge Denim Pant - Indigo', BD + '/products/type-00-15oz-selvedge-denim-pant-indigo-1', 385, 'Type 02 14.7oz Denim Pant - Light Washed Indigo',
                BD + '/products/type-02-14-7oz-denim-pant-light-washed-indigo', 'range', BD + '/collections/denim', 'Brain Dead x A.P.C. denim (295-375) excluded as collaboration'),
        dress_pants=G(175, 'Brain Dead Equipment Nylon Utility Pant - Black', BD + '/products/brain-dead-equipment-nylon-utility-pant-black', 375, 'Washed Ripstop Climber Pant - Brown (compare-at 375)',
                      BD + '/products/washed-ripstop-climber-pant-brown', 'range', BD + '/collections/pant', 'no dress trouser or chino; non-denim trousers stand in'),
        sweater=G(195, 'Raglan Mock Neck Pullover - White (compare-at 195)', BD + '/products/raglan-mock-neck-pullover-white', 295, 'Hole Mock Neck Pullover - Black (compare-at 295)',
                  BD + '/products/hole-mock-neck-pullover-black', 'range', BD + '/collections/sweater', 'the only crewneck is the Logohead Alpaca Crewneck (89% alpaca, compare-at 275)'),
        outerwear=G(220, 'Brain Dead Equipment Tennis Zip Jacket - Black Mesh', BD + '/products/brain-dead-equipment-tennis-zip-jacket-black-mesh', 500, 'Washed Ripstop Toggle Jacket - Brown (compare-at 500; on sale 250)',
                    BD + '/products/washed-ripstop-toggle-jacket-brown', 'range', BD + '/collections/jacket', 'Brooks Brothers California blazer (700) excluded as collaboration'),
        shoes=NONE_(listing=BD + '/collections/footwear', note='every shoe on the store is a collaboration (adidas, Crocs, Coach, Andersson Bell): no own-label shoe, NONE under the 11 Oct ruling')),
    own_doors_us=5, own_doors_world=7, locator_url=BD + '/pages/stores',
    doors_basis="brand's stores page: Studios (Fairfax LA), Fabrications (Sunset LA), New York, Portland, Long Beach Rising (US); Studios Harajuku and Shibuya PARCO (Tokyo). Long Beach counted as own-door under the 10 Oct ruling (listed as 'BRAIN DEAD @ LONG BEACH RISING'), flagged",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=BD + '/products/washed-ripstop-toggle-jacket-brown', proposed_tech=NC,
    owned_facility='no claim found (about page and 64 site pages read)',
    named_makers='no',
    named_mills='no: denim and shirting "sourced from Japan", mill not named',
    made_in_stated_share='48/71 own-line clothing listings state where made (Portugal and Peru on knits and tees; denim "Cut and sewn in Los Angeles, CA")',
    heritage_claim='none on site: about page is undated and unplaced',
    process_documented='partial: denim pages list Japanese denim, cut-and-sew and leather patch in Los Angeles, hardware made in Japan, sanforized right-hand twill',
    craft_url_1=BD + '/products/type-00-15oz-selvedge-denim-pant-indigo-1', craft_url_2=BD + '/pages/about-us', proposed_craft=2,
    craft_reasoning='Two thirds of the own-line listings state where they are made, and the denim pages say what is cut and sewn in Los Angeles and what comes from Japan. No maker, mill or facility is named and the brand gives no founding story on its own site.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    lookbook_found='no', lookbook_season_label='NONE', lookbook_mens='NONE', lookbook_url='NONE',
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=542734&catalog[]=5', vinted_brand_ids='542734', grailed_url='https://www.grailed.com/designers/brain-dead',
    quote='Brain Dead is ultimately about people, their cultures, and their attitudes.', quote_who='the house, about page', quote_source='wearebraindead.com /pages/about-us',
    quote_url=BD + '/pages/about-us', quote_date='undated page (read 2026-10-11)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: wearebraindead.com products.json (294 products), 71 own-line PDPs (SPECS Material), /pages/stores, /pages/about-us, sitemap pages, /collections.json',
    note='Style split (11 Oct ruling): styles_total 132 = 63 own-line styles (71 listings) + 69 collaboration styles (81 listings: adidas, Coach, Brooks Brothers California, A.P.C., UD Ibiza, Magic: The Gathering, Disney, Star Wars, Sound & Fury and others), so collaborations are 52% of the clothing. Fibre figures, colourway_ratio and the style table cover the own line only; mens_styles_excl_swim adds the 68 non-swim collaboration styles (one collaboration swim trunk). Long Beach door kept as own door, flagged (brand name on the listing; hours suggest a host site). Kids, dresses and skirts excluded. Mark on site: Brain Dead (stores page writes BRAIN DEAD).')

# ------------------------------------------------------------------------------------------------ Budd
M['Budd Shirtmakers'] = dict(
    site_domain='buddshirts.co.uk', store_used=BU + ' (Shopify, USD presentment; no US domain)', currency='USD', search_url=BU + '/search?q=', feed_currency_rate='1.3501638', sublines_included='-',
    g=dict(
        tee=NONE_(note='the tees on the store are Zimmerli (third-party), not counted'), polo=NONE_(),
        dress_shirt=G(310, 'Tailored Fit Plain Pinpoint Oxford Button Cuff Shirt in White', BU + '/products/tailored-fit-plain-pinpoint-oxford-button-cuff-shirt-in-white', 557,
                      'Classic Fit Plain Soyella Double Cuff Shirt in Sky Blue', BU + '/products/classic-fit-plain-soyella-double-cuff-shirt-in-sky-blue', 'range', BU + '/collections/business-shirts',
                      'day shirts; poplin staple is 321; evening dress shirts run to 782 (hand-pleated voile); outlet shirts are login-gated and not counted; feed = page on two products (321, 563)'),
        jeans=NONE_(), dress_pants=NONE_(),
        sweater=G(563, 'Scottish Cashmere Crewneck Sweater in Burlington Blue', BU + '/products/scottish-cashmere-crewneck-sweater-in-burlington', 1007,
                  'Bowhill Scottish Cashmere Cable Knit Jumper in Blackberry', BU + '/products/bowhill-scottish-cashmere-cable-knit-jumper-in-blackberry', 'pair', BU + '/collections/knitwear',
                  'entry is already cashmere; high is the dearest cashmere jumper (named judgement)'),
        outerwear=NONE_(note='jackets (Pure Cashmere Safari Jacket 1570, English Wool Flannel Safari Jacket 1007, Chore Jacket 895) are typed shirts and cut as shirt-jackets: excluded from outerwear (agreed 11 Oct: a jacket sold as a shirt is a shirt); two Safari Jackets and the Chore Jacket listed here so the slot can be revisited'),
        shoes=NONE_()),
    own_doors_us=0, own_doors_world=1, locator_url=BU + '/pages/our-store',
    doors_basis="brand's store page: one shop, 3 Piccadilly Arcade, London SW1Y 6NH (since 1910); US presence is trunk shows only (/pages/usa-trunk-shows)",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=BU + '/pages/what-makes-a-budd-shirt', proposed_tech=NC,
    owned_facility='yes, evidenced: "We make our shirts at our workshop in Andover, under the guidance of Di Bainbridge and Gwenda Witts. They joined the company in 1969 and 1976" (/pages/our-workshop); boxer shorts "Made at our Andover workshop"; silk pyjama cloth "washed at our Andover workshop"',
    named_makers='own workshop named (Andover); knitwear says "Made in Scotland" without naming the knitter',
    named_mills='yes: Alumo (Swiss poplin, boxer cloth), Thomas Mason, Loro Piana (cashmere yarn, linen cloth), Solbiati, Fox Brothers (flannel gowns), Holland (herringbone) named on product pages',
    made_in_stated_share='MADEIN_BU', heritage_claim='dated and placed: "since its foundation in 1910 ... the heart of Jermyn Street in the Piccadilly Arcade since day one"; founder Harold Budd (/pages/about-us)',
    process_documented='partial: finishing-board inspection at Andover, hand-piped nightwear, hand-pleated dress shirts, 2-fold 100s poplin described on product pages',
    craft_url_1=BU + '/pages/our-workshop', craft_url_2=BU + '/products/tailored-fit-plain-poplin-button-cuff-shirt-in-pink', proposed_craft=4,
    craft_reasoning='Budd names its own Andover workshop and the two long-serving staff who run it, and product pages name the cloth mills (Alumo, Thomas Mason, Loro Piana). Shirts and nightwear come from that workshop; knitwear and some cloth goods are bought in without a named maker, so it stops at 4.',
    founded_year=1910, founded_place='Piccadilly Arcade, London', founders='Harold Budd', owner_today=NC, ownership_url=NC,
    lookbook_found='no', lookbook_season_label='NONE', lookbook_mens='NONE', lookbook_url='NONE',
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='NONE',
    quote="No nonsense design. That's the philosophy.", quote_who='the house, workshop page ("Meet the designer")', quote_source='buddshirts.co.uk /pages/our-workshop',
    quote_url=BU + '/pages/our-workshop', quote_date='undated page (read 2026-10-11)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: buddshirts.co.uk products.json (2069 products), 184 full-price PDP descriptions (two passes), /pages/our-workshop, /pages/about-us, /pages/our-store, /pages/usa-trunk-shows, sitemap pages',
    note='Style layer = full-price in-stock clothing: 184 listings / 102 styles. Outlet products (tag Outlet, 130) require a customer login to view and are not counted. Excluded: 332 made-to-measure cloth listings, studs/half suites, bib fronts and waistcoat slips, Zimmerli. Most compositions are a fibre named in prose without a percentage ("2-fold cotton poplin"); 29 styles name no fibre. Mark: Budd (ruled). Vinted and Grailed carry no Budd brand page.')

# ------------------------------------------------------------------------------------------------ C.P. Company
M['C.P. Company'] = dict(
    site_domain='cpcompany.com', store_used=CP + '/ (Salesforce Commerce Cloud, US site)', currency='USD', search_url=CP + '/search?q=', feed_currency_rate='not shopify',
    sublines_included='Metropolis Series (own section of the C.P. Company store, counted)',
    g=dict(
        tee=G(140, '30/1 Jersey Short Sleeve Logo Label T-Shirt', CP + '/green-30-1-jersey-short-sleeve-logo-label-t-shirt/21CMTS723A005100W697.html', 330, '20/1 Jersey Boxy Long Sleeve Logo T-Shirt',
              CP + '/silver-20-1-jersey-boxy-long-sleeve-logo-t-shirt/21CMTS162A005697G120.html', 'range', CP + '/shop/main-collection/clothing/t-shirts-polos/', 'listing mixes tees and polos (parent category)'),
        polo=G(185, 'Metropolis Series Stretch Piquet Short Sleeve Polo', CP + '/green-metropolis-series-stretch-piquet-short-sleeve-polo/21CLPL044A005263W661.html', 215, 'Stretch Piquet Long Sleeve Zip Polo',
               CP + '/grey-stretch-piquet-long-sleeve-zip-polo/21CMPL152A005263W985.html', 'range', CP + '/shop/main-collection/clothing/t-shirts-polos/', 'Tennis kit polos (250) are a capsule, not taken as high'),
        dress_shirt=G(435, 'Corduroy Long Sleeve Lens Button Shirt', CP + '/grey-corduroy-long-sleeve-lens-button-shirt/21CMSH147A006410O950.html', 475, 'Organic Gabardine Long Sleeve Lens Hidden Zip Shirt',
                      CP + '/green-organic-gabardine-long-sleeve-lens-hidden-zip-shirt/21CMSH145A110143G683.html', 'range', CP + '/shop/main-collection/clothing/shirts/', 'two casual shirts only'),
        jeans=NONE_(note='no five-pocket jean; the Bull Denim No Side Seams Pants (330) is a denim-cloth trouser'),
        dress_pants=G(360, 'Cotton Gabardine No Side Seams Pants', CP + '/beige-cotton-gabardine-no-side-seams-pants/21CMPA060A110458G340.html', 475, 'Micro-Reps No Side Seams Pants',
                      CP + '/grey-micro-reps-no-side-seams-pants/21CMPA059A110324G985.html', 'range', CP + '/shop/main-collection/clothing/trousers/', 'chinos stand in; cargo pants run to 580'),
        sweater=G(330, 'Full Rib Cotton Lens Crewneck Sweater', CP + '/blue-full-rib-cotton-lens-crewneck-sweater/21CMKN101A006608A871.html', 510, 'Merino Wool Re-Colour Lens Crewneck Sweater',
                  CP + '/brown-merino-wool-re-colour-lens-crewneck-sweater/21CMKN046A003247SR30.html', 'range', CP + '/shop/main-collection/clothing/knitwear/', 'no crewneck in an elevated fibre'),
        outerwear=G(700, 'C.P. Shell-R Goggle Jacket', CP + '/beige-c.p.-shell-r-goggle-jacket/21CMOW700A006097A356.html', 2795, 'Leather Goggle Jacket',
                    CP + '/brown-leather-goggle-jacket/21CMOW305A110457L380.html', 'range', CP + '/shop/main-collection/clothing/jackets-coats/',
                    'same Goggle style in leather; filed as range because leather is not on the elevated list; gilets from 580; the 2795 Montone Curly shearling is fur, excluded'),
        shoes=NONE_(listing=CP + '/shop/main-collection/accessories/shoes/', note='all footwear is collaborative (ASICS x C.P. Company GEL-QUANTUM 360 I 200; Moonstar Mais B 255-310): no own-label shoe, NONE under the 11 Oct ruling')),
    own_doors_us=0, own_doors_world=19, locator_url=CP + '/stores/',
    doors_basis='Stores-FindStores endpoint queried at radius 20000 from New York, Tokyo, Milan and Sydney: 23 locations, none in the US; 19 own doors, 1 outlet (Gotemba Premium Outlets), 3 in department stores (Réel Shanghai, Hankyu Mens Osaka, Osaka Takashimaya)',
    tech_named_fabrics='TECH_CP', tech_owned_or_licensed='house-named fabrics (Chrome-R, Shell-R, D.D. Shell, Nycra-R, Flatt Nylon, Micro Kei, Metro-Tek, Micro-Tek) plus licensed PrimaLoft® and GORE-TEX (Gore G-Type)',
    tech_share_of_range='TECHSHARE_CP', tech_evidence_url=CP + '/garment-dyeing.html', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no', named_mills='no: fabrics carry house names, mills not named',
    made_in_stated_share='MADEIN_CP',
    heritage_claim='dated and placed: "In 1971, Osti founded Chester Perry ... In 1978, Chester Perry became C.P. Company" in Bologna (/en-us/our-story.html)',
    process_documented='yes: garment dyeing explained step by step against piece dyeing, with the 1970s origin and the 2005 first garment-dyed GORE-TEX (/en-us/garment-dyeing.html); product passport gives the weaving, dyeing and confection country for each product',
    craft_url_1=CP + '/garment-dyeing.html', craft_url_2=CP + '/our-story.html', proposed_craft=3,
    craft_reasoning='C.P. documents its signature process (garment dyeing) in detail and publishes a passport with the weaving, dyeing and sewing country for nearly every product. It names no factory or mill and owns no facility on the evidence read, so 3 rests on process and supply-chain disclosure rather than named making.',
    founded_year=1971, founded_place='Bologna', founders='Massimo Osti (as Chester Perry; renamed C.P. Company 1978)', owner_today='Tristate International S.A., Lugano (named on the corporate information page)',
    ownership_url=CP + '/corporate-information.html',
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=73952&catalog[]=5', vinted_brand_ids='73952', grailed_url='https://www.grailed.com/designers/c-p-company',
    quote='a garment, usually made from white or raw, uncoloured fabric, is dyed only as a final manufacturing step, after being fully fashioned',
    quote_who='the house, garment dyeing page', quote_source='cpcompany.com /en-us/garment-dyeing.html', quote_url=CP + '/garment-dyeing.html', quote_date='undated page (read 2026-10-11)',
    signature_product='Goggle Jacket (the house runs a dedicated Goggle Jacket page)', signature_product_url=CP + '/shop/focus-on/goggle-jacket/', status='partial',
    source=f'Chrome {D}: cpcompany.com/en-us Main Collection clothing (?sz=500, 181 tiles) and 10 sub-categories, Metropolis Series (34), 215 PDPs (Composition, Product passport), Stores-FindStores, our-story, garment-dyeing, corporate-information',
    note='Style = data-pid style code (each listing tile is one style with colours inside, so colourway_ratio reads 1.00 by construction). Excluded: Alessi collaboration overshirt, tennis bag, one duplicate tennis-shorts colour. Main fabric = EXTERNAL MAIN FABRIC / External fabric (linings, padding and coatings cut).')

# ------------------------------------------------------------------------------------------------ Carmina
M['Carmina'] = dict(
    site_domain='carminashoemaker.com', store_used=CA + ' (US/English store, USD)', currency='USD', search_url=NC, feed_currency_rate='not shopify', sublines_included='-',
    g=dict(tee=NONE_(), polo=NONE_(), dress_shirt=NONE_(), jeans=NONE_(), dress_pants=NONE_(), sweater=NONE_(), outerwear=NONE_(),
           shoes=G(475, 'Penny Loafers 80160 Xim (navy repello)', CA + '/penny-loafers-navy-repello-80160', 1125, "Men's Penny Loafers 793 Chelsea (burgundy cordovan)",
                   CA + '/cordovan-penny-loafers-burgundy-000793', 'pair', CA + '/mens-loafers',
                   'all 156 men\'s loafers read across 8 pages (data-product basePrice = displayed price on 24 tiles checked); alligator loafers (3090-3990) excluded as exotic skin; several cordovan loafers at 1125; 474.99 on file')),
    own_doors_us=2, own_doors_world=9, locator_url=CA + '/carmina-stores',
    doors_basis="brand's stores page: New York (45 E 45th St) and San Francisco (54 Geary St) in the US; Madrid, Barcelona, Palma, Paris, London, Luxembourg, Tokyo; the Inca store is the Carmina Outlet (not counted)",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=CA + '/shoemaking', proposed_tech=NC,
    owned_facility='claim, dated: "Our family manufactures all shoes on the island of Mallorca since 1866"; 1905 "one of the first factories of Goodyear-stitched shoes in the Balearic Islands" (/history); factory not named or pictured in this read',
    named_makers='own manufacture claimed (Inca, Mallorca)', named_mills=NC, made_in_stated_share=NC,
    heritage_claim='dated and placed: 1866 Matías Pujadas workshop in Inca; 1997 Carmina Shoemaker founded by José Albaladejo; first store Madrid 1998 (/history)',
    process_documented='yes: "The whole manufacturing process includes over 190 steps"; Goodyear welting (/shoemaking)',
    craft_url_1=CA + '/history', craft_url_2=CA + '/shoemaking', proposed_craft=4,
    craft_reasoning='Carmina states that the family makes every shoe on Mallorca and dates the line of shoemakers from 1866, with a documented 190-step process. The factory is claimed rather than shown in this read and product pages were not checked for leather sources, so 4 not 5.',
    founded_year=1997, founded_place='Mallorca', founders='José Albaladejo Pujadas, with his wife and sons (family shoemaking since 1866)', owner_today=NC, ownership_url=NC,
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='https://www.grailed.com/designers/carmina',
    quote='Our family manufactures all shoes on the island of Mallorca since 1866.', quote_who='the house, history page', quote_source='carminashoemaker.com /us/en/history',
    quote_url=CA + '/history', quote_date='undated page (read 2026-10-11)',
    signature_product='Loafer Mod. 1330 (launched 1962; the history page calls it iconic)', signature_product_url=CA + '/history', status='partial',
    styles=NO_STYLES,
    source=f'Chrome {D}: carminashoemaker.com/us/en /mens-loafers pages 1-8 (data-product JSON), /carmina-stores and store pages, /physicalLocation/stores, /history, /shoemaking',
    note='Shoe-only house: seven garment slots NONE and no clothing style table. Search URL not tested.')

# ------------------------------------------------------------------------------------------------ Castaway
M['Castaway Nantucket Island'] = dict(
    site_domain='castawayclothing.com', store_used=CW, currency='USD', search_url=CW + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(48, 'Beach Tee Mint Castaway (compare-at 48; on sale 26.99)', CW + '/products/beach-tee-mint-castaway', 48, 'Beach Tee Mint Castaway (compare-at 48)', CW + '/products/beach-tee-mint-castaway',
              'single', CW + '/collections/mens-tee-shirts', 'only in-stock tee; compare-at not confirmed by a full-price listing'),
        polo=G(110, 'Onshore Polo Shirt Pink (compare-at 110)', CW + '/products/onshore-polo-shirt-pink', 110, 'Terry Cloth Polo Navy Stripe (compare-at 110)', CW + '/products/terry-cloth-polo-navy-white-stripe',
               'range', CW + '/collections/mens-tops', 'both polos marked down; parent listing'),
        dress_shirt=G(138, 'Chase Shirt Orange & Blue Seersucker (full price)', CW + '/products/chase-shirt-orange-blue-seersucker', 168, 'Straight Wharf Shirt White Oxford with Shamrock (full price)',
                      CW + '/products/oxford-straight-wharf-shirt-white-oxford-kelly-shamrock', 'range', CW + '/collections/mens-sport-shirts', 'sport shirts only; compare-ats vary inside the Chase model (138-168)'),
        jeans=NONE_(),
        dress_pants=G(138, 'Harbor Pant Stretch Twill Blue Storm (full price)', CW + '/products/harbor-pant-stretch-twill-blue-storm', 185, 'Beachcomber Corduroy Pant Nantucket Navy with Snowman Sledding (full price)',
                      CW + '/products/beachcomber-corduroy-pant-nantucket-navy-with-snowman-sledding', 'range', CW + '/collections/mens-pants', 'chinos stand in; embroidered pants carry the higher prices'),
        sweater=G(145, 'Yachtsman Crewneck Sweater (compare-at 145 on all five colours; on sale 59.99-98.99)', CW + '/products/yachtsman-crewneck-sweater-seafoam', 215, 'Scottish Shetland Crew Neck Sweater Oatmeal (compare-at 215)',
                  CW + '/products/shetland-crew-neck-sweater-oatmeal', 'range', CW + '/collections/mens-tops', 'both crewnecks marked down; compare-ats consistent across colours'),
        outerwear=G(135, 'Tidal Wind Vest Moss Green (compare-at 135)', CW + '/products/tidal-wind-vest-moss-green', 295, 'Mariner Jacket Seapoint Patch Madras (compare-at 295)',
                    CW + '/products/mariner-jacket-seapoint-patch-madras', 'range', CW + '/collections/mens-tops', 'sport coats and blazers (Philip 595, Spinnaker 395, Tweedbank 485) excluded'),
        shoes=NONE_()),
    own_doors_us=0, own_doors_world=0, locator_url=CW + '/apps/store-locator',
    doors_basis='ruled 10 Oct: no Castaway-banner door; Murray\'s Toggery Shop (62 Main Street, Nantucket) is a stockist row (other brand own door)',
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=CW + '/pages/about-us', proposed_tech=NC,
    owned_facility='no claim', named_makers='no', named_mills='no ("Authentic Patch Madras", no mill)', made_in_stated_share='MADEIN_CW',
    heritage_claim='vague: no founding date or place on the site; about page speaks of "a truly American style"', process_documented='no',
    craft_url_1=CW + '/pages/about-us', craft_url_2=CW + '/products/harbor-pant-stretch-twill-blue-storm', proposed_craft=1,
    craft_reasoning='Product pages give composition and the word "Imported" but no country, maker or mill, and the about page gives no dated history. Nothing about the making can be checked.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='NONE',
    quote='At Castaway, we are preserving a truly American style, born at beach bonfires and aboard anything that floats.', quote_who='the house, about page',
    quote_source='castawayclothing.com /pages/about-us', quote_url=CW + '/pages/about-us', quote_date='undated page (read 2026-10-11)',
    signature_product='Cisco Short (embroidered short with its own page)', signature_product_url=CW + '/pages/cisco-shorts', status='partial',
    source=f'Chrome {D}: castawayclothing.com products.json (676), 58 style PDPs (Fabric & Care), /apps/store-locator stores endpoint (145 rows), /pages/about-us, /pages/our-story (empty), collections.json',
    note='Style = SKU model + fabric (first two SKU segments): embroidery variants collapse (302 listings / 58 styles). Excluded: MENS OUTLET types, ladies, boys, accessories, and third-party vendors (Murray\'s Toggery, Smathers & Branson, Holebrook, etc.). The house writes compositions as "98/2 Cotton/Stretch"; "Stretch" filed as elastane. Site search renders client-side (server HTML returned no tiles). Mark: Castaway Nantucket Island (footer).')

# ------------------------------------------------------------------------------------------------ Closed
CLP = CL + '/products/'
M['Closed'] = dict(
    site_domain='closed.com', store_used=CL + ' (Global-e: United States / USD selected; duties included; copy in German)', currency='USD_landed', search_url=NC, feed_currency_rate='not shopify', sublines_included='-',
    g=dict(
        tee=G(85, 'T-Shirt aus Baumwolle (white)', CLP + 'men-t-shirts-und-sweatshirts-t-shirt-aus-baumwolle-white-c85588-40d-22-200.html', 125, 'Gestreiftes T-Shirt (black)',
              CLP + 'men-t-shirts-und-sweatshirts-gestreiftes-t-shirt-black-c85026-45a-st-100.html', 'range', CL + '/men/tshirts', 'USD as displayed by Global-e on the listing tiles'),
        polo=G(165, 'Gestreiftes Polo-Shirt (espresso brown)', CLP + 'men-t-shirts-und-sweatshirts-gestreiftes-polo-shirt-espresso-brown-c85229-45a-st-765.html', 165, 'Gestreiftes Polo-Shirt',
               CLP + 'men-t-shirts-und-sweatshirts-gestreiftes-polo-shirt-espresso-brown-c85229-45a-st-765.html', 'single', CL + '/men/tshirts', 'only jersey polo; knitted polos sit in knitwear; parent listing'),
        dress_shirt=G(220, 'Button-Down-Hemd aus Bio-Baumwolle (dark night)', CLP + 'men-hemden-button-down-hemd-aus-bio-baumwolle-dark-night-c84271-20f-20-568.html', 275, 'Hemd aus Baumwoll-Chambray (dark night)',
                      CLP + 'men-hemden-hemd-aus-baumwoll-chambray-dark-night-c84938-20j-20-568.html', 'range', CL + '/men/hemden', 'casual shirts only'),
        jeans=G(255, 'Slim Jeans - Unity Slim (black)', CLP + 'men-jeans-slim-jeans-unity-slim-black-black-c31102-02g-2l-bbk.html', 425, 'Regular Jeans - Cooper True (mid blue, 05K denim)',
                CLP + 'men-jeans-regular-jeans-cooper-true-mid-blue-c31205-05k-4c-mbl.html', 'range', CL + '/men/jeans', 'USD differs by colour on some models (Cooper True 05K: 330 and 425)'),
        dress_pants=G(315, 'Regular Pants - Vigo Formal (dark night)', CLP + 'men-hosen-regular-pants-vigo-formal-dark-night-c31345-37a-22-568.html', 355, 'Relaxed Wool Pants - Fairport Relaxed (espresso brown)',
                      CLP + 'men-hosen-relaxed-pants-fairport-relaxed-espresso-brown-c31600-55d-22-765.html', 'range', CL + '/men/hosen', ''),
        sweater=G(295, 'Crewneck aus Wolle (rock beige)', CLP + 'men-strick-crewneck-aus-wolle-rock-beige-c86439-98u-22-920.html', 745, 'Kaschmir-Pullover (dark night)',
                  CLP + 'men-strick-kaschmir-pullover-dark-night-c86381-99l-22-568.html', 'pair', CL + '/men/strick', 'wool crewneck vs 100% cashmere pullover'),
        outerwear=G(385, 'Atelier-Jacke aus Cord (rock beige)', CLP + 'men-jacken-und-maentel-atelier-jacke-aus-cord-rock-beige-c87800-38y-am-920.html', 1340, 'Doubleface-Mantel aus Woll-Mix (black melange)',
                    CLP + 'men-jacken-und-maentel-doubleface-mantel-aus-woll-mix-black-melange-c87444-65g-22-177.html', 'range', CL + '/men/jacken',
                    'the dark-night colour of the same coat shows 940; shearling (Lammfell) jackets 2145-2290 excluded as fur'),
        shoes=NONE_()),
    own_doors_us=0, own_doors_world=30, locator_url=CL + '/stores',
    doors_basis="brand's stores page: 30 stores (Germany 21, Belgium 3, Netherlands 2, Switzerland 2, Austria 1, Spain 1), none in the US; 7 are women's-only stores, counted and flagged womens-only (11 Oct ruling); Münster and both Zürich stores are operator-run (store e-mails at viehoff.com and bollag.net), flagged",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=CLP + 'men-hosen-regular-pants-vigo-tapered-light-grey-melange-c31245-353-22-127.html', proposed_tech=NC,
    owned_facility='no claim found',
    named_makers='yes: 188 of 221 men\'s product pages name the production partner in a "Produktion" note (Pan-Ko, Istanbul, trousers, since 1993; Income SPA, Italy, denim, since 1951; Esvap, Istanbul, knitwear; Aten, Shanghai, knitwear; Suntex, Istanbul, sweats; Texdata, Romania; Mundicorte, Portugal, shirts, since 1975; Global Textile, Turkey; Otto, Istanbul, leather; Union Apparel, denim)',
    named_mills='no', made_in_stated_share='MADEIN_CL',
    heritage_claim='none on site: no about or history page (/about, /ueber-uns, /history, /geschichte, /unternehmen all 404)',
    process_documented='partial: each partner note describes what the factory makes and for how long',
    craft_url_1=CLP + 'men-hosen-regular-pants-vigo-tapered-light-grey-melange-c31245-353-22-127.html', craft_url_2=CLP + 'men-jeans-relaxed-jeans-shoreham-wide-dark-blue-c31229-12k-2h-dbl.html', proposed_craft=3,
    craft_reasoning='Closed names the factory behind nearly every product (Pan-Ko for trousers, Income for denim, Esvap and Aten for knitwear) and states the country on all of them. It owns no facility on the evidence read and names no mills, which is the rubric\'s 3.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=CL + '/impressum',
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=17919&catalog[]=5', vinted_brand_ids='17919', grailed_url='https://www.grailed.com/designers/closed',
    quote='NONE', quote_who='NONE', quote_source='NONE', quote_url='NONE', quote_date='NONE',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: closed.com /men pages 1-6 (248 products), 221 PDPs (Material & Pflege, Made in, Produktion), listing tiles in USD via Global-e, /stores, /impressum',
    note='Style = model + fabric code (C31245-353): 221 colourway listings / 121 styles; 27 accessories excluded. HTML and ld+json carry EUR; Global-e sets US prices per product (not a single rate), so every USD figure was read off the displayed tiles. Impressum names the operating company Closed Direct GmbH, Hamburg (managing director Dieter Holzer); owner not stated. Quote NONE: no about page on the site.')

# ------------------------------------------------------------------------------------------------ Danner
M['Danner'] = dict(
    site_domain='danner.com', store_used=DN, currency='USD', search_url=NC, feed_currency_rate='not shopify', sublines_included='-',
    g=dict(
        tee=G(26, 'Danner License Plate Tee', DN + '/danner-license-plate-tee.html', 65, 'Danner 10.5oz Heavy Weight Pocket Tee (made in USA)', DN + '/danner-10-5oz-heavy-weight-pocket-tee-glazed-ginger.html',
              'range', DN + '/danner-apparel/shirts', 'apparel is largely unisex sizing; listing not men-only'),
        polo=NONE_(),
        dress_shirt=G(210, 'Danner Cedar Mill Cotton Flannel (black plaid)', DN + '/danner-cedar-mill-cotton-flannel-black-plaid.html', 280, "Men's Cedar Mill Cotton Flannel (Japanese flannel, navy/olive tartan)",
                      DN + '/men-s-cedar-mill-cotton-flannel-navy-olive-tartan-plaid.html', 'range', DN + '/danner-apparel/button-downs', 'flannel shirts, made in USA'),
        jeans=G(220, "Men's Kenton Double Knee Pants Denim Dark Wash Indigo", DN + '/men-s-kenton-double-knee-pants-denim-dark-wash-indigo.html', 220, "Men's Kenton Double Knee Pants Denim",
                DN + '/men-s-kenton-double-knee-pants-denim-dark-wash-indigo.html', 'single', DN + '/danner-apparel/bottoms', 'the only denim trouser is a double-knee work pant'),
        dress_pants=G(160, "Men's Pleated Forager Pants (golden brown)", DN + '/men-s-pleated-forager-pants-golden-brown.html', 220, 'Danner Kenton Double Knee Pants (olive duck canvas)',
                      DN + '/danner-kenton-double-knee-pants-olive.html', 'range', DN + '/danner-apparel/bottoms', 'work and trail trousers stand in'),
        sweater=G(240, "Men's DWR Wool/Cotton Sweater", DN + '/men-s-dwr-wool-cotton-sweater-urban-chic.html', 240, "Men's DWR Wool/Cotton Sweater", DN + '/men-s-dwr-wool-cotton-sweater-urban-chic.html',
                  'single', DN + '/danner-apparel/sweatshirts', 'only knit; no knitwear category (sits with sweatshirts)'),
        outerwear=G(140, 'Wolf Creek Sherpa Jacket', DN + '/wolf-creek-sherpa-jacket-outer-space-ermine.html', 550, 'Woodsman 2L GTX Jacket', DN + '/woodsman-2l-gtx-jacket-black-m.html',
                    'range', DN + '/danner-apparel/outerwear', ''),
        shoes=G(75, 'Shelter Cove Slide Orion', DN + '/shelter-cove-slide-orion.html', 540, 'Danner Light Revival 8" Khaki', DN + '/danner-light-revival-8-khaki.html', 'range', DN + '/men/all-footwear',
                'no loafer; 365 men\'s footwear records read from the Constructor browse API behind /men/all-footwear (price_x0101); zero-price records ignored')),
    own_doors_us=6, own_doors_world=NC, locator_url=DN + '/store-finder',
    doors_basis='counts return (10 Oct): Locally conversion_data, Danner-named markers: Factory Store Portland (flagged), Landing Renton, Tanasbourne Hillsboro, Box Factory Bend, Denver, Woodinville; world NC (Danner Japan is a separate account)',
    tech_named_fabrics='TECH_DN', tech_owned_or_licensed='licensed: GORE-TEX (boots, Cascade Crest and Woodsman jackets), WINDSTOPPER, PrimaLoft, CORDURA, Octa (Teijin Frontier)',
    tech_share_of_range='TECHSHARE_DN', tech_evidence_url=DN + '/cascade-crest-packable-3l-gtx-jacket-glazed-ginger-m.html', proposed_tech=NC,
    owned_facility='yes, evidenced: "INSIDE OUR USA FACTORY" factory-tour page (materials, preparation, construction, finishing); the Portland factory store sits at the factory site (counts return)',
    named_makers='own factory for the USA-made boots and apparel; imported product makers not named', named_mills='no', made_in_stated_share='MADEIN_DN',
    heritage_claim='dated: "EST. 1932" in the logo; Charles Danner "came west" to the Pacific Northwest (/about-danner); founding town not stated',
    process_documented='yes: factory tour walks through material preparation, construction and finishing; recrafting (resoling) service (/recrafting)',
    craft_url_1=DN + '/factory-tour', craft_url_2=DN + '/about-danner', proposed_craft=4,
    craft_reasoning='Danner shows its own USA factory and documents the stages of making, and the apparel pages state the country of origin on every style. A large share of the range is imported from unnamed factories, so the owned making does not cover it all.',
    founded_year=1932, founded_place=NC, founders='Charles Danner', owner_today=NC, ownership_url=NC,
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=717118&catalog[]=5', vinted_brand_ids='717118', grailed_url='https://www.grailed.com/designers/danner',
    quote='You don’t put on a pair of Danner boots to sit around the house.', quote_who='the house, about page', quote_source='danner.com /about-danner',
    quote_url=DN + '/about-danner', quote_date='undated page (read 2026-10-11)',
    signature_product='Danner Light (USA-made GORE-TEX hiking boot)', signature_product_url=DN + '/danner-light.html', status='partial',
    source=f'Chrome {D}: danner.com Constructor browse API (men all-footwear 365; danner-apparel 136), 88 apparel PDPs (Fabric Content, Country of Origin), /about-danner, /factory-tour; doors from the 10 Oct counts return',
    note='Footwear-led house; the style table covers apparel only (women\'s excluded; Sig Zane x Danner collaboration excluded): 87 colourway records / 46 styles. Owner not stated on the site (image paths point to LaCrosse).')

# ------------------------------------------------------------------------------------------------ Denim Tears
M['Denim Tears'] = dict(
    site_domain='denimtears.com', store_used=DT, currency='USD', search_url=DT + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(50, 'Flag Claw Tee White', DT + '/products/flag-claw-tee-white', 90, 'Cotton Wreath 2000s Tee', DT + '/products/cotton-wreath-tall-tee-white', 'range', DT + '/collections/short-sleeve-tees',
              'unisex house; no men-only listing'),
        polo=G(118, 'Wreath Polo', DT + '/products/peace-wreath-polo-white', 128, 'Pique Panther Long Sleeve Polo', DT + '/products/pique-panther-long-sleeve-polo-navy', 'range', DT + '/collections/polo', ''),
        dress_shirt=G(148, 'Peace Wreath Oxford Shirt', DT + '/products/peace-wreath-oxford-shirt-blue', 178, 'André Leon Talley Two-Tone Button-Up Shirt', DT + '/products/andre-leon-talley-two-tone-button-up-shirt',
                      'range', DT + '/collections/shirts', 'casual shirts only'),
        jeans=G(210, 'Straight Denim Pant (light wash)', DT + '/products/straight-denim-pant-light-wash', 295, 'Straight Cotton Wreath Denim Pant Selvedge', DT + '/products/straight-cotton-wreath-denim-pant-selvedge',
                'range', DT + '/collections/jeans', 'plain and Cotton Wreath versions of the same jean; all made in USA'),
        dress_pants=G(188, 'Panther Chino', DT + '/products/panther-chino', 188, 'Panther Chino', DT + '/products/panther-chino', 'single', DT + '/collections/casual-pants', 'only chino; carpenter pants 228-298'),
        sweater=G(198, 'Pilled Cotton Wreath Sweater (100% wool)', DT + '/products/pilled-cotton-wreath-sweater-navy', 198, 'Pan-African American Sweater (95% cotton, 5% cashmere)',
                  DT + '/products/pan-african-american-pilled-sweater-black', 'range', DT + '/collections/knits', 'both crewnecks are 198'),
        outerwear=G(248, 'Stadium Jacket', DT + '/products/stadium-jacket-black-pink', 498, 'Cotton Wreath Chainstitch N-2B Flight Jacket', DT + '/products/cotton-wreath-chainstitch-n-2b-flight-jacket-military-green',
                    'range', DT + '/collections/outerwear', 'Bobby Huey Reversible Varsity Jacket also 498'),
        shoes=NONE_(note='no footwear in stock')),
    own_doors_us=1, own_doors_world=1, locator_url=DT + '/pages/stores',
    doors_basis="brand's stores page: Denim Tears Flagship (African Diaspora Goods, 176 Spring Street, New York); the Atlanta Residency in Lenox Square is a pop-up (ruled), dates not given on the page; Dover Street Market London, LA, New York and Ginza are stockists",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=DT + '/pages/about', proposed_tech=NC,
    owned_facility='no claim', named_makers='no', named_mills='no', made_in_stated_share='MADEIN_DT',
    heritage_claim='dated, not placed: "Since 2019 ... articulated by multidisciplinary artist and designer Tremaine Emory" (/pages/about)', process_documented='no',
    craft_url_1=DT + '/pages/about', craft_url_2=DT + '/products/straight-cotton-wreath-denim-pant-selvedge', proposed_craft=2,
    craft_reasoning='Every product description states its country (denim made in the USA, fleece in Turkey, tees in China), but no maker, mill or process is named. The brand story is about meaning rather than making.',
    founded_year=2019, founded_place=NC, founders='Tremaine Emory', owner_today=NC, ownership_url=NC,
    lookbook_found='yes', lookbook_season_label='Fall/Winter 2026', lookbook_mens=NC, lookbook_url=DT + '/blogs/lookbook/fall-winter-2026',
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=4684131&catalog[]=5', vinted_brand_ids='4684131', grailed_url='https://www.grailed.com/designers/denim-tears',
    quote='Denim Tears utilizes its creative catalog to drive culture forward with uncompromising intention.', quote_who='the house, about page', quote_source='denimtears.com /pages/about',
    quote_url=DT + '/pages/about', quote_date='undated page (read 2026-10-11)',
    signature_product='Cotton Wreath denim', signature_product_url=DT + '/collections/jeans', status='partial',
    source=f'Chrome {D}: denimtears.com products.json (261; 231 in stock), body_html compositions, /pages/stores, /pages/about, /blogs/lookbook, collections.json',
    note='Style = title de-dup with colour words stripped: 145 in-stock clothing listings / 102 styles; kids and accessories excluded; Billionaire Boys Club collaboration sweater excluded. Mark: DENIM TEARS (capitals on site).')

# ------------------------------------------------------------------------------------------------ Deus Ex Machina
M['Deus Ex Machina'] = dict(
    site_domain='deuscustoms.com', store_used=DE + ' (Deus Ex Machina USA)', currency='USD', search_url=DE + '/search?q=', feed_currency_rate='1.0', sublines_included='Deus Classics (vendor on the US store, counted)',
    g=dict(
        tee=G(49, 'Shield Standard Tee (Deus Classics)', DE + '/products/shield-standard-tee-grey-marle', 89, 'Merz Oversized Tee', DE + '/products/merz-oversized-tee-dirty-white', 'range', DE + '/collections/tees',
              'Deus x AGTZ tee (99) excluded as collaboration'),
        polo=G(129, 'Grand Prix Polo (compare-at 129; on sale 90)', DE + '/products/grand-prix-polo-race-green', 129, 'Grand Prix Polo (compare-at 129)', DE + '/products/grand-prix-polo-race-green', 'single', DE + '/collections/tees',
               'only polo; parent listing'),
        dress_shirt=G(99, 'Bad Sign Shirt', DE + '/products/bad-sign-shirt-navy', 229, 'Anityata Shirt (compare-at 229; on sale 114.50)', DE + '/products/anityata-shirt-black-iris', 'range', DE + '/collections/shirts',
                      'casual shirts; the dearest current-season shirt at full price is the Maxwell Check Shirt (189)'),
        jeans=G(139, 'True Line Straight Jean (washed indigo)', DE + '/products/true-line-straight-jean-washed-indigo', 149, 'True Line Straight Jean (dirty denim)', DE + '/products/true-line-straight-jean-dirty-denim',
                'range', DE + '/collections/denim', 'all three jean cuts are 139-149 by wash'),
        dress_pants=G(129, 'Marnus Pant', DE + '/products/marnus-pant-khaki-2', 129, 'Otto Pleated Pant', DE + '/products/otto-pleated-pant-black', 'range', DE + '/collections/pants', 'chinos stand in; every chino is 129'),
        sweater=G(149, 'One More Marle Crew (compare-at 149)', DE + '/products/one-more-marle-crew-lt-grey-marle', 219, 'Henzen LS Knit Jersey (100% merino)', DE + '/products/henzen-ls-knit-jersey-tofu-white',
                  'range', DE + '/collections/knitwear', ''),
        outerwear=G(139, 'Venice Coach', DE + '/products/venice-coach-mechanic-blue', 429, 'Suka Reversible Bomber (compare-at 429; on sale 214.50)', DE + '/products/suka-reversible-bomber-multi',
                    'range', DE + '/collections/jackets', 'dearest full-price jacket is the Monument Coat (329)'),
        shoes=NONE_(note='footwear collection has no product in stock')),
    own_doors_us=1, own_doors_world=6, locator_url=DE + '/pages/flagship-stores',
    doors_basis="brand's flagship page: The Emporium of Post Modern Activities, 1001 Venice Boulevard, Venice CA (US); Biarritz, Milan, Canggu, Sydney (Camperdown), São Paulo (store e-mail at deusbr.com: operator-run, flagged)",
    tech_named_fabrics='TECH_DE', tech_owned_or_licensed='licensed: GORE WINDSTOPPER', tech_share_of_range='TECHSHARE_DE', tech_evidence_url=DE + '/products/offshore-windstopper-tendril-green', proposed_tech=NC,
    owned_facility='no claim for clothing (the flagships run motorcycle workshops)', named_makers='no', named_mills='no', made_in_stated_share='0/246 styles state a country in the product text read',
    heritage_claim=NC, process_documented='no',
    craft_url_1=DE + '/pages/flagship-stores', craft_url_2=DE + '/products/cutaway-jacket-navy', proposed_craft=1,
    craft_reasoning='Product pages give composition (on just over half the range) but no country, maker or mill. The about and history pages were not read in the time box.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=199668&catalog[]=5', vinted_brand_ids='199668', grailed_url='https://www.grailed.com/designers/deus-ex-machina',
    quote=NC, quote_who=NC, quote_source=NC, quote_url=NC, quote_date=NC,
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: deuscustoms.com products.json (3516; 614 in stock), 253 style PDPs plus a second read of 111 without composition, /pages/flagship-stores and five flagship pages, stockist.co u17277 locations (365)',
    note='Archive feed: only in-stock men\'s clothing counted (366 listings / 246 styles by 10-character SKU stem; Deus x AGTZ and Deus Ex Attaquer collaborations excluded). 111 carry-over and markdown listings state no composition on a second read, so coverage is 55%. Boardshorts and swim shorts are swim.')

# ------------------------------------------------------------------------------------------------ Dickies
M['Dickies'] = dict(
    site_domain='dickies.com', store_used=DK, currency='USD', search_url=DK + '/search?q=', feed_currency_rate='1.0', sublines_included='Dickies Skateboarding (sold in the men\'s range, counted)',
    g=dict(
        tee=G(15, 'Short Sleeve T-Shirt (14.99 base size)', DK + '/products/short-sleeve-t-shirt-dk0ws4800bk', 55, 'Mineral Heavyweight Short Sleeve T-Shirt (compare-at 55)', DK + '/products/mineral-heavyweight-short-sleeve-t-shirt-dk0a87qeri2',
              'range', DK + '/collections/mens-t-shirts', 'collaboration tees (Harley-Davidson, Thrasher, Budweiser) excluded'),
        polo=G(30, 'Short Sleeve Performance Polo Shirt (29.99 base size)', DK + '/products/short-sleeve-performance-polo-shirt-dkws247fin2', 30, 'Short Sleeve Performance Polo Shirt', DK + '/products/short-sleeve-performance-polo-shirt-dkws247fin2',
               'single', DK + '/collections/mens-shirts', 'only polo (32.99 in larger sizes); parent listing'),
        dress_shirt=G(28, 'Short Sleeve Work Shirt (27.99 base size)', DK + '/products/short-sleeve-work-shirt-dk0015740bk', 85, 'Springdale Short Sleeve Button-Up Shirt (compare-at 85)', DK + '/products/springdale-short-sleeve-button-up-shirt-dk0a88k5c48',
                      'range', DK + '/collections/mens-button-up-shirts', 'work shirts stand in for a dress shirt'),
        jeans=G(30, 'Regular Fit Jeans (29.99 base size)', DK + '/products/regular-fit-jeans-dk009393rnb', 130, 'Selvedge Double Knee Denim Jeans (compare-at 130)', DK + '/products/selvedge-double-knee-denim-jeans-dk0a87nj0wh',
                'range', DK + '/collections/mens-jeans', ''),
        dress_pants=G(30, 'Original 874® Work Pants (29.99 base size)', DK + '/products/original-874-r-work-pants-dk0008740bk', 115, 'Hemp Twill Work Pants (compare-at 115)', DK + '/products/hemp-twill-work-pants-dk0a88gwl44',
                      'range', DK + '/collections/mens-work-pants', 'work pants stand in; the 873 Slim Fit is also 29.99'),
        sweater=G(85, 'Union Jacquard Sweater (compare-at 84.99)', DK + '/products/union-jacquard-sweater-dk0a88gsc48', 85, 'Union Jacquard Sweater', DK + '/products/union-jacquard-sweater-dk0a88gsc48',
                  'single', DK + '/collections/mens-hoodies-sweatshirts', 'only knit sweater (100% acrylic); sits with sweatshirts'),
        outerwear=G(55, 'Fleece Lined Nylon Hooded Jacket (54.99 base size)', DK + '/products/fleece-lined-nylon-hooded-jacket-dk0332370bk', 180, 'Selvedge Pleated Denim Jacket (compare-at 180)',
                    DK + '/products/selvedge-pleated-denim-jacket-dk0a87o90wh', 'range', DK + '/collections/mens-coats-jackets', 'shirt-jackets excluded; Harley-Davidson denim jacket (160) excluded'),
        shoes=NONE_(note='no footwear on the US store (1,741-product feed checked)')),
    own_doors_us=NC, own_doors_world=NC, locator_url=DK + '/pages/stores',
    doors_basis='NC (ruled): /en-us/pages/stores embeds hosted.where2getit.com/dickies/index.1116.html, which returns HTTP 404 (counts return, 10 Oct)',
    tech_named_fabrics='TECH_DK', tech_owned_or_licensed='house-named (FLEX stretch, Cooling, DuraTech) plus licensed LYCRA® fiber', tech_share_of_range='TECHSHARE_DK',
    tech_evidence_url=DK + '/products/flex-regular-fit-duck-carpenter-pants-dk0dp802ssl', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no', named_mills='no', made_in_stated_share='MADEIN_DK',
    heritage_claim='dated and placed: "On the job since 1922. A century ago, we were just a small Texas company making bib overalls." (/pages/dickies-history)', process_documented='no',
    craft_url_1=DK + '/pages/dickies-history', craft_url_2=DK + '/products/original-874-r-work-pants-dk0008740bk', proposed_craft=1,
    craft_reasoning='The site dates the company to 1922 in Texas but product pages say only "Imported", with no country, maker or mill. Nothing about present-day making can be checked.',
    founded_year=1922, founded_place='Texas', founders=NC, owner_today='Bluestar Alliance (acquired from VF Corporation, about $600 million, announced September 2025; press)',
    ownership_url='https://fashionunited.uk/news/business/dickies-acquired-by-bluestar-alliance-in-600-million-dollars-deal/2025091583921',
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=65&catalog[]=5', vinted_brand_ids='65', grailed_url='https://www.grailed.com/designers/dickies',
    quote='A century ago, we were just a small Texas company making bib overalls.', quote_who='the house, heritage page', quote_source='dickies.com /en-us/pages/dickies-history',
    quote_url=DK + '/pages/dickies-history', quote_date='undated page (read 2026-10-11)',
    signature_product='Original 874® Work Pants', signature_product_url=DK + '/products/original-874-r-work-pants-dk0008740bk', status='partial',
    source=f'Chrome {D}: dickies.com/en-us /collections/mens products.json (1070; 739 in stock), 266 style PDPs, store feed (1741) for footwear, /pages/dickies-history, search check',
    note='Style = first SKU segment (D874, WS450): 722 in-stock listings / 247 styles after excluding 17 collaboration styles. Markdown house: most listings carry compare-ats; regular price = compare-at where present. Larger sizes carry a higher price on many styles (e.g. the Short Sleeve T-Shirt is 14.99, 17.99 in big sizes); every price cell is the base-size regular price, checked against the product .js record, filed whole-dollar half-up. Ownership is from press, not the brand.')
