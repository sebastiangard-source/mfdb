#!/usr/bin/env python3
"""
Reconcile externally-authored brand names against the file's canonical keys.

Run this on every brief's output before writing anything into the spectrum.
The briefs were worked in other threads; 21 of the 186 keys carry punctuation
another thread will render differently, and a mismatch does not error — it
writes an orphan that displays nowhere.

  python3 reconcile.py names.txt            one name per line
  python3 reconcile.py --dump               write canonical_keys.txt and exit

Output is three lists: exact matches, near misses with the canonical form to
use, and names with no plausible match (a genuinely new brand, or a typo).
"""
import sys, re, unicodedata, difflib

# Keys come from canonical_keys.txt when it is present, and from the build only when
# it is not. A thread checking names needs the key list, not an 810KB build it has been
# told not to edit — and one thread had to fabricate a stand-in build to run this at all.
import os
HTML = 'menswear_spectrum.html'
KEYS = 'canonical_keys.txt'
if os.path.exists(KEYS):
    CANON = [l.strip() for l in open(KEYS, encoding='utf8') if l.strip()]
    SOURCE = KEYS
elif os.path.exists(HTML):
    S = open(HTML, encoding='utf8').read()
    CANON = [r[0] for r in re.findall(r'\["([^"]+)",([01]),\[[\d,\s]+\]', S)]
    SOURCE = HTML
else:
    sys.exit(f'reconcile: need {KEYS} or {HTML} in the working directory')


def fold(s):
    """Aggressive normalisation for matching only — never for storage."""
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.lower().replace('&', 'and').replace('’', "'")
    return re.sub(r'[^a-z0-9]', '', s)


FOLDED = {}
for c in CANON:
    FOLDED.setdefault(fold(c), c)

if '--dump' in sys.argv:
    if SOURCE != HTML:
        sys.exit('reconcile: --dump regenerates the key file from the build, '
                 'so it needs menswear_spectrum.html')
    with open('canonical_keys.txt', 'w', encoding='utf8') as f:
        f.write('\n'.join(CANON) + '\n')
    print(f'wrote canonical_keys.txt — {len(CANON)} keys')
    tricky = [c for c in CANON
              if not c.isascii() or re.search(r"[.'&]", c)]
    print(f'{len(tricky)} keys carry punctuation or accents:')
    for t in tricky:
        print(f'    {t}')
    sys.exit(0)

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(2)

names = [l.strip() for l in open(sys.argv[1], encoding='utf8') if l.strip()]
exact, near, miss = [], [], []
for n in names:
    if n in CANON:
        exact.append(n)
    elif fold(n) in FOLDED:
        near.append((n, FOLDED[fold(n)]))
    else:
        m = difflib.get_close_matches(fold(n), FOLDED, n=1, cutoff=0.85)
        if m:
            near.append((n, FOLDED[m[0]]))
        else:
            miss.append(n)

print(f'{len(names)} names in — {len(exact)} exact, {len(near)} to rewrite, '
      f'{len(miss)} unmatched\n')
if near:
    print('REWRITE before merging:')
    for a, b in near:
        print(f'    {a!r:34} -> {b!r}')
    print()
if miss:
    print('NO MATCH — new brand, or a name to chase:')
    for m in miss:
        print(f'    {m}')
    print()
if not near and not miss:
    print('All names match canonical keys. Safe to merge.')
