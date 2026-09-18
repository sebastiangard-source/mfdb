"""Full pass over the build in this directory. Exits 1 on any failure."""
from playwright.sync_api import sync_playwright
import pathlib, sys, json, re, hashlib

PATH = sys.argv[1] if len(sys.argv)>1 else 'menswear_spectrum.html'
url = 'file://'+str(pathlib.Path(PATH).resolve())
S = open(PATH, encoding='utf8').read()
fails, checks = [], [0]
def ck(name, cond, detail=""):
    checks[0]+=1
    if not cond: fails.append(f'{name} — {detail}')
def head(t): print(f'\n--- {t}')

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1400,'height':1000})
    pg.goto(url); pg.wait_for_timeout(600)
    # read from the build, so renaming the region never reds the suite
    REGION_NAME = pg.evaluate('()=>REGION_NAME')
    errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(url); pg.wait_for_timeout(600)

    head('natural fibre, measured')
    ck('the natural dial exists', pg.eval_on_selector_all('.dial[data-attr="natural"]','e=>e.length')==1)
    # Derived, not a literal list: this asserted six brands and went red the moment a
    # seventh was counted, which is the data improving rather than a fault.
    # Derived from the values, not the keys: a house entered in NATURAL carrying the 99
    # sentinel would otherwise red the suite for no fault, and the failure printed a bare
    # False with nothing to act on.
    ck('the dial is scored for exactly the houses that were counted', pg.evaluate(
       '''()=>{const scored=[...document.querySelectorAll(".brand")]
         .filter(e=>e.dataset.natural!=="99").map(e=>e.textContent).sort();
         const want=Object.entries(NATURAL).filter(([,v])=>v!==99).map(([k])=>k).sort();
         return scored.length===want.length && scored.every((x,i)=>x===want[i]);}'''),
       pg.evaluate('()=>Object.keys(NATURAL).length'))
    ck('an uncounted house reads not-assessed, never zero', pg.evaluate(
       '''()=>[...document.querySelectorAll(".brand")].find(e=>e.textContent==="Hermès").dataset.natural''')=='99')
    pg.eval_on_selector('.dial[data-attr="natural"] input',
       "e=>{e.value=3;e.dispatchEvent(new Event('input',{bubbles:true}))}")
    pg.eval_on_selector('.dial[data-attr="tech"] input',
       "e=>{e.value=3;e.dispatchEvent(new Event('input',{bubbles:true}))}")
    pg.wait_for_timeout(550)
    # Was exactly ['Peter Millar'] when seven brands were counted; with 195 the set is
    # larger, and the invariant is that Peter Millar is in it and nothing uncounted is.
    _pm = pg.eval_on_selector_all('.brand',"e=>e.filter(x=>!x.classList.contains('out')).map(x=>[x.textContent,x.dataset.natural])")
    ck('natural and tech together find the split house',
       any(n=='Peter Millar' for n,_ in _pm) and all(v!='99' for _,v in _pm), f'{len(_pm)} shown')
    pg.goto(url+'#brand=Peter%20Millar'); pg.reload(); pg.wait_for_timeout(430)
    ck('a counted house states how its range divides',
       'Kept apart' in pg.eval_on_selector('#detailBody','e=>e.innerText'))
    _t = [l for l in pg.eval_on_selector('#detailBody','e=>e.innerText').split('\n') if l.strip()]
    ck('the range block sits inside Fabrics, above Registers',
       _t.index('FABRICS') < _t.index('THE RANGE') < _t.index('REGISTERS'))
    pg.goto(url+'#brand=Herm%C3%A8s'); pg.reload(); pg.wait_for_timeout(400)   # held short of a read
    ck('an uncounted house claims nothing',
       pg.eval_on_selector_all('#detailBody .fibre-line','e=>e.length')==0)
    pg.goto(url); pg.reload(); pg.wait_for_timeout(450)

    head('eight price slots')
    # PRSHORT was missed when the map went from five garments to eight, and every one
    # of the 200 hover cards printed three "undefined" rows for a full day. Assert on
    # every label array at once rather than on the one that happened to be found.
    ck('every garment label array is eight long', pg.evaluate('''()=>{
      const arrays = {PRGARMENTS: typeof PRGARMENTS!=="undefined" && PRGARMENTS,
                      PRSHORT:    typeof PRSHORT!=="undefined"    && PRSHORT};
      return Object.values(arrays).every(a => Array.isArray(a) && a.length===8);}'''))
    ck('no hover strip renders undefined', pg.evaluate('''()=>[...document.querySelectorAll(".brand")]
      .every(e => !/undefined/i.test(pricesStripHTML(e.textContent)))'''))
    ck('no surface renders undefined', pg.evaluate(
       "()=>document.body.innerText.toLowerCase().indexOf('undefined')<0"))
    ck('every short label array carries eight entries',
       pg.evaluate('()=>PRSHORT.length===8 && PRGARMENTS.length===8'))
    ck('every brand carries eight slots',
       pg.evaluate("()=>Object.values(PRICES).every(v=>v.length===8)"))
    ck('the slot labels match the data', pg.evaluate("()=>PRGARMENTS.length===8"))
    pg.goto(url+'#brand=Golden%20Goose'); pg.reload(); pg.wait_for_timeout(420)
    ck('the detail card draws eight rows',
       pg.eval_on_selector_all('#detailBody .pr-row','e=>e.length')==8)
    ck('a checked brand says so',
       pg.eval_on_selector_all('#detailBody .pv-ok','e=>e.length')==1)
    # Derived: the first brand with an unassessed slot, whichever it is this build.
    _unc = pg.evaluate("Object.keys(PRICES).find(k=>PRICES[k].includes('?') && !PRICE_PASS.includes(k))")
    pg.goto(url+'#brand='+_unc.replace(' ','%20').replace("'", '%27')); pg.reload(); pg.wait_for_timeout(400)
    ck('an unchecked brand does not',
       pg.eval_on_selector_all('#detailBody .pv-ok','e=>e.length')==0)
    pg.goto(url+'#prices'); pg.reload(); pg.wait_for_timeout(450)
    ck('the prices overlay offers all eight',
       len(pg.eval_on_selector_all('#pvG button','e=>e.map(x=>x.textContent)'))==9)
    ck('the garment bars carry one colour, not five',
       len(set(pg.evaluate('''()=>{const s=new Set();
         document.querySelectorAll('#detailBody [class*=pg]').forEach(e=>s.add(getComputedStyle(e).backgroundColor));
         return [...s];}''')))<=1)
    # leave no overlay open: the next block navigates by hash, which does not reload
    pg.goto(url); pg.reload(); pg.wait_for_timeout(400)

    head('map chrome')
    ck('bands show no price-and-posture line',
       pg.eval_on_selector_all('.band-range','e=>e.length')==0)
    ck('the tee bookends are gone',
       'TEE' not in pg.eval_on_selector('.scroll-note','e=>e.innerText').upper())
    ck('clear all sits above the dials',
       pg.eval_on_selector('.clearall','e=>e.getBoundingClientRect().top')
       < pg.eval_on_selector('.grp','e=>e.getBoundingClientRect().top'))

    head('rail and masthead')
    ck('all dial groups open by default',
       all(pg.eval_on_selector_all('.grp','e=>e.map(x=>x.open)')))
    ck('channel chips are gone', pg.eval_on_selector_all('.chip','e=>e.length')==0)
    # Removed once, restored 14 Sep: Golffice answers course-vs-office, not how much
    # golf runs the brand, and both questions were being asked.
    ck('golfiness dial is back, once, at the top of Culture',
       pg.eval_on_selector_all('.dial[data-attr="golf"]','e=>e.length')==1 and
       pg.eval_on_selector_all('.grp .gbody .dial','e=>e.map(x=>x.dataset.attr)').index('golf') ==
       pg.eval_on_selector_all('.grp .gbody .dial','e=>e.map(x=>x.dataset.attr)').index('status')-1)
    ck('the four two-way dials sit in one row',
       pg.eval_on_selector_all('.birow .dial','e=>e.map(x=>x.dataset.attr)')==['fuss','golffice','bruv','sail'])
    ck('no two-way dial is left in a group',
       pg.eval_on_selector_all('.grp .dial[data-bipolar="1"]','e=>e.length')==0)
    ck('group badges match their contents',
       pg.eval_on_selector_all('.grp',"e=>e.every(g=>+g.querySelector('.gn').textContent===g.querySelectorAll('.dial').length)"))
    ck('masthead pills share a row on desktop',
       pg.eval_on_selector_all('.mastbtn','e=>e[0].getBoundingClientRect().top===e[1].getBoundingClientRect().top'))
    ck('no horizontal overflow at this width',
       not pg.evaluate('()=>document.documentElement.scrollWidth>innerWidth'))

    head('structure')
    dials = pg.eval_on_selector_all('.dial','e=>e.map(x=>x.dataset.attr)')
    brands = pg.eval_on_selector_all('.brand','e=>e.length')
    ck('every dial has a data-attr', all(dials) and len(dials)>25, len(dials))
    # count comes from the file so a seating does not fail the suite; the check that
    # matters is that every surface agrees, not that the number is any given value.
    import re as _re
    expected = len(_re.findall(r'\["([^"]+)",[01],\[[\d,\s]+\]', S))
    ck('every brand row renders', brands==expected, f'{brands} rendered vs {expected} in BANDS')
    ck('no duplicate dial keys', len(set(dials))==len(dials), f'{len(dials)} dials, {len(set(dials))} unique')
    labs = pg.eval_on_selector_all('.dl','e=>e.map(x=>x.textContent)')
    ck('all labels lowercase', not [x for x in labs if any(c.isupper() for c in x)],
       [x for x in labs if any(c.isupper() for c in x)])
    gn = pg.eval_on_selector_all('.gn','e=>e.map(x=>+x.textContent)')
    bi = pg.eval_on_selector_all('.birow .dial','e=>e.length')
    ck('grouped badges plus the two-way row account for every dial',
       sum(gn)+bi==len(dials), f'{gn} + {bi} vs {len(dials)}')
    print(f'    dials {len(dials)}  brands {brands}  groups {gn}')

    head('every dial explainer opens and is clean')
    bad=[]
    for k in dials:
        pg.goto(url+'#dial='+k); pg.wait_for_timeout(190)
        shown = pg.eval_on_selector('#dialView','e=>e.classList.contains("show")')
        txt = pg.eval_on_selector('#dialBody','e=>e.innerText')
        h2  = pg.eval_on_selector('#dialBody h2','e=>e.textContent')
        lv  = pg.eval_on_selector_all('#dialBody .lvl b','e=>e.map(x=>x.textContent)')
        if not shown: bad.append(f'{k}: did not open')
        # "99 more not shown" is a legitimate count; only a level *labelled* 99 is the sentinel
        if any(x.strip() in ('99','\u221299') for x in lv): bad.append(f'{k}: sentinel rendered as a level')
        if 'NOT_ASSESSED' in txt: bad.append(f'{k}: constant name leaked to the UI')
        if not h2.strip(): bad.append(f'{k}: no title')
        if any(x.strip()=='0' for x in lv): bad.append(f'{k}: zero rendered as a level')
        if 'undefined' in txt.lower() or 'NaN' in txt: bad.append(f'{k}: undefined/NaN in body')
    ck('every dial explainer is clean', not bad, bad[:6])
    print(f'    checked {len(dials)} explainers, {len(bad)} problems')

    head('counts add up per dial')
    mismatch=[]
    for k in dials:
        pg.goto(url+'#dial='+k); pg.wait_for_timeout(170)
        sub = pg.eval_on_selector('#dialBody .dv-sub','e=>e.textContent')
        m = re.search(r'(\d+) brands? placed \u00b7 (\d+) at zero(?: \u00b7 (\d+) not assessed)?', sub)
        if not m: mismatch.append(f'{k}: sub unparsable {sub!r}'); continue
        placed, zero, un = int(m.group(1)), int(m.group(2)), int(m.group(3) or 0)
        if placed+zero+un != brands:
            mismatch.append(f'{k}: {placed}+{zero}+{un}={placed+zero+un} != {brands}')
    ck('placed+zero+unassessed == brand count for every dial', not mismatch, mismatch[:5])
    print(f'    {len(dials)-len(mismatch)}/{len(dials)} dials reconcile to {brands}')

    head('bipolar dials keep both poles')
    for k in ['bruv','sail','fuss','golffice']:
        pg.goto(url+'#dial='+k); pg.wait_for_timeout(200)
        lv = pg.eval_on_selector_all('#dialBody .lvl b','e=>e.map(x=>x.textContent)')
        neg = [x for x in lv if x.startswith('\u2212')]
        ck(f'{k} shows negative levels', len(neg)>0, lv)
    print('    bruv/sail/fuss/golffice negative halves present')

    head('chip -> brand card, one overlay at a time')
    for k in ['scandi','briish','prep']:
        pg.goto(url+'#dial='+k); pg.wait_for_timeout(220)
        nm = pg.eval_on_selector('#dialBody .exl a','e=>e.textContent')
        pg.eval_on_selector('#dialBody .exl a','e=>e.click()'); pg.wait_for_timeout(480)
        top = pg.evaluate("()=>{const el=document.elementFromPoint(700,500);"
                          "return el.closest('#dialView')?'dial':el.closest('#detailView')?'detail':'other'}")
        ck(f'{k}: chip opens brand card on top', top=='detail', top)
        ck(f'{k}: dial view closed', not pg.eval_on_selector('#dialView','e=>e.classList.contains("show")'))
        ck(f'{k}: right brand', pg.eval_on_selector('#detailBody h2','e=>e.textContent')==nm)
    print('    chips navigate correctly from 3 dials')

    head('stockist record')
    pg.goto(url+'#brand=Jack%20Victor'); pg.wait_for_timeout(380)
    t = pg.eval_on_selector('#detailBody','e=>e.innerText')
    ck('a no-own-door brand still shows where to buy it', REGION_NAME in t)
    ck('stockist record is labelled regional', REGION_NAME in t)
    ck('own-door zero and stockists coexist', 'none' in t and 'independent stockist' in t)
    # a brand outside the register must show nothing rather than an empty claim
    pg.goto(url+'#brand=Hackett'); pg.wait_for_timeout(330)
    t2 = pg.eval_on_selector('#detailBody','e=>e.innerText')
    ck('no stockist row where the register has not reached', REGION_NAME not in t2)
    ck('no zero-shop claim anywhere', '0 shops' not in t2 and '0 shops' not in t)
    pg.goto(url+'#brand=Jack%20Victor'); pg.wait_for_timeout(350)
    ck('regional row and button on the card', pg.eval_on_selector_all('.region-btn','e=>e.length')==1)
    ck('the regional control is a filled green pill',
       pg.eval_on_selector('.region-btn',"e=>getComputedStyle(e).backgroundColor")=='rgb(18, 59, 43)')
    ck('it stays compact with a mouse',
       pg.eval_on_selector('.region-btn','e=>e.getBoundingClientRect().height')<=28,
       pg.eval_on_selector('.region-btn','e=>e.getBoundingClientRect().height'))
    ck('no chevron on the label',
       '\u203a' not in pg.eval_on_selector('.region-btn','e=>e.textContent'))
    ck('the regional copy says stores, not doors',
       'own store' in pg.eval_on_selector('#detailBody','e=>e.innerText'))
    pg.eval_on_selector('.region-btn','e=>e.click()'); pg.wait_for_timeout(420)
    ck('panel opens over the card',
       pg.eval_on_selector('#regionView','e=>e.classList.contains("show")') and
       pg.evaluate("()=>!!document.elementFromPoint(700,500).closest('#regionView')"))
    dl = pg.eval_on_selector_all('#regionView .rv-door','e=>e.map(x=>({h:x.href,t:x.target,c:x.className}))')
    # Derived: sixteen shops arrived with Merz b. Schwanen and a literal 19 would have
    # gone red with a number and no explanation.
    want = pg.evaluate("()=>(REGION['Jack Victor']||{s:[]}).s.length")
    ck('every stockist row opens its shop page', len(dl)==want and
       all('shop-open' in x['c'] and '#shop=' in x['h'] for x in dl), f'{len(dl)} of {want}')
    pg.goto(url+'#region=Lululemon'); pg.reload(); pg.wait_for_timeout(420)
    ol = pg.eval_on_selector_all('#regionView .rv-door','e=>e.map(x=>({h:x.href,t:x.target}))')
    ck('own doors still go straight to a map in a new tab',
       all(x['h'].startswith('https://www.google.com/maps/search/') and x['t']=='_blank' for x in ol), len(ol))
    pg.goto(url+'#brand=Jack%20Victor'); pg.reload(); pg.wait_for_timeout(400)
    pg.eval_on_selector('.region-btn','e=>e.click()'); pg.wait_for_timeout(350)
    ck('both channels are labelled',
       set(pg.eval_on_selector_all('#regionView .rv-kind','e=>e.map(x=>x.textContent)'))=={'STOCKIST'})
    ck('panel states the regional limit', 'register has not reached' in
       pg.eval_on_selector('#regionBody','e=>e.innerText'))
    ck('the panel counts stores, not doors',
       'brand-owned store' in pg.eval_on_selector('#regionBody .rv-lead','e=>e.textContent'))
    pg.keyboard.press('Escape'); pg.wait_for_timeout(320)
    ck('escape returns to the brand card',
       pg.eval_on_selector('#detailView','e=>e.classList.contains("show")') and
       not pg.eval_on_selector('#regionView','e=>e.classList.contains("show")') and
       pg.evaluate('location.hash')=='#brand=Jack%20Victor')
    pg.goto(url+'#region=Peter%20Millar'); pg.wait_for_timeout(400)
    ck('deep link opens the panel', pg.eval_on_selector('#regionView','e=>e.classList.contains("show")'))
    ck('own doors and stockists both shown',
       set(pg.eval_on_selector_all('#regionView .rv-kind','e=>e.map(x=>x.textContent)'))=={'OWN STORE','STOCKIST'})
    # stockist detail pages
    # enter through the brand card so the whole stack exists to peel
    pg.goto(url+'#brand=Peter%20Millar'); pg.reload(); pg.wait_for_timeout(430)
    pg.eval_on_selector('.region-btn','e=>e.click()'); pg.wait_for_timeout(330)
    pg.eval_on_selector('#regionView .shop-open','e=>e.click()'); pg.wait_for_timeout(360)
    sb = pg.eval_on_selector('#shopBody','e=>e.innerText')
    ck('stockist page opens with an origin', pg.eval_on_selector('#shopView','e=>e.classList.contains("show")')
       and 'ORIGIN' in sb.upper())
    ck('stockist page cites its source', 'Source:' in sb or 'confidence' in sb)
    ck('stockist page carries its assortment caveat', 'not what is on the rack' in sb)
    ck('brand chips link out', pg.eval_on_selector_all('#shopBody .exl a','e=>e.length')>0)
    ck('every stockist page offers the visit form',
       pg.evaluate("()=>PLACES.filter(p=>p.k==='s').every(p=>visitUrl(p).startsWith('https://form.jotform.com/'))"))
    ck('every shop sends the state', pg.evaluate(
       "()=>PLACES.filter(p=>p.k==='s').every(p=>visitUrl(p).includes(VISIT_PARAM.state+'='))"))
    # The form has one Store dropdown per state and reached seven before the register
    # did: shops in NJ, PA and DE have no parameter to target until it is rebuilt. They
    # still prefill State. Assert only over the states the form actually carries.
    ck('each shop targets the dropdown for its own state', pg.evaluate(
       """()=>PLACES.filter(p=>p.k==='s'&&STORE_PARAM[p.s])
            .every(p=>visitUrl(p).includes(STORE_PARAM[p.s]+'='))"""))
    ck('a shop outside the form\'s states still prefills the state', pg.evaluate(
       """()=>PLACES.filter(p=>p.k==='s'&&!STORE_PARAM[p.s])
            .every(p=>visitUrl(p).includes(VISIT_PARAM.state+'='))"""))
    ck('no shop targets another state\'s dropdown', pg.evaluate(
       "()=>PLACES.filter(p=>p.k==='s').every(p=>Object.entries(STORE_PARAM)"
       ".filter(([k])=>k!==p.s).every(([,v])=>!visitUrl(p).includes(v+'=')))"))
    ck('nothing is sent to the deleted fields', pg.evaluate(
       "()=>PLACES.filter(p=>p.k==='s').every(p=>!visitUrl(p).includes('q6_')&&!visitUrl(p).includes('otherStore'))"))
    ck('the store string is the register text where one exists',
       pg.evaluate("()=>PLACES.filter(p=>p.k==='s'&&p.f).every(p=>storeString(p)===p.f)"))
    ck('the report action is the section\'s only filled control',
       pg.eval_on_selector('#shopBody .sv-cta','e=>getComputedStyle(e).backgroundColor')=='rgb(18, 59, 43)')
    ck('the paste string is a value, not another button',
       'dashed' in pg.eval_on_selector('#shopBody .sv-store','e=>getComputedStyle(e).borderStyle'))
    ck('the shop page shows the exact string to paste',
       pg.eval_on_selector('#shopBody .sv-store','e=>e.textContent')==
       pg.eval_on_selector('#shopBody a.visit-link','e=>e.dataset.store'))
    ck('urls encode spaces as %20, never +',
       pg.evaluate("()=>PLACES.filter(p=>p.k==='s').every(p=>!visitUrl(p).includes('+'))"))
    ck('every shop page carries a copyable store name',
       pg.evaluate("()=>PLACES.filter(p=>p.k==='s').every(p=>storeString(p).includes(' \u2014 '))"))

    ck('shop slugs are unique',
       pg.evaluate("()=>{const s=PLACES.filter(p=>p.k==='s').map(shopSlug);return s.length===new Set(s).size}"))
    for i,exp in enumerate([('shop',False),('region',False),('brand',False)]):
        pass
    ids = ['#shopView','#regionView','#detailView']
    pg.keyboard.press('Escape'); pg.wait_for_timeout(280)
    ck('escape closes only the shop page',
       not pg.eval_on_selector(ids[0],'e=>e.classList.contains("show")')
       and pg.eval_on_selector(ids[1],'e=>e.classList.contains("show")'), 'peeled too many layers')
    pg.keyboard.press('Escape'); pg.wait_for_timeout(280)
    ck('next escape closes only the region panel',
       not pg.eval_on_selector(ids[1],'e=>e.classList.contains("show")')
       and pg.eval_on_selector(ids[2],'e=>e.classList.contains("show")'))
    # a chip must not open the brand card underneath a taller overlay
    slug = pg.evaluate("()=>shopSlug(PLACES.find(p=>p.k==='s'&&brandsAt(PLACES.indexOf(p)).length))")
    pg.goto(url+'#shop='+slug); pg.reload(); pg.wait_for_timeout(420)
    ck('a shop page opens from its slug', pg.eval_on_selector('#shopView','e=>e.classList.contains("show")'))
    pg.eval_on_selector('#shopBody .exl a','e=>e.click()'); pg.wait_for_timeout(380)
    ck('brand chip from a shop page lands on top',
       pg.evaluate("()=>!!document.elementFromPoint(700,500).closest('#detailView')"))
    # a researched-but-unwritten shop must say so rather than show nothing
    idx = pg.evaluate("()=>PLACES.findIndex(p=>p.k==='s' && (!p.o || !p.o.s))")
    if idx >= 0:
        pg.goto(url+'#shop='+pg.evaluate("i=>shopSlug(PLACES[i])",idx)); pg.reload(); pg.wait_for_timeout(400)
        ck('a shop with no story says so',
           'not yet written up' in pg.eval_on_selector('#shopBody','e=>e.innerText').lower()
           or 'No origin research' in pg.eval_on_selector('#shopBody','e=>e.innerText'))

    pg.goto(url+'#region=Peter%20Millar'); pg.reload(); pg.wait_for_timeout(420)
    ck('lead line uses numerals throughout',
       not any(w in pg.eval_on_selector('#regionBody .rv-lead','e=>e.textContent')
               for w in ['One ','Two ','Three ','Seventeen']))

    head('a brand card always lands on top')
    # every route in: dial chip, region panel via a shop page, boutiques index via a shop
    for label,h,sel,second in [
        ('dial chip','#dial=prep','#dialBody .exl a',None),
        ('region panel','#region=Peter%20Millar','#regionView .shop-open','#shopBody .exl a'),
        ('stores index','#stores=shop','#boutiquesView .bo-row.shop-open','#shopBody .exl a')]:
        pg.goto(url+h); pg.reload(); pg.wait_for_timeout(450)
        pg.eval_on_selector(sel,'e=>e.click()'); pg.wait_for_timeout(430)
        if second:
            pg.eval_on_selector(second,'e=>e.click()'); pg.wait_for_timeout(430)
        ck(f'{label}: the brand card is on top', pg.evaluate(
           "()=>!!document.elementFromPoint(700,500).closest('#detailView')"))
        ck(f'{label}: nothing left open above it', pg.evaluate(
           "()=>['shopView','boutiquesView','regionView','dialView']"
           ".every(id=>!document.getElementById(id).classList.contains('show'))"))

    head('region is the Northeast')
    ck('the region covers ten states', pg.evaluate('()=>REGION_STATES.length')==10)
    # NJ and PA rendered as bare codes in the index because both state-name maps stopped
    # at New York. Every state the register can hold must have a name.
    ck('every region state has a full name', pg.evaluate(
       '()=>REGION_STATES.every(s=>ST_NAME[s]&&ST_FULL[s])'))
    ck('no shop renders a bare state code', pg.evaluate(
       '''()=>[...new Set(PLACES.filter(p=>p.k==="s").map(p=>p.s))].every(s=>!!ST_NAME[s])'''))

    head('state codes')
    # Southern Tide carried full state names on 39 towns, so five stores in Chatham,
    # Mashpee, Nantucket, Newport and Westport matched no state filter anywhere.
    ck('every door record uses two-letter state codes', pg.evaluate('''()=>
      [...document.querySelectorAll(".brand")].every(e=>{const d=DOORS[e.textContent];
        return !d||!d.cities||d.cities.every(c=>/^[A-Z]{2}$/.test(c[1]));})'''))
    ck('and so does every addressed place', pg.evaluate(
       '()=>PLACES.every(p=>/^[A-Z]{2}$/.test(p.s))'))

    head('a brand with stores in the region never reads silent')
    pg.goto(url); pg.reload(); pg.wait_for_timeout(500)
    _cov = pg.evaluate('''()=>{let a=0,b=0,c=[];
      [...document.querySelectorAll(".brand")].forEach(e=>{const h=regionLineHTML(e.textContent,true);
        if(!h){const g=regionFromDoors(e.textContent); if(g) c.push(e.textContent);}
        else if(h.includes("region-pending"))b++; else a++;});
      return {addressed:a, count_only:b, wrongly_silent:c};}''')
    ck('no brand with regional stores renders nothing',
       not _cov['wrongly_silent'], _cov['wrongly_silent'][:4])
    ck('brands with counts but no addresses say so', _cov['count_only'] > 0, _cov['count_only'])
    # Canali had 11 stockist addresses and an empty own-door list, so the record existed
    # and the fallback never fired: it read 0 own stores while the map held two of its shops.
    ck('an empty own-door list is not treated as no stores', pg.evaluate('''()=>
      Object.entries(REGION).filter(([n,v])=>!(v.o||[]).length && regionFromDoors(n))
        .every(([n])=>/own store/.test(regionLineHTML(n,true)))'''))
    # Named brands keep graduating out of this state as their addresses are merged, so
    # find one at runtime rather than hardcoding a third. Skip if none is left.
    _co = pg.evaluate('''()=>[...document.querySelectorAll(".brand")].map(e=>e.textContent)
      .filter(n=>{const r=REGION[n]; return (!r||!r.o.length) && regionFromDoors(n);})''')
    if not _co:
        ck('no brand is left in the count-only state', True, 'all addressed')
    else:
        pg.goto(url+'#brand='+_co[0].replace(' ','%20').replace('&','%26'))
        pg.reload(); pg.wait_for_timeout(430)
        ck('the detail card names the gap rather than staying silent',
           'addresses not yet on file' in pg.eval_on_selector('#detailBody','e=>e.innerText'), _co[0])
        # The intent is that no button opens an empty panel, not that a partly-addressed
        # brand loses its button: Bonobos has one stockist address and nine unaddressed
        # stores, and the button honours the address it has.
        ck('no button opens an empty panel', pg.evaluate('''()=>
          [...document.querySelectorAll(".brand")].map(e=>e.textContent).every(n=>{
            const f = regionFigures(n);
            if(!f) return true;
            const html = stockistRow(n);
            return !/region-btn/.test(html) || f.ids.length > 0;})'''))

    head('regional line appears everywhere a brand is presented')
    pg.goto(url); pg.reload(); pg.wait_for_timeout(500)
    pg.eval_on_selector_all('.brand',"e=>e.find(x=>x.textContent==='Peter Millar').click()")
    pg.wait_for_timeout(480)
    hc = pg.eval_on_selector('#hoverCard','e=>e.innerText')
    ck('hover card carries the regional line', REGION_NAME in hc)
    ck('hover card button opens the panel', pg.eval_on_selector_all('#hoverCard .region-btn','e=>e.length')==1)
    ck('the pill sits on its own line, never inline',
       pg.eval_on_selector('#hoverCard .region-btn','e=>e.getBoundingClientRect().top')
       > pg.eval_on_selector('#hoverCard .hc-region','e=>e.getBoundingClientRect().top') + 8)
    pg.eval_on_selector('#hoverCard .region-btn','e=>e.click()'); pg.wait_for_timeout(400)
    ck('panel opens from the hover card',
       pg.eval_on_selector('#regionView','e=>e.classList.contains("show")') and
       pg.eval_on_selector('#regionBody h2','e=>e.textContent').startswith('Peter Millar'))
    pg.keyboard.press('Escape'); pg.wait_for_timeout(280)
    pg.goto(url); pg.reload(); pg.wait_for_timeout(450)
    pg.eval_on_selector('.dial[data-attr="scandi"] input',
      "el=>{el.value=4; el.dispatchEvent(new Event('input',{bubbles:true}));}")
    pg.wait_for_timeout(520)
    wc = pg.eval_on_selector_all('.whycard','e=>e.map(x=>x.innerText)')
    # Derived: this asserted 3 and went to 5 when the Mid-Atlantic shops gave more brands
    # a stockist. The invariant is that a card shows the line exactly when a record exists.
    want = pg.evaluate('''()=>[...document.querySelectorAll(".whycard")]
      .filter(c=>{const n=c.querySelector("h4").textContent.replace(/\\(.*\\)$/,"").trim();
                  return !!regionFigures(n);}).length''')
    ck('why cards carry it exactly where a record exists',
       sum(1 for x in wc if REGION_NAME in x)==want,
       f'{sum(1 for x in wc if REGION_NAME in x)} of {want}')
    ck('why card buttons present',
       pg.eval_on_selector_all('.whycard .region-btn','e=>e.length')==want)
    pg.eval_on_selector('.whycard .region-btn','e=>e.click()'); pg.wait_for_timeout(400)
    ck('panel opens from a why card', pg.eval_on_selector('#regionView','e=>e.classList.contains("show")'))
    pg.keyboard.press('Escape'); pg.wait_for_timeout(250)
    pg.eval_on_selector('.clearall','e=>e.click()'); pg.wait_for_timeout(300)
    pg.eval_on_selector_all('.brand',"e=>e.find(x=>x.textContent==='Hackett').click()")
    pg.wait_for_timeout(430)
    ck('no line where the register has not reached',
       REGION_NAME not in pg.eval_on_selector('#hoverCard','e=>e.innerText'))

    head('brand card <-> dial explainer')
    pg.goto(url+'#brand=Buck%20Mason'); pg.reload(); pg.wait_for_timeout(450)
    nl = pg.eval_on_selector_all('#detailBody .noterow a.dial-link','e=>e.length')
    ck('note rows link to their dial', nl>0, nl)
    ck('dial links are not uppercased',
       pg.eval_on_selector('#detailBody .noterow a.dial-link','e=>getComputedStyle(e).textTransform')=='none')
    pg.eval_on_selector('#detailBody .noterow a.dial-link','e=>e.click()'); pg.wait_for_timeout(330)
    ck('dial stacks over the brand card',
       pg.eval_on_selector('#dialView','e=>e.classList.contains("show")') and
       pg.eval_on_selector('#detailView','e=>e.classList.contains("show")') and
       pg.evaluate("()=>!!document.elementFromPoint(700,500).closest('#dialView')"))
    pg.keyboard.press('Escape'); pg.wait_for_timeout(300)
    ck('escape peels one layer, brand card survives',
       pg.eval_on_selector('#detailView','e=>e.classList.contains("show")') and
       not pg.eval_on_selector('#dialView','e=>e.classList.contains("show")'))
    ck('brand hash restored on the way back', pg.evaluate('location.hash')=='#brand=Buck%20Mason',
       pg.evaluate('location.hash'))
    pg.eval_on_selector('#detailBody .chipd','e=>e.click()'); pg.wait_for_timeout(280)
    ck('inline rubric offers a way through',
       pg.eval_on_selector_all('#detailBody .rub-inline a.dial-link','e=>e.length')>0)
    pg.goto(url); pg.wait_for_timeout(400)
    pg.eval_on_selector('.dial[data-attr="prep"] .dl','e=>e.click()'); pg.wait_for_timeout(280)
    pg.keyboard.press('Escape'); pg.wait_for_timeout(280)
    ck('a dial opened from the rail still closes to the map',
       not pg.eval_on_selector('#dialView','e=>e.classList.contains("show")') and pg.evaluate('location.hash')=='')

    head('filtering still works, and NOT_ASSESSED satisfies nothing')
    pg.goto(url); pg.wait_for_timeout(500)
    def setdial(k,v):
        pg.eval_on_selector(f'.dial[data-attr="{k}"] input',
          "el=>{el.value=%d; el.dispatchEvent(new Event('input',{bubbles:true}));}"%v)
        pg.wait_for_timeout(420)
    def passing(): return sorted(pg.eval_on_selector_all('.brand',
        "e=>e.filter(x=>!x.classList.contains('out')).map(x=>x.textContent)"))
    setdial('scandi',4); a=passing()
    ck('scandi>=4 returns the six', a==['Acne Studios','Les Deux','NN07','Norse Projects','Our Legacy','Samsøe Samsøe'], a)
    pg.eval_on_selector('.clearall','e=>e.click()'); pg.wait_for_timeout(400)
    ck('clear all restores everything', len(passing())==brands, len(passing()))
    setdial('briish',5); bb=passing()
    ck("bri'ish=5 returns ten", len(bb)==10, bb)
    pg.eval_on_selector('.clearall','e=>e.click()'); pg.wait_for_timeout(350)
    # a dial with many unassessed must exclude them
    setdial('shoes',3); sh=passing()
    unass = pg.eval_on_selector_all('.brand',"e=>e.filter(x=>+x.dataset.shoes===99).map(x=>x.textContent)")
    ck('not-assessed brands excluded by a filter', not set(sh)&set(unass), list(set(sh)&set(unass))[:4])
    print(f'    shoes>=3 passes {len(sh)}, none of the {len(unass)} unassessed')
    pg.eval_on_selector('.clearall','e=>e.click()'); pg.wait_for_timeout(350)
    # two-way, negative direction
    setdial('fuss',-2); fz=passing()
    neg = pg.eval_on_selector_all('.brand',"e=>e.filter(x=>+x.dataset.fuss<=-2&&+x.dataset.fuss!==99).length")
    ck('two-way negative filter matches the data', len(fz)==neg, f'{len(fz)} vs {neg}')
    pg.eval_on_selector('.clearall','e=>e.click()'); pg.wait_for_timeout(350)

    head('empty-state guard (anySurvivor)')
    # Turning a dial to a value nothing satisfies must never leave a blank map:
    # the guard walks the dial back. Unassessed brands must not count as survivors.
    empty=[]
    for k in dials:
        pg.eval_on_selector('.clearall','e=>e.click()'); pg.wait_for_timeout(120)
        mx = pg.eval_on_selector(f'.dial[data-attr="{k}"] input','e=>+e.max')
        setdial(k, mx)
        vis = len(passing())
        if vis == 0: empty.append(f'{k} at {mx} left the map blank')
    ck('no dial setting empties the map', not empty, empty[:5])
    pg.eval_on_selector('.clearall','e=>e.click()'); pg.wait_for_timeout(300)
    print(f'    swept {len(dials)} dials at max, {len(empty)} blank states')

    # Direct cover for the guard's not-assessed clause. No real dial state can
    # distinguish it today — every value with unassessed brands also has real
    # survivors — so the state is contrived in-page and then restored.
    guard = pg.evaluate('''()=>{
      const brands=[...document.querySelectorAll('.brand')];
      const dials=[...document.querySelectorAll('.legend .dial')];
      const d=dials.find(x=>x.dataset.attr==='shoes');
      const saved=brands.map(b=>b.dataset.shoes);
      brands.forEach(b=>b.dataset.shoes=99);
      dials.forEach(x=>x.querySelector('input').value=0);
      d.querySelector('input').value=3;
      const r=anySurvivor();
      brands.forEach((b,i)=>b.dataset.shoes=saved[i]);
      dials.forEach(x=>x.querySelector('input').value=0);
      return r;}''')
    ck('guard treats an all-unassessed dial as no survivors', guard is False, guard)
    pg.eval_on_selector('.clearall','e=>e.click()'); pg.wait_for_timeout(250)
    print('    anySurvivor returns', guard, 'when every brand is unassessed')

    head('why cards')
    setdial('scandi',4); pg.wait_for_timeout(300)
    ck('why cards appear under ten', pg.eval_on_selector_all('.whycard','e=>e.length')==6)
    setdial('scandi',2); pg.wait_for_timeout(350)
    ck('why cards hide above ten', pg.eval_on_selector_all('.whycard','e=>e.length')==0,
       pg.eval_on_selector_all('.whycard','e=>e.length'))
    pg.eval_on_selector('.clearall','e=>e.click()'); pg.wait_for_timeout(300)

    head('hover card fit')
    pg.goto(url); pg.reload(); pg.wait_for_timeout(500)
    res = pg.evaluate('''async ()=>{
      const sleep=ms=>new Promise(r=>setTimeout(r,ms)); const out=[];
      for(const el of document.querySelectorAll('.brand')){
        el.scrollIntoView({block:'center'}); await sleep(4);
        el.click(); await sleep(22);
        const c=document.getElementById('hoverCard');
        const r=c.getBoundingClientRect();
        out.push({hidden:c.scrollHeight-Math.round(r.height),
                  flagged:c.classList.contains('is-clipped'),
                  off:r.top<-1||r.bottom>innerHeight+1});
        document.body.click(); await sleep(4);}
      return out;}''')
    ck('no hover card is placed off-screen', not [r for r in res if r['off']],
       len([r for r in res if r['off']]))
    missed = [r for r in res if r['hidden']>4 and not r['flagged']]
    ck('every clipped card is flagged as scrollable', not missed, len(missed))
    # the hint must be opaque, or content scrolls under it and both render at once
    # measure on a card that is actually clipped, or ::after has no rule to compute
    tall = pg.evaluate('''async ()=>{
      const sleep=ms=>new Promise(r=>setTimeout(r,ms));
      for(const el of document.querySelectorAll('.brand')){
        el.scrollIntoView({block:'center'}); await sleep(4); el.click(); await sleep(24);
        const c=document.getElementById('hoverCard');
        if(c.classList.contains('is-clipped')) return el.textContent;
        document.body.click(); await sleep(4);
      } return null;}''')
    ck('a clipped card exists to measure', tall is not None)
    bg = pg.eval_on_selector('#hoverCard',"e=>getComputedStyle(e,'::after').backgroundColor")
    ck('the scroll hint has a solid background',
       bg not in ('rgba(0, 0, 0, 0)','transparent'), f'{tall}: {bg}')
    ck('no mask fades the card content',
       pg.eval_on_selector('#hoverCard',"e=>getComputedStyle(e).maskImage")=='none')
    # a hidden card measures 0; open one before asking how wide it is
    pg.eval_on_selector_all('.brand',"e=>e.find(x=>x.textContent==='Theory').click()")
    pg.wait_for_timeout(350)
    ck('the card widens on a roomy window',
       pg.eval_on_selector('#hoverCard','e=>e.getBoundingClientRect().width')>400,
       pg.eval_on_selector('#hoverCard','e=>e.getBoundingClientRect().width'))
    pg.eval_on_selector('body','e=>e.click()'); pg.wait_for_timeout(200)

    head('pronunciation')
    pg.goto(url+'#brand=Herm%C3%A8s'); pg.reload(); pg.wait_for_timeout(400)
    ck('detail card shows the respelling',
       pg.eval_on_selector('#detailBody h2 .say','e=>e.textContent')=='(air-MEZ)')
    ck('respelling stays subordinate to the name',
       pg.eval_on_selector('#detailBody h2 .say','e=>parseFloat(getComputedStyle(e).fontSize)')
       / pg.eval_on_selector('#detailBody h2','e=>parseFloat(getComputedStyle(e).fontSize)') < 0.5)
    ck('respelling is spaced from the name',
       pg.eval_on_selector('#detailBody h2 .say','e=>parseFloat(getComputedStyle(e).marginLeft)')>=6)
    pg.goto(url+'#brand=Buck%20Mason'); pg.reload(); pg.wait_for_timeout(380)
    ck('no respelling where none was assessed',
       pg.eval_on_selector_all('#detailBody h2 .say','e=>e.length')==0)
    pg.goto(url); pg.reload(); pg.wait_for_timeout(450)
    pg.eval_on_selector_all('.brand',"e=>e.find(x=>x.textContent==='Jacquemus').click()")
    pg.wait_for_timeout(430)
    ck('hover card shows it too',
       pg.eval_on_selector('#hoverCard h4 .say','e=>e.textContent')=='(zhak-MOOSE)')
    ck('hover name does not wrap because of it',
       pg.eval_on_selector('#hoverCard h4','e=>e.getBoundingClientRect().height')<40)

    head('boutiques index')
    pg.goto(url); pg.reload(); pg.wait_for_timeout(450)
    ck('masthead reads Prices and Stores',
       pg.eval_on_selector_all('.mastbtn','e=>e.map(x=>x.textContent)')==['Prices','Stores'])
    pg.eval_on_selector('#boutiquesBtn','e=>e.click()'); pg.wait_for_timeout(430)
    ck('index opens with every store of both kinds',
       pg.eval_on_selector_all('#boutiquesView .bo-row','e=>e.length')==
       pg.evaluate("()=>PLACES.filter(p=>p.k==='s'||p.k==='o').length"))
    ck('every independent shop row offers a report action',
       pg.eval_on_selector_all('#boutiquesView .bo-report.visit-link','e=>e.length')==
       pg.eval_on_selector_all('#boutiquesView .bo-line:not(.bo-own)','e=>e.length'))
    ck('it targets exactly what the shop page targets',
       pg.evaluate("()=>[...document.querySelectorAll('#boutiquesView .bo-report.visit-link')]"
                   ".every(a=>{const p=PLACES.find(x=>x.k==='s'&&storeString(x)===a.dataset.store);"
                   "return p && a.getAttribute('href')===visitUrl(p);})"))
    # Grouped by state until 15 Sep; now one alphabetical list with a region tag per row,
    # and the tag set must cover every sub-region the data declares for the shops shown.
    want_regions = pg.evaluate("()=>new Set(PLACES.filter(p=>p.k==='s'||p.k==='o').map(p=>SUBREGION[p.s+'|'+p.c])).size")
    got_regions = len(set(pg.eval_on_selector_all('#boutiquesView .bo-region','e=>e.map(x=>x.textContent)')))
    ck('index tags every declared sub-region', got_regions==want_regions, f'{got_regions} of {want_regions}')
    ck('index is no longer grouped by state', pg.eval_on_selector_all('#boutiquesView .rv-state','e=>e.length')==0)
    ck('index states the regional limit',
       'register has not reached' in pg.eval_on_selector('#boBody','e=>e.innerText'))
    pg.eval_on_selector('#boutiquesView .bo-row.shop-open','e=>e.click()'); pg.wait_for_timeout(380)
    ck('a row opens its shop page over the index',
       pg.eval_on_selector('#shopView','e=>e.classList.contains("show")') and
       pg.eval_on_selector('#boutiquesView','e=>e.classList.contains("show")'))
    pg.keyboard.press('Escape'); pg.wait_for_timeout(300)
    ck('escape peels the shop and keeps the index',
       not pg.eval_on_selector('#shopView','e=>e.classList.contains("show")') and
       pg.eval_on_selector('#boutiquesView','e=>e.classList.contains("show")') and
       pg.evaluate('location.hash').startswith('#stores'))
    pg.keyboard.press('Escape'); pg.wait_for_timeout(300)
    ck('second escape closes the index', pg.evaluate('location.hash')=='')
    pg.goto(url+'#boutiques'); pg.reload(); pg.wait_for_timeout(420)
    ck('index is deep-linkable', pg.eval_on_selector('#boutiquesView','e=>e.classList.contains("show")'))

    head('headings clear the close button')
    # measure the rendered text, not the block box: an h2 always spans its column,
    # so a box comparison can never show the collision that padding-right fixes.
    TEXT = '''(sel)=>{const el=document.querySelector(sel);const r=document.createRange();
      r.selectNodeContents(el);return [...r.getClientRects()].map(x=>[x.left,x.right,x.top,x.bottom]);}'''
    collide = []
    for h,btn,h2 in [('#region=Vuori','#regionClose','#regionBody h2'),
                     ('#brand=Ralph%20Lauren%20Purple%20Label','#detailClose','#detailBody h2'),
                     ('#dial=scandi','#dialClose','#dialBody h2'),
                     ('#shop=nantucket-boat-basin-authentic-shop-nantucket-ma','#shopClose','#shopBody h2'),
                     ('#boutiques','#boClose','#boBody h2')]:
        pg.goto(url+h); pg.reload(); pg.wait_for_timeout(400)
        B = pg.eval_on_selector(btn,'e=>{const b=e.getBoundingClientRect();return [b.left,b.right,b.top,b.bottom]}')
        for L,R,T,Bo in pg.evaluate(TEXT, h2):
            if not (R <= B[0]+1 or Bo <= B[2] or T >= B[3]): collide.append(h); break
    ck('no overlay heading runs under its close button', not collide, collide)

    head('close buttons sit with the content')
    for h,btn,body in [('#brand=Peter%20Millar','#detailClose','#detailBody .dv-prose'),
                       ('#dial=scandi','#dialClose','#dialBody .dv-prose'),
                       ('#region=Southern%20Tide','#regionClose','#regionBody .rv-lead'),
                       ('#shop=blue-dry-goods-concord-ma','#shopClose','#shopBody p')]:
        pg.goto(url+h); pg.reload(); pg.wait_for_timeout(400)
        got = pg.eval_on_selector(btn,'e=>Math.round(e.getBoundingClientRect().right)')
        col = pg.eval_on_selector(body,'e=>Math.round(e.getBoundingClientRect().right)')
        ck(f'{btn} aligns with its column', abs(got-col)<=2, f'{got} vs {col}')
        ck(f'{btn} is on screen',
           pg.eval_on_selector(btn,'e=>{const b=e.getBoundingClientRect();return b.right<=innerWidth&&b.left>=0}'))

    head('release metadata')
    pg.goto(url+'#changes'); pg.reload(); pg.wait_for_timeout(450)
    cl = pg.eval_on_selector('#clBody','e=>e.innerText')
    ver = pg.evaluate('()=>VERSION')
    ck('the changelog has a newest entry', 'Version '+ver in cl, ver)
    ck('the stated current version matches it', 'Current version '+ver in cl, ver)
    ck('the footer shows the same version',
       'v'+ver in pg.eval_on_selector('footer','e=>e.innerText'), ver)
    ck('the build is not a dev tag', '-dev' not in ver, ver)

    head('the card stays with its brand')
    pg.goto(url); pg.reload(); pg.wait_for_timeout(500)
    t = [e for e in pg.query_selector_all('.brand') if e.inner_text().strip()=='Comme des Garçons'][0]
    t.scroll_into_view_if_needed(); pg.wait_for_timeout(150); t.click(); pg.wait_for_timeout(400)
    GAP = '''()=>{const c=document.getElementById('hoverCard').getBoundingClientRect();
      const e=[...document.querySelectorAll('.brand')].find(x=>x.textContent==='Comme des Garçons').getBoundingClientRect();
      return {gap: c.top>=e.bottom ? c.top-e.bottom : e.top-c.bottom,
              covers: !(c.bottom<=e.top+1||c.top>=e.bottom-1),
              onScreen: c.top>=-1 && c.bottom<=innerHeight+1};}'''
    drift = []
    for dy in [200, 400, -300]:
        pg.evaluate(f'()=>scrollBy(0,{dy})'); pg.wait_for_timeout(330)
        m = pg.evaluate(GAP)
        if m['gap'] > 40 or m['covers'] or not m['onScreen']: drift.append((dy, m))
    ck('it re-anchors on scroll rather than floating away', not drift, drift[:2])
    pg.set_viewport_size({'width':760,'height':700}); pg.wait_for_timeout(420)
    ck('it stays on screen after a resize',
       pg.eval_on_selector('#hoverCard','e=>{const b=e.getBoundingClientRect();return b.left>=-1&&b.right<=innerWidth+1}'))
    pg.set_viewport_size({'width':1257,'height':1000}); pg.wait_for_timeout(300)
    pg.keyboard.press('Escape'); pg.wait_for_timeout(250)
    ck('the beta badge sits inside its dial pill',
       pg.evaluate('''()=>{const d=document.querySelector('.dial[data-attr="shoes"]');
         return d.querySelector('.proto').getBoundingClientRect().right <= d.getBoundingClientRect().right;}'''))
    ck('the masthead lines up with the rail',
       abs(pg.eval_on_selector('h1','e=>e.getBoundingClientRect().left')
           - pg.eval_on_selector('.legend','e=>e.getBoundingClientRect().left')) < 2)

    head('contrast and the pinned card')
    # Own page: both this block and the next assert on document.body state, and a page
    # carried through forty navigations can arrive with an overlay or a pinned card
    # still showing. A fresh context is the only way these mean what they say.
    pgs = b.new_page(viewport={'width':1257,'height':1000})
    _pg_outer = pg; pg = pgs
    pg.goto(url); pg.wait_for_timeout(550)
    ck('True Luxury opens dark enough for cream text',
       'rgb(94, 112, 80)' in pg.eval_on_selector('.band--true','e=>getComputedStyle(e).backgroundImage'))
    pg.goto(url); pg.reload(); pg.wait_for_timeout(450)
    pg.eval_on_selector_all('.brand',"e=>e.find(x=>x.textContent==='Prada').click()")
    pg.wait_for_timeout(420)
    ck('the card is a dialog, not a tooltip',
       pg.eval_on_selector('#hoverCard','e=>e.getAttribute("role")')=='dialog')
    ck('the pill withdraws for a pinned card',
       pg.eval_on_selector('.search-float','e=>getComputedStyle(e).display')=='none')
    pg.keyboard.press('Escape'); pg.wait_for_timeout(330)
    ck('escape closes the card from anywhere',
       not pg.eval_on_selector('#hoverCard','e=>e.classList.contains("show")'))
    ck('the dismissed card leaves no brand selected',
       pg.eval_on_selector_all('.brand[aria-selected="true"]','e=>e.length')==0)
    ck('the pill comes back', pg.eval_on_selector('.search-float','e=>getComputedStyle(e).display')!='none')
    pg.eval_on_selector('.clearall','e=>e.focus()')
    ck('clear all has a visible focus ring',
       pg.eval_on_selector('.clearall','e=>getComputedStyle(e).outlineColor')!='rgb(18, 59, 43)')

    head('search pill is the map\'s alone')
    pg.goto(url); pg.reload(); pg.wait_for_timeout(430)
    ck('visible on the map', pg.eval_on_selector('.search-float','e=>getComputedStyle(e).display!=="none"'))
    hidden = []
    for h in ['#brand=Peter%20Millar','#dial=prep','#region=Peter%20Millar',
              '#shop=blue-dry-goods-concord-ma','#boutiques','#prices','#changes']:
        pg.goto(url+h); pg.reload(); pg.wait_for_timeout(400)
        if pg.eval_on_selector('.search-float','e=>getComputedStyle(e).display!=="none"'):
            hidden.append(h)
    ck('hidden behind every overlay', not hidden, hidden)
    pg.goto(url+'#brand=Peter%20Millar'); pg.reload(); pg.wait_for_timeout(400)
    pg.keyboard.press('Escape'); pg.wait_for_timeout(350)
    ck('returns when the overlay closes',
       pg.eval_on_selector('.search-float','e=>getComputedStyle(e).display!=="none"'))

    pg.close(); pg = _pg_outer

    head('routing and overlays')
    for h,sel in [('#prices','#pricesView'),('#changes','#changelog'),('#brand=Barbour','#detailView'),('#dial=prep','#dialView')]:
        pg.goto(url+h); pg.wait_for_timeout(330)
        ck(f'{h} opens {sel}', pg.eval_on_selector(sel,'e=>e.classList.contains("show")'), h)
    # a hash-only goto does not reload, so the brand card from the previous step is
    # still open behind the dial. Reload first to test a dial opened on its own.
    pg.reload(); pg.wait_for_timeout(400)
    pg.keyboard.press('Escape'); pg.wait_for_timeout(250)
    ck('escape clears the dial hash', pg.evaluate('location.hash')=='', pg.evaluate('location.hash'))

    head('search and did-you-mean (editDist untouched)')
    # Escape cleared the hash, so goto(url) is a same-URL navigation and does not
    # reload — any overlay still showing would keep the search pill hidden, which is
    # correct behaviour and made this block fail on an invisible input.
    # Typed through the DOM, not pg.fill: the pill correctly hides behind any overlay,
    # so a visibility-dependent fill hung on state left by an earlier block.
    pg.goto('about:blank'); pg.goto(url); pg.wait_for_timeout(600)
    pg.evaluate('''()=>{const e=document.getElementById("brandSearch");
      e.value="barbor"; e.dispatchEvent(new Event("input",{bubbles:true}));}'''); pg.wait_for_timeout(420)
    ac = pg.eval_on_selector_all('.ac-item','e=>e.map(x=>x.textContent)')
    ck('fuzzy search still suggests', any('Barbour' in x for x in ac), ac[:3])
    pg.evaluate('''()=>{const e=document.getElementById("brandSearch");
      e.value="sams"; e.dispatchEvent(new Event("input",{bubbles:true}));}'''); pg.wait_for_timeout(400)
    ac2 = pg.eval_on_selector_all('.ac-item','e=>e.map(x=>x.textContent)')
    ck('new brand is searchable', any('Sams' in x for x in ac2), ac2[:3])

    head('keyboard reaches the explainer')
    pg.goto(url); pg.wait_for_timeout(400)
    # dials in the collapsed Fabric/Culture groups are not focusable until opened,
    # which is ordinary <details> behaviour — open them before testing the keyboard.
    pg.evaluate('()=>{document.querySelectorAll(".grp").forEach(d=>d.open=true)}'); pg.wait_for_timeout(200)
    pg.focus('.dial[data-attr="tech"] .dl'); pg.keyboard.press('Enter'); pg.wait_for_timeout(320)
    ck('Enter on a dial label opens it', pg.eval_on_selector('#dialView','e=>e.classList.contains("show")'))
    pg.keyboard.press('Escape'); pg.wait_for_timeout(200)
    pg.focus('.dial[data-attr="prep"] .dl'); pg.keyboard.press(' '); pg.wait_for_timeout(320)
    ck('Space on a dial label opens it', pg.eval_on_selector('#dialView','e=>e.classList.contains("show")'))
    ck('label has a button role', pg.eval_on_selector('.dial[data-attr="prep"] .dl','e=>e.getAttribute("role")')=='button')
    ck('label reachable by tab', pg.eval_on_selector('.dial[data-attr="prep"] .dl','e=>e.getAttribute("tabindex")')=='0')

    head('sheet opens at the top')
    pg.set_viewport_size({'width':390,'height':844})
    pg.goto(url); pg.reload(); pg.wait_for_timeout(500)
    pg.click('.brand:has-text("Hiroshi Kato")'); pg.wait_for_timeout(300)
    pg.evaluate("document.getElementById('hoverCard').scrollTop=400"); pg.wait_for_timeout(100)
    pg.click('#hoverCard .hc-close'); pg.wait_for_timeout(200)
    pg.click('.brand:has-text("Sugar Cane")'); pg.wait_for_timeout(300)
    ck('a second card on the phone opens scrolled to the top', pg.evaluate("document.getElementById('hoverCard').scrollTop")==0)
    ck('the card carries the details link in its header', pg.evaluate("!!document.querySelector('#hoverCard .hc-head a.detail-link')"))
    ck('the header holds the close button beside the link', pg.evaluate("!!document.querySelector('#hoverCard .hc-head .hc-close')"))
    ck('no card foot remains', pg.evaluate("!document.querySelector('#hoverCard .hc-foot')"))

    head('golfiness dial')
    pg.set_viewport_size({'width':1400,'height':1000})
    pg.goto(url); pg.reload(); pg.wait_for_timeout(500)
    ck('golfiness dial is on the rail', pg.evaluate("!!document.querySelector('.dial[data-attr=\"golf\"] input[type=range]')"))
    pg.evaluate("()=>{const d=document.querySelector('.dial[data-attr=\"golf\"] input[type=range]'); d.value=5; d.dispatchEvent(new Event('input',{bubbles:true})); d.dispatchEvent(new Event('change',{bubbles:true}));}")
    pg.wait_for_timeout(300)
    shown = pg.evaluate("[...document.querySelectorAll('.brand:not(.out)')].map(b=>b.textContent.trim())")
    want = pg.evaluate("[...document.querySelectorAll('.brand')].filter(b=>+b.dataset.golf===5).map(b=>b.textContent.trim())")
    ck('golfiness at 5 shows exactly the brands scored 5', sorted(shown)==sorted(want), f'{len(shown)} shown vs {len(want)} scored')
    ck('golfiness at 5 shows the pro-shop natives', all(b in shown for b in ['Rhoback','Criquet','Malbon','Peter Millar']))
    pg.evaluate("()=>{const d=document.querySelector('.dial[data-attr=\"golf\"] input[type=range]'); d.value=0; d.dispatchEvent(new Event('input',{bubbles:true})); d.dispatchEvent(new Event('change',{bubbles:true}));}")

    head('the range, measured')
    pg.set_viewport_size({'width':1400,'height':1000})
    pg.goto(url+'#brand=PAIGE'); pg.reload(); pg.wait_for_timeout(400)
    fl = pg.evaluate("document.querySelector('#detailBody .fibre-line')?.innerText || ''")
    ck('PAIGE range line carries the cellulosic figure', '34% cellulosic' in fl, fl[:80])
    ck('PAIGE range line carries both stretch numbers', 'stretch in 55%' in fl and 'performance stretch in 2%' in fl, fl[:120])
    # Derived from the data: the first brand under 50% coverage, whichever it is this build.
    low = pg.evaluate("()=>{for(const [k,f] of Object.entries(FIBRE)){ if(f.t && f.w/f.t<0.5) return [k, Math.round(100*f.w/f.t)]; } return null}")
    ck('the map still holds a low-coverage house to test against', low is not None)
    pg.goto(url+'#brand='+low[0].replace(' ','%20')); pg.reload(); pg.wait_for_timeout(400)
    fl = pg.evaluate("document.querySelector('#detailBody .fibre-line')?.innerText || ''")
    ck('a low-coverage range line says how many state a composition', f'{low[1]}% state a composition' in fl, fl[-90:])
    ck('a low-coverage house has no natural dial', pg.evaluate("n=>[...document.querySelectorAll('.brand')].find(b=>b.textContent.trim()===n).dataset.natural", low[0])=='99')
    pg.goto(url+"#brand=Rothy%27s"); pg.reload(); pg.wait_for_timeout(400)
    fl = pg.evaluate("document.querySelector('#detailBody .fibre-line')?.innerText || ''")
    ck("Rothy's counted zero reads as a finding", 'no men' in fl and 'zero is the finding' in fl, fl[:80])
    ck('natural dial derived for the seven at their old bands', pg.evaluate("[...document.querySelectorAll('.brand')].filter(b=>['J.Crew','Merz b. Schwanen','Todd Snyder','Loro Piana'].includes(b.textContent.trim())).every(b=>b.dataset.natural==='5')"))
    ck('natural dial covers most of the map now', pg.evaluate("[...document.querySelectorAll('.brand')].filter(b=>b.dataset.natural!=='99').length")>=190)

    head('lead line')
    pg.set_viewport_size({'width':1400,'height':1000})
    pg.goto(url); pg.reload(); pg.wait_for_timeout(500)
    lines = pg.evaluate("[...document.querySelectorAll('.brand')].map(b=>traitLine(b))")
    ck('every card lead line has one to three clauses', all(1 <= l.count(' · ')+1 <= 3 for l in lines), [l for l in lines if l.count(' · ')+1 > 3][:2])
    ck('no lead line carries the filler clauses', not any(x in l for l in lines for x in ('national reach','works in both','sold everywhere','accommodating')))
    ck('the page keeps the full trait line', pg.evaluate("typeof traitLineFull==='function'"))

    head('why cards reachable on a phone')
    pg.set_viewport_size({'width':390,'height':844})
    pg.goto(url); pg.reload(); pg.wait_for_timeout(500)
    pg.evaluate("()=>{const d=document.querySelector('.dial[data-attr=\"avant\"] input[type=range]'); d.value=5; d.dispatchEvent(new Event('input',{bubbles:true})); d.dispatchEvent(new Event('change',{bubbles:true}));}")
    pg.wait_for_timeout(600)
    shown = pg.evaluate("!document.getElementById('whyPanel').hidden && document.querySelectorAll('.whycard').length>0")
    ck('dragging a dial to 5 on a phone shows why cards', shown)
    ck('the why panel does not scroll inside itself on a phone', pg.evaluate("getComputedStyle(document.getElementById('whyPanel')).overflowY")!='auto')
    ck('the last why card sits inside the document height, not a clipped box', pg.evaluate("()=>{const c=[...document.querySelectorAll('.whycard')].pop(); const r=c.getBoundingClientRect(); return r.bottom + window.scrollY <= document.documentElement.scrollHeight + 1}"))
    pg.evaluate("()=>{const d=document.querySelector('.dial[data-attr=\"avant\"] input[type=range]'); d.value=0; d.dispatchEvent(new Event('input',{bubbles:true})); d.dispatchEvent(new Event('change',{bubbles:true}));}")

    head('garment labels shop')
    pg.set_viewport_size({'width':1400,'height':1000})
    pg.goto(url+'#brand=Todd%20Snyder'); pg.reload(); pg.wait_for_timeout(400)
    links = pg.evaluate("[...document.querySelectorAll('#detailBody .pr-lab a.gl-link')].map(a=>[a.textContent, a.href])")
    npriced = pg.evaluate("PRICES['Todd Snyder'].filter(Array.isArray).length")
    ck('priced garment labels link to the brand site search', len(links)==npriced and all('toddsnyder' in h for _,h in links), f'{len(links)} links, {npriced} priced')
    ck('unpriced garment labels stay plain', pg.evaluate("[...document.querySelectorAll('#detailBody .pr-row')].filter(r=>r.textContent.includes('not assessed')).every(r=>!r.querySelector('a'))"))
    pg.goto(url+'#brand=Tecovas'); pg.reload(); pg.wait_for_timeout(400)
    ck('the Shoes label uses the curated shoe link where one exists', pg.evaluate("document.querySelectorAll('#detailBody .pr-row')[7].querySelector('a')?.href")=='https://www.tecovas.com/search?q=Cartwright%20boot')
    pg.goto(url); pg.reload(); pg.wait_for_timeout(400); pg.hover('.brand:has-text("Todd Snyder")'); pg.wait_for_timeout(600)
    ck('card garment labels link too', pg.evaluate("document.querySelectorAll('#hoverCard .hp-name a.gl-link').length")==npriced)
    ck('the separate Shoes line is gone from the card', pg.evaluate("!document.querySelector('#hoverCard .hc-shoe')"))

    head('prev / next')
    pg.set_viewport_size({'width':1400,'height':1000})
    pg.goto(url+'#brand=Barbour'); pg.reload(); pg.wait_for_timeout(420)
    nav = pg.evaluate("()=>{const n=document.querySelector('#detailBody .pg-nav'); return n? {prev:n.querySelector('.pg-prev')?.dataset.brand, next:n.querySelector('.pg-next')?.dataset.brand, at:n.querySelector('.pg-at').textContent} : null}")
    ck('brand page carries a prev/next nav', nav is not None)
    order = pg.evaluate("()=>[...document.querySelectorAll('.brand')].map(b=>b.textContent.trim())")
    i = order.index('Barbour')
    ck('brand next follows the spectrum order', nav and nav['next']==order[i+1], f"{nav and nav['next']} vs {order[i+1]}")
    ck('brand prev follows the spectrum order', nav and nav['prev']==order[i-1], f"{nav and nav['prev']} vs {order[i-1]}")
    ck('brand nav says where it is', nav and nav['at']==f'{i+1} of {len(order)}', nav and nav['at'])
    pg.click('#detailBody .pg-nav a.pg-next'); pg.wait_for_timeout(250)
    ck('clicking next opens the next brand', pg.evaluate("document.querySelector('#detailBody h2').textContent").startswith(order[i+1]))
    ck('clicking next moves the hash', pg.evaluate('location.hash')=='#brand='+order[i+1].replace(' ','%20').replace("'", '%27'), pg.evaluate('location.hash'))
    pg.keyboard.press('ArrowLeft'); pg.wait_for_timeout(250)
    ck('arrow left goes back', pg.evaluate("document.querySelector('#detailBody h2').textContent").startswith('Barbour'))
    first = order[0]
    pg.goto(url+'#brand='+first.replace(' ','%20').replace("'", '%27')); pg.reload(); pg.wait_for_timeout(400)
    ck('first brand has no prev link, only an end marker', pg.evaluate("()=>!document.querySelector('#detailBody .pg-nav a.pg-prev') && !!document.querySelector('#detailBody .pg-nav .pg-end')"))
    # shops: open the first shop in the boutiques index and step
    pg.goto(url+'#stores=shop'); pg.reload(); pg.wait_for_timeout(500)
    slugs = pg.evaluate("()=>[...document.querySelectorAll('#boBody a.shop-open')].map(a=>a.dataset.i)")
    ck('boutiques index has shops', len(slugs)>2)
    pg.click('#boBody a.shop-open'); pg.wait_for_timeout(300)
    snav = pg.evaluate("()=>{const n=document.querySelector('#shopBody .pg-nav'); return n? {next:n.querySelector('.pg-next')?.dataset.shop, at:n.querySelector('.pg-at').textContent} : null}")
    ck('stockist page carries a prev/next nav', snav is not None)
    ck('stockist next follows the boutiques index order', snav and snav['next']==slugs[1], f"{snav and snav['next']} vs {slugs[1]}")
    ck('stockist nav says where it is', snav and snav['at']==f'1 of {len(slugs)}', snav and snav['at'])
    pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(250)
    ck('arrow right pages the stockist view, not the brand view', pg.evaluate("location.hash")=='#shop='+slugs[1], pg.evaluate('location.hash'))
    names = pg.evaluate("()=>[...document.querySelectorAll('#boBody .bo-name')].map(e=>e.firstChild.textContent.trim().toLowerCase())")
    ck('boutiques index is alphabetical', names==sorted(names), f'{[n for n,m in zip(names,sorted(names)) if n!=m][:3]}')
    ck('every boutique row carries a region tag', pg.evaluate("[...document.querySelectorAll('#boBody .bo-line')].every(l=>l.querySelector('.bo-region')?.textContent.trim())"))
    pg.evaluate("shopView.classList.remove('show')")   # the prev/next check left a shop page open
    pg.click("#boBody .bo-region[data-region='South Shore']"); pg.wait_for_timeout(300)
    ck('tapping a region tag filters the index to that region', pg.evaluate("[...document.querySelectorAll('#boBody .bo-region')].every(e=>e.textContent==='South Shore') && document.querySelectorAll('#boBody .bo-line').length>=3"))
    ck('the filtered index sets a shareable hash', pg.evaluate('location.hash')=='#stores=south-shore+shop')
    rl = pg.evaluate("[...document.querySelectorAll('#boBody a.bo-route')].map(a=>a.href)")
    ck('a region view offers a Google Maps route', len(rl)==1 and rl[0].startswith('https://www.google.com/maps/dir/'))
    pg.goto(url+'#stores'); pg.reload(); pg.wait_for_timeout(400)
    ck('the full index offers no route', pg.evaluate("document.querySelectorAll('#boBody a.bo-route').length")==0)
    pg.goto(url+'#stores=south-shore+shop'); pg.reload(); pg.wait_for_timeout(400)
    ck('the route carries every shop in the region as a stop', rl and rl[0].count('/')-4==pg.evaluate("document.querySelectorAll('#boBody .bo-line').length"), rl and rl[0].count('/')-4)
    # Derived: the largest region by shop count, whatever it is this build.
    big = pg.evaluate("()=>{const c={}; PLACES.filter(p=>p.k==='s').forEach(p=>{const r=SUBREGION[p.s+'|'+p.c]; c[r]=(c[r]||0)+1}); const e=Object.entries(c).sort((a,b)=>b[1]-a[1])[0]; return [e[0], e[1]]}")
    pg.goto(url+'#stores='+big[0].lower().replace(' ','-')+'+shop'); pg.reload(); pg.wait_for_timeout(500)
    rl2 = pg.evaluate("[...document.querySelectorAll('#boBody a.bo-route')].map(a=>a.href)")
    ck('the largest region splits into legs of at most ten', len(rl2)==-(-big[1]//10) and all(0 < h.count('/')-4 <= 10 for h in rl2), [h.count('/')-4 for h in rl2])
    pg.goto(url+'#stores=south-shore+shop'); pg.reload(); pg.wait_for_timeout(500)
    pg.click('#boBody a.bo-all'); pg.wait_for_timeout(300)
    ck('show all restores the whole index', pg.evaluate("document.querySelectorAll('#boBody .bo-line').length")==len(slugs))
    pg.click("#boBody button.bo-kind[data-kind='all']"); pg.wait_for_timeout(300)
    nAll = pg.evaluate("document.querySelectorAll('#boBody .bo-line').length"); nOwn = pg.evaluate("document.querySelectorAll('#boBody .bo-line.bo-own').length")
    ck('the All filter shows both kinds', nAll==pg.evaluate("PLACES.filter(p=>p.k==='s'||p.k==='o').length") and nOwn>0, f'{nAll} rows, {nOwn} own')
    ck('a brand store row opens the brand page', pg.evaluate("document.querySelector('#boBody .bo-own a.bo-row').getAttribute('href').startsWith('#brand=')"))
    pg.click("#boBody button.bo-kind[data-kind='own']"); pg.wait_for_timeout(300)
    ck('Brand stores filter shows only own stores', pg.evaluate("[...document.querySelectorAll('#boBody .bo-line')].every(l=>l.classList.contains('bo-own'))") and pg.evaluate('location.hash')=='#stores=own')
    ck('every store row of either kind carries a region tag', pg.evaluate("[...document.querySelectorAll('#boBody .bo-line')].every(l=>l.querySelector('.bo-region')?.textContent.trim())"))
    pg.goto(url+'#boutiques'); pg.reload(); pg.wait_for_timeout(400)
    ck('the old #boutiques hash still opens the index', pg.evaluate("boutiquesView.classList.contains('show')"))
    pg.goto(url+'#stores=shop'); pg.reload(); pg.wait_for_timeout(500)
    pg.goto(url+'#stores=the-cape+shop'); pg.reload(); pg.wait_for_timeout(500)
    ck('a region hash opens the index filtered', pg.evaluate("document.querySelector('#boBody h2').textContent")=='The Cape')
    pg.goto(url+'#stores=shop'); pg.reload(); pg.wait_for_timeout(500)
    ck('Louie is tagged South Shore', pg.evaluate("[...document.querySelectorAll('#boBody .bo-line')].find(l=>l.textContent.includes('Louie'))?.querySelector('.bo-region').textContent")=='South Shore')

    head('phone')
    # a real touch context, so pointer:coarse rules are exercised as on a phone
    pg2 = b.new_page(viewport={'width':390,'height':844}, is_mobile=True, has_touch=True); e2=[]
    pg2.on('pageerror', lambda e: e2.append(str(e)))
    pg2.goto(url+'#dial=briish'); pg2.wait_for_timeout(600)
    ck('phone: explainer opens', pg2.eval_on_selector('#dialView','e=>e.classList.contains("show")'))
    ck('phone: no horizontal overflow',
       pg2.evaluate('document.getElementById("dialBody").scrollWidth <= document.getElementById("dialView").clientWidth'))
    pg2.goto(url); pg2.wait_for_timeout(500)
    ck('phone: map renders', pg2.eval_on_selector_all('.brand','e=>e.length')==expected)
    ck('phone: no horizontal overflow',
       not pg2.evaluate('()=>document.documentElement.scrollWidth>innerWidth'))
    # opening the regional panel from the sheet should not leave the sheet behind
    pg2.goto(url); pg2.reload(); pg2.wait_for_timeout(550)
    pg2.evaluate("()=>{const e=[...document.querySelectorAll('.brand')].find(x=>x.textContent==='Peter Millar');e.scrollIntoView({block:'center'});e.click();}")
    pg2.wait_for_timeout(500)
    ck('phone: the brand sheet opens', pg2.eval_on_selector('#hoverCard','e=>e.classList.contains("show")'))
    pg2.eval_on_selector('#hoverCard .region-btn','e=>e.click()'); pg2.wait_for_timeout(500)
    ck('phone: the sheet slides away when the panel opens',
       not pg2.eval_on_selector('#hoverCard','e=>e.classList.contains("show")')
       and pg2.eval_on_selector('#regionView','e=>e.classList.contains("show")'))
    ck('phone: the slide transform is cleaned up',
       pg2.eval_on_selector('#hoverCard','e=>e.style.transform')=='')
    pg2.keyboard.press('Escape'); pg2.wait_for_timeout(350)
    pg2.goto(url+'#boutiques'); pg2.wait_for_timeout(450)
    ck('phone: report actions are thumb-sized',
       pg2.eval_on_selector('#boutiquesView .bo-report','e=>e.getBoundingClientRect().height')>=36)
    ck('phone: the action holds its line while the name wraps',
       pg2.evaluate('''()=>[...document.querySelectorAll('#boutiquesView .bo-line')].every(l=>{
         const n=l.querySelector('.bo-name').getBoundingClientRect();
         const b=l.querySelector('.bo-report').getBoundingClientRect();
         return b.left >= n.right - 1;})'''))
    ck('phone: report actions are all present',
       pg2.eval_on_selector_all('#boutiquesView .bo-report','e=>e.length')==
       pg2.eval_on_selector_all('#boutiquesView .bo-line','e=>e.length'))
    ck('phone: no page errors', not e2, e2)

    ck('no page errors anywhere', not errs, errs[:3])
    b.close()

print('\n' + '='*60)
print(f'{checks[0]} checks, {len(fails)} failures')
for f in fails: print('  FAIL', f)
sys.exit(1 if fails else 0)
