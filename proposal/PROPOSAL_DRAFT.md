# Project proposal

## Title and contributors

**Generalising Linguistic Fingerprints across LLM Families and Genres**

**Contributors:** Dominik Soballa and Luca Bouché. The project is joint work. Dominik has primary responsibility for reproducible local model inference, data engineering, and the cross-genre/cross-family evaluation pipelines. Luca has primary responsibility for the literature review, prompt design, linguistic feature validation, paired contrasts, and transfer interpretation. Both contributors review the pilot, all sensitivity analyses, the final report, and the reproducibility audit.

## 1. Introduction and motivation

Large language models are frequently described in generational terms, but release date is not a single causal variable. Successive versions may differ in training data, architecture, scale, tokenization, post-training, alignment, and chat templates. A measured predecessor-successor contrast is therefore associated with a deployed model transition; it cannot isolate the causal effect of “newer-generation training.”

Previous work already shows that generated texts contain source-model and version signals. Uchendu et al. (2020), Munir et al. (2021), and Zahid et al. (2024) establish model attribution and interpretable linguistic profiling. More importantly for this proposal, Przystalski et al. (2026) directly compare Llama 2 and Llama 3 over the same Wikipedia topics and prompt templates, using interpretable stylometric features, tree classifiers, and topic-grouped cross-validation. Huynh and McNamara (2026) measure linguistic shifts across GPT updates under identical personalization tasks, while Rudnicka and Juzek (2026) compare 2024 and 2026 model cohorts using the same societal-topic prompts.

It is therefore no longer defensible to claim that matched-prompt, interpretable comparisons of earlier and later models are missing. The narrower open question is whether predecessor-successor differences transfer across open-weight families and heterogeneous text genres. This project tests that question with matched Llama and Gemma pairs, five writing-task types, and a compact prespecified set of 30 interpretable features. Simple version classification becomes a baseline; leave-one-task-type-out and bidirectional cross-family transfer become the main analyses.

## 2. Research objective

**Main research question:**

> To what extent do linguistically interpretable predecessor-successor differences generalise across open-weight model families and text genres?

**Subquestions:**

1. Which predefined lexical, morphosyntactic, and structural features change within the Llama and Gemma predecessor-successor pairs?
2. Which effect directions agree across both families?
3. Does an earlier-versus-later classifier generalise to a writing-task type absent from training?
4. Does a classifier trained on Llama transfer to Gemma, and vice versa?
5. Does cross-family transfer remain when target prompts are also absent from training?

The project does not seek a universal property of all historical LLM generations. “Generation” is operationalized as an earlier/later relation inside each selected family, and conclusions are limited to the four models, prompt sample, English language, local runtime, and recorded generation settings.

## 3. Hypotheses

- **H1 — Feature differences:** At least one preregistered feature differs between the earlier and later version within at least one family after false-discovery-rate correction.
- **H2 — Cross-family directional replication:** A prespecified subset of features has concordant earlier-to-later directions in Llama and Gemma, with effect estimates and uncertainty reported for both.
- **H3 — Cross-genre generalisation:** L2-regularized logistic regression retains above-baseline balanced accuracy when each complete writing-task type is held out in turn, reported separately by family.
- **H4 — Cross-family transfer:** The fixed classifier transfers above baseline from Llama to Gemma and from Gemma to Llama. A stricter prompt-blocked transfer is the robustness test.

An absence of support is informative: it would show that the selected simple features do not provide a stable cross-family generational fingerprint under the controlled conditions.

## 4. Preliminary literature review and research gap

Research on neural-text authorship attribution shows that generators leave detectable traces. Uchendu et al. (2020) formulate source-generator attribution, Munir et al. (2021) identify inherited source-model signals, and Zahid et al. (2024) profile conversational agents using linguistic features, PCA, and classification. Guo et al. (2025) complements this work by treating lexical, syntactic, and semantic diversity as evaluation objects.

