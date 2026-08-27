---
id: "01"
title: "Introduction, IPython and Jupyter"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-01-ipython-jupyter.pdf"
pages: 34
date: "2026-04-23"
---

# Session 1: Introduction, IPython and Jupyter

> Full slide text extracted from `datsci-01-ipython-jupyter.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-01-ipython-jupyter.pdf -->

## Session 1: Introduction, IPython and Jupyter

Johannes Dellert
23 April, 2026

---

<!-- page:2 source:datsci-01-ipython-jupyter.pdf -->

## Table of Contents

What is Data Science?
Data Science and Linguistics
Course Overview
IPython
Jupyter
Course Organization
Assignment 1

---

<!-- page:3 source:datsci-01-ipython-jupyter.pdf -->

## What is Data Science?

- a data scientist is sometimes simply deﬁned as a person with workable coding skills,
a good background in statistics, and knowledge of a relevant domain
- these three areas map nicely to the prerequisites for this course:
- Methods I: Programming (alternatively, the elementary Python covered in Session 0)
- Methods II: Statistics (taking that course in parallel is ﬁne)
- Linguistic Fundamentals (domain knowledge)
- but this deﬁnition would also ﬁt a data analyst, who is typically described as
using the very same skills to answer questions asked by other people
- the crucial difference is that a scientist will ask their own questions
- this course could be described as getting you on track towards combining these three areas
of pre-existing knowledge in a productive way, allowing you to do data-based science:
- ask meaningful questions that can be answered based on empirical data
- develop strategies for data acquisition, preprocessing and reshaping
- code statistical analyses which can provide answers to your questions

---

<!-- page:4 source:datsci-01-ipython-jupyter.pdf -->

Table of Contents
What is Data Science?
Data Science and Linguistics
Course Overview
IPython
Jupyter
Course Organization
Assignment 1

---

<!-- page:5 source:datsci-01-ipython-jupyter.pdf -->

## Why is Data Science Relevant for Linguistics?

- many research questions asked in various branches of linguistics can only be answered
based on large amounts of data (instead of e.g. hand-curated sets of example cases)
- linguistic data comes in various shapes depending on the subdiscipline:
- audio and video recordings (the result of experiments or ﬁeldwork)
- eyetracking or other measurement data
- scanned grammars describing many languages
- digitalised dictionaries and lexical databases
- curated typological databases (grammatical features across languages)
- annotated corpora of various types (newspaper, literature, movie subtitles)
- large amounts of raw text data (typically scraped from the web)
- crowdsourced lexical and encyclopedic information (Wiktionary, Wikipedia)
- in modern science, there will be more relevant data than we could ever process manually
- exploratory data analysis is necessary to understand what is contained in a dataset
- statistical tests are necessary to decide whether there is a signal or only random noise
- modeling is necessary to understand the dynamics of complex systems (like language)

---

<!-- page:6 source:datsci-01-ipython-jupyter.pdf -->

Table of Contents
What is Data Science?
Data Science and Linguistics
Course Overview
IPython
Jupyter
Course Organization
Assignment 1

---

<!-- page:7 source:datsci-01-ipython-jupyter.pdf -->

Session 01: IPython and Jupyter
- Questions you will be able to answer after this session:
- How can we describe the tasks performed by a data scientist?
- What are the topics covered by this and other courses on data science?
- What are some of the advantages of IPython over vanilla Python?
- How do I set up a Jupyter notebook, and what is the basic workﬂow?
- How can I use Jupyter’s capabilities to efﬁciently perform a small data analyis?
- How are assignments structured in this course, and what are you expected to do?

---

<!-- page:8 source:datsci-01-ipython-jupyter.pdf -->

Session 02: Introduction to NumPy and Seaborn
- Questions you will be able to answer after this session:
- Why is it standard practice to convert large datasets into arrays of numbers?
- Why should I not use nested Python lists to represent numerical arrays?
- How do I set up and populate large arrays using NumPy?
- How can I slice, reshape, join and split NumPy arrays?
- Why are universal functions preferable to loops?
- How do I perform basic aggreggation tasks in NumPy?
- How do broadcasting and masks work?
- How can I use the options for fancy indexing in order to bin data?
- How do I sort arrays along rows and columns?
- How can I use the Seaborn library in order visualise aspects of my data,
creating a large variety of nice-looking graphs with very little code?

---

<!-- page:9 source:datsci-01-ipython-jupyter.pdf -->

Session 03: Pandas and Data Handling
- Questions you will be able to answer after this session:
- What is a data frame, and why is it so useful?
- What is the nature of Series and Index objects in Pandas?
- How do I select and ﬁlter in order to work with subsets of my data?
- What are my options for sorting and ranking data in my data frame?
- How do I compute basic summarising and descriptive statistics?
- How do I get data in various formats into my data frames?
- What are some basic strategies for handling missing data?
- How do I efﬁciently remove duplicates?
- What are the best options for replacing certain values?
- How do I detect and ﬁlter outliers?
- How do I efﬁciently create random samples?
- How can I work with categorical data?

---

<!-- page:10 source:datsci-01-ipython-jupyter.pdf -->

Session 04: Linguistic Preprocessing
- Questions you will be able to answer after this session:
- What are the most popular libraries for linguistic preprocessing?
- Why should I use existing tokenisers for some languages?
- Why is lemmatisation necessary for corpus-based research?
- What can I expect from a morphological analyser,
and why does it need to be combined with other tools in order to become fruitful?
- What are the beneﬁts of dependency parsing for corpus-based methods?
- How do I extract salient linguistic features from documents?
- What can I achieve on data from languages for which few resources exist?

---

<!-- page:11 source:datsci-01-ipython-jupyter.pdf -->

Session 05: Data Wrangling - Join, Combine, Reshape
- Questions you will be able to answer after this session:
- What is hierarchical indexing?
- How do I compute summary statistics by level?
- How can I merge together data frames using the join operation?
- What are the options for merging datasets, and how do I execute them?
- How do I reshape data using hierarchical indexing?
- How do I pivot data between long and wide formats?

---

<!-- page:12 source:datsci-01-ipython-jupyter.pdf -->

Session 06: Data Aggregation and Grouping
- Questions you will be able to answer after this session:
- What is the most productive way to think about group operations?
- Which options for grouping are supported best by Pandas?
- How do I perform column-wise and multiple function application?
- How does the split-apply-combine workﬂow operate?
- What are pivot tables, and what capabilities do they provide?
- What is cross-tabulation, and what are its main uses?

---

<!-- page:13 source:datsci-01-ipython-jupyter.pdf -->

Session 07: Modeling and Prediction
- Questions you will be able to answer after this session:
- What is the role of statistical models in data science?
- How does statistical modeling work in general?
- What are my options in case I want to predict unseen data?
- What was linear regression again, and why does it crop up everywhere?
- How can I catch non-linear patterns through polynomial regression?
- How can I use logistic regression to predict categorical variables?

---

<!-- page:14 source:datsci-01-ipython-jupyter.pdf -->

Session 08: Classiﬁcation
- Questions you will be able to answer after this session:
- When and why do I want to use classiﬁcation as part of my data processing workﬂow?
- In which contexts is Naive Bayes classiﬁcation likely to work?
- Why did Support Vector Machines (SVM) become the main workhorse for classiﬁcation,
and why are they still popular in the age of deep learning?
- Which package for decision trees and random forests provide the best compromise
between ﬂexibility and ease of use?

---

<!-- page:15 source:datsci-01-ipython-jupyter.pdf -->

Session 09: Clustering
- Questions you will be able to answer after this session:
- How can clustering help me to infer some structure over a large number of datapoints?
- Why is k-means clustering a mainstay of machine learning textbooks?
- What are Gaussian Mixture Models, and what is their key advantage?
- Why is the decision on the number of clusters to infer such a tricky issue?
- Why is clustering a central topic of unsupervised learning,
and what else can we do in the absence of labeled data?

---

<!-- page:16 source:datsci-01-ipython-jupyter.pdf -->

Session 10: Pattern Extraction and Density Estimation
- Questions you will be able to answer after this session:
- Which types of problems can be framed in terms of networks,
and what are major types of techniques in network analysis?
- How do we interpret a Principal Component Analysis (PCA),
and why is it such a popular tools for linear dimensionality reduction?
- What are the major approaches to manifold learning for non-linear dimensionality reduction?
- How does kernel density estimation work, and when do we want to use it?

---

<!-- page:17 source:datsci-01-ipython-jupyter.pdf -->

Session 11: Statistical Inference
- Questions you will be able to answer after this session:
- What are the major pitfalls of statistical testing, and how do we avoid them?
- Why does multiple testing increase the risk of false positives,
and what are the standard strategies for keeping this risk under control?
- What are the advantages of parameter estimation over classical hypothesis testing?
- How do we perform model selection, and how can we know how our model performs?
- What is the role of resampling methods in assessing how certain we can be of our results?

---

<!-- page:18 source:datsci-01-ipython-jupyter.pdf -->

Session 12: Data Science Projects
- Questions you will be able to answer after this session:
- What are the prototypical stages of a data-based research project?
- How do I set up a project plan for a data science project?
- What are potential issues in data access and data ethics that we should routinely consider?
- How do data scientists share their results with colleagues or the wider world?
- Which measures are important to implement in order to ensure reproducibility?
- What are typical topics of student projects in this course (from different areas of linguistics)?

---

<!-- page:19 source:datsci-01-ipython-jupyter.pdf -->

Table of Contents
What is Data Science?
Data Science and Linguistics
Course Overview
IPython
Jupyter
Course Organization
Assignment 1

---

<!-- page:20 source:datsci-01-ipython-jupyter.pdf -->

## IPython: Setup

- if you already have Python installed, installing IPython should be as easy as this:
$ pip3 install ipython
- otherwise, follow instructions on the webpage ( https://ipython.org/install.html)
- IPython should now be callable via terminal using an ipython command
(analogous to the python command of vanilla Python)

---

<!-- page:21 source:datsci-01-ipython-jupyter.pdf -->

## IPython: Improved Features

- advantages of IPython over vanilla Python:
- much better copying and pasting of formatted Python code
- more intelligent and readable output formatting
- very good command completion and other options for saving keyboard strokes
- for access to documentation, appending a question mark (?) to anything provides an
equivalent of the Python help function with improved functionality; try list.insert?
- a double question mark (??) provides a shortcut to the source code to view internals
(in case the function in question is implemented in Python)
- tab completion (like a good shell) complements Python’s dir function;
if you don’t know how a method was called, just hit T AB after typing your_object.
- tab completion is also very useful in order to save typing effort:
for most people, typing l.a<tab> is quicker than l.append
- many shortcuts for navigation, text entry, command history
- one neat example: _ for previous output extended to __, ___, etc.

---

<!-- page:22 source:datsci-01-ipython-jupyter.pdf -->

## IPython: Magic Commands

- IPython comes with a range of special magic commands preﬁxed by %:
- %run allows you to execute external script ﬁles as part of the code
- %pwd shows the current working directory
- %timeit measures and reports how long a statement takes to execute
- in many cases, doubling the percentage sign %% creates a cell magic which can operate on
multiple lines of input ( %%timeit is especially useful)
- %lsmagic gives you a list of magics to be explored using?

---

<!-- page:23 source:datsci-01-ipython-jupyter.pdf -->

Table of Contents
What is Data Science?
Data Science and Linguistics
Course Overview
IPython
Jupyter
Course Organization
Assignment 1

---

<!-- page:24 source:datsci-01-ipython-jupyter.pdf -->

## Jupyter

- Jupyter provides useful interactive interfaces to IPython (and other kernels)
- most recent interface, and likely soon the standard for data analyses in Python:
the Jupyter Lab (browser-based integrated environment for data science)
- we will rely on the classic and much simpler Jupyter Notebook, which is little more than a
browser-based editor for project ﬁles called notebooks
- ﬁle format has the ending.ipynb (“IPython notebook”), this is a very convenient
JSON-based format for sharing your data analysis projects with others

---

<!-- page:25 source:datsci-01-ipython-jupyter.pdf -->

## Jupyter: Setup

- installation should be just as easy as for IPython (if not: https://jupyter.org/install)
$ pip3 install notebook
- to run the notebook:
$ jupyter notebook
- after startup, you should see the notebook dashboard contents of your personal directory in
the browser window you were directed to (it is actually hosted on the local machine)
- navigate to the directory where you want to create your ﬁrst notebook ﬁle
- the New dropdown button is in a slightly unintuitive position (to me) on the upper right, this is
where you create a new empty notebook (choosing IPython as the kernel if several options)

---

<!-- page:26 source:datsci-01-ipython-jupyter.pdf -->

## Jupyter Notebooks: Basic Usage

- at its core, a Jupyter notebook consists of a sequence of numbered cells in which you interact
with the IPython interpreter which runs in the background
- currently selected cell is highlighted in blue, arrow keys for scrolling up and down
- when a cell is selected, use A and B keys to create a new cell above or below it
- cell you are currently editing is highlighted in green
- Enter on selected cell brings you into editing mode, Esc brings you back to selection mode
- to execute a cell: Shift + Enter while it is selected
- to delete a cell: select it (should be highlighted in blue), then Shift + Backspace or D → D
- there are also Markdown cells which allow you to insert formatted explanations in between
your code cells; to turn a cell into a Markdown cell, select it and press M (and Y to go back)
- closing the notebook will not shut down the server, you will have to go back to the terminal
from where you started it, and terminate the process using Ctrl+D

---

<!-- page:27 source:datsci-01-ipython-jupyter.pdf -->

## Jupyter Notebooks: Further Useful Features

- notebooks can be exported to various formats: PDF, HTML,...
- in most cases, best results for PDF export are achieved by using the menu option
File → Download as → PDF via LaTeX (but you might have to install xelatex for it)
- a good alternative might be File → Download as → PDF via HTML
- if both fails, you should be able to use the Print function of your browser, and conﬁgure it to
print to a PDF ﬁle (not necessary if you do not have any driver for a printer installed)

---

<!-- page:28 source:datsci-01-ipython-jupyter.pdf -->

Table of Contents
What is Data Science?
Data Science and Linguistics
Course Overview
IPython
Jupyter
Course Organization
Assignment 1

---

<!-- page:29 source:datsci-01-ipython-jupyter.pdf -->

## Course Organization

- practical seminar consisting of 12 sessions, leads to completion of a data science project
- goals of this course format:
- acquire ability to work with current standard tools of data science in Python
- achieve a good overview of algorithms and Python libraries for data modeling tasks
- taking a deep dive into a dataset of your own choice
- practice in deﬁning a data science project, and carrying it out within time constraints
- mandatory parts of coursework during the semester which can give you 3 CP ungraded:
- attendance (talk to me in case there are exceptional circumstances)
- assignments (requirements and possibility of group work will depend on participants)
- each session I introduce a new topic, interspersed with questions and practical elements
- the course concludes with a 90-hour semester project (more information on next slide)
- by default, you receive a graded 6 CP Schein, but you can register it as ungraded
- initial registration is via the Moodle

---

<!-- page:30 source:datsci-01-ipython-jupyter.pdf -->

## Possibilities for Projects

- towards the end of the lecture period, you should have found a research question about
some aspect(s) of some language(s) that you would like to answer, and have a good idea of
what relevant data is freely available, or needs to be collected
- good types of research questions for a Schein in Language and Cognition:
- try to predict judgments (difﬁculty, register) from linguistic features as an explanatory model
- join several sets of psycholinguistic data, and test for potential links between variables
- good types of research questions for a Schein in Variation, Evolution, and Change:
- comparing the strategies of expressing a given function in a parallel corpus
- testing a hypothesis based on a lexicostatistical database of a given family
- good types of research questions for a Schein in Language Use:
- corpus-driven answers to hypotheses about the grammar of a given language
- do individual authors or groups of authors differ in usage patterns?
- by default, submission is as a Jupyter notebook which does not only contain commented
code, but Markdown annotations explaining the background, your steps, and your conclusions

---

<!-- page:31 source:datsci-01-ipython-jupyter.pdf -->

Table of Contents
What is Data Science?
Data Science and Linguistics
Course Overview
IPython
Jupyter
Course Organization
Assignment 1

---

<!-- page:32 source:datsci-01-ipython-jupyter.pdf -->

## Assignment 1

- the ﬁrst of ten assignments is available on Moodle as a PDF
- for the ﬁrst three assignments, you have two weeks of processing time until submission;
from Assignment 4 we will switch to a weekly rhythm, as density of new concepts increases
- the purpose of this ﬁrst assignment is to help you brush up your elementary Python skills
(in case you have not programmed in a while), and to get used to the workﬂow
- the tasks can be performed using elementary Python, but some standard packages
will be very useful (intentionally, there are some utilities not all of you might know)
- tasks are intentionally a bit open-ended in order to help you get into the mindset of being
responsible for your own decisions in data processing; there is no perfect solution!
- the corpus is realistic in having many of the problems you will constantly see in other datasets
- you will need to export your notebook with the outputs as a PDF, and submit it via Moodle
before the start of the 7 May session (when the solution will be uploaded)

---

<!-- page:33 source:datsci-01-ipython-jupyter.pdf -->

## Course Plan

0 16/04 Elementary Python
1 23/04 Course Overview, IPython and Jupyter
2 30/04 Introduction to NumPy and Seaborn
3 07/05 Pandas and Data Handling
14/05 (Ascension of Christ)
4 21/05 Linguistic Preprocessing
28/05 (Pentecost Break)
04/06 (Corpus Christi)
5 11/06 Data Wrangling: Join, Combine, Reshape
6 18/06 Data Aggregation and Grouping
7 25/06 Modeling and Prediction
8 02/07 Classiﬁcation
9 09/07 Clustering
10 16/07 Pattern Extraction and Density Estimation
11 23/07 Statistical Inference
12 30/07 Data Science Projects (Hybrid)

---

<!-- page:34 source:datsci-01-ipython-jupyter.pdf -->

## Questions

Questions?
Comments?
Suggestions?

---
