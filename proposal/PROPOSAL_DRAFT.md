# Project proposal

## Title and contributors

**Linguistic Fingerprints across LLM Generations: A Matched-Family, Prompt-Controlled Study**

**Contributors:** Dominik Soballa and Luca Bouché. The project is joint work. Dominik has primary responsibility for reproducible local model inference, data engineering, PCA, and classification. Luca has primary responsibility for the literature review, prompt design, linguistic feature validation, and paired group comparisons. Both contributors review the pilot, interpret all results, write the report, and perform the final reproducibility audit.

## 1. Introduction and motivation

Large language models are frequently described in generational terms, but release date is not a single causal variable. Successive versions may differ in training data, architecture, scale, post-training, safety alignment, tokenization, and chat templates. Consequently, apparent differences between “older” and “newer” models may instead reflect model-family or task effects. A controlled, linguistically interpretable comparison is needed before claims about generational writing styles can be made.

Previous work shows that generated texts contain source-model signals. Uchendu et al. (2020) and Munir et al. (2021) demonstrated that synthetic texts can be attributed to their generating systems, while Zahid et al. (2024) constructed linguistic profiles for five conversational agents and reported strong model-attribution performance. Guo et al. (2025) further argues that LLM evaluation should include lexical and syntactic diversity, rather than focusing only on task performance.

Most directly, Gude et al. (2026) compared two groups of LLMs and found lower lexical and syntactic diversity in the newer group. Their older group consisted mainly of base models, whereas the newer group consisted of instruction-tuned systems, and the experiment was restricted to news leads. The proposed project is therefore a controlled replication and extension: it compares instruction/chat-tuned predecessors and successors within two matched families, generates all texts locally through the same runtime, uses the same prompts for every model, and tests five writing-task types. It uses simpler, transparent corpus-linguistic features that fit the methods taught in the course.

## 2. Research objective

**Main research question:**

> Do selected earlier and later instruction-tuned versions of matched LLM families exhibit distinguishable linguistic profiles under controlled prompting?

**Subquestions:**

1. Which predefined lexical, morphosyntactic, and structural features differ between the selected earlier and later versions?
2. Which differences have the same direction in both the Llama and Gemma families?
3. Do standardized feature vectors display earlier/later structure in a two-dimensional PCA representation?
4. Can a transparent classifier predict the earlier/later label for responses to prompts that were absent from training?
5. To what extent do any observed differences depend on model family or writing-task type?

The project does not seek a universal property of all historical LLM generations. “Generation” is operationalized as an earlier/later relation inside each selected family, and conclusions are limited to the four models, prompt sample, English language, local runtime, and recorded generation settings.

## 3. Hypotheses

- **H1 — Feature differences:** At least one preregistered feature differs between the earlier and later version within at least one model family after false-discovery-rate correction.
- **H2 — Cross-family replication:** At least one feature has the same earlier-to-later direction and a corrected non-zero paired effect in both families.
- **H3 — Multivariate structure:** PCA reveals partial earlier/later structure after feature standardization. This hypothesis is exploratory because PCA components are not automatically linguistically interpretable.
- **H4 — Out-of-prompt prediction:** L2-regularized logistic regression predicts `earlier` versus `later` above the balanced 0.50 baseline when every response to one prompt is kept in the same cross-validation fold.

An absence of support is informative: it would show that the selected simple features do not provide a stable cross-family generational fingerprint under the controlled conditions.

## 4. Preliminary literature review and research gap

Research on neural-text authorship attribution provides evidence that generators leave detectable traces. Uchendu et al. (2020) formulated attribution tasks for distinguishing human and machine texts and for identifying a generating method. Munir et al. (2021) similarly argued that subtle marks inherited from a source model can support attribution, although their strongest system used a fine-tuned transformer rather than transparent linguistic features.

Zahid et al. (2024) is especially relevant methodologically: the authors profiled five conversational agents using linguistic features, PCA, and classifiers, finding that individual agents could often be distinguished. Their goal, however, was attribution to individual systems rather than controlled comparison of predecessor/successor pairs. Guo et al. (2025) supplies a complementary diversity perspective by benchmarking LLM outputs at lexical, syntactic, and semantic levels.

