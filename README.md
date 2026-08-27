# Generalising Linguistic Fingerprints across LLM Families and Genres

A controlled corpus-linguistic study of whether interpretable predecessor-successor differences transfer across open-weight model families and unseen writing-task types.

## Research question and gap

> To what extent do linguistically interpretable predecessor-successor differences generalise across open-weight model families and text genres?

Prior work already shows that LLM versions can be distinguished. Most notably, Przystalski et al. compare Llama 2 and Llama 3 under matched prompts with interpretable stylometric features and topic-grouped cross-validation. The novelty claim is therefore **not** that this project is the first controlled comparison of earlier and later versions.

The narrower gap is whether an earlier-to-later contrast learned in one open-weight family transfers to another family and remains detectable when an entire writing-task type is unseen during training. The project asks:

1. Which of the 30 prespecified linguistic features change from Llama 2 to Llama 3.1 and from Gemma 2 to Gemma 3?
2. Do the directions of those changes agree across the two families?
3. Do classifiers retain signal on a held-out writing-task type?
4. Does an earlier-versus-later classifier trained on Llama transfer to Gemma, and vice versa?
5. Does cross-family transfer survive the stricter condition in which target prompts are also unseen?

The scientific outcome is the generalisation pattern, not classification accuracy by itself. Failure to transfer is informative evidence that the measured differences are family- or version-specific fingerprints rather than a shared generation-associated shift.

## Planned design

| Dimension | Planned value |
|---|---|
| Model comparison | Llama 2 7B Chat → Llama 3.1 8B Instruct; Gemma 2 9B IT → Gemma 3 12B IT |
| Language | English |
| Prompt bank | 100 prompts; 20 in each of five writing-task types |
| Pairing | Every model receives every registered prompt |
| Output length | 120–150 requested words; actual length audited and controlled in sensitivity analyses |
| Sampling | One deterministic response per prompt/model; seed 42 |
| Features | 30 prespecified, interpretable linguistic measures |
| Supporting analysis | Paired earlier-to-later feature contrasts within each family |
| Cross-genre analysis | Leave one writing-task type out, separately by family |
| Cross-family analysis | Llama → Gemma and Gemma → Llama transfer |
| Strict robustness test | Cross-family transfer with target `prompt_id` values withheld from training |
| Baseline | Prompt-blocked within-family L2 logistic regression and dummy classifier |

The proposal-level design and exact Ollama tags are recorded in [config/study.yaml](config/study.yaml) and [config/models.yaml](config/models.yaml). They become the main-run freeze only after all four models have been installed and the pilot has passed its documented quality gates.

## Non-negotiable validity rules

- The same registered prompt text, system instruction, decoding settings, and requested length are used for every model.
- Raw generations are immutable and retain exact model/runtime provenance.
- Feature scaling and imputation are fitted on training data only.
- Ordinary predictive evaluation groups by `prompt_id`; cross-genre evaluation holds out the complete writing-task type.
- Cross-family results are reported in both directions and never replaced by a pooled score.
- Length is measured rather than assumed to be controlled by a prompt instruction. Results include a length-aware sensitivity analysis.
- Family-specific feature contrasts are reported before any cross-family interpretation.
- Claims are associations with the selected model versions, not effects caused by model age or training recency.
- With only two families, transfer is evidence about these pairs, not a universal trend among newer LLMs.

See [AGENTS.md](AGENTS.md) for operational rules and [PROJECT_PLAN.md](PROJECT_PLAN.md) for the complete analysis design.

## Repository map

```text
AGENTS.md                    instructions and scientific guardrails
PROJECT_PLAN.md              research design, estimands, and decision gates
proposal/                    course proposal and submission checklist
config/                      study, evaluation, and exact model configuration
prompts/                     pilot prompts and final prompt registry
data/raw/                    immutable model outputs (not committed by default)
data/interim/                validated and reshaped data
data/processed/              extracted feature matrices
src/linguistic_fingerprints/ validation, features, and generalisation protocols
scripts/                     command-line entry points
notebooks/                   numbered analysis narrative
reports/                     status, run log, and known pitfalls
literature/                  verified literature map and BibTeX
llm_corpus/                  searchable course extracts
tests/                       automated checks
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install .
python -m spacy download en_core_web_sm
python scripts/check_project.py
python -m pytest
```

After generation data follows the schema in [data/README.md](data/README.md):

```bash
python scripts/extract_features.py \
  --input data/raw/generations.csv \
  --output data/processed/features.csv

python scripts/evaluate_generalization.py \
  --input data/processed/features.csv \
  --output reports/generalization_results.csv
```

The second command produces logistic-regression and stratified-dummy results for leave-one-task-type-out evaluation, direct cross-family transfer, cross-family transfer to unseen prompts, and the prompt-blocked within-family baseline. Every protocol runs once with the 30 confirmatory features and once with actual word count added as a length-sensitivity covariate. Confidence intervals and the post-pilot length-matched sensitivity analysis remain part of the report/notebook layer and must follow `PROJECT_PLAN.md`.

## Current status

The research question, literature positioning, configurations, and evaluation code have been updated for cross-genre and cross-family generalisation. Before the main run:

- obtain supervisor approval for the reframed objective;
- install and verify the four exact model manifests;
- complete and review the 100-prompt registry;
- run the pilot and audit length, refusals, formatting, and annotations;
- confirm that every writing-task type has enough valid paired responses for held-out evaluation;
- record the post-pilot analysis freeze.

The remaining human decisions are tracked in [proposal/PROPOSAL_CHECKLIST.md](proposal/PROPOSAL_CHECKLIST.md).
