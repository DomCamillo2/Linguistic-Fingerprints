# Data contract

## Raw generations

The canonical file is `data/raw/generations.csv`. It is ignored until a release review has confirmed provider terms, privacy, and file size.

Required columns:

| Column | Meaning |
|---|---|
| `run_id` | unique immutable generation attempt |
| `prompt_id` | stable prompt registry ID |
| `model_id` | project model ID from `config/models.yaml` |
| `family` | matched model family |
| `generation` | `earlier` or `later` |
| `task_type` | registered prompt category |
| `prompt_text` | exact user prompt |
| `system_prompt` | exact system instruction |
| `response_text` | unmodified model response |
| `provider_model_id` | exact provider/model identifier |
| `revision_or_digest` | immutable revision if available |
| `temperature` | decoding temperature |
| `top_p` | nucleus-sampling value |
| `seed` | provider seed if supported |
| `runtime_version` | exact Ollama version used for the attempt |
| `generation_options_json` | canonical JSON containing all generation options, including `top_k`, `repeat_penalty`, `num_ctx`, and `num_predict` |
| `created_at_utc` | ISO-8601 timestamp |
| `status` | `ok`, `refusal`, `error`, or `invalid` |
| `error` | raw error text when applicable |

Do not modify a row after collection. A retry receives a new `run_id`.

## Processed features

`data/processed/features.csv` contains one row per successful `run_id`. It retains the experimental identifiers and appends deterministic linguistic feature columns.

## Split rule

Ordinary within-family evaluation assigns all responses sharing a `prompt_id` to the same train/test fold. Never create random row-level splits.

The primary generalisation protocols add stronger domain boundaries:

- cross-genre: hold out the complete `task_type`;
- cross-family: train on one complete family and test on the other, in both directions;
- strict robustness: train on source-family prompt folds and test on the target family with held-out `prompt_id` values.

Fit imputation, scaling, feature selection, and any model tuning on training-domain rows only.
