D = '2026-10-10'
NC = 'NC'

def G(low, lp, lu, high, hp, hu, basis, listing, note=''):
    return dict(low=low, low_product=lp, low_url=lu, high=high, high_product=hp, high_url=hu, basis=basis, mens_listing_url=listing, _note=note)

def NONE_(listing='NONE'):
    return dict(low='NONE', low_product='NONE', low_url='NONE', high='NONE', high_product='NONE', high_url='NONE', basis='NONE', mens_listing_url=listing, _note='')

def NP(listing, note=''):
    return dict(low='np', low_product='np', low_url='np', high='np', high_product='np', high_url='np', basis='np', mens_listing_url=listing, _note=note)

AI = 'https://www.angloitalian.com'
AW = 'https://awakenyclothing.com'
AZ = 'https://aztechmountain.com'
BBG = 'https://badbirdiegolf.com'
BG = 'https://bergbergstore.com'
BW = 'https://www.birdwell.com'
BL = 'https://www.blundstone.com'
AS = 'https://www.asket.com/en-us'
AF = 'https://alanflusser.com'

M = {}

M['Alan Flusser'] = dict(
    site_domain='alanflusser.com', store_used=AF, currency='USD', search_url='NONE', feed_currency_rate='not shopify', sublines_included='-',
    g=dict(tee=NONE_(), polo=NONE_(), dress_shirt=G(525, 'Bespoke shirt (from; three-shirt minimum on first order)', AF + '/shirts', 525, 'Bespoke shirt (from)', AF + '/shirts', 'single', AF + '/shirts',
                                               'custom house: published from-price only'),
           jeans=NONE_(), dress_pants=NP(AF + '/mens-custom', 'trousers made only within custom suits; no separate trouser price published (suits from 2700 Club / 3300 Gentry / 4600 Heritage)'),
           sweater=NONE_(), outerwear=NP(AF + '/mens-custom', 'custom overcoats not priced on site'), shoes=NONE_()),
    styles=dict(styles_total=0, styles_with_composition=0, natural_pct=NC, synthetic_pct=NC, cellulosic_pct=NC, spandex_styles=0, shape=NC, natural_categories='[]', synthetic_categories='[]',
                colourway_ratio='0/0', style_method='manual', swim_styles=0, swim_share_of_range=NC, mens_styles_excl_swim=0),
    own_doors_us=1, own_doors_world=1, locator_url=AF + '/appointment', doors_basis='facts-first: footer address 3 East 48th Street, Floor 3, New York NY 10017; by appointment; site names no other door',
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=AF + '/mens-custom', proposed_tech=NC,
    owned_facility='claim, partly evidenced: "Our in-house tailors in NYC handle alterations and hand-finishing on all garments" (/mens-custom); Heritage make "made by hand, start to finish in New York ... by expert tailors in a boutique workshop" (workshop not named, ownership not stated); Gentry "constructed in our partner workshop offshore"',
    named_makers='no — workshops described, not named (NY boutique workshop; offshore partner workshop; shirt workshop "a few blocks from our showroom")',
    named_mills='yes (shirting): "fabrics from the top mills in the world, including our favorites Alumo, Bonfanti, and Thomas Mason" (/shirts)',
    made_in_stated_share='custom only: Heritage = New York; Gentry = offshore (country not named); bespoke shirts = Manhattan',
    heritage_claim='dated and placed: "1986: The Alan Flusser Custom Shop debuts"; Saks 1993–2001; 3 East 48th in the 2000s (/about)',
    process_documented='yes: three levels of make described step by step — hand-padded full canvas, collar attached by hand, hand-finishing of armholes, collar, lapels, pockets; paper pattern drafted and kept on file; muslin fitting (/mens-custom, /shirts)',
    craft_url_1=AF + '/mens-custom', craft_url_2=AF + '/shirts', proposed_craft=4,
    craft_reasoning='The house documents its making in unusual detail (hand-padded canvas, hand-set collars, a NY handmade top line, in-house tailors for finishing) and names its shirting mills (Alumo, Bonfanti, Thomas Mason). It does not name its workshops or show it owns one, and its middle line is made offshore, so it stops short of 5.',
    founded_year=1986, founded_place='New York', founders='Alan Flusser', owner_today='Jonathan Sigmon ("Long-time director Jonathan Sigmon takes over the business as Alan retires", 2020)', ownership_url=AF + '/about',
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=937280&catalog[]=5', vinted_brand_ids='937280', grailed_url='https://www.grailed.com/designers/alan-flusser',
    quote='The Promise: crafting one-of-a-kind clothing with years of fashion longevity.', quote_who='the house (Alan Flusser Custom), about page timeline entry for 1986', quote_source='alanflusser.com /about', quote_url=AF + '/about', quote_date='undated page (read 2026-10-10)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: alanflusser.com home, /mens-custom, /shirts, /about, /products',
    note='Custom house: no ready-to-wear clothing, so no style table. Ready-made goods are neckwear, pocket squares, socks, suspenders and books. Mark on site: "Alan Flusser Custom" (ruled: Alan Flusser).')

