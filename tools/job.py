#!/usr/bin/env python3
"""
job.py — orchestrate the worker threads.

A job is one bounded research task briefed out to another thread. Its whole life
is recorded in jobs/manifest.json and nowhere else; jobs/STATUS.md is derived
from it and never hand-edited (the handoff's nine-row table was hand-maintained
and drifted like every other hand-maintained list).

    job.py status                          print the board, rewrite jobs/STATUS.md
    job.py new ID --kind K --title T [--brands all|FILE] [--pilot N]
                                           scaffold jobs/briefs/ID/ from the template
    job.py schema ID col:type[:range] ...  declare the return columns (see below)
    job.py writes ID PATH=COLUMN ...       declare where checked columns land
                                           e.g. dials.golf=golf_score  prices.3=jeans_range
    job.py issue ID                        mark issued; freezes the brief
    job.py check ID RETURN.csv             reconcile names, validate columns, triage rows
                                           -> jobs/triage/ID_<n>.md and ID_<n>.merge.csv
    job.py merge ID ID_<n>.merge.csv       apply the mergeable rows to data/brands/*.json
    job.py hold ID "reason" | close ID     state changes with a note
    job.py release                         lint -> build -> validate -> testpass -> hash

Column types:  key (the brand name, required, exactly one)
               int[:lo:hi]  str  url  json  provenance (required, exactly one)
               enum:a|b|c
Every column except key and provenance accepts the job's not-checked token
(default "NC"), which is distinct from an empty string: NC means nobody looked,
"" is a shape error. A row whose provenance is empty, "N/A", or "n/a" is HELD.
"""
import sys, os, json, csv, re, subprocess, datetime, difflib, hashlib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import spec
from spec import fold

JOBS = os.path.join(spec.ROOT, 'jobs')
MANIFEST = os.path.join(JOBS, 'manifest.json')
STATES = ['drafted', 'issued', 'pilot_returned', 'returned', 'merged', 'held', 'closed']
TODAY = datetime.date.today().isoformat()


def load_manifest():
    return json.load(open(MANIFEST, encoding='utf8')) if os.path.exists(MANIFEST) else {'jobs': []}


def save_manifest(m):
    with open(MANIFEST, 'w', encoding='utf8') as f:
        f.write(spec.dump(m))
    status(m, quiet=True)


def job_of(m, jid):
    for j in m['jobs']:
        if j['id'] == jid:
            return j
    sys.exit(f'no job {jid!r}; job.py status lists them')


# ---------------------------------------------------------------- status

def status(m=None, quiet=False):
    m = m or load_manifest()
    rows = []
    for j in m['jobs']:
        last = j['returns'][-1] if j.get('returns') else None
        rows.append((j['id'], j['state'], j.get('issued') or '', j.get('kind', ''),
                     f'{last["merged"]}/{last["rows"]}' if last else '',
                     j.get('blocked_on', '') or j.get('note', '')))
    lines = ['# Job board — derived from jobs/manifest.json by job.py; do not edit', '',
             f'_{len(rows)} jobs · rewritten {TODAY}_', '',
             '| job | state | issued | kind | merged/returned | blocked on / note |',
             '|---|---|---|---|---|---|']
    for r in rows:
        lines.append('| ' + ' | '.join(str(x) for x in r) + ' |')
    open(os.path.join(JOBS, 'STATUS.md'), 'w', encoding='utf8').write('\n'.join(lines) + '\n')
    if not quiet:
        w = [max(len(str(r[i])) for r in rows + [('job', 'state', 'issued', 'kind', 'ret', 'note')]) for i in range(6)]
        for r in rows:
            print('  '.join(str(x).ljust(w[i]) for i, x in enumerate(r)))
        if not rows:
            print('no jobs yet')


# ---------------------------------------------------------------- new / schema / writes / issue

