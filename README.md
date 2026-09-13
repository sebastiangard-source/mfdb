# mfdb — The Menswear Spectrum

Source lives in `data/` and `app/template.html`. The page is built, not edited.

    python3 tools/lint.py        check the data
    python3 tools/build.py       build dist/
    python3 tools/job.py         orchestrate worker threads (run with no args for help)
    python3 tools/job.py release lint -> build -> validate -> testpass -> hash

Read `ARCHITECTURE.md` for why, `audit_protocol.md` for how threads are briefed,
`jobs/STATUS.md` for where every thread is.
