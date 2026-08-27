# Data Science for Linguists — LLM Corpus Index

**Course:** Data Science for Linguists (Summer 2026)
**Instructor:** Johannes Dellert · Seminar für Sprachwissenschaft, Universität Tübingen
**Purpose:** Machine-readable full-text extracts of every lecture slide and assignment sheet so an LLM can answer questions without parsing PDFs.

## How an LLM should use this corpus

1. Start here, or `COURSE_MAP.md` / `TOPIC_INDEX.md`, for orientation.
2. Open **only** the relevant `lectures/NN_*.md` or `assignments/exNN.md` file(s).
3. Official solutions are not included in this public repository.
4. Raw page dumps are generated locally by rebuild scripts (not in git). Prefer these cleaned markdown files.
5. Cite YAML `source_pdf` and `<!-- page:N -->` markers when grounding answers.
6. Assignment data lives in `assignment_NN/` (see `ASSIGNMENTS.md (workspace) / course assignment folders`).

## Directory layout

```
llm_corpus/
  INDEX.md              ← this file
  COURSE_MAP.md         ← syllabus, goals, project rules
  TOPIC_INDEX.md        ← heading index over lectures
  manifest.json         ← machine index of lecture extracts
  lectures/             ← sessions 01–12 (full slide text)
  assignments/          ← ex01–ex08 sheets
  # original PDFs, raw extraction dumps, datasets, and solutions are local-only
```

The source workspace contains rebuild scripts and original PDFs. They are not published here.

## Lecture map (full page coverage)

| ID | File | Topic | Pages |
|----|------|-------|------:|
| 01 | [lectures/01_ipython_jupyter.md](lectures/01_ipython_jupyter.md) | Intro, IPython, Jupyter | 34 |
| 02 | [lectures/02_numpy_seaborn.md](lectures/02_numpy_seaborn.md) | NumPy & Seaborn | 27 |
| 03 | [lectures/03_pandas_data_handling.md](lectures/03_pandas_data_handling.md) | Pandas | 40 |
| 04 | [lectures/04_linguistic_preprocessing.md](lectures/04_linguistic_preprocessing.md) | SpaCy / NLTK | 20 |
| 05 | [lectures/05_data_wrangling.md](lectures/05_data_wrangling.md) | Join / reshape | 30 |
| 06 | [lectures/06_data_aggregation_and_grouping.md](lectures/06_data_aggregation_and_grouping.md) | GroupBy | 29 |
| 07 | [lectures/07_modeling_and_prediction.md](lectures/07_modeling_and_prediction.md) | Regression / prediction | 28 |
| 08 | [lectures/08_classification.md](lectures/08_classification.md) | Classification | 41 |
| 09 | [lectures/09_clustering.md](lectures/09_clustering.md) | Clustering | 34 |
| 10 | [lectures/10_pattern_extraction.md](lectures/10_pattern_extraction.md) | PCA / density | 31 |
| 11 | [lectures/11_statistical_inference.md](lectures/11_statistical_inference.md) | Inference | 19 |
| 12 | [lectures/12_data_science_projects.md](lectures/12_data_science_projects.md) | Research projects | 25 |

Source PDFs: `Vorlesungenslides/ (local PDFs; optional)` (optional; markdown is authoritative for LLM work).

## Assignments

| ID | Sheet | Folder | Solution MD |
|----|-------|--------|-------------|
| ex01 | [assignments/ex01.md](assignments/ex01.md) | local course workspace | not published |
| ex02 | [assignments/ex02.md](assignments/ex02.md) | local course workspace | — |
| ex03 | [assignments/ex03.md](assignments/ex03.md) | local course workspace | — |
| ex04 | [assignments/ex04.md](assignments/ex04.md) | local course workspace | — |
| ex05 | [assignments/ex05.md](assignments/ex05.md) | local course workspace | — |
| ex06 | [assignments/ex06.md](assignments/ex06.md) | local course workspace | — |
| ex07 | [assignments/ex07.md](assignments/ex07.md) | local course workspace | not published |
| ex08 | [assignments/ex08.md](assignments/ex08.md) | local course workspace | not published |

## Quick topic → file routing

| User asks about… | Open |
|------------------|------|
| Jupyter / IPython | `01` |
| NumPy / Seaborn | `02` |
| Pandas / missing data | `03` |
| SpaCy / NLTK / lemmas | `04` |
| merge / pivot / MultiIndex | `05` |
| groupby / crosstab | `06` |
| regression / Patsy / CV | `07` |
| NB / SVM / RF / kNN | `08` |
| k-means / GMM / DBSCAN | `09` |
| PCA / MDS / KDE | `10` |
| bootstrap / Bayes / tests | `11` |
| project proposal / tracks | `12` |

## Format convention

```yaml
---
id: "03"
title: "Pandas and Data Handling"
kind: "lecture"
source_pdf: "Vorlesungenslides/...."
pages: N
---
```

```html
<!-- page:12 source:datsci-03-pandas-data-handling.pdf -->
```

## Caveats

- PDF text extraction: spacing quirks, missing figures/plots, incomplete equations.
- Original PDFs, assignment datasets, raw extraction dumps, and official solutions remain local.
- Consult the local PDF only when visuals matter.
