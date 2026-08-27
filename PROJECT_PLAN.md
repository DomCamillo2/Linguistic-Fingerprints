# Project plan

## Working title

**Generalising Linguistic Fingerprints across LLM Families and Genres**

## Research question and contribution

> To what extent do linguistically interpretable predecessor-successor differences generalise across open-weight model families and text genres?

The study no longer treats mere separability of earlier and later models as the contribution. Prior work already compares Llama 2 and Llama 3 under matched prompts with interpretable stylometry and topic-grouped cross-validation. The remaining gap is narrower: whether predecessor-successor signals transfer across open-weight families and unseen writing-task types under one compact, prespecified feature inventory.

The two primary generalisation targets are:

1. **Cross-genre:** train on four writing-task types and evaluate on the fifth, separately within Llama and Gemma.
2. **Cross-family:** train an earlier-versus-later classifier on Llama and evaluate it on Gemma, then reverse the direction.

A stricter robustness analysis combines cross-family transfer with unseen prompts. Within-family prompt-blocked classification is retained only as a baseline.

## Operational definition and claim boundary

“Generation” is shorthand for the documented predecessor-successor relation between two selected versions inside a family:

```text
Llama: Llama 2 7B Chat → Llama 3.1 8B Instruct
Gemma: Gemma 2 9B Instruction Tuned → Gemma 3 12B Instruction Tuned
```

The estimand is a difference **associated with** these version transitions under the recorded runtime. It is not a causal effect of newer training: architecture, tokenizer, data, parameter count, post-training, alignment, and native chat templates also change. With two families, a shared direction is a replicated pattern in these pairs, not a universal LLM generation effect.

## Hypotheses

- **H1 — Interpretable predecessor-successor contrasts:** at least one prespecified feature differs within at least one family after paired inference and false-discovery-rate correction.
- **H2 — Cross-family directional replication:** a prespecified subset of feature directions agrees between Llama and Gemma. Effect estimates and uncertainty, not a binary sign count alone, determine interpretation.
- **H3 — Cross-genre generalisation:** the fixed L2-logistic pipeline retains above-baseline balanced accuracy when each writing-task type is held out in turn, reported separately by family.
- **H4 — Cross-family transfer:** a classifier trained on one family transfers above baseline to the other family in both directions. The cross-family/unseen-prompt variant is the stronger robustness test.

PCA and clustering are exploratory and are not hypotheses. A result where H1 is supported but H3/H4 are not is substantively important: it indicates version-specific fingerprints without a transferable generation-associated pattern.

## Study matrix

| Factor | Levels/role |
|---|---|
| `family` | Llama, Gemma; transfer domain and fixed moderator |
| `generation` | earlier/later within family; prediction target |
| `model_id` | four exact versions; nested in family × generation |
| `prompt_id` | 100 registered prompts; repeated-measures group |
| `task_type` | five writing-task types; cross-genre holdout domain |
| response | one deterministic text per prompt/model cell |

Main corpus: 100 prompts × 4 models = 400 texts. Every task type contains 20 prompts. One deterministic generation does not estimate decoding variance; this remains an explicit scope limitation.

## Prompt design

The prompt bank is balanced across explanation, narrative, argumentation, advice/instructions, and reflection/description. Each prompt must:

- request the same 120–150-word range;
- avoid model identity or generation cues;
- be answerable without browsing;
- avoid sensitive personal data;
- have a stable `prompt_id`, version, and task type;
- be sent unchanged to every model;
- pass pilot checks for refusals, formatting artifacts, and sufficient valid pairs.

The prompt instruction does not itself control actual length. Actual word count is audited, feature rates are normalised where appropriate, and the primary conclusions require length-aware sensitivity analyses.

## Feature inventory

The 30 confirmatory features are defined once in `src/linguistic_fingerprints/features.py` as `CONFIRMATORY_FEATURES`. They cover:

- lexical diversity and repetition;
- mean word and sentence length plus sentence-length variation;
- function words, modals, connectives, punctuation, and contractions;
- paragraph/list/heading structure and adjacent-sentence overlap;
- 13 UPOS proportions.

`n_surface_tokens`, `n_words`, and raw TTR are audit-only variables. No confirmatory feature may be selected or removed after viewing target-family or held-out-task performance. All measures use the same pinned linguistic pipeline for all models.

## Analysis plan

### A. Audit and paired description

- confirm complete prompt × model coverage and exact provenance;
- report failures, refusals, formatting problems, and actual length distributions;
- manually audit a stratified annotation sample;
- calculate `later − earlier` for every prompt, feature, and family;
- report family-specific means, standardized paired effects, and 95% prompt-bootstrap intervals;
- use two-sided paired permutation tests and Benjamini-Hochberg correction across the 60 feature/family tests at `q=0.05`;
- summarize cross-family sign concordance with effect intervals visible.

