D = '2026-10-12'
NC = 'NC'

def G(low, lp, lu, high, hp, hu, basis, listing, note=''):
    return dict(low=low, low_product=lp, low_url=lu, high=high, high_product=hp, high_url=hu, basis=basis, mens_listing_url=listing, _note=note)

def NONE_(listing='NONE', note=''):
    return dict(low='NONE', low_product='NONE', low_url='NONE', high='NONE', high_product='NONE', high_url='NONE', basis='NONE', mens_listing_url=listing, _note=note)

def NCG(listing='NC', note=''):
    return dict(low=NC, low_product=NC, low_url=NC, high=NC, high_product=NC, high_url=NC, basis=NC, mens_listing_url=listing, _note=note)

def NP(listing, note=''):
    return dict(low='np', low_product=NC, low_url=NC, high='np', high_product=NC, high_url=NC, basis='np', mens_listing_url=listing, _note=note)

def VIN(i): return f'https://www.vinted.com/catalog?brand_ids[]={i}&catalog[]=5'

COMMON = dict(b_corp=NC, b_corp_entity=NC, gots_certified=NC, gots_entity=NC, pronunciation=NC, read_date=D)
NOLOOK = dict(lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC)
NO_STYLES = dict(styles_total=0, styles_with_composition=0, natural_pct=NC, synthetic_pct=NC, cellulosic_pct=NC, spandex_styles=0, shape=NC,
                 natural_categories='[]', synthetic_categories='[]', colourway_ratio='0/0', style_method='manual', swim_styles=0, swim_share_of_range=NC, mens_styles_excl_swim=0)
NC_STYLES = dict(styles_total=NC, styles_with_composition=NC, natural_pct=NC, synthetic_pct=NC, cellulosic_pct=NC, spandex_styles=NC, shape=NC,
                 natural_categories=NC, synthetic_categories=NC, colourway_ratio=NC, style_method=NC, swim_styles=NC, swim_share_of_range=NC, mens_styles_excl_swim=NC)
M = {}

# ------------------------------------------------------------------------------------------------ Gap
GP = 'https://www.gap.com/browse/product.do?pid='
GL = 'https://www.gap.com/browse/men/shop-all-styles?cid=1127944'
M['Gap'] = dict(
    site_domain='gap.com', store_used="https://www.gap.com (read through the site's own product-search API, api.gap.com product_search_cc_aggregations, cid 1127944, department 75)",
    currency='USD', search_url=NC, feed_currency_rate='not shopify',
    sublines_included='GapStudio (elevated line sold as Gap, counted); OuiGap is a capsule (in the fibre layer, never a high)',
    g=dict(
        tee=G(19.95, 'Classic T-Shirt', GP + '440775002', 78, 'GapStudio Extra Heavyweight Pocket T-Shirt', GP + '910342002', 'range', GL, 'regularPrice; most items carry a "40% off at checkout" flag; main-line tees top out below GapStudio'),
        polo=G(34.95, 'Pique Polo Shirt', GP + '223627012', 69.95, 'Heavyweight Jersey Polo Shirt', GP + '800317012', 'range', GL, 'Oversized Pique Polo also 69.95'),
        dress_shirt=G(49.95, 'Dobby Relaxed Straight-Hem Shirt', GP + '886386002', 118, 'GapStudio Poplin Big Shirt', GP + '910343002', 'range', GL,
                      'no dress shirts sold; casual woven shirts stand in; Denim Relaxed Utility Shirt Jacket also 118'),
        jeans=G(69.95, 'Straight Jeans in GapFlex', GP + '709159002', 168, 'GapStudio Baggy Utility Jeans', GP + '1182714002', 'range', GL, 'main-line high is the Baggy Jeans at 99.95'),
        dress_pants=G(59.95, 'Modern Slim Khakis', GP + '440943002', 89.95, 'Heavyweight Twill Baggy Khakis', GP + '907827002', 'range', GL, 'no dress trousers sold; khakis stand in'),
        sweater=G(69.95, 'CashSoft Crew Sweater', GP + '907276002', 89.95, 'CashSoft Crew Sweater (dearest colours)', GP + '907276002', 'range', GL,
                  'one crew style spans the slot: colours run 69.95-89.95; CashSoft is a house yarn name, not cashmere'),
        outerwear=G(89.95, 'Classic Icon Denim Jacket', GP + '819576002', 248, 'Wool-Blend Car Coat (50% wool)', GP + '1186542002', 'range', GL, 'GapStudio Herringbone Peacoat 168'),
        shoes=NONE_(listing=GL, note='no men\'s footwear in the men\'s catalogue')),
    own_doors_us=150, own_doors_world=NC, locator_url='https://www.gap.com/stores',
    doors_basis='gap.com/stores crawl, 393 store pages read 12 Oct; format from each page\'s store_type: 149 Gap full-price (Gap, babyGap, GapKids, GapBody banners) + 1 mixed record (Wichita, lists Gap banners and Gap Factory Store; counted, flagged) = 150 own doors incl. 1 in Puerto Rico; 241 Gap Factory Store = outlets, not counted; 2 pages with every day "closed" and no store type (Fresno 3685 North Gap Drive; Chester NJ 270 US-206) excluded. Non-US stores not read.',
    tech_named_fabrics='TECH_GAP', tech_owned_or_licensed='own house names: GapFlex (stretch denim), CashSoft (knit yarn); licensed: TENCEL / Lenzing (lyocell, modal) and LYCRA named in compositions',
    tech_share_of_range='TECHSHARE_GAP', tech_evidence_url=GP + '709159002', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no (the API names a supplier group per colour, e.g. Yakjin Trading, Makalot, Shinwon, Sae-A, Hansae, Arvind, Nien Hsing; not shown on product pages)',
    named_mills='no', made_in_stated_share='MADEIN_GAP', heritage_claim='NC (no about page read)', process_documented='no',
    craft_url_1=GP + '440775002', craft_url_2='https://www.gap.com/stores', proposed_craft=1,
    craft_reasoning='Every own style states its composition and "Imported", but no country, maker or mill appears to shoppers; nothing on making was found.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url=VIN(6), vinted_brand_ids='6', grailed_url='https://www.grailed.com/designers/gap',
    quote=NC, quote_who=NC, quote_source=NC, quote_url=NC, quote_date=NC,
    signature_product=NC, signature_product_url=NC, status='partial (large house: full catalogue counted, fibre shares from a 152-row category-stratified sample)',
    source=f'Chrome {D}: api.gap.com product_search_cc_aggregations (769 rows, pages 0-6), product.do PDP fabric bullets for 290 men\'s styles, gap.com/stores state-city-store pages (393; ld+json address, markerData store_type)',
    note='Style = style id (cc minus colour): 290 men\'s clothing styles / 869 colours; 46 collaboration or licensed-collab styles excluded (Gap x A.P.C. 15, Gap x Malbon 13, Gap x BEIS, Gap x Disney, Gap / Lichtenstein / Whitney 7, FIFA World Cup 3, NBA 5, NFL 49ers) -> 244 own styles / 816 colours. Licensed band and artist graphic tees without an "x" kept as Gap product. Dropship third-party listings (109) and women\'s excluded. Four store addresses carried typos on the store page (Labeaus, Highgway, Villge, Blv) and are written corrected in own_doors.csv.')