M['Anglo-Italian'] = dict(
    site_domain='angloitalian.com', store_used=AI + ' (Shopify Markets, country US, USD active)', currency='USD', search_url=AI + '/search?q=', feed_currency_rate='1.32369', sublines_included='-',
    g=dict(tee=NONE_(),
           polo=G(229, 'Polo Shirt Long Sleeve Lemon (229.33)', AI + '/products/polo-shirt-long-sleeve-lemon', 410, 'Knitted Polo Silk Chocolate (410.01)', AI + '/products/knitted-polo-silk-chocolate', 'pair', AI + '/collections/polo',
                  'high is the silk knitted polo (elevated fibre); the Raglan Cableknit Polo Wool-Cashmere is dearer but 70/30 wool-cashmere is not an elevated fibre under the 18 Sep ruling'),
           dress_shirt=G(243, 'Point Collar Shirt Cotton Poplin White (243.23)', AI + '/products/point-collar-shirt-cotton-poplin-white', 271, 'Spread Collar Shirt Zephyr Cotton-Linen Blue Reverse Stripe (271.03)', AI + '/products/spread-collar-shirt-zephyr-cotton-linen-blue-reverse-stripe', 'range', AI + '/collections/shirting', 'no elevated-fibre dress shirt; mechanics shirt 74/26 cotton-silk same price'),
           jeans=G(382, 'Denim One Wash Mk. II (382.22)', AI + '/products/aic-denim-one-wash-mkii-fit', 382, 'Denim Black Wash Mk. II (382.22)', AI + '/products/aic-denim-black-wash-jeans', 'range', AI + '/collections/denim-5-pockets', 'every 5-pocket and jean is the same price'),
           dress_pants=G(486, 'Tailored Trouser High-Twist Wool Mid Grey (486.46)', AI + '/products/tailored-trouser-twisted-wool-mid-grey', 584, 'Tailored Trouser Cotton-Cashmere Drill Navy (583.75)', AI + '/products/tailored-trouser-textured-winter-twill-navy', 'range', AI + '/collections/trousers', 'flannel tailored trousers between'),
           sweater=G(347, 'Crewneck Lambswool Shetland Blend Navy (347.47)', AI + '/products/crewneck-lambswool-navy', 459, 'Crewneck Cotton Navy Patchwork (458.66)', AI + '/products/crewneck-cotton-navy-patchwork', 'range', AI + '/collections/knitwear',
                     'no crewneck in an elevated fibre; Cableknit Wool-Cashmere neckline not read'),
           outerwear=G(549, 'Keepers Fleece Olive (549.00)', AI + '/products/keepers-fleece-olive', 1070, 'Creek Jacket Ventile Cotton Olive (1070.20)', AI + '/products/creek-jacket-ventile-cotton-olive', 'range', AI + '/collections/outerwear',
                       'facts-first read 1069.49 on 2026-10-08'),
           shoes=G(368, 'Desert Boot Crepe Sole Black Suede (368.32)', AI + '/products/desert-boots', 493, 'Mountain Boot Crepe Sole Black Suede (493.41)', AI + '/products/mountain-boot-crepe-sole-black-suede', 'range', AI + '/collections/footwear',
                   'no own-label loafer: the loafers on the site are Crockett & Jones (stocked, not counted)')),
    own_doors_us=0, own_doors_world=1, locator_url=AI + '/pages/our-store', doors_basis="brand's store page: one store, 57 Weymouth Street London W1G 8NP; New York trunk shows only (not a door)",
    tech_named_fabrics='Ventile (cotton)', tech_owned_or_licensed='licensed (third-party cloth)', tech_share_of_range='2/92 styles (Creek Jacket Ventile Cotton, 2 colourways)', tech_evidence_url=AI + '/products/creek-jacket-ventile-cotton-olive', proposed_tech=NC,
    owned_facility='no: "partnering with workshops, mills and factories operated by people we have the utmost admiration for" (/pages/about)',
    named_makers='no: makers are placed by region only — Tuscany (RTW & MTM tailoring), Liguria (bespoke), Naples (trousers), Lombardy (shirting), Veneto (buttons), Como (linings) (/pages/services-25)',
    named_mills='no names: own "Tessuti" cloth woven with "small mills in Prato, Biella and Huddersfield" (/pages/tessuti); product pages give composition and weight, no mill',
    made_in_stated_share='MADEIN_AI',
    heritage_claim='dated and placed, young: "Founded by Jake Grantham in 2017 ... based in Marylebone, London" (/pages/about)',
    process_documented='partial: own cloth designed since 2019 with a heavily milled matte "Anglo finish"; a category-by-region map of where each part is made; house tailoring style described (/pages/tessuti, /pages/services-25)',
    craft_url_1=AI + '/pages/services-25', craft_url_2=AI + '/pages/tessuti', proposed_craft=2,
    craft_reasoning='Every style states a country (almost all Italy) and the house publishes a region-by-region map of its making and designs its own cloth. But it names no workshop or mill, and owns nothing; the rubric step for naming makers or mills (3) is not reached.',
    founded_year=2017, founded_place='Marylebone, London', founders='Jake Grantham', owner_today=NC, ownership_url=NC,
    lookbook_found='yes', lookbook_season_label='SS26 Lookbook', lookbook_mens='yes', lookbook_url=AI + '/blogs/journal/ss26-lookbook',
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='https://www.grailed.com/designers/anglo-italian',
    quote='Anglo-Italian does not wholesale or discount, we charge what we deem is fair for garments that will endure.', quote_who='the house, about page', quote_source='angloitalian.com /pages/about', quote_url=AI + '/pages/about', quote_date='undated page (read 2026-10-10)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: angloitalian.com products.json (232 products, 10 nav collections), /pages/about, /pages/our-store, /pages/tessuti, /pages/services-25, /blogs/journal, /search',
    note='PRICES ARE THE DISPLAYED US PRICES read from each product page; on 10 Oct the products.json / .js feed in USD presentment ran 1.48% above the displayed price on all 14 products checked (e.g. polo feed 232.77, page $229.33), so the feed was not used for prices. Domain correction stands (angloitalian.com). The site says "does not wholesale", so there is no stockist list. Style count is title-dedup over colourway handles (151 listings -> 92 clothing styles); Mk. II denim washes stay separate styles.')

