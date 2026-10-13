D = '2026-10-11'
NC = 'NC'

def G(low, lp, lu, high, hp, hu, basis, listing, note=''):
    return dict(low=low, low_product=lp, low_url=lu, high=high, high_product=hp, high_url=hu, basis=basis, mens_listing_url=listing, _note=note)

def NONE_(listing='NONE', note=''):
    return dict(low='NONE', low_product='NONE', low_url='NONE', high='NONE', high_product='NONE', high_url='NONE', basis='NONE', mens_listing_url=listing, _note=note)

def NCG(listing='NC', note=''):
    return dict(low=NC, low_product=NC, low_url=NC, high=NC, high_product=NC, high_url=NC, basis=NC, mens_listing_url=listing, _note=note)

ES = 'https://eastsidegolf.com'; ESP = ES + '/products/'
EG = 'https://www.edwardgreen.com'
EK = 'https://evankinori.com'; EKP = EK + '/products/'
EX = 'https://www.express.com'; EXM = EX + '/clothing/men/'
HB = 'https://huckberry.com'; FTP = HB + '/store/flint-and-tinder/category/p/'
FN = 'https://freenotecloth.com'; FNP = FN + '/products/'
FR = 'https://www.thefryecompany.com'; FRP = FR + '/products/'
FU = 'https://fusalp.com/en-us'; FUP = FU + '/products/'
GS = 'https://www.g-star.com/en_us'; GSM = GS + '/shop/men/'
GD = 'https://gallerydept.com'; GDP = GD + '/products/'

COMMON = dict(b_corp=NC, b_corp_entity=NC, gots_certified=NC, gots_entity=NC, pronunciation=NC, read_date=D)
NO_STYLES = dict(styles_total=0, styles_with_composition=0, natural_pct=NC, synthetic_pct=NC, cellulosic_pct=NC, spandex_styles=0, shape=NC,
                 natural_categories='[]', synthetic_categories='[]', colourway_ratio='0/0', style_method='manual', swim_styles=0, swim_share_of_range=NC, mens_styles_excl_swim=0)
M = {}
NOLOOK = dict(lookbook_found=NC, lookbook_season_label=NC, lookbook_mens=NC, lookbook_url=NC)
NOBOOK = dict(lookbook_found='no', lookbook_season_label='NONE', lookbook_mens='NONE', lookbook_url='NONE')

# ------------------------------------------------------------------------------------------------ Eastside Golf
M['Eastside Golf'] = dict(
    site_domain='eastsidegolf.com', store_used=ES, currency='USD', search_url=ES + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(45, 'Core SS T-Shirt', ESP + 'ec2050301-435-electric-blue-core-ss-t-shirt', 70, 'Ace Tee', ESP + 'egmf2014-blk-black-ace-tee', 'range', ES + '/collections/golf-t-shirts',
              'Sequence Tee (EGMF2012) also 70; regular = compare-at where marked down'),
        polo=G(68, 'Signature Polo', ESP + 'eo2040201-435-electric-blue-signature-polo', 98, 'Multi-Color Scenic Pique Polo', ESP + 'el2040861-961-multi-color-scenic-pique-polo', 'range', ES + '/collections/mens-polos', 'the Breaker Polo (132; Camo 115) is a woven polyester wind shirt with a bungee hem (image files name it BreakerPoloWindShirt), not taken as a polo; Camo Snap Placket Polo also 98'),
        dress_shirt=G(78, 'Boxford Shirt (100% cotton; compare-at 78, on sale 29)', ESP + 'el2080101-100-bright-white-boxford-shirt', 118, 'Cabana Shirt (100% TENCEL; compare-at 118, on sale 44)', ESP + 'el2030809-100-white-black-cabana-shirt',
                      'range', ES + '/collections/button-ups', 'casual button-ups only (the house types them T-Shirts); Corduroy Shirt also 118'),
        jeans=NONE_(),
        dress_pants=G(98, 'Pro Series Pant', ESP + 'ep2090701-414-navy-pro-series-pant', 168, 'Range Pant', ESP + 'el2091159-317-prime-green-midnight-navy-range-pant', 'range', ES + '/collections/golf-pants',
                      'golf trousers stand in; track and rain pants left out'),
        sweater=G(115, 'Links Sweater, navy (compare-at 115; on sale 46; the prime green colour is 128)', ESP + 'ep2060301-414-navy-links-sweater', 155, 'Camo Crew Sweater', ESP + 'egmf1022-taupe-taupe-camo-crew-sweater', 'range', ES + '/collections/mens-collection',
                  'sweaters type (crew not separable for every title); Signature Cardigan Sweater also 155; no elevated fibre (wool at most 10%)'),
        outerwear=G(78, 'Club Vest', ESP + 'el2060401-044-opal-grey-club-vest', 498, 'Lambskin Stadium Jacket', ESP + 'egmh9007-nvy-midnight-navy-lamb-skin-stadium-jacket', 'range', ES + '/collections/mens-jackets',
                    'filed as range: lambskin is leather, not on the elevated list; dearest textile jacket is the Black Sideliner Jacket (198)'),
        shoes=NONE_(listing=ES + '/collections/golf-shoes', note='every shoe on the store is stocked Nike/Jordan golf product or a Nike x Eastside Golf collaboration (Victory Tour 4, Air Max Plus G): no own-label shoe')),
    own_doors_us=0, own_doors_world=0, locator_url=ES + '/pages/store-locator',
    doors_basis='no Eastside Golf store: the store-locator page (stockist.co widget u22909) lists golf clubs, pro shops and boutiques only; two "Corporate" office rows (Indianapolis, Cincinnati) dropped',
    tech_named_fabrics='TECH_ES', tech_owned_or_licensed='licensed: TENCEL™ (Lenzing lyocell) named in composition', tech_share_of_range='TECHSHARE_ES', tech_evidence_url=ESP + 'el2030809-100-white-black-cabana-shirt', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no', named_mills='no', made_in_stated_share='MADEIN_ES',
    heritage_claim='dated, not placed: "Eastside Golf was founded June 1st, 2019 by Olajuwon Ajanaku" (/pages/about-us)', process_documented='no',
    craft_url_1=ES + '/pages/about-us', craft_url_2=ESP + 'ec2050301-435-electric-blue-core-ss-t-shirt', proposed_craft=1,
    craft_reasoning='Product pages give composition on most styles but no country, maker or mill (three pages checked for "Made in" or "Imported": neither appears). The about page is a mission statement, not a making story.',
    founded_year=2019, founded_place=NC, founders='Olajuwon Ajanaku (founder); Earl A. Cooper, PGA Professional (co-founder)', owner_today=NC, ownership_url=NC,
    **NOBOOK,
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='NONE',
    quote='Eastside Golf is a lifestyle golf brand developed to raise awareness about golf among youth and non golfers.', quote_who='the house, about page', quote_source='eastsidegolf.com /pages/about-us',
    quote_url=ES + '/pages/about-us', quote_date='undated page (read 2026-10-11)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: eastsidegolf.com products.json (506; 384 available), clothing body_html compositions, /pages/store-locator (stockist.co u22909 locations/all, 214 rows), /pages/about-us, collections.json, search check',
    note='Style = SKU stem (EC2050301): 241 available clothing listings / 118 styles. Nike and Jordan product (vendor Nike, or vendor Eastside Golf on Nike shoes) excluded as stocked third-party. Women\'s pieces sit in separate collections with other product types and none fall in the counted types. Markdown house: regular = compare-at; many products also carry a "30% Off" badge tag (TeeUp30%Off) with no compare-at, read as a promotion applied at checkout, so the listed price is filed as regular. Vinted has no brand entry; Grailed has no designer page.')