# ------------------------------------------------------------------------------------------------ Goldwin
GW = 'https://us.goldwin.global'; GWP = GW + '/products/'
M['Goldwin'] = dict(
    site_domain='us.goldwin.global', store_used=GW + ' (Shopify; goldwin.com does not reach the house)', currency='USD', search_url=GW + '/search?q=', feed_currency_rate='1.0',
    sublines_included='Goldwin 0 ("experimental and technical platform", 2022; sold under Goldwin, counted). C3fit (separate compression brand) and Coming Soon pieces excluded',
    g=dict(
        tee=G(100, 'WF-Dry T-shirt', GWP + 'gm66119', 350, 'Moon Hybrid L/S T-shirt (84% nylon, 16% spandex)', GWP + 'gm46342', 'range', GW + '/collections/men', ''),
        polo=NONE_(note='no polo shirt sold: shirts-poloshirts holds woven shirts and pullovers'),
        dress_shirt=G(230, 'All Direction Light S/S Shirt (compare-at 230; on sale 161)', GWP + 'gm55101', 400, 'Goldwin 0 Retroreflective Striped Shirt', GWP + 'gz56104', 'range', GW + '/collections/men',
                      'casual and technical shirts; no dress shirt'),
        jeans=G(370, 'Goldwin 0 Helicoid Jeans', GWP + 'gz76154', 370, 'Goldwin 0 Helicoid Jeans', GWP + 'gz76154', 'single', GW + '/collections/men', 'only jean sold'),
        dress_pants=G(240, 'One Tuck Tapered Light Pants (compare-at 240; on sale 168)', GWP + 'gl76180', 430, 'Hyperdense Taffeta U/S Destra Pants (90% polyester, 10% wool)', GWP + 'gl76170',
                      'range', GW + '/collections/men', 'trousers stand in; the PERTEX SHIELD PRO Mountaineering Pants (490, gm76157) sold out between the 12 Oct capture and the spot-check, so not taken; Goldwin 0 3L Rain Wrap (400) left out as rainwear'),
        sweater=G(250, 'Mesh Pile Crew (compare-at 250; on sale 175)', GWP + 'gm35301', 350, 'Ulmus Knit Cardigan', GWP + 'gl36334', 'range', GW + '/collections/men', 'knitwear typed sweaters-cardigans; all polyester (no elevated fibre)'),
        outerwear=G(250, 'Floating Wind Shell Vest (compare-at 250; on sale 175)', GWP + 'gm16106', 1300, 'Voxeloft Insulated Vest', GWP + 'g56304', 'range', GW + '/collections/men',
                    'Coming Soon pieces (Auxetic Inflatable Vest 1400) not yet on sale, excluded'),
        shoes=NONE_(note='no footwear sold')),
    own_doors_us=1, own_doors_world=16, locator_url=GW + '/pages/shoplist',
    doors_basis='brand shop list (re-read 12 Oct): US 1 (Goldwin NewYork, 300 Lafayette Street); world 16 Goldwin-named shops: New York; Tokyo Marunouchi and Harajuku, Kyoto, Sapporo; London; Munich; Seoul (Eonju-ro); China 8 (Beijing Sanlitun, Chengdu Taikoo Li, Shanghai Jing\'an Kerry Centre, Hangzhou, Nanjing Deji Plaza, Shenyang MixC, Shenzhen MixC, Xi\'an SEG), the China shops sitting in shopping centres. 4 Korean department-store shops (Shinsegae Gangnam, Hyundai Pangyo, Shinsegae Centum City, Hyundai Trade Center) = concessions, not counted; 3 GRAVITY ski shops (Kanda, Niseko, Yuzawa) not Goldwin-named, not counted (for ruling). The worklist "SF store" does not appear.',
    tech_named_fabrics='GORE-TEX (3L, PRO, PAC-LITE, LABS); WINDSTOPPER by GORE-TEX LABS; PERTEX (Quantum, Quantum Air, Shield Pro, Unlimited, Equilibrium); POLARTEC (200, Wind Pro, Power Wool); CORDURA; SOLOTEX; THERMOFRAME; CLEANDOWN; Polygiene StayFresh; KODENSHI; Brewed Protein (Spiber)',
    tech_owned_or_licensed='licensed: GORE-TEX / WINDSTOPPER, PERTEX, POLARTEC, CORDURA, SOLOTEX, CLEANDOWN, Polygiene; Brewed Protein from Spiber (partner); THERMOFRAME and KODENSHI not stated as owned or licensed',
    tech_share_of_range='TECHSHARE_GOLD', tech_evidence_url=GW + '/pages/brand-material', proposed_tech=NC,
    owned_facility='history only: began in 1950 as the Tsuzawa Knit Fabric Factory in Oyabe City (/pages/brand); no present-day own factory claimed',
    named_makers='no', named_mills='no (fabric brands named, not mills)', made_in_stated_share='MADEIN_GOLD',
    heritage_claim='dated and placed: "GOLDWIN started its page of history in 1950 from a small knit fabric factory, Tsuzawa Knit Fabric Factory, in Oyabe City in Toyama Prefecture" (/pages/brand)',
    process_documented='no', craft_url_1=GW + '/pages/brand', craft_url_2=GWP + 'gm46342', proposed_craft=2,
    craft_reasoning='Product pages state composition and a country of origin on 139 of 146 styles and name the fabric technologies; the brand page gives the 1950 knit-factory origin, but no maker, mill or making process is shown today.',
    founded_year=1950, founded_place='Oyabe City, Toyama Prefecture, Japan', founders=NC, owner_today='Goldwin Inc. (footer: © GOLDWIN INC.)', ownership_url=GW,
    **NOLOOK,
    vinted_mens_url=VIN(330213), vinted_brand_ids='330213', grailed_url='https://www.grailed.com/designers/goldwin',
    quote='Harmony with nature can, and should, be heightened by the clothes you wear.', quote_who='the house, brand manifesto', quote_source='us.goldwin.global /pages/brand', quote_url=GW + '/pages/brand',
    quote_date='undated page (read 2026-10-12)', signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: us.goldwin.global products.json (232; 201 available), PDP composition and Country of origin (146), /pages/brand, /pages/brand-material, /pages/shoplist, .js price spot-check',
    note='Style = style code from the SKU (2363-GL26337-NM-1 -> GL26337): men-tagged clothing (every men\'s piece is also tagged unisex) 152 listings, one colour per listing -> 149 codes; 3 collaborations excluded (Goldwin x Cactus Store 2; Goldwin 0 PERTEX SHIELD PRO Gleam Anorak, performance x nur) -> 146 styles. Composition is the face fabric. Markdown house: regular = compare-at. No polo, one jean.')

