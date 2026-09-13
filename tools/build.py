#!/usr/bin/env python3
"""
build.py — assemble the deployable single-file page from data/ and app/template.html.

    python3 tools/build.py            writes dist/menswear_spectrum.html, dist/index.html,
                                      dist/canonical_keys.txt; prints version, size, sha256

The output is still one HTML file with no dependencies — that part of the deploy
story does not change. What changes is that the file is a product, not a source.
Nothing is edited in dist/. If it needs to change, change data/ or app/template.html
and build again.

Version comes from changelog.json (first entry). A build whose data or template has
changed since the top changelog entry was written is caught by the release gate in
job.py, not here — build.py never refuses to build.
"""
import sys, os, json, hashlib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import spec

SETS = {'ADDMEN', 'ADDCLOTH'}


def js(obj):
    return json.dumps(obj, ensure_ascii=False)


def emit_data(bands):
    """The hand-formatted DATA block: one band per section, rows packed several
    per line the way the original was written, so a diff on the built file stays
    readable."""
    out = ['const DATA = {']
    keys = list(bands)
    for bi, key in enumerate(keys):
        b = bands[key]
        out.append(f'  {key}: {{')
        out.append(f'    name:{js(b["name"])}, range:{js(b["range"])},')
        out.append('    brands:[')
        line = '      '
        rows = [js(r).replace('", ', '",').replace(', ', ',') for r in b['brands']]
        for i, r in enumerate(rows):
            piece = r + ('' if i == len(rows) - 1 else ',')
            if len(line) + len(piece) > 100 and line.strip():
                out.append(line.rstrip())
                line = '      '
            line += piece
        if line.strip():
            out.append(line.rstrip())
        out.append('    ]')
        out.append('  }' + (',' if bi < len(keys) - 1 else ''))
    out.append('};')
    return '\n'.join(out)


def build(root=spec.ROOT, outdir=None):
    data = spec.load()
    C = spec.consts(data)
    tmpl = open(os.path.join(root, 'app', 'template.html'), encoding='utf8').read()

    def sub(m):
        name = m.group(1)
        if name not in C:
            raise SystemExit(f'build: template wants @@{name}@@ and the data has no such const')
        v = C.pop(name)
        if name == 'DATA':
            return emit_data(v)
        if name in SETS:
            return f'const {name} = new Set({js(v)});'
        return f'const {name} = {js(v)};'

    html = re.sub(r'/\*@@([A-Z_]+)@@\*/', sub, tmpl)
    if C:
        raise SystemExit(f'build: data carries consts the template never asks for: {sorted(C)}')

    outdir = outdir or os.path.join(root, 'dist')
    os.makedirs(outdir, exist_ok=True)
    for fn in ('menswear_spectrum.html', 'index.html'):
        with open(os.path.join(outdir, fn), 'w', encoding='utf8', newline='\n') as f:
            f.write(html)
    with open(os.path.join(outdir, 'canonical_keys.txt'), 'w', encoding='utf8') as f:
        f.write('\n'.join(data.names) + '\n')
    b = html.encode('utf8')
    sha = hashlib.sha256(b).hexdigest()
    ver = data.changelog[0]['v']
    print(f'built v{ver}  {len(b):,} bytes  sha256 {sha[:16]}  {len(data.brands)} brands  -> {outdir}')
    return sha


if __name__ == '__main__':
    build()
