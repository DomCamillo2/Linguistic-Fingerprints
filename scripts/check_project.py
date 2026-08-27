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
    "proposal/PROPOSAL_CHECKLIST.md",
    "config/study.yaml",
    "config/models.yaml",
    "literature/REFERENCES.md",
    "literature/references.bib",
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

    models_path = ROOT / "config" / "models.yaml"
    if models_path.is_file():
        models_text = models_path.read_text(encoding="utf-8")
        model_count = sum(line.startswith("  - model_id:") for line in models_text.splitlines())
        if model_count != 4:
            errors.append(f"expected 4 configured models, found {model_count}")
        if "TBD" in models_text:
            errors.append("config/models.yaml still contains TBD placeholders")

    proposal_path = ROOT / "proposal" / "PROPOSAL_DRAFT.md"
    if proposal_path.is_file() and "TBD" in proposal_path.read_text(encoding="utf-8"):
        errors.append("proposal draft still contains TBD placeholders")

    if errors:
        raise SystemExit("Project check failed:\n- " + "\n- ".join(errors))
    print("Project check passed: structure, lecture corpus, and pilot registry are consistent.")


if __name__ == "__main__":
    main()