# ------------------------------------------------------------------------------------------------ Edward Green
EGS = EG + '/shop/shoes/'
M['Edward Green'] = dict(
    site_domain='edwardgreen.com', store_used=EG + '/shop (Magento, US session showing USD)', currency='USD_landed', search_url=EG + '/shop/catalogsearch/result/?q=', feed_currency_rate='not shopify', sublines_included='-',
    g=dict(tee=NONE_(), polo=NONE_(), dress_shirt=NONE_(), jeans=NONE_(), dress_pants=NONE_(), sweater=NONE_(), outerwear=NONE_(),
           shoes=G(915, 'Polperro, 389 Last, espresso baby calf suede', EGS + 'polperro-espresso-baby-calf-suede-brown-389-last.html', 2925, 'Greenwich Unlined, 184 Last, Horween shell cordovan',
                   EGS + 'greenwich-unlined-horween-cordovan-tan-184-last.html', 'pair', EG + '/shop/shoes.html?product_list_limit=all',
                   'loafers; prices "US Duty Paid" (DHL), so USD_landed; Piccadilly Unlined cordovan also 2925; calf Piccadilly 1750; dearest shoe overall Galway boot 3295; no markdowns')),
    own_doors_us=0, own_doors_world=2, locator_url=EG + '/store/jermyn-st',
    doors_basis="brand's own store pages: 75 Jermyn Street, London, and 199 bis Boulevard St. Germain, Paris (\"our own shops in London and Paris\", /about); no US shop",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=EG + '/about', proposed_tech=NC,
    owned_facility='yes, stated: "We\'re still based in Northampton and have over sixty skilled artisans making around 350 pairs of shoes a week"; workshop established in Northampton in 1890 (/about)',
    named_makers='own workshop (Northampton)', named_mills='tannery named: Horween (shell cordovan) on product pages; calf "the finest French and Italian calf" without a tannery name',
    made_in_stated_share='NC', heritage_claim='dated and placed: "He established his own workshop in Northampton in 1890" (/about)',
    process_documented='partial: Goodyear welting, oak-bark-tanned soles ("tanned for nine months"), hand-sewn Dover "with a boar\'s bristle needle" (/about)',
    craft_url_1=EG + '/about', craft_url_2=EGS + 'greenwich-unlined-horween-cordovan-tan-184-last.html', proposed_craft=4,
    craft_reasoning='Edward Green states its own Northampton workshop, its headcount and weekly output, names Horween for cordovan and describes welting, sole tanning and hand-sewing. The workshop is described rather than shown, and the calf tanneries are unnamed, so 4 not 5.',
    founded_year=1890, founded_place='Northampton', founders='Edward Green', owner_today=NC, ownership_url=NC,
    **NOBOOK,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=555011&catalog[]=5', vinted_brand_ids='555011', grailed_url='https://www.grailed.com/designers/edward-green',
    quote='Excellence without compromise', quote_who="Edward Green's promise, as the about page gives it", quote_source='edwardgreen.com /about',
    quote_url=EG + '/about', quote_date='undated page (read 2026-10-11)',
    signature_product='Dover, 202 Last ("our signature handsewn derby")', signature_product_url=NC, status='partial',
    styles=NO_STYLES,
    source=f'Chrome {D}: edwardgreen.com/shop /shop/shoes.html?product_list_limit=all (158 listings), loafer PDPs, /about, /store/jermyn-st, /store/boulevard-st-germain, /stockists, journal, search check',
    note='Shoe-only house: seven garment slots NONE and no clothing style table (no clothing sold; accessories are belts, cardholders and care). Founder: the about page tells the story of Edward Green founding the workshop. Owner today not stated on the site. Made-in share NC: product pages were read for price and leather, not country.')

