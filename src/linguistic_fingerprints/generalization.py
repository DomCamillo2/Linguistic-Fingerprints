"""Leakage-safe evaluations for genre and model-family generalization."""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


REQUIRED_ANALYSIS_COLUMNS = {
    "prompt_id",
    "family",
    "generation",
    "task_type",
}


def validate_analysis_frame(frame: pd.DataFrame, features: Sequence[str]) -> list[str]:
    """Return contract errors for an analysis-ready feature table."""

    errors: list[str] = []
    missing = sorted((REQUIRED_ANALYSIS_COLUMNS | set(features)) - set(frame.columns))
    if missing:
        return [f"missing required analysis columns: {', '.join(missing)}"]

    labels = set(frame["generation"].dropna())
    if labels != {"earlier", "later"}:
        errors.append(f"generation labels must be earlier/later, found {sorted(labels)}")
    if frame["family"].nunique(dropna=True) < 2:
        errors.append("cross-family evaluation requires at least two families")
    if frame["task_type"].nunique(dropna=True) < 2:
        errors.append("cross-genre evaluation requires at least two task types")
    if frame["prompt_id"].isna().any():
        errors.append("prompt_id contains missing values")

    feature_values = frame.loc[:, features].apply(pd.to_numeric, errors="coerce")
    entirely_missing = feature_values.columns[feature_values.isna().all()].tolist()
    if entirely_missing:
        errors.append(f"features contain no numeric values: {', '.join(entirely_missing)}")
    return errors


def build_classifier(C: float = 1.0, seed: int = 42) -> Pipeline:
    """Create the preregistered interpretable classification pipeline."""

    return Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(C=C, max_iter=2_000, random_state=seed),
            ),
        ]
    )


def build_dummy(seed: int = 42) -> Pipeline:
    """Create the preregistered stratified baseline with the same input contract."""

    return Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("classifier", DummyClassifier(strategy="stratified", random_state=seed)),
        ]
    )


def _estimators(estimator: Pipeline, seed: int) -> tuple[tuple[str, Pipeline], ...]:
    return (
        ("logistic_l2", estimator),
        ("dummy_stratified", build_dummy(seed)),
    )


def _xy(frame: pd.DataFrame, features: Sequence[str]) -> tuple[pd.DataFrame, pd.Series]:
    x = frame.loc[:, features].apply(pd.to_numeric, errors="coerce")
    y = frame["generation"].map({"earlier": 0, "later": 1}).astype(int)
    return x, y


def _score(model: Pipeline, test: pd.DataFrame, features: Sequence[str]) -> dict[str, float]:
    x_test, y_test = _xy(test, features)
    prediction = model.predict(x_test)
    probability = model.predict_proba(x_test)[:, 1]
    return {
        "balanced_accuracy": float(balanced_accuracy_score(y_test, prediction)),
        "macro_f1": float(f1_score(y_test, prediction, average="macro")),
        "roc_auc": float(roc_auc_score(y_test, probability)),
    }


def leave_one_task_type_out(
    frame: pd.DataFrame,
    features: Sequence[str],
    *,
    estimator: Pipeline | None = None,
    seed: int = 42,
) -> pd.DataFrame:
    """Train within a family on all but one task type and test on the held-out type."""

    estimator = estimator or build_classifier(seed=seed)
    rows: list[dict[str, object]] = []
    for family in sorted(frame["family"].unique()):
        family_frame = frame.loc[frame["family"].eq(family)]
        for held_out in sorted(family_frame["task_type"].unique()):
            train = family_frame.loc[~family_frame["task_type"].eq(held_out)]
            test = family_frame.loc[family_frame["task_type"].eq(held_out)]
            x_train, y_train = _xy(train, features)
            for estimator_name, estimator_template in _estimators(estimator, seed):
                model = clone(estimator_template)
                model.fit(x_train, y_train)
                rows.append(
                    {
                        "protocol": "leave_one_task_type_out",
                        "estimator": estimator_name,
                        "train_family": family,
                        "test_family": family,
                        "held_out_task_type": held_out,
                        "fold": np.nan,
                        "n_train": len(train),
                        "n_test": len(test),
                        **_score(model, test, features),
                    }
                )
    return pd.DataFrame(rows)


