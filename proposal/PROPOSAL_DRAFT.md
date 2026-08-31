# Project proposal

## Title and contributors

**Interpretable Linguistic Fingerprints of Earlier and Later Open-Weight LLM Versions: A Controlled Replication across Writing Tasks**

**Contributors:** Dominik Soballa and Luca Bouché.

The project is joint work. Dominik has primary responsibility for reproducible local inference, data engineering, and classification. Luca has primary responsibility for the literature review, prompt design, linguistic feature validation, and paired statistical analysis. Both contributors review the pilot, interpret the results, write the final report, and conduct the reproducibility audit.

## 1. Introduction and motivation

Large language models are often discussed in generations, but release date is not a single causal variable. Successive versions can differ in architecture, parameter count, tokenisation, training data, post-training, alignment, quantisation, and chat templates. A comparison of two versions therefore measures a difference associated with a deployed model transition; it cannot isolate the causal effect of being newer.

Previous work shows that generated texts contain identifiable linguistic traces. Uchendu et al. (2020), Munir et al. (2021), and Zahid et al. (2024) demonstrate model attribution and linguistic profiling. Przystalski et al. (2026) directly compare Llama 2 and Llama 3 on matched topics and prompt templates, using interpretable stylometric features and topic-grouped cross-validation. Huynh and McNamara (2026) analyse linguistic shifts across GPT updates under identical tasks, while Rudnicka and Juzek (2026) compare model cohorts with matched prompts.

This project therefore does not claim that matched-prompt comparisons or version fingerprints are new. Its contribution is a controlled course-level replication with two selected open-weight model pairs, a compact set of 15 interpretable features, five writing-task types, and leakage-safe evaluation. It adds one focused robustness question: does a within-family distinction survive when an entire writing-task type is unseen during training?

This scope follows the course guidance that a project should have a clear research question, feasible design, reproducible analysis, and interpretable conclusions. A completely novel research gap is helpful but not mandatory; replication on new data and informative null results are legitimate outcomes.

## 2. Research objective

**Main research question**

> Can earlier and later versions within the Llama and Gemma families be distinguished using a small set of interpretable linguistic features, and how robust is this distinction across unseen prompts and writing-task types?

**Subquestions**

1. Which prespecified lexical, morphosyntactic, and structural features differ between the earlier and later version within each family?
2. Can a simple classifier distinguish the versions on prompts that were not used for training?
3. Does the distinction remain when an entire writing-task type is absent from training?
4. Are the observed patterns similar or different in the two family-specific case studies?

The last question is descriptive. The project does not train on one family and test on the other, and it does not claim a universal generation effect.

## 3. Hypotheses

- **H1 — Paired feature differences:** At least one of the 15 prespecified features differs between the earlier and later version within at least one family after Bonferroni correction.
- **H2 — Unseen-prompt classification:** Within each family, a fixed L2-regularised logistic-regression classifier performs above a stratified dummy baseline under five-fold prompt-blocked cross-validation.
- **H3 — Task-type robustness:** Within each family, the classifier remains above the dummy baseline when each complete writing-task type is held out in turn.

A failure to support H2 or H3 is informative. It would indicate that the selected interpretable features are insufficient or that the measured fingerprint depends on prompt genre.

## 4. Preliminary literature review and project contribution

Neural-text authorship research shows that generators leave detectable traces. Uchendu et al. (2020) formulate source-generator attribution, Munir et al. (2021) identify inherited source-model signals, and Zahid et al. (2024) use linguistic features, PCA, and classification to distinguish conversational AI agents.

The closest methodological precedent is Przystalski et al. (2026). They compare Llama 2, Llama 3, and other generators on matched Wikipedia topics and use topic-grouped cross-validation. Their study already combines version comparison, matched content, stylometric features, and grouped evaluation. Accordingly, none of these individual elements is presented as novel here.

Other recent work also reports linguistic change across model updates or cohorts. Gude et al. (2026) compare older and newer model groups in a news-writing setting. Huynh and McNamara (2026) examine GPT deployments using identical personalisation tasks. Rudnicka and Juzek (2026) report both cohort-level tendencies and model-specific profiles under matched prompts. Research on detector generalisation further shows that performance can degrade across prompts, tasks, models, and domains (Xu et al., 2024; Xia et al., 2026).

The project contribution is therefore deliberately modest: reproduce version-sensitive linguistic analysis with a smaller transparent inventory in two open-weight family pairs, then test whether within-family classification is robust to unseen prompts and unseen writing-task types. This is an incremental replication and robustness study rather than a claim of a completely unexplored phenomenon.

## 5. Data, models, and scope

### 5.1 Selected models

All models are instruction/chat-tuned variants run locally through Ollama with Q4_K_M quantisation.

| Family | Version role | Exact Ollama tag | Parameters | Release |
|---|---|---|---:|---|
| Meta Llama | earlier | llama2:7b-chat-q4_K_M | 6.74B | 18 July 2023 |
| Meta Llama | later | llama3.1:8b-instruct-q4_K_M | 8.03B | 23 July 2024 |
| Google Gemma | earlier | gemma2:9b-instruct-q4_K_M | 9.24B | 27 June 2024 |
| Google Gemma | later | gemma3:12b-it-q4_K_M | approximately 12B | 12 March 2025 |