The closest methodological precedent is Przystalski et al. (2026). Their dataset contains Wikipedia-topic descriptions from Llama 2 7B, Llama 3 8B, and other generators. The models receive the same two prompt templates, their outputs are represented with 195 StyloMetrix features or approximately 3,000 frequency features, and decision-tree/LightGBM classifiers use 10-fold grouped cross-validation so one topic never appears in both training and test data. This directly combines an earlier/later Llama comparison, matched prompts, interpretable features, classification, and topic blocking. Accordingly, none of those components is presented as novel here.

Other recent work further narrows the claim. Gude et al. (2026) compare older and newer model cohorts and report reduced linguistic diversity in the newer cohort, although generation overlaps with tuning regime and the data are news leads. Huynh and McNamara (2026) use identical personalization tasks and NLP features to document shifts between GPT-4o deployments and GPT-4.1. Rudnicka and Juzek (2026) use the same prompts for 2024 and 2026 model cohorts and report both cohort-level change and model-specific profiles.

The defensible gap is therefore a generalisation question. Existing evidence does not establish whether a compact, prespecified predecessor-successor signal learned in one open-weight family transfers to another, or whether it survives complete text-genre shift. Xu et al. (2024) and Xia et al. (2026) show why this matters: detectors can fail under prompt, task, model, and domain shift, and those failures correspond to linguistic feature changes. The proposed contribution is a controlled, incremental multi-family and multi-genre extension with explicit failure-compatible outcomes.

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
- leave-one-task-type-out generalisation;
- bidirectional cross-family transfer;
- strict cross-family transfer to unseen prompts;
- prompt-blocked within-family classification, PCA, and optional clustering as supporting analyses.

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
- provenance fields and raw responses are complete;
- every task type retains enough valid earlier/later pairs for held-out evaluation.

If length compliance fails, the wording may be revised once for all prompts and models; any revision increments the prompt version and requires a new pilot. No model-specific prompt repair is permitted.

### 6.3 Linguistic processing and preregistered features

All successful responses are processed with the same pinned `en_core_web_sm` SpaCy pipeline. A stratified 10% sample (balanced by model and task type) is manually inspected for sentence-boundary and POS errors. NLP output is treated as automated measurement, not gold annotation.

Thirty features form the confirmatory inventory:

- structure and length: sentence count, paragraph count, mean word length, mean sentence length, sentence-length standard deviation;
- lexical/stylistic: MATTR with a 50-token window, repeated-token rate, repeated-bigram rate, adjacent-sentence lexical overlap;
- function/style markers: function-word, modal, connective, sentence-initial-connective, punctuation, apostrophe-word, list-line, and heading-line proportions;
- UPOS proportions: `ADJ`, `ADP`, `ADV`, `AUX`, `CCONJ`, `DET`, `NOUN`, `NUM`, `PART`, `PRON`, `PROPN`, `SCONJ`, and `VERB`.

Actual word count, surface-token count, and raw TTR are audit variables, not confirmatory fingerprint features. Proportions use the relevant token or line denominator. MATTR is preferred to raw TTR because raw TTR is strongly length-dependent.

### 6.4 Paired feature analysis

Coverage, failures, length, and every feature are summarized by model, family, generation, task type, and prompt. The primary unit for feature inference is the within-prompt difference `later − earlier`, calculated separately for Llama and Gemma.

For each feature/family combination, the analysis reports the mean paired difference, a standardized paired effect, and a 95% percentile confidence interval from 10,000 bootstrap resamples of prompts with seed 42. Two-sided paired permutation tests are corrected across the 60 confirmatory feature/family tests with the Benjamini–Hochberg procedure at `q=0.05`. Task-type estimates are exploratory and reported with uncertainty but without separate confirmatory claims.