# ------------------------------------------------------------------------------------------------ Golf Wang
GWG = 'https://golfwang.com'; GWGP = GWG + '/products/'
M['Golf Wang'] = dict(
    site_domain='golfwang.com', store_used=GWG, currency='USD', search_url=GWG + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(48, 'FORSAKEN TEE', GWGP + 'foresaken-tee-by-golf-wang', 55, 'FALL WASHED LOGO TEE', GWGP + 'washed-brown-logo-tee-by-golf-wang', 'range', GWG + '/collections/tees',
              'album and tour merchandise (CHROMAKOPIA, Don\'t Tap The Glass) kept out (for ruling); Eye Test Long Sleeve Tee also 55'),
        polo=G(110, 'DANTE STRIPED POLO', GWGP + 'dante-striped-polo-by-golf-wang', 110, 'DANTE STRIPED POLO', GWGP + 'dante-striped-polo-by-golf-wang', 'single', GWG + '/collections/tops', 'only polo'),
        dress_shirt=G(98, 'TIGER BOWLING SHIRT', GWGP + 'tiger-bowling-shirt-by-golf-wang', 150, 'AUTUMN LINEN BUTTON UP (100% linen)', GWGP + 'autumn-linen-button-up-by-golf-wang', 'range', GWG + '/collections/tops',
                      'casual shirts; no dress shirt'),
        jeans=G(128, 'STRIPED DENIM PANT', GWGP + 'striped-denim-pant-by-golf-wang', 128, 'STRIPED DENIM PANT', GWGP + 'striped-denim-pant-by-golf-wang', 'single', GWG + '/collections/bottoms', 'only denim trouser'),
        dress_pants=G(108, 'RELAXED CHINO PANTS', GWGP + 'relaxed-chino-pants-by-golf-wang', 108, 'RELAXED CHINO PANTS', GWGP + 'relaxed-chino-pants-by-golf-wang', 'single', GWG + '/collections/bottoms', 'chino stands in'),
        sweater=G(108, 'FORSAKEN JACQUARD SWEATER', GWGP + 'forsaken-jacquard-sweater-by-golf-wang', 108, 'FORSAKEN JACQUARD SWEATER', GWGP + 'forsaken-jacquard-sweater-by-golf-wang', 'single', GWG + '/collections/tops', 'only knit sweater'),
        outerwear=G(130, 'STRIKE TRACK JACKET', GWGP + 'strike-track-jacket-by-golf-wang', 244, 'HEATHER WOOL VARSITY (wool shell, cowskin leather sleeves)', GWGP + 'heather-wool-varsity-by-golf-wang', 'range', GWG + '/collections/outerwear',
                    'Striped Denim Overshirt (120) typed outerwear; Glass Jacket (160) is box-set merchandise, kept out'),
        shoes=NONE_(listing='NONE', note='only shoe is the CLARKS WALLABEE by GOLF WANG (vendor Clarks), a collaboration')),
    own_doors_us=2, own_doors_world=4, locator_url=GWG + '/pages/golf-wang-la (one page per store: golf-wang-la, golf-wang-new-york, golf-wang-london, golf-wang-sydney)',
    doors_basis='brand store pages /pages/golf-wang-la, -new-york, -london, -sydney (live 12 Oct): Los Angeles 350 N. Fairfax Ave, New York 35 Howard St, London 57-59 Beak Street, Sydney 58 Oxford Street; the holiday-shop page lists 2-24 Dec 2023 pop-ups (closed, not counted)',
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=GWGP + 'tucker-flannel-button-up-by-golf-wang', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no on product pages (the feed\'s vendor field carries factory names, e.g. WAN NING GARMENT, REIMAGINE, not shown to shoppers)', named_mills='no',
    made_in_stated_share='0/42 own styles state a country (no "Made in" on any product body)', heritage_claim='none on site (/pages/about is an empty shell)', process_documented='no',
    craft_url_1=GWG + '/pages/about', craft_url_2=GWGP + 'heather-wool-varsity-by-golf-wang', proposed_craft=1,
    craft_reasoning='Product bodies name the fibre in words (percentages on 3 of 42) and nothing more: no country, maker, mill or making story; the about page is empty.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url=VIN(379819), vinted_brand_ids='379819 (also 7386290 "Golf Wang x Tyler The Creator")', grailed_url='https://www.grailed.com/designers/golf-wang',
    quote=NC, quote_who=NC, quote_source=NC, quote_url=NC, quote_date=NC, signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: golfwang.com products.json (145; 143 available), product bodies, store pages (LA, NYC, London, Sydney), holiday-shops page, .js price spot-check',
    note='Style = SKU stem; one colour per listing: 62 clothing listings -> 42 own styles after excluding 19 album/tour merchandise pieces (CHROMAKOPIA and TOUR25 tags, CH24/CHR24/TTC codes, Don\'t Tap The Glass box set; for ruling) and 1 other label (ALMOST FAMOUS by BRICK STOWELL). Boxers counted in the fibre layer as underwear. No markdowns. NFL "by GOLF" and Converse pages are collaborations.')

