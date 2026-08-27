# Prompt registry

`pilot_prompts.csv` contains 20 balanced prompts for feasibility testing only. It is not the frozen main prompt bank.

Every prompt revision increments `version`; never silently change the text under an existing `(prompt_id, version)` pair. The final registry will contain exactly 100 prompts—20 per task type—with a documented review for length, refusals, topic sensitivity, topic duplication, and accidental formatting constraints.