M['Asket'] = dict(
    site_domain='asket.com', store_used=AS, currency='USD', search_url='NC', feed_currency_rate='not shopify', sublines_included='-',
    g=dict(tee=G(65, 'The T-Shirt', AS + '/mens-t-shirt-white', 95, 'The Lightweight T-Shirt', AS + '/mens-lightweight-t-shirt-white', 'range', AS + '/mens/t-shirts', 'The Long Sleeve T-Shirt also 95'),
           polo=G(120, 'The Pique Polo', AS + '/mens-pique-polo-white', 240, 'The Merino Wool Polo', AS + '/mens-merino-wool-polo-light-brown-melange', 'range', AS + '/mens/t-shirts', 'merino polo is knitwear; extra-fine merino not ruled elevated'),
           dress_shirt=G(190, 'The Oxford Shirt', AS + '/mens-oxford-shirt-white', 220, 'The Flannel Shirt', AS + '/mens-flannel-shirt-charcoal-melange', 'range', AS + '/mens/shirts', 'The Denim Shirt also 220; overshirts (300, 320) excluded as shirt-jackets'),
           jeans=G(230, 'The Slim Jeans', AS + '/mens-slim-jeans-raw-denim', 230, 'The Loose Jeans', AS + '/mens-loose-jeans-raw-denim', 'range', AS + '/mens/denim', 'all nine jeans 230'),
           dress_pants=G(320, 'The Wool Trousers', AS + '/mens-wool-trousers-dark-navy', 320, 'The Wool Trousers', AS + '/mens-wool-trousers-dark-navy', 'single', AS + '/mens/trousers', 'chinos 230; linen trousers 230'),
           sweater=G(150, 'The Cotton Sweater', AS + '/mens-cotton-sweater-grey-melange', 270, 'The Recycled Cashmere Sweater', AS + '/mens-recycled-cashmere-sweater-light-grey', 'range', AS + '/mens/knitwear', 'cashmere sweater composition not read on the product page, so not claimed as an elevated-fibre pair; The Merino Sweater 210'),
           outerwear=G(510, 'The Wool Jacket', AS + '/mens-wool-jacket-dark-navy', 680, 'The Wool Coat', AS + '/mens-wool-coat-dark-navy', 'range', AS + '/mens/outerwear', 'Car Coat and Field Jacket 650'),
           shoes=NONE_()),
    own_doors_us=0, own_doors_world=2, locator_url=AS + '/stores', doors_basis="brand's stores page: London (72-74 Brewer Street) and Stockholm (Norrmalmstorg 1) full-price; Asket Archive at Stockholm Quality Outlet, Barkarby = outlet; Munich pop-up 5–28 Nov 2026 = pop-up",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=AS + '/about', proposed_tech=NC,
    owned_facility='no (no owned factory claimed; "manufacture transparently in Europe")',
    named_makers='yes, in product data: supplierName names AGENDA SRL / INCOM S.P.A (jeans), Cottonparadise, Lda (tees), SC ALEXTRICOT SRL (recycled cashmere), Impetus (boxer briefs), Insitepart (sweatshorts); most other styles show "ASKET HQ"',
    named_mills='yes: Manteco (recycled wool coat and jacket), Candiani (denim), Kurabo (raw denim yarn), Tollegno 1900 (merino) named in product descriptions',
    made_in_stated_share='47/47 styles carry countryOfOrigin in product data (Portugal, Italy, Romania)',
    heritage_claim='dated and placed: "We founded Asket in 2015 in Stockholm, Sweden" (/about)',
    process_documented='yes: per-product traceability, cost and footprint published ("exhaustive supply chain traceability ... available on each product page"); mill-to-make chains in descriptions ("milled by Manteco, Italy, cut and sewn in Portugal")',
    craft_url_1=AS + '/about', craft_url_2=AS + '/mens-wool-coat-dark-navy', proposed_craft=3,
    craft_reasoning='Asket names its makers in product data and its mills in descriptions (Manteco, Candiani, Kurabo, Tollegno 1900), and states country of origin on every style. It owns no facility, which is the 3 step exactly. Its about page says garments are made "exclusively in Italy and Portugal" while its own product data lists Romania for several knits and the wool coat.',
    founded_year=2015, founded_place='Stockholm, Sweden', founders='Jakob Sazon Dworsky; August Bard Bringéus', owner_today=NC, ownership_url=NC,
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=824491&catalog[]=5', vinted_brand_ids='824491', grailed_url='https://www.grailed.com/designers/asket',
    quote='We envision a world free from mindless consumption.', quote_who='August Bard Bringéus, co-founder', quote_source='asket.com /about (Vision)', quote_url=AS + '/about', quote_date='undated page (read 2026-10-10)',
    signature_product='The T-Shirt (the 2015 launch product per the about-page timeline)', signature_product_url=AS + '/mens-t-shirt-white', status='partial',
    source=f'Chrome {D}: asket.com/en-us men\'s listing pages (SSR state window.__INITIAL_PROMISES_CONTEXT__) for denim, trousers, knitwear, t-shirts, shirts, outerwear, sweats, underwear; product-page state for each style; /about; /stores',
    note='Not Shopify; site search URL not tested (NC). Composition read for 33 of 47 styles; on the rest neither the listing card nor the product\'s own description states it. The product pages render other products\' material blocks, so a page-wide read was rejected. Listing pages may be lazy-loaded: 47 styles is what the server-rendered pages carry.')

M['Awake NY'] = dict(
    site_domain='awakenyclothing.com', store_used=AW, currency='USD', search_url=AW + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(tee=G(60, 'Gradient Sport Tee (regular 60; on sale at 30)', AW + '/products/gradient-sport-tee', 85, 'Thermal Long Sleeve Tee', AW + '/products/thermal-long-sleeve-tee-2', 'range', AW + '/collections/tees-1',
                 'graphic tees regular 60 on several products (Champs, Tres Golpes, New York Star); Pocket Tee 75 full price; collab tees excluded'),
           polo=G(145, 'Crown Polo (regular 145; on sale at 72.50)', AW + '/products/crown-polo-copy', 175, 'Mesh Zip Polo (regular 175; on sale at 87.50)', AW + '/products/mesh-zip-polo-1', 'range', AW + '/collections/shirts-1', 'parent listing: shirts'),
           dress_shirt=G(85, 'Campus Shirt (regular 85; on sale at 42.50)', AW + '/products/campus-shirt-1', 175, 'Orchard St. Plaid Shirt (regular 175; on sale at 87.50)', AW + '/products/orchard-st-plaid-shirt', 'range', AW + '/collections/shirts-1', 'casual button shirts only; no dress shirt'),
           jeans=G(199, 'Orchard St. Baggie Denim (regular 199; on sale at 99.50)', AW + '/products/orchard-st-denim-copy', 299, 'Skyline Denim', AW + '/products/skyline-denim', 'range', AW + '/collections/bottoms-1', 'parent listing: bottoms'),
           dress_pants=NONE_(), sweater=G(195, 'Hand Dip-Dyed Knit (regular 195; on sale at 97.50)', AW + '/products/hand-dipped-dyed-sweater-change-name', 195, 'Hand Dip-Dyed Knit', AW + '/products/hand-dipped-dyed-sweater-change-name', 'single', 'NC', 'only knit in the live range; no knitwear listing in nav'),
           outerwear=G(225, 'LES Performance Track Jacket', AW + '/products/les-performance-track-jacket-2', 225, 'Pusherman Track Jacket (regular 225; on sale at 112.50)', AW + '/products/fisherman-track-jacket-1', 'range', AW + '/collections/outerwear-1', 'Rivington Zip Flannel (235) is a shirt-jacket, excluded'),
           shoes=NONE_()),
    own_doors_us=1, own_doors_world=1, locator_url=AW + '/pages/flagship', doors_basis="brand's flagship page: 62 Orchard St, New York NY (no other door on site)",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=AW, proposed_tech=NC,
    owned_facility='no claim', named_makers='no', named_mills='no', made_in_stated_share='0/39 live styles state a country in the feed description',
    heritage_claim='dated and placed: "Launched in New York City in 2012" (/pages/about)', process_documented='no (one product: "hand dipped-dyed sweater with hand-sewn logo")',
    craft_url_1=AW + '/pages/about', craft_url_2=AW + '/products/hand-dipped-dyed-sweater-change-name', proposed_craft=1,
    craft_reasoning='Nothing about making is checkable on the site: no country on the live styles, no makers, no mills. Only the founding date and place are stated.',
    founded_year=2012, founded_place='New York City', founders='Angelo Baque', owner_today=NC, ownership_url=NC,
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=620932&catalog[]=5', vinted_brand_ids='620932', grailed_url='https://www.grailed.com/designers/awake-ny',
    quote='Community remains central to Awake NY’s mission.', quote_who='the house, about page', quote_source='awakenyclothing.com /pages/about', quote_url=AW + '/pages/about', quote_date='undated page (read 2026-10-10)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: awakenyclothing.com products.json (382 products), /products/<h>.js and PDPs for 4 styles, /pages/about, /pages/flagship, /pages/stockists',
    note='Feed carries 260 untyped archive products; only the 52 live (available) groups were counted, 39 of them clothing. Most live product is marked down 50% with compare-at = regular price, so every figure here is the compare-at. Composition: a % on 6 styles; 16 more name a fibre without a %; 17 state nothing. Unisex streetwear label: listings are the house\'s own (no men\'s path exists).')

