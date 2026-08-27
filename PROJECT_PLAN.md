# Project plan

## Working title

**Linguistic Fingerprints across LLM Generations**

## Research question

Do earlier and later versions of matched LLM families exhibit distinguishable linguistic profiles under controlled prompting?

## Operational definition

“Generation” means the earlier/later relation between two documented versions inside the same model family. It does not mean a universal historical era shared by all LLMs.

Proposal-level design:

```text
Llama: Llama 2 7B Chat → Llama 3.1 8B Instruct
Gemma: Gemma 2 9B Instruction Tuned → Gemma 3 12B Instruction Tuned
```

The family-matched design helps distinguish an earlier/later contrast from a pure provider or family contrast. With two families, replication across families remains limited and all conclusions must be cautious.

## Hypotheses

- **H1 — Feature differences:** selected earlier and later versions differ in at least some predefined lexical, morphosyntactic, or stylistic features after controlling for prompt and family.
- **H2 — Cross-family consistency:** a subset of feature directions is consistent across both matched families.
- **H3 — Multivariate profile:** standardized feature vectors show partial earlier/later structure in PCA, without assuming that principal components are directly linguistic.
- **H4 — Out-of-prompt prediction:** an interpretable classifier predicts earlier/later labels above a balanced baseline on unseen prompts.

H4 is supported only by prompt-blocked evaluation. A classifier that sees the same prompt in training and testing is invalid for this study.

## Study matrix

| Factor | Levels/role |
|---|---|
| `family` | 2 matched model families; blocking/moderating factor |
| `generation` | earlier/later; primary explanatory variable |
| `model_id` | 4 exact versions; nested in family × generation |
| `prompt_id` | 100 prompts; repeated-measures block |
| `task_type` | balanced prompt genre; stratification variable |
| response | one deterministic generated text per cell |

Main corpus: 100 prompts × 4 models = 400 texts.

## Prompt design

Prompts are balanced across five task types, with 20 prompts each:

1. explanation;
2. narrative;
3. argumentation;
4. advice/instructions;
5. reflection/description.

Each prompt must:

- request the same target word range;
- avoid mentioning model identity or generation;
- be answerable without browsing;
- avoid sensitive personal data;
- have a stable `prompt_id` and version;
- be piloted for refusal and formatting artifacts.

## Feature inventory

The 30 proposal-level confirmatory features are listed in the proposal and implemented in `src/linguistic_fingerprints/features.py`. They become the main-run freeze after the pilot and code audit. Groups:

### Lexical

- mean token length;
- lemma/type counts;
- MATTR;
- frequency of selected function words;
- normalized repeated-token and repeated-bigram rates;
- normalized modal and connective rates.

### Morphosyntactic

- UPOS proportions;
- mean and standard deviation of sentence length;
- pronoun, auxiliary, conjunction, adjective, and adverb rates;
- optional dependency-relation proportions after a reliability check.

### Stylistic/structural

- paragraph count;
- punctuation rates;
- sentence-initial connective rate;
- list/heading/markdown markers;
- contraction rate for English;
- lexical overlap between adjacent sentences.

All measures must have a transparent definition and be computed identically for every model.

## Analysis plan

### A. Audit and aggregation

- confirm complete prompt × model coverage;
- report refusals, failures, and actual length distributions;
- summarize features by generation, model, family, and task type;
- visualize paired earlier/later differences per prompt.

### B. Primary inference

For each of the 30 features and two families, compute the within-prompt contrast `later − earlier`. Report the mean paired difference, a standardized paired effect, and a 95% percentile interval from 10,000 prompt bootstrap resamples with seed 42. Use two-sided paired permutation tests and Benjamini–Hochberg correction across the 60 confirmatory feature/family tests at `q=0.05`.

### C. PCA

- standardize features;
- report explained variance;
- inspect loadings;
- color by generation and shape/facet by family and task type;
- do not treat visual separation as inferential proof.

### D. Classification

Primary model: L2-regularized logistic regression (`C=1`) in a scikit-learn pipeline.

- outer evaluation: five-fold `StratifiedGroupKFold`, groups=`prompt_id`;
- preprocessing fitted within folds;
- report balanced accuracy, macro-F1, ROC-AUC where appropriate, and fold uncertainty;
- compare against a dummy baseline;
- inspect stable standardized coefficients/permutation importance;
- optionally test whether directions generalize across families, clearly marked as low-powered.

### E. Clustering

Exploratory only. Compare multiple seeds/algorithms and report silhouette/stability. Cluster composition by generation is descriptive and does not prove a generation effect.

## Confounds and mitigations

| Threat | Mitigation |
|---|---|
| Family/provider effects | matched earlier/later versions within each family; family-specific results |
| Model size | match parameter class where possible; document differences |
| Instruction-tuning differences | compare equivalent chat/instruct variants |
| Prompt topic/genre | every model receives every prompt; balance task types |
| Prompt leakage | group all identical `prompt_id` responses into one CV fold |
| Output length | identical requested range; normalized features; length audit |
| Decoding/interface | freeze and record system prompt and settings |
| NLP measurement bias | same pipeline for all texts; manual audit of a small stratified sample |
| Researcher degrees of freedom | freeze prompt registry, feature list, and primary analysis after pilot |

## Decision gates

### Gate 1 — model feasibility

Install and load all four exact tags from `config/models.yaml`; capture the local Ollama version and full runtime digests. Proposal-level public manifests have been verified, but local installation remains pending.

### Gate 2 — pilot

At least 20 prompts run successfully across all four models; failure/refusal rate and length compliance are acceptable; metadata capture is complete.

### Gate 3 — analysis freeze

Prompt registry, feature list, transformations, primary contrasts, CV groups, metrics, and seeds are recorded before the main run.

## Definition of done

- reproducible 4-model controlled corpus;
- validated feature table;
- descriptive and paired group analyses;
- PCA with loadings and caveats;
- prompt-blocked classification with baseline and uncertainty;
- optional stable clustering analysis;
- notebook/report answering H1–H4 and documenting limitations;
- pinned environment, immutable configurations, and complete run log.