BRIEF_TMPL = '''# {id} — {title}

**Issued** {date} · **Kind** {kind} · **Pilot** {pilot} rows first · **Returns to** the Spectrum thread

Read `audit_protocol.md` before starting. This brief carries everything it requires.
If any instruction below would make you produce a confident wrong answer, stop and say so
before doing it. Returns that say *the brief got this wrong* have been worth more than
the ones that said *done*.

## The job

_One paragraph. What is being checked, for which brands, and what a finding looks like._

## What to return

Two files, nothing else:

1. `return.csv` in exactly the schema in `schema.json` (a template with the brand keys
   prefilled is in `return_template.csv`). One row per brand. Never prose.
2. `NOTE.md`: what was checked, what was not reached, what contradicted the existing
   record, and what this brief got wrong.

Send the first {pilot} rows before doing the rest. Format errors caught at {pilot} rows cost
minutes; caught at the end they cost the pass.

## Rules

- Brand names must match `canonical_keys.txt` exactly. Run `python3 reconcile.py names.txt`
  before returning. Zero rewrites, zero unmatched.
- `{nc}` in a cell means *nobody looked*. An empty cell is an error. Never leave a cell blank.
- `source` is required on every row that carries a finding. A URL. `N/A` is not a source
  and the row will be held.
- Do not touch `menswear_spectrum.html`. Do not rebuild the tool. Do not send working files.
- Out of scope but noticed: record it anyway in `NOTE.md` or an extra column, do not discard it.

## Stop conditions

- More than a third of the pilot returns nothing usable: stop, the brief is mis-aimed.
- Any single brand takes more than 25 minutes: mark it `{nc}` with a note and move on.
- A source that cannot be resolved (page 404s, locator caps at N): record what the widget
  itself says and do not fill from memory.

## Columns

{columns}
'''


def new(args):
    jid = args[0]
    opts = dict(zip(args[1::2], args[2::2]))
    m = load_manifest()
    if any(j['id'] == jid for j in m['jobs']):
        sys.exit(f'{jid} already exists')
    kind = opts.get('--kind', 'audit')
    pilot = int(opts.get('--pilot', 8))
    brands_opt = opts.get('--brands', 'all')
    data = spec.load()
    if brands_opt == 'all':
        brands = data.names
    else:
        brands = [l.strip() for l in open(brands_opt, encoding='utf8') if l.strip()]
        bad = [b for b in brands if b not in data.by_name]
        if bad:
            sys.exit(f'brand list carries names not on the map: {bad} — run reconcile first')
    j = {'id': jid, 'title': opts.get('--title', jid), 'kind': kind, 'state': 'drafted',
         'created': TODAY, 'issued': None, 'pilot': pilot, 'nc': 'NC',
         'brands': brands if brands_opt != 'all' else 'all',
         'schema': [{'name': 'brand', 'type': 'key'},
                    {'name': 'source', 'type': 'provenance'},
                    {'name': 'note', 'type': 'str'}],
         'writes': {}, 'returns': [], 'blocked_on': ''}
    m['jobs'].append(j)
    d = os.path.join(JOBS, 'briefs', jid)
    os.makedirs(d, exist_ok=True)
    save_manifest(m)
    materialise(j, data)
    print(f'scaffolded jobs/briefs/{jid}/ — now: job.py schema {jid} col:type ...  then edit BRIEF.md')


