"""Fibre parsing per rules_fibre.md — main fabric line only; never keyed on product names."""
import re, unicodedata

NAT = {'cotton','wool','linen','silk','cashmere','hemp','alpaca','mohair','camel','vicuna','yak','leather','down','other-natural'}
CEL = {'viscose','modal','lyocell','cupro','acetate','triacetate','other-cellulosic'}
SYN = {'polyester','polyamide','elastane','acrylic','polypropylene','polyurethane','elastolefin','elastomultiester','other-synthetic'}

# order matters: longer / more specific first
WORDS = [
 (r'elastomultiester','elastomultiester'),(r'elastolefin|xlance','elastolefin'),
 (r'other fibres|other fibers|andere fasern','other'),(r'baumwolle|bio-baumwolle','cotton'),(r'lammleder|leder\b','leather'),(r'daune','down'),
 (r'elastane|elasthane|elasthan|elastan|elastine|spandex|lycra|\bEL\b|\bEA\b','elastane'),
 (r'polyurethane|\bPU\b|ポリウレタン','polyurethane'),
 (r'polyamide|polyamid|nylon|cordura|corudra|surfnyl|\bPA\b|ナイロン','polyamide'),
 (r'polyester|\bpoly\b|coolmax|\bPL\b|ポリエステル','polyester'),
 (r'acrylic|\bPC\b|アクリル','acrylic'),
 (r'lyocell|tencel','lyocell'),(r'modal','modal'),(r'cupro|キュプラ','cupro'),(r'triacetate','triacetate'),(r'acetate','acetate'),
 (r'viscose|viskose|rayon|ecovero|\bCV\b|\bVI\b|レーヨン','viscose'),
 (r'cashmere|kaschmir|\bWS\b|カシミヤ','cashmere'),(r'alpaca|alpaka|アルパカ','alpaca'),(r'mohair|モヘア','mohair'),
 (r'camel','camel'),(r'vicu[nñ]a','vicuna'),(r'\byak\b','yak'),
 (r'merino|lambswool|schurwolle|wolle|wool|\bWO\b|\bWV\b|ウール|毛','wool'),
 (r'linen|leinen|flax|\bLI\b|麻|リネン','linen'),(r'silk|\bSE\b|シルク','silk'),(r'hemp|ヘンプ','hemp'),(r'paper|washi|kapok|和紙','other-natural'),
 (r'cotton|\bCO\b|コットン|綿','cotton'),
 (r'leather|suede|lambskin|lamb skin|goatskin|calf|steerhide|horsehide|cowhide','leather'),(r'\bdown\b|feather','down'),
]

def fold(s):
    if re.search(r'[\u3040-\u30ff\u4e00-\u9fff]', s):
        return unicodedata.normalize('NFC', s)
    s = unicodedata.normalize('NFD', s)
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')

def fibre_of(tok):
    t = fold(tok)
    for pat, f in WORDS:
        if re.search(pat, t, re.I if not re.fullmatch(r'\\b[A-Z]{2}\\b', pat) else 0):
            # two-letter codes are case-sensitive
            if re.fullmatch(r'\\b[A-Z]{2}\\b', pat) or '|' in pat and re.search(r'\\b[A-Z]{2}\\b', pat):
                pass
            return f
    return None

def fibre_of_strict(tok):
    t = fold(tok)
    for pat, f in WORDS:
        alts = pat.split('|')
        for a in alts:
            code = re.fullmatch(r'\\b([A-Z]{2})\\b', a)
            if code:
                if re.search(r'\b' + code.group(1) + r'\b', t):
                    return f
            elif re.search(a, t, re.I):
                return f
    return None

MAIN_SPLIT = re.compile(r'\s//\s|;|\b(Lining|Liner|Backer|Accent|Fill|Pockets?|Ribbing|Rib|Collar|襟|リブ|裏地)\b\s*:?', re.I)