The closest study is Gude et al. (2026), which compares two model generations using formal HPSG analyses and diversity indices. It provides a concrete result to replicate—reduced diversity in newer models—but its generation contrast also overlaps with base-versus-instruction-tuned status and its data cover one genre. The present project holds instruction-tuned status constant, compares versions inside families, and samples five task types. It therefore tests whether a generational pattern remains visible with accessible UPOS, lexical-diversity, repetition, and structural features.

Evaluation design is also important. Xu et al. (2024) found that trained detectors are sensitive to shifts in prompts, text length, topics, and tasks. Xia et al. (2026) linked cross-prompt, cross-model, and cross-domain generalization gaps to shifts in linguistic features. These findings motivate the paired prompt design and the rule that a `prompt_id` cannot appear in both training and testing.

## 5. Data, models, and scope

### 5.1 Selected models

All four models are instruction/chat-tuned variants run locally through Ollama with the same Q4_K_M quantization class.

| Family | Generation | Exact Ollama tag | Parameters | Release | Ollama manifest |
|---|---|---|---:|---|---|
| Meta Llama | earlier | `llama2:7b-chat-q4_K_M` | 6.74B | 18 July 2023 | `fe3834f64df5` |
| Meta Llama | later | `llama3.1:8b-instruct-q4_K_M` | 8.03B | 23 July 2024 | `46e0c10c039e` |
| Google Gemma | earlier | `gemma2:9b-instruct-q4_K_M` | 9.24B | 27 June 2024 | `c20bec88025f` |
| Google Gemma | later | `gemma3:12b-it-q4_K_M` | approximately 12B | 12 March 2025 | `f4031aab637d` |

The pairs are not identical in size, but each predecessor/successor difference is modest enough for local execution and both members have corresponding instruction/chat tuning. Model size and changes to training/post-training remain limitations rather than controlled causal variables. Gemma 3 is multimodal, but only text input and text output are used.

### 5.2 Prompt corpus

The study language is **English**. The final prompt registry will contain 100 prompts: 20 each for explanation, narrative, argumentation, advice/instruction, and reflection/description. Every prompt requests 120–150 words, is answerable without browsing, contains no personal data, and is sent to every model. The design produces 100 prompts × 4 models = **400 responses**.

One response is collected per prompt/model cell. Generation uses temperature 0 and seed 42 to minimize stochastic variation; the 100 prompts, not repeated random generations, are the sampling units. This choice keeps the corpus within scope but means that within-model decoding variability is not estimated.

### 5.3 In-scope and out-of-scope

Included:

- transparent lexical, UPOS, sentence-length, repetition, connective, punctuation, and formatting features;
- paired earlier/later comparisons within each family;
- task-type sensitivity;
- PCA, prompt-blocked logistic regression, and optional clustering.

Excluded:

- factual correctness, semantic answer quality, human preference, and model benchmarking;
- human-versus-machine detection;
- multilingual comparison;
- causal attribution to release date, training data, architecture, or alignment;
- claims about all LLMs or all model generations;
- embeddings or fine-tuned neural detectors as primary features.

## 6. Methodology

### 6.1 Controlled local generation

The Ollama chat API receives the same system message and user prompt for every model. Common options are fixed at temperature 0, `top_p=1`, `top_k=40`, `repeat_penalty=1`, `seed=42`, `num_ctx=4096`, and `num_predict=384`. The last setting is a safety ceiling and responses are not manually truncated. Each model's native chat template and stop tokens are retained and archived because they form part of the deployed model version; this prevents the study from claiming that observed effects arise from model weights alone.

Every attempt receives an immutable `run_id`. Stored provenance includes `prompt_id`, model tag, family, generation label, manifest/runtime digest, exact messages, all decoding options, Ollama version, timestamp, status, raw response, and error text. Failed attempts remain in the raw table; a retry creates a new row.

### 6.2 Pilot and quality gates

The existing 20-prompt pilot registry contains four prompts per task type. The pilot is run across all four models before the main collection. It passes if:

- all four exact tags load on the 24-GB M4 Pro machine;
- at least 95% of the 80 planned responses have status `ok`;
- at least 80% fall within 120–150 words;
- no model has a systematic refusal or formatting failure rate above 10%;
- provenance fields and raw responses are complete.

If length compliance fails, the wording may be revised once for all prompts and models; any revision increments the prompt version and requires a new pilot. No model-specific prompt repair is permitted.

### 6.3 Linguistic processing and preregistered features

