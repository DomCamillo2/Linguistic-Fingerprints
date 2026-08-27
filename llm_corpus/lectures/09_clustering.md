---
id: "09"
title: "Clustering"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-09-clustering.pdf"
pages: 34
date: "2026-07-09"
---

# Session 9: Clustering

> Full slide text extracted from `datsci-09-clustering.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-09-clustering.pdf -->

## Session 9: Clustering

Johannes Dellert
9 July, 2026

---

<!-- page:2 source:datsci-09-clustering.pdf -->

## Table of Contents

Clustering
Agglomerative Clustering
k-Means Clustering
Gaussian Mixture Models (GMM)
DBSCAN

---

<!-- page:3 source:datsci-09-clustering.pdf -->

## Clustering Problems: General Setup

- in a clustering problem, we want to partition our set of data points into a limited number of
groups (called clusters) which are connected in some fashion by shared features or attributes
- any procedure which infers categories from data can be seen as a clustering algorithm
- in contrast to classiﬁcation, we do not attempt to apply preconceived categories to our data
points, but we ask whether there are categories inherent in the dataset, and if so
- into how many subsets the data points should be partitioned (difﬁcult!)
- which point should be assigned to which cluster
- clustering operates without labeled training data, which makes it
one of the main paradigms of unsupervised machine learning
- especially important in the initial stages of data analysis, providing an initially completely
unstructured dataset with (preliminary) structure which shows whether there are subsets of the
data points which “behave similarly”, and helps us conceptualise different subsets of the data
- clustering can help to guide sampling in order to tackle datasets of untractable size
(infer structure, then sample from each cluster for a more varied representation of diversity)

---

<!-- page:4 source:datsci-09-clustering.pdf -->

## Role of Clustering in Data Science

- clustering is a central element of many data science workﬂows
- the primary use cases can be summarised as abstraction over similar data points
- like classiﬁcation, clustering allows complex information about data points to be
preprocessed into values of a categorical variable which can then be used for modeling
- this is especially useful in case we are dealing with a large number of highly confounded
variables for which we have data (e.g. coded facts about grammar) that can be summarised
into some kind of distance or similarity measure
- clustering can allow us to compile these variables into a single categorical variable which
can then be used as an independent predictor (e.g. typological variables)

---

<!-- page:5 source:datsci-09-clustering.pdf -->

## Clustering Algorithms: Landscape

- we will ignore the branch leading to MiniBatch KMeans here (>10k points to cluster unlikely)

---

<!-- page:6 source:datsci-09-clustering.pdf -->

## Clustering Algorithms: General Overview

- mainstream clustering algorithms can be seen as implementations of one of four central
principles of cluster formation (all of which we will illustrate by at least one algorithm)
- connectivity-based clustering directly implements the intuition that objects are more related
to, and should therefore cluster with, nearby objects rather than with objects farther away
- in centroid-based clustering, each cluster is represented by a central vector which is not
necessarily a member of the data set, and points are assigned to the closest center
- in model-based clustering, each cluster is treated as arising from an underlying probability
distribution which we need to identify and keep separate within the mixture generating our data
- in density-based clustering, clusters are deﬁned as areas of higher density than the
remainder of the data set, leaving objects in sparse areas unassigned as noise

---

<!-- page:7 source:datsci-09-clustering.pdf -->

## Clustering Algorithms: Comparison

- as in the illustration of classiﬁers, intuitions might not carry over to high-dimensional data!

---

<!-- page:8 source:datsci-09-clustering.pdf -->

Table of Contents
Clustering
Agglomerative Clustering
k-Means Clustering
Gaussian Mixture Models (GMM)
DBSCAN

---

<!-- page:9 source:datsci-09-clustering.pdf -->

## Agglomerative Clustering

- in agglomerative clustering, we start with clusters of size one which we progressively merge
into ever bigger clusters; this results in a tree structure being inferred over the data points,
and is therefore also called hierarchical clustering
- at each step, two smaller clusters are linked into a larger one, and the decision which clusters
to merge next is determined by a cluster linkage criterion
- the most common linkage types are:
- complete linkage clustering (always link the two clusters with smallest maximum distance)
- single linkage clustering (always link the two clusters with smallest minimum distance)
- average linkage clustering (always link the two clusters with smallest average distance)
- Ward linkage clustering (always link the pair of clusters that leads to minimum increase in
total within-cluster variance, i.e. sum of squares of distances from average, after merging)
- we stop at a threshold which needs to be tuned as a hyperparameter

---

<!-- page:10 source:datsci-09-clustering.pdf -->

## Agglomerative Clustering: Illustration

- this is an example of the hierarchical structure resulting from agglomerative clustering:
- choosing the threshold parameter corresponds to cutting this tree at a certain height,
and treating the connected pieces as clusters

---

<!-- page:11 source:datsci-09-clustering.pdf -->

## Comparison of Hierarchical Linkage Methods

- in this comparison, there is no ground truth,
but the intended clusters are visually
prominent (except in the last row, which is
intended to show the behaviour on
completely random data)
- note that single linkage shows “chaining”
behaviour which is good for ﬁnding
line-shaped clusters, whereas the other
methods prefer compact shapes
- due to being distance-based, intuitions
about the behaviour of agglomerative
clustering carry over to higher dimensions
better than for previous illustrations

---

<!-- page:12 source:datsci-09-clustering.pdf -->

## Agglomerative Clustering: Strengths and Weaknesses

- strengths:
- most variants do not need an (explicit) mapping of data points to vectors in a space,
a pairwise distance (or similarity) matrix is all we needed
- very fast implementations are possible (at least for single linkage and complete linkage)
- behaviour is very intuitive, can be traced well due to very local decisions
- weaknesses:
- mathematical properties are often unsatisfactory (we would typically want to be able to
characterise the output as optimising a given well-understood criterion)
- picking threshold values is a difﬁcult problem without a general solution
- unstable, slight changes to the input can lead to very different results
- very sensitive to outliers
- output can vary a lot with the linkage criterion chosen

---

<!-- page:13 source:datsci-09-clustering.pdf -->

## Agglomerative Clustering in Scikit-Learn

- the common interface for clustering algorithms in Scikit-Learn is just as streamlined as the one
we have seen last time for classiﬁcation (except evaluation metrics differ between algorithms)
- the design matrix X is identical to the one from the classiﬁcation examples
(it is just that the labels we provided in the vector y are irrelevant in the clustering scenario)
- this is a minimal example of agglomerative clustering from the documentation:
- by default, Ward linkage clustering is used; the linkage parameter can be used to change it
(values: "complete", "average", "single")

---

<!-- page:14 source:datsci-09-clustering.pdf -->

Table of Contents
Clustering
Agglomerative Clustering
k-Means Clustering
Gaussian Mixture Models (GMM)
DBSCAN

---

<!-- page:15 source:datsci-09-clustering.pdf -->

## k-Means Clustering

- k-Means clustering is the primary example of centroid-based clustering; it uses the mean of
the data points in a cluster in order to represent (and characterise) it
- k-Means clustering operates in an expectation-maximisation (EM) framework, in which we
perform inference by alternating between two stages until a convergence criterion is reached:
- the expectation step (E step) draws samples from the model given the current parameters
in order to approximate the probability of the data given the model
- the maximisation step (M step) changes the model parameters in order to maximise the
likelihood of the samples drawn in the E step
- in the case of k-Means, the model consists of a set of k cluster means as well as a mapping
from data points to clusters, and the stages of expectation-maximisation look as follows:
- in the E step, we (re)assign each data point to its closest cluster mean
- in the M step, we update the cluster mean by averaging the points assigned to it

---

<!-- page:16 source:datsci-09-clustering.pdf -->

## k-Means Clustering: Illustration by VanderPlas (2023)

- in each E step, each point is assigned to its nearest cluster mean (this assignment is
represented by colour) according to some distance metric (Euclidean in the example)
- in the following M step, the position of each cluster mean (non-transparent black dot)
is updated to the average of the points currently assigned
- convergence is reached when the cluster means do not get changed any more in an M step
(which will happen if no point got reassigned to a different cluster in the previous E step)

---

<!-- page:17 source:datsci-09-clustering.pdf -->

## k-Means Clustering: Strengths and Weaknesses

- strengths:
- conceptually close to nearest neighbour classiﬁcation
- expectation-maximisation framework gives it a model-based interpretation
- weaknesses:
- objects need to live in a space in which computation of means makes sense
- mathematically well-founded, fruitful connections to geometric inference problems
- NP-hard optimisation problem (i.e. very likely that any algorithm has exponential runtime);
algorithms need to look for approximate solutions, and often run into local minima
- not fully probabilistic: no intrinsic measure of probability or uncertainty of cluster
assignments, hard cluster boundaries which will lead to “clashes” in complex situations
- clusters are always circular / (hyper)spherical in shape

---

<!-- page:18 source:datsci-09-clustering.pdf -->

## k-Means Clustering: Poor Convergence (VanderPlas 2023)

- there would be a much better solution for k = 4, but due to bad luck with the initial state,
the EM algorithm got stuck in a highly suboptimal local optimum (this easily happens!)

---

<!-- page:19 source:datsci-09-clustering.pdf -->

## k-Means Clustering in Scikit-Learn

- minimal example from the Scikit-Learn documentation:
- by default, the initial centroids are chosen based on empirical measures of contributions in
exploratory samples, but switching to init="random" will pick random data points in order
to explore a larger part of the search space (this can be used to avoid local optima)
- the parameter n_init allows to conﬁgure how many times the EM algorithm will be restarted
with a different initial state (the result will be the best-scoring one across all attempts)

---

<!-- page:20 source:datsci-09-clustering.pdf -->

## k-Means Clustering: Poor Choice of k (VanderPlas 2023)

- k-Means will ﬁnd clusters for any choice of k, but we need a way of deciding on the k
- this decision (value of n_clusters) is much more involved

---

<!-- page:21 source:datsci-09-clustering.pdf -->

## Silhouette Scores as a Criterion for Choosing k

- a very common practice is to compute the silhouette scores for different values of k
- a silhouette coefﬁcient (range [-1,1]) measures how close each point in a cluster is to points
in the neighboring clusters (1 means far away from other clusters, 0 at decision boundary)
- the silhouette score is the average of silhouette coefﬁcient across all points
- implemented by sklearn.metrics.silhouette_score
- the following example show how a better choice of k will lead to better silhouette coefﬁcients
on average (the red dashed lines represent the resulting scores)
- if the silhouette scores are inconclusive, it is worth exploring several of the best options in
detail (often the difference will be about making local decisions about merging clusters or not)

---

<!-- page:22 source:datsci-09-clustering.pdf -->

Table of Contents
Clustering
Agglomerative Clustering
k-Means Clustering
Gaussian Mixture Models (GMM)
DBSCAN

---

<!-- page:23 source:datsci-09-clustering.pdf -->

## Gaussian Mixture Models (GMM)

- Gaussian Mixture Models (GMM) are the prime example of model-based clustering
- basic ideas:
- model the data in each cluster as arising from a separate Gaussian distribution,
and the entire dataset as the combined result of sampling from these distributions
- to perform clustering, infer the combination of parameters of a given number of Gaussian
distributions (and a mapping of data points to these distributions) which maximises the
likelihood of the data being generated
- again, inference is approximated via expectation-maximisation:
- during the E step, we (re)assign each data point to the cluster distribution which assigns the
highest probability to it
- during the M step, we adapt the parameters of each cluster distribution to maximise the
likelihood of the assigned data points being generated from it

---

<!-- page:24 source:datsci-09-clustering.pdf -->

## Gaussian Mixture Models (GMM): Illustration

---

<!-- page:25 source:datsci-09-clustering.pdf -->

## Gaussian Mixture Models: Strengths and Weaknesses

- strengths:
- support for elliptical clusters (not only circles)
- fully probabilistic: cluster assignments are parameters!
- number of components can be decided based on well-behaved
standard measures of model quality (e.g. BIC and AIC)
- weaknesses:
- the other two weaknesses of k-means remain:
objects need to live in a space in which we can model Gaussians, risk of local minima
- limited to elliptical clusters (perhaps in transformed spaces)

---

<!-- page:26 source:datsci-09-clustering.pdf -->

## Gaussian Mixture Models in Scikit-Learn

- minimal example of a Gaussian Mixture Model from the documentation:

---

<!-- page:27 source:datsci-09-clustering.pdf -->

Table of Contents
Clustering
Agglomerative Clustering
k-Means Clustering
Gaussian Mixture Models (GMM)
DBSCAN

---

<!-- page:28 source:datsci-09-clustering.pdf -->

## Density-Based Clustering: DBSCAN

- DBSCAN is the most popular algorithm implementing the intuition of density-based clustering
- group together points that are “closely packed” (i.e. which have many nearby neighbors)
- marks as outliers points that lie alone in low-density regions (those whose nearest
neighbors are too far away)
- to go a little bit more into detail, DBSCAN proceeds in three stages:
- ﬁnd the points within a meaningful distance threshold for every point, identify core points
which have more neighbors than a given minimum cluster size
- clusters are connected components of core points on their neighbor graph
- assign each non-core point to a nearby cluster if within threshold, otherwise to noise

---

<!-- page:29 source:datsci-09-clustering.pdf -->

## DBSCAN: Illustration

- the radius of the circles is the distance
threshold, showing for each point
which other points are “within reach”
- the resulting neighbour graph is
represented by the black arrows
- core points are marked in red
(the minimum cluster size threshold
chosen here was 2)
- in this case, all core points
form a single cluster
- yellow points are the non-core points
which are assigned to a cluster due to
being within the distance threshold
- nodes that are not within the
threshold of any core point of are not
assigned to any cluster (outliers, like
the example in blue)

---

<!-- page:30 source:datsci-09-clustering.pdf -->

## DBSCAN: Strengths and Weaknesses

- strengths:
- no need to specify the number of clusters in advance
- possibility to ﬁnd arbitrarily-shaped clusters
- high robustness to outliers
- only two parameters which domain experts will have intuitions about
(meaningful distance threshold and minimum cluster size)
- weaknesses:
- depends on quality of the distance measure, curse of dimensionality can kick in quite early
- performs badly in case clusters are of different density

---

<!-- page:31 source:datsci-09-clustering.pdf -->

## DBSCAN in Scikit-Learn

- minimal example of DBSCAN from the documentation:

---

<!-- page:32 source:datsci-09-clustering.pdf -->

## Sources

- Grus (2019): “Data Science from Scratch: First Principles with Python, 2nd edition”,
Chapter 20: “Clustering”
- VanderPlas (2023): “Python Data Science Handbook, 2nd edition”,
Chapter 47: “In Depth: k-Means Clustering”
- VanderPlas (2023): “Python Data Science Handbook, 2nd edition”,
Chapter 48: “In Depth: Gaussian Mixture Models”
- various parts of the Scikit-Learn online documentation

---

<!-- page:33 source:datsci-09-clustering.pdf -->

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

<!-- page:34 source:datsci-09-clustering.pdf -->

## Questions

Questions?
Comments?
Suggestions?

---
