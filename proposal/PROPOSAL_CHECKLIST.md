# Proposal checklist

This checklist maps the course proposal requirements to the simplified English draft.

## Course requirements

| Requirement | Proposal location | Status |
|---|---|---|
| Title and contributors | Title and contributors | Complete; both contributors should confirm the responsibility split |
| Introduction and motivation | Section 1 | Complete |
| Research objective and questions | Section 2 | Complete |
| Testable hypotheses | Section 3 | Complete |
| Preliminary literature review | Section 4 and literature/ | Complete with primary sources |
| Data and scope | Section 5 | Complete |
| Methodology | Section 6 | Complete |
| Risks and limitations | Section 7 | Complete |
| Work and time plan | Section 8 | Complete; dates need confirmation |
| Expected outcomes, including null results | Section 9 | Complete |
| Reproducibility and data management | Section 10 | Complete |
| References | References and literature/references.bib | Complete for draft review |

## Decisions frozen for supervisor review

- Four exact Ollama model tags from config/models.yaml.
- English; 100 prompts; five balanced task types; 400 planned responses.
- One deterministic response per prompt/model with seed 42.
- Fifteen transparent confirmatory features.
- Paired later-minus-earlier comparisons inside each family.
- Prompt bootstrap intervals and paired t-tests with Bonferroni correction.
- Prompt-blocked five-fold L2 logistic regression with a dummy baseline.
- Leave-one-task-type-out as the single main robustness extension.
- Actual-length audit and length-covariate sensitivity.
- Optional PCA only if time permits.
- No mixed-effects model, cross-family classifier transfer, or required clustering.

## Required before submission

- [ ] Dominik and Luca confirm the title, responsibility split, and timeline.
- [ ] Add any required course, module, or cover-page metadata.
- [ ] Confirm the submission format and maximum length.
- [ ] Ask the supervisor to approve the simplified scope and wording.
- [ ] Proofread the final exported proposal.

## Required after approval and before the main run

- [ ] Install all four model tags and capture local runtime digests.
- [ ] Expand and review the final 100-prompt registry.
- [ ] Run all 80 pilot cells and apply the quality gates.
- [ ] Audit a stratified sample of responses and SpaCy annotations.
- [ ] Confirm sufficient valid pairs in every task type.
- [ ] Freeze features, splits, metrics, length sensitivity, and seeds.
- [ ] Record any pilot-motivated amendment in the proposal, plan, config, and run log.

No main-corpus generation should begin before these items pass.