All successful responses are processed with the same pinned `en_core_web_sm` SpaCy pipeline. A stratified 10% sample (balanced by model and task type) is manually inspected for sentence-boundary and POS errors. NLP output is treated as automated measurement, not gold annotation.

Thirty features form the confirmatory inventory:

- structure and length: sentence count, paragraph count, mean word length, mean sentence length, sentence-length standard deviation;
- lexical/stylistic: MATTR with a 50-token window, repeated-token rate, repeated-bigram rate, adjacent-sentence lexical overlap;
- function/style markers: function-word, modal, connective, sentence-initial-connective, punctuation, apostrophe-word, list-line, and heading-line proportions;
- UPOS proportions: `ADJ`, `ADP`, `ADV`, `AUX`, `CCONJ`, `DET`, `NOUN`, `NUM`, `PART`, `PRON`, `PROPN`, `SCONJ`, and `VERB`.

Actual word count, surface-token count, and raw TTR are audit variables, not confirmatory fingerprint features. Proportions use the relevant token or line denominator. MATTR is preferred to raw TTR because raw TTR is strongly length-dependent.

### 6.4 Aggregation and primary inference

Coverage, failures, length, and every feature are summarized by model, family, generation, task type, and prompt. The primary unit for feature inference is the within-prompt difference `later − earlier`, calculated separately for Llama and Gemma.

For each feature/family combination, the analysis reports the mean paired difference, a standardized paired effect, and a 95% percentile confidence interval from 10,000 bootstrap resamples of prompts with seed 42. Two-sided paired permutation tests are corrected across the 60 confirmatory feature/family tests with the Benjamini–Hochberg procedure at `q=0.05`. Task-type estimates are exploratory and reported with uncertainty but without separate confirmatory claims.

H1 is supported if at least one corrected feature/family test is non-zero. H2 is supported only when the same feature has the same effect direction and passes the corrected criterion in both families.

### 6.5 PCA and clustering

The 30 features are standardized before PCA. The analysis reports explained-variance ratios and loadings and plots points by generation, family, and task type. PCA is used for visualization, not significance testing. Clustering is optional and secondary; if performed, it uses standardized features, multiple seeds, silhouette scores, and cluster-stability checks. Cluster composition alone is not evidence of a generation effect.

### 6.6 Classification

The primary classifier is L2-regularized logistic regression with fixed `C=1`. A scikit-learn pipeline fits imputation and standardization only on training folds. Five-fold `StratifiedGroupKFold` evaluation groups by `prompt_id`, so all four responses to one prompt remain in the same fold. A stratified dummy classifier provides the 0.50 baseline.

The report includes balanced accuracy, macro-F1, ROC-AUC, fold results, prompt-level bootstrap uncertainty for out-of-fold predictions, confusion matrices, and standardized coefficients. Classification supports H4 only if the confidence interval for balanced accuracy excludes 0.50. Coefficients are interpreted as associations among correlated measurements, not causal effects.

## 7. Risks and limitations

The design contains only two families and one predecessor/successor pair per family. Family is therefore a fixed comparison, not a population sample. The pairs differ somewhat in parameter count, training, architecture, tokenization, alignment, context length, and native chat template. These differences are scientifically interesting parts of deployed versions but prevent causal attribution to age alone.

Prompt genre and output length can dominate linguistic features. Pairing every prompt across models, balancing task types, requesting one length range, using normalized features, and blocking cross-validation by prompt reduce these threats. Automated SpaCy annotation can introduce measurement error, addressed through one pinned pipeline and a manual audit. Temperature-zero single runs prioritize reproducibility but do not estimate stochastic decoding variation. Finally, results may not generalize beyond English, short prompted texts, Ollama's quantized implementations, or the four exact manifests.

## 8. Work and time plan

