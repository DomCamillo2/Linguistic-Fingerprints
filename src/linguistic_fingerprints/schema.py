"""Validation for the immutable generation table."""

from __future__ import annotations

import pandas as pd


REQUIRED_GENERATION_COLUMNS = {
    "run_id",
    "prompt_id",
    "model_id",
    "family",
    "generation",
    "task_type",
    "prompt_text",
    "system_prompt",
    "response_text",
    "provider_model_id",
    "revision_or_digest",
    "temperature",
    "top_p",
    "seed",
    "created_at_utc",
    "status",
    "error",
}

VALID_GENERATIONS = {"earlier", "later"}
VALID_STATUSES = {"ok", "refusal", "error", "invalid"}


def validate_generations(df: pd.DataFrame) -> list[str]:
    """Return human-readable validation errors without mutating *df*."""

    errors: list[str] = []
    missing = sorted(REQUIRED_GENERATION_COLUMNS - set(df.columns))
    if missing:
        errors.append(f"missing required columns: {', '.join(missing)}")
        return errors

    if df["run_id"].isna().any():
        errors.append("run_id contains missing values")
    duplicate_ids = df.loc[df["run_id"].duplicated(keep=False), "run_id"].dropna()
    if not duplicate_ids.empty:
        errors.append(f"run_id is not unique: {sorted(duplicate_ids.astype(str).unique())[:5]}")

    invalid_generations = sorted(set(df["generation"].dropna()) - VALID_GENERATIONS)
    if invalid_generations:
        errors.append(f"invalid generation labels: {invalid_generations}")

    invalid_statuses = sorted(set(df["status"].dropna()) - VALID_STATUSES)
    if invalid_statuses:
        errors.append(f"invalid status labels: {invalid_statuses}")

    ok_without_text = df["status"].eq("ok") & df["response_text"].fillna("").str.strip().eq("")
    if ok_without_text.any():
        errors.append(f"{int(ok_without_text.sum())} ok rows have empty response_text")

    missing_prompt_keys = df[["prompt_id", "model_id"]].isna().any(axis=1)
    if missing_prompt_keys.any():
        errors.append(f"{int(missing_prompt_keys.sum())} rows lack prompt_id or model_id")

    prompt_versions = df.groupby("prompt_id", dropna=False)["prompt_text"].nunique(dropna=False)
    changed_prompts = prompt_versions[prompt_versions > 1]
    if not changed_prompts.empty:
        errors.append(
            "prompt_id maps to multiple prompt texts; version the registry first: "
            + ", ".join(map(str, changed_prompts.index[:5]))
        )

    model_metadata = (
        df.groupby("model_id", dropna=False)[["family", "generation", "provider_model_id"]]
        .nunique(dropna=False)
        .max(axis=1)
    )
    unstable_models = model_metadata[model_metadata > 1]
    if not unstable_models.empty:
        errors.append(
            "model_id maps to inconsistent metadata: "
            + ", ".join(map(str, unstable_models.index[:5]))
        )

    return errors
