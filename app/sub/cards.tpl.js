/* Brand cards for the companion pages (overlaps, CAKE and Croissant, WS centers).
   Built by tools/build_womens.py into app/sub/cards.js. The shared pieces (store tree, About block, social and
   link rows, helpers) are copied from app/womens_template.html at build time, so the cards stay in step with the
   Explorer. The brand data (cards_data.js, same folder) loads on the first click.
   A page marks a brand with data-brand="Name" and may define window.cardCtx(name) -> {lists:[], centers:[], ig, tt}. */
(function(){
'use strict';
const SRC=(document.currentScript&&document.currentScript.src)||location.href;
/*__SHARED__*/
const TIERNAME={Basic:'Tier 1',Premium:'Tier 2',Accessible:'Tier 3','True Luxury':'Tier 4',Pending:'Prices to come'};
const bandName=b=>TIERNAME[b]||b;
let NE=new Set(), DATA=null, IDX=null, ALIAS={}, loading=null;
function fold(x){
  x=String(x||'').normalize('NFKD').replace(/[̀-ͯ]/g,'').replace(/[^\x00-\x7f]/g,'').toLowerCase().replace(/&/g,'and').replace(/\+/g,'and');
  x=x.trim().replace(/^the /,'').replace(/[^a-z0-9]/g,'');
  return ALIAS[x]||x;}
function load(){
  if(DATA) return Promise.resolve(); if(loading) return loading;
  loading=new Promise((ok,bad)=>{const s=document.createElement('script'); s.src=new URL('cards_data.js',SRC).href;
    s.onload=()=>{DATA=window.CX_DATA; ALIAS=DATA.alias||{}; NE=new Set(DATA.ne||[]); IDX={};
      for(const b of DATA.brands) IDX[fold(b.n)]=['b',b];
      for(const o of DATA.other) if(!IDX[fold(o.n)]) IDX[fold(o.n)]=['o',o];
      for(const [k,v] of Object.entries(DATA.keys||{})) if(!IDX[k]&&IDX[v]) IDX[k]=IDX[v];
      ok();};
    s.onerror=bad; document.head.appendChild(s);});
  return loading;}
const CSS=`
#cxov{position:fixed;inset:0;background:rgba(30,30,27,.28);display:none;z-index:900}#cxov.show{display:block}
#cx{--cream:#F6F4EF;--ink:#1E1E1B;--ink-soft:#4E4C45;--ink-faint:#6B695F;--hairline:#DCD8CC;--green:#123B2B;--basic:#F2EEE2;--premium:#E9EFE7;--accessible:#E6EAF0;--trueLux:#EFE6E8;--pending:#EDEBE6;
  position:fixed;top:0;right:0;height:100%;width:min(720px,100%);background:var(--cream);color:var(--ink);z-index:901;transform:translateX(100%);transition:transform .25s;overflow-y:auto;padding:36px 32px 60px;box-shadow:-10px 0 30px rgba(0,0,0,.08);
  font-family:'Inter',system-ui,sans-serif;font-size:15px;line-height:1.55;text-align:left;-webkit-font-smoothing:antialiased;box-sizing:border-box}
#cx *{box-sizing:border-box;margin:0;padding:0}#cx.show{transform:none}
#cx .close{position:absolute;top:18px;right:20px;background:var(--green);color:#fff;border:0;border-radius:999px;padding:8px 18px;font:inherit;font-size:13px;cursor:pointer}
#cx h2{font-family:'Prata',Georgia,serif;font-weight:400;font-size:30px;line-height:1.1;margin:8px 90px 4px 0;color:var(--ink)}
#cx h3{font-family:'Prata',Georgia,serif;font-weight:400;font-size:17px;margin:18px 0 8px}
#cx h4{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-faint);margin:12px 0 6px;font-weight:500}
#cx a{color:var(--green)}
#cx .pill{display:inline-block;padding:4px 11px;border-radius:999px;font-size:12px;font-weight:600;margin:6px 6px 0 0;background:var(--pending);color:var(--ink-soft)}
#cx .pill.Basic{background:var(--basic)}#cx .pill.Premium{background:var(--premium)}#cx .pill.Accessible{background:var(--accessible)}#cx .pill.True{background:var(--trueLux)}#cx .pill.none{background:transparent;border:1px solid var(--hairline);font-weight:500}
#cx .basis{font-size:12.5px;color:var(--ink-faint);margin:8px 0 14px}
#cx .kv{display:grid;grid-template-columns:auto 1fr;gap:4px 14px;font-size:13.5px;margin:0 0 16px}#cx .kv dt{color:var(--ink-faint)}#cx .kv dd{color:var(--ink)}
#cx .lkc{font-size:11.5px;color:var(--ink-faint)}#cx dd.lk .sep{color:var(--ink-faint)}
#cx .prices{display:grid;grid-template-columns:repeat(4,1fr);gap:6px 14px;font-size:13px;margin:0 0 16px}
#cx .prices div span{display:block;font-size:11px;color:var(--ink-faint);letter-spacing:.03em;text-transform:uppercase}
#cx .prices div a{display:block;font-size:11px;text-decoration:none;margin-top:1px}
#cx .muted{color:var(--ink-faint)}#cx .sells{font-size:14px;line-height:1.5;margin:0 0 10px}
#cx .q{margin:4px 0 18px;padding:10px 14px;border-left:2px solid var(--green);font-family:'Playfair Display',Georgia,serif;font-style:italic;font-size:15px;line-height:1.5}
#cx .q cite{display:block;font-family:Inter,system-ui,sans-serif;font-style:normal;font-size:11.5px;color:var(--ink-faint);margin-top:6px}
#cx .dg{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2px 24px;margin:0 0 6px}
#cx .dm summary{display:grid;grid-template-columns:minmax(0,1fr) auto 18px;align-items:center;gap:10px;padding:7px 0;border-bottom:1px solid var(--hairline);cursor:pointer;list-style:none;font-size:13px}
#cx .dm summary::-webkit-details-marker{display:none}#cx .dm[data-empty] summary{cursor:default}
#cx .dm .dk{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#cx .dm .mt{display:flex;gap:3px}#cx .dm .mt i{display:block;width:16px;height:6px;border-radius:3px;background:var(--hairline)}#cx .dm .mt i.on{background:var(--green)}#cx .dm.five .mt i.on{background:#B9962F}
#cx .dm b{font-weight:600;font-size:12.5px;text-align:right;color:var(--ink-soft)}
#cx .dm p{font-size:12px;line-height:1.5;color:var(--ink-soft);margin:0 0 8px;padding:0 0 10px;border-bottom:1px solid var(--hairline)}
#cx .dm:not([data-empty]) .dk::after{content:" ›";color:var(--ink-faint)}#cx .dm[open] .dk::after{content:" ⌄"}
#cx .dhint{font-size:11.5px;color:var(--ink-faint);margin:8px 0 16px;line-height:1.5}
#cx .tree summary{display:flex;justify-content:space-between;align-items:baseline;cursor:pointer;list-style:none;padding:9px 0;border-bottom:1px solid var(--hairline)}
#cx .tree summary::-webkit-details-marker{display:none}
#cx .tree summary span::before{content:"▸";display:inline-block;width:14px;color:var(--ink-faint);transition:transform .15s}
#cx .tree details[open]>summary span::before{transform:rotate(90deg)}
#cx .tree summary b,#cx .tree .dh b{font-weight:600;font-size:12.5px;color:var(--ink-soft)}
#cx .tree .rg>summary{font-family:'Prata',Georgia,serif;font-size:16px}
#cx .tree .stt{margin-left:14px}#cx .tree .stt>summary{font-size:13.5px;font-weight:500}
#cx .tree .ds{margin:6px 0 10px 28px}
#cx .tree .dh{display:flex;justify-content:space-between;font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-faint);padding:4px 0}
#cx .tree .dh .muted{text-transform:none;letter-spacing:0}
#cx .st{list-style:none}#cx .st li{display:flex;justify-content:space-between;gap:12px;padding:7px 0;border-bottom:1px solid var(--hairline);font-size:13.5px}
#cx .st li .where{color:var(--ink-faint);font-size:12.5px}
#cx .st li a{flex:none;border:1px solid var(--hairline);border-radius:999px;padding:4px 12px;font-size:12px;text-decoration:none;align-self:center}
#cx .note{font-size:12.5px;color:var(--ink-soft);margin:14px 0 0;line-height:1.5}
#cx .cav{font-size:12px;color:var(--ink-faint);margin:22px 0 0;line-height:1.5;border-top:1px solid var(--hairline);padding-top:12px}
#cx .ld{color:var(--ink-faint);font-size:13.5px;margin-top:30px}
[data-brand]{cursor:pointer}[data-brand]:hover{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}
@media (max-width:700px){#cx{padding:28px 18px 60px}#cx .prices{grid-template-columns:repeat(2,1fr)}}
@media (max-width:520px){#cx .dg{grid-template-columns:1fr}}`;
function ui(){
  if(document.getElementById('cx')) return;
  const st=document.createElement('style'); st.textContent=CSS; document.head.appendChild(st);
  if(!document.querySelector('link[href*="family=Prata"]')){const l=document.createElement('link'); l.rel='stylesheet'; l.href='https://fonts.googleapis.com/css2?family=Prata&family=Playfair+Display:ital@0;1&family=Inter:wght@400;500;600&display=swap'; document.head.appendChild(l);}
  const ov=document.createElement('div'); ov.id='cxov'; const p=document.createElement('aside'); p.id='cx'; p.setAttribute('aria-hidden','true');
  p.innerHTML='<button class="close" type="button">close</button><div id="cxb"></div>';
  document.body.appendChild(ov); document.body.appendChild(p);
  ov.onclick=close; p.querySelector('.close').onclick=close;
  document.addEventListener('keydown',e=>{if(e.key==='Escape')close();});}
function show(html){ui(); document.getElementById('cxb').innerHTML=html; const p=document.getElementById('cx'); p.scrollTop=0; p.classList.add('show'); p.setAttribute('aria-hidden','false'); document.getElementById('cxov').classList.add('show');}
function close(){const p=document.getElementById('cx'); if(!p) return; p.classList.remove('show'); p.setAttribute('aria-hidden','true'); document.getElementById('cxov').classList.remove('show');}
function ctxRows(c){const r=[];
  const ls=(c.lists||[]).filter(x=>!(x==='WS centers'&&c.centers&&c.centers.length)); if(ls.length) r.push(`<dt>On these lists</dt><dd>${ls.map(esc).join(', ')}</dd>`);
  if(c.centers&&c.centers.length) r.push(`<dt>WS centers</dt><dd>${c.centers.map(esc).join(', ')}</dd>`);
  return r.join('');}
function socFrom(c){const so={}; if(c.ig) so.ig=[c.ig,'',null]; if(c.tt) so.tt=[c.tt,'',null]; return (so.ig||so.tt)?so:null;}
function brandCard(b,c){
  const prices=b.prices?`<div class="prices">${Object.entries(b.prices).map(([g,v])=>`<div><span>${g}</span>${Array.isArray(v)?('$'+v[0]+(v[1]&&v[1]!==v[0]?'–'+v[1]:'')):esc(v)}${b.gl&&b.gl[g]?`<a href="${esc(b.gl[g])}" target="_blank" rel="noopener">see the range ↗</a>`:''}</div>`).join('')}</div>`:'';
  const FN={tech:'tech',comfort:'comfort',craft:'craft',style:'style'}, FAN={cotton:'cotton',silk:'silk',wool:'wool',cashmere:'cashmere',linen:'linen',denim:'denim',synth:'synthetic'};
  const nt0=b.nt||{}, nt={}; for(const k in nt0) nt[k]=String(nt0[k]||'').replace(/\s*—\s*seeded .*$/i,'').replace(/^seeded .*provisional.*$/i,'');
  const row=(lab,v,note)=>`<details class="dm${v===5?' five':''}"${note?'':' data-empty'}><summary><span class="dk">${esc(lab)}</span><span class="mt">${[1,2,3,4,5].map(x=>`<i class="${x<=v?'on':''}"></i>`).join('')}</span><b>${v}</b></summary>${note?`<p>${esc(note)}</p>`:''}</details>`;
  const focusRows=b.f?Object.entries(FN).filter(([k])=>b.f[k]!=null).map(([k,l])=>row(l,b.f[k],nt[k])).join(''):'';
  const fabRows=b.fa?[
      b.cf!=null?row('natural or lyocell',b.cf,'Share of styles made only of natural fibers or lyocell (Tencel), with no more than 5% stretch'+(b.cfl&&b.cfl!=='0'?'; '+b.cfl+' contain lyocell':'')+'.'):'',
      b.nat!=null?row('natural fibers',b.nat,'Share of styles that are mostly a natural fiber: 5 is all of them, 4 at least 95%, 3 at least 85%, 2 at least 70%.'):'',
      ...Object.entries(FAN).filter(([k])=>b.fa[k]!=null).map(([k,l])=>row(l,b.fa[k],nt[k]))].join(''):'';
  const dials=(b.f||b.fa)?`<h3>Dials</h3>${focusRows?`<div class="dg">${focusRows}</div>`:''}${fabRows?`<h4>Fabric</h4><div class="dg">${fabRows}</div>`:''}<p class="dhint">Tap a dial to see why.${b.fi?' '+esc(b.fi):''}</p>`:'';
  if(!b.so&&!(b.about)) b={...b,so:socFrom(c)};
  return `<h2>${esc(b.n)}</h2>
    <span class="pill ${b.band.split(' ')[0]}">${esc(bandName(b.band))}</span>
    ${b.sg?`<p class="basis" style="margin-bottom:4px"><b style="color:var(--ink)">${esc(b.sg)}</b>${b.sg2?` · also ${esc(b.sg2)}`:''}</p>`:''}
    <p class="basis">${esc(b.basis)}</p>
    <dl class="kv">
      <dt>Full-price stores</dt><dd>${b.own} in the US${b.ne?` · ${b.ne} in the Northeast`:''}</dd>
      ${b.out?`<dt>Outlets</dt><dd>${b.out}</dd>`:''}
      ${b.con?`<dt>Shops in department stores</dt><dd>${b.con}</dd>`:''}
      ${b.locator?`<dt>Store finder</dt><dd><a href="${esc(b.locator)}" target="_blank" rel="noopener">${esc(b.locator.replace(/^https?:\/\//,'').slice(0,60))}</a></dd>`:''}
      ${ctxRows(c)}
      ${b.read?`<dt>Checked</dt><dd>${esc(fmtDate(b.read))}</dd>`:''}
      ${!b.about&&b.so?soRow(b.so):''}
    </dl>
    ${aboutHtml(b)}
    ${dials}
    ${prices?'<h3>Starting and top prices</h3>'+prices:''}
    ${b.stores.length?'<h3>Stores</h3>'+storeTree(b):'<p class="note">Stores are counted but not addressed for this brand.</p>'}
    ${b.note?`<p class="note">${esc(b.note)}</p>`:''}
    <p class="cav">From The Cyprus Brand Explorer. Full-price stores from the brand’s own website. Outlets and pop-ups aren’t included.</p>`;}
function otherCard(o,c){const so=o.so||socFrom(c);
  return `<h2>${esc(o.n)}</h2><span class="pill">${esc(CATN[o.cat]||o.cat)}</span>
    <dl class="kv" style="margin-top:14px"><dt>Full-price stores</dt><dd>${o.own==null?'Count coming':o.none?'None of its own in the US; sold through other stores':o.own+' in the US'}</dd>
    ${o.locator?`<dt>Store finder</dt><dd><a href="${esc(o.locator)}" target="_blank" rel="noopener">${esc(o.locator.replace(/^https?:\/\//,'').slice(0,60))}</a></dd>`:''}${ctxRows(c)}${o.read?`<dt>Checked</dt><dd>${esc(fmtDate(o.read))}</dd>`:''}${so?soRow(so):''}${o.lk?lkRows(o.lk).join(''):''}</dl>
    ${o.stores.length?'<h3>Stores</h3>'+storeTree(o):''}
    <p class="cav">From The Cyprus Brand Explorer’s other brands. Stores under the brand’s own name, from its website. Counters inside department stores aren’t included.</p>`;}
function basicCard(n,c){const k=fold(n), s=(DATA.soc||{})[k], so=s||socFrom(c);
  return `<h2>${esc(n)}</h2><span class="pill none">Not on the Brand Explorer</span>
    <dl class="kv" style="margin-top:14px">${ctxRows(c)}${so?soRow(so):'<dt>Social</dt><dd class="muted">No handles on file yet</dd>'}</dl>
    <p class="cav">This brand isn’t on The Cyprus Brand Explorer yet, so there are no stores or prices for it here.</p>`;}
async function open(n){
  const c=(typeof window.cardCtx==='function'&&window.cardCtx(n))||{};
  if(!DATA){show(`<h2>${esc(n)}</h2><p class="ld">Loading…</p>`); try{await load();}catch(e){show(`<h2>${esc(n)}</h2><p class="ld">The brand data didn’t load. Try again in a moment.</p>`); loading=null; return;}}
  const hit=IDX[fold(n)];
  show(!hit?basicCard(n,c):hit[0]==='b'?brandCard(hit[1],c):otherCard(hit[1],c));}
document.addEventListener('click',e=>{const el=e.target.closest('[data-brand]'); if(!el||e.target.closest('#cx')) return; if(e.target.closest('a[href]')&&!e.target.closest('a[href]').hasAttribute('data-brand')) return; e.preventDefault(); open(el.getAttribute('data-brand'));});
document.addEventListener('keydown',e=>{if(e.key!=='Enter') return; const el=e.target.closest&&e.target.closest('[data-brand]'); if(el){e.preventDefault(); open(el.getAttribute('data-brand'));}});
window.Cards={open,close};
})();
