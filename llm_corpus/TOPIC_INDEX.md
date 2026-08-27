# Topic Index

Auto-generated from `##` headings in `lectures/`. Use for retrieval routing.

## Session 01: Introduction, IPython and Jupyter

File: `llm_corpus/lectures/01_ipython_jupyter.md`

- Session 1: Introduction, IPython and Jupyter
- Table of Contents
- What is Data Science?
- Why is Data Science Relevant for Linguistics?
- IPython: Setup
- IPython: Improved Features
- IPython: Magic Commands
- Jupyter
- Jupyter: Setup
- Jupyter Notebooks: Basic Usage
- Jupyter Notebooks: Further Useful Features
- Course Organization
- Possibilities for Projects
- Assignment 1
- Course Plan
- Questions

## Session 02: NumPy and Seaborn

File: `llm_corpus/lectures/02_numpy_seaborn.md`

- Session 2: Introduction to NumPy and Seaborn
- Table of Contents
- NumPy: Purpose and Basic Usage
- NumPy Arrays: Creation
- NumPy Arrays: Data Types
- NumPy Arrays: Vectorisation and Broadcasting
- NumPy Arrays: Indexing and Slicing
- NumPy Arrays: Boolean Indexing and Filtering
- NumPy Arrays: Sorting and Searching
- Vectorisation and Universal Functions
- Array-Oriented Programming
- Pseudorandom Numbers with np.random
- Linear Algebra
- Matplotlib and the Role of Seaborn
- Seaborn: Installation Basic Usage
- Matplotlib: Histogram Example
- Seaborn: Smooth Density Estimates
- Seaborn: Two-Dimensional Smoothed Joint Density
- Categorical Plots: Factor Plot
- Categorical Plots: Joint Distributions
- Categorical Plots: Bar Plots
- Categorical Plots: Swarm and Violin Plots
- Categorical Plots: Scatter Plots
- Course Plan
- Questions

## Session 03: Pandas and Data Handling

File: `llm_corpus/lectures/03_pandas_data_handling.md`

- Session 3: Pandas and Data Handling
- Table of Contents
- Pandas: Purpose and Usage
- Pandas: Fundamental Data Structures
- pd.Series as an Indexed Sequence
- pd.Series as a Specialized Dictionary
- Constructing pd.Series Objects
- pd.DataFrame as Generalized NumPy Array
- pd.DataFrame as Generalised Array and Specialised Dictionary
- Constructing pd.DataFrame Objects
- pd.Index as Immutable Array
- pd.Index as Ordered Set
- Data Selection in Series as Dictionary
- Data Selection in Series as One-Dimensional Array
- Data Selection in Data Frame as Dictionary
- Data Selection in Data Frame as Two-Dimensional Array
- Data Loading and Storage
- Data Exploration and Summary Statistics
- Sorting and Ranking
- Data Cleaning and Preparation
- NaN and None in Pandas
- Pandas Nullable Dtypes
- Detecting Null Values
- Dropping Null Values with dropna()
- Filling Null Values with fillna()
- Removing Duplicates
- Replacing Values
- Renaming Axis Indexes
- Detecting and Filtering Outliers
- Discretisation and Binning
- Permutation and Random Sampling
- Vectorised String Operations: Equivalents of Basic Methods
- Vectorised String Operations: Regular Expressions
- Vectorised String Operations: Miscellaneous Methods
- Categorical Data: Background and Motivation
- Categorical Extension Type
- Course Plan
- Questions

## Session 04: Linguistic Preprocessing

File: `llm_corpus/lectures/04_linguistic_preprocessing.md`

- Session 4: Linguistic Preprocessing
- Table of Contents
- Linguistic Preprocessing
- Removing Stop Words
- SpaCy
- SpaCy: General Design
- Installing and Running a SpaCy model from Jupyter
- SpaCy: Self-Guided Tutorial
- Natural Language Toolkit (NLTK)
- NLTK: General Design
- SpaCy vs. NLTK: Comparison
- Keyword Extraction
- Tuple Extraction
- Collocation Extraction
- Course Plan
- Questions

## Session 05: Data Wrangling

File: `llm_corpus/lectures/05_data_wrangling.md`