# ------------------------------------------------------------------------------------------------ Hender Scheme
HS = 'https://online.henderscheme.com'; HSI = HS + '/item/detail/'
M['Hender Scheme'] = dict(
    site_domain='henderscheme.com', store_used=HS + ' (スキマ Hender Scheme Official Online Shop; prices tax-inclusive)', currency='JPY', search_url=NC, feed_currency_rate='not shopify', sublines_included='-',
    g=dict(
        tee=NONE_(), polo=NONE_(), dress_shirt=NONE_(), jeans=NONE_(), dress_pants=NONE_(), sweater=NONE_(),
        outerwear=G(204050, 'collar jacket (leather)', HSI + '1_1_zw-c-lcj_1/black', 204050, 'collar jacket (leather)', HSI + '1_1_zw-c-lcj_1/black', 'single', HS + '/item?category_id=520',
                    'the only clothing piece: the wear category holds this jacket and a glove'),
        shoes=G(83160, 'loafer #2146', HSI + '1_1_vs-rs-loa_1/black', 98098, 'argyle loafer', HSI + '1_1_zw-s-agl_1/argyleblack', 'pair', HS + '/item?category_id=503',
                'loafers; polar loafer 93,478; dearest shoe mip-34 135,850; Artek + Hender Scheme collaboration excluded')),
    own_doors_us=0, own_doors_world=6, locator_url='https://henderscheme.com (shop pages)',
    doors_basis='directly operated "sukima" shops (エンダースキーマ直営店「スキマ」): Tokyo Ebisu, Kappabashi, Miyashita Park; Osaka; Fukuoka; Nagoya. The door sign reads "sukima" with Hender Scheme; counted as own doors, flagged for ruling. No US shop.',
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE (soles co-developed with Vibram on some shoes; not a fabric)', tech_share_of_range='0', tech_evidence_url='https://henderscheme.com', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no factory named; "workmen" named as a class ("the workmen exerting their professionalism into each production process")', named_mills='no',
    made_in_stated_share=NC, heritage_claim='collection archive from 2010 A/W ("2011 S/S - manual industry -"); no founding statement read',
    process_documented='partial: manual industrial products re-make sneakers "in a different producing process, the manual industry"; "left to right" uses floor leather; repair service',
    craft_url_1='https://henderscheme.com', craft_url_2=HSI + '1_1_vs-rs-loa_1/black', proposed_craft=2,
    craft_reasoning='The house explains its manual-industry idea and leather choices and offers repairs, but names no workshop, tannery or maker and states no country on the pages read.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url=VIN(388790), vinted_brand_ids='388790', grailed_url='https://www.grailed.com/designers/hender-scheme',
    quote='This uniqueness is created by the workmen exerting their professionalism into each production process.', quote_who='the house, manual industrial products text', quote_source='henderscheme.com',
    quote_url='https://henderscheme.com', quote_date='undated page (read 2026-10-12)', signature_product='manual industrial products (mip), leather re-makes of sneakers', signature_product_url=HS + '/item?category_id=503', status='partial',
    styles=None,
    source=f'Chrome {D}: online.henderscheme.com categories wear (520) and shoes (503), henderscheme.com collection archive and shop pages, stockist page',
    note='Shoe house with one garment: seven garment slots NONE; style table is the collar jacket only (checked for clothing before writing it, per instructions). Prices in JPY as displayed (tax-inclusive). Owner today not stated (corporate link laicos.co.jp).')

# ------------------------------------------------------------------------------------------------ Hickey Freeman
HF = 'https://www.hickeyfreeman.com'
M['Hickey Freeman'] = dict(
    site_domain='hickeyfreeman.com', store_used=HF + ' (single landing page; no shop)', currency=NC, search_url='NONE', feed_currency_rate='not shopify', sublines_included=NC,
    g=dict(tee=NCG(), polo=NCG(), dress_shirt=NP(HF, 'no price published: the site has no shop and sends buyers to Dillard\'s (not read)'), jeans=NCG(),
           dress_pants=NP(HF, 'no price published on the brand site'), sweater=NCG(), outerwear=NP(HF, 'tailoring (suits, sport coats): no price published on the brand site'), shoes=NCG()),
    own_doors_us=0, own_doors_world=0, locator_url='NONE',
    doors_basis='the brand site is one landing page whose only buying route is "SHOP NOW AT DILLARD\'S"; no store list, no own door named (flagged)',
    tech_named_fabrics=NC, tech_owned_or_licensed=NC, tech_share_of_range=NC, tech_evidence_url=NC, proposed_tech=NC,
    owned_facility=NC, named_makers=NC, named_mills=NC, made_in_stated_share=NC, heritage_claim=NC, process_documented=NC,
    craft_url_1=HF, craft_url_2=NC, proposed_craft=NC, craft_reasoning='NC: the brand site carries no product or making text to score.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today='ABG-HMX, LLC (footer: "Hickey Freeman™ is a registered trademark of ABG-HMX, LLC")', ownership_url=HF,
    **NOLOOK,
    vinted_mens_url=VIN(693210), vinted_brand_ids='693210', grailed_url='https://www.grailed.com/designers/hickey-freeman',
    quote=NC, quote_who=NC, quote_source=NC, quote_url=NC, quote_date=NC, signature_product=NC, signature_product_url=NC, status='partial (brand site has no shop; seated as np/NC)',
    styles=NC_STYLES,
    source=f'Chrome {D}: hickeyfreeman.com landing page (brand film, Dillard\'s link, footer)',
    note='No style table: the brand sells only through Dillard\'s from its site, and Dillard\'s was not read. How to seat a house whose own site sells nothing is put for ruling in NOTE.md.')