# ------------------------------------------------------------------------------------------------ Evan Kinori
M['Evan Kinori'] = dict(
    site_domain='evankinori.com', store_used=EK, currency='USD', search_url=NC, feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(115, 'Pocket Tee (55% hemp / 45% organic cotton)', EKP + 'pocket-tee-earth', 165, 'Long Sleeve Tee', EKP + 'long-sleeve-tee-taupe-natural', 'range', EK + '/collections/all', 'made in California; no men-only listing (the house makes menswear only)'),
        polo=NONE_(),
        dress_shirt=G(425, 'Band Collar Shirt - Organic Cotton/Hemp Twill', EKP + 'band-collar-shirt-organic-cotton-hemp-twill-anthracite', 1095, 'Big Shirt - Fox British Wool Twill', EKP + 'big-shirt-fox-wool-british-twill',
                      'range', EK + '/collections/all', 'casual shirts only; high is a wool shirt (wool is not on the elevated list unless superfine)'),
        jeans=NONE_(note='the only jean in stock is orSlow (third-party label): not counted'),
        dress_pants=G(445, 'Four Pocket Pant (tumbled hemp canvas)', EKP + 'four-pocket-pant-tumbled-hemp-canvas', 1245, 'Two Pleat Pant - Cashmere/Linen Twill', EKP + 'two-pleat-pant-cashmere-linen-twill-black',
                      'pair', EK + '/collections/all', 'Single Pleat Pant also 445; high is a cashmere-linen pleated trouser (fibre share not stated on the page, so not claimed as majority cashmere)'),
        sweater=G(495, 'Big Sweater - Yak Wool (knitted in Kathmandu)', EKP + 'big-sweater-yak-wool-1', 845, 'Crewneck Cardigan - Wool/Cashmere Tweed', EKP + 'crewneck-cardigan-wool-cashmere-tweed-black',
                  'range', EK + '/collections/all', 'knitwear; no crew pullover separable by title; Crewneck Cardigan - Cashmere/Lambswool 745'),
        outerwear=G(445, 'Pleated Jacket (Bedford cord)', EKP + 'pleated-jacket-bedford-cord', 2195, 'Big Coat - Brushed Wool/Cashmere Check', EKP + 'big-coat-brushed-cashmere-wool-check-navy-grey',
                    'range', EK + '/collections/all', 'Three Button Jacket tailoring (1395-1895) kept out; fibre shares on the coat not stated'),
        shoes=NONE_(note='no footwear in stock')),
    own_doors_us=1, own_doors_world=1, locator_url=EK + '/pages/visit',
    doors_basis="brand's visit page: San Francisco store, 1367 Valencia Street (Mission District), opened December 2021, joined to the studio",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=EK + '/pages/visit', proposed_tech=NC,
    owned_facility='partial: the San Francisco studio sits behind the store ("connected to the studio space ... where ideas take shape", /pages/visit); California-made pieces do not name the workroom',
    named_makers='no factory named; knitwear process named ("Made in the cottage industry style around the village of Lucca, Italy")',
    named_mills='yes, in titles: Fox (Fox Brothers flannels, twill, tweed and worsted), Casentino wool, Irish wool; washi',
    made_in_stated_share='MADEIN_EK', heritage_claim='none on site: no founding year or founder statement; store opened December 2021 (/pages/visit)',
    process_documented='partial: knitwear "panels are knitted and brought to different homes where they are linked together" (product pages)',
    craft_url_1=EKP + 'crewneck-cardigan-cashmere-lambswool-black-1', craft_url_2=EK + '/pages/visit', proposed_craft=3,
    craft_reasoning='Every style states where it is made (Japan, California, UK, Italy, Kathmandu), titles name the cloth mills (Fox, Casentino) and the knitwear page describes how the pieces are linked by hand. No factory is named and no owned workroom is shown.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    **NOBOOK,
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='https://www.grailed.com/designers/evan-kinori',
    quote='It is uniquely connected to the studio space, which is located in the back half of the building, where ideas take shape.', quote_who='the house, visit page', quote_source='evankinori.com /pages/visit',
    quote_url=EK + '/pages/visit', quote_date='undated page (read 2026-10-11)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: evankinori.com products.json (456; 419 available), body_html (composition, made-in), /pages/visit, /pages/about (stockists), nav',
    note='Style = model + fabric (colour after the last comma dropped): 354 available clothing listings / 320 styles after dropping the orSlow jean (third-party) and the MAN-TLE down jacket (collaboration). About a third of styles state percentages; the rest name the fibre in the title (counted as composition without a share). Objects (furniture, ceramics), accessories and gift card excluded. Mark: evan kinori (lower case on site). No markdowns. Vinted has no brand entry.')

