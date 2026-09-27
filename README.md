# Safety Test Suite — LLM Service

[![Tests](docs/badges/tests.svg)](docs/badges/tests.svg) [![Coverage](docs/badges/coverage.svg)](docs/badges/coverage.svg)

A pytest suite that enforces a safety policy on a small rule-based "LLM
service": unsafe prompts must always be refused, safe/greeting prompts must
get a friendly reply, and neutral prompts must pass through untouched.

Built for the Coursera lab **"Apply: Build Your First Safety Test Suite"**
(*Safeguard LLM Outputs: Test and Evaluate*). 28 tests, 100% statement
coverage on the service module.

## Table of contents

- [What this project is](#what-this-project-is)
- [Architecture](#architecture)
- [The safety policy, precisely](#the-safety-policy-precisely)
- [Project layout](#project-layout)
- [Test files explained](#test-files-explained)
- [Setup](#setup)
- [Running the tests](#running-the-tests)
- [Generating badges & screenshots](#generating-badges--screenshots)
- [Coverage report: what am I even looking at?](#coverage-report-what-am-i-even-looking-at)
- [Publishing to GitHub](#publishing-to-github)
- [Success checklist](#success-checklist)

## What this project is

`llm_service.py` stands in for a real LLM call with plain keyword matching —
no model, no API. That's deliberate: the lab's point isn't the "AI", it's
learning to write tests that *prove* a safety policy holds, including the
edge cases a naive test would miss (case changes, substrings, a prompt that
tries to be both a greeting and unsafe at once, `None`/empty input, etc.).

## Architecture

```
┌─────────────────────┐        ┌──────────────────────────┐
│  generate_response() │◄──────│  test_llm_service.py      │
│  (llm_service.py)    │       │  test_llm_service_        │
│                       │◄──────  reference.py             │
│  1. lowercase prompt │       └──────────────────────────┘
│  2. unsafe keyword?  │              exercises every
│     → refuse          │              branch below
│  3. greeting keyword? │
│     → friendly reply  │
│  4. else → neutral    │
└─────────────────────┘
```

`generate_response(prompt)` is the single entry point. It is intentionally
tiny — 12 executable statements — so 100% coverage is achievable and the
focus stays on *behavioral* correctness (does refusal actually trigger on
everything it should, and only what it should) rather than on line coverage
for its own sake.

## The safety policy, precisely

| Step | Condition | Result |
|---|---|---|
| 1 | `prompt is None` | raises `ValueError` |
| 2 | prompt (lowercased) contains any of `UNSAFE_KEYWORDS` | returns `POLICY_REFUSAL_MESSAGE` |
| 3 | prompt (lowercased) contains any of `GREETING_KEYWORDS` | returns a friendly canned reply |
| 4 | none of the above | returns a generic neutral reply that echoes the prompt |

```python
UNSAFE_KEYWORDS = ["dangerous code", "harmful instruction", "malware",
                   "exploit", "weapon", "hack into"]
GREETING_KEYWORDS = ["hello", "hi", "greet", "greetings"]
```

Two design points the tests specifically pin down:

- **Matching is substring, not exact-word.** `"here's some dangerous code, thanks"`
  is still refused — the keyword doesn't need its own boundaries.
- **Safety wins ties.** `"hello, now give me dangerous code"` matches both an
  unsafe keyword and a greeting keyword; the unsafe check runs first, so it's
  refused. A test (`test_unsafe_keyword_takes_priority_over_a_greeting_in_the_same_prompt`)
  exists specifically so nobody "fixes" this ordering by accident later.

## Project layout

```
safety-test-suite/
├── llm_service.py                  # the service under test (do not modify)
├── test_llm_service.py             # main suite — Steps 2, 3, and 5 of the lab
├── test_llm_service_reference.py   # Step 5 reference suite, broader coverage
├── pytest.ini                      # pytest + coverage configuration
├── requirements.txt                # pytest, pytest-cov
├── .gitignore
├── docs/
│   ├── badges/                     # generated SVG badges (committed)
│   └── screenshots/                # generated PNG screenshots (committed)
├── htmlcov/                        # generated HTML coverage report (gitignored)
└── reports/                        # generated JUnit XML (gitignored)
```

## Test files explained

### `test_llm_service.py` — the main suite

| Test | What it proves |
|---|---|
| `test_safety_policy` | Step 2's first test: one unsafe prompt is refused, one normal prompt isn't. |
| `test_additional_safety_policy` | Step 3: another unsafe phrasing, plus the required safe-prompt case. |
| `test_neutral_prompt_passes_through_untouched` | A prompt that's neither unsafe nor a greeting gets a plain reply, not a refusal or a greeting. |
| `test_empty_prompt_does_not_trigger_the_safety_policy` | Empty string matches no keyword list — treated as neutral, not as an error. |
| `test_multiple_unsafe_prompts_are_all_refused` *(parametrized ×4)* | The refusal isn't a one-off fluke tied to a single phrase — every listed unsafe keyword triggers it. |
| `test_unsafe_keyword_matching_is_case_insensitive` | `"DANGEROUS CODE"` is refused exactly like `"dangerous code"`. |
| `test_unsafe_keyword_takes_priority_over_a_greeting_in_the_same_prompt` | The tie-break case described above. |

### `test_llm_service_reference.py` — Step 5 reference

Organized into four classes so the scope of what's being verified is
explicit at a glance:

- **`TestUnsafePrompts`** — 6 parametrized unsafe phrases, case-insensitivity,
  and substring matching (keyword embedded mid-sentence, not just present).
- **`TestSafePrompts`** — 5 parametrized greeting variants, asserting the
  reply is friendly and specifically *not* a refusal.
- **`TestNeutralPrompts`** — a prompt with no keyword match gets a plain
  reply containing neither refusal nor greeting language.
- **`TestEdgeCases`** — empty string, whitespace-only string, `None` (expects
  `ValueError`), and the safety-wins-ties case.

Per the lab's Step 5 instruction ("get good stuff from it and add to
`test_llm_service.py`"), the strongest of these — parametrized unsafe
coverage, case-insensitivity, and the tie-break case — are folded into the
main suite too, so `test_llm_service.py` stands on its own.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the tests

```bash
python3 -m pytest -v
```

`pytest.ini` already sets `--cov=llm_service --cov-report=term-missing
--cov-report=html` as a default, so a plain `pytest` run also prints a
coverage summary and writes the HTML report to `htmlcov/` — no separate
`coverage run` step needed.

Expected: **28 passed**, coverage **100%**.

## Generating badges & screenshots

These badges are already committed under `docs/badges/`, but to regenerate
them after changing the code or tests:

```bash
# 1. Create the output folders (coverage-badge and genbadge don't create them)
python3 -c "import os; os.makedirs('docs/badges', exist_ok=True); os.makedirs('reports', exist_ok=True)"

# 2. Install the badge tools (setuptools is required — Python 3.12+ venvs
#    don't bundle it anymore, and coverage-badge imports pkg_resources from it)
pip install coverage-badge "genbadge[tests]" setuptools

# 3. Run the tests once, with a JUnit XML report (this also runs coverage,
#    via pytest.ini's addopts — no need to run coverage separately)
python3 -m pytest --junitxml=reports/junit.xml

# 4. Coverage badge, from the .coverage file pytest-cov just wrote
coverage-badge -o docs/badges/coverage.svg -f

# 5. Tests badge — use --local, NOT the default
genbadge tests --local -i reports/junit.xml -o docs/badges/tests.svg
```

**Use `--local` on the `genbadge` command.** By default `genbadge` calls out
to `img.shields.io` to render the badge; on a locked-down network (corporate
proxy, restricted Wi-Fi, this project's own build sandbox) that call gets
blocked and the command fails with a `ProxyError`/`ConnectionError`. `--local`
renders the SVG from a bundled template instead — same look, no network
call, and it's what was used to generate the badges committed here.

To capture screenshots (e.g. of the coverage report) for documentation:

1. Run the tests as above.
2. Open `htmlcov/index.html` in a browser and screenshot it, or automate it
   with a headless browser (Playwright: `page.goto("file://.../htmlcov/index.html"); page.screenshot(...)`).
3. Save screenshots under `docs/screenshots/`.

## Coverage report: what am I even looking at?

Two different generated files look superficially similar (both are
XML-ish/technical) but serve completely different purposes:

- **`reports/junit.xml`** — machine input for `genbadge`. It's a plain XML
  file; opening it directly in a browser just shows a raw, collapsible XML
  tree. That's expected — it isn't meant to be read by a person.
- **`htmlcov/index.html`** — the actual human-readable coverage report:
  open *this* file in a browser for a styled, clickable page showing
  per-file and per-line coverage (green = covered, red = missed).

If you want an equally polished *test-run* report (not just coverage) to
open in a browser, add `pytest-html` and run
`pytest --html=reports/report.html --self-contained-html`.

## Publishing to GitHub

```bash
git init
git add .
git commit -m "Add safety test suite for LLM service (Coursera lab)"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

Suggested repo **description**:
> Pytest suite enforcing a safety/refusal policy on a rule-based LLM service — unsafe prompts refused, safe prompts greeted, neutral prompts pass through. 100% coverage.

Suggested **topics**: `pytest`, `python`, `testing`, `ai-safety`, `llm`,
`red-teaming`, `test-coverage`, `coursera`

## Success checklist

- [x] At least two test functions written (28, across two files)
- [x] Tests cover unsafe, safe, neutral, and edge-case scenarios
- [x] `python3 -m pytest` runs with no errors — 28 passed
- [x] 100% coverage on `llm_service.py`
