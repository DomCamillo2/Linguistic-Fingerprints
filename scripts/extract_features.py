#!/usr/bin/env python3
"""Validate a generation CSV and extract one linguistic feature row per ok run."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import spacy

from linguistic_fingerprints.features import extract_text_features
from linguistic_fingerprints.schema import validate_generations


IDENTIFIER_COLUMNS = [
    "run_id",
    "prompt_id",
    "model_id",
    "family",
    "generation",
    "task_type",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--spacy-model", default="en_core_web_sm")
    parser.add_argument("--mattr-window", type=int, default=50)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    frame = pd.read_csv(args.input)
    errors = validate_generations(frame)
    if errors:
        raise SystemExit("Generation-table validation failed:\n- " + "\n- ".join(errors))

    ok = frame.loc[frame["status"].eq("ok")].copy()
    nlp = spacy.load(args.spacy_model)
    docs = nlp.pipe(ok["response_text"].astype(str), batch_size=64)

    rows: list[dict] = []
    for (_, record), doc in zip(ok.iterrows(), docs):
        row = {column: record[column] for column in IDENTIFIER_COLUMNS}
        row.update(extract_text_features(doc, str(record["response_text"]), args.mattr_window))
        rows.append(row)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(args.output, index=False)
    print(f"wrote {len(rows)} feature rows to {args.output}")


if __name__ == "__main__":
    main()