# ------------------------------------------------------------------------------------------------ Express
M['Express'] = dict(
    site_domain='express.com', store_used=EX + ' (custom React storefront; read through the site\'s own Apollo GraphQL client)', currency='USD', search_url=EX + '/exp/search?q=', feed_currency_rate='not shopify',
    sublines_included='1MX (shirt line sold under Express, counted)',
    g=dict(
        tee=G(28, 'Slim Supersoft Moisture-Wicking Crew Neck T-Shirt', EXM + 'slim-supersoft-moisture-wicking-crew-neck-t-shirt/pro/05051953', 74, 'Relaxed Fit Johnny Collar Long Sleeve T-Shirt', EX + '/clothing/men/relaxed-fit-johnny-collar-long-sleeve-t-shirt/pro/05731048',
              'range', 'NC', 'list prices; nearly everything is on promotion'),
        polo=G(44, 'Mini Emblem Logo Cotton Pique Polo', EXM + 'mini-emblem-logo-cotton-pique-polo/pro/05040958', 88, "The '01 Rugby Stripe Polo", EXM + 'the-01-rugby-stripe-polo/pro/05041162', 'range', EX + '/exp/search?q=polo', 'no polo category URL captured; site search for polo (232 products) given as the listing'),
        dress_shirt=G(68, 'Extra Slim Solid Cotton Stretch 1MX Dress Shirt', EXM + 'extra-slim-solid-cotton-stretch-1mx-dress-shirt/pro/00305332', 78, 'Slim Solid Stretch Modern Tech 1MX Dress Shirt',
                      EXM + 'slim-solid-stretch-modern-tech-1mx-dress-shirt/pro/06039140', 'range', 'NC', 'long-sleeve dress shirts; short-sleeve 1MX (58) excluded'),
        jeans=G(88, 'Straight Dark Wash Jeans', EXM + 'straight-dark-wash-jeans/pro/27508551', 98, "The '96 Bootcut Jean", EXM + 'the-96-bootcut-jean/pro/28410059', 'range', 'NC', ''),
        dress_pants=G(88, 'Slim Heather Belted Pant', EXM + 'slim-heather-belted-pant/pro/03040023', 148, 'Slim Black Performance Stretch Wool-Blend Tuxedo Pant',
                      EXM + 'slim-black-performance-stretch-wool-blend-tuxedo-pant/pro/03253847', 'range', 'NC', ''),
        sweater=G(68, 'Crew Neck Cotton-Cashmere Sweater (95% cotton, 5% cashmere)', EXM + 'crew-neck-cotton-cashmere-sweater/pro/01770093', 98, 'Oversized Cable Knit Crew Neck Sweater',
                  EXM + 'oversized-cable-knit-crew-neck-sweater/pro/01777219', 'range', 'NC', 'crew necks; no elevated-fibre crew (the merino blend is 45% merino, 88)'),
        outerwear=G(128, 'Denim Medium Wash Trucker Jacket', EXM + 'denim-medium-wash-trucker-jacket/pro/06210029', 298, 'Houndstooth Wool-Blend Carcoat', EXM + 'houndstooth-wool-blend-carcoat/pro/04125691',
                    'range', 'NC', 'Black Wool-Blend Topcoat also 298; Black Nylon Quilted Vest 88 is a vest'),
        shoes=NONE_(note='no footwear: site search "loafers" returns 0 products and none of the 69 men\'s nav categories is shoes')),
    own_doors_us=226, own_doors_world=NC, locator_url='https://stores.express.com',
    doors_basis='stores.express.com Yext directory: state counts sum to 226 and all 226 store pages were read (one, Town Center at Boca Raton, is an Express Women store: counted, flagged womens-only); Express Factory Outlet runs a separate directory (stores.expressfactoryoutlet.com, 160 stores in 38 states) counted as outlets, not own doors and not rowed; world NC (international not checked)',
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=EXM + 'slim-solid-stretch-modern-tech-1mx-dress-shirt/pro/06039140', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no', named_mills='no',
    made_in_stated_share='no country stated: 415 of 426 men\'s products say "Imported" (fabricCare read for the full catalogue); none names a country',
    heritage_claim=NC, process_documented='no',
    craft_url_1=EXM + 'crew-neck-cotton-cashmere-sweater/pro/01770093', craft_url_2='https://stores.express.com', proposed_craft=1,
    craft_reasoning='Product records give composition on 81% of the men\'s range and the word "Imported", with no country, maker or mill. Nothing about the making can be checked.',
    founded_year=NC, founded_place=NC, founders=NC,
    owner_today='Phoenix, the operating platform formed by WHP Global with Simon and Brookfield (bought Express out of Chapter 11; court approval 17 June 2024; press)',
    ownership_url='https://www.retaildive.com/news/express-bonobos-acquired-bankruptcy-simon-brookfield-centennial-whp-global/719103/',
    **NOLOOK,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=8515&catalog[]=5', vinted_brand_ids='8515', grailed_url='https://www.grailed.com/designers/express',
    quote=NC, quote_who=NC, quote_source=NC, quote_url=NC, quote_date=NC,
    signature_product=NC, signature_product_url=NC, status='partial (large house: style table is a category-stratified sample)',
    source=f'Chrome {D}: express.com Apollo CategoryQuery over 22 men\'s categories (426 unique products, 1,971 colour tiles), PantseractProduct.fabricCare for all 426, PDP prices, site search, stores.express.com (226 store pages), stores.expressfactoryoutlet.com state counts',
    note='LARGE HOUSE (stratified sample): styles_total, styles_with_composition and colourway_ratio are full-catalogue counts (426 products read, one women\'s Halter Cutaway Blazer Vest that leaked into blazers-vests dropped = 425; the 1,971 colour tiles were counted before that drop); natural/synthetic/cellulosic shares, spandex count, shape and categories come from the 139-row sample (every k-th product per category, up to 12 per category), which is not proportional to category size. "G"-suffix product ids are clearance copies and were not counted as styles. Ownership from press; the site was not read for founding or owner.')

# ------------------------------------------------------------------------------------------------ Flint and Tinder
M['Flint and Tinder'] = dict(
    site_domain='huckberry.com (Flint and Tinder is Huckberry\'s house label; no own site)', store_used=HB + '/store/flint-and-tinder', currency='USD', search_url=NC, feed_currency_rate='not shopify',
    sublines_included='365 Collection; All-American (USA-made denim) — both sold as Flint and Tinder, counted',
    g=dict(
        tee=G(38, 'Slub Pocket T-Shirt', FTP + '95306-short-sleeve-slub-pocket-t-shirt', 108, 'Striped Yarn Dyed Longsleeve T-Shirt', FTP + '99924-striped-yarn-dyed-longsleeve-t-shirt', 'range', HB + '/store/flint-and-tinder', ''),
        polo=G(88, 'Pique Polo Shirt', FTP + '96008-pique-polo', 118, 'Bolinas Johnny Collar Sweater Polo', FTP + '88617-bolinas-johnny-collar-sweater-polo', 'range', HB + '/store/flint-and-tinder', ''),
        dress_shirt=G(98, 'Oxford Draftsman Shirt', FTP + '99152-oxford-draftsman-shirt', 158, 'Bone Button Western Shirt (made in USA)', FTP + '92555-bone-button-western-shirt-2-0', 'range', HB + '/store/flint-and-tinder',
                      'casual shirts only; Cash Diamond Snap Western Shirt (collaboration) excluded'),
        jeans=G(128, 'Stretch Selvedge Denim - HB Straight', FTP + '99164-stretch-selvedge-denim-hb-straight', 178, 'Japanese Stretch Selvedge Denim - HB Straight', FTP + '99253-japanese-stretch-selvedge-denim-hb-straight', 'range', HB + '/store/flint-and-tinder', ''),
        dress_pants=G(108, '365 Chino Pant - HB Straight', FTP + '99584-365-chino-pant-hb-straight', 128, 'Brushed Sateen Fatigue Pant', FTP + '1001044-flannel-sateen-fatigue-pant', 'range', HB + '/store/flint-and-tinder', 'chinos stand in'),
        sweater=G(108, 'Bolinas Crewneck Sweater', FTP + '99220-bolinas-crewneck-sweater', 128, 'Fine Merino Crewneck Sweater (100% extrafine merino)', FTP + '99763-fine-merino-sweater-crewneck', 'pair', HB + '/store/flint-and-tinder',
                  'entry crew vs extrafine-merino crew (named judgement: extrafine merino taken as superfine wool); dearest crew is the Washed Cotton Cableknit (148)'),
        outerwear=G(188, 'Classic Chore Coat', FTP + '99538-classic-chore-coat', 698, 'Bandit Leather Jacket', FTP + '92701-collard-leather-jacket', 'range', HB + '/store/flint-and-tinder', 'leather is not on the elevated list'),
        shoes=NONE_(note='both shoes are collaborations (Flint and Tinder x Rancourt & Co. Beef Roll Penny Loafer 334; Waxy Kudu Roper Boot by Rios of Mercedes 748): NONE under the 11 Oct ruling')),
    own_doors_us=0, own_doors_world=0, locator_url=HB + '/explore/stores',
    doors_basis='ruled 10 Oct: no Flint and Tinder door; the three Huckberry stores (San Francisco, Washington DC, Chicago) are stockist rows (other brand own door)',
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=FTP + '99538-classic-chore-coat', proposed_tech=NC,
    owned_facility='no claim', named_makers='no factory named; USA-made pieces (waxed truckers, All-American denim, heavyweight tees, boxer briefs, Bone Button Western) say where, not who',
    named_mills='yes: Halley Stevensons (waxed cotton), British Millerain, deadstock Cone Mills denim (American Reserve Type II jacket) named in descriptions',
    made_in_stated_share='MADEIN_FT', heritage_claim='none: Huckberry\'s house label; brand copy speaks of "archival designs" without a date or place', process_documented='no',
    craft_url_1=FTP + '99538-classic-chore-coat', craft_url_2=HB + '/store/flint-and-tinder', proposed_craft=2,
    craft_reasoning='Every style states a country of origin and several descriptions name the cloth mill (Halley Stevensons, British Millerain, Cone Mills). No factory is named and there is no making story beyond the brand line, so 2.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today='Huckberry (house label; the brand page sits in the Huckberry store)', ownership_url=HB + '/store/flint-and-tinder',
    **NOLOOK,
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='https://www.grailed.com/designers/flint-and-tinder',
    quote='Flint and Tinder reworks archival designs for today.', quote_who='the house, Huckberry brand page', quote_source='huckberry.com /store/flint-and-tinder',
    quote_url=HB + '/store/flint-and-tinder', quote_date='undated page (read 2026-10-11)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: Huckberry /api/pages/tiles for the Flint and Tinder brand page (in_stock, 3 pages: 309 colour listings), payload compare_at_price, country_of_origin and description; product pages for picks; huckberry.com/explore/stores (facts-first 8 Oct)',
    note='Style = Huckberry product_group_id: 283 in-stock clothing colour listings / 126 styles; accessories, hats, belts and gloves excluded; the Cash Diamond Snap Western Shirt (collaboration) excluded. Composition is read from description text (tiles write "98% brushed cotton twill" and the like, so some sums fall short of 100). Markdowns: regular = compare-at. Vinted has no brand entry.')

