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

## 2026-08-27 — generalisation-focused reframing

- Replaced the simple “are earlier and later versions distinguishable?” objective with cross-genre and bidirectional cross-family generalisation.
- Added Przystalski et al. (2026) as the closest precedent and removed claims that matched prompts, interpretable features, direct Llama version comparison, or grouped evaluation are novel.
- Added Huynh and McNamara (2026) and Rudnicka and Juzek (2026) to the literature positioning.
- Made leave-one-task-type-out and Llama ↔ Gemma transfer primary; retained within-family classification as a baseline.
- Added the stricter cross-family/unseen-prompt robustness protocol and required length-aware sensitivity analyses.
- Added reusable evaluation code, a CLI, and automated tests. No model outputs or empirical study results were created.
- Main-run status remains **not started** pending supervisor approval, installation, full prompt-bank review, pilot, and final freeze.

## 2026-08-31 — course-aligned scope reduction

- Revised the English proposal after reviewing the course project guidance, especially the expected scope and the value of replication on new data.
- Reframed the contribution as a controlled replication and robustness study rather than a claim of a new universal cross-family fingerprint.
- Retained four exact models, 100 matched English prompts, five task types, and deterministic local generation.
- Reduced the confirmatory inventory from 30 to 15 interpretable features.
- Made paired within-family contrasts and prompt-blocked logistic regression the primary analyses.
- Retained leave-one-task-type-out evaluation as the single robustness extension.
- Removed mixed-effects modelling, cross-family classifier transfer, clustering, permutation testing, and false-discovery-rate procedures from the confirmatory plan.
- Updated the default evaluation command to run only the two course-aligned classification protocols. Reusable cross-family helper functions remain in the codebase for explicitly labelled future or exploratory work.
- No models were downloaded and no generations or empirical analyses were run. The main run remains blocked on supervisor approval, model installation, prompt-bank completion, and the four-model pilot.
