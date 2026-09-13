# The Menswear Spectrum — architecture

13 September 2026. Written against build v3.6.0 (`dc8dcc16…`). Everything described under
"What exists now" is built, run, and committed in this folder. Nothing has been deployed.

---

## The problem, stated plainly

The build was 810KB, and 75% of it was data written into JavaScript constants inside the
page. That one fact is upstream of most of the failure classes in the handoff:

- **The file was both source and product.** Every merge edited an 800KB HTML file by string
  replacement, which is why batch scripts were all-or-nothing, why an anchor with `\n` in it
  could "succeed" having changed nothing, and why a const read before its declaration could kill
  the script while the page still rendered.
- **Every brand-keyed dict was an independent list that could drift.** Forty-three dicts, each
  keyed by brand name, each hand-maintained. An orphan in one of them displays nowhere and
  errors nowhere. `validate.py` guards the ones it knows about; it did not know about `ADDCLOTH`,
  which has been carrying `"Ralph Lauren"` — not a seated brand — for some time.
- **Nothing could be diffed.** A change to one brand's price was a change to a 18KB line. A
  git history was not possible in any useful sense, so the version string went stale across ten
  builds and two external reviews were mis-attributed.
- **The thread status table was hand-maintained**, in the handoff, in prose, which is the exact
  pattern the handoff itself warns against.

The fix is not a framework or a server. It is the same split the audit protocol already
imposes on people, imposed on the files: **a source that is edited and a product that is built.**

---

## The shape

```
spectrum/
  schema/fields.json       the field registry — one entry per field: const, path, type, range,
                           what absence means. Every tool reads it; nothing else lists dials.
  data/
    brands/<slug>.json     one record per seated brand. 204 files.
    bands.json             band name + range copy
    places.json            the 807 shops (was PLACES)
    changelog.json         the changelog; entry [0].v is the version
    rubric.json            dial rubrics
    settings.json          six scalar consts (NOT_ASSESSED, VISIT_FORM, …)
  app/template.html        the page with /*@@CONST@@*/ markers where data used to be. 199KB.
  tools/
    spec.py                shared: registry, load(), slug(), get/put, consts()
    extract.py             one-time migration, build -> data. Already run. Kept for the record.
    lint.py                registry-driven checks on data/, run before anything is built
    build.py               data + template -> dist/menswear_spectrum.html, index.html, canonical_keys.txt
    job.py                 the worker-thread orchestrator (below)
  validate.py testpass.py  unchanged; still run on the built page; still the release gate
  reconcile.py             unchanged
  jobs/
    manifest.json          the only record of every job
    STATUS.md              derived from the manifest by job.py. Never edited.
    briefs/<id>/           what a thread receives: BRIEF.md, schema.json, return_template.csv,
                           canonical_keys.txt, reconcile.py, audit_protocol.md
    triage/                what came back and what was done with it
    MERGELOG.md            every value a merge changed, old -> new, with its source
    releases.json          version -> sha256, so a stale version string is a hard stop
  registers/               the three CSV registers, unchanged for now (see "Next")
  dist/                    build output. Git-ignored. Never edited.
```

### A brand record

```json
{
  "name": "J.McLaughlin",
  "band": "accessible", "seat": 66, "dagger": 1,
  "focus":  {"tech": 1, "comfort": 3, "craft": 2, "style": 3},
  "fabric": {"denim": 1, "cashmere": 1, "linen": 2, "cotton": 3, "wool": 2, "synth": 1},
  "dials":  {"reach": 3, "dur": 3, "forg": 3, "fuss": -1, "golffice": -1,
             "golf": 3, "status": 2, "finbro": 2, "ivy": 3, "murica": 3, "prep": 4, "boat": 2, "racquet": 3},
  "why": "…", "origin": "…", "opview": "…", "say": "jay mick-LOCK-lin",
  "chan": ["O"], "conf": "H", "forgc": [3, 3, 1], "shop": "https://…",
  "onething": {"p": "Pima knit polo", "u": "https://…", "n": "…"},
  "prices": [[45, 75], [85, 135], [115, 165], [125, 175], [115, 185], "?", "?", "?"],
  "notes": {"ivy": "…", "golf": "…"},
  "doors": {"c": "full", "n": 164, "cities": [["Alexandria", "VA", 1], …]},
  "cities": "…", "region": {"o": [], "s": [153, 156, …]}
}
```