# ------------------------------------------------------------------------------------------------ Freenote Cloth
M['Freenote Cloth'] = dict(
    site_domain='freenotecloth.com', store_used=FN, currency='USD', search_url=FN + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(65, '9 Ounce Pocketless T-Shirt Midnight', FNP + '9-ounce-pocketless-t-shirt-midnight', 125, 'Shifter L/S Tee', FNP + 'shifter-l-s-tee-black-combo', 'range', FN + '/collections/all', '13oz pocket tees 80-90; the Fairmont S/S Henley is 130'),
        polo=NONE_(),
        dress_shirt=G(220, 'Dayton Chambray', FNP + 'dayton-chambray', 360, 'Sinclair Ivory', FNP + 'sinclair-ivory', 'range', FN + '/collections/all', 'work and western shirts; no dress shirt'),
        jeans=G(285, 'Belford Straight 14.50 Ounce Kaihara Denim', FNP + 'belford-straight-14-50-ounce-kaihara-denim', 325, 'Modesto 14.50 Ounce Indigo Unsanforized Denim', FNP + 'modesto-14-50-ounce-indigo-unsanforized-denim',
                'range', FN + '/collections/all', 'each cut runs 285-325 by denim (Kaihara and ecru 285, brown and heavy denims 305, rinsed 325); the Modesto Buckleback (350) is natural canvas, not denim, so not the high'),
        dress_pants=G(280, 'Workers Chino Slim Fit Khaki', FNP + 'workers-chino-slim-fit-khaki', 350, 'Duster Pant Brown Wool (100% wool)', FNP + 'duster-pant-brown-wool',
                      'range', FN + '/collections/all', 'chinos and work trousers stand in; Benton Hunting Pant also 350'),
        sweater=NONE_(note='no knit sweater; the Deck Sweatshirt (150) is a sweatshirt'),
        outerwear=G(350, 'Grafton Jacket Black', FNP + 'grafton-jacket-black', 2400, 'Grafton Jacket Tan Horsehide', FNP + 'grafton-jacket-tan-horsehide', 'pair', FN + '/collections/all',
                    'same Grafton model in cloth and in horsehide (horsehide is not exotic: ruled); Mooch Moto steerhide and Locklin horsehide also reach 2400'),
        shoes=NONE_(note='footwear on the store is third-party (Viberg, John Lofgren, Red Wing, White\'s, Nicks, Fenoglio), even where the vendor field says Freenote Cloth: no own-label shoe')),
    own_doors_us=2, own_doors_world=2, locator_url=FN + '/pages/locations',
    doors_basis="brand's locations page: Los Angeles (5509 N. Figueroa St, open daily) and San Juan Capistrano (32122 Camino Capistrano, Mon-Fri 9-5, weekends 9-4: office-style hours, flagged); both carry the Freenote name",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=FN + '/pages/our-story', proposed_tech=NC,
    owned_facility='claim, not shown: "We engage in every step of the manufacturing process ... All product is cut sewn and finished in California" (/pages/our-story)',
    named_makers='no factory named (own making claimed)', named_mills='partly: Kaihara named on one denim; other denims "Japanese selvedge" without a mill; SB Tanning Co named for the leather patch',
    made_in_stated_share='MADEIN_FN', heritage_claim='placed, not dated: "Freenote creates quality menswear manufactured in the United States" (/pages/our-story)',
    process_documented='partial: chain-stitch hemming on a Union Special 43200g in store (/pages/locations); cut, sew and finish in California stated',
    craft_url_1=FN + '/pages/our-story', craft_url_2=FNP + 'modesto-14-50-ounce-indigo-unsanforized-denim', proposed_craft=3,
    craft_reasoning='114 of 116 styles say "Sewn in USA" and the brand claims every step of making in California, with one mill (Kaihara) and the patch tannery named. The workshop is claimed rather than shown or named, so 3.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url='NONE', vinted_brand_ids='NONE', grailed_url='https://www.grailed.com/designers/freenote-cloth',
    quote='Freenote creates quality menswear manufactured in the United States.', quote_who='the house, our story page', quote_source='freenotecloth.com /pages/our-story',
    quote_url=FN + '/pages/our-story', quote_date='undated page (read 2026-10-11)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: freenotecloth.com products.json (693; 558 available), body_html compositions, /pages/our-story, /pages/locations, stockist page (404), search check',
    note='Style = SKU stem (M0008015): 408 current-season listings / 116 styles. Excluded: Past Season (43, all marked down, final sale), Collaboration types (Golden Age Supply, Codina Leather, Bell & Oak, Bowman Hat, Tatton Baird and others), third-party footwear, gift cards. Leather jackets: body composition is the lining, so the main fabric is filed as the hide named in the title (steerhide, horsehide, goatskin, suede). 9 denim styles name the mill or origin but no fibre: ND. No markdowns on the current range. Vinted has no brand entry.')

