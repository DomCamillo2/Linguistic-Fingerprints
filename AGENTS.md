# AGENTS.md — Linguistic Fingerprints

Read this file before changing the project. It is the authoritative guide for LLMs and coding agents.

## 1. Mandatory read order

1. `AGENTS.md`
2. `PROJECT_PLAN.md`
3. `reports/PREP_STATUS.md`
4. `reports/CHANGELOG_RUNS.md`
5. `reports/MISTAKES.md`
6. Only then open the files needed for the current task.

For course questions, begin at `llm_corpus/INDEX.md`, open only the relevant lecture or assignment Markdown, and cite the YAML `source_pdf` plus the nearest `<!-- page:N -->` marker.

## 2. Locked scientific framing

This is a controlled corpus-linguistic study of whether interpretable predecessor-successor differences generalise across selected open-weight model families and unseen writing-task types.

It is **not**:

- a general old-versus-new model leaderboard;
- a test of factual correctness, intelligence, or overall writing quality;
- a detector intended to identify arbitrary AI-generated text;
- the first matched-prompt or interpretable comparison of LLM versions;
- evidence about all model generations from four selected models.

Primary question:

> To what extent do linguistically interpretable predecessor-successor differences generalise across open-weight model families and text genres?

The main scientific object is the generalisation pattern of the interpretable linguistic feature profile. Classification is an evidential tool, not the end goal. Within-family separability is a baseline; cross-genre and cross-family transfer are the primary contribution.

## 3. Experimental unit and identifiers

The experimental unit is one generated response to one registered prompt by one exact model version.

Required keys:

- `prompt_id`: stable ID for a prompt;
- `model_id`: stable project ID;
- `family`: matched model family;
- `generation`: `earlier` or `later` within that family;
- `run_id`: unique generation-run ID.

Never use display names alone as provenance. Preserve provider/model identifiers, revision or digest when available, access date, system prompt, decoding settings, and raw response.

## 4. Hard validity constraints

1. Every model receives the exact same registered prompt text.
2. Freeze the system prompt and generation configuration before the main run.
3. Keep requested output length identical. Record actual length; do not silently truncate or claim that the prompt instruction alone controls length.
4. Raw generations are immutable. Corrections create a new `run_id` and retain the failed run.
5. Use the same linguistic pipeline and model version for all texts.
6. Use normalized rates for count features where appropriate.
7. Prefer MATTR/MTLD-style diversity measures; raw TTR is descriptive only.
8. Standardize numeric features before PCA, distance-based clustering, linear SVM, or regularized regression.
9. Fit scalers, imputers, feature selection, and PCA inside training folds for predictive evaluation.
10. Ordinary cross-validation must be grouped by `prompt_id`. Leave-one-task-type-out evaluation must withhold the complete task type. Direct cross-family transfer may use the matched prompt bank because prompt is balanced across labels, but the stricter cross-family/unseen-prompt result must also be reported.
11. Report uncertainty and effect sizes, not only p-values or accuracy.
12. Treat PCA and clustering as exploratory. Inspect loadings and stability before interpretation.
13. Set and log random seeds for every stochastic procedure.
14. Report cross-family transfer in both directions and family-specific effects before any aggregate.
15. Do not claim a universal generation effect from the selected models.
16. Describe findings as differences associated with the selected predecessor-successor relation, not changes caused by newer-generation training.

## 5. Analysis priority

1. Data audit, length audit, and descriptive summaries.
2. Paired feature contrasts within prompt and model family, including direction concordance.
3. Leave-one-task-type-out evaluation within each family.
4. Cross-family transfer in both directions, plus the unseen-prompt robustness variant.
5. Prompt-blocked within-family classification as a baseline.
6. PCA for visualization, with scaling and loading inspection.
7. Clustering only as a secondary exploratory analysis with stability checks.

Use the preregistered L2-regularized logistic regression for every primary transfer comparison. A linear SVM or random forest may be a clearly labeled robustness check, but correlated feature importances must not be read causally. Never tune a model on the held-out family or task type.

## 6. Proposal-level decisions and remaining freeze

Recorded in `config/study.yaml` and `config/models.yaml`:

- exact Llama and Gemma versions;
- English as the sole study language;
- one deterministic generation per prompt/model;
- 100 prompts, split equally across five task types;
- 30 confirmatory features;
- paired bootstrap/permutation inference;
- leave-one-task-type-out evaluation;
- Llama → Gemma and Gemma → Llama transfer;
- prompt-blocked cross-family/unseen-prompt robustness evaluation;
- prompt-blocked within-family logistic regression as a baseline.

Still pending are supervisor approval, installation verification, completion of the 100-prompt bank, the four-model pilot, and the post-pilot main-run freeze.

Do not start the main collection until these values are recorded in `config/study.yaml` and `config/models.yaml` and the pilot has passed.

## 7. Data handling

- `data/raw/`: append-only generations and provenance; never edit in place.
- `data/interim/`: validated/reshaped data that can be regenerated.
- `data/processed/`: feature tables and analysis-ready outputs that can be regenerated.
- Never commit API keys, tokens, provider account data, or private prompts.
- Generated corpora may be committed only after license, terms, privacy, and file-size checks.

## 8. Reproducibility and run logging

Every material run must append to `reports/CHANGELOG_RUNS.md`:

- timestamp;
- command or notebook;
- input and output paths;
- configuration hash or relevant settings;
- seed;
- result and anomalies.

Do not erase failed attempts. Document why a run was superseded.

## 9. Course proposal fidelity

Major deviations from the approved proposal must be explicitly justified. Update the proposal, `PROJECT_PLAN.md`, and the run log together when the design changes.

## 10. Do not

- mix prompts across CV folds;
- choose features after looking at test-set performance;
- pool families without also showing family-specific contrasts;
- interpret separation in a plot as proof of a stable effect;
- describe model release date alone as a causal variable;
- upload original course PDFs or official solutions to this public repository;
- fabricate citations, model metadata, or missing results.
