# Preparation status

Last updated: 2026-08-31

## Completed

- [x] Public repository and reproducible project structure created.
- [x] Searchable course lecture and assignment Markdown added without publishing the original PDFs.
- [x] Preliminary literature review completed with verified primary sources.
- [x] Closest matched-prompt Llama 2/3 precedent identified.
- [x] Exact Llama and Gemma model pairs selected.
- [x] English, 100 prompts, five task types, 120–150 words, and deterministic generation selected.
- [x] Proposal scope reviewed against the course project guidance.
- [x] English proposal reframed as controlled replication plus task-type robustness.
- [x] Confirmatory inventory reduced from 30 to 15 features.
- [x] Mixed models, cross-family transfer, and required clustering removed from the confirmatory plan.
- [x] Default evaluation command aligned with prompt-blocked and leave-one-task-type-out analysis.
- [x] Data contract, pilot registry, extraction code, tests, and CI scaffolding added.

## Required before submission or supervisor sign-off

- [ ] Both contributors confirm the title, division of work, and timeline.
- [ ] Confirm required proposal format, length, and cover metadata.
- [ ] Obtain supervisor approval for the simplified replication-and-robustness design.

## Required before the main run

- [ ] Install all four exact model tags and capture local runtime digests.
- [ ] Complete and review the 100-prompt bank.
- [ ] Run the 20-prompt pilot across all four models.
- [ ] Audit length compliance, failures, refusals, formatting, provenance, and annotations.
- [ ] Confirm enough valid paired responses in every task type.
- [ ] Preregister the exact length-matched sensitivity rule.
- [ ] Record the post-pilot analysis freeze.

## Current bottleneck

Supervisor approval and the four-model pilot are the current gates. No main corpus has been generated. Reusable cross-family evaluation functions remain in the repository, but they are explicitly outside the current proposal and default analysis.