# ------------------------------------------------------------------------------------------------ Frye
M['Frye'] = dict(
    site_domain='thefryecompany.com', store_used=FR, currency='USD', search_url=FR + '/search?q=', feed_currency_rate='1.0',
    sublines_included='Men\'s leather jackets by Moda Piel (licensee; sold under the FRYE name on the brand\'s store, counted as own label: for ruling)',
    g=dict(
        tee=NONE_(), polo=NONE_(), dress_shirt=NONE_(), jeans=NONE_(), dress_pants=NONE_(), sweater=NONE_(),
        outerwear=G(299, 'Desert Racer Jacket (Moda Piel for Frye)', FRP + 'desert-racer-jacket-tobacco', 645, 'Huck Racer Jacket, cognac/black (Moda Piel for Frye)', FRP + 'huck-racer-jacket-cognac-black', 'range', FR + '/collections/all',
                    'all men\'s clothing is leather and suede jackets; the Trailblazer Trucker shows one colour at 229 with no compare-at (not used); Jethro Flight Style Jacket also 645; the moka/tobacco Huck Racer is 599'),
        shoes=G(148, 'Beau Penny (compare-at 148; on sale 59.98-79.98)', FRP + 'beau-penny-black', 278, 'Chris Venetian (full price)', FRP + 'chris-venetian-black', 'range', FR + '/collections/all',
                'loafers (32 listings); men\'s new footwear runs 148-498; Frye Exchange resale (Trove, Recurate) excluded')),
    own_doors_us=0, own_doors_world=0, locator_url=NC,
    doors_basis='counts return (10 Oct): the store-locator page redirects to contact; no Frye store listed',
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=FR + '/pages/heritage', proposed_tech=NC,
    owned_facility='no present-day claim: heritage page tells the 1863 Marlboro shop and 1923 Goodyear welting, nothing on where shoes are made today', named_makers='licensee named as vendor for jackets (Moda Piel); shoe maker not named', named_mills='no',
    made_in_stated_share='NC', heritage_claim='dated and placed: "In March 1863, John A. Frye opened the doors of a small shop on Elm Street in Marlboro, Massachusetts." (/pages/heritage)',
    process_documented='no (history only: 1888 first Frye boot, 1923 Goodyear welt)',
    craft_url_1=FR + '/pages/heritage', craft_url_2=FRP + 'chris-venetian-black', proposed_craft=1,
    craft_reasoning='Frye dates and places its founding but says nothing about present-day making; the jackets are made by a licensee and no factory, tannery or country was found in what was read.',
    founded_year=1863, founded_place='Marlboro, Massachusetts', founders='John A. Frye', owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=2061&catalog[]=5', vinted_brand_ids='2061', grailed_url='https://www.grailed.com/designers/frye',
    quote='In March 1863, John A. Frye opened the doors of a small shop on Elm Street in Marlboro, Massachusetts.', quote_who='the house, heritage page', quote_source='thefryecompany.com /pages/heritage',
    quote_url=FR + '/pages/heritage', quote_date='undated page (read 2026-10-11)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: thefryecompany.com products.json (2213; 1870 available), vendor split, men\'s jackets and men\'s footwear, /pages/heritage, search check; doors from the 10 Oct counts return',
    note='Footwear-led house; the style table is the 34 men\'s leather jacket styles (51 listings) made by Moda Piel and sold under the FRYE name (counted as own label: brand name on the product; for ruling). Excluded: Frye Exchange resale (vendors Trove, Recurate), bags (Centric) and sunglasses (FGXI) as licensee accessories. Markdown house: regular = compare-at. Made-in share NC: jacket and shoe pages were read for price and material only.')