The pairs differ in more than release date. Results concern these exact deployed versions and settings.

### 5.2 Prompt corpus

The study language is English. The final registry contains 100 prompts: 20 each for explanation, narrative, argumentation, advice/instruction, and reflection/description. Every prompt requests 120–150 words, is answerable without browsing, contains no personal data, and is sent unchanged to all four models.

The full design produces 100 prompts × 4 models = 400 responses. One deterministic response is collected per prompt/model cell with temperature 0 and seed 42. Prompts are the sampling and pairing units; decoding variability is not estimated.

### 5.3 In scope

- controlled local text generation and provenance;
- 15 prespecified interpretable features;
- paired earlier/later comparisons inside each family;
- prompt-blocked within-family logistic regression;
- leave-one-task-type-out robustness evaluation;
- length sensitivity;
- optional scaled PCA.

### 5.4 Out of scope

- mixed-effects models;
- cross-family classifier transfer;
- clustering as a required analysis;
- factual correctness, human preference, or overall model quality;
- human-versus-machine detection;
- multilingual analysis;
- causal attribution to model age or training recency;
- universal claims about LLM generations;
- neural or embedding-based detectors.

## 6. Methodology

### 6.1 Controlled local generation

The same system instruction, user prompt, and common decoding options are used for all models. Generation uses temperature 0, top_p 1, top_k 40, repeat_penalty 1, seed 42, num_ctx 4096, and num_predict 384. Each model retains its native chat template and stop tokens, which are treated as part of the deployed version.

Every attempt receives an immutable run_id. Stored metadata includes prompt_id, model_id, family, version role, runtime digest, exact messages, decoding settings, Ollama version, timestamp, status, raw response, and error text. Failed attempts remain in the raw table; retries create new rows.

### 6.2 Pilot and quality gates

The 20-prompt pilot contains four prompts per task type and is run across all four models. The pilot passes if:

- all four model tags load on the available hardware;
- at least 95% of the 80 planned responses have status ok;
- at least 80% fall within the requested word range;
- no model has a refusal or formatting-failure rate above 10%;
- provenance fields are complete;
- every task type retains sufficient valid earlier/later pairs.

If a common prompt wording change is necessary, the prompt version is incremented and the complete pilot is repeated.

### 6.3 Linguistic processing and feature inventory

All successful responses are processed with one pinned English SpaCy pipeline. A stratified 10% sample is manually inspected for sentence-boundary and POS errors.

The 15 confirmatory features are:

- structure and length: sentence count, mean word length, mean sentence length, and sentence-length standard deviation;
- lexical style: MATTR with a 50-token window, repeated-token rate, repeated-bigram rate, and adjacent-sentence lexical overlap;
- function and style markers: function-word, modal, connective, and punctuation proportions;
- UPOS proportions: adjective, noun, and verb.

Actual word count, surface-token count, raw TTR, and additional extracted columns are audit or exploratory variables. Only the frozen 15 features enter confirmatory tests and classifiers.

### 6.4 Paired feature analysis

Coverage, failures, length, and feature distributions are first summarised by model, family, version role, task type, and prompt.

For each prompt and feature, the analysis calculates later minus earlier separately inside Llama and Gemma. For every family × feature combination, it reports the mean paired difference, a standardised paired effect, and a 95% confidence interval from prompt-level bootstrap resampling. A paired t-test is used for each comparison, with Bonferroni correction across the 30 family × feature tests.

Pairing by prompt controls prompt content directly. The two families are reported separately; similar directions are descriptive replication, not proof of a universal effect.

### 6.5 Prompt-blocked classification

The primary predictive model is L2-regularised logistic regression with fixed C=1. A pipeline fits median imputation and standardisation on training data only. The comparison is earlier versus later within each family.

Five-fold cross-validation is grouped by prompt_id so all responses to the same prompt remain in one fold. A stratified dummy classifier uses the same folds. Results include balanced accuracy, macro-F1, fold-level scores, and confusion matrices. No hyperparameter search is planned.

### 6.6 Leave-one-task-type-out evaluation

For each family, the classifier is trained on four task types and tested on the complete fifth type. This is repeated for all five task types. All family × held-out-task results are reported, not only an average. The procedure tests robustness to genre shift and is stricter than ordinary unseen-prompt evaluation.

### 6.7 Length sensitivity and optional exploration

Actual word count is audited. Classification is repeated with word count as an explicit covariate and, if the pilot supports an objective rule, on a preregistered length-matched subset.

PCA is optional and exploratory. Features are standardised, and explained variance and loadings are reported. Visual separation is not treated as hypothesis-test evidence.

## 7. Risks and limitations

Only two families and one predecessor-successor pair per family are included. The models differ in architecture, parameter count, training, alignment, tokenizer, and chat template, so causal claims about age are impossible. The project uses short English responses, local quantised models, and a single deterministic generation per prompt/model cell.

