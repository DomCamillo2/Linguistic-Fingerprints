# AGENTS.md — Linguistic Fingerprints

Read this file before changing the project. It is the authoritative guide for LLMs and coding agents.

## 1. Mandatory read order

1. AGENTS.md
2. PROJECT_PLAN.md
3. reports/PREP_STATUS.md
4. reports/CHANGELOG_RUNS.md
5. reports/MISTAKES.md
6. Only then open the files needed for the current task.

For course questions, begin at llm_corpus/INDEX.md, open only the relevant lecture or assignment Markdown, and cite the YAML source_pdf plus the nearest page marker.

## 2. Locked scientific framing

This is a controlled corpus-linguistic replication and robustness study. It compares an earlier and a later version within the Llama family and within the Gemma family using identical prompts and a small set of interpretable linguistic features.

Primary question:

> Can earlier and later versions within the Llama and Gemma families be distinguished using a small set of interpretable linguistic features, and how robust is this distinction across unseen prompts and writing-task types?

It is not:

- a general old-versus-new model leaderboard;
- a causal test of model age or newer training;
- a detector intended to identify arbitrary AI-generated text;
- the first matched-prompt or interpretable comparison of LLM versions;
- a claim that one fingerprint transfers across all model families;
- a test of factual correctness, intelligence, or overall writing quality.

The contribution is a transparent replication on two selected open-weight version pairs plus one robustness extension across task types. Novelty is useful but not required for the course project; a carefully controlled replication or a null result is valid.

## 3. Experimental unit and identifiers

The experimental unit is one generated response to one registered prompt by one exact model version.

Required keys:

- prompt_id: stable ID for a prompt;
- model_id: stable project ID;
- family: matched model family;
- generation: earlier or later within that family;
- run_id: unique generation-run ID.

Preserve provider/model identifiers, revision or digest, access date, system prompt, decoding settings, and raw response.

## 4. Hard validity constraints

1. Every model receives the exact same registered prompt text.
2. Freeze the system prompt and generation configuration before the main run.
3. Keep requested output length identical and audit actual length.
4. Raw generations are immutable. A retry creates a new run_id.
5. Use the same linguistic pipeline and model version for every text.
6. Use normalized rates for count features where appropriate.
7. Raw TTR is descriptive only; MATTR is the confirmatory diversity measure.
8. Fit imputation and scaling inside each predictive training fold.
9. Ordinary cross-validation must keep every prompt_id entirely in one fold.
10. Leave-one-task-type-out evaluation must withhold the complete task type.
11. Report family-specific effects and classifier results; do not pool away opposing directions.
12. Report uncertainty, effect sizes, balanced accuracy, macro-F1, a dummy baseline, and confusion matrices.
13. PCA is optional and exploratory. Scale features and inspect loadings.
14. Set and log random seeds.
15. Describe findings as associations with the selected deployed model versions, not changes caused by release date or newer training.

## 5. Analysis priority

1. Corpus, provenance, failure, formatting, and length audit.
2. Paired later-minus-earlier feature contrasts within prompt and family.
3. Prompt-blocked five-fold L2 logistic regression within each family.
4. Leave-one-task-type-out evaluation within each family.
5. Length-aware sensitivity analysis.
6. Optional PCA visualisation.

Mixed-effects models, clustering, cross-family classifier transfer, neural detectors, and model-quality evaluation are outside the confirmatory plan. Existing cross-family helper functions may be retained for future reuse, but they must not be presented as proposal analyses without an explicit proposal amendment.

## 6. Proposal-level decisions and remaining freeze

Recorded in config/study.yaml and config/models.yaml:

- four exact Llama and Gemma versions;
- English as the sole study language;
- one deterministic generation per prompt/model;
- 100 prompts split equally across five task types;
- 15 confirmatory features;
- paired prompt-level comparisons with bootstrap uncertainty;
- paired t-tests with Bonferroni correction;
- prompt-blocked within-family logistic regression;
- leave-one-task-type-out robustness evaluation;
- actual-length audit and sensitivity analysis;
- optional scaled PCA.

Still pending are supervisor approval, installation verification, completion of the 100-prompt bank, the four-model pilot, and the post-pilot main-run freeze.

Do not start the main collection until the proposal is approved and the pilot has passed.

## 7. Data handling

- data/raw/: append-only generations and provenance;
- data/interim/: validated or reshaped data that can be regenerated;
- data/processed/: feature tables and analysis-ready outputs;
- never commit secrets, private prompts, or unreviewed generated corpora.

## 8. Reproducibility and run logging

Every material run must append to reports/CHANGELOG_RUNS.md with timestamp, command or notebook, input/output paths, relevant settings, seed, result, and anomalies. Never erase failed attempts.

## 9. Course proposal fidelity

Major deviations from the approved proposal require explicit justification. Update the proposal, PROJECT_PLAN.md, configuration, and run log together when the design changes.

## 10. Do not

- mix prompts across folds;
- choose features after seeing test performance;
- treat the 400 response rows as independent in paired inference;
- overclaim novelty or generalisation;
- interpret a PCA plot as proof;
- upload original course PDFs or official solutions to this public repository;
- fabricate citations, model metadata, or results.