M['Aztech Mountain'] = dict(
    site_domain='aztechmountain.com', store_used=AZ, currency='USD', search_url=AZ + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(tee=G(125, 'Aspen Tennis Festival Tee', AZ + '/products/aspen-tennis-festival-tee', 125, 'Aspen Tennis Festival Tee', AZ + '/products/aspen-tennis-festival-tee', 'single', AZ + '/collections/mens-shirts-and-flannels', 'only own-label tee in the men\'s range; Amundsen tees are third-party'),
           polo=NONE_(),
           dress_shirt=G(395, 'Loge Peak Ski Shirt', AZ + '/products/loge-peak-ski-shirt-5', 2100, 'Sopris Shirt (100% cashmere)', AZ + '/products/sopris-shirt-1', 'range', AZ + '/collections/mens-shirts-and-flannels', 'ski/overshirts, no dress shirt; Tony Ski Shirt 1200'),
           jeans=NONE_(), dress_pants=NONE_(),
           sweater=G(795, 'Matterhorn Half Zip Sweater', AZ + '/products/m-matterhorn-half-zip-fa25', 2800, 'Duane Street Zip Hoody', AZ + '/products/m-duane-street-zip-hoody-fa25', 'range', AZ + '/collections/mens-sweaters',
                     'only crewneck is Friedl Brushed Crew Sweater 1100; Duane Street composition not stated on page'),
           outerwear=G(795, 'Hayden 3L Shell Jacket', AZ + '/products/hayden-3l-shell-jacket-copy', 2995, 'Matador 3 in 1 Jacket', AZ + '/products/matador-jacket', 'range', AZ + '/collections/mens-ski-jackets', 'Super Lite Jacket regular 1995, on sale 1895'),
           shoes=NONE_()),
    own_doors_us=1, own_doors_world=1, locator_url=AZ + '/pages/locations', doors_basis="brand's locations page: 42 Hudson Street, New York NY 10013 (own door, also stocks other ski brands); Arlberg Club House, Lech, Austria = concession (not counted)",
    tech_named_fabrics='Toray Dermizax; Toray EV 4-way stretch nylon; Dyntex GRS nylon; PrimaLoft Gold / Silver / ThermoPlume; "proprietary GRS-certified 4-way stretch nylon" (Hayden)', tech_owned_or_licensed='licensed (Toray, Dyntex, PrimaLoft); one fabric described as proprietary',
    tech_share_of_range='14/35 styles name a technical fabric or insulation', tech_evidence_url=AZ + '/products/matador-jacket', proposed_tech=NC,
    owned_facility='no claim', named_makers='no', named_mills='yes, on some: Tollegno 1900 named on 5 merino sweaters; Toray, Dyntex fabrics named on shells',
    made_in_stated_share='MADEIN_AZ', heritage_claim='dated and placed: "Founded in 2013 by David Roth and Heifara Rutgers"; "Born and raised in Aspen" (/pages/about)',
    process_documented='partial: technical specifications per product (shell, membrane, insulation, waterproof and breathability ratings); no making process',
    craft_url_1=AZ + '/pages/about', craft_url_2=AZ + '/products/matterhorn-hybrid-half-zip', proposed_craft=3,
    craft_reasoning='Names a mill (Tollegno 1900) on its merino knits and its technical fabric suppliers (Toray, Dyntex, PrimaLoft) on the shells, and states a country on 16 of 35 styles. Nothing owned, and the makers are not named; 3 is the top of what the evidence supports.',
    founded_year=2013, founded_place='Aspen, Colorado', founders='David Roth; Heifara Rutgers', owner_today=NC, ownership_url=NC,
    lookbook_found='yes', lookbook_season_label='Lookbook FW 26', lookbook_mens='mixed (collection, men\'s and women\'s)', lookbook_url=AZ + '/collections/lookbook-fw-26',
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=1451017&catalog[]=5', vinted_brand_ids='1451017', grailed_url='https://www.grailed.com/designers/aztech-mountain',
    quote='Thirteen years on, we still build every piece to be worn season after season, for a lifetime.', quote_who='the house, about page', quote_source='aztechmountain.com /pages/about', quote_url=AZ + '/pages/about', quote_date='undated page (read 2026-10-10)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: aztechmountain.com /collections/mens-shop-all products.json (36), every PDP specifications block, /pages/about, /pages/locations',
    note='Composition is in the PDP specifications block, not the feed. founded_place: the about page says "Born and raised in Aspen"; Aspen is not named as the founding place in so many words. No Aspen door on the locations page.')

