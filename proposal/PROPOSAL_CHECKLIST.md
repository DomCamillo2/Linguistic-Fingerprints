# Proposal checklist

This checklist maps the course proposal requirements to the current draft and separates completed design work from decisions that require human approval or empirical validation.

## Course requirements

| Requirement | Proposal location | Status |
|---|---|---|
| Title and contributors | Title and contributors | Complete; responsibility split needs both contributors' confirmation |
| Introduction and motivation | Section 1 | Complete |
| Research objective and questions | Section 2 | Complete |
| Testable hypotheses | Section 3 | Complete |
| Preliminary literature review | Section 4 and `literature/` | Complete with verified primary sources |
| Data and scope | Section 5 | Complete at proposal level |
| Methodology | Section 6 | Complete at proposal level |
| Risks and limitations | Section 7 | Complete |
| Work and time plan | Section 8 | Complete; dates and ownership need both contributors' confirmation |
| Expected outcomes | Section 9 | Complete |
| Reproducibility and data management | Section 10 | Complete |
| References | References and `literature/references.bib` | Complete for proposal submission |

## Decisions frozen for the proposal

- Research question: linguistic profiles of selected earlier/later versions within matched Llama and Gemma families.
- Models: the four exact Ollama Q4_K_M tags in `config/models.yaml`.
- Language and corpus: English; 100 prompts; five balanced task types; 400 planned responses.
- Output: 120–150 words; one deterministic response per prompt/model; seed 42.
- Features: 30 transparent confirmatory measures plus three audit-only length/diversity measures.
- Primary inference: within-prompt later-minus-earlier contrasts within each family, prompt bootstrap, paired permutation tests, and BH correction.
- Predictive evaluation: L2 logistic regression with five-fold `StratifiedGroupKFold` grouped by `prompt_id`.

## Required before submission

- [ ] Dominik and Luca verify the stated division of work and timeline.
- [ ] Proofread names, course metadata, and any required cover-page information.
- [ ] Confirm the proposal's required submission format and length with the course instructions.
- [ ] Submit the topic change and proposal for supervisor approval.

## Required after proposal approval and before the main run

- [ ] Install the four model tags and capture local Ollama/runtime digests.
- [ ] Expand the pilot registry to the reviewed 100-prompt final registry.
- [ ] Run all 80 pilot cells and apply the preregistered quality gates.
- [ ] Audit a stratified sample of responses and SpaCy annotations.
- [ ] Record any pilot-motivated changes consistently in the proposal, configs, and run log.
- [ ] Mark the final prompt, feature, and analysis configuration as the main-run freeze.

No main-corpus generation should begin before these items pass.