def main_line(comp):
    """First listed composition; shell over lining; labelled first part."""
    c = comp.strip()
    c = re.sub(r'^(Shell( & Lining)?|Main fabric( 1)?|Outer|Body|Pants|本体|Fabric)\s*[:\-–]\s*', '', c, flags=re.I)
    c = re.sub(r'^Material:\s*', '', c, flags=re.I)
    # strip any other leading part label ("Short sleeve part:", "Main body:", "Outer material:")
    FW = re.compile(r'cotton|wool|linen|silk|cashmere|nylon|polyamide|polyester|poly\b|elastane|spandex|viscose|rayon|leather|acrylic|polyurethane|merino|alpaca|mohair|hemp|cupro|modal|lyocell|down|fleece|coolmax|surf', re.I)
    lm = re.match(r'^([A-Za-z][A-Za-z /&-]{1,30}?)\s*[:\-–]\s+\S', c)
    if lm and not FW.search(lm.group(1)):
        c = c[lm.end() - 1:]
    # cut at the next labelled part ("Contrast fabric:", "Rib part:", "Waist Part:", "Leather Parts -", "Lining:")
    for mm in re.finditer(r'(?<=[\d%a-zA-Z.)®,])\s+(?=([A-Z][A-Za-z]+(?: [a-zA-Z]+){0,3})\s*(?::|\s-\s))', c):
        if mm.start() > 0 and not FW.search(mm.group(1)):
            c = c[:mm.start()]; break
    c = re.sub(r'\(paper\)', 'paper', c, flags=re.I)
    c = re.sub(r'^表地\s*[:：]\s*', '', c)
    c = re.split(r'襟|リブ|裏地|付属|袖口', c)[0]
    c = MAIN_SPLIT.split(c)[0]
    c = re.split(r'\s/\s(?=\d{1,3}\s?%)', c)[0]
    c = re.sub(r'\((?:[^()]*?(recycled|virgin|organic|oz|gsm|g\b)[^()]*)\)', ' ', c, flags=re.I)
    return c.strip()

PCT = re.compile(r'(\d{1,3}(?:[.,]\d+)?)\s?%%?\s*([A-Za-zÀ-ÿ぀-ヿ一-鿿][A-Za-zÀ-ÿ぀-ヿ一-鿿 \-®™]*)')
PCT_AFTER = re.compile(r'([A-Za-z぀-ヿ一-鿿][A-Za-z぀-ヿ一-鿿 ]*?)\s?(\d{1,3})\s?%')

def parse(comp):
    """Return (parts[(fibre,pct,house)], named_only_fibres, status) where status in pct|named|trademark|none."""
    if not comp or comp.upper().startswith('ND'):
        return [], [], 'none'
    m = main_line(comp)
    parts = []
    jp = re.search(r'[\u3040-\u30ff\u4e00-\u9fff]\d', m)
    if jp:
        for word, pct in re.findall(r'([\u3040-\u30ff\u4e00-\u9fff]+)(\d{1,3})\s?%', m):
            f = fibre_of_strict(word)
            parts.append((f or 'UNK:' + word, float(pct), word))
    for pct, word in ([] if jp else PCT.findall(m)):
        f = fibre_of_strict(word)
        parts.append((f or 'UNK:' + word.strip()[:20], float(pct.replace(',', '.')), word.strip()))
    if not parts:
        for word, pct in PCT_AFTER.findall(m):
            f = fibre_of_strict(word)
            if f: parts.append((f, float(pct), word.strip()))
    if parts and all(f.startswith('UNK') for f, p, w in parts) and re.search(r'surfstretch', m, re.I):
        return [], [], 'trademark'
    if parts:
        # merge same fibre
        agg = {}
        for f, p, w in parts:
            agg.setdefault(f, [0, w]); agg[f][0] += p
        parts = [(f, v[0], v[1]) for f, v in agg.items()]
        return parts, [], 'pct'
    if re.search(r'surfstretch', m, re.I) and not re.search(r'cotton|nylon|wool|surfnyl', re.sub(r'surfstretch', '', m, flags=re.I), re.I):
        return [], [], 'trademark'
    named = []
    for pat, f in WORDS:
        for a in pat.split('|'):
            if re.fullmatch(r'\\b[A-Z]{2}\\b', a):
                continue
            if re.search(a, fold(m), re.I) and f not in named:
                named.append(f); break
    # order named by position in string
    named.sort(key=lambda f: min([fold(m).lower().find(x.lower()) for p, ff in WORDS if ff == f for x in p.split('|') if not x.startswith('\\') and fold(m).lower().find(x.lower()) >= 0] or [999]))
    if named:
        return [], named, 'named'
    return [], [], 'none'

def klass(f):
    return 'natural' if f in NAT else 'cellulosic' if f in CEL else 'synthetic' if f in SYN else 'other'