| Dates | Deliverable | Dominik — primary | Luca — primary | Joint checkpoint |
|---|---|---|---|---|
| 27–28 Aug | verified literature and model design | runtime/model feasibility | literature and research gap | approve RQ and model pairs |
| 29–30 Aug | proposal and pilot readiness | configs, data contract, pilot runner | prompt audit, feature definitions | freeze proposal draft |
| 31 Aug | proposal submission | repository/reproducibility check | final language/editing check | submit and request topic-change approval |
| 1–14 Sep | final prompt bank and collection tooling | generation/cache implementation | expand and balance 100 prompts | code and prompt review |
| 15–28 Sep | four-model pilot and design freeze | install/run models, capture manifests | manual response and POS audit | pilot pass/fail decision |
| 29 Sep–12 Oct | main corpus | resumable generation and provenance | live quality audit | confirm 400-cell coverage |
| 13–26 Oct | feature corpus | pipeline and validation | linguistic error analysis | freeze analysis table |
| 27 Oct–9 Nov | group analysis | reproducible summaries | paired bootstrap/permutation analysis | interpret H1–H2 |
| 10–23 Nov | PCA and classification | PCA/CV pipelines | loading/coefficient linguistic interpretation | interpret H3–H4 |
| 24 Nov–7 Dec | optional clustering and robustness | stability implementation | cluster profile analysis | retain only stable results |
| 8–21 Dec | final report | methods/reproducibility sections | background/results discussion | joint full-paper revision |
| 22–31 Dec | submission | clean re-run and release | citation/argument audit | final GitHub submission |

Both contributors participate across all stages; the primary column denotes responsibility for producing the first complete version, while the other contributor reviews it.

## 9. Expected outcomes

Three result patterns are meaningful:

1. **Replicated differences:** the same features change in the same direction in both families and out-of-prompt classification is above baseline. This supports a limited cross-family fingerprint for the selected versions.
2. **Family-specific differences:** effects or classification are strong inside one family but inconsistent across families. This argues against a shared generational fingerprint and points to family-specific development.
3. **No robust separation:** corrected paired effects are small and classification remains near baseline. This shows that the selected transparent features do not distinguish these versions reliably under the sampled conditions.

The study's contribution is therefore not contingent on obtaining high accuracy. It provides a controlled test, an interpretable feature inventory, and a reproducible corpus design that can later be extended to more families, languages, genres, or repeated generations.

## 10. Reproducibility and data management

Prompts, configurations, source code, feature definitions, analysis notebooks, environment requirements, seeds, and the append-only run log are versioned in Git. Raw outputs are immutable and released only after checking model licenses, provider terms, privacy, and repository size. Derived tables are reproducible from documented commands. Exact Ollama manifest IDs are recorded in the proposal configuration and runtime digests are captured again immediately before collection.

## References

Gude, A., Santos-Rios, R., Bond, F., Flickinger, D., Gómez-Rodríguez, C., & Zamaraeva, O. (2026). More aligned, less diverse? Analyzing the grammar and lexicon of two generations of LLMs. *Proceedings of ACL 2026*, 38900–38911. https://doi.org/10.18653/v1/2026.acl-long.1803

Guo, Y., Shang, G., & Clavel, C. (2025). Benchmarking linguistic diversity of large language models. *Transactions of the Association for Computational Linguistics, 13*, 1507–1526. https://doi.org/10.1162/tacl.a.47

Munir, S., Batool, B., Shafiq, Z., Srinivasan, P., & Zaffar, F. (2021). Through the looking glass: Learning to attribute synthetic text generated by language models. *Proceedings of EACL 2021*, 1811–1822. https://doi.org/10.18653/v1/2021.eacl-main.155

Uchendu, A., Le, T., Shu, K., & Lee, D. (2020). Authorship attribution for neural text generation. *Proceedings of EMNLP 2020*, 8384–8395. https://doi.org/10.18653/v1/2020.emnlp-main.673

Xia, Y., Stańczak, K., & Roth, B. (2026). Explaining generalization of AI-generated text detectors through linguistic analysis. *Proceedings of EACL 2026*, 6524–6546. https://doi.org/10.18653/v1/2026.eacl-long.307

Xu, H., Ren, J., He, P., Zeng, S., Cui, Y., Liu, A., Liu, H., & Tang, J. (2024). On the generalization of training-based ChatGPT detection methods. *Findings of EMNLP 2024*, 7223–7243. https://doi.org/10.18653/v1/2024.findings-emnlp.424

Zahid, I., Madusanka, T., Batista-Navarro, R., & Sun, Y. (2024). Probing the uniquely identifiable linguistic patterns of conversational AI agents. *Findings of ACL 2024*, 4612–4628. https://doi.org/10.18653/v1/2024.findings-acl.274

Model reports and release documentation are listed with verified URLs in `literature/REFERENCES.md` and the exact runtime models are frozen in `config/models.yaml`.

## Approval status

This proposal replaces the previous SpaCy–LLM disagreement topic. The scientific design is ready for supervisor review; the topic change and final proposal still require the supervisor's approval.
