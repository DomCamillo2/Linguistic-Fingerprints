#!/usr/bin/env python3
"""Fast, dependency-light checks for the repository contract."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    "AGENTS.md",
    "llms.txt",
    "PROJECT_PLAN.md",
    "proposal/PROPOSAL_DRAFT.md",
    "config/study.yaml",
    "config/models.example.yaml",
    "prompts/pilot_prompts.csv",
    "data/README.md",
    "reports/PREP_STATUS.md",
    "reports/CHANGELOG_RUNS.md",
    "reports/MISTAKES.md",
    "llm_corpus/INDEX.md",
]


def main() -> None:
    errors: list[str] = []
    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    lecture_files = sorted((ROOT / "llm_corpus" / "lectures").glob("*.md"))
    if len(lecture_files) != 12:
        errors.append(f"expected 12 lecture extracts, found {len(lecture_files)}")

    prompt_path = ROOT / "prompts" / "pilot_prompts.csv"
    if prompt_path.is_file():
        with prompt_path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        prompt_ids = [row["prompt_id"] for row in rows]
        if len(rows) != 20:
            errors.append(f"expected 20 pilot prompts, found {len(rows)}")
        if len(prompt_ids) != len(set(prompt_ids)):
            errors.append("pilot prompt_id values are not unique")
        task_counts: dict[str, int] = {}
        for row in rows:
            task_counts[row["task_type"]] = task_counts.get(row["task_type"], 0) + 1
        if len(set(task_counts.values())) != 1:
            errors.append(f"pilot task types are not balanced: {task_counts}")

    if errors:
        raise SystemExit("Project check failed:\n- " + "\n- ".join(errors))
    print("Project check passed: structure, lecture corpus, and pilot registry are consistent.")


if __name__ == "__main__":
    main()
