# Known mistakes and anti-patterns

## Data leakage

**Wrong:** randomly split individual responses into train and test sets.

**Why:** the classifier can exploit prompt topic or wording because other responses to the same prompt occur in training.

**Required:** group every response with the same `prompt_id` into the same fold.

## Universal generation claims

**Wrong:** “new LLMs use more adjectives.”

**Required:** “the selected later versions used a higher adjective proportion under these prompts and settings,” followed by family-specific evidence.

## Confusing family and generation

Pooling two earlier and two later models can hide opposite within-family directions. Always report earlier/later contrasts inside each family before pooled summaries.

## Length-sensitive diversity

Raw TTR falls as text length increases. Prefer MATTR or another length-robust metric and audit actual output length.

## PCA interpretation

Principal components are weighted mixtures of scaled features. Inspect loadings; do not name an axis from a visually convenient story alone.

## Feature leakage

Scaling, imputation, selection, and PCA fitted on the full dataset leak test information. Put every learned transformation inside the cross-validation pipeline.

## Accuracy-only reporting

Report baseline, balanced accuracy, macro-F1, uncertainty, fold behavior, and interpretable feature evidence. Accuracy alone does not answer the linguistic question.

## Silent retries

Never overwrite a failed generation. Record it and create a new `run_id` for any retry.

## Post-hoc feature fishing

Features selected after viewing test performance require confirmation on fresh data and must be labeled exploratory.