def cross_family_transfer(
    frame: pd.DataFrame,
    features: Sequence[str],
    *,
    estimator: Pipeline | None = None,
    seed: int = 42,
) -> pd.DataFrame:
    """Train on one complete family and test on every other complete family."""

    estimator = estimator or build_classifier(seed=seed)
    rows: list[dict[str, object]] = []
    families = sorted(frame["family"].unique())
    for train_family in families:
        for test_family in families:
            if train_family == test_family:
                continue
            train = frame.loc[frame["family"].eq(train_family)]
            test = frame.loc[frame["family"].eq(test_family)]
            x_train, y_train = _xy(train, features)
            for estimator_name, estimator_template in _estimators(estimator, seed):
                model = clone(estimator_template)
                model.fit(x_train, y_train)
                rows.append(
                    {
                        "protocol": "cross_family_transfer",
                        "estimator": estimator_name,
                        "train_family": train_family,
                        "test_family": test_family,
                        "held_out_task_type": None,
                        "fold": np.nan,
                        "n_train": len(train),
                        "n_test": len(test),
                        **_score(model, test, features),
                    }
                )
    return pd.DataFrame(rows)


def cross_family_unseen_prompt(
    frame: pd.DataFrame,
    features: Sequence[str],
    *,
    n_splits: int = 5,
    seed: int = 42,
    estimator: Pipeline | None = None,
) -> pd.DataFrame:
    """Transfer between families while also withholding the target prompt IDs."""

    estimator = estimator or build_classifier(seed=seed)
    rows: list[dict[str, object]] = []
    families = sorted(frame["family"].unique())
    for train_family in families:
        source = frame.loc[frame["family"].eq(train_family)].copy()
        x_source, y_source = _xy(source, features)
        splitter = StratifiedGroupKFold(n_splits=n_splits, shuffle=True, random_state=seed)
        for test_family in families:
            if train_family == test_family:
                continue
            target = frame.loc[frame["family"].eq(test_family)]
            for fold, (train_index, held_out_index) in enumerate(
                splitter.split(x_source, y_source, groups=source["prompt_id"]), start=1
            ):
                held_out_prompts = set(source.iloc[held_out_index]["prompt_id"])
                test = target.loc[target["prompt_id"].isin(held_out_prompts)]
                if test.empty:
                    raise ValueError(
                        f"no shared held-out prompts for {train_family} -> {test_family}, fold {fold}"
                    )
                for estimator_name, estimator_template in _estimators(estimator, seed):
                    model = clone(estimator_template)
                    model.fit(x_source.iloc[train_index], y_source.iloc[train_index])
                    rows.append(
                        {
                            "protocol": "cross_family_unseen_prompt",
                            "estimator": estimator_name,
                            "train_family": train_family,
                            "test_family": test_family,
                            "held_out_task_type": None,
                            "fold": fold,
                            "n_train": len(train_index),
                            "n_test": len(test),
                            **_score(model, test, features),
                        }
                    )
    return pd.DataFrame(rows)


def prompt_blocked_within_family(
    frame: pd.DataFrame,
    features: Sequence[str],
    *,
    n_splits: int = 5,
    seed: int = 42,
    estimator: Pipeline | None = None,
) -> pd.DataFrame:
    """Run the supporting within-family baseline on prompt-grouped folds."""

    estimator = estimator or build_classifier(seed=seed)
    rows: list[dict[str, object]] = []
    for family in sorted(frame["family"].unique()):
        family_frame = frame.loc[frame["family"].eq(family)].copy()
        x, y = _xy(family_frame, features)
        splitter = StratifiedGroupKFold(n_splits=n_splits, shuffle=True, random_state=seed)
        for fold, (train_index, test_index) in enumerate(
            splitter.split(x, y, groups=family_frame["prompt_id"]), start=1
        ):
            test = family_frame.iloc[test_index]
            for estimator_name, estimator_template in _estimators(estimator, seed):
                model = clone(estimator_template)
                model.fit(x.iloc[train_index], y.iloc[train_index])
                rows.append(
                    {
                        "protocol": "prompt_blocked_within_family",
                        "estimator": estimator_name,
                        "train_family": family,
                        "test_family": family,
                        "held_out_task_type": None,
                        "fold": fold,
                        "n_train": len(train_index),
                        "n_test": len(test_index),
                        **_score(model, test, features),
                    }
                )
    return pd.DataFrame(rows)
