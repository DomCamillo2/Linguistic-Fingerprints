# Prompt registry

`pilot_prompts.csv` contains 20 balanced prompts for feasibility testing only. It is not the frozen main prompt bank.

Every prompt revision increments `version`; never silently change the text under an existing `(prompt_id, version)` pair. The final registry should contain 100–120 prompts with balanced task types and a documented review for length, refusals, topic sensitivity, and accidental formatting constraints.