These analyses establish what changes. They do not by themselves establish generalisation.

### B. Cross-genre generalisation — primary

For each family and each of the five task types:

1. train the fixed L2-logistic pipeline on the other four task types;
2. fit median imputation and standardisation on training rows only;
3. test on every response in the held-out task type;
4. report balanced accuracy, macro-F1, ROC-AUC, confusion counts, and uncertainty;
5. report all family × held-out-task cells, not only an average.

The macro-summary across held-out task types is secondary to the complete cell table. The held-out task type must not influence feature selection, preprocessing, or thresholds.

### C. Cross-family transfer — primary

Fit the same fixed pipeline in both directions:

- all Llama responses → all Gemma responses;
- all Gemma responses → all Llama responses.

The matched prompt bank is label-balanced inside every family, so direct transfer targets family shift rather than ordinary prompt shift. Both directions are required; a mean may not replace them. Coefficient signs and predictive behavior are compared with the paired feature results.

### D. Cross-family transfer to unseen prompts — robustness

Use five prompt-grouped folds. For each direction, fit on source-family responses from four prompt folds and test on target-family responses whose `prompt_id` values are in the held-out fold. Thus both family and prompt change at test time. This is the strongest planned evidence but is expected to have wider uncertainty.

### E. Supporting baselines and sensitivity analyses

- prompt-blocked five-fold within-family classification;
- a stratified dummy classifier evaluated on identical splits;
- length-aware variants adding actual word count as an explicit covariate and using a preregistered length-matched subset;
- performance by task type and length-compliance status;
- optional linear SVM as a labeled robustness model without retuning on target domains.

### F. PCA and clustering

PCA is used only for scaled visualisation with explained variance and loadings. Clustering is optional and exploratory, uses multiple seeds, and reports stability. Neither visual separation nor cluster composition is evidence of transfer.

## Evaluation implementation

`scripts/evaluate_generalization.py` runs the preregistered transfer protocols and baseline implemented in `src/linguistic_fingerprints/generalization.py`:

- `leave_one_task_type_out`;
- `cross_family_transfer`;
- `cross_family_unseen_prompt`;
- `prompt_blocked_within_family`.

The classifier is an L2-regularized logistic regression with `C=1` in a pipeline containing median imputation and standardisation. The configuration in `config/study.yaml` is authoritative. Any analysis-code change after the pilot freeze must be logged and rerun from raw immutable data.

## Confounds and mitigations

| Threat | Mitigation |
|---|---|
| Family/provider fingerprints | bidirectional cross-family transfer; family-specific paired results |
| Task/genre shortcuts | leave-one-task-type-out evaluation |
| Prompt/topic leakage | prompt grouping; strict cross-family/unseen-prompt robustness test |
| Output length | actual-length audit, normalised rates, covariate and length-matched sensitivity analyses |
| Model size and architecture | document differences; avoid causal age claims |
| Instruction/chat-template differences | exact template provenance; describe deployed-version contrasts |
| NLP measurement bias | one pinned pipeline plus stratified manual audit |
| Researcher degrees of freedom | freeze prompt registry, features, splits, metrics, and seed before main collection |
| Only two families | report pair-specific evidence and avoid universal claims |
| One response per cell | deterministic reproducibility; acknowledge unestimated decoding variance |

## Decision gates

### Gate 1 — supervisor and model feasibility

Obtain approval for the reframed objective. Install all four exact tags in `config/models.yaml`; capture the Ollama version and full runtime digests.

### Gate 2 — pilot

Run all four models on the registered pilot. Verify failure/refusal rate, length behavior, metadata, annotation quality, and sufficient valid earlier/later pairs in every task type.

### Gate 3 — analysis freeze

Freeze the 100-prompt registry, feature list, transformations, paired tests, transfer protocols, folds, metrics, length sensitivities, and seeds before the main run.

## Definition of done

- reproducible four-model controlled corpus with immutable provenance;
- validated 30-feature analysis table and length audit;
- paired family-specific feature contrasts with uncertainty;
- complete leave-one-task-type-out results per family;
- Llama → Gemma and Gemma → Llama transfer results;
- cross-family/unseen-prompt robustness results;
- prompt-blocked and dummy baselines;
- length-aware sensitivity analyses;
- carefully bounded conclusion: transferable pattern, family-specific fingerprints, or insufficient evidence;
- pinned environment, configuration freeze, tests, and complete run log.