# ------------------------------------------------------------------------------------------------ Holderness & Bourne
HB = 'https://holdernessandbourne.com'; HBP = HB + '/products/'
M['Holderness & Bourne'] = dict(
    site_domain='holdernessandbourne.com', store_used=HB, currency='USD', search_url=HB + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(60, 'The Mason T-Shirt', HBP + 'the-mason-tshirt-pacific-blue', 90, 'The Carr T-Shirt', HBP + 'the-carr-tshirt-heathered-gray', 'range', HB + '/collections/t-shirts', ''),
        polo=G(115, 'The Anderson Shirt (polo)', HBP + 'the-anderson-shirt-california-spruce', 135, 'The Hatcher Shirt (94% pima cotton)', HBP + 'the-hatcher-shirt-harbor-white', 'range', HB + '/collections/golf-shirts',
               'the house calls its polos "shirts"; Macdonald Shirt also 115; collegiate logo versions not priced'),
        dress_shirt=G(165, 'The Mendenhall Shirt', HBP + 'the-mendenhall-shirt-sonoma-pacific-blue', 178, 'The Cullinane Shirt', HBP + 'the-cullinane-shirt-heathered-vista-blue', 'range', HB + '/collections/button-down-shirt',
                      'button-downs (stretch); no dress shirt'),
        jeans=NONE_(note='no jeans; five-pocket trousers are twill and corduroy'),
        dress_pants=G(178, 'The Baxter 5 Pocket Corduroy Pant', HBP + 'the-baxter-5-pocket-corduroy-pant-driftwood', 188, 'The Wilson 5 Pocket Pant', HBP + 'the-wilson-5-pocket-pant-california-spruce', 'range', HB + '/collections/pants', 'trousers stand in'),
        sweater=G(195, 'The Ward Crewneck Sweater (100% Egyptian cotton)', HBP + 'the-ward-crewneck-sweater-heathered-california-spruce', 645, 'The Buckley Crewneck Sweater (100% Scottish cashmere, Made in Scotland)',
                  HBP + 'the-buckley-crewneck-sweater-heathered-california-spruce', 'pair', HB + '/collections/sweaters', 'crew necks; high is majority cashmere -> pair'),
        outerwear=G(155, 'The Ventura Vest', HBP + 'the-ventura-vest-black', 295, 'The Wells Jacket', HBP + 'the-wells-jacket-cypress', 'range', HB + '/collections/jackets-vests', 'Wells Vest 255'),
        shoes=NONE_(note='no footwear sold')),
    own_doors_us=0, own_doors_world=0, locator_url='NONE',
    doors_basis='no store page and no own store found; distribution through golf-club pro shops and named stockists',
    tech_named_fabrics='AIRATION® (perforated performance fabric); Swing Knit™ (pique)', tech_owned_or_licensed='own: "Our proprietary AIRATION® perforated performance fabric"; Swing Knit™ is a house name',
    tech_share_of_range=NC, tech_evidence_url=HB + '/pages/fabric-guide', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no', named_mills='no by name: "one of the world\'s oldest and most renowned Scottish cashmere mills"; Egyptian cotton "spun and finished in Italy"; pima jersey "Made in Peru"',
    made_in_stated_share='1/92 styles state a country on the product page (Buckley Crewneck, Made in Scotland); the fabric guide places three fabrics (Peru, Scotland, Italy)',
    heritage_claim='founders\' story, undated: "having grown up around the game in North Carolina and on Long Island" (/pages/tenets)', process_documented='no',
    craft_url_1=HB + '/pages/fabric-guide', craft_url_2=HB + '/pages/tenets', proposed_craft=2,
    craft_reasoning='Every style gives its main composition and the fabric guide says where three fabrics are spun or made, but no mill or maker is named and only one product states a country.',
    founded_year=NC, founded_place=NC, founders='Alex Holderness & John Bourne (signed, /pages/tenets)', owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='NONE',
    quote='We firmly believe that quality speaks for itself, and that branding should be subtle.', quote_who='Alex Holderness & John Bourne, founders (Our Story)', quote_source='holdernessandbourne.com /pages/tenets',
    quote_url=HB + '/pages/tenets', quote_date='undated page (read 2026-10-12)', signature_product='Ward Sweater ("our signature Ward Sweater", fabric guide)', signature_product_url=HBP + 'the-ward-crewneck-sweater-heathered-california-spruce',
    status='partial',
    source=f'Chrome {D}: holdernessandbourne.com products.json (723; 713 available), PDP Fabric & Care, /pages/fabric-guide, /pages/tenets, blog, .js price spot-check',
    note='Style = model name (title before ":" minus "The"): 610 men\'s listings -> 600 after the H&B x Yale Golf Course collaboration (10) -> 92 models. Collegiate licensed versions (211 listings, ~25 universities) folded into their base models as colourways and not priced (for ruling). No markdowns. Vinted has no brand entry; Grailed has no designer page.')

# ------------------------------------------------------------------------------------------------ Imogene + Willie
IW = 'https://imogeneandwillie.com'; IWP = IW + '/products/'
M['Imogene + Willie'] = dict(
    site_domain='imogeneandwillie.com', store_used=IW, currency='USD', search_url=IW + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(56, 'spruce knit midweight crew', IWP + 'spruce-knit-midweight-tee', 110, 'long sleeve pocket tee in washed slate', IWP + 'long-sleeve-pocket-tee-in-washed-slate', 'range', IW + '/collections/men',
              'graphic tees (69) and the other 56 crews in the same band'),
        polo=NONE_(note='no polo sold'),
        dress_shirt=G(225, 'lightweight beach oxford in white (100% supima cotton)', IWP + 'classic-oxford-button-down-in-white', 295, 'earl plaid in cedar', IWP + 'earl-plaid-in-cedar', 'range', IW + '/collections/men',
                      'casual wovens; earl plaid in juniper also 295'),
        jeans=G(235, 'barton black rigid jp', IWP + 'barton-black-rigid', 325, 'willie 20oz indigo rigid', IWP + 'willie-20oz-indigo-rigid', 'range', IW + '/collections/men',
                'many fit+wash listings at 325; limited edition love fades no.070 barton (525) left out as a numbered limited edition (capsule); carpenter pants in denim (350-395) left out as work trousers'),
        dress_pants=G(175, 'ventura chore pant in jade', IWP + 'ventura-chore-pant-in-jade-m', 275, 'wilkison trouser in brushstroke camo', IWP + 'wilkison-trouser-in-brushstroke-camo', 'range', IW + '/collections/men', 'non-denim trousers stand in'),
        sweater=G(350, 'galway wool sweater in black nep', IWP + 'the-galway-wool-sweater-in-black-nep-m', 395, 'berkley cardigan marled grey (100% wool)', IWP + 'berkley-cardigan-marl-grey', 'range', IW + '/collections/men',
                  'knitwear; no elevated fibre'),
        outerwear=G(245, 'the "service station" jacket', IWP + 'the-service-station-jacket', 595, 'quilt lined canvas chore coat in camo', IWP + 'quilt-lined-canvas-chore-coat-in-camo', 'range', IW + '/collections/men',
                    'quilt lined washed denim chore coat also 595; i+w x Schott NYC collaboration excluded'),
        shoes=NONE_(note='footwear on the site is third-party only')),
    own_doors_us=2, own_doors_world=2, locator_url=IW + '/pages/locations',
    doors_basis='brand locations page (live 12 Oct): Nashville flagship, 2601 12th Avenue South; Austin, 1401 S Congress Ave',
    tech_named_fabrics='SUPIMA® cotton (named in composition)', tech_owned_or_licensed='licensed: SUPIMA® cotton named in compositions', tech_share_of_range='TECHSHARE_IW', tech_evidence_url=IWP + 'classic-oxford-button-down-in-white', proposed_tech=NC,
    owned_facility='yes, stated: "we constructed our own sewing room in los angeles"; sewing "team of 12" (/pages/our-story)', named_makers='own sewing room (Los Angeles)', named_mills='no',
    made_in_stated_share='brand-wide claim, not per style: "when we started in 2009, we had a simple goal: to make all of our clothing in the usa" (/pages/made-in-usa); per-product "made in usa" text not counted because the site footer carries the same words',
    heritage_claim='dated and placed: "we set up shop in an old service station in Nashville, TN" in 2009 (/pages/our-story)',
    process_documented='partial: small-batch production; own sewing room; chainstitch hemming; free repairs for a year and hardware for life (/pages/denim-repair)',
    craft_url_1=IW + '/pages/our-story', craft_url_2=IW + '/pages/made-in-usa', proposed_craft=4,
    craft_reasoning='The house states it built its own Los Angeles sewing room, gives the team size, claims USA small-batch making since 2009 and runs its own repair service; the room is described rather than shown and no mill is named, so 4 not 5.',
    founded_year=2009, founded_place='Nashville, Tennessee', founders=NC, owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='https://www.grailed.com/designers/imogene-willie',
    quote='when we started in 2009, we had a simple goal: to make all of our clothing in the usa', quote_who='the house, made-in-USA page', quote_source='imogeneandwillie.com /pages/made-in-usa',
    quote_url=IW + '/pages/made-in-usa', quote_date='undated page (read 2026-10-12)', signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: imogeneandwillie.com products.json (625; 535 available), PDP and body composition, /pages/our-story, /pages/made-in-usa, /pages/locations, /pages/stockists, /pages/denim-repair, .js price spot-check',
    note='Mark: imogene + willie (lower case). Own men\'s and unisex clothing 246 listings -> 226 listing keys; denim (one product per fit + wash) grouped by fit, washes as colourways. Third-party lines ("3rd party-*" vendors) and collaborations (i+w x Schott NYC, x Wrangler, x American Woolen) excluded. No markdowns. Vinted has no brand entry.')