M['Bad Birdie'] = dict(
    site_domain='badbirdiegolf.com', store_used=BBG, currency='USD', search_url=BBG + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(tee=G(38, 'Bad Tee - Black', BBG + '/products/black-bad-tee', 55, 'Boxy Tee - Dark Navy', BBG + '/products/oversized-graphic-tee-dark-navy', 'range', BBG + '/collections/t-shirts', ''),
           polo=G(78, 'The Tux', BBG + '/products/the-tux-polo', 94, 'Prodigy Jacquard Polo - Black', BBG + '/products/prodigy-2026-polo-black', 'range', BBG + '/collections/polos',
                  'core printed polo (BBMP001) is 88; one BBMP001 print carries 108 and was not taken as the top of the regular range'),
           dress_shirt=NONE_(), jeans=NONE_(),
           dress_pants=G(110, 'Golf Pant - Black', BBG + '/products/golf-pant-black', 110, 'Golf Pant - Black', BBG + '/products/golf-pant-black', 'single', BBG + '/collections/pants', 'golf trouser stands in for a dress pant; Hybrid Golf Jogger also 110'),
           sweater=NONE_(),
           outerwear=G(130, 'Kinetic Wind Pullover - Black - Warm Olive', BBG + '/products/kinetic-wind-pullover-black-warm-olive', 240, 'Atmos Rain Anorak - White Onyx', BBG + '/products/atmos-rain-anorak-white-onyx', 'range', BBG + '/collections/jackets', ''),
           shoes=G(180, 'Bad Birdie x Payntr "Paint Splatter" Reserve Classic SL', BBG + '/products/bad-birdie-x-payntr-paint-splatter', 180, 'Bad Birdie x Payntr "Paint Splatter" Reserve Classic SL', BBG + '/products/bad-birdie-x-payntr-paint-splatter', 'single', BBG + '/collections/bad-birdie-x-payntr',
                   'the only shoe is a collaboration with Payntr; recorded because the brand sells it under its name, flagged')),
    own_doors_us=3, own_doors_world=3, locator_url=BBG + '/pages/stores', doors_basis="brand's stores page: Scottsdale Fashion Square, UTC Westfield San Diego, Kierland Commons Scottsdale; the Sprinter van is not a door",
    tech_named_fabrics='Coolmax (1 style)', tech_owned_or_licensed='licensed', tech_share_of_range='1/30', tech_evidence_url=BBG + '/products/bad-elements-range-short-black', proposed_tech=NC,
    owned_facility='no claim', named_makers='no', named_mills='no', made_in_stated_share='1/30 (The Tux: Made in Peru)',
    heritage_claim='vague: founder story without a date ("started as a side hustle in our founder Jason Richardson’s apartment")', process_documented='no',
    craft_url_1=BBG + '/pages/about-us', craft_url_2=BBG + '/products/salt-shaker-baby-blue', proposed_craft=1,
    craft_reasoning='The site gives composition and weight for every style but nothing about who makes it or where (one style states Peru). The founding story is undated. Nothing checkable about making.',
    founded_year=NC, founded_place=NC, founders='Jason Richardson', owner_today=NC, ownership_url=NC,
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=11944693&catalog[]=5', vinted_brand_ids='11944693', grailed_url='https://www.grailed.com/designers/bad-birdie',
    quote='our mission remains the same: to make golf apparel that swings as hard as you do', quote_who='the house, about page', quote_source='badbirdiegolf.com /pages/about-us', quote_url=BBG + '/pages/about-us', quote_date='undated page (read 2026-10-10)',
    signature_product='Core Performance Polo (the printed polo, SKU stem BBMP001)', signature_product_url=BBG + '/collections/polos', status='partial',
    source=f'Chrome {D}: badbirdiegolf.com /collections/mens products.json (231), PDP "Materials + Care" for all 30 clothing styles, /pages/about-us, /pages/stores',
    note='Style = SKU stem: 37 prints of the core polo collapse to one style. Domain on file should be badbirdiegolf.com.')

M['Berg & Berg'] = dict(
    site_domain='bergbergstore.com', store_used=BG + ' (country US, USD)', currency='USD_landed', search_url=BG + '/search?q=', feed_currency_rate='1.142604', sublines_included='-',
    g=dict(tee=G(100, 'Tony Mercerized T-Shirt - White', BG + '/products/tony-mercerized-t-shirt-white', 100, 'Torgny Pocket T-Shirt - White', BG + '/products/torgny-pocket-t-shirt-white', 'range', BG + '/collections/t-shirts-1', ''),
           polo=G(420, 'Benny Wool/Cashmere Polo - Navy', BG + '/products/benny-wool-cashmere-polo-navy-1', 420, 'Benny Wool/Cashmere Polo', BG + '/products/benny-wool-cashmere-polo-navy-1', 'single', BG + '/collections/knitwear', 'knitted polo; parent listing knitwear'),
           dress_shirt=G(240, 'Ferdinand Oxford Button Down Shirt - White', BG + '/products/ferdinand-oxford-button-down-shirt-white-5', 380, 'Francois Denim Shirt - Dark Blue Wash', BG + '/products/francois-denim-shirt-dark-blue-wash', 'range', BG + '/collections/shirts', 'no elevated dress shirt; Fernando Western 380'),
           jeans=G(470, 'Arthuro Jeans - Rinsed Indigo', BG + '/products/arthuro-jeans-rinsed-indigo', 470, 'Arthuro Jeans', BG + '/products/arthuro-jeans-rinsed-indigo', 'single', BG + '/collections/jeans', ''),
           dress_pants=G(480, 'August Flannel Trousers - Charcoal', BG + '/products/august-flannel-trousers-charcoal-1', 480, 'Alfredo Flannel Trousers - Charcoal', BG + '/products/alfredo-flannel-trousers-charcoal', 'range', BG + '/collections/trousers', 'cotton and corduroy trousers 430'),
           sweater=G(560, 'Brian Aran Sweater - Dark Blue (90% wool, 10% cashmere)', BG + '/products/brian-aran-sweater-dark-blue', 820, 'Ben Cashmere Sweater - Cream (100% cashmere)', BG + '/products/ben-cashmere-sweater-cream', 'pair', BG + '/collections/knitwear', 'high is 100% cashmere (elevated)'),
           outerwear=G(1700, 'Nelson II Tweed Raglan Coat - Navy', BG + '/products/nelson-ii-tweed-raglan-coat-navy', 2300, 'Noel Tumbled Leather Jacket - Dark Brown', BG + '/products/noel-tumbled-leather-jacket-dark-brown', 'range', BG + '/collections/outerwear', 'all coats 1700; suede and leather jackets 2300'),
           shoes=G(380, 'Svante Beef Roll Penny Loafer - Dark Brown Grain', BG + '/products/svante-beef-roll-penny-loafer-dark-brown-grain', 380, 'Svante Beef Roll Penny Loafer - Mid Brown Suede', BG + '/products/svante-beef-roll-penny-loafer-mid-brown-suede', 'single', BG + '/collections/shoes', 'loafer in grain and suede both 380; boat shoe 380')),
    own_doors_us=0, own_doors_world=0, locator_url='NONE', doors_basis='facts-first: no store or showroom page anywhere on the site; contact is email only; store paths 404',
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=BG, proposed_tech=NC,
    owned_facility='no claim', named_makers='no', named_mills='no names; cloth origin stated by country ("English cloth", "Portuguese cloth", "Italian yarn", "Italian selvedge denim")',
    made_in_stated_share='24/24 styles (Portugal, Italy; blazer "Made in Europe")', heritage_claim='dated and placed: "Founded in Oslo in 2009, and based in Sweden since 2012" (/pages/carefully-considered-meticulously-made-1)',
    process_documented='no (care and intent described, not process)', craft_url_1=BG + '/pages/carefully-considered-meticulously-made-1', craft_url_2=BG + '/products/nelson-ii-tweed-raglan-coat-brown-cream', proposed_craft=2,
    craft_reasoning='Every style states where it is made and where its cloth or yarn comes from by country, but no mill or maker is named and nothing is owned. That is the rubric 2: a country and little else.',
    founded_year=2009, founded_place='Oslo, Norway', founders=NC, owner_today=NC, ownership_url=NC,
    lookbook_found='yes', lookbook_season_label='Autumn Winter Lookbook Pt. 2', lookbook_mens='yes', lookbook_url=BG + '/pages/autumn-winter-lookbook-pt-2',
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='https://www.grailed.com/designers/berg-berg',
    quote='We expend a great deal of effort making clothes that appear effortless.', quote_who='the house, about page', quote_source='bergbergstore.com /pages/carefully-considered-meticulously-made-1', quote_url=BG + '/pages/carefully-considered-meticulously-made-1', quote_date='undated page (read 2026-10-10)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: bergbergstore.com products.json (163 store-wide), clothing2 + category collections, PDP "Details Materials" for all 88 clothing and shoe products, about page, /pages/usa',
    note='Prices are duties-paid (DDP) for the US. Ties (24), scarves, hats, sunglasses, belts and gloves are most of the store and are out of scope. Lookbook season year not on the page.')