Prompt genre and length may dominate linguistic features. Matched prompts, prompt grouping, leave-one-task-type-out evaluation, normalised rates, and length sensitivity reduce these threats. SpaCy annotations can contain errors, which motivates a manual audit. Twenty prompts per task type yield limited precision for individual held-out-task estimates. Classification performance demonstrates separability under the sampled conditions, not linguistic importance or model quality.

## 8. Work and time plan

| Dates | Deliverable | Dominik — primary | Luca — primary | Joint checkpoint |
|---|---|---|---|---|
| 27–31 Aug | literature, scope, and proposal | runtime feasibility | literature and proposal | approve simplified design |
| 1–14 Sep | final prompt bank and tooling | generation implementation | prompt expansion and audit | code and prompt review |
| 15–28 Sep | four-model pilot | install and run models | response and annotation audit | pilot pass/fail decision |
| 29 Sep–12 Oct | main corpus | resumable generation | quality monitoring | verify 400 cells |
| 13–26 Oct | feature corpus | extraction and validation | linguistic audit | freeze analysis table |
| 27 Oct–9 Nov | paired analysis | reproducible tables | bootstrap and paired tests | interpret H1 |
| 10–23 Nov | classification | grouped and held-out-task runs | error analysis | interpret H2–H3 |
| 24 Nov–7 Dec | sensitivity and optional PCA | reproducible reruns | length and task analysis | freeze conclusions |
| 8–21 Dec | report | methods and reproducibility | background and discussion | full-paper revision |
| 22–31 Dec | submission | clean rerun | citation and claim audit | final release |

Both contributors participate across all stages. Primary responsibility indicates who produces the first complete version.

## 9. Expected outcomes

Three outcomes are scientifically useful:

1. **Robust within-family fingerprints:** paired effects and classification remain visible on unseen prompts and task types.
2. **Task-specific fingerprints:** ordinary grouped classification works, but held-out-task performance falls to baseline.
3. **Insufficient evidence:** effects are small and classifiers remain near the dummy baseline.

The second and third outcomes do not make the project a failure. They delimit what the selected transparent features can support.

## 10. Reproducibility and data management

Prompts, configurations, feature definitions, scripts, environment requirements, seeds, and the append-only run log are versioned in Git. Raw outputs are immutable. Generated corpora are released only after license, privacy, provider-term, and file-size review. Derived tables must be reproducible from documented commands.

## References

Gude, A., Santos-Rios, R., Bond, F., Flickinger, D., Gómez-Rodríguez, C., & Zamaraeva, O. (2026). More aligned, less diverse? Analyzing the grammar and lexicon of two generations of LLMs. Proceedings of ACL 2026, 38900–38911. https://doi.org/10.18653/v1/2026.acl-long.1803

Huynh, L., & McNamara, D. S. (2026). Evaluation of linguistic consistency of LLM-generated text personalization using natural language processing. Electronics, 15(6), 1262. https://doi.org/10.3390/electronics15061262

Munir, S., Batool, B., Shafiq, Z., Srinivasan, P., & Zaffar, F. (2021). Through the looking glass: Learning to attribute synthetic text generated by language models. Proceedings of EACL 2021, 1811–1822. https://doi.org/10.18653/v1/2021.eacl-main.155

Przystalski, K., Argasiński, J. K., Grabska-Gradzińska, I., & Ochab, J. K. (2026). Stylometry recognizes human and LLM-generated texts in short samples. Expert Systems with Applications, 296, 129001. https://doi.org/10.1016/j.eswa.2025.129001

Rudnicka, K., & Juzek, T. S. (2026). Beyond AI Language: The case for the idiolectal nature of LLM output. arXiv preprint. https://arxiv.org/abs/2608.06589

Uchendu, A., Le, T., Shu, K., & Lee, D. (2020). Authorship attribution for neural text generation. Proceedings of EMNLP 2020, 8384–8395. https://doi.org/10.18653/v1/2020.emnlp-main.673

Xia, Y., Stańczak, K., & Roth, B. (2026). Explaining generalization of AI-generated text detectors through linguistic analysis. Proceedings of EACL 2026, 6524–6546. https://doi.org/10.18653/v1/2026.eacl-long.307

Xu, H., Ren, J., He, P., Zeng, S., Cui, Y., Liu, A., Liu, H., & Tang, J. (2024). On the generalization of training-based ChatGPT detection methods. Findings of EMNLP 2024, 7223–7243. https://doi.org/10.18653/v1/2024.findings-emnlp.424

Zahid, I., Madusanka, T., Batista-Navarro, R., & Sun, Y. (2024). Probing the uniquely identifiable linguistic patterns of conversational AI agents. Findings of ACL 2024, 4612–4628. https://doi.org/10.18653/v1/2024.findings-acl.274

Full literature notes, verified links, and model documentation are stored in literature/REFERENCES.md and literature/references.bib.

## Approval status

This draft supersedes the earlier cross-family-transfer framing. The simplified replication-and-robustness design is ready for supervisor review. Final approval, model installation, prompt-bank completion, and the pilot are still pending.
