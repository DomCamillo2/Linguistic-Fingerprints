---
id: "11"
title: "Statistical Inference"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-11-statistical-inference.pdf"
pages: 19
date: "2026-07-23"
---

# Session 11: Statistical Inference

> Full slide text extracted from `datsci-11-statistical-inference.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-11-statistical-inference.pdf -->

## Session 11: Statistical Inference

Johannes Dellert
23 July, 2026

---

<!-- page:2 source:datsci-11-statistical-inference.pdf -->

## Table of Contents

Hypothesis T esting
Resampling Methods
Statistical Modeling and Inference

---

<!-- page:3 source:datsci-11-statistical-inference.pdf -->

## Testable Hypotheses

- the science part of “data science” typically involves forming and testing hypotheses about
- patterns in our data that are stable against random noise
- properties of the processes we assume to have generated our data
- examples of hypotheses about data from the domain of linguistics:
- speakers are more likely to extrapose relative clauses with periphrastic tenses
- the basic vocabulary of German and Hindi is more similar than either is to that of Georgian
- the collocations in the works of author A are noticeably more similar to those in works of
author B than to those in works by other authors
- examples of hypotheses about the underlying processes:
- auxiliaries trigger extraposition by contributing to an overall sense of “heaviness”
- languages whose basic vocabulary show as many similarities as German and Hindi cannot
have arisen independently or merely through language contact
- it is more likely that author A was inﬂuenced by author B, than the other way around
- hypotheses about the data are typically investigated in terms of signiﬁcance testing
- hypotheses about the underlying processes are typically investigated through statistical
modeling and model comparison (which might in turn involve signiﬁcance testing)

---

<!-- page:4 source:datsci-11-statistical-inference.pdf -->

## Classical Statistical Tests

- in order to be able to test a hypothesis about our data, we need to be able to translate it
into a statement about one or several statistics (quantitative summaries of the data)
- if we assume that a statistic is sampled from a known distribution, we can use its observed
value to draw conclusions about the plausibility of these assumptions
- more speciﬁcally, if we have a well-understood distibution of a statistic given the truth of a
competing null hypothesis, we can measure how far the statistic differs from the values we
would expect under the null hypothesis
- examples of potentially useful statistics and relevant null hypotheses in our example cases:
- difference in percentage of extraposed clauses with and without auxiliaries; relative clauses
in periphrastic tenses are extraposed just as often as relative clauses without auxiliaries
- number of translations in a 100-concept list which exceed a certain phonetic similarity value;
the words in German, Hindi, and Georgian are generated independently
- Jaccard coefﬁcients between the results of applying a collocation extraction algorithm on
the works of both authors; the two authors are randomly selected (i.e. their works are as
similar as between an average pair of authors)

---

<!-- page:5 source:datsci-11-statistical-inference.pdf -->

## Signiﬁcance Testing

- in a classical signiﬁcance test, we reject the null hypothesis in case the probability of seeing a
value which is at least as extreme as the one we actually observed (the p-value) is lower than
a certain pre-deﬁned threshold (the signiﬁcance level α)
- the signiﬁcance level at which we consider the null hypothesis as rejected can be interpreted
as our willingness to make a type I error (where we reject the null hypothesis even if is true);
conventional choices include 1%, 2%, and 5%
- it is generally good practice to report the p-values, and let the reader decide whether they
consider them sufﬁcient evidence for rejecting the null hypothesis
- not all null hypotheses and assumptions about distributions are equally good, they can differ in
their statistical power (the probability of not making a type II error, i.e. avoiding the situation
where we fail to reject the null hypothesis although it is false)
- very important caveat in classical signiﬁcance testing: we need to always ensure that the
assumptions are compatible with the actual distributions of the data (for instance, many
classical tests assume that the relevant variables are normally distributed!)

---

<!-- page:6 source:datsci-11-statistical-inference.pdf -->

## Multiple Tests

- deciding on a given signiﬁcance threshold means that even if there are no patterns at all in the
data, in a certain percentage of tests we will erroneously reject the null hypothesis
- this implies that if we test different things long enough ( p-hacking), some test is bound to
come back as signiﬁcant, even on completely random data!
- principles of good science, all with the goal of reducing the risk of p-hacking:
- determine a single hypothesis you want to test before even looking at the data
(or only after looking at a small subset, think “development set” in machine learning)
- clean the data without your hypothesis in mind (maybe even let a different person do it)
- if you need to test several hypotheses on the same data, correct for multiple testing by
lowering the signiﬁcance threshold (e.g. Bonferroni correction, dividing the α value
by the number of tests, but this comes at the cost of decreased power, risking type II errors)
- note that this implies that exploring several hypotheses on the same dataset, as when reusing
a dataset for several studies, is always very problematic (although it cannot be avoided in
practice - for instance, there is a limited number of documented languages!)

---

<!-- page:7 source:datsci-11-statistical-inference.pdf -->

Table of Contents
Hypothesis T esting
Resampling Methods
Statistical Modeling and Inference

---

<!-- page:8 source:datsci-11-statistical-inference.pdf -->

## Resampling Methods

- a resampling method involves repeatedly drawing samples from a dataset, and repeating
some computation on many such datasets, in order to get an impression of the variability of
results against variations of the input data
- unlike most classical tests, resampling-based methods have the advantage that they are
generally nonparametric, i.e. they do not need to rely on assumptions about the underlying
distributions (though that comes at the cost of statistical power)
- resampling can also compensate to a certain degree for the problem of having to work with a
limited dataset (e.g. for every hypothesis test in typology, we should use a different resample)
- the two most commonly used resampling methods are cross-validation (known as the
standard technique for avoidance of overﬁtting in supervised machine learning) as well as
the bootstrap (much more relevant in the context of hypothesis testing)
- the two are not actually mutually exclusive: cross-validation can involve many types of
resampling, and also be performed based on bootstrap samples
(see sklearn.cross_validation.Bootstrap)

---

<!-- page:9 source:datsci-11-statistical-inference.pdf -->

## Resampling Methods: The Bootstrap

- the bootstrap is most commonly used to provide a measure of accuracy of parameter
estimates (quantifying the uncertainty arising from the structure and the size of the sample)
- basic idea: emulate obtaining new samples by sampling with replacement
from the original sample as many observations as were contained in the original sample
- with increased sample size, the resamples will be more similar to the original dataset,
whereas for smaller sample sizes, resamples will vary a lot (and contain many duplicates)
- we perform any statistical analysis we are interested in on e.g. 1000 such samples, and report
the distributions of the relevant statistics (or the percentage of resamples with a given result)
- widely applicable and extremely powerful statistical tool, as it allows to derive a measure of
variability for the outputs of any complex algorithm (example: phylogenetic tree inference)

---

<!-- page:10 source:datsci-11-statistical-inference.pdf -->

## Resampling Methods: Bootstrap Example

- example: we want to ﬁnd out whether VO word order is more marked than OV order
- assume we have some data for 12 languages from different language families
arb cmn eus evn ind jpn kor mon pol tam tha tur (5 < 7, yes?)
- then a series of Bootstrap samples might look like this (ﬁrst ﬁve in my experiment):
- sample 1: cmn evn evn ind kor kor kor kor pol tam tha tur (4 < 8, yes)
- sample 2: arb cmn cmn cmn cmn eus evn jpn kor mon tam tha (6 = 6, no)
- sample 3: arb cmn cmn eus eus evn jpn jpn mon pol tam tam (4 < 8, yes)
- sample 4: cmn cmn cmn eus evn ind ind jpn pol pol tha tur (8 > 4, no)
- sample 5: arb arb cmn jpn jpn kor kor tam tam tur tur tur (3 < 9, yes)
- we compute whatever statistic we are interested in on the basis of each bootstrap sample,
and receive a collection of e.g. 1000 values which expresses how much results might have
varied on different samples of the same size (my result: 62% of samples have |VO| < |OV|)
- this example reduced each language to a binary feature (and we could have used a binomial
test), but the same principle can be applied to much more complex objects and measures!
- important: we will not avoid biases contained in the original dataset through bootstrapping!

---

<!-- page:11 source:datsci-11-statistical-inference.pdf -->

Table of Contents
Hypothesis T esting
Resampling Methods
Statistical Modeling and Inference

---

<!-- page:12 source:datsci-11-statistical-inference.pdf -->

## Statistical Modeling and Inference

- a statistical model speciﬁes an assumed mathematical relationship between one or more
random variables and one or several non-random variables (parameters)
- Example 1: linear model which models one variable as a noisy weighted sum of others
- Example 2: Gaussian mixture model, where several Gaussians co-generated the data
- statistical inference is the estimation of model parameters which provide the best ﬁt to data
(a deﬁnition which actually includes many approaches to machine learning)
- Example 1: infer the intercept and regression coefﬁcients in a linear model
- Example 2: infer the means and covariance matrix of each distribution in a GMM
- especially in a Bayesian setting (see next slide), we do not derive point estimates (as we
generally do when training parameters in machine learning), but compatibility intervals for
parameter values, which can provide a less reductionist approach to investigating hypotheses
- in order to investigate a hypothesis about a data-generating process, we build models which
differ in the structural property that we want to investigate, and then perform model selection
by measuring which model can ﬁt the data best

---

<!-- page:13 source:datsci-11-statistical-inference.pdf -->

## Bayesian Statistics

- basic idea: deﬁne prior beliefs for the parameters, use Bayes’ theorem to compute belief
updates based on the data in order to derive posterior distributions for the parameters:
p(M|D) = p(D|M) · p(M)
p(D)
- Bayes’ theorem involves the explicit statement of the likelihood p(D|M), the probability of the
data given the parameter values, which can involve very complex computations that are often
best understood in terms of a data-generating process
- recap: Naive Bayes assumed that components of D are independent for a given model M
- in practice, the posterior distributions will almost never be directly computable as a function,
but will instead be approximated by a collection of samples from the posterior distribution
(which can be summarised in various ways to draw conclusions)
- while Bayesian inference provides more systematic approaches to many of the mentioned
problems of classical statistics (especially uncertainty), implementation can be very tricky,
and running Bayesian inference on larger models requires substantial computing resources

---

<!-- page:14 source:datsci-11-statistical-inference.pdf -->

## Bayesian Inference: Example from McElreath (2020, p. 347ff)

- goal: account for differences in the size of the tool kits of different Oceanic societies
- generative model for society i (Ti = number of tools, Pi = population, ci = contact intensity):
Ti ∼ Poisson(λi)
log λi = αci + βci log Pi
αj ∼ Normal (3, 0.5)
βj ∼ Normal (0, 0.2)
- reading: “the number of tools used by a population is Poisson-distributed with a rate whose
logarithm linearly depends on the logarithm of the population size with an intercept and
coefﬁcient sampled from different normal distributions depending on contact intensity”
- the priors for the parameters αj and βj were determined using prior predictive simulation
(running the model without any data to see whether the generated outcomes are plausible)
- to understand how much the model has learned from the data, we will typically perform
posterior predictive simulation (generating outcomes based on parameter distributions)

---

<!-- page:15 source:datsci-11-statistical-inference.pdf -->

Bayesian Inference: Example from McElreath (2020, p. 347ff)

---

<!-- page:16 source:datsci-11-statistical-inference.pdf -->

## Model Selection

- model selection is typically based on some information criterion, a measure
which balances out goodness of ﬁt against model complexity (again to avoid overﬁtting)
- many criteria exist, we are going to focus on very intuitive examples which forms the basis of
many more advanced criteria that are used a lot (such as WAIC and DIC)
- recap: the Akaike Information Criterion (AIC) is deﬁned in terms of the number k of model
parameters and the maximum likelihood ˆL of the data given the ﬁtted model: 2k − 2 ln(ˆL)
- a model is good if it assigns a high likelihood to the observed data
- more parameters are only worthwhile if each of them makes the ﬁt exponentially better
- as an alternative, the Bayes factor is the quotient of the marginal likelihoods p(D|M1) and
p(D|M2) for models M1 and M2 (each integrated over prior probabilities of the parameters)
- model complexity comes into play indirectly because a more complex model will have more
possible outcomes, or it will distribute the likelihood more evenly among outcomes
- all these measures are difﬁcult to compute on complex models, and are therefore often only
estimated based on samples (especially in Bayesian inference)
- in practice, some criterion will be reported by your modeling library,
and the important thing to understand is how to interpret the results

---

<!-- page:17 source:datsci-11-statistical-inference.pdf -->

## Main Sources

- Grus (2019): “Data Science from Scratch: First Principles with Python, 2nd edition”,
Chapter 6: “Probability”
- Grus (2019): “Data Science from Scratch: First Principles with Python, 2nd edition”,
Chapter 7: “Hypothesis and Inference”
- James ea. (2023): “Introduction to Statistical Learning”,
Chapter 5: “Resampling Methods”
- James ea. (2023): “Introduction to Statistical Learning”,
Chapter 12: “Multiple T esting”
- McElreath (2020): “Statistical Rethinking:
A Bayesian Course with Examples in R and Stan, 2nd edition”

---

<!-- page:18 source:datsci-11-statistical-inference.pdf -->

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

<!-- page:19 source:datsci-11-statistical-inference.pdf -->

## Questions

Questions?
Comments?
Suggestions?

---
