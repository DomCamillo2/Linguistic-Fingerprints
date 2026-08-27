#!/usr/bin/env python3
"""Run the preregistered cross-genre and cross-family evaluations."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from linguistic_fingerprints.features import CONFIRMATORY_FEATURES
from linguistic_fingerprints.generalization import (
    cross_family_transfer,
    cross_family_unseen_prompt,
    leave_one_task_type_out,
    prompt_blocked_within_family,
    validate_analysis_frame,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--folds", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    frame = pd.read_csv(args.input)
    features = list(CONFIRMATORY_FEATURES)
    errors = validate_analysis_frame(frame, features)
    if errors:
        raise SystemExit("Analysis-table validation failed:\n- " + "\n- ".join(errors))

    variants = {
        "confirmatory_features": features,
        "confirmatory_plus_length": [*features, "n_words"],
    }
    outputs: list[pd.DataFrame] = []
    for variant_name, variant_features in variants.items():
        variant_errors = validate_analysis_frame(frame, variant_features)
        if variant_errors:
            raise SystemExit(
                f"Analysis-table validation failed for {variant_name}:\n- "
                + "\n- ".join(variant_errors)
            )
        variant_results = pd.concat(
            [
                leave_one_task_type_out(frame, variant_features, seed=args.seed),
                cross_family_transfer(frame, variant_features, seed=args.seed),
                cross_family_unseen_prompt(
                    frame, variant_features, n_splits=args.folds, seed=args.seed
                ),
                prompt_blocked_within_family(
                    frame, variant_features, n_splits=args.folds, seed=args.seed
                ),
            ],
            ignore_index=True,
        )
        variant_results.insert(1, "analysis_variant", variant_name)
        outputs.append(variant_results)

    results = pd.concat(outputs, ignore_index=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(args.output, index=False)
    print(f"wrote {len(results)} generalization results to {args.output}")


if __name__ == "__main__":
    main()
