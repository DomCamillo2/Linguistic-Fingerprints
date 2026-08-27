---
id: "10"
title: "Pattern Extraction and Density Estimation"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-10-pattern-extraction.pdf"
pages: 31
date: "2026-07-16"
---

# Session 10: Pattern Extraction and Density Estimation

> Full slide text extracted from `datsci-10-pattern-extraction.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-10-pattern-extraction.pdf -->

## Session 10: Pattern Extraction and Density Estimation

Johannes Dellert
16 July, 2026

---

<!-- page:2 source:datsci-10-pattern-extraction.pdf -->

## Table of Contents

Pattern Extraction
Dimensionality Reduction
Density Estimation

---

<!-- page:3 source:datsci-10-pattern-extraction.pdf -->

## Pattern Extraction: Deﬁnition and Approaches

 clustering (the topic of the last session) can be seen as a special case of pattern extraction,
i.e. the unsupervised assignment of additional structure to a dataset
 pattern extraction is at the core of the informal process of “making sense of a dataset”
 many inference problems can be framed as pattern extraction:
- clustering as a way to ﬁnd classes of similar instances
- community detection as a way of ﬁnding clusters in a neighborhood graph
- signiﬁcance tests in order to ﬁnd the correlation structure connecting a set of variables
- tests for vanishing mutual information in order to infer the information geometry
- v-structure tests in order to infer a causal graph over a set of variables
 but in this session, we are going to focus on two classical inference problems:
- making the relevant structure of a dataset appear by ‘boiling it down’ to a managable
number of dimensions ( dimensionality reduction)
- approximating an underlying joint distribution from samples ( density estimation),
though a distribution would not conventionally be called a “pattern” (hence the session title)

---

<!-- page:4 source:datsci-10-pattern-extraction.pdf -->

Table of Contents
Pattern Extraction
Dimensionality Reduction
Principal Component Analysis
Manifold Learning
Density Estimation

---

<!-- page:5 source:datsci-10-pattern-extraction.pdf -->

## Dimensionality Reduction: Deﬁnition and Role in Data Science

 dimensionality reduction is the task of transforming data into a lower-dimensional space so
that the low-dimensional representation retains meaningful properties of the original data
 this is central to overcoming the curse of dimensionality that we have encountered
- regression, classiﬁcation and clustering perform much better in lower-dimensional spaces
- for instance, if we pick a dimensionality reduction which approximates the original similarity
relations well, the much more tractable clustering task will still yield good results
 dimensionality reduction techniques are generally unsupervised, i.e. they are typically run on
unlabeled data in order to understand their inherent structure as it arises from relations
between datapoints
 some methods can be used to approximate the intrinsic dimension of a dataset (roughly: the
lowest number of dimensions to which a dataset can be compressed), which is a measure of
the complexity of the dataset (with important implications e.g. for the size of design spaces)

---

<!-- page:6 source:datsci-10-pattern-extraction.pdf -->

## Dimensionality Reduction: Overview of Approaches

 approaches to linear dimensionality reduction:
- feature selection (= discarding some variables)
- linear feature extraction/projection (= aggregating variables through weighted sums),
especially Principal Component Analysis (PCA, see below)
- singular value decomposition (very math-heavy, largely replaced by embeddings)
 approaches to non-linear dimensionality reduction:
- kernel PCA (Principal Component Analysis using kernels)
- manifold learning (see below)
- learning embeddings in a neural architecture with non-linear activation functions
- autoencoders are architectures trained to reproduce the output through a
lower-dimensional intermediate representation

---

<!-- page:7 source:datsci-10-pattern-extraction.pdf -->

## Principal Component Analysis: General Idea and Mathematical Background

 Principle Component Analysis (PCA) is a fast and very ﬂexible dimensionality reduction
technique which is based on determining the principal axes (the axes of maximum variation)
in the data, and projecting each data point onto these principal axes
 a full understanding presupposes good knowledge of linear algebra (it relies on singular value
decomposition), but informally, PCA can be described as proceeding in the following fashion:
- 1) ﬁnd the weight vector which maximises the variances of the result of multiplying each
variable by its weight (i.e. the “mix of axes” on which the data varies the most)
w(1) = arg max
jjwjj=1
{∑
i
(x(i)  w)2
}
- 2) project all data points onto this new principle axis, and subtract the vectors performing
these projections from the original data (this share of the variation is now accounted for!)
- 3) go back to step 1) on the reduced data in order to determine the next principal axis
 if we stop the process after a number of iterations that is lower than the dimensionality of the
original data, we have performed dimensionality reduction!

---

<!-- page:8 source:datsci-10-pattern-extraction.pdf -->

## Principal Component Analysis: Illustration (First Two Components)

---

<!-- page:9 source:datsci-10-pattern-extraction.pdf -->

## Principal Component Analysis: Further Uses and Limitations

 beyond its core purpose of dimensionality reduction, PCA is a very widespread standard
technique in several additional contexts:
- visualisation (getting an informative two- or three-dimensional view of complex data)
- noise ﬁltering (discarding variation beyond a certain number of dimensions as noise)
- feature extraction for the purposes of machine learning (pre-processed input)
 when using PCA, it is important to be aware of the following limitations:
- results depend on the scaling of variables (i.e. proper use normally requires variables to be
scaled by their standard deviation; many implementations do not do this by default!)
- dimensions after the transformation are linear interpolations of the original variables,
i.e. the axes of a PCA visualisation cannot be expected to be interpretable
- PCA only captures linear correlations between features, though as in other methods,
kernelisation can help overcome this restriction

---

<!-- page:10 source:datsci-10-pattern-extraction.pdf -->

## Principle Component Analysis in Scikit-Learn

 minimal example of a PCA from the documentation:
 the explained variance ratios can be used to decide how many components make sense (in
this example, the data can be reduced very well to a single dimension)
 the singular values reﬂect the eigenvalues of the covariance matrix
(and thereby the dimensions of the projected unit square/(hyper)cube in each direction)
 variants: IncrementalPCA (closest to the informal explanation), SPARSE PCA, KernelPCA

---

<!-- page:11 source:datsci-10-pattern-extraction.pdf -->

## Dimensionality Reduction: Advanced Techniques

 we will cover PCA, LLE, IsoMap, and Kernel Approximation in this session

---

<!-- page:12 source:datsci-10-pattern-extraction.pdf -->

## Manifold Learning: General Idea

 manifold learning can be pictured as learning to “squeeze” a low-dimensional map into a
higher-dimensional space (including equivalents of twists and turns, bending and crumpling!)
in order to adjust to its structure
 in principle, this is a very mature and ﬂexible mathematical framework, the implementation of
which leads to very interesting capabilities which are easy to demonstrate on toy datasets
 in practice, manifold learning techniques are quite ﬁnicky on real-world data, and are therefore
rarely used beyond qualitative visualisation of high-dimensional data

---

<!-- page:13 source:datsci-10-pattern-extraction.pdf -->

## Manifold Learning: Some (Semi-)Mathematical Background

 “intuitively”, amanifold is a (sub)space which can be mapped out using overlapping charts
(more technically, a topological space where each point has a neighbourhood which behaves
sufﬁciently like an open subset of Euclidean space to allow continuity-preserving mappings)
- a circle within a plane is a one-dimensional submanifold of a two-dimensional space
- the earth’s surface is a two-dimensional submanifold of three-dimensional space
(non-Euclidean as a whole, but locally we can approximate the structure by a plane)
 note that this notion trivially includes linear subspaces such as lines or hyperplanes!
 the placement of each point within the manifold is generally framed as an optimisation
problem which is solved by minimising a cost function of the Euclidean distance on the
embedded manifold; depending on the algorithm used, the function will includes terms such as
- differences from an arbitrary pointwise distance matrix between points
- distances between points and linear combinations of their closest neighbours
- differences from distances derived from a neighborhood graph

---

<!-- page:14 source:datsci-10-pattern-extraction.pdf -->

## Manifold Learning: Main Techniques

 multidimensional scaling (MDS) optimises for the most faithful representation of an arbitrary
distance matrix between points, abstracting over rotations, translations, and scalings
 locally linear embedding (LLE) is similar to MDS, but it only tries to preserve distances
between neighboring points (e.g. the nearest 100 neighbors of each point) by characterising
each point as a weighted sum of its neighbors and trying to preserve these relationships
 isometric mapping (Isomap) extends MDS by incorporating the geodesic distances
(by default: shortest paths) imposed by a neighbour graph with edge weights derived from
Euclidean distances, instead of using Euclidean distances directly

---

<!-- page:15 source:datsci-10-pattern-extraction.pdf -->

## Manifold Learning: Successful Multidimensional Scaling

 if the data is embedded linearly by being placed on a plane in three-dimensional space, MDS
manages to recover the underlying structure up to a rotation and reﬂection

---

<!-- page:16 source:datsci-10-pattern-extraction.pdf -->

## Manifold Learning: Failed Multidimensional Scaling

 if the data is embedded nonlinearly by being placed on a surface bent in an S-shape, MDS
fails to recover the underlying structure as it tries to maintain the distance of distant points

---

<!-- page:17 source:datsci-10-pattern-extraction.pdf -->

## Manifold Learning: Comparison of MDS and LLE on Toy Example

---

<!-- page:18 source:datsci-10-pattern-extraction.pdf -->

## Manifold Learning: Isomap on “Swiss Roll” Example Dataset

---

<!-- page:19 source:datsci-10-pattern-extraction.pdf -->

## Manifold Learning: Challenges

 major reasons why according to VanderPlas (2023), manifold learning is mostly used for
visualisation, and rarely as part of processing pipelines:
- while there are straightforward iterative approaches for dealing with missing data in PCA,
there is no good framework for this in manifold learning
- presence of noise can easily “short-circuit” or even partially collapse the manifold and
drastically change the embedding, unlike PCA which is not only robust to noise, but even
used in noise ﬁltering
- embedding result highly depends on the number of neighbors chosen, and much like
selecting the number of clusters in many clustering methods, there is no solid quantitiative
criterion for choosing an optimum number
- while PCA allows to optimise the number of output dimensions using the well-deﬁned
criterion of variance explained, the globally optimal number of dimensions in a manifold is
difﬁcult to determine
- meaning of embedded dimensions is even less clear than in PCA
(a weighted sum is not very easy to grasp intuitively, but still somewhat interpretable!)

---

<!-- page:20 source:datsci-10-pattern-extraction.pdf -->

Table of Contents
Pattern Extraction
Dimensionality Reduction
Density Estimation
Intuition and Motivation
Kernel Density Estimation

---

<!-- page:21 source:datsci-10-pattern-extraction.pdf -->

## Density Estimation Problems: General Setup

 density estimation is the task of inferring from a D-dimensional dataset an estimate
of the D-dimensional probability density function which generated the data
 this does not mean we are literally trying to infer the exact distribution of an underlying
data-generating process (most processes are far too complex for that), but that we infer a
model which matches the true process well enough to serve as an emulation of it
 for one-dimensional data, a normalised histogram can be seen as a very simple density
estimator (it allows us to see how the probability mass is distributed across possible values),
and this will also be our starting point for developing an intuitive understanding
 we already saw density estimation in model-based clustering (Gaussian Mixture Models),
though there the density estimate was an intermediate step to assigning points to clusters
 if we take the idea of Gaussian mixture modeling to an extreme and infer one Gaussian
component per point, we arrive at a nonparametric kernel estimator of density (see below)

---

<!-- page:22 source:datsci-10-pattern-extraction.pdf -->

## Role of Density Estimation in Data Science

 density estimation is an important tool for visualisation, because smooth “landscapes” are
much easier to interpret by eyeballing than “point clouds” (= scatter plots) in order to spot
- multimodality (indicating that a complex process is at work)
- skewness (indicating that data should perhaps be transformed)
 on sparse data, density estimation can be used for smoothing,
because it will assign a non-zero probability to unobserved outcomes / ranges
 a density estimate also provides a well-grounded basis for anomaly detection,
in the simplest case by ﬁltering out all observations below a certain density threshold
 model-based density estimates (such as GMMs) have the advantage of allowing sampling in
order to generate additional synthetic data which behaves similarly to the observed data
(proceed with caution – if an initial density estimate is off, this can lead to wrong conclusions!)

---

<!-- page:23 source:datsci-10-pattern-extraction.pdf -->

## Kernel Density Estimation: General Idea

 histograms have the issue that bin size and location can affect the interpretation considerably
(in the histogram to the left, the distribution looks bimodal, but unimodal in the one to the right!)

---

<!-- page:24 source:datsci-10-pattern-extraction.pdf -->

Kernel Density Estimation: General Idea
 histograms can be seen as stacks of blocks where for each point in the dataset, one block of
height 1 gets stacked within the associated bin (“on top of the data point”)
 if we do not stack aligned with the bins, but centered on each block, and measure the amount
of overlapping blocks at each point on the x-axis, we have arrived at a kernel density estimate!

---

<!-- page:25 source:datsci-10-pattern-extraction.pdf -->

## Kernel Density Estimation: Gaussian Kernel

 if we apply the same principle not to blocks (= a tophat kernel), but by adding up a Gaussian
per point, we arrive at the very popular Gaussian kernel density estimate:

---

<!-- page:26 source:datsci-10-pattern-extraction.pdf -->

## Kernel Density Estimation: Some Mathematical Background

 for a given kernel K (x; h) which depends on a distance vector x and a bandwith h,
the kernel density estimate at a point y within a group of points xi is given by
K (y) =
N∑
i=1
K (y   xi; h)
 full KDE can be quite expensive to run, advanced implementations will provide an option to
trade off computation time for accuracy (e.g. via a tree-based neighbour search heuristics)
 a KDE amounts to a very efﬁcient non-parametric generative model of the dataset:
- draw one point xi from the set of points underlying the KDE
- draw a value from the kernel associated with the point xi
 the usual caveats about the curse of dimensionality apply
(but it can be combined with dimensionality reduction!)

---

<!-- page:27 source:datsci-10-pattern-extraction.pdf -->

## Kernel Density Estimation: Practical Considerations

 one free parameter is the choice of kernel, i.e. the shape of the distribution placed at each
point; the Scikit-Learn implementation of KDE supports the following six kernels:
 the second parameter is the kernel bandwith h which controls the size of the kernel at each
point (larger bandwith means more smoothing at the cost of underestimating variance)
 hyperparameter h can be tuned by maximising log likelihoods in leave-one-out cross-validation

---

<!-- page:28 source:datsci-10-pattern-extraction.pdf -->

## Kernel Density Estimation in Scikit-Learn

 minimal example of Kernel Density Estimation from the documentation:
 the score_samples method will return the assigned (log-transformed) densities for an array
of input points, translating these scores to a colour gradient allows to render a “heat map” at
arbitrary resolutions

---

<!-- page:29 source:datsci-10-pattern-extraction.pdf -->

## Main Sources

 VanderPlas (2023): “Python Data Science Handbook, 2nd edition”,
Chapter 45: “In Depth: Principal Component Analysis”
 VanderPlas (2023): “Python Data Science Handbook, 2nd edition”,
Chapter 46: “In Depth: Manifold Learning”
 VanderPlas (2023): “Python Data Science Handbook, 2nd edition”,
Chapter 49: “In Depth: Kernel Density Estimation”
 Wikipedia (quite technical, a bit of background in mathematics required)

---

<!-- page:30 source:datsci-10-pattern-extraction.pdf -->

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

<!-- page:31 source:datsci-10-pattern-extraction.pdf -->

## Questions

Questions?
Comments?
Suggestions?

---
