// Batch 3 Shopify helper (Chrome). Paste on the brand's origin, then:
//   await DUMP({types:/re/, exclude:/re/, pdp:true, key:p=>stem, prefix:'/en-us'})
// Output, one line per style: key~handle~title~type~n~lo~loHandle~hi~hiHandle~comp~madein~sale~tags
// lo/hi are REGULAR prices (compare-at where above price) of variant[0] (base size).
const strip=h=>(h||'').replace(/<style[\s\S]*?<\/style>|<script[\s\S]*?<\/script>/g,' ').replace(/<[^>]+>/g,' ').replace(/&nbsp;|&#160;/g,' ').replace(/&amp;/g,'&').replace(/\s+/g,' ');
const FIB='(?:organic |recycled |supima |pima |merino |extra fine merino |lambswool |virgin |egyptian |mercerized |bci |regenerative |performance |certified organic )?(?:cotton|polyester|poly(?![a-z])|nylon|polyamide|spandex|elastane|lycra|wool|cashmere|silk|linen|hemp|viscose|rayon|lyocell|tencel|modal|cupro|acrylic|alpaca|mohair|leather|lambskin|lamb skin|cowhide|horsehide|goatskin|suede|polyurethane|ramie|yak|camel|down|feather|acetate|triacetate|metallic|polypropylene|elastomultiester|elasterell|other fibers?)';
const CR=new RegExp('(\\d{1,3}(?:[.,]\\d)?\\s?%\\s?'+FIB+'(?:[\\s,/&+-]{1,4}(?:and\\s)?\\d{1,3}(?:[.,]\\d)?\\s?%\\s?'+FIB+')*)','i');
const CR2=new RegExp('('+FIB+'\\s?\\d{1,3}\\s?%(?:[\\s,/&+-]{1,4}'+FIB+'\\s?\\d{1,3}\\s?%)*)','i');
const KR=new RegExp('\\b'+FIB+'\\b','ig');
const comp=t=>{const m=t.match(CR)||t.match(CR2);return m?m[1].trim():''};
const kw=t=>[...new Set((t.match(KR)||[]).map(x=>x.toLowerCase()))].slice(0,4).join('+');
const mi=t=>{const m=t.match(/(?:Made|Crafted|Produced|Manufactured|Sewn|Knit(?:ted)?|Woven) in (?:the )?([A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+)?)/);return m?m[1]:''};
window.DUMP=async function(o){const pre=o.prefix||'';let all=[];
for(let p=1;p<60;p++){const j=await fetch(pre+'/products.json?limit=250&page='+p).then(r=>r.json());if(!j.products.length)break;all=all.concat(j.products)}
window.ALL=all;
let av=all.filter(p=>p.variants.some(v=>v.available)&&(!o.types||o.types.test(p.product_type))&&!(o.exclude&&o.exclude.test(p.title+' | '+p.vendor+' | '+p.tags.join(','))));
if(o.filter)av=av.filter(o.filter);
const G={};
for(const p of av){const v=p.variants[0];const b=strip(p.body_html);let c=comp(b),k=c?'':kw(b),m=mi(b);
 if(o.pdp&&!c){try{const h=await fetch(pre+'/products/'+p.handle).then(r=>r.text());const t=strip(h.replace(/<head[\s\S]*?<\/head>/,''));const c2=o.pdpre?((t.match(o.pdpre)||[])[1]||''):comp(t);if(c2){c=comp(c2)||c2;k=''}else if(!k)k=kw(t);if(!m)m=mi(t)}catch(e){}}
 const pr=+v.price,ca=+(v.compare_at_price||0),reg=ca>pr?ca:pr;const key=o.key?o.key(p):p.handle;
 const g=G[key]||(G[key]={key,h:p.handle,t:p.title,ty:p.product_type,n:0,lo:1e9,loH:'',hi:0,hiH:'',c:'',m:'',sale:0,tags:''});
 g.n++;if(reg<g.lo){g.lo=reg;g.loH=p.handle}if(reg>g.hi){g.hi=reg;g.hiH=p.handle}if(ca>pr)g.sale++;
 if(!g.c||g.c.startsWith('KW:')||g.c=='ND')g.c=c||(k?'KW:'+k:(g.c||'ND'));if(!g.m&&m)g.m=m;
 if(o.tagre&&!g.tags)g.tags=p.tags.filter(x=>o.tagre.test(x)).join(',')}
const out=Object.values(G).map(g=>[g.key,g.h,g.t,g.ty,g.n,g.lo,g.loH==g.h?'=':g.loH,g.hi,g.hiH==g.h?'=':g.hiH,g.c||'ND',g.m||'-',g.sale,g.tags||'-'].join('~'));
document.body.innerHTML='<pre id=o></pre>';document.getElementById('o').textContent=`styles=${out.length} listings=${av.length} feed=${all.length}\n`+out.join('\n');return out.length};