- Session 5: Data Wrangling – Join, Combine, Reshape
- Table of Contents
- Data Wrangling: Overview
- Hierarchical Indexing: Basic Example
- Hierarchical Indexing: Both Axes
- Hierarchical Indexing: Naming Levels
- Hierarchical Indexing: Partial Indexing
- Hierarchical Indexing: Cross-Sectioning
- Hierarchical Indexing: unstack and stack
- Hierarchical Indexing: Reordering and Sorting Levels
- Hierarchical Indexing: Indexing with a DataFrame’s columns
- Combining Datasets: Overview
- Combining Datasets: Concatenation
- Combining Datasets: Further Options of pd.concat
- Combining Datasets: a.combine_first(b)
- Merging Datasets: Database-Style DataFrame Joins
- Merging Datasets: Functionality of pd.merge
- Merging Datasets: Merging on Index
- Reshaping and Pivoting: Overview
- Long Format
- Pivoting from Long to Wide Format
- pd.pivot_table: Further Examples
- Pivoting from Wide to Long Format
- Course Plan
- Questions

## Session 06: Data Aggregation and Grouping

File: `llm_corpus/lectures/06_data_aggregation_and_grouping.md`

- Session 6: Data Aggregation and Grouping
- Table of Contents
- Data Aggregation and Grouping: Overview
- Group Operations: Motivation
- Group Operations: Illustration
- Group Operations: Splitting into Groups
- Group Operations: Iterating over Groups
- Group Operations: Selection by Columns
- Grouping with Dictionaries and Series
- Grouping with Functions
- Grouping by Index Levels
- Data Aggregation: Optimised GroupBy Methods
- Data Aggregation: Custom Functions
- Data Aggregation: Column-Wise and Multiple Function Application
- Apply: Basic Split-Apply-Combine Pattern
- Example: Quantile and Bucket Analysis (McKinney 2022, p. 338f)
- Example: Group Weighted Average and Correlation (McKinney 2022, p. 344f)
- Pivot Tables
- Pivot Tables: Example from McKinney (2022), p. 352f
- Pivot Tables: Options
- Cross-Tabulation
- Cross-Tabulation: Example from McKinney (2022), p. 354f
- Course Plan

## Session 07: Modeling and Prediction

File: `llm_corpus/lectures/07_modeling_and_prediction.md`

- Session 7: Modelling and Prediction
- Table of Contents
- Recap: Statistics and Probability
- Statistical Modelling
- From Pandas to Modelling
- Patsy Library
- Patsy: Introductory Example from McKinney (2022)
- Patsy: Categorical Data Example
- Patsy: Interaction Term Example
- The statsmodels library
- Frequentist Statistics: Overview (University of Dundee)
- Frequentist Statistics: Overview (Brian Y uen, University of Southampton)
- The statsmodels library: Basic Usage
- statsmodels Example: Running a Statistical Test
- statsmodels Example: OLS Linear Regression
- statsmodels Example: Interpreting the Results
- statsmodels Example: Basic Criteria of Regression Model Quality
- statsmodels Example: Using the Model for Prediction
- The scikit-learn library
- scikit-learn: Algorithm Cheat Sheet
- scikit-learn: Basic Usage
- Logistic Regression
- scikit-learn: Cross-Validation
- Sources
- Course Plan
- Questions

## Session 08: Classification

File: `llm_corpus/lectures/08_classification.md`

- Session 8: Classiﬁcation
- Table of Contents
- Classiﬁcation Problems: General Setup
- Role of Classiﬁcation in Data Science
- Classiﬁcation Algorithms: Landscape
- Classiﬁcation Algorithms: Comparison
- k-Nearest Neighbours: Motivation
- k-Nearest Neighbours in scikit-learn
- k-Nearest Neighbours: Inﬂuence of Prediction Weights
- k-Nearest Neighbours: Strengths and Weaknesses
- Naive Bayes: Motivation
- Naive Bayes: Variants
- Gaussian Naive Bayes: Illustration of a Trained Two-Label Classiﬁer
- Gaussian Naive Bayes: Visualisation of Predictions on Random Data
- Gaussian Naive Bayes in scikit-learn: VanderPlas (2023)
- Multinomial Naive Bayes: Application to Text Classiﬁcation
- Multinomial Naive Bayes: Text Classiﬁcation Example by VanderPlas (2023)
- Naive Bayes: Strengths and Weaknesses
- Decision Trees: Motivation
- Decision Trees: Illustration of Decision Boundaries
- Decision Trees: Strengths and Weaknesses
- Random Forests
- Random Forests: Illustration of Decision Boundaries
- Decision Trees in Scikit-Learn: Code Examples from VanderPlas (2023)
- Linear Discriminative Classiﬁers
- Support Vector Machines: Intuition
- Support Vector Machines: Illustration
- Support Vector Machines: Softening the Margin
- Beyond Linear Boundaries
- Kernel SVMs
- Support Vector Machines: Strengths and Weaknesses
- Support Vector Machines in Scikit-Learn: Code Examples
- Sources
- Course Plan
- Questions