def materialise(j, data=None):
    """Write the brief directory from the manifest entry. Re-run after schema/writes change."""
    data = data or spec.load()
    d = os.path.join(JOBS, 'briefs', j['id'])
    brands = data.names if j['brands'] == 'all' else j['brands']
    cols = [c['name'] for c in j['schema']]
    with open(os.path.join(d, 'return_template.csv'), 'w', encoding='utf8', newline='') as f:
        w = csv.writer(f)
        w.writerow(cols)
        for b in brands:
            w.writerow([b] + [j['nc'] if c['type'] not in ('key', 'provenance') else ''
                              for c in j['schema'][1:]])
    with open(os.path.join(d, 'schema.json'), 'w', encoding='utf8') as f:
        f.write(spec.dump({'not_checked': j['nc'], 'columns': j['schema']}))
    with open(os.path.join(d, 'canonical_keys.txt'), 'w', encoding='utf8') as f:
        f.write('\n'.join(data.names) + '\n')
    for fn in ('reconcile.py', 'audit_protocol.md'):
        src = os.path.join(spec.ROOT, fn)
        if os.path.exists(src):
            open(os.path.join(d, fn), 'w', encoding='utf8').write(open(src, encoding='utf8').read())
    coltxt = '\n'.join(f'- `{c["name"]}` — {c["type"]}' +
                       (f' {c["range"]}' if 'range' in c else '') +
                       (f' one of {c["values"]}' if 'values' in c else '') +
                       (f'. {c["doc"]}' if c.get('doc') else '')
                       for c in j['schema'])
    bp = os.path.join(d, 'BRIEF.md')
    if not os.path.exists(bp) or j['state'] == 'drafted':
        existing = open(bp, encoding='utf8').read() if os.path.exists(bp) else ''
        body = BRIEF_TMPL.format(id=j['id'], title=j['title'], date=j['issued'] or 'not yet',
                                 kind=j['kind'], pilot=j['pilot'], nc=j['nc'], columns=coltxt)
        # keep an edited "The job" paragraph if the operator already wrote one
        mm = re.search(r'## The job\n\n(.*?)\n\n## What to return', existing, re.S)
        if mm and not mm.group(1).startswith('_One paragraph'):
            body = body.replace('_One paragraph. What is being checked, for which brands, and what a finding looks like._',
                                mm.group(1))
        open(bp, 'w', encoding='utf8').write(body)


def schema(args):
    jid, specs = args[0], args[1:]
    m = load_manifest(); j = job_of(m, jid)
    if j['state'] not in ('drafted', 'issued', 'pilot_returned'):
        sys.exit('schema is frozen once a full return is in; make a new job')
    if j['state'] != 'drafted':
        print(f'amending the schema of an issued job — re-send jobs/briefs/{jid}/ and say what changed')
    cols = [{'name': 'brand', 'type': 'key'}]
    for s in specs:
        parts = s.split(':')
        name, t = parts[0], parts[1]
        c = {'name': name, 'type': t}
        if t == 'int' and len(parts) == 4:
            c['range'] = [int(parts[2]), int(parts[3])]
        if t == 'enum':
            c['type'] = 'enum'; c['values'] = parts[2].split('|')
        cols.append(c)
    if not any(c['type'] == 'provenance' for c in cols):
        cols.append({'name': 'source', 'type': 'provenance'})
    if not any(c['name'] == 'note' for c in cols):
        cols.append({'name': 'note', 'type': 'str'})
    j['schema'] = cols
    save_manifest(m); materialise(j)
    print('schema:', ', '.join(f'{c["name"]}:{c["type"]}' for c in cols))


def writes(args):
    jid, specs = args[0], args[1:]
    m = load_manifest(); j = job_of(m, jid)
    cols = {c['name'] for c in j['schema']}
    w = {}
    for s in specs:
        path, col = s.split('=')
        if col not in cols:
            sys.exit(f'column {col!r} is not in the schema')
        w[path] = col
    j['writes'] = w
    save_manifest(m)
    print('writes:', w)


def issue(args):
    m = load_manifest(); j = job_of(m, args[0])
    j['state'] = 'issued'; j['issued'] = TODAY
    save_manifest(m); materialise(j)
    d = os.path.join(JOBS, 'briefs', j['id'])
    print(f'issued {j["id"]} on {TODAY}. Send the thread jobs/briefs/{j["id"]}/ — '
          f'{", ".join(sorted(os.listdir(d)))}')


def note(args, state):
    m = load_manifest(); j = job_of(m, args[0])
    j['state'] = state
    j['blocked_on' if state == 'held' else 'note'] = ' '.join(args[1:])
    save_manifest(m)


# ---------------------------------------------------------------- check