M['Birdwell'] = dict(
    site_domain='birdwell.com', store_used=BW, currency='USD', search_url=BW + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(tee=G(40, 'License Plate T-Shirt - White/Red', BW + '/products/license-plate-t-shirt-white-1', 60, 'Special Teez Pastime', BW + '/products/special-teez-pastime-vintage-white-navy', 'range', BW + '/collections/fw26-t-shirts', 'High Tee Pocket Long Sleeve also 60'),
           polo=NONE_(), dress_shirt=NONE_(), jeans=NONE_(),
           dress_pants=G(200, 'Stockman Chino Pants', BW + '/products/stockman-chino-pants-moss', 200, 'Classic Corduroy Pants', BW + '/products/classic-corduroy-pants-charcoal', 'range', BW + '/collections/fw26-pants', 'chinos stand in; no dress trouser'),
           sweater=G(200, 'Comp Stripe Sweater', BW + '/products/comp-stripe-sweater-gray-navy', 250, 'Comp Zip Sweater', BW + '/products/comp-stripe-hooded-sweater-navy-bone', 'range', BW + '/collections/fw26-sweaters', 'North Pole Sweater (80, a 2024 holiday piece) excluded as a capsule'),
           outerwear=G(175, 'Competition Jacket', BW + '/products/competition-jacket-black-slate', 250, 'Quilt Lined Racing Jacket', BW + '/products/quilt-lined-racing-jacket-brown-bone-gold', 'range', BW + '/collections/mens-jackets-vests', ''),
           shoes=NONE_()),
    own_doors_us=0, own_doors_world=0, locator_url=BW + '/pages/authorized-dealers', doors_basis='see return_counts.csv: no Birdwell-named door anywhere on birdwell.com; dealer page lists third-party shops only',
    tech_named_fabrics='SurfNyl®; SurfStretch®', tech_owned_or_licensed='owned (Birdwell trademarks; "Birdwell\'s proprietary SurfNyl®")', tech_share_of_range='TECH_BW', tech_evidence_url=BW + '/products/310-boardshorts-desert-camo', proposed_tech=NC,
    owned_facility='claim: "we’ve been hand-making boardshorts in the USA since 1961" (/pages/about-us); no facility named or shown',
    named_makers='no', named_mills='no (SurfNyl "Milled and dyed in the USA", mill not named)', made_in_stated_share='MADEIN_BW',
    heritage_claim='dated and placed: "born in Santa Ana, California ... hand-making boardshorts in the USA since 1961" (/pages/about-us); founder Carrie Birdwell-Mann (home page)',
    process_documented='no', craft_url_1=BW + '/pages/about-us', craft_url_2=BW + '/products/310-boardshorts-desert-camo', proposed_craft=2,
    craft_reasoning='States a country (USA) on its boardshorts and a dated, placed heritage since 1961, with an owned-sounding claim of hand-making. No maker, mill or facility is named or shown, so the evidence supports a 2.',
    founded_year=1961, founded_place='Santa Ana, California', founders='Carrie Birdwell-Mann', owner_today=NC, ownership_url=NC,
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='NONE',
    quote='Building on the pillars of enduring quality and timeless style, we’ve been hand-making boardshorts in the USA since 1961.', quote_who='the house, about page', quote_source='birdwell.com /pages/about-us', quote_url=BW + '/pages/about-us', quote_date='undated page (read 2026-10-10)',
    signature_product='310 Boardshorts (SurfNyl®)', signature_product_url=BW + '/products/310-boardshorts-desert-camo', status='partial',
    source=f'Chrome {D}: birdwell.com products.json (372), body_html Fabric lines, /pages/about-us, home page, /pages/authorized-dealers',
    note='Style = SKU stem. SurfNyl® filed as nylon (polyamide) per ruling 10 Oct 2026 (the site states no fibre). The 11 SurfStretch® boardshorts stay undisclosed: no fibre stated and no ruling. Boardshorts are swim (21 styles).')

