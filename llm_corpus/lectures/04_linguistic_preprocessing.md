---
id: "04"
title: "Linguistic Preprocessing"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-04-linguistic-preprocessing.pdf"
pages: 20
date: "2026-05-21"
---

# Session 4: Linguistic Preprocessing

> Full slide text extracted from `datsci-04-linguistic-preprocessing.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-04-linguistic-preprocessing.pdf -->

## Session 4: Linguistic Preprocessing

Johannes Dellert
21 May, 2026

---

<!-- page:2 source:datsci-04-linguistic-preprocessing.pdf -->

## Table of Contents

Linguistic Preprocessing
SpaCy and NL TK
Keyword Extraction
T uple Extraction
Collocation Extraction

---

<!-- page:3 source:datsci-04-linguistic-preprocessing.pdf -->

## Linguistic Preprocessing

- in the data science literature, linguistic preprocessing typically comprises
- stemming or lemmatisation in order to reduce texts to standardised content words
- topic modeling and sentiment detection in order to classify texts into categories
- named entity recognition
- information extraction from textual data (e.g. the places at which events occurred)
- training simple sequence models or embeddings from corpora in order to generate
simulated language data
- the literature is written from the perspective of people who are not primarily interested in
answering questions about language, but about other domains, and NLP is mostly seen as a
tool for extracting the actually relevant information from textual data
- as computational linguists, we are of course aware of much more sophisticated NLP tasks
- as general linguists, the questions which we want to answer based on our data are going to be
focused on linguistic properties of the data, leading to a focus on the automated generation of
annotations (part-of-speech tagging, dependency parses, semantic role labeling,...)

---

<!-- page:4 source:datsci-04-linguistic-preprocessing.pdf -->

## Removing Stop Words

- whenever we are interested in the content rather than the linguistic structure of a text,
we want to focus on the content words and to ignore grammatical words such as articles and
prepositions which are traditionally called stop words
- in the typical case, a list of stop words (or stoplist) deﬁnes a ﬁlter which simply deletes the
tokens on the list during preprocessing, so that the result consists of content words:
any group of words might be chosen might become group words chosen
- there are no universally agreed-upon stoplists for individual languages; rather than containing
only grammatical words, many simply include the top-200 or top-50 most frequent words
(including e.g. nouns like name or year or verbs like go and try )
- while modern attention-based neural architectures have made this ﬁltering unnecessary for
NLP applications, it is still common practice in document indexing, and a helpful
preprocessing step for many of the more explainable methods used in science

---

<!-- page:5 source:datsci-04-linguistic-preprocessing.pdf -->

Table of Contents
Linguistic Preprocessing
SpaCy and NL TK
SpaCy
NL TK
SpaCy vs. NL TK: Comparison
Keyword Extraction
T uple Extraction
Collocation Extraction

---

<!-- page:6 source:datsci-04-linguistic-preprocessing.pdf -->

## SpaCy

- SpaCy is the most popular library for NLP tasks in Python
- started in 2015; coordinated by Explosion AI, many volunteer contributors
- main purpose is to provide a uniﬁed interface to a curated collection of deep learning models
which makes efﬁcient high-quality NLP technology easily accessible for production purposes
- very large ecosystem, efﬁcient implementation and streamlined interface
- markets itself as an industry standard (and it is difﬁcult to argue with that)

---

<!-- page:7 source:datsci-04-linguistic-preprocessing.pdf -->

## SpaCy: General Design

- the conﬁguration returns a pipeline method which you run once on a string of text, and the
result is a very complex Doc object which contains annotations on various levels of
description, organised into a hierarchy of containers:
- sentences and other larger units are organised into Span objects which form a tree over
Token objects
- every Token contains information about the lemma, the syntactic category (UDPOS tags),
the dependency label and the head (for UD dependency structures), as well as
morphological features
- NB: for the actual string content, the relevant ﬁelds have an underscore sufﬁx
(token.lemma is just an integer ID, token.lemma_ the actual string)
- it is a very large and very mature library, perusing the tutorials and the extensive
documentation is very much worth your while (if you are not a ﬂuent user already)!

---

<!-- page:8 source:datsci-04-linguistic-preprocessing.pdf -->

## Installing and Running a SpaCy model from Jupyter

- for spacy download in Jupyter, you need to use the! preﬁx for command execution:
!python -m spacy download en_core_web_sm
- after installation, restart the kernel to make sure the installed package is found
- this is how you load a model, and run the pipeline on some input for ﬁrst experiments:
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a first example sentence.")
- exploring the structure of the resulting Doc object is very instructive,
and a very good starting point for taking things from there

---

<!-- page:9 source:datsci-04-linguistic-preprocessing.pdf -->

## SpaCy: Self-Guided Tutorial

- if you have never worked with SpaCy, you might want to go through the following course in
order to understand the basic concepts and usage patterns before tackling the assignment
https://course.spacy.io/en/chapter1

---

<!-- page:10 source:datsci-04-linguistic-preprocessing.pdf -->

## Natural Language Toolkit (NLTK)

- the oldest major Python toolkit for NLP, has been around since 2001 (!)
- has grown constantly, and now provides support for a vast variety of NLP tools and resources
that were created during the past two decades (including many experimental approaches)
- has lost ground to newcomers like SpaCy in the deep learning era due to its focus on
individual modules for isolated tasks (which used to be its major strength)
- much more stable than SpaCy (in the sense that updates do not constantly break things),
comprehensive and reliable documentation

---

<!-- page:11 source:datsci-04-linguistic-preprocessing.pdf -->

## NLTK: General Design

- results are not available through a uniﬁed object hierarchy that is generated by pipelines,
but individual tools interface using elementary Python constructs like lists and dictionaries
- this makes things less streamlined, but makes it easier to just import one isolated function
from the toolkit (or add some custom logic in the middle of a pipeline):
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
your_lemmas = [lemmatizer.lemmatize(token) for token in your_sentence]

---

<!-- page:12 source:datsci-04-linguistic-preprocessing.pdf -->

## SpaCy vs. NLTK: Comparison

SpaCy
- focus on providing a uniﬁed and
streamlined interface to modern neural
models, but changes fast
- very good tokenisation, much faster at
processing large amounts of text due to
Cython backend
- integrates many models for tasks of
relevance for industry applications
(named entitry recognition, text
classiﬁcation)
- provides trained pipelines for only 24
major languages
NL TK
- less straightforward to use and steeper
learning curve, but more ﬂexible
- implements or provides interfaces to
many legacy approaches and resources
from the rule-based and statistical eras of
NLP (e.g. WordNet, PropBank,... )
- some support for many smaller
languages (for which deep learning
models might not be an option due to
lack of training data)
- very well-documented, good integration
with libraries like scikit-learn and
T ensorFlow (not just pretrained models)

---

<!-- page:13 source:datsci-04-linguistic-preprocessing.pdf -->

Table of Contents
Linguistic Preprocessing
SpaCy and NL TK
Keyword Extraction
T uple Extraction
Collocation Extraction

---

<!-- page:14 source:datsci-04-linguistic-preprocessing.pdf -->

## Keyword Extraction

- a good approximation of the intuitive notion of a keyword is that it is a content word
which occurs more often than we would expect on average in other texts
- most keyword extraction methods are based on comparing the relative frequencies pT (x)
of each lemma x in a text T with its global frequency p(x) estimated from a larger sample
- through parametric tests or bootstrapping, we can determine whether pT (x) exceeds a
signiﬁcance threshold given its distribution under the null hypothesis pT (x) = p(x)
- the signiﬁcance threshold is difﬁcult to decide; if we want to extract a ﬁxed number of
keywords in order to represent any text, we need an effect-size statistic which allows us to
rank keywords, not just a signiﬁcance statistic
- a useful measure for this purpose is log2
pT (x)
p(x), which is sometimes called the log ratio
- a value of 1 indicates that the word is twice as common as in average text
- a value close to 0 indicates that the word occurs about as much as in average text
- in practice, both distributions need to be smoothed, or only words of a certain base
frequency can be considered, otherwise rare words can receive extreme scores

---

<!-- page:15 source:datsci-04-linguistic-preprocessing.pdf -->

Table of Contents
Linguistic Preprocessing
SpaCy and NL TK
Keyword Extraction
T uple Extraction
Collocation Extraction

---

<!-- page:16 source:datsci-04-linguistic-preprocessing.pdf -->

## Tuple Extraction

- syntactic parsing (especially dependency parsing) is not often used by non-linguist
data scientists, though it makes it easy to extract predicate-argument tuples
- for example, if I want to extract information about which adjectives are often used to describe
a given noun (say, bridge), dependency structures (in UD format) can be used to extract
tuples of shape amod(bridge, X) from large amount of texts
- in this example, we would be able to extract the tuple from all kinds of syntactic environments:
- the long but narrow bridge
- ﬁve narrow stone bridges
- a bridge narrow like a needle
- in the new assignment, you will do this for verb-subject and verb-object combinations!

---

<!-- page:17 source:datsci-04-linguistic-preprocessing.pdf -->

Table of Contents
Linguistic Preprocessing
SpaCy and NL TK
Keyword Extraction
T uple Extraction
Collocation Extraction

---

<!-- page:18 source:datsci-04-linguistic-preprocessing.pdf -->

## Collocation Extraction

- pointwise mutual information (PMI) is a standard measure of how often two outcomes x
and y occur together compared to how often we would expect that to happen if the two events
occurred independently (note that this is a log ratio!)
pmi(x; y ):= log2
p(x, y )
p(x)p(y )
- popular in lexicography for lexical proﬁling (mining the most frequent word combinations
involving a word of interest from a large corpus), but also useful for author proﬁling (ﬁnding
combinations of words which are favoured by an author ⇒ useful for authorship attribution!)
- both applications can be framed as instances of collocation extraction

---

<!-- page:19 source:datsci-04-linguistic-preprocessing.pdf -->

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

<!-- page:20 source:datsci-04-linguistic-preprocessing.pdf -->

## Questions

Questions?
Comments?
Suggestions?

---
