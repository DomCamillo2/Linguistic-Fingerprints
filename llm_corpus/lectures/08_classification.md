---
id: "08"
title: "Classification"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-08-classification.pdf"
pages: 41
date: "2026-07-02"
---

# Session 8: Classification

> Full slide text extracted from `datsci-08-classification.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-08-classification.pdf -->

## Session 8: Classiﬁcation

Johannes Dellert
2 July, 2026

---

<!-- page:2 source:datsci-08-classification.pdf -->

## Table of Contents

Classiﬁcation
k-Nearest Neighbours
Naive Bayes
Decision T rees and Random Forests
Support Vector Machines

---

<!-- page:3 source:datsci-08-classification.pdf -->

## Classiﬁcation Problems: General Setup

- in a classiﬁcation problem, we want to categorise data points as belonging
to one of a set of predeﬁned classes based on their features or attributes
- any model which predicts values of a categorical variable can therefore be seen (and
modeled) as a classiﬁer; we have thus already seen our ﬁrst example: logistic regression
- most problems in language technology can be treated as classiﬁcation problems,
making machine learning approaches to classiﬁcation the dominant paradigm in NLP
- part-of-speech tagging (choice between tags)
- morphological analysis (choice between possible analyses)
- dependency parsing (choice between heads, choice between relations)
- semantic role labelling (choice among inventory of roles)
- word sense disambiguation (choice between word senses)
- sentiment detection (choice within inventory of sentiments)

---

<!-- page:4 source:datsci-08-classification.pdf -->

## Role of Classiﬁcation in Data Science

- the role of classiﬁcation in data science is somewhat more limited
than in the engineering applications of machine learning
- the primary use case is in explanatory models of categorical variables
- two other applications are best seen as preprocessing techniques
- imputation (“informed guesses”) of missing values in categorical variables
- treat the records with known values for the relevant variables as labeled instances
- apply machine learning in order to predict the missing labels,
evaluate the model in the usual way to assess how successful the imputation was
- important: treating imputed values as data will make inference less reliable!
- classiﬁcation allows complex information about data points to be summarised as
values of a categorical variable which can then be used for modeling
- this is especially useful in case we are dealing with a large number of highly confounded
categorical variables for which we have data (e.g. coded facts about grammar)
- a classiﬁer can allow us to summarise these variables into a single categorical variable
which can be used as an independent predictor (e.g. typological variables)

---

<!-- page:5 source:datsci-08-classification.pdf -->

## Classiﬁcation Algorithms: Landscape

- we are going to ignore the branch leading to the SGD classiﬁer here (>100k samples unlikely)

---

<!-- page:6 source:datsci-08-classification.pdf -->

## Classiﬁcation Algorithms: Comparison

- this chart illustrates the decision boundaries learnt by various algorithms on three prototypical
example datasets for binary classiﬁcation in two dimensions: spiral, circle, linearly separable
- note that at higher dimensions, most categories become linearly separable!

---

<!-- page:7 source:datsci-08-classification.pdf -->

Table of Contents
Classiﬁcation
k-Nearest Neighbours
Naive Bayes
Decision T rees and Random Forests
Support Vector Machines

---

<!-- page:8 source:datsci-08-classification.pdf -->

## k-Nearest Neighbours: Motivation

- basic idea of exemplar-based learning: just remember all the training instances,
predict new instances by retrieving similar instances and interpolating between them
- k-nearest neighbours is the application of this idea to classiﬁcation: ﬁnd a predeﬁned number
k of training samples closest in distance to the new point, and predict the label from these
- algorithmic challenge for larger amounts of training data: efﬁcient indexing structures which
allow quick extraction of the closest points for any unseen input instance
- various parameters need to be chosen for each application:
- number k of nearest neighbours to retrieve (can be treated as a hyperparameter)
- alternative: retrieve all neighbours in a given radius r (a radius neighbours classiﬁer )
- distance measure (any metric, Euclidean distance is the default)
- uniform prediction weights, or scaled with inverse of distance?
- nearest neighbours form the core of more advanced algorithms, e.g. kernel density estimation

---

<!-- page:9 source:datsci-08-classification.pdf -->

## k-Nearest Neighbours in scikit-learn

- minimal example from the Scikit-Learn documentation:
- equivalent code for radius neighbours classiﬁcation:

---

<!-- page:10 source:datsci-08-classification.pdf -->

## k-Nearest Neighbours: Inﬂuence of Prediction Weights

---

<!-- page:11 source:datsci-08-classification.pdf -->

## k-Nearest Neighbours: Strengths and Weaknesses

- strengths:
- conceptually very simple, very transparent decisions that are easy to trace
- non-parametric method without any underlying assumptions, which often makes it
successful in classiﬁcation situations where the decision boundary is very irregular
- weaknesses:
- sensitivity to scaling (all input dimensions should be standardised!)
- no underlying model which would represent any understanding of the domain
⇒ not useful for understanding why data points group the way they do
- curse of dimensionality in high-dimensional spaces, where samples are very sparsely
distributed, and new data points are very unlikely to be close to training instances

---

<!-- page:12 source:datsci-08-classification.pdf -->

Table of Contents
Classiﬁcation
k-Nearest Neighbours
Naive Bayes
Decision T rees and Random Forests
Support Vector Machines

---

<!-- page:13 source:datsci-08-classification.pdf -->

## Naive Bayes: Motivation

- probabilistic approaches to solving a classiﬁcation problem amount to ﬁtting a conditional
probability distribution P(L | Features) over different labels L given the observed features
- directly ﬁtting P(L | Features) is difﬁcult to impossible, but it is often straightforward to estimate
from training data the feature distribution for each label, i.e. P(Features | L)
- Bayes’ theorem allows us to translate one into the other:
P(L | Features) = P(Features | L) · P(L)
P(Features)
- full Bayesian inference is computationally very intensive, and relies heavily on deﬁning a good
prior P(L) and a potentially quite complex likelihood function P(Features | L) (to understand
why, note that this involves parametrising complex joint distributions across all features!)
- in many cases, we can get away with very naive assumptions about the generative model
which underlies the likelihood function; we arrive at a Naive Bayes classiﬁer when we
introduce the very unrealistic assumption that features are conditionally independent, i.e.
P(Features | L) = P(F1,...,Fk | L) =
k∏
i=1
P(Fi | L)

---

<!-- page:14 source:datsci-08-classification.pdf -->

## Naive Bayes: Variants

- several common variants are distinguished by which assumption they make
with respect to the generative distributions P(Fi | L) for each label L
- Gaussian Naive Bayes assumes that each P(Fi | L) can be characterised as generated
from a Gaussian distribution (one distribution for each feature-label combination!)
- training boils down to computing the mean and variance for each feature on each class of
training instances (note that we assume independence ⇒ no covariance!)
- the default choice for continuous data, especially if normality assumptions are met
- if some distributions are very skewed, we can kernelise (see below)
- this is the default choice for continuous data
- Multinomial Naive Bayes assumes each joint P(F | L) to be generated from a simple
multinomial distribution (the naive independence assumption applies within the distribution!)
- a multinomial distribution is parametrised by counts of each event, so training just counts for
each feature how often it occurs in instances labeled by L (followed by some smoothing)
- this is the default choice for count data (e.g. token frequencies in documents)

---

<!-- page:15 source:datsci-08-classification.pdf -->

## Gaussian Naive Bayes: Illustration of a Trained Two-Label Classiﬁer

---

<!-- page:16 source:datsci-08-classification.pdf -->

## Gaussian Naive Bayes: Visualisation of Predictions on Random Data

---

<!-- page:17 source:datsci-08-classification.pdf -->

## Gaussian Naive Bayes in scikit-learn: VanderPlas (2023)

- the make_blobs function is useful for creating random test data as in the previous example:
- using the usual Scikit-Learn interface, training a Gaussian Naive Bayes classiﬁer is trivial:
- in order to visualise the decision boundary, random data were generated like this:

---

<!-- page:18 source:datsci-08-classification.pdf -->

## Multinomial Naive Bayes: Application to Text Classiﬁcation

- Multinomial Naive Bayes is especially popular as a baseline model in document classiﬁcation
(classiﬁcation by genre or topic; spam detection, though it is easily tricked)
- underlying assumption: texts from every genre/topic arise from a multinomial distribution,
i.e. generated by sequences of random draws from an urn with a certain mixture of words
- we are going to walk through a simple example from VanderPlas (2023):
- we use parts of a dataset covering texts from 20 newsgroups that comes with Scikit-Learn:
from sklearn.datasets import fetch_newsgroups
- we select four categories, and retrieve the train and test data by the original split provided:

---

<!-- page:19 source:datsci-08-classification.pdf -->

## Multinomial Naive Bayes: Text Classiﬁcation Example by VanderPlas (2023)

- the MultinomialNB class expects count features in its input ( X consists of numbers!),
and we could just count words in order to prepare the training data
- but we can also do something (slightly) more sophisticated by applying TF-IDF vectorisation
- TF-IDF: term frequency multiplied by inverse document frequency
- we apply this to create higher “counts” for words that are unique to each document
- Scikit-Learn implements this in a TfidfVectorizer class which produces exactly the output
format we will need as input, so we can use Scikit-Learn’s pipeline functionality to chain the
two components together, and receive a model object we can ﬁt in the usual way:

---

<!-- page:20 source:datsci-08-classification.pdf -->

Multinomial Naive Bayes: Text Classiﬁcation Example by VanderPlas (2023)
- for evaluation, we use the confusion_matrix method from sklearn.metrics:
- it turns out that already such a simple classiﬁer can
successfully separate space discussions from
computer discussions!
- perhaps unsurprisingly, discussions of Christianity
and religion more generally turn out to be much
harder to separate based on the words used

---

<!-- page:21 source:datsci-08-classification.pdf -->

Multinomial Naive Bayes: Text Classiﬁcation Example by VanderPlas (2023)
- this is how we can create a prediction method:
- showing the method at work:

---

<!-- page:22 source:datsci-08-classification.pdf -->

## Naive Bayes: Strengths and Weaknesses

- stengths:
- very fast both in training and prediction
- straightforward probabilistic interpretation
- often easily interpretable
- very few tunable parameters
- weaknesses:
- simplifying assumptions cause lower performance by default
- not very adaptive, few reﬁnements possible
- overall: useful “quick and dirty” baseline for classiﬁcation problems

---

<!-- page:23 source:datsci-08-classification.pdf -->

Table of Contents
Classiﬁcation
k-Nearest Neighbours
Naive Bayes
Decision T rees and Random Forests
Support Vector Machines

---

<!-- page:24 source:datsci-08-classification.pdf -->

## Decision Trees: Motivation

- decision trees are a very common way of structuring knowledge about categories:
- learning a decision tree means to boils down to selecting at each node which predictor to split
on (this is done based on information theory), and to decide on a separation criterion (partition
for categorical predictors, threshold values for numerical predictors, with the goal of balance)
- parameters to decide when ﬁtting a decision tree include
- maximum tree depth, maximum number of leaf nodes
- constraints on number of samples per branch/leaf

---

<!-- page:25 source:datsci-08-classification.pdf -->

## Decision Trees: Illustration of Decision Boundaries

---

<!-- page:26 source:datsci-08-classification.pdf -->

## Decision Trees: Strengths and Weaknesses

- stengths:
- very easy to understand and interpret,
and the process by which they reach a prediction is completely transparent
- can easily handle a mix of numerical and categorical predictor variables
- weaknesses:
- ﬁnding an optimal solution is computationally a very hard problem
- it is very easy to overﬁt trees to the training data (especially with many predictors)

---

<!-- page:27 source:datsci-08-classification.pdf -->

## Random Forests

- to avoid overﬁtting, we use an ensemble classiﬁer consisting of simple classiﬁers:
- ﬁt parallel instances of a simpler high-bias model to variations (e.g. resamples)
of the training data (this is where the decision tree becomes a “forest”)
- make the classiﬁcation decision based on majority vote
- in the case of a random forest, we make each split decision on a random subset
consisting of only m of the p predictors; this helps to decorrelate the trees

---

<!-- page:28 source:datsci-08-classification.pdf -->

## Random Forests: Illustration of Decision Boundaries

---

<!-- page:29 source:datsci-08-classification.pdf -->

## Decision Trees in Scikit-Learn: Code Examples from VanderPlas (2023)

- basic usage of a decision tree classiﬁer:
- basic usage of a random forest classiﬁer:
- for the available options, check the documentation and examples!

---

<!-- page:30 source:datsci-08-classification.pdf -->

Table of Contents
Classiﬁcation
k-Nearest Neighbours
Naive Bayes
Decision T rees and Random Forests
Support Vector Machines

---

<!-- page:31 source:datsci-08-classification.pdf -->

## Linear Discriminative Classiﬁers

- a linear discriminative classiﬁer ﬁnds a linear decision boundary which separates the
instances of the training data, which it will compare unseen inputs against
- there can be many solutions which will differ in their behaviour on certain inputs (cross)
- how do we select the optimal one between these options?

---

<!-- page:32 source:datsci-08-classification.pdf -->

## Support Vector Machines: Intuition

- one obvious idea is to maximise the margin, i.e. to pick a decision boundary which keeps
maximum distance to the nearest training data points with both labels
- the data points which limit the margin of the decision boundary are called its support vectors

---

<!-- page:33 source:datsci-08-classification.pdf -->

## Support Vector Machines: Illustration

- the maximum-margin hyperplane can be characterised by its normal vector w and an offset b,
and for any data point x, the sign of wT x − b tells us which side of the hyperplane it ends up on
- for ﬁtting the hyperplane, we get a loss function which only depends on the support vectors
(circled in the example below), hence the name support vector machine (SVM)

---

<!-- page:34 source:datsci-08-classification.pdf -->

## Support Vector Machines: Softening the Margin

- in case the training data are not linearly separable, we can make the method more tolerant by
allowing some points to lie within the margin; this is controlled by a “fudge factor” C which
“hardens” the margin at high values, and penalises within-margin points less at low values

---

<!-- page:35 source:datsci-08-classification.pdf -->

## Beyond Linear Boundaries

- in some cases (like the circle dataset), adding additional dimensions to the input data would
make a linear decision boundary possible:

---

<!-- page:36 source:datsci-08-classification.pdf -->

## Kernel SVMs

- SVMs can be enhanced by a kernel which generalises the scalar product by implicitly
computing it in a higher-dimensional space (without explicitly transforming the data points)
- different kernels allow various types of non-linear decision boundaries in the original space:

---

<!-- page:37 source:datsci-08-classification.pdf -->

## Support Vector Machines: Strengths and Weaknesses

- strengths:
- compact and memory-efﬁcient (storage only for a few support vectors)
- very fast prediction once the model is trained
- very good performance on high-dimensional data
- very adaptable due to integration with kernel methods
- weaknesses:
- training time scales at least quadratically with the number of samples
- results can depend very much on the softening parameter C,
which therefore has to be chosen carefully using cross-validation (expensive!)
- results do not have a direct probabilistic interpretation

---

<!-- page:38 source:datsci-08-classification.pdf -->

## Support Vector Machines in Scikit-Learn: Code Examples

- ﬁtting a basic SVM (= linear kernel), starting with a high C (as recommended for exploration):
- the model provides the usual predict method
- kernelisation merely involves switching to a non-linear kernel,
e.g. radial basis functions (RBF), as was done for the example:
- note that kernel='rbf' is the default, i.e. 'linear' must be set explicitly for a linear SVM!
- for the available options, check the documentation and examples!

---

<!-- page:39 source:datsci-08-classification.pdf -->

## Sources

- VanderPlas (2023): “Python Data Science Handbook, 2nd edition”,
Chapter 41: “In Depth: Naive Bayes Classiﬁcation”
- VanderPlas (2023): “Python Data Science Handbook, 2nd edition”,
Chapter 43: “In Depth: Support Vector Machines”
- VanderPlas (2023): “Python Data Science Handbook, 2nd edition”,
Chapter 44: “In Depth: Decision T rees and Random Forests”

---

<!-- page:40 source:datsci-08-classification.pdf -->

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
7 25/06 Modelling and Prediction
8 02/07 Classiﬁcation
9 09/07 Clustering
10 16/07 Pattern Extraction and Density Estimation
11 23/07 Statistical Inference
12 30/07 Data Science Projects (Online)

---

<!-- page:41 source:datsci-08-classification.pdf -->

## Questions

Questions?
Comments?
Suggestions?

---