H1 is supported if at least one corrected feature/family test is non-zero. H2 is evaluated with the two family-specific estimates and their uncertainty visible; sign agreement alone is not treated as proof of a general generation effect. These analyses explain the measured differences but do not establish that they transfer.

### 6.5 Cross-genre generalisation

For each family, five leave-one-task-type-out evaluations are run. In each evaluation, the fixed classifier is fitted on four task types and tested on the complete fifth type. Median imputation and standardisation are fitted on training data only. Results include balanced accuracy, macro-F1, ROC-AUC, confusion counts, and uncertainty for every family × held-out-task cell. The complete cell table is primary; an average across task types cannot hide one failed genre.

### 6.6 Cross-family transfer

The primary classifier is L2-regularized logistic regression with fixed `C=1`. A scikit-learn pipeline fits median imputation and standardisation on training data only. It is evaluated in both directions: train on all Llama responses and test on Gemma, then train on Gemma and test on Llama. Both directions are reported separately against a stratified dummy baseline.

A stricter robustness test changes both family and prompt: five prompt-grouped folds train on source-family responses from four folds and test on target-family responses whose `prompt_id` values are in the fifth. This distinguishes transfer to a new family from memorisation of prompt-specific content. The report includes balanced accuracy, macro-F1, ROC-AUC, fold results, prompt-level bootstrap uncertainty, confusion matrices, and standardised coefficients. Coefficients are associations among correlated measurements, not causal effects.

### 6.7 Baselines, length sensitivity, and exploration

Prompt-blocked five-fold within-family classification establishes simple separability but is a supporting baseline, not the contribution. Actual word count is audited. The analysis is repeated with actual length as an explicit covariate and on a preregistered length-matched subset; a 120–150-word prompt instruction is not described as complete length control.

The 30 features are standardised before PCA. Explained variance and loadings are reported, and points are marked by generation, family, and task type. Clustering is optional and secondary; it uses multiple seeds and stability checks. Visual separation or cluster composition is not evidence of transfer.

## 7. Risks and limitations

The design contains only two families and one predecessor/successor pair per family. Family is therefore a fixed comparison, not a population sample. The pairs differ somewhat in parameter count, training, architecture, tokenization, alignment, context length, and native chat template. These differences are scientifically interesting parts of deployed versions but prevent causal attribution to age alone.

Prompt genre and output length can dominate linguistic features. Pairing every prompt across models, balancing task types, holding out complete task types, using normalised features, and running length-aware sensitivity analyses reduce these threats. Automated SpaCy annotation can introduce measurement error, addressed through one pinned pipeline and a manual audit. Temperature-zero single runs prioritise reproducibility but do not estimate stochastic decoding variation. Twenty prompts per task type make individual genre estimates imprecise, and two families provide only two predecessor-successor replications. Results may not generalise beyond English, short prompted texts, Ollama's quantised implementations, or the four exact manifests.

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
| 27 Oct–9 Nov | feature contrasts | reproducible summaries | paired bootstrap/permutation analysis | interpret H1–H2 |
| 10–23 Nov | generalisation tests | cross-genre/cross-family pipelines | coefficient and failure analysis | interpret H3–H4 |
| 24 Nov–7 Dec | robustness and exploration | unseen-prompt, PCA, stability code | length and genre sensitivity analysis | retain only preregistered conclusions |
| 8–21 Dec | final report | methods/reproducibility sections | background/results discussion | joint full-paper revision |
| 22–31 Dec | submission | clean re-run and release | citation/argument audit | final GitHub submission |

Both contributors participate across all stages; the primary column denotes responsibility for producing the first complete version, while the other contributor reviews it.

## 9. Expected outcomes

Three result patterns are meaningful:

1. **Transferable pattern:** feature directions agree, held-out-task performance is stable, and transfer works in both family directions. This supports a limited shared pattern for the selected transitions.
2. **Family- or genre-specific fingerprints:** within-family separation is present, but cross-family or cross-genre transfer fails. This is evidence against a shared generation-associated fingerprint and is a central result rather than a failed experiment.
3. **Insufficient interpretable signal:** paired effects are small and all classifiers remain near baseline. This shows that the compact feature inventory does not distinguish the selected transitions reliably under the sampled conditions.

