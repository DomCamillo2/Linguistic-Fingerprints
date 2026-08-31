# Project plan

## Working title

**Interpretable Linguistic Fingerprints of Earlier and Later Open-Weight LLM Versions: A Controlled Replication across Writing Tasks**

## Research question and contribution

> Can earlier and later versions within the Llama and Gemma families be distinguished using a small set of interpretable linguistic features, and how robust is this distinction across unseen prompts and writing-task types?

Prior work already demonstrates model and version fingerprints. This project therefore does not claim to invent matched-prompt stylometry or LLM-version classification. Its course-appropriate contribution is a controlled replication with two open-weight family pairs, a compact feature inventory, identical prompts, leakage-safe evaluation, and one clearly defined robustness question.

The study asks:

1. Which prespecified features differ between the earlier and later model within each family?
2. Can a simple classifier distinguish the two versions on prompts that were not used for training?
3. Does the distinction remain when an entire writing-task type is absent from training?

The Llama and Gemma comparisons are parallel case studies. Cross-family classifier transfer is not part of the confirmatory project.

## Operational definition and claim boundary

Generation means the documented predecessor-successor relation inside a selected family:

- Llama 2 7B Chat → Llama 3.1 8B Instruct
- Gemma 2 9B Instruction Tuned → Gemma 3 12B Instruction Tuned

Observed differences are associated with these deployed version transitions. Architecture, parameter count, tokenizer, training data, post-training, alignment, quantisation, and native chat templates also differ. The design cannot isolate a causal effect of model age.

## Hypotheses

- **H1 — Paired linguistic differences:** at least one of the 15 prespecified features differs between the earlier and later version within at least one family after Bonferroni correction.
- **H2 — Unseen-prompt classification:** within each family, a fixed L2-logistic classifier performs above a stratified dummy baseline under five-fold prompt-blocked cross-validation.
- **H3 — Task-type robustness:** within each family, performance remains above the dummy baseline when each writing-task type is held out in turn.

H3 is deliberately stricter than H2. Failure of H3 is meaningful evidence that a fingerprint depends on genre rather than a failed project.

## Study matrix

| Factor | Levels or role |
|---|---|
| family | Llama and Gemma, analysed separately |
| generation | earlier or later within family |
| model_id | four exact versions |
| prompt_id | 100 matched prompts and the pairing/grouping unit |
| task_type | five writing-task types |
| response | one deterministic text per prompt/model cell |

Main corpus: 100 prompts × 4 models = 400 texts. Each task type contains 20 prompts.

## Prompt design

The prompt bank is balanced across explanation, narrative, argumentation, advice/instructions, and reflection/description. Every prompt:

- requests 120–150 words;
- avoids model identity cues;
- is answerable without browsing;
- contains no sensitive personal data;
- has a stable prompt_id, version, and task type;
- is sent unchanged to every model.

Actual output length is audited; requesting a word range does not guarantee length control.

## Confirmatory feature inventory

The fixed 15-feature inventory is:

1. sentence count;
2. mean word length;
3. mean sentence length;
4. sentence-length standard deviation;
5. MATTR with a 50-token window;
6. repeated-token rate;
7. repeated-bigram rate;
8. function-word proportion;
9. modal proportion;
10. connective proportion;
11. punctuation proportion;
12. adjacent-sentence lexical overlap;
13. adjective proportion;
14. noun proportion;
15. verb proportion.

The extractor may retain additional audit or exploratory columns, but only the features in CONFIRMATORY_FEATURES enter confirmatory tests and classifiers. No feature may be selected after examining held-out performance.

## Analysis plan

### A. Audit and descriptive analysis

- verify complete prompt × model coverage and provenance;
- report failures, refusals, formatting problems, and actual word counts;
- inspect feature distributions by model, family, generation, and task type;
- manually review a stratified 10% sample for sentence-boundary and POS errors.

### B. Paired feature comparisons — primary linguistic analysis

For every prompt, calculate later minus earlier separately within Llama and Gemma. For each family × feature combination, report:

- mean paired difference;
- standardised paired effect;
- 95% confidence interval from prompt-level bootstrap resampling;
- paired t-test with Bonferroni correction across the 30 family × feature tests.

The paired design controls prompt content directly. Results remain family-specific.

### C. Prompt-blocked classification — primary predictive analysis

Within each family, run five-fold cross-validation. All responses sharing a prompt_id must remain in the same fold. The fixed pipeline contains median imputation, standardisation, and L2 logistic regression with C=1. Compare it with a stratified dummy classifier on identical folds.

Report balanced accuracy, macro-F1, fold-level results, and confusion matrices. Do not tune the model on test folds.

### D. Leave-one-task-type-out — robustness analysis

Within each family, train on four task types and test on the complete fifth task type, repeating this for all five types. Report every family × held-out-task result as well as a cautious summary. This tests domain shift, not just unseen prompt wording.

### E. Length sensitivity

Audit actual word count. Repeat the classifiers with n_words included as an explicit covariate and, if the pilot supports a clear rule, on a preregistered length-matched subset.

### F. Optional exploration

A scaled PCA may visualise broad structure. Explained variance and loadings must be shown. Clustering, mixed-effects models, and cross-family transfer are outside the project scope.

## Evaluation implementation

The default scripts/evaluate_generalization.py command runs:

- prompt_blocked_within_family;
- leave_one_task_type_out.

Both run once with the 15 confirmatory features and once with actual word count added for length sensitivity. Reusable cross-family functions remain in the package but are not part of the proposal.

## Confounds and mitigations

| Threat | Mitigation |
|---|---|
| Prompt/topic leakage | group all rows by prompt_id |
| Task-type shortcuts | leave one complete task type out |
| Output length | audit actual length and run sensitivity variants |
| Model size and architecture | document differences and avoid causal age claims |
| Chat-template differences | preserve exact runtime provenance |
| NLP measurement error | one pinned pipeline and manual audit |
| Multiple testing | fixed features and Bonferroni correction |
| Only one response per cell | deterministic reproducibility; acknowledge unmeasured decoding variance |
| Only two family pairs | family-specific reporting and no universal claims |

## Decision gates

### Gate 1 — approval and feasibility

Confirm the simplified proposal with the supervisor. Install the four exact model tags and capture Ollama/runtime digests.

### Gate 2 — pilot

Run the 20-prompt pilot across all four models. Audit failures, refusals, length, metadata, and NLP annotations.

### Gate 3 — analysis freeze

Freeze the 100 prompts, 15 features, paired tests, folds, metrics, length sensitivity, and seeds before the main run.

## Definition of done

- reproducible four-model corpus with immutable provenance;
- validated feature table and length audit;
- paired family-specific feature results with uncertainty;
- prompt-blocked logistic and dummy results for both families;
- complete leave-one-task-type-out results;
- length-aware sensitivity analysis;
- optional PCA only if time permits;
- bounded conclusion covering positive, task-specific, or null results;
- pinned environment, tests, and complete run log.
