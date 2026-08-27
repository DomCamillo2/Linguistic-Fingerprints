# Course Map — Data Science for Linguists (SoSe 2026)

Structured reference for LLMs and humans. Full slide content lives under `lectures/`.

> Public-project note: paths describing original PDFs, assignment datasets, raw extraction dumps, or official solutions refer to the complete local course workspace. Those files are intentionally not published in this repository.

## Meta

| Field | Value |
|-------|-------|
| Course | Data Science for Linguists |
| Term | Summer 2026 |
| Instructor | Johannes Dellert |
| Department | Seminar für Sprachwissenschaft, Philosophische Fakultät |
| Prerequisites | Methods I (Programming) or Session 0 elementary Python; Methods II (Statistics, can be parallel); Linguistic Fundamentals |
| Deliverables | ~10 Moodle assignments (notebook → PDF); optional graded Schein via final project; final **project proposal** due **31 August 2026** (not part of 3 CP coursework) |

## Schedule

| # | Date | Topic | Corpus file |
|---|------|-------|-------------|
| 0 | 16/04 | Elementary Python | *(not in workspace)* |
| 1 | 23/04 | Course Overview, IPython and Jupyter | `lectures/01_ipython_jupyter.md` |
| 2 | 30/04 | NumPy and Seaborn | `lectures/02_numpy_seaborn.md` |
| 3 | 07/05 | Pandas and Data Handling | `lectures/03_pandas_data_handling.md` |
| — | 14/05 | Ascension (no class) | |
| 4 | 21/05 | Linguistic Preprocessing | `lectures/04_linguistic_preprocessing.md` |
| — | 28/05–04/06 | Pentecost / Corpus Christi | |
| 5 | 11/06 | Data Wrangling: Join, Combine, Reshape | `lectures/05_data_wrangling.md` |
| 6 | 18/06 | Data Aggregation and Grouping | `lectures/06_data_aggregation_and_grouping.md` |
| 7 | 25/06 | Modelling and Prediction | `lectures/07_modeling_and_prediction.md` |
| 8 | 02/07 | Classification | `lectures/08_classification.md` |
| 9 | 09/07 | Clustering | `lectures/09_clustering.md` |
| 10 | 16/07 | Pattern Extraction and Density Estimation | `lectures/10_pattern_extraction.md` |
| 11 | 23/07 | Statistical Inference | `lectures/11_statistical_inference.md` |
| 12 | 30/07 | Data Science Projects | `lectures/12_data_science_projects.md` |

Assignments 1–3: two weeks each. From Assignment 4: weekly rhythm.

## Learning goals by session

### 01 — IPython & Jupyter
Describe data-scientist tasks; course map; IPython vs vanilla Python; Jupyter workflow; small analyses; assignment expectations.

### 02 — NumPy & Seaborn
Why numeric arrays; create/slice/reshape/join/split; ufuncs vs loops; aggregation; broadcasting & masks; fancy indexing; sorting; Seaborn plots.

### 03 — Pandas
DataFrame / Series / Index; select & filter; sort & rank; summary stats; I/O; missing data; duplicates; replace; outliers; sampling; categoricals.

### 04 — Linguistic preprocessing
SpaCy vs NLTK; tokenisation; lemmatisation; morphology; dependency parsing; keywords / tuples / collocations; low-resource caveats.

### 05 — Wrangling
Hierarchical indexing; join/merge/concat; stack/unstack; long ↔ wide pivot.

### 06 — Aggregation
Split-apply-combine; GroupBy options; multi-function agg; pivot tables; cross-tabulation.

### 07 — Modeling & prediction
Role of models; linear / polynomial / logistic regression; Patsy formulas; statsmodels; scikit-learn basics; cross-validation.

### 08 — Classification
When to classify; Naive Bayes; SVM; decision trees & random forests; kNN landscape.

### 09 — Clustering
Structure over unlabeled points; k-means; GMM; choosing *k*; unsupervised learning framing; DBSCAN / agglomerative.

### 10 — Pattern extraction
Networks framing; PCA; manifold learning (MDS, LLE, Isomap); kernel density estimation.

### 11 — Statistical inference
Pitfalls of testing; multiple testing; parameter estimation vs classical tests; model selection; resampling / bootstrap; Bayesian sketch.

### 12 — Projects
Research stages; project plan; data access & ethics; sharing results; reproducibility; example project ideas by linguistics track.

## Conceptual pipeline (course arc)

```
question → data acquisition → clean/wrangle (Pandas)
        → linguistic annotate (SpaCy/NLTK) if text
        → explore / aggregate / visualise
        → model / classify / cluster / reduce / infer
        → report reproducibly (notebook + requirements + README)
```

## Tool stack (as taught)

| Layer | Libraries |
|-------|-----------|
| Interactive | IPython, Jupyter |
| Arrays / viz | NumPy, Matplotlib, Seaborn |
| Tabular | Pandas |
| NLP | SpaCy (`en_core_web_sm` etc.), NLTK |
| Formulas / classical stats | Patsy, statsmodels |
| ML | scikit-learn |

## Final project proposal (Session 12)

**Deadline:** 31 August (proposal). One feedback round; major revisions need re-approval. Graded courses: grade reflects final result **and** adherence to (or justified deviation from) the proposal.

### Required proposal sections
1. Title + contributors
2. Introduction / research question + context
3. Clear objective (question to answer or result to replicate)
4. Preliminary literature review (methods + datasets)
5. Scope in/out + reasons (data, time)
6. Methodology (acquisition + analysis techniques)
7. Week-by-week contributor plan
8. Expected outcomes (including failed replication / null results)

### Research stages (idealised)
1. Research question → 2. Preliminary research → 3. Hypotheses → 4. Design → 5. Data collection → 6. Analysis & interpretation → 7. Conclusions & reporting

### Reproducibility checklist (from slides)
- Archive unmodified original data
- Document all transformations
- Fix random seeds
- README with re-run steps
- `requirements` with package versions

### Example project themes by Schein track
- **Language & Cognition:** predict judgments from features; join psycholinguistic datasets and test links
- **Variation, Evolution & Change:** parallel-corpus strategies; lexicostatistical family hypotheses
- **Language Use:** corpus-driven grammar hypotheses; author/group usage differences

Concrete idea sketches (definitions basicness, cross-lingual collocations, etc.) are in `lectures/12_data_science_projects.md`.

## Workspace status (non-corpus)

| Path | Status |
|------|--------|
| `Vorlesungenslides/*.pdf` | Lecture slides |
| `assignment_01` … `assignment_08` | Sheets + data (+ solutions for 01/07/08) |
| `ASSIGNMENTS.md` | Mapping of files ↔ assignments |
| `homework_scripts/` | Empty |
| `.venv`, `.venv-1` | Local Python envs (ignore for content) |

## Suggested LLM prompts for this corpus

- “Explain hierarchical indexing like Session 5 and show a minimal Pandas example.”
- “Compare SpaCy vs NLTK for lemmatisation using Session 4 criteria.”
- “Draft a project proposal outline for [topic] following Session 12 structure.”
- “Which lecture covers silhouette scores for choosing *k*?” → Session 09
- “Summarise pitfalls of multiple testing from Session 11.”