def style_row(comp):
    """-> dict lead_fibre, lead_pct, elastane_pct, pure, single_fibre, has_comp, lead_class, spandex, spandex_high, note"""
    parts, named, st = parse(comp)
    if st == 'pct':
        unk = [f for f, p, w in parts if f.startswith('UNK')]
        known = [(f, p, w) for f, p, w in parts if not f.startswith('UNK')]
        tot = sum(p for f, p, w in parts)
        lead = max(known, key=lambda x: x[1]) if known else None
        # ties: first listed
        if known:
            top = max(p for f, p, w in known)
            lead = [x for x in known if x[1] == top][0]
        el = sum(p for f, p, w in known if f in ('elastane', 'elastolefin'))
        classes = {klass(f) for f, p, w in known}
        pure = classes.pop() if len(classes) == 1 else 'blend'
        single = known[0][0] if len(known) == 1 and abs(known[0][1] - 100) < 0.6 else '-'
        note = []
        if unk: note.append('unparsed token: ' + ','.join(u[3:] for u, p, w in parts if u.startswith('UNK')))
        if abs(tot - 100) > 1 and not unk: note.append(f'main line sums to {tot:g}')
        if not lead:
            return dict(lead_fibre='ND', lead_pct='ND', elastane_pct='ND', pure='undisclosed', single_fibre='-', has=False, cls=None, sp=0, sph=0, note='; '.join(note))
        return dict(lead_fibre=lead[0], lead_pct=int(lead[1]+0.5), elastane_pct=int(el+0.5), pure=pure, single_fibre=single,
                    has=True, cls=klass(lead[0]), sp=1 if el > 0 else 0, sph=1 if el >= 5 else 0, note='; '.join(note))
    if st == 'named':
        lead = named[0]
        classes = {klass(f) for f in named}
        pure = classes.pop() if len(classes) == 1 else 'blend'
        if len(named) == 1:
            return dict(lead_fibre=lead, lead_pct=100, elastane_pct=0, pure=pure, single_fibre='-', has=True, cls=klass(lead), sp=0, sph=0,
                        note='fibre named without a percentage; lead_pct 100 assumes the single named fibre is the whole main line, single_fibre left -')
        return dict(lead_fibre=lead, lead_pct='NC', elastane_pct=0 if 'elastane' not in named else 'NC', pure=pure, single_fibre='-', has=True, cls=klass(lead),
                    sp=1 if 'elastane' in named else 0, sph=0, note='blend named without percentages; lead = first named, share not stated')
    if st == 'trademark':
        return dict(lead_fibre='ND', lead_pct='ND', elastane_pct='ND', pure='undisclosed', single_fibre='-', has=False, cls=None, sp=0, sph=0,
                    note='house trademark fabric SurfStretch®; the site states no fibre for it — not inferred')
    return dict(lead_fibre='ND', lead_pct='ND', elastane_pct='ND', pure='undisclosed', single_fibre='-', has=False, cls=None, sp=0, sph=0, note='')

if __name__ == '__main__':
    for c in ['Outer: 87% PL 13% PU // Lining 85% PL 15% PU', '70% WO 30%WS', '100% CO (12.5oz)', 'Shell: 70% polyamide, 26% polyurethane, 4% elastane; Lining: 78% polyamide',
              'Main fabric 1: 86% polyamide, 14% elastane; Main fabric 2: 85%', '27% Cotton, 69.5% Polyester, 3.5% Spandex', 'Washed cotton (named, no %)',
              'Brushed alpaca and wool blend (named, no %)', '100% SurfStretch®.', 'Shell & Lining - 100% SurfNyl®. Milled and dyed in the USA.',
              '100% cotton 14-wale corduroy with SurfNyl® contrast fly', 'Pants: 100% Polyester / 210 GSM Pockets: 92% Polyester, 8% Spandex',
              'Outer: 53% Coolmax Poly, 47% Polyester Liner: 100% Polyester', '本体：コットン53% レーヨン29% ナイロン18% 襟・リブ部分：コットン76%', '55%% cotton, 45% polyester',
              '100% cashmere (65% recycled, 35% virgin) Italian yarn', '85% Solid Stretch Woven Nylon, 15% Spandex', '100% Pima Cotton.', '50% wool, 50% Camel hair Portugese cloth']:
        print(c[:50].ljust(52), style_row(c))
