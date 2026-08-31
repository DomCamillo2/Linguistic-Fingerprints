# Interpretable Linguistic Fingerprints of LLM Versions

A controlled course project comparing earlier and later open-weight LLM versions with matched prompts and interpretable linguistic features.

## Research question

> Can earlier and later versions within the Llama and Gemma families be distinguished using a small set of interpretable linguistic features, and how robust is this distinction across unseen prompts and writing-task types?

Prior studies already show that generated text can reveal its source model or version. This repository therefore frames the project as a controlled replication and robustness study, not as the discovery of a universal cross-family fingerprint.

The project has three focused goals:

1. measure paired earlier-to-later feature differences inside Llama and Gemma;
2. test simple within-family version classification on unseen prompts;
3. test whether performance survives a completely unseen writing-task type.

Cross-family classifier transfer, mixed-effects models, and clustering are not part of the confirmatory proposal.

## Planned design

| Dimension | Planned value |
|---|---|
| Models | Llama 2 7B Chat → Llama 3.1 8B Instruct; Gemma 2 9B IT → Gemma 3 12B IT |
| Language | English |
| Prompt bank | 100 prompts; 20 per writing-task type |
| Pairing | Every model receives every prompt |
| Output length | 120–150 requested words; actual length audited |
| Sampling | One deterministic response per prompt/model; seed 42 |
| Confirmatory features | 15 interpretable linguistic measures |
| Linguistic analysis | Paired later-minus-earlier contrasts within each family |
| Primary prediction | Prompt-blocked five-fold L2 logistic regression |
| Robustness | Leave one complete writing-task type out |
| Optional exploration | Scaled PCA |

Exact models and settings are recorded in config/models.yaml and config/study.yaml. The main-run freeze occurs only after approval and a successful pilot.

## Why this scope fits the course

The design uses methods covered in the course: linguistic preprocessing, pandas aggregation, hypothesis testing, bootstrap uncertainty, logistic regression, cross-validation, classification metrics, and optional PCA. Prompt grouping and leave-one-task-type-out are leakage-safe adaptations of cross-validation. A mixed model is not required.

The contribution can be a replication, a robustness result, or a well-supported null result. It does not depend on proving a previously unknown universal law.

## Validity rules

- Use the same registered prompt and generation configuration for every model.
- Keep raw generations immutable and preserve exact provenance.
- Pair earlier and later outputs by prompt inside each family.
- Keep every prompt_id in one cross-validation fold.
- Fit imputation and scaling on training data only.
- Report a dummy baseline, balanced accuracy, macro-F1, fold results, and confusion matrices.
- Audit actual length and run a length-aware sensitivity analysis.
- Report family-specific results and avoid causal claims about model age.

See AGENTS.md for operational rules and PROJECT_PLAN.md for the full design.

## Repository map

~~~text
AGENTS.md                    project rules and scientific guardrails
PROJECT_PLAN.md              research design and decision gates
proposal/                    English proposal and checklist
config/                      study and exact model configuration
prompts/                     pilot and final prompt registries
data/raw/                    immutable model outputs
data/interim/                validated intermediate data
data/processed/              extracted feature tables
src/linguistic_fingerprints/ features and evaluation functions
scripts/                     command-line entry points
notebooks/                   planned analysis narrative
reports/                     status, decisions, and known pitfalls
literature/                  verified literature and BibTeX
llm_corpus/                  searchable course extracts
tests/                       automated checks
~~~

## Quick start

~~~bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install .
python -m spacy download en_core_web_sm
python scripts/check_project.py
python -m pytest
~~~

After generation data follows data/README.md:

~~~bash
python scripts/extract_features.py   --input data/raw/generations.csv   --output data/processed/features.csv

python scripts/evaluate_generalization.py   --input data/processed/features.csv   --output reports/evaluation_results.csv
~~~

The evaluation command produces prompt-blocked within-family and leave-one-task-type-out results with the 15 confirmatory features, plus a length-covariate sensitivity variant.

## Current status

The proposal and repository have been simplified to the course-aligned scope. Before the main run:

- obtain supervisor approval;
- install and verify the four exact models;
- complete and review the 100-prompt registry;
- run the four-model pilot;
- audit length, failures, formatting, provenance, and annotations;
- record the post-pilot analysis freeze.

Open decisions are tracked in proposal/PROPOSAL_CHECKLIST.md.
