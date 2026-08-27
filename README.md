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
| Model comparison | 2 matched families × 2 versions (earlier/later) |
| Language | English working assumption; freeze before main collection |
| Prompts | 100–120 prompts, balanced across task types |
| Pairing | Every model receives every prompt |
| Output length | Same requested range for all models |
| Features | Approximately 20–30 predefined linguistic measures |
| Main analysis | Paired/grouped comparisons by prompt and family |
| Exploratory analysis | PCA and clustering |
| Predictive analysis | Interpretable old/new classifier with prompt-blocked CV |

Model pairs are deliberately not frozen yet. They must be comparable in scale and instruction-tuning status, accessible through a reproducible interface, and documented by immutable model identifiers.

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
config/                      study and model configuration templates
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

The repository is in the design/pilot stage. Before the main run, freeze:

- the two matched model families and four exact model identifiers;
- the study language;
- the final prompt registry;
- generation settings and target length;
- the primary feature list and statistical contrasts.
