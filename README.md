# Linguistic Fingerprints across LLM Generations

A controlled corpus-linguistic study of whether earlier and later versions of matched large-language-model families exhibit distinguishable linguistic profiles under identical prompts.

## Research question

> Do earlier and later versions of matched LLM families exhibit distinguishable linguistic profiles under controlled prompting?

The project treats generated responses as a small experimental corpus. It measures transparent lexical, morphosyntactic, and stylistic features and asks:

1. Which features differ between selected earlier and later model versions?
2. Are the differences consistent across matched model families?
3. Do the texts occupy different regions in a lower-dimensional feature space?
4. Can an interpretable classifier distinguish the two version groups on unseen prompts?

The goal is explanation, not a model leaderboard. Predictive accuracy is secondary to identifying stable linguistic features.

## Planned design

| Dimension | Planned value |
|---|---|
| Model comparison | Llama 2 7B Chat → Llama 3.1 8B Instruct; Gemma 2 9B IT → Gemma 3 12B IT |
| Language | English |
| Prompts | 100 prompts; 20 in each of five task types |
| Pairing | Every model receives every prompt |
| Output length | 120–150 words for every response |
| Sampling | One deterministic response per prompt/model; seed 42 |
| Features | 30 predefined linguistic measures |
| Main analysis | Paired prompt-level contrasts within each family |
| Exploratory analysis | PCA and clustering |
| Predictive analysis | L2 logistic regression with prompt-blocked 5-fold CV |

The proposal-level design and exact Ollama tags are recorded in [config/study.yaml](config/study.yaml) and [config/models.yaml](config/models.yaml). They become the main-run freeze only after all four models have been installed and the 20-prompt pilot has passed its documented quality gates.

## Non-negotiable validity rules

- The same prompt, system instruction, decoding settings, and length request are used for every model.
- Responses to one `prompt_id` never appear in both training and test data.
- Feature scaling and selection are fitted inside each training fold, never on the full dataset.
- Raw generations are append-only and accompanied by provenance metadata.
- Length-sensitive lexical diversity uses MATTR or a comparable robust measure, not raw TTR alone.
- PCA components and cluster labels are treated as exploratory, not self-explanatory linguistic categories.
- Conclusions are limited to the sampled prompts and selected model versions.

See [AGENTS.md](AGENTS.md) for operational rules and [PROJECT_PLAN.md](PROJECT_PLAN.md) for the complete design.

## Repository map

```text
AGENTS.md                    instructions and guardrails for LLM/coding agents
llms.txt                     short LLM entry point
PROJECT_PLAN.md              locked research design and decision gates
proposal/                    course proposal draft
config/                      proposal-level study and exact model configuration
prompts/                     pilot prompts and final prompt registry
data/raw/                    immutable model outputs (not committed by default)
data/interim/                validated and reshaped data
data/processed/              extracted feature matrices
src/linguistic_fingerprints/ reusable validation and feature code
scripts/                     command-line entry points
notebooks/                   numbered analysis narrative
reports/                     status, run log, and known pitfalls
llm_corpus/                  searchable course-slide and assignment extracts
tests/                       automated checks
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m spacy download en_core_web_sm
python scripts/check_project.py
python -m pytest
```

After generation data follows the schema in [data/README.md](data/README.md):

```bash
python scripts/extract_features.py \
  --input data/raw/generations.csv \
  --output data/processed/features.csv
```

## Course context

`llm_corpus/` contains searchable Markdown extracts of all 12 lecture sessions and the assignment sheets. Each lecture extract retains `source_pdf` metadata and `<!-- page:N -->` markers for precise citation. Original lecture PDFs and official solutions are intentionally not published in this public repository.

## Current status

The proposal design, preliminary literature review, model selection, and analysis plan are complete. Before the main run:

- obtain supervisor approval for the topic change;
- install and verify all four exact model manifests;
- complete and review the 100-prompt registry;
- run the 20-prompt pilot and apply its pass/fail gates;
- record the resulting final analysis freeze.

The course-requirement mapping and remaining human decisions are tracked in [proposal/PROPOSAL_CHECKLIST.md](proposal/PROPOSAL_CHECKLIST.md).