# ------------------------------------------------------------------------------------------------ Fusalp
M['Fusalp'] = dict(
    site_domain='fusalp.com', store_used=FU + ' (Shopify Markets, US market in USD)', currency='USD', search_url=NC, feed_currency_rate='1.14775 (Shopify.currency; feed prices equal the displayed USD)',
    sublines_included='-',
    g=dict(
        tee=G(230, 'Riviere Tee Shirt', FUP + 't-shirt-short-sleeve-men-riviere-iii-noir', 230, 'Riviere Tee Shirt', FUP + 't-shirt-short-sleeve-men-riviere-iii-noir', 'single', FU + '/collections/all',
              'only men\'s tee in stock; page shows 230 = feed'),
        polo=NONE_(), dress_shirt=NONE_(), jeans=NONE_(),
        dress_pants=G(390, 'Malaga Pants', FUP + 'malaga-pants-noir', 690, 'Gaston Pants (95% wool)', FUP + 'pantalon-gaston-noir', 'range', FU + '/collections/all',
                      'city trousers (ski pants excluded); Norean wool/cashmere 610'),
        sweater=G(440, 'Ceillac Sweater (70% viscose, 30% polyester)', FUP + 'sweater-ceillac-dark-blue', 690, 'Wengen Sweater (100% wool)', FUP + 'pull-wengen-grove', 'range', FU + '/collections/all',
                  'sweaters (crew not separable by title); Dolmiron mohair-blend (50% mohair) and others also 690'),
        outerwear=G(320, 'Mariozip Lightweight Jacket', FUP + 'veste-technique-mariozip-dark-blue-spicy', 2620, 'John Ski Jacket', FUP + 'veste-de-ski-john-edelweiss-neige-grey-sea', 'range', FU + '/collections/all',
                    'page shows 2620 as 3 x 873.33; Berlioz down 2270; Power Ski Jacket colours 909-1670 with no compare-at'),
        shoes=NONE_(note='no footwear sold')),
    own_doors_us=2, own_doors_world=40, locator_url='https://fusalpen.storeloc.unique.paris (store locator embedded on fusalp.com)',
    doors_basis='store locator category "Fusalp store", 53 entries: 40 own doors (US 2: Vail, Aspen), 5 outlets in outlet centres, 4 department-store counters (concessions, not counted; one women\'s), 4 Korean department-store pop-ups (store e-mails say pop-up; dates not given; for ruling); "Partner store" category (110) are stockists',
    tech_named_fabrics=NC, tech_owned_or_licensed=NC, tech_share_of_range=NC, tech_evidence_url=FUP + 'veste-de-ski-john-edelweiss-neige-grey-sea', proposed_tech=NC,
    owned_facility='no claim found in what was read', named_makers='no', named_mills='no', made_in_stated_share='MADEIN_FU',
    heritage_claim='dated and placed: "The Fusalp Maison was founded in 1952, on the shores of Annecy Lake, by two tailors, Georges Ribola and René Veyrat." (/pages/fusalp-story)', process_documented='no',
    craft_url_1=FU + '/pages/fusalp-story', craft_url_2=FUP + 'veste-de-ski-john-edelweiss-neige-grey-sea', proposed_craft=1,
    craft_reasoning='Fusalp dates and places its founding by two tailors, but product pages read give composition only; a country appears on a handful of styles through tags and no maker or mill is named.',
    founded_year=1952, founded_place='Annecy', founders='Georges Ribola and René Veyrat', owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=29329&catalog[]=5', vinted_brand_ids='29329', grailed_url='https://www.grailed.com/designers/fusalp',
    quote='The Fusalp Maison was founded in 1952, on the shores of Annecy Lake, by two tailors, Georges Ribola and René Veyrat.', quote_who='the house, story page', quote_source='fusalp.com /en-us/pages/fusalp-story',
    quote_url=FU + '/pages/fusalp-story', quote_date='undated page (read 2026-10-11)',
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: fusalp.com/en-us products.json (534; 409 available), men\'s PDPs (Composition and care), displayed prices on two products, Unique store locator (categories 1 and 2), /pages/fusalp-story',
    note='Style = article code (CODE_ART_COM): 150 men\'s listings / 82 styles; accessories excluded. Tech fabrics NC: PDP technical blocks were not read, only the composition line. Ski pants and ski jackets are in the style table as outerwear and trousers by house category.')

# ------------------------------------------------------------------------------------------------ G-Star
M['G-Star'] = dict(
    site_domain='g-star.com', store_used=GS + ' (Next.js storefront; catalogue read through the site\'s Algolia index)', currency='USD', search_url=GS + '/search?q=' , feed_currency_rate='not shopify',
    sublines_included='G-Star RAW Research (RR / GSRR) and E (premium) lines, sold under G-Star, counted',
    g=dict(
        tee=G(35, 'Slim Base T-Shirt', GSM + 't-shirts/d19070-c723-1260', 230, 'RR Graphic Longsleeve', GSM + 't-shirts/d30266-e401-b564', 'range', 'NC', 'full-price colours only; WVB tee (360) excluded as collaboration'),
        polo=G(55, 'Dunda Slim Polo', GSM + 't-shirts/d11595-5864-504', 130, 'Essential Polo', GSM + 'menpolos/d22783-d287-724', 'range', 'NC', ''),
        dress_shirt=G(110, 'Dressed Super Slim Shirt', GSM + 'shirts/d17026-c271-110', 690, 'RR Baked Shirt', GSM + 'shirts/d30272-e692-b230', 'range', 'NC', 'high is a RAW Research piece (sub-line counted; for ruling)'),
        jeans=G(130, '3301 Regular Tapered Jeans', GSM + 'jeans/51003-c922-c776', 590, 'Unisex GSRR Maxi Navy Jeans', GSM + 'jeans/d25431-d807-001', 'range', 'NC', 'Dakota Selvedge 490 is the dearest main-line jean'),
        dress_pants=G(120, 'Bronson Slim Chino', GSM + 'pants/d01794-5126-4213', 370, 'G-S037 Military Chino', GSM + 'pants/d30666-e662-2199', 'range', 'NC', 'chinos stand in'),
        sweater=G(110, 'Logo Structure Knitted Sweater', GSM + 'knitwear/d20768-c868-1632', 470, 'E Shawl Collar Knitted Sweater', GSM + 'knitwear/d20679-5375-7293', 'range', 'NC', 'crew not separable by title'),
        outerwear=G(150, 'Rackam Zip Jacket', GSM + 'jackets_and_blazers/d06697-4753-862', 1850, 'GSRR Parka', GSM + 'jackets_and_blazers/d22268-d225-d573', 'range', 'NC',
                    'E Lammy Coat (1890) is shearling: excluded as fur'),
        shoes=G(80, 'Cadet Sneakers', GSM + 'shoes/d16796-a940-990', 310, 'Lintell Contrast Sole Hiker Leather Boots', GSM + 'shoes/d22691-01-c844', 'range', 'NC',
                'own-label footwear; no full-price loafer (one loafer, markdown only), so the range is all men\'s shoes at full price; slides left out')),
    own_doors_us=9, own_doors_world=NC, locator_url=NC,
    doors_basis='facts-first (8 Oct), store finder getstores?country_iso=US: 101 US points of sale (52 department store, 28 multi-brand, 13 mono-brand, 7 shop-in-shop, 1 Q-Store); 9 G-Star-named full-price doors counted; 3 outlets (Sawgrass Mills, Jersey Gardens, Woodbury Common) and G-Star Belmont Park Village (format unstated) not counted; store endpoint not reached in this read; world NC',
    tech_named_fabrics='TECH_GS', tech_owned_or_licensed='licensed fibres named in composition: LYCRA®, Sorona®', tech_share_of_range='TECHSHARE_GS', tech_evidence_url=GSM + 'jeans/51003-c922-c776', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no', named_mills='no', made_in_stated_share='NC',
    heritage_claim=NC, process_documented='no',
    craft_url_1=GSM + 'jeans/51003-c922-c776', craft_url_2=GSM + 'jeans/d25431-d807-001', proposed_craft=1,
    craft_reasoning='Composition is published on 98% of the men\'s range, but country, maker and mill were not found in the catalogue data read, and no making story was read.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=258&brand_ids[]=2782756&catalog[]=5', vinted_brand_ids='258; 2782756', grailed_url='https://www.grailed.com/designers/g-star',
    quote=NC, quote_who=NC, quote_source=NC, quote_url=NC, quote_date=NC,
    signature_product=NC, signature_product_url=NC, status='partial (large house: style table is a category-stratified sample)',
    source=f'Chrome {D}: g-star.com/en_us Algolia index l1_gstar_US-Index_en_US (site\'s own app id and public search key; distinct by style, gender Men, 70 product types: 5,410 colour records / 2,158 styles), fiberCompositionsJson, salesClassification, PDPs for picks; doors from facts-first 8 Oct',
    note='LARGE HOUSE (stratified sample): styles_total (1,835 men\'s clothing styles), styles_with_composition (1,798) and colourway_ratio (4,744 colour records) are full-catalogue counts; fibre shares, spandex count, shape and categories come from the 176-row sample (up to 5 styles per product type, every k-th by style code), which is not proportional to category size. Swim NC at full-catalogue level (the sample holds 5 swim shorts). 1,243 styles have a full-price colour; the rest are markdown only. Collaborations excluded: WVB, G-STAR x Yay Abe. Mark: G-Star (the site and Grailed write G-Star; Vinted carries G-Star and G-Star RAW).')