## Session 09: Clustering

File: `llm_corpus/lectures/09_clustering.md`

- Session 9: Clustering
- Table of Contents
- Clustering Problems: General Setup
- Role of Clustering in Data Science
- Clustering Algorithms: Landscape
- Clustering Algorithms: General Overview
- Clustering Algorithms: Comparison
- Agglomerative Clustering
- Agglomerative Clustering: Illustration
- Comparison of Hierarchical Linkage Methods
- Agglomerative Clustering: Strengths and Weaknesses
- Agglomerative Clustering in Scikit-Learn
- k-Means Clustering
- k-Means Clustering: Illustration by VanderPlas (2023)
- k-Means Clustering: Strengths and Weaknesses
- k-Means Clustering: Poor Convergence (VanderPlas 2023)
- k-Means Clustering in Scikit-Learn
- k-Means Clustering: Poor Choice of k (VanderPlas 2023)
- Silhouette Scores as a Criterion for Choosing k
- Gaussian Mixture Models (GMM)
- Gaussian Mixture Models (GMM): Illustration
- Gaussian Mixture Models: Strengths and Weaknesses
- Gaussian Mixture Models in Scikit-Learn
- Density-Based Clustering: DBSCAN
- DBSCAN: Illustration
- DBSCAN: Strengths and Weaknesses
- DBSCAN in Scikit-Learn
- Sources
- Course Plan
- Questions

## Session 10: Pattern Extraction and Density Estimation

File: `llm_corpus/lectures/10_pattern_extraction.md`

- Session 10: Pattern Extraction and Density Estimation
- Table of Contents
- Pattern Extraction: Deﬁnition and Approaches
- Dimensionality Reduction: Deﬁnition and Role in Data Science
- Dimensionality Reduction: Overview of Approaches
- Principal Component Analysis: General Idea and Mathematical Background
- Principal Component Analysis: Illustration (First Two Components)
- Principal Component Analysis: Further Uses and Limitations
- Principle Component Analysis in Scikit-Learn
- Dimensionality Reduction: Advanced Techniques
- Manifold Learning: General Idea
- Manifold Learning: Some (Semi-)Mathematical Background
- Manifold Learning: Main Techniques
- Manifold Learning: Successful Multidimensional Scaling
- Manifold Learning: Failed Multidimensional Scaling
- Manifold Learning: Comparison of MDS and LLE on Toy Example
- Manifold Learning: Isomap on “Swiss Roll” Example Dataset
- Manifold Learning: Challenges
- Density Estimation Problems: General Setup
- Role of Density Estimation in Data Science
- Kernel Density Estimation: General Idea
- Kernel Density Estimation: Gaussian Kernel
- Kernel Density Estimation: Some Mathematical Background
- Kernel Density Estimation: Practical Considerations
- Kernel Density Estimation in Scikit-Learn
- Main Sources
- Course Plan
- Questions

## Session 11: Statistical Inference

File: `llm_corpus/lectures/11_statistical_inference.md`

- Session 11: Statistical Inference
- Table of Contents
- Testable Hypotheses
- Classical Statistical Tests
- Signiﬁcance Testing
- Multiple Tests
- Resampling Methods
- Resampling Methods: The Bootstrap
- Resampling Methods: Bootstrap Example
- Statistical Modeling and Inference
- Bayesian Statistics
- Bayesian Inference: Example from McElreath (2020, p. 347ff)
- Model Selection
- Main Sources
- Course Plan
- Questions

## Session 12: Data Science Projects

File: `llm_corpus/lectures/12_data_science_projects.md`

- Session 12: Data Science Projects
- Table of Contents
- What is a Research Project?
- Stages of a Research Project
- Stage 1: Research Question
- Stage 2: Preliminary Research
- Stage 3: Formulating Hypotheses
- Stage 4: Research Design
- Stage 5: Data Collection
- Stage 6: Data Analysis and Interpretation
- Stage 7: Drawing Conclusions and Reporting Findings
- Important Issues for Science Projects
- Project Organisation
- Project Ideas: Overview
- Project Ideas: Variation, Evolution and Change
- Project Ideas: Language and Cognition
- Project Ideas: Language Use
- Final Assignment: Project Proposal
- Project Proposal: Structure
- Additional Reading
- Course Plan
- Questions
