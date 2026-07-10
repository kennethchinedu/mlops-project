# Curriculum: One Production ML System, Built by You

**The core goal:** build a real, end-to-end, automated MLOps project — dataset → cleaning → training → experiment tracking (MLflow) → serving (FastAPI) → containers (Docker) → CI/CD (GitHub Actions) → Kubernetes serving (KServe) → monitoring & automated retraining — and through building it, become genuinely good at Python and ready to work as an **entry-level MLOps engineer**.

Python is not a separate course: every Python concept is taught right before the project needs it, then immediately used in the project. The student writes ALL code (see CLAUDE.md).

A milestone is "done" only when: the code passes teacher review, the milestone quiz is passed, and the work is committed with clean history. Capstone-level milestones (M2, M4, M6, M8) get a deep review by the `capstone-reviewer` agent.

---

## M0 — Foundations (env, git, GitHub)
The project's home. Lessons: which Python runs and why (PATH), venv isolation, git basics, GitHub remote, `.gitignore`, commit hygiene.
**Exit:** repo on GitHub, venv working, student can explain the three git states cold.

## M1 — Python core, taught through data
The minimum Python to touch data honestly: variables/types/strings, lists/dicts/sets, control flow, functions, exceptions & tracebacks, reading files (CSV/JSON), modules and `__main__`, project layout.
**Project deliverable:** a small CLI tool that loads a raw dataset file and prints basic facts about it (row count, columns, missing values per column) — written with the standard library only, no pandas yet, so the student feels what pandas later saves them from.
**Exit:** deliverable passes review; student explains their own code line by line.

## M2 — Dataset, EDA & a real cleaning pipeline  *(capstone review)*
Choose the project dataset (student decides, teacher advises: tabular, real-world messiness, a clear prediction target — the `Mlops/Datasets` folder is a candidate source). Learn NumPy essentials and pandas properly.
New Python here (just-in-time): type hints, `pytest` (tests for every cleaning function), logging module, dataclasses/config objects, comprehensions.
**Project deliverable:** `src/` package with a tested, logged, config-driven cleaning pipeline: raw file in → clean training file out, rerunnable, deterministic.
**Exit:** pipeline runs end-to-end on the raw data; tests pass; review PASS.

## M3 — Training pipeline + MLflow
scikit-learn workflow: split, baseline, fit, metrics, avoiding leakage. Reproducibility: seeds, pinned deps, config-driven runs. MLflow: tracking server, log params/metrics/artifacts, compare runs, model registry, promote a model.
New Python: decorators (as used by tools), context managers, packaging with `pyproject.toml`.
**Project deliverable:** `train.py` that reads config, runs the pipeline, logs everything to MLflow, and registers the model. Several tracked experiments with an honest comparison.
**Exit:** student can point at MLflow UI and defend which model was promoted and why.

## M4 — Serving: FastAPI + real error handling  *(capstone review)*
HTTP basics, FastAPI, pydantic validation, loading the registered model, a `/predict` endpoint, a `/health` endpoint. Error handling as a first-class topic: invalid input, missing model, malformed payloads — correct status codes, no stack traces leaking to clients. Tests for the API (happy path + every failure path).
**Exit:** API survives hostile input in review; all failure paths tested.

## M5 — Docker
Images vs containers, Dockerfile for the API (layers, caching, slim images, non-root), `.dockerignore`, docker-compose to run API + MLflow together locally.
**Exit:** `docker compose up` brings up the whole system from a clean clone; student explains every Dockerfile line.

## M6 — CI/CD with GitHub Actions  *(capstone review)*
Pipelines as code: on every push → lint (ruff) + tests; on main → build the Docker image and push to a registry. Secrets management, branch protection, the PR workflow (student opens PRs to themself and I review them there).
**Exit:** a red build blocks merge; a green merge produces a pushed image with zero manual steps.

## M7 — Kubernetes + KServe
Why orchestration exists. k8s core objects: Pod, Deployment, Service, namespace — hands-on with a local cluster (kind or minikube). Then KServe: InferenceService serving the MLflow model, request/response, scaling behavior. (Cloud deploy of the FastAPI variant as a fallback/optional extra, e.g. Render.)
**Exit:** the model answers predictions through KServe on the cluster; student can explain the path a request takes.

## M8 — Monitoring, drift & automated retraining  *(final capstone)*
Structured logging, metrics (Prometheus + Grafana basics: latency, error rate, request volume), alerting on what matters. Data drift concept + a drift check (e.g. Evidently). Scheduled retraining job; automated model promotion with a quality gate; rollback story.
**Final deliverable — the actual core goal:** push a change → CI tests → image built → deployed → serving on k8s → monitored → retraining loop functioning. All automated, all built by the student.

---

## Final assessment — "entry-level MLOps engineer" gate

Not done until ALL pass:
1. **Python check:** solve unseen small problems live (no hints), explain any line of the project when pointed at randomly.
2. **System walkthrough:** whiteboard-style — draw the full architecture from memory and justify every tool choice ("why MLflow", "why a registry", "why KServe over plain FastAPI on k8s").
3. **Breakage drill:** I break something (bad model, failing test, dead container, wrong config) — the student must diagnose from logs/CI output alone and fix it.
4. **Mock interview:** standard entry-level MLOps interview questions across all milestones; weak spots trigger targeted re-drills until closed.

## Rules
- No copy-paste from tutorials; type everything, understand everything.
- Every deliverable is committed with meaningful history and reviewed before moving on.
- Weak spots go to PROGRESS.md and get re-quizzed until they die.