A dial that is absent is absent — the registry says whether that means *not assessed* (the UI
reads 99) or *not represented* (the UI reads 0), and lint enforces which fields may be absent at
all. The record carries no value it was not given. The rule-one distinction — a checked absence
and an unasked question must never look alike — is now a property of the schema rather than a
discipline the editor has to remember.

### Why per-brand files and not per-const files

Per-const files would have been the minimal change and the wrong one. Every job a thread does is
per brand: a price pass returns one row per brand, a locations pass returns one brand's doors, a
seating adds one brand. A merge that touches one brand should touch one file. A seat should be
one file added. A diff should read `data/brands/fedeli.json | 2 +-`, not `line 1917 | 1 +-`.

Per-const is also how the drift happened. Forty-three lists that must agree is a schema with the
consistency rule left to the operator. One record per brand with a registry over it is the same
data with the rule made structural.

### Why the product is still one HTML file

Because the deploy story works and nothing about it needed to change. `build.py` emits a single
file with no dependencies, uploaded as `index.new.html` and renamed, exactly as before. The
alternative — the page fetching `spectrum.json` at runtime — buys a smaller app file and costs
the ability to open the page from disk, adds a second artefact to keep in step, and moves the
truncation window from one upload to two. Not worth it at 800KB. It becomes worth it if the
data passes ~3MB or if a second consumer (Cyprus front end) wants the data without the page.
The split is a ten-line change to `build.py` when that day comes, and nothing in `data/` moves.

### Why JSON and not CSV

Brand records are nested (prices are eight pairs, doors are a coverage state with a city list,
one-thing is three keys). CSV flattens badly and every worker return is already CSV — that is the
right shape for a *return*, one row per finding, and `job.py` converts it into the record on
merge. The registers (`registers/*.csv`) stay CSV because they are flat.

### Why a registry

`schema/fields.json` is the one file that says what a field is. It replaced five places that
used to know: the `bandEl()` dataset assignments, `validate.py`'s constant lists, the `NOTE_KEYS`
set, the brief templates, and whoever's head held the rule that shoes 1 and 2 are retired. Adding
a dial is now: one registry entry, one marker in the template, and the JS that reads it. Lint,
build, and brief scaffolding pick it up without being told.

---

## What exists now, and what was proven

1. **Extraction is complete and clean.** 204 brands, 807 places, 56 consts. Every brand-keyed
   dict was checked against the roster; one orphan surfaced (`ADDCLOTH` → `"Ralph Lauren"`,
   dropped and logged).
2. **The rebuild is the same page.** The built file was compared against the original three
   ways: every const parsed and compared as data (all equal; dict key order differs, and every
   iteration site was checked — `brandsAt` sorts, the prices table sorts, nothing reads insertion
   order); the non-data lines of the file diffed (zero differences); and both pages rendered in
   Chromium with body text, all 204 chip datasets, and a hover card compared (identical).
3. **Both gates pass on the product.** `validate.py` PASS, `testpass.py` 203/203.
4. **The loop runs end to end.** A job was scaffolded, a synthetic pilot return seeded with the
   classic failures was checked (it caught the duplicate row, the near-miss name, the `N/A`
   provenance, the blank cell, and the all-NC row), a clean return was merged into two brand files,
   lint → build → validate → testpass ran green, and the release gate then refused to ship the
   changed build under the unbumped version. The demo data was reverted; the golf brief was kept
   as the worked example.
5. **Lint found something the old validator could not.** Five brands carry the "all eight garments
   opened and read" tick and still have `"?"` slots — Rhone, Barbour, BOSS, Ferragamo, Fedeli
   (two). Fedeli is on the held-EUR list, so the likeliest reading is that held non-USD figures
   are wearing the not-assessed mark: a checked figure rendering as an unasked question, which is
   rule one. Left as a WARN, not fixed, because it is a ruling.

---

## Orchestrating the threads

The handoff had nine threads in a table it maintained by hand, several of them holding data
"that never reached the build". The orchestrator's whole job is to make that state impossible
to lose: a job exists in the manifest or it does not exist, and its state is set by what
actually happened to its files.

### Lifecycle

```
drafted -> issued -> pilot_returned -> returned -> merged -> closed
                 \-> held (blocked on a ruling; says which)
```

