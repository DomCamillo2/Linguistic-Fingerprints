# Data contract

## Raw generations

The canonical file is data/raw/generations.csv. It remains ignored until a release review confirms provider terms, privacy, and file size.

Required columns:

| Column | Meaning |
|---|---|
| run_id | unique immutable generation attempt |
| prompt_id | stable prompt registry ID |
| model_id | project model ID from config/models.yaml |
| family | matched model family |
| generation | earlier or later |
| task_type | registered prompt category |
| prompt_text | exact user prompt |
| system_prompt | exact system instruction |
| response_text | unmodified model response |
| provider_model_id | exact provider/model identifier |
| revision_or_digest | immutable revision if available |
| temperature | decoding temperature |
| top_p | nucleus-sampling value |
| seed | provider seed if supported |
| runtime_version | exact Ollama version |
| generation_options_json | canonical JSON with all generation options |
| created_at_utc | ISO-8601 timestamp |
| status | ok, refusal, error, or invalid |
| error | raw error text when applicable |

Do not modify a collected row. A retry receives a new run_id.

## Processed features

data/processed/features.csv contains one row per successful run_id, retains the experimental identifiers, and appends deterministic linguistic measurements. The extractor can produce more columns than the 15 confirmatory features; only CONFIRMATORY_FEATURES enters the preregistered tests and classifiers.

## Pairing and split rules

For feature comparisons, pair the earlier and later response to the same prompt inside the same family.

For prompt-blocked classification, assign every response sharing a prompt_id to the same fold. Never use a random row-level split.

For leave-one-task-type-out evaluation, withhold the complete task_type and fit on the other four types.

Fit imputation and scaling on training rows only. Cross-family transfer is outside the current proposal.