The study's contribution is therefore not contingent on obtaining high accuracy. It provides a controlled test, an interpretable feature inventory, and a reproducible corpus design that can later be extended to more families, languages, genres, or repeated generations.

## 10. Reproducibility and data management

Prompts, configurations, source code, feature definitions, analysis notebooks, environment requirements, seeds, and the append-only run log are versioned in Git. Raw outputs are immutable and released only after checking model licenses, provider terms, privacy, and repository size. Derived tables are reproducible from documented commands. Exact Ollama manifest IDs are recorded in the proposal configuration and runtime digests are captured again immediately before collection.

## References

Gude, A., Santos-Rios, R., Bond, F., Flickinger, D., Gómez-Rodríguez, C., & Zamaraeva, O. (2026). More aligned, less diverse? Analyzing the grammar and lexicon of two generations of LLMs. *Proceedings of ACL 2026*, 38900–38911. https://doi.org/10.18653/v1/2026.acl-long.1803

Guo, Y., Shang, G., & Clavel, C. (2025). Benchmarking linguistic diversity of large language models. *Transactions of the Association for Computational Linguistics, 13*, 1507–1526. https://doi.org/10.1162/tacl.a.47

Huynh, L., & McNamara, D. S. (2026). Evaluation of linguistic consistency of LLM-generated text personalization using natural language processing. *Electronics, 15*(6), 1262. https://doi.org/10.3390/electronics15061262

Munir, S., Batool, B., Shafiq, Z., Srinivasan, P., & Zaffar, F. (2021). Through the looking glass: Learning to attribute synthetic text generated by language models. *Proceedings of EACL 2021*, 1811–1822. https://doi.org/10.18653/v1/2021.eacl-main.155

Przystalski, K., Argasiński, J. K., Grabska-Gradzińska, I., & Ochab, J. K. (2026). Stylometry recognizes human and LLM-generated texts in short samples. *Expert Systems with Applications, 296*, 129001. https://doi.org/10.1016/j.eswa.2025.129001

Rudnicka, K., & Juzek, T. S. (2026). Beyond “AI Language”: The case for the idiolectal nature of LLM output. *arXiv preprint*. https://arxiv.org/abs/2608.06589

Uchendu, A., Le, T., Shu, K., & Lee, D. (2020). Authorship attribution for neural text generation. *Proceedings of EMNLP 2020*, 8384–8395. https://doi.org/10.18653/v1/2020.emnlp-main.673

Xia, Y., Stańczak, K., & Roth, B. (2026). Explaining generalization of AI-generated text detectors through linguistic analysis. *Proceedings of EACL 2026*, 6524–6546. https://doi.org/10.18653/v1/2026.eacl-long.307

Xu, H., Ren, J., He, P., Zeng, S., Cui, Y., Liu, A., Liu, H., & Tang, J. (2024). On the generalization of training-based ChatGPT detection methods. *Findings of EMNLP 2024*, 7223–7243. https://doi.org/10.18653/v1/2024.findings-emnlp.424

Zahid, I., Madusanka, T., Batista-Navarro, R., & Sun, Y. (2024). Probing the uniquely identifiable linguistic patterns of conversational AI agents. *Findings of ACL 2024*, 4612–4628. https://doi.org/10.18653/v1/2024.findings-acl.274

Model reports and release documentation are listed with verified URLs in `literature/REFERENCES.md` and the exact runtime models are frozen in `config/models.yaml`.

## Approval status

This proposal replaces the previous SpaCy–LLM disagreement topic and supersedes the earlier separability-focused framing. The cross-family and cross-genre objective is ready for supervisor review; the topic change and final proposal still require approval.