| step | command | what it enforces |
|---|---|---|
| scaffold | `job.py new ID --kind K --title T --brands FILE --pilot N` | brand list must be seated names; refuses otherwise |
| declare columns | `job.py schema ID col:type[:lo:hi] …` | a `key` column and a `provenance` column, always; frozen once issued |
| declare landing | `job.py writes ID dials.golf=col prices.3=col` | column must exist in the schema; a screen with no writes is legal (screens count, never score) |
| issue | `job.py issue ID` | materialises the brief dir with keys, schema, template, reconcile, protocol |
| check a return | `job.py check ID return.csv` | reconcile → column shape → per-row triage into MERGE / HOLD / SKIP / REJECT, with the reason; writes the triage report and a `.merge.csv` of only the rows that survived; hard errors (duplicate rows, wrong columns) block the whole return |
| merge | `job.py merge ID X.merge.csv` | writes into brand files; logs every old→new with source; runs lint immediately |
| release | `job.py release` | lint → build → validate → testpass → hash; **stops if the version was already released at a different hash** |
| board | `job.py status` | prints and rewrites `jobs/STATUS.md`; the only status table |

### What the brief carries

The scaffolded `BRIEF.md` has the protocol's six requirements pre-filled — canonical keys,
flat schema with legal values, required provenance, an explicit not-checked token (`NC`, distinct
from blank, which is an error), an out-of-scope instruction, and a pilot size — plus the stop
conditions from the rubric screens. The operator writes one paragraph ("The job") and sends the
folder. The `return_template.csv` arrives with the brand keys already in it and every cell
already `NC`, so a thread that touches nothing returns a file that says, correctly, that nobody
looked.

### What it does not yet do

- Complex merges. `writes` handles scalars, strings, JSON literals, and one list slot
  (`prices.3`). Doors, fibre, and one-thing need a `kind`-specific merger; the price pass and the
  locations pass are the two jobs that will need one, and each is an afternoon.
- Kind-specific brief templates. One template serves all kinds; the rubric-screen stop
  conditions are in it whether or not they apply.
- It does not read the thread. Sebastian still copies the folder out and the return in. That is
  deliberate: the boundary between the thread and the file is the point.

---

## Day to day

```
# a merge arrives
python3 tools/job.py check price_pass_2026-09 queue3_return.csv
python3 tools/job.py merge price_pass_2026-09 price_pass_2026-09_3.merge.csv
# write the changelog entry in data/changelog.json (bump the version)
python3 tools/job.py release
git add -A && git commit -m "price pass queue 3: 41 brands"
# deploy dist/index.html as index.new.html, rename

# a seat
cp data/brands/_template.json.example data/brands/gant.json
python3 tools/lint.py                                  # tells you exactly which required field is missing
```

Git is the substrate. Two commits exist: the extraction, and the job board. The repo has no
remote; that is the first thing to decide.

---

## Next, in order

1. **A remote.** GitHub, private. Until then the folder is the only copy.
2. **Places get ids.** `region` still points at `places.json` by array index, which means a shop
   inserted anywhere but the end silently re-points every brand. Give each place a stable id
   (slug of name + city), rewrite `region` to use it, and the register CSVs can then move into
   `data/` as the same records — at which point **the visit form's dropdowns are derived from the
   data** rather than rebuilt by hand, which is the fix the handoff put first.
3. **Retire the parallel lists in the template.** `G`/`SHORT`/`TICKS` duplicate
   `PRGARMENTS`/`PRSHORT`/`PRTICKS` inside the prices overlay; `price_slots` in the registry should
   be the one source and the template should read it once.
4. **`testpass.py` reads the data, not the page.** Several of its 203 checks assert counts that
   `spec.load()` can supply; a check that derives its expected value from `data/` cannot go red
   because a seventh brand was counted.
5. **Retire `cities` (prose).** `doors` carries the same information structurally for all 204.
6. **The fibre chase**, the link audit, the other dials — unchanged from the handoff, but each now
   starts with `job.py new`.

---

## Rulings this surfaces, none of which were taken

- The five brands (six slots) whose price tick contradicts their `"?"` slots. If those are held
  non-USD figures, the schema wants a third price token — `"held"` — distinct from `"?"`.
- Whether `ADDCLOTH` meant Polo Ralph Lauren, Purple Label, or both.
- Whether the changelog stays inside the data (it is the version authority, so it travels with
  the build) or becomes a `CHANGELOG.md` the build reads. Left inside.