# ------------------------------------------------------------------------------------------------ Jos. A. Bank
JB = 'https://www.josbank.com'; JBP = JB + '/p/'
M['Jos. A. Bank'] = dict(
    site_domain='josbank.com', store_used=JB + " (HCL Commerce; read through the site's own search service, store 13452, catalog 14052)", currency='USD', search_url=NC, feed_currency_rate='not shopify',
    sublines_included='Reserve (Collection), 1905 (Collection), Traveler (incl. COOLMOTION, Traveltech), Signature, Executive: sold under Jos. A. Bank, counted',
    g=dict(
        tee=G(29.5, 'Jos. A. Bank Tailored Fit Jersey Tee', JBP + 'jos-a-bank-tailored-fit-jersey-tee', 29.5, 'Jos. A. Bank Tailored Fit Jersey Tee', JBP + 'jos-a-bank-tailored-fit-jersey-tee', 'single', JB + '/c/casual-tops/polo-t-shirts', 'only own tee; list price (site permanently on promotion)'),
        polo=G(39.5, '1905 Collection Tailored Fit Polo', JBP + '1905-collection-tailored-fit-polo', 59.5, 'Traveler® Traditional Fit Short Sleeve Performance Polo', JBP + 'traveler-traditional-fit-short-sleeve-performance-polo', 'range', JB + '/c/casual-tops/polo-t-shirts',
               'other Traveler polos also 59.5'),
        dress_shirt=G(39.5, '1905 Collection Traditional Fit Solid Dress Shirt', JBP + '1905-collection-traditional-fit-solid-dress-shirt-5BHB', 89.5, 'Reserve Collection Traditional Fit Point Collar Formal Solid Dress Shirt (100% Egyptian cotton)',
                      JBP + 'reserve-collection-traditional-fit-point-collar-formal-solid-dress-shirt', 'range', JB + '/c/dress-shirts/all-shirts', ''),
        jeans=G(74.5, 'Jos. A. Bank Slim Fit Ultra Stretch Jean', JBP + 'jos-a-bank-slim-fit-ultra-stretch-jean', 74.5, 'Jos. A. Bank Slim Fit Ultra Stretch Jean', JBP + 'jos-a-bank-slim-fit-ultra-stretch-jean', 'single', JB + '/c/pants/mens-all-pants', 'all four own jeans list at 74.5'),
        dress_pants=G(89, 'Jos. A. Bank Tailored Fit Comfort Stretch Dress Pants', JBP + 'jos-a-bank-tailored-fit-comfort-stretch-dress-pants', 129, 'Reserve Tailored Fit Italian Wool Dress Pants (99% Italian wool)', JBP + 'reserve-tailored-fit-italian-wool-dress-pants',
                      'range', JB + '/c/pants/all-dress-pants', 'suit trousers sold with suits not taken'),
        sweater=G(69.5, 'Jos. A. Bank Tailored Fit Pima Cotton Crew Neck Sweater', JBP + 'jos-a-bank-tailored-fit-pima-cotton-crew-neck-sweater', 199.5, 'Reserve Collection Tailored Crew Neck Cashmere Sweater (100% cashmere)',
                  JBP + 'reserve-collection-tailored-crew-neck-cashmere-sweater', 'pair', JB + '/c/sweaters/crewneck-sweaters', 'crew necks; high is majority cashmere -> pair'),
        outerwear=G(79.5, 'Traveler® Collection Tailored Fit Reversible Quilted Vest', JBP + 'traveler-collection-tailored-fit-reversible-quilted-vest', 595, 'Reserve Collection Tailored Fit Leather Bomber Jacket',
                    JBP + 'reserve-collection-tailored-fit-leather-bomber-jacket', 'range', JB + '/c/outerwear/mens-all-outerwear', 'filed as range: leather is not on the elevated list; dearest textile coat Reserve Collection Traditional Fit Wool Blend Camel Coat 399.5'),
        shoes=G(119.5, 'Jos. A. Bank Moc Toe Loafers', JBP + 'jos-a-bank-moc-toe-loafers', 119.5, 'Jos. A. Bank Moc Toe Loafers', JBP + 'jos-a-bank-moc-toe-loafers', 'single', JB + '/c/shoes/jos-a-bank-shoes',
                'the only own-label loafer among 13 own shoes; stocked Johnston & Murphy, Cole Haan, Florsheim and others not counted')),
    own_doors_us=185, own_doors_world=NC, locator_url=NC,
    doors_basis='registered from the 10 Oct counts return (185 own doors + 1 outlet); not re-read, per instructions',
    tech_named_fabrics='COOLMOTION (Traveler COOLMOTION line); 37.5® Technology (polyester); TENCEL™ lyocell (jeans) — named in titles and Product Details across the full read', tech_owned_or_licensed='licensed: COOLMOTION (Traveler COOLMOTION line), 37.5® Technology polyester, TENCEL™ lyocell, named in titles and compositions',
    tech_share_of_range='TECHSHARE_JAB', tech_evidence_url=JBP + 'traveler-traditional-fit-short-sleeve-performance-polo', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no', named_mills='in titles only as origin of cloth ("Italian Wool"); no mill named', made_in_stated_share='2/653 own clothing products state "Made in"; "Imported" on about 549 (full catalogue)',
    heritage_claim=NC, process_documented='no', craft_url_1=JBP + 'reserve-tailored-fit-italian-wool-dress-pants', craft_url_2=NC, proposed_craft=1,
    craft_reasoning='Most products state composition and "Imported"; almost none state a country and no maker, mill or making story was found.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url=VIN(814037), vinted_brand_ids='814037 (listed as JoS. A. Bank)', grailed_url='https://www.grailed.com/designers/jos-a-bank',
    quote=NC, quote_who=NC, quote_source=NC, quote_url=NC, quote_date=NC, signature_product=NC, signature_product_url=NC,
    status='partial (large house: full catalogue counted, fibre shares from a 123-row category-stratified sample)',
    source=f'Chrome {D}: josbank.com search service byCategory (all-suits, all-sportcoats-blazers, all-shirts, all-casual-tops, mens-all-pants, all-sweaters-and-vests, mens-all-outerwear, all-shoes; 7,732 records), Product Details attribute, productview price check of every pick, /p/ URL check',
    note='Own label = Jos. A. Bank and its named lines; third-party brands sold on the store excluded (Johnston & Murphy, Cole Haan, Haggar, Wrangler, Weatherproof Vintage, Joseph Abboud, Hart Schaffner Marx, Dockers, Florsheim and others). 666 own live products (653 clothing + 13 shoes); boys, suit separates and clearance copies (_C) excluded. Composition stated on 555/653 (suit bundles carry none). Prices are list prices. The 1905 dress shirt\'s URL carries its part-number suffix (the bare title slug returns 404).')

