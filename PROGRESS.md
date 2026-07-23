# Progress

**Goal:** one end-to-end automated MLOps project (see CURRICULUM.md) + entry-level MLOps engineer readiness
**Current milestone:** M1 — Python core, taught through data
**Current lesson:** 1.4 — not yet assigned
**Project dataset:** not chosen yet (decided in M2)

## Daily targets — 2026-07-23
- [ ] Assign and start lesson 1.4

## Completed lessons
- 0.1 — Python verification + git basics (PASSED 2026-07-10 after 3 review rounds)
- 0.2 — Virtual environments (PASSED 2026-07-10; needed several rounds on PATH/activation mechanism but demonstrated it in the end, incl. correct two-terminal prediction)
- 0.3 — pip freeze & requirements.txt (PASSED 2026-07-11; exercise flawless, but needed full walkthrough on freeze-vs-install-r direction; re-verified by rebuilding env from memory)
- 0.4 — GitHub remote & push (PASSED 2026-07-11; repo live at github.com/kennethchinedu/mlops-project, tracking set up, proved commit→push loop; initially left answers uncommitted — good lesson in "unpushed = at risk")
- 1.1 — Variables, types, strings, f-strings, input() (PASSED 2026-07-11 after 4 review rounds; recurring issues: skimming feedback instead of reading it — 3 items re-flagged; pasted docs example code verbatim; confused `//` with `%` repeatedly before clearing it)
- 1.2 — Lists, dicts, loops: mini data-quality profiler (PASSED 2026-07-16 after 6 review rounds; bugs hit in order: `=+1` typo instead of `+=`, inverted if/else logic, `elif` chaining independent checks (masked missing values when multiple fields were None in the same row), crash calling `.items()` on a list, leftover unlabeled prints alongside the report, stray `input()` left over from lesson 1.1 habits. Good: self-corrected `==` to `is None` once, built a harder test dataset with overlapping missing fields unprompted.)
- 1.3 — Functions: split profiler into `dataset_summary` (counts, returns 4 values as a tuple) + `data_info` (prints report) (PASSED 2026-07-23 after ~9 review rounds; bugs hit in order: indexed a string key (`key["name"]`) instead of comparing `key`/`value` directly, inverted check (`if key is None` instead of `if value is None`), `UnboundLocalError` from `missing_name`/`row_count` declared outside the function while mutated inside — first real collision with function scope, swapped which function's call needed unpacking vs. which needed arguments passed in, row count incremented once per field instead of once per row (loop-nesting mistake, same class of bug as lesson 1.2). Good: correctly used `elif` for the three key checks since they're genuinely mutually exclusive (contrast with the 1.2 `elif` bug); once shown the tuple-unpacking mechanism via a tiny isolated REPL example, applied it correctly to the real 4-value case unprompted. Also hit a GitHub push 403 — stale `hexanams` credential cached in macOS osxkeychain; fixed by clearing the Keychain entry and re-authenticating as `kennethchinedu`.)

## Weak spots to revisit
- Commit message quality — STILL OPEN: 2026-07-11 commits were diary-style ("learnt about datatypes...") instead of describing the snapshot; next diary-style message gets rejected
- Answering "why" questions with mechanisms, not restated facts
- Reading review feedback fully before fixing — 3 items had to be re-flagged in lesson 1.1
- `//` (floor division) vs `%` (remainder) — cleared verbally 2026-07-11, re-quiz later to confirm
- `elif` vs independent `if`s — confused these when checking multiple unrelated conditions on the same row (lesson 1.2 round 3); understood after being asked to trace a row with two missing fields through the chain
- `=+` vs `+=` typo — caught in lesson 1.2 round 2 review, not yet re-quizzed
- `== None` vs `is None` — flagged twice in lesson 1.2 (reverted once after fixing), self-corrected on final round; re-quiz to confirm it's stuck
- Leaves stray/leftover code from earlier drafts (dead prints, unused input()) instead of cleaning before submitting for review — recurring across lesson 1.2 rounds 3-5; NOTE: cleaned up unprompted before final submission in lesson 1.3, first time doing so without being told
- Function scope (reading a variable declared outside a function is fine, but `+=`/reassigning it inside without passing it in triggers `UnboundLocalError`) — hit live in lesson 1.3 round 4-5; re-quiz to confirm it's stuck
- Mixing up which function's call needs tuple-unpacking (`a, b = f()`) vs. which needs values passed as arguments (`g(a, b)`) — confused in lesson 1.3; cleared after being walked through a minimal 2-value REPL example separate from the real code

## Cleared weak spots
- 2026-07-11 M0 quiz (5/5): staging vs tracked ✓, PATH/venv activation ✓, freeze vs install -r ✓ — all answered cold

## Review notes
- 2026-07-10 — Lesson 0.1 review #1: **NOT YET.** Python 3.13.7 ✓, git init ✓, config ✓. Missing: notes.md (main deliverable, answers were written into the assignment sheet instead); commit message was the instruction text pasted verbatim; used `git add .` instead of selective staging; Q1/Q3 check answers didn't answer the question. Positive: created .gitignore unprompted to exclude teacher files.
- 2026-07-16 — Lesson 1.2 review, 6 rounds, final verdict **PASS**. Final script: 5-row list-of-dicts dataset, independent `if age/city/name is None` checks (not `elif`), correct counters for rows + missing-per-key, single f-string report, no `input()`. Still owed before lesson 1.3: answer the two "check yourself" questions in notes.md (dict-vs-.items() looping; empty-list edge case), then commit + push with a non-diary message.
- 2026-07-23 — Lesson 1.3 review, ~9 rounds, final verdict **PASS**. Final script: `dataset_summary(dataset)` returns `(missing_city, missing_name, missing_school, row_count)` as a tuple; `data_info(...)` takes those 4 values and prints the report; both functions run correctly against two differently-shaped datasets (2-row and 5-row) with verified-by-hand counts. All 3 check-yourself questions answered correctly in notes.md (parameter vs. argument initially swapped, corrected on request). Also resolved a git push 403 (stale `hexanams` credential in macOS Keychain) by clearing the osxkeychain entry and re-authenticating as `kennethchinedu` — both commits pushed and confirmed against `origin/main`.
