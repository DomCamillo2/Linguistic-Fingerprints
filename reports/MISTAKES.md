# Known mistakes and anti-patterns

## Data leakage

**Wrong:** randomly split individual responses into train and test sets.

**Why:** another response to the same prompt can appear in training, allowing the classifier to exploit prompt content.

**Required:** keep every response sharing a prompt_id in the same fold. For leave-one-task-type-out evaluation, withhold the complete task type.

## Ignoring the paired design

**Wrong:** treat all 400 response rows as independent observations for feature inference.

**Required:** calculate later-minus-earlier differences within prompt and family, then analyse prompts as the sampling units.

## Overclaiming novelty

**Wrong:** claim that no previous study compares LLM versions with matched prompts, interpretable features, or grouped evaluation.

**Why:** Przystalski et al. already combine these elements for Llama 2 and Llama 3.

**Required:** present the work as a controlled replication and task-type robustness study.

## Scope creep

Mixed-effects models, cross-family classifier transfer, clustering, neural detectors, and additional tuned classifiers are not part of the confirmatory proposal. Do not add them merely because helper code exists.

## Universal generation claims

**Wrong:** state that newer LLMs generally use more adjectives.

**Required:** describe a feature difference for the selected later version, family, prompts, and settings.

## Confusing family and version

Pooling Llama and Gemma can hide opposite within-family directions. Always report both family-specific comparisons.

## Length-sensitive diversity

Raw TTR falls as text length increases. Use MATTR for confirmatory diversity, audit actual word counts, and run the planned sensitivity analysis.

## Feature leakage

Imputation and scaling fitted on the full dataset leak test information. Fit them inside each training fold.

## Accuracy-only reporting

Report a dummy baseline, balanced accuracy, macro-F1, fold behaviour, and confusion matrices. Accuracy alone does not answer the linguistic question.

## PCA interpretation

PCA axes are weighted combinations of scaled features. Inspect loadings and explained variance. Visual separation is exploratory evidence only.

## Post-hoc feature fishing

Features selected after seeing held-out performance are exploratory and require confirmation on fresh data.

## Silent retries

Never overwrite a failed generation. Keep it and create a new run_id for any retry.