def check(args):
    jid, path = args[0], args[1]
    m = load_manifest(); j = job_of(m, jid)
    data = spec.load()
    canon = data.names
    folded = {}
    for c in canon:
        folded.setdefault(fold(c), c)
    nc = j['nc']
    cols = j['schema']
    keycol = next(c['name'] for c in cols if c['type'] == 'key')
    provcol = next(c['name'] for c in cols if c['type'] == 'provenance')
    rows = list(csv.DictReader(open(path, encoding='utf-8-sig')))
    if not rows:
        sys.exit('empty return')
    expected = [c['name'] for c in cols]
    got = list(rows[0].keys())
    hard = []
    if got != expected:
        hard.append(f'columns are {got}, schema says {expected}')
    verdict = []   # (name, MERGE|HOLD|REJECT, reason)
    seen = collections.Counter()
    for r in rows:
        name = (r.get(keycol) or '').strip()
        why = []
        if name in data.by_name:
            canon_name = name
        elif fold(name) in folded:
            canon_name = folded[fold(name)]
            why.append(f'name rewritten from {name!r}')
        else:
            mm = difflib.get_close_matches(fold(name), folded, n=1, cutoff=0.85)
            if mm:
                canon_name = folded[mm[0]]
                why.append(f'name rewritten from {name!r} (fuzzy)')
            else:
                verdict.append((name, 'REJECT', 'not a seated brand — new brand or a typo'))
                continue
        seen[canon_name] += 1
        if j['brands'] != 'all' and canon_name not in j['brands']:
            why.append('outside the briefed brand list')
        finding = False
        for c in cols:
            v = (r.get(c['name']) or '').strip()
            t = c['type']
            if t in ('key', 'provenance'):
                continue
            if v == nc:
                continue
            if v == '':
                why.append(f'{c["name"]} is blank — use {nc} if nobody looked')
                continue
            if c['name'] not in ('note', 'status'):
                finding = True
            if t == 'int':
                if not re.fullmatch(r'-?\d+', v):
                    why.append(f'{c["name"]}={v!r} is not an integer')
                elif 'range' in c and not c['range'][0] <= int(v) <= c['range'][1]:
                    why.append(f'{c["name"]}={v} outside {c["range"]}')
            elif t == 'url' and not v.startswith('https://'):
                why.append(f'{c["name"]} is not https')
            elif t == 'enum' and v not in c['values']:
                why.append(f'{c["name"]}={v!r} not in {c["values"]}')
            elif t == 'json':
                try:
                    json.loads(v)
                except Exception:
                    why.append(f'{c["name"]} is not valid JSON')
        prov = (r.get(provcol) or '').strip()
        if finding and (not prov or prov.lower() in ('n/a', 'na', 'none', '-')):
            why.append('finding with no provenance')
        # composite target: several columns land in one record object (fibre.*). A row
        # that fills some of them would write a half-object the page cannot read.
        wcols = list(j.get('writes', {}).values())
        prefixes = {p.split('.')[0] for p in j.get('writes', {})}
        if wcols and len(prefixes) == 1 and '.' in next(iter(j['writes'])):
            missing = [c for c in wcols if (r.get(c) or '').strip() == nc]
            if missing and len(missing) == len(wcols):
                finding = False   # nothing that lands; provenance/status alone is a skip
            elif missing:
                why.append(f'partial object: {", ".join(missing)} still {nc} — all of '
                           f'{prefixes.pop()} lands together or not at all')
        if not finding:
            verdict.append((canon_name, 'SKIP', f'all {nc} — nobody looked'))
        elif why:
            verdict.append((canon_name, 'HOLD', '; '.join(why)))
        else:
            verdict.append((canon_name, 'MERGE', ''))
    for n, c in seen.items():
        if c > 1:
            hard.append(f'{n} appears {c} times')
    counts = collections.Counter(v[1] for v in verdict)
    n = len(j['returns']) + 1
    tag = f'{jid}_{n}'
    os.makedirs(os.path.join(JOBS, 'triage'), exist_ok=True)
    rep = [f'# Triage — {tag}', '', f'return `{os.path.basename(path)}` · {len(rows)} rows · {TODAY}', '',
           f'**MERGE {counts["MERGE"]} · HOLD {counts["HOLD"]} · SKIP {counts["SKIP"]} · REJECT {counts["REJECT"]}**', '']
    if hard:
        rep += ['## Goes back to the thread', ''] + [f'- {h}' for h in hard] + ['']
    for kind in ('REJECT', 'HOLD', 'SKIP'):
        items = [v for v in verdict if v[1] == kind]
        if items:
            rep += [f'## {kind} ({len(items)})', ''] + [f'- {v[0]}: {v[2]}' for v in items] + ['']
    rep += [f'## MERGE ({counts["MERGE"]})', '', ', '.join(v[0] for v in verdict if v[1] == 'MERGE') or '—', '']
    open(os.path.join(JOBS, 'triage', tag + '.md'), 'w', encoding='utf8').write('\n'.join(rep))
    # mergeable rows, with canonical names written in
    mergeable = {v[0] for v in verdict if v[1] == 'MERGE'}
    with open(os.path.join(JOBS, 'triage', tag + '.merge.csv'), 'w', encoding='utf8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=expected)
        w.writeheader()
        for r in rows:
            name = (r.get(keycol) or '').strip()
            cn = name if name in data.by_name else folded.get(fold(name))
            if cn in mergeable and not hard:
                r = dict(r); r[keycol] = cn
                w.writerow({k: r.get(k, '') for k in expected})
    j['returns'].append({'n': n, 'file': os.path.basename(path), 'received': TODAY, 'rows': len(rows),
                         'mergeable': counts['MERGE'], 'held': counts['HOLD'], 'merged': 0,
                         'triage': f'jobs/triage/{tag}.md'})
    worked = sum(1 for v in verdict if v[1] != 'SKIP')
    j['state'] = 'pilot_returned' if worked <= j['pilot'] else 'returned'
    save_manifest(m)
    print('\n'.join(rep))
    if hard:
        print('NOT MERGEABLE — fix the items under "Goes back to the thread" first.')
    else:
        print(f'-> job.py merge {jid} {tag}.merge.csv')


# ---------------------------------------------------------------- merge

def coerce(path, v, ctype):
    if ctype == 'int':
        return int(v)
    if ctype == 'json':
        return json.loads(v)
    return v


def merge(args):
    jid, fn = args[0], args[1]
    m = load_manifest(); j = job_of(m, jid)
    if not j['writes']:
        sys.exit('job declares no writes — job.py writes ID path=column ... first')
    path = fn if os.path.exists(fn) else os.path.join(JOBS, 'triage', fn)
    rows = list(csv.DictReader(open(path, encoding='utf-8-sig')))
    data = spec.load()
    ctype = {c['name']: c['type'] for c in j['schema']}
    keycol = next(c['name'] for c in j['schema'] if c['type'] == 'key')
    changed = collections.Counter()
    log = []
    for r in rows:
        rec = data.by_name[r[keycol]]
        for fpath, col in j['writes'].items():
            v = (r.get(col) or '').strip()
            if v == j['nc'] or v == '':
                continue
            val = coerce(fpath, v, ctype[col])
            mm = re.fullmatch(r'(.+)\.(\d+)', fpath)
            if mm:   # list index, e.g. prices.3
                lst = spec.get(rec, mm.group(1))
                old = lst[int(mm.group(2))]
                lst[int(mm.group(2))] = val
            else:
                old = spec.get(rec, fpath)
                spec.put(rec, fpath, val)
            if old != val:
                changed[fpath] += 1
                log.append(f'{rec["name"]}: {fpath} {old!r} -> {val!r}  [{r.get("source","")}]')
        spec.save_brand(rec)
    with open(os.path.join(JOBS, 'MERGELOG.md'), 'a', encoding='utf8') as f:
        f.write(f'\n## {TODAY} · {jid} · {os.path.basename(path)}\n\n' +
                '\n'.join(f'- {l}' for l in log) + '\n')
    for ret in j['returns']:
        if os.path.basename(path).startswith(f'{jid}_{ret["n"]}'):
            ret['merged'] = len(rows)
    j['state'] = 'merged'
    save_manifest(m)
    print(f'merged {len(rows)} rows: ' + ', '.join(f'{k} x{v}' for k, v in changed.items()))
    print('-> python3 tools/lint.py ; python3 tools/job.py release')
    r = subprocess.run([sys.executable, os.path.join(spec.ROOT, 'tools', 'lint.py')])
    if r.returncode:
        print('LINT FAILED after merge — data/ is dirty; fix or git checkout data/')


# ---------------------------------------------------------------- release

def release(args):
    tools = os.path.join(spec.ROOT, 'tools')
    dist = os.path.join(spec.ROOT, 'dist')
    steps = [('lint', [sys.executable, os.path.join(tools, 'lint.py')], spec.ROOT),
             ('build', [sys.executable, os.path.join(tools, 'build.py')], spec.ROOT),
             ('validate', [sys.executable, os.path.join(spec.ROOT, 'validate.py'), 'menswear_spectrum.html'], dist),
             ('testpass', [sys.executable, os.path.join(spec.ROOT, 'testpass.py')], dist)]
    for name, cmd, cwd in steps:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        tail = (r.stdout or '').strip().split('\n')[-1]
        print(f'{name:9} {"ok " if r.returncode == 0 else "FAIL"}  {tail}')
        if r.returncode:
            print(r.stdout[-3000:]); print(r.stderr[-2000:])
            sys.exit(1)
    html = open(os.path.join(dist, 'menswear_spectrum.html'), 'rb').read()
    sha = hashlib.sha256(html).hexdigest()
    data = spec.load()
    ver = data.changelog[0]['v']
    rel = os.path.join(JOBS, 'releases.json')
    rels = json.load(open(rel)) if os.path.exists(rel) else []
    if rels and rels[-1]['v'] == ver and rels[-1]['sha256'] != sha:
        print(f'\nSTOP: v{ver} was already released at {rels[-1]["sha256"][:16]} and the build now '
              f'hashes {sha[:16]}. Add a changelog entry (bump the version) before shipping.')
        sys.exit(1)
    if not rels or rels[-1]['sha256'] != sha:
        rels.append({'v': ver, 'sha256': sha, 'bytes': len(html), 'date': TODAY, 'brands': len(data.brands)})
        open(rel, 'w').write(spec.dump(rels))
    print(f'\nRELEASE v{ver}  {len(html):,} bytes  sha256 {sha}')
    if '--deploy' in args:
        # Only a build that has just passed every gate reaches the deploy branch.
        import shutil, tempfile
        wt = tempfile.mkdtemp()
        subprocess.run(['git', 'worktree', 'add', '-q', wt, 'deploy'], cwd=spec.ROOT, check=True)
        shutil.copy(os.path.join(dist, 'index.html'), os.path.join(wt, 'index.html'))
        subprocess.run(['git', 'add', 'index.html'], cwd=wt, check=True)
        subprocess.run(['git', '-c', 'user.name=mfdb', '-c', 'user.email=mfdb@local', 'commit', '-qm', f'deploy v{ver} {sha[:8]}'], cwd=wt)
        subprocess.run(['git', 'push', '-q', 'origin', 'deploy'], cwd=wt, check=True)
        subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=spec.ROOT)
        print(f'deploy branch updated: v{ver} {sha[:8]}')
    print('upload dist/index.html to public_html/mfdb as index.new.html, then rename.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    cmd, rest = sys.argv[1], sys.argv[2:]
    {'status': lambda a: status(),
     'new': new, 'schema': schema, 'writes': writes, 'issue': issue,
     'check': check, 'merge': merge, 'release': release,
     'hold': lambda a: note(a, 'held'), 'close': lambda a: note(a, 'closed'),
     }.get(cmd, lambda a: sys.exit(f'unknown command {cmd}'))(rest)
