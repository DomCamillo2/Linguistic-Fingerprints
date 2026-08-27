import pandas as pd

from linguistic_fingerprints.schema import REQUIRED_GENERATION_COLUMNS, validate_generations


def valid_row():
    row = {column: "value" for column in REQUIRED_GENERATION_COLUMNS}
    row.update(
        {
            "run_id": "run_001",
            "prompt_id": "EXP_001",
            "model_id": "family_a_earlier",
            "family": "family_a",
            "generation": "earlier",
            "provider_model_id": "provider/model-a",
            "status": "ok",
            "response_text": "A valid response.",
        }
    )
    return row


def test_valid_generation_table_has_no_errors():
    assert validate_generations(pd.DataFrame([valid_row()])) == []


def test_duplicate_run_ids_are_rejected():
    row = valid_row()
    errors = validate_generations(pd.DataFrame([row, row]))
    assert any("not unique" in error for error in errors)


def test_prompt_text_changes_are_rejected():
    first = valid_row()
    second = valid_row() | {"run_id": "run_002", "prompt_text": "changed"}
    errors = validate_generations(pd.DataFrame([first, second]))
    assert any("multiple prompt texts" in error for error in errors)