# ------------------------------------------------------------------------------------------------ Gallery Dept.
M['Gallery Dept.'] = dict(
    site_domain='gallerydept.com', store_used=GD, currency='USD', search_url=GD + '/search?q=', feed_currency_rate='1.0', sublines_included='-',
    g=dict(
        tee=G(155, 'Active Fitness Tee', GDP + 'active-fitness-tee-white', 750, 'Salvage Tee', GDP + 'salvage-tee-black', 'range', GD + '/collections/all',
              'unisex house; the Trucker Sleeveless Marley (1400) is sleeveless and not taken as a tee'),
        polo=NONE_(),
        dress_shirt=G(550, 'French Parker Shirt', GDP + 'french-parker-shirt-black', 995, 'Willie Shirt', GDP + 'willie-shirt-blue-plaid', 'range', GD + '/collections/all', 'casual shirts only; Marley Retouche Flannel also 995'),
        jeans=G(625, 'Pascal Dépt. Cut', GDP + 'pascal-dept-cut-light-denim-blue', 2500, 'G Time LA Flare', GDP + 'g-time-la-flare-black', 'range', GD + '/collections/all', 'painted and reworked denim'),
        dress_pants=G(895, 'Marley Pant', GDP + 'marley-pant-yellow-gold', 2595, 'Composition Pant (mixed denim)', GDP + 'composition-pant-mixed-denim', 'range', GD + '/collections/all', 'no dress trouser; non-jean trousers stand in'),
        sweater=NONE_(note='sweatshirts only (Basic Crewneck sweatshirt 495)'),
        outerwear=G(550, 'French Track Jacket', GDP + 'french-track-jacket-deep-navy', 1595, 'Everglades Vest', GDP + 'everglades-vest-black', 'range', GD + '/collections/all',
                    'dearest jacket is the Santa Fe Trucker (1295); GD x LA Rams Anorak (2800) excluded as collaboration'),
        shoes=NONE_(note='all footwear on the store is UGG x Gallery Dept. (collaboration): NONE under the 11 Oct ruling')),
    own_doors_us=2, own_doors_world=2, locator_url=GD + '/pages/stores',
    doors_basis="brand's stores page: Los Angeles (7956 Beverly Blvd) and Miami (140 NE 39th St, Design District)",
    tech_named_fabrics='NONE', tech_owned_or_licensed='NONE', tech_share_of_range='0', tech_evidence_url=GDP + 'pascal-dept-cut-light-denim-blue', proposed_tech=NC,
    owned_facility='no claim found', named_makers='no', named_mills='no', made_in_stated_share='MADEIN_GD', heritage_claim=NC,
    process_documented='partial: product pages name a "patent wash process that uses unique fading techniques for each piece"',
    craft_url_1=GDP + 'pascal-dept-cut-light-denim-blue', craft_url_2=GD + '/pages/stores', proposed_craft=2,
    craft_reasoning='Nearly every style states its country (most Made in USA, others Portugal and Italy) and the denim pages describe a hand-finished wash process. No maker, mill or facility is named and the about page returns 404.',
    founded_year=NC, founded_place=NC, founders=NC, owner_today=NC, ownership_url=NC,
    **NOLOOK,
    vinted_mens_url='https://www.vinted.com/catalog?brand_ids[]=2929083&catalog[]=5', vinted_brand_ids='2929083', grailed_url='https://www.grailed.com/designers/gallery-dept',
    quote=NC, quote_who=NC, quote_source=NC, quote_url=NC, quote_date=NC,
    signature_product=NC, signature_product_url=NC, status='partial',
    source=f'Chrome {D}: gallerydept.com products.json (265; 234 available), body_html (Material, made-in), /pages/stores, /pages/about (404), search check',
    note='Style = title de-dup (colour SKUs collapse): 134 rows / 97 styles. Excluded: Chateau Josué (separate label under its own name), Art That Kills (record-label line), collaborations (UGG footwear, GD x LA Rams), Stevie Women\'s Tank. Many unisex pieces also carry a WOMENS tag: kept (unisex house). Founder not filed: the site\'s nav names Josué Thomas ("BTS: JOSUÉ THOMAS") and the Art That Kills copy says he founded that label, but no page states he founded Gallery Dept. Mark: GALLERY DEPT. (capitals with full stop). No markdowns.')