M['Blundstone'] = dict(
    site_domain='blundstone.com', store_used=BL + ' (Blundstone USA)', currency='USD', search_url=BL + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(tee=NONE_(), polo=NONE_(), dress_shirt=NONE_(), jeans=NONE_(), dress_pants=NONE_(), sweater=NONE_(), outerwear=NONE_(),
           shoes=G(155, "Men's Aerocork #2699 (154.95)", BL + '/products/sand-suede-leather-sandals-mens-style-2699', 395, "Men's Heritage #156 (394.95)", BL + '/products/black-premium-leather-heritage-chelsea-boots-mens-style-156', 'range', BL + '/collections/mens-shoes',
                   "no loafer; the staple Men's Originals #500 is 209.95")),
    styles=dict(styles_total=0, styles_with_composition=0, natural_pct=NC, synthetic_pct=NC, cellulosic_pct=NC, spandex_styles=0, shape=NC, natural_categories='[]', synthetic_categories='[]',
                colourway_ratio='0/0', style_method='manual', swim_styles=0, swim_share_of_range=NC, mens_styles_excl_swim=0),
    own_doors_us=7, own_doors_world=NC, locator_url=BL + '/pages/blundstone-shops', doors_basis="brand's shops page: Williamsburg, SoHo, Boston, Seattle, Silver Lake, Portland, Chicago; world not read",
    tech_named_fabrics=NC, tech_owned_or_licensed=NC, tech_share_of_range=NC, tech_evidence_url=NC, proposed_tech=NC,
    owned_facility=NC, named_makers=NC, named_mills=NC, made_in_stated_share=NC, heritage_claim='dated and placed: "John Blundstone started making fit-for-purpose footwear ... Hobart, Tasmania, in 1870" (/pages/our-story)',
    process_documented=NC, craft_url_1=BL + '/pages/our-story', craft_url_2=NC, proposed_craft=NC, craft_reasoning='Not read past the heritage page within the time box; footwear-only house. No proposal.',
    founded_year=1870, founded_place='Hobart, Tasmania', founders='John Blundstone', owner_today=NC, ownership_url=NC,
    lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=247144&catalog[]=5', vinted_brand_ids='247144', grailed_url='https://www.grailed.com/designers/blundstone',
    quote='For over 150 years we’ve been a company always on the go, always evolving.', quote_who='the house, our-story page', quote_source='blundstone.com /pages/our-story', quote_url=BL + '/pages/our-story', quote_date='undated page (read 2026-10-10)',
    signature_product="Men's Originals #500 (Chelsea boot)", signature_product_url=BL + '/products/stout-brown-premium-leather-v-cut-boots-mens-style-500', status='partial',
    source=f'Chrome {D}: blundstone.com /collections/mens-shoes products.json (89), /pages/blundstone-shops, /pages/our-story',
    note='Footwear-only house: seven NONE garments as expected, and no clothing, so no style table. The retailer locator (/pages/stores) renders client-side and its stockists were not read.')

COMMON = dict(b_corp='NC', b_corp_entity='NC', gots_certified='NC', gots_entity='NC', pronunciation='NC', read_date=D)

BE = 'https://www.beams.co.jp'
M['Beams'] = dict(
    site_domain='beams.co.jp', store_used=BE + ' (Japanese store, JPY; no US storefront)', currency='JPY', search_url=BE + '/search/?search=true', feed_currency_rate='not shopify', sublines_included='BEAMS PLUS (label 0038) only — scope for ruling',
    g=dict(tee=G(6600, 'BEAMS PLUS Pocket Tee Colored Grandrelle', BE + '/item/beamsplus/t-shirt/38040095156/', 16500, 'BEAMS PLUS Pocket Tee Multi Stripe', BE + '/item/beamsplus/t-shirt/38140099103/', 'range', BE + '/category/t-shirt/?label=0038', 'listing prices; third-party and 【別注】 items excluded'),
           polo=G(16500, 'BEAMS PLUS Knit Polo Velour', BE + '/item/beamsplus/shirt/38120049156/', 35200, 'BEAMS PLUS Pique Polo 7G', BE + '/item/beamsplus/shirt/38120046156/', 'range', BE + '/category/shirt/?label=0038', 'polos sit in the shirt category'),
           dress_shirt=G(11000, 'BEAMS PLUS B.D. Short Sleeve Oxford', BE + '/item/beamsplus/shirt/38010032139/', 69300, 'BEAMS PLUS MIL-Shirt Supima Herringbone Big Camo Print', BE + '/item/beamsplus/shirt/38112049139/', 'range', BE + '/category/shirt/?label=0038', 'casual shirting house: button-downs and work shirts; no dress shirt as such'),
           jeans=NP if False else dict(low='NC', low_product='NC', low_url='NC', high='NC', high_product='NC', high_url='NC', basis='NC', mens_listing_url=BE + '/category/pants/?label=0038', _note='pants listing timed out at 30, 60 and 90 s'),
           dress_pants=dict(low='NC', low_product='NC', low_url='NC', high='NC', high_product='NC', high_url='NC', basis='NC', mens_listing_url=BE + '/category/pants/?label=0038', _note='pants listing timed out'),
           sweater=dict(low='NC', low_product='NC', low_url='NC', high='NC', high_product='NC', high_url='NC', basis='NC', mens_listing_url=BE + '/category/tops/?label=0038', _note='tops (knitwear) listing timed out at 30, 60 and 90 s'),
           outerwear=G(24200, 'BEAMS PLUS MIL Liner Jersey Back Fleece', BE + '/item/beamsplus/blouson/38180001139/', 206800, 'BEAMS PLUS Overcoat Herringbone Tweed', BE + '/item/beamsplus/coat/38190165564/', 'range', BE + '/category/blouson/?label=0038', 'blouson, coat and jacket listings combined; Post Overalls deerskin jacket (308,000) is third-party'),
           shoes=G(53900, 'BEAMS PLUS Oxford Shoes Suede', BE + '/item/beamsplus/shoes/38320072302/', 53900, 'BEAMS PLUS Oxford Shoes Suede', BE + '/item/beamsplus/shoes/38320072302/', 'single', BE + '/category/shoes/?label=0038', 'only own-label shoe; 44 others on the label page are 【別注】 or third-party (Alden, Sperry ...)')),
    styles=dict(styles_total='NC', styles_with_composition=16, natural_pct='NC', synthetic_pct='NC', cellulosic_pct='NC', spandex_styles='NC', shape='NC', natural_categories='[]', synthetic_categories='[]',
                colourway_ratio='NC', style_method='product_code', swim_styles='NC', swim_share_of_range='NC', mens_styles_excl_swim='NC'),
    own_doors_us=0, own_doors_world='NC', locator_url=BE + '/shop/', doors_basis='facts-first shop finder: overseas doors in China, Hong Kong, Taiwan, Thailand, Singapore; none in the US; world not counted',
    tech_named_fabrics='NONE in sample', tech_owned_or_licensed='NONE', tech_share_of_range='NC', tech_evidence_url='NC', proposed_tech=NC,
    owned_facility=NC, named_makers=NC, named_mills=NC, made_in_stated_share='16/16 sampled product pages state 原産国 (country of origin): 10 Japan, 6 China', heritage_claim=NC, process_documented=NC,
    craft_url_1=NC, craft_url_2=NC, proposed_craft=NC, craft_reasoning='Not read within the time box; no proposal.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    lookbook_found='yes', lookbook_season_label='BEAMS PLUS 2026AW LOOK', lookbook_mens='yes', lookbook_url=BE + '/special/beamsplus/2026aw/look/',
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=327116&brand_ids[]=7373680&catalog[]=5', vinted_brand_ids='327116 (Beams); 7373680 (Beams Plus)', grailed_url='https://www.grailed.com/designers/beams-plus',
    quote='NC', quote_who='NC', quote_source='NC', quote_url='NC', quote_date='NC',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: beams.co.jp/beamsplus/, BEAMS PLUS label (0038) category listings t-shirt, shirt, blouson, coat, jacket, suit, shoes; 25 sampled product pages (16 loaded)',
    note='Server answers in 10–90 s per page. 327 items enumerated on the label pages, 151 of them own-label (title without "Brand /" and without 【別注】); tops and pants never loaded. Style table holds the 16 sampled styles with composition only: 16 of 16 cotton-, wool- or silk-led on the main line; 11 are 100% cotton, 1 wool, 1 silk, 3 blends with rayon, nylon or cupro. Grailed also has /designers/beams-japan. Mark: BEAMS.')