# ------------------------------------------------------------------------------------------------ Katin
KT = 'https://katinusa.com'; KTP = KT + '/products/'
M['Katin'] = dict(
    site_domain='katinusa.com', store_used=KT + ' (Katin USA)', currency='USD', search_url=KT + '/search?q=', feed_currency_rate='1.0', sublines_included='OTG (Out There Gear), sold under Katin, counted',
    g=dict(
        tee=G(35, 'BARRA TEE (100% organic cotton)', KTP + 'barra-tee', 55, 'OTG FLOW TEE (compare-at 55; on sale 39)', KTP + 'otg-flow-tee', 'range', KT + '/collections/tees', 'many graphic tees at 35'),
        polo=G(49, 'SLUB POLO (compare-at 49; on sale 35)', KTP + 'slub-polo', 89, 'GREG LS RUGBY POLO', KTP + 'greg-ls-rugby-polo', 'range', KT + '/collections/knits', 'Ronan Polo 79'),
        dress_shirt=G(75, 'ALAN SHIRT (52% cotton, 48% linen)', KTP + 'alan-shirt', 99, 'SHILOH FLANNEL', KTP + 'shiloh-flannel', 'range', KT + '/collections/shirts',
                      'casual shirts; shirt jackets (119-129) sit with outerwear'),
        jeans=G(89, 'PATTERSON 99 BAGGY', KTP + 'patterson-99-baggy', 89, 'PATTERSON 99 BAGGY', KTP + 'patterson-99-baggy', 'single', KT + '/collections/denim', 'every denim pant lists at 89'),
        dress_pants=G(79, 'CLARK PANT', KTP + 'clark-pant', 89, 'WARD PANT', KTP + 'ward-pant', 'range', KT + '/collections/pants', 'Lounge Pant (65) left out as loungewear'),
        sweater=G(75, 'RIVERS SWEATER', KTP + 'rivers-sweater', 99, 'GALLANT CARDIGAN SWEATER', KTP + 'gallant-cardigan-sweater', 'range', KT + '/collections/sweaters', 'no crew separable at the high; no elevated fibre'),
        outerwear=G(99, 'OTG SHADOW JACKET', KTP + 'otg-shadow-jacket', 159, 'HARRIS CORDUROY JACKET', KTP + 'harris-corduroy-jacket', 'range', KT + '/collections/jackets', 'Sam Jacket and Yukon Jacket also 159'),
        shoes=NONE_(note='no footwear sold')),
    own_doors_us=NC, own_doors_world=NC, locator_url='NONE',
    doors_basis='NC (for ruling): the story page says Sato Hughes and her son Glenn "have since continued to run the original surf shop" (Surfside Kanvas by Katin) but the site gives no address, hours or store page',
    tech_named_fabrics='TENCEL™ lyocell (named in composition)', tech_owned_or_licensed='licensed: TENCEL lyocell; none owned', tech_share_of_range='TECHSHARE_KAT', tech_evidence_url=KTP + 'otg-flow-tee', proposed_tech=NC,
    owned_facility='history only: trunks were sewn "in the back room of the Surfside Kanvas by Katin store"; present-day making place not stated', named_makers='no (seamstress Sato Hughes named in the history)', named_mills='no',
    made_in_stated_share='NC: no country on the product pages checked (Waterman Trunk, Harris Corduroy Jacket); product bodies carry none',
    heritage_claim='dated and placed: "In the summer of 1954, Nancy and Walter Katin opened a small boat cover business in the quaint beach town of Surfside, California" (/pages/the-katin-story)',
    process_documented='no (history of the first trunk, 1957, for Corky Carroll; no present-day process)', craft_url_1=KT + '/pages/the-katin-story', craft_url_2=KTP + 'waterman-trunk', proposed_craft=1,
    craft_reasoning='Composition is stated on almost every style and the story page tells the 1954 founding, but no current maker, mill or country is given.',
    founded_year=1954, founded_place='Surfside, California', founders='Nancy and Walter Katin', owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url=VIN(589720), vinted_brand_ids='589720', grailed_url='https://www.grailed.com/designers/katin',
    quote='In the summer of 1954, Nancy and Walter Katin opened a small boat cover business in the quaint beach town of Surfside, California.', quote_who='the house, Katin story page',
    quote_source='katinusa.com /pages/the-katin-story', quote_url=KT + '/pages/the-katin-story', quote_date='undated page (read 2026-10-12)',
    signature_product='Waterman Trunk ("traces back to the original surf trunk sewn by Walter Katin in the 1950s")', signature_product_url=KTP + 'waterman-trunk', status='partial',
    source=f'Chrome {D}: katinusa.com products.json (328; 326 available), product bodies, /pages/the-katin-story, .js price spot-check',
    note='Style = SKU stem (KTNGSBAR): men\'s clothing 181 listings -> 178 styles; boys, hats, bags, towels and gift cards excluded. No collaborations found. Trunks and volleys counted as swim. A few markdowns: regular = compare-at. No stockist page and no store page.')

