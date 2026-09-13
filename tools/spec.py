"""
spec.py — shared library for every Spectrum tool.

    REG              the field registry (schema/fields.json)
    slug(name)       canonical file stem for a brand name
    load()           -> Data(brands, places, changelog, rubric, bands, settings)
    get(rec, path)   dotted-path read on a brand record; None if absent
    put(rec, path, v) dotted-path write
    consts(data)     -> ordered {CONST_NAME: python value} exactly as the build emits them

Nothing else parses the HTML, and nothing else knows which const a field maps to.
"""
import json, os, re, unicodedata, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
BRANDS = os.path.join(DATA, 'brands')
SCHEMA = os.path.join(ROOT, 'schema', 'fields.json')

REG = json.load(open(SCHEMA, encoding='utf8'))
FIELDS = REG['fields']
BRAND_FIELDS = {k: v for k, v in FIELDS.items() if v['scope'] == 'brand'}
GLOBAL_FIELDS = {k: v for k, v in FIELDS.items() if v['scope'] == 'global'}
REGISTERS = [k for k, v in BRAND_FIELDS.items() if v.get('register')]
NOTE_KEYS = {k for k, v in BRAND_FIELDS.items() if v.get('note')}


def slug(name):
    s = unicodedata.normalize('NFKD', name)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace('&', ' and ').replace("'", '').replace('’', '')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s


def fold(s):
    """Aggressive normalisation for matching only — never for storage."""
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.lower().replace('&', 'and').replace('’', "'")
    return re.sub(r'[^a-z0-9]', '', s)


def get(rec, path):
    cur = rec
    for p in path.split('.'):
        if not isinstance(cur, dict) or p not in cur:
            return None
        cur = cur[p]
    return cur


def put(rec, path, value):
    parts = path.split('.')
    cur = rec
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = value


def drop(rec, path):
    parts = path.split('.')
    cur = rec
    for p in parts[:-1]:
        if p not in cur:
            return
        cur = cur[p]
    cur.pop(parts[-1], None)


def dump(obj):
    """Canonical on-disk JSON: indented, UTF-8, keys in insertion order,
    with short lists kept on one line so a prices row or a focus vector is
    one diff line, not eight."""
    return _fmt(obj, 0) + '\n'


def _fmt(o, ind):
    pad = '  ' * ind
    flat = json.dumps(o, ensure_ascii=False)
    if isinstance(o, dict):
        if not o:
            return '{}'
        items = [f'{pad}  {json.dumps(k, ensure_ascii=False)}: {_fmt(v, ind + 1)}' for k, v in o.items()]
        return '{\n' + ',\n'.join(items) + '\n' + pad + '}'
    if isinstance(o, list):
        if not o:
            return '[]'
        if len(flat) <= 100 and not any(isinstance(x, dict) for x in o):
            return flat
        items = [f'{pad}  {_fmt(v, ind + 1)}' for v in o]
        return '[\n' + ',\n'.join(items) + '\n' + pad + ']'
    return flat


class Data:
    def __init__(self, brands, places, changelog, rubric, bands, settings):
        self.brands = brands          # list of records, in seat order
        self.places = places
        self.changelog = changelog
        self.rubric = rubric
        self.bands = bands
        self.settings = settings
        self.by_name = {b['name']: b for b in brands}

    @property
    def names(self):
        return [b['name'] for b in self.brands]


def load():
    recs = []
    for fn in sorted(os.listdir(BRANDS)):
        if fn.endswith('.json'):
            r = json.load(open(os.path.join(BRANDS, fn), encoding='utf8'))
            if slug(r['name']) + '.json' != fn:
                raise SystemExit(f'{fn}: file name does not match slug of {r["name"]!r}')
            recs.append(r)
    seats = [r['seat'] for r in recs]
    if sorted(seats) != list(range(1, len(recs) + 1)):
        dup = [s for s, c in collections.Counter(seats).items() if c > 1]
        raise SystemExit(f'seats are not dense 1..{len(recs)}; duplicates {dup}')
    recs.sort(key=lambda r: r['seat'])

    def g(name):
        return json.load(open(os.path.join(DATA, name), encoding='utf8'))
    return Data(recs, g('places.json'), g('changelog.json'), g('rubric.json'),
                g('bands.json'), g('settings.json'))


def save_brand(rec):
    with open(os.path.join(BRANDS, slug(rec['name']) + '.json'), 'w', encoding='utf8') as f:
        f.write(dump(rec))


def save_global(name, obj):
    with open(os.path.join(DATA, name), 'w', encoding='utf8') as f:
        f.write(dump(obj))


# ------------------------------------------------------------------ assembly

def consts(data):
    """Rebuild every JS const from the records. Returns an ordered dict of
    CONST_NAME -> python object. Set/array consts are returned as lists."""
    out = collections.OrderedDict()
    # brand-keyed dicts, one per const, keys in seat order
    by_const = collections.defaultdict(collections.OrderedDict)
    for rec in data.brands:
        n = rec['name']
        for fname, f in BRAND_FIELDS.items():
            c = f['const']
            if c == 'DATA' or c is None:
                continue
            v = get(rec, f['path'])
            if v is None:
                continue
            if f['type'] == 'bool':
                if v:
                    by_const[c].setdefault('__list__', []).append(n)
                continue
            # composite consts: several fields fold into one value
            if c == 'FAB':
                by_const['FAB'][n] = [rec['fabric'][k] for k in
                                      ('denim', 'cashmere', 'linen', 'cotton', 'wool', 'synth')]
            else:
                by_const[c][n] = v
    for c, d in by_const.items():
        out[c] = d.get('__list__', d) if '__list__' in d else d
    # DATA: bands with rows in seat order
    bands = collections.OrderedDict()
    for key, meta in data.bands.items():
        bands[key] = {'name': meta['name'], 'range': meta['range'], 'brands': []}
    for rec in data.brands:
        row = [rec['name'], rec['dagger'],
               [rec['focus'][k] for k in ('tech', 'comfort', 'craft', 'style')]]
        if rec.get('row_class') is not None or rec.get('row_override') is not None:
            row += [rec.get('row_class', ''), rec.get('row_override', '')]
        bands[rec['band']]['brands'].append(row)
    out['DATA'] = bands
    out['PLACES'] = data.places
    out['CHANGELOG'] = data.changelog
    out['RUBRIC'] = data.rubric
    for k, v in data.settings.items():
        out[k] = v
    return out
