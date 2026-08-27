# Project proposal — draft

## Title and contributors

**Linguistic Fingerprints across LLM Generations: A Controlled Comparison of Earlier and Later Model Versions**

**Contributors:** Dominik Soballa and Luca Bouché. The project is joint work. Primary responsibilities will be recorded per task and both contributors will review the complete analysis and report.

## 1. Introduction

Large language models are often discussed as if models from one technological period shared a single writing style. Yet individual systems differ in training data, architecture, scale, instruction tuning, and deployment interfaces. It is therefore unclear whether successive versions within model families exhibit systematic linguistic differences that can be observed under controlled prompting.

This project constructs a small experimental corpus by giving selected earlier and later versions of two matched LLM families the same writing prompts. Instead of rating the factual quality or general usefulness of the responses, we analyze transparent lexical, morphosyntactic, and stylistic features. The project connects corpus-linguistic preprocessing with aggregation, dimensionality reduction, clustering, and classification.

## 2. Research objective

**Main research question:**

> Do earlier and later versions of matched LLM families exhibit distinguishable linguistic profiles under controlled prompting?

Subquestions:

1. Which predefined linguistic features differ between the selected earlier and later versions?
2. Are the directions of these differences consistent across both model families?
3. Do the texts display earlier/later structure in a lower-dimensional feature representation?
4. Can an interpretable classifier predict the earlier/later label for responses to unseen prompts?

The project does not aim to establish a universal distinction between all “old” and “new” LLMs. Its conclusions will be limited to the selected model versions, prompt sample, and generation conditions.

## 3. Hypotheses

- **H1:** Selected earlier and later model versions differ in at least some predefined lexical, morphosyntactic, or stylistic features after prompt and family are taken into account.
- **H2:** A subset of feature differences has the same direction in both model families.
- **H3:** Standardized linguistic feature vectors show partial earlier/later structure in PCA, although the components themselves are not assumed to have direct linguistic interpretations.
- **H4:** An interpretable classifier predicts earlier/later labels above a balanced baseline when evaluated on prompts absent from the training data.

## 4. Preliminary literature review

The final proposal will connect four bodies of work:

1. stylometry and authorship attribution based on lexical and syntactic features;
2. linguistic descriptions and detection of machine-generated text;
3. attribution of generated text to model families or versions;
4. robust evaluation of text classifiers under topic and prompt shift.

The literature review must establish which interpretable features have previously been useful, how strongly results depend on topic and text length, and whether comparisons across successive versions of matched model families have already been conducted. Exact references will be added after a focused literature search; no citations should be added without verification.

## 5. Data and scope

The working design uses two model families, each represented by one earlier and one later version. Versions should be comparable in parameter scale and instruction-tuning status. Exact model identifiers and revisions will be frozen after an access and feasibility check.

The working language is English. The main corpus will contain approximately 100–120 prompts balanced across explanation, narrative, argumentation, advice/instruction, and reflection/description. Every model receives every prompt, the same system instruction, the same target range of 120–150 words, and the same supported decoding settings. With 100 prompts and one response per model, the minimum corpus contains 400 texts.

The study excludes factual correctness, human preference, semantic quality ratings, broad AI-text detection, and claims about all LLM generations. It also excludes multilingual comparison in order to keep the project within the available time.

## 6. Methodology

### Data collection and provenance

Each generation is stored with a stable prompt ID, exact model/provider identifier, revision or digest when available, model family, earlier/later label, generation settings, timestamp, and unmodified response. Failed generations and refusals are retained and reported. The prompt registry and configuration are frozen after a pilot with at least 20 prompts.

### Linguistic preprocessing and features

All texts are processed with the same pinned SpaCy English pipeline. The planned feature groups include:

- sentence and token-length statistics;
- length-robust lexical diversity such as MATTR;
- normalized UPOS proportions;
- normalized frequencies of pronouns, auxiliaries, conjunctions, adjectives, adverbs, function words, modals, and selected connectives;
- punctuation, paragraph, list, and heading rates;
- repeated-token and repeated-bigram measures;
- optional dependency features after a small reliability audit.

The final feature list and definitions are frozen before the main analysis.

### Aggregation and inference

Descriptive statistics will be grouped by model, family, generation, task type, and prompt. Earlier/later comparisons will respect the paired structure because every prompt is answered by all models. Effect sizes and uncertainty intervals will be reported; the exact primary paired or hierarchical method will be selected after the pilot and recorded before the main run.

### PCA and clustering

Features will be standardized before PCA. Explained variance and loadings will be reported, and plots will distinguish generation, family, and task type. PCA is exploratory; component axes will not be assumed to be linguistically interpretable. Clustering will be an optional secondary analysis and will include sensitivity or stability checks.

### Classification

A regularized logistic regression or linear SVM will predict `earlier` versus `later`. Preprocessing will be implemented in a pipeline and fitted only on training folds. Cross-validation will be grouped by `prompt_id`, ensuring that responses to the same prompt never occur in both training and testing. Balanced accuracy, macro-F1, ROC-AUC where appropriate, uncertainty across folds, and a dummy baseline will be reported. Coefficients or stable permutation importances will be used to identify distinguishing linguistic features.

## 7. Risks and limitations

The small number of model families limits generalization. Release date is confounded with many technical changes, so observed differences cannot be causally attributed to age alone. Provider interfaces may not expose identical decoding controls. Topic, genre, output length, and NLP annotation error may also influence features. The paired prompt design, family-specific reporting, length controls, frozen configurations, and manual audit mitigate but do not remove these limitations.

## 8. Preliminary work plan

| Phase | Work | Primary responsibility | Joint check |
|---|---|---|---|
| 1 | literature, exact model selection, access check | TBD | both |
| 2 | prompt design and 20-prompt pilot | TBD | both |
| 3 | freeze design and collect main corpus | TBD | both |
| 4 | validate corpus and extract features | TBD | both |
| 5 | descriptive and paired analyses | TBD | both |
| 6 | PCA and classification; optional clustering | TBD | both |
| 7 | interpretation, limitations, and report | TBD | both |
| 8 | reproducibility audit and final submission | TBD | both |

The responsibility column will be completed with both contributors before submission, as required for group work.

## 9. Expected outcomes

If stable differences occur within both families and an out-of-prompt classifier performs above baseline, the project will provide evidence that the selected successive versions have distinguishable linguistic profiles. If differences appear only within one family, the result will support a family-specific development effect rather than a general generation pattern. If neither feature comparisons nor classification show robust differences, this will indicate that simple interpretable features do not reliably separate the selected versions under the sampled tasks. All three outcomes answer the research question and inform the design of larger follow-up studies.

## 10. Reproducibility

The repository will archive prompts, configurations, exact model identifiers, seeds, processing code, feature definitions, analysis notebooks, and a run log. Raw outputs will be immutable, and derived files will be reproducible from documented commands. Course concepts and methodological decisions will be cited using the local page-indexed lecture corpus.

## Items to complete before submission

- [ ] Verify and cite the relevant literature.
- [ ] Freeze the two model families and four exact versions.
- [ ] Confirm English as the sole study language.
- [ ] Decide whether repeated generations are feasible and scientifically necessary.
- [ ] Complete the division of labor.
- [ ] Add a calendar with dates through the final deadline.
- [ ] Obtain approval for the change from the previous project proposal.