# ------------------------------------------------------------------------------------------------ Kiel James Patrick
KJ = 'https://kieljamespatrick.com'; KJP_ = KJ + '/products/'
M['Kiel James Patrick'] = dict(
    site_domain='kieljamespatrick.com', store_used=KJ, currency='USD', search_url=KJ + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(40, 'Kennedy for President Graphic T-Shirt', KJP_ + 'kennedy-for-president-tee-shirt', 58, 'America 250th Celebration Graphic T-Shirt (compare-at 58; on sale 28; Made in USA)', KJP_ + 'america-250-celebration-tee',
              'range', KJ + '/collections/mens-tshirts', 'other 250th tees also 58'),
        polo=G(72, 'American Yacht Polo in Olive', KJP_ + 'american-yacht-polo-in-olive', 72, 'American Yacht Polo in Olive', KJP_ + 'american-yacht-polo-in-olive', 'single', KJ + '/collections/mens-polos-2020', 'all polos list at 72'),
        dress_shirt=G(88, 'Essex Patchwork Madras Shirt', KJP_ + 'essex-patchwork-madras-shirt', 148, 'Rangeley Trail Plaid Shirt Jacket (50% wool, 50% polyester)', KJP_ + 'rangeley-trail-plaid-shirt-jacket', 'range', KJ + '/collections/mens-collection',
                      'casual shirts; the Rangeley is sold in Men\'s Shirts, so a shirt (ruling: a jacket sold as a shirt is a shirt)'),
        jeans=NONE_(note='no jeans sold'),
        dress_pants=G(98, 'American Flag Corduroy Pants (compare-at 98; on sale 73.50)', KJP_ + 'american-flag-mens-corduroy-pants', 118, 'Newport Chino Pants in Oatmeal (compare-at 118; on sale 88.50)', KJP_ + 'newport-chino-pants-in-oatmeal',
                      'range', KJ + '/collections/mens-pants', 'cords and chinos stand in'),
        sweater=G(128, "Cozy Pumpkin Sweater - Men's", KJP_ + 'the-cozy-pumpkin-sweater-mens', 198, 'American Yacht Flag Sweater in Cream (100% cotton, Made in USA)', KJP_ + 'american-yacht-sweater-cream', 'range', KJ + '/collections/mens-collection',
                  'sweaters; Bristol Cable Knit (65% merino, 188) not superfine-stated, so not elevated'),
        outerwear=G(168, "Old Salt Raincoat in Yellow - Men's", KJP_ + 'old-salt-raincoat-mens', 228, 'North Country Denim Chore Jacket', KJP_ + 'north-country-denim-chore-jacket', 'range', KJ + '/collections/mens-outerwear',
                    'KJP X F.L. Woods Mariner\'s Waxed Jacket (468) is a collaboration, excluded'),
        shoes=NONE_(note='no footwear sold')),
    own_doors_us=1, own_doors_world=1, locator_url=KJ + '/pages/about-us',
    doors_basis='about page: KJP Flagship Store, 3 Bowen\'s Wharf, Newport RI ("est 2017"); the Pawtucket office and factory is "not open to the public", not counted',
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=KJ + '/pages/about-us', proposed_tech=NC,
    owned_facility='yes, for jewellery: "To this day we continue to handcraft all our jewelry right here in the Ocean State"; office and factory at 925 Central Ave, Pawtucket RI (clothing making place not stated)',
    named_makers='own Pawtucket factory (jewellery)', named_mills='no', made_in_stated_share='MADEIN_KJP',
    heritage_claim='placed, undated: "Inspired by the rugged charm of New England"; flagship "est 2017"', process_documented='no',
    craft_url_1=KJ + '/pages/about-us', craft_url_2=KJP_ + 'american-yacht-sweater-cream', proposed_craft=2,
    craft_reasoning='Product pages state composition and "Imported" or "Made in USA"; the house says it hand-makes its jewellery in its own Rhode Island factory, but says nothing about who makes the clothing.',
    founded_year=NC, founded_place=NC, founders='Kiel and Sarah Patrick ("the brand\'s founders", /pages/about-us)', owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='https://www.grailed.com/designers/kiel-james-patrick',
    quote='Inspired by the rugged charm of New England, Kiel James Patrick takes pride in creating timeless locally designed fashion and accessory pieces.', quote_who='the house, about page',
    quote_source='kieljamespatrick.com /pages/about-us', quote_url=KJ + '/pages/about-us', quote_date='undated page (read 2026-10-12)', signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: kieljamespatrick.com products.json (1420; 1125 available), product bodies ("Product Details"), /pages/about-us, flagship page, .js price spot-check',
    note='Style = title minus " in <Colour>": men\'s and unisex clothing 254 listings -> 216 keys; excluded vintage resale (14, e.g. Belstaff, Brooks Brothers), collaborations (Jeep x KJP, Goslings x KJP, KJP X F.L. Woods) and one third-party-named piece (Aperol) -> 190 styles. Pajamas excluded. Markdowns: regular = compare-at. Vinted has no brand entry.')

TECH = {'Gap': r'GapFlex|CashSoft|TENCEL|Lenzing|LYCRA|REPREVE|ECOVERO', 'Imogene + Willie': r'supima|TENCEL', 'Jos. A. Bank': r'COOLMOTION|37\.5|TENCEL',
        'Katin': r'TENCEL|LYCRA|REPREVE|supima', 'Goldwin': r'GORE-TEX|WINDSTOPPER|PERTEX|POLARTEC|CORDURA|SOLOTEX|THERMOFRAME|CLEANDOWN|Polygiene|KODENSHI'}
