# Run and decision log

Append entries; never erase history.

## 2026-08-27 — repository initialization

- Created project structure, LLM instructions, proposal draft, data contract, configuration templates, pilot prompts, validation/feature code, tests, and CI.
- Added searchable Markdown for all 12 course lecture sessions and assignment sheets.
- Did not add original lecture PDFs or official solutions because the repository is public.
- Scientific design uses two matched model families with earlier/later versions and prompt-blocked predictive evaluation.
- Main-run status: **not started**; exact models and design are not frozen.

## 2026-08-27 — proposal design and literature freeze

- Reframed the study as a matched-family, prompt-controlled replication and extension of recent work on linguistic differences across LLM generations.
- Selected proposal-level pairs: Llama 2 7B Chat / Llama 3.1 8B Instruct and Gemma 2 9B IT / Gemma 3 12B IT, all through Ollama Q4_K_M.
- Verified public tags, release metadata, parameter counts, and manifest IDs; checked local 24-GB Apple M4 Pro feasibility.
- Fixed English, 100 prompts across five balanced task types, a 120–150-word target, one response per cell, temperature 0, and seed 42.
- Fixed 30 confirmatory features, paired prompt bootstrap/permutation inference, BH correction across 60 tests, and prompt-blocked L2 logistic regression.
- Added an annotated literature review, BibTeX database, exact model configuration, proposal checklist, and expanded proposal draft.
- No models were downloaded and no generations or analyses were run. Main-run status remains **not started** pending approval, installation, prompt completion, and pilot.
