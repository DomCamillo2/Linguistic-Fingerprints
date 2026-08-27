import numpy as np
import pandas as pd

from linguistic_fingerprints.generalization import (
    cross_family_transfer,
    cross_family_unseen_prompt,
    leave_one_task_type_out,
    prompt_blocked_within_family,
    validate_analysis_frame,
)


FEATURES = ["feature_a", "feature_b"]


def synthetic_frame() -> pd.DataFrame:
    rows = []
    genres = ["advice", "argumentation", "explanation", "narrative", "reflection"]
    for prompt_index in range(25):
        genre = genres[prompt_index % len(genres)]
        for family_index, family in enumerate(["gemma", "llama"]):
            for generation_index, generation in enumerate(["earlier", "later"]):
                direction = -1 if generation == "earlier" else 1
                rows.append(
                    {
                        "prompt_id": f"P{prompt_index:03d}",
                        "family": family,
                        "generation": generation,
                        "task_type": genre,
                        "feature_a": direction * (2.0 + family_index * 0.1),
                        "feature_b": direction + prompt_index * 0.001,
                    }
                )
    return pd.DataFrame(rows)


def test_analysis_contract_accepts_balanced_frame():
    assert validate_analysis_frame(synthetic_frame(), FEATURES) == []


def test_leave_one_task_type_out_reports_every_family_and_genre():
    result = leave_one_task_type_out(synthetic_frame(), FEATURES)
    assert len(result) == 20
    assert set(result["held_out_task_type"]) == set(synthetic_frame()["task_type"])
    logistic = result.loc[result["estimator"].eq("logistic_l2")]
    assert np.allclose(logistic["balanced_accuracy"], 1.0)


def test_cross_family_transfer_runs_in_both_directions():
    result = cross_family_transfer(synthetic_frame(), FEATURES)
    logistic = result.loc[result["estimator"].eq("logistic_l2")]
    assert set(zip(logistic["train_family"], logistic["test_family"])) == {
        ("gemma", "llama"),
        ("llama", "gemma"),
    }
    assert np.allclose(logistic["balanced_accuracy"], 1.0)


def test_cross_family_unseen_prompt_has_disjoint_prompt_roles():
    result = cross_family_unseen_prompt(synthetic_frame(), FEATURES, n_splits=5)
    assert len(result) == 20
    assert set(result["fold"]) == {1, 2, 3, 4, 5}
    logistic = result.loc[result["estimator"].eq("logistic_l2")]
    assert np.allclose(logistic["balanced_accuracy"], 1.0)


def test_prompt_blocked_baseline_reports_models_and_folds():
    result = prompt_blocked_within_family(synthetic_frame(), FEATURES, n_splits=5)
    assert len(result) == 20
    assert set(result["estimator"]) == {"logistic_l2", "dummy_stratified"}
    logistic = result.loc[result["estimator"].eq("logistic_l2")]
    assert np.allclose(logistic["balanced_accuracy"], 1.0)