BA = 'https://beams-america.com'
M['Beams'] = dict(
    site_domain='beams-america.com', store_used=BA + ' (Beams America, USD)', currency='USD', search_url=BA + '/search?q=', feed_currency_rate='1.0', sublines_included='BEAMS T; "the A" by BEAMS; BEAMS JAPAN (geta only)',
    g=dict(tee=G(100, 'Ryota Daimon Art For Everyday Tee (BEAMS T)', BA + '/products/7508165614619', 140, 'Vintage Layered Fade Long-Sleeve T-Shirt', BA + '/products/beams-vintage-layered-fade-long-sleeve-t-shirt-faded-black', 'range', BA + '/collections/mens-t-shirts', 'mens-t-shirts is multi-brand; BEAMS-only listing is /collections/beams'),
           polo=G(165, 'Striped Velvet Polo Shirt', BA + '/products/beams-striped-velvet-polo-shirt-burgundy', 165, 'Striped Velvet Polo Shirt', BA + '/products/beams-striped-velvet-polo-shirt-burgundy', 'single', BA + '/collections/mens-shirts', 'only own-label polo'),
           dress_shirt=G(150, 'Broadcloth Shirt', BA + '/products/beams-broadcloth-shirt-sax', 413, 'Indigo Check Shirt', BA + '/products/indigo-check-shirt', 'range', BA + '/collections/mens-shirts', 'casual shirting; no dress shirt as such'),
           jeans=G(184, 'Wide Fit Denim Pants', BA + '/products/wide-denim-1', 436, 'Selvedge Indigo Denim Pants', BA + '/products/selvedge-denim-pants', 'range', BA + '/collections/mens-denim', 'one Wide Fit Denim colourway is 220'),
           dress_pants=G(255, 'Easy-Wear Relaxed Fit Wide Slacks', BA + '/products/1123120188717', 255, 'Easy-Wear Relaxed Fit Wide Slacks', BA + '/products/1123120188717', 'single', BA + '/collections/mens-pants', 'chinos from 190'),
           sweater=G(165, '7-Gauge Mesh Crew Neck Top', BA + '/products/1115197580379', 516, '5 Gauge Suvin Crewneck', BA + '/products/5-gauge-suvin-crewneck', 'range', BA + '/collections/mens-knitwear', 'no crewneck in an elevated fibre'),
           outerwear=G(295, 'Nep Denim Zip Jacket', BA + '/products/1118952179175', 803, '"the A" by BEAMS MA1', BA + '/products/crazy-ma1', 'range', BA + '/collections/mens-coats-jackets', 'Goat Leather Wide Short Fit Zip Jacket 800'),
           shoes=G(125, 'BEAMS JAPAN Wooden Geta Sandal', BA + '/collections/mens-shoes', 125, 'BEAMS JAPAN Wooden Geta Sandal', BA + '/collections/mens-shoes', 'single', BA + '/collections/mens-shoes', 'only own-label shoe; the rest of the shoe listing is Hender Scheme, OAO, adidas, PPACO, Hoka')),
    own_doors_us=1, own_doors_world=NC, locator_url=BA + '/pages/our-locations', doors_basis="Beams America's locations page: BEAMS MALIBU, 23710 Malibu Rd, Malibu CA 90265; world not counted",
    tech_named_fabrics='Renewool (recycled wool blend, 1 style)', tech_owned_or_licensed=NC, tech_share_of_range='1/67', tech_evidence_url=BA + '/products/beams-renewool-jacket-charcoal-grey', proposed_tech=NC,
    owned_facility=NC, named_makers='no', named_mills='no', made_in_stated_share='MADEIN_BE', heritage_claim='dated: "BEAMS has reimagined American style through a Japanese lens since 1976"; "Born in Tokyo" (/pages/about)',
    process_documented='no', craft_url_1=BA + '/pages/about', craft_url_2=NC, proposed_craft=1,
    craft_reasoning='On the US store, product pages give composition but name no maker or mill and state a country on only a handful of styles. Heritage is dated (1976, Tokyo). Nothing about making is checkable here.',
    founded_year=1976, founded_place='Tokyo', founders=NC, owner_today=NC, ownership_url=NC,
    lookbook_found='yes', lookbook_season_label="BEAMS FALL WINTER '26", lookbook_mens='mixed', lookbook_url=BA + '/collections/beams-fall-winter-26',
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=327116&brand_ids[]=7373680&catalog[]=5', vinted_brand_ids='327116 (Beams); 7373680 (Beams Plus)', grailed_url='https://www.grailed.com/designers/beams-plus',
    quote='BEAMS has reimagined American style through a Japanese lens since 1976.', quote_who='the house (Beams America), about page', quote_source='beams-america.com /pages/about', quote_url=BA + '/pages/about', quote_date='undated page (read 2026-10-10)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: beams-america.com /collections/all-mens products.json (381), vendor BEAMS + BEAMS T = 140 products / 74 SKU stems, PDP "Composition & Care" for every stem, /pages/about, /pages/our-locations',
    note='Re-read on beams-america.com per ruling 10 Oct (replaces the beams.co.jp attempt). Beams America is multi-brand: only vendor BEAMS and BEAMS T counted (140 of 381 men\'s products); NEEDLES, TEATORA, Hender Scheme, Buzz Rickson\'s etc. excluded. 67 clothing styles; composition on 59. Labels use "polyurethane" for stretch (Japanese labelling) — filed as written, so spandex_styles undercounts stretch. US door count corrected 0 -> 1 (BEAMS MALIBU). Mark: BEAMS.')
