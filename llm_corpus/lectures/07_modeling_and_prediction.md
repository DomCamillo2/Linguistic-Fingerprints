---
id: "07"
title: "Modeling and Prediction"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-07-modeling-and-prediction.pdf"
pages: 28
date: "2026-06-25"
---

# Session 7: Modeling and Prediction

> Full slide text extracted from `datsci-07-modeling-and-prediction.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-07-modeling-and-prediction.pdf -->

## Session 7: Modelling and Prediction

Johannes Dellert
25 June, 2026

---

<!-- page:2 source:datsci-07-modeling-and-prediction.pdf -->

## Table of Contents

Recap: Basic Statistics and Probability
Statistical Modelling
Model Development Workﬂow

---

<!-- page:3 source:datsci-07-modeling-and-prediction.pdf -->

## Recap: Statistics and Probability

 must-know concepts from basic statistics:
- central tendency: mean, mode, median, quantiles
- dispersion: range, variance, standard deviation
- covariance, Pearson correlation
- Simpson’s paradox (Grus 2019, p. 67)
 must-know concepts from basic probability theory:
- joint probability, dependence and independence
- conditional probability and Bayes’ Theorem
- random variable, expected value
- continuous distribution
- probability density function and cumulative distribution function
- normal distribution
- Bernoulli distribution and binomial distribution
- multivariate normal distribution (location and covariance matrix)
- joint density and marginal density

---

<!-- page:4 source:datsci-07-modeling-and-prediction.pdf -->

Table of Contents
Recap: Basic Statistics and Probability
Statistical Modelling
Model Development Workﬂow

---

<!-- page:5 source:datsci-07-modeling-and-prediction.pdf -->

## Statistical Modelling

 throughout the past weeks, we have built (or refreshed) some skills in getting the data into
useful shapes, and performing some basic analysis and visualisation tasks on them
 but to actually answer a scientiﬁc question which furthers our understanding of a domain,
we will need to develop theories of how the data came about, and test these theories
 in general, we can only be conﬁdent that we understand how a domain works if we can create
an explicit model of it, which allows us to make predictions about unseen data
 the quality of a model (whether statistical or formal) can be evaluated by seeing how good it is
at predicting unseen data (completely new or masked during development and parameter
inference), or how well it predicts the data given its complexity (e.g. information criteria)
 building a good model almost always involves picking from a large set of possible model
architectures, and then solving an optimisation problem in order to pick parameter values
which provide the best ﬁt of the model to the data (depending on the tradition,
this is called statistical inference or machine learning)
 quick question round: what is overﬁtting? precision and recall? what are features?
development set, training set, test set? cross-validation? known model types?

---

<!-- page:6 source:datsci-07-modeling-and-prediction.pdf -->

Table of Contents
Recap: Basic Statistics and Probability
Statistical Modelling
Model Development Workﬂow
The Patsy Library
Introduction to statsmodels
Introduction to scikit-learn

---

<!-- page:7 source:datsci-07-modeling-and-prediction.pdf -->

## From Pandas to Modelling

 many statistical problems can be solved using simple techniques (like linear regression),
other problems may require more advanced machine learning methods
 common workﬂow for model development for any type of model: use pandas for data loading
and cleaning, then switch to modelling library to build the model itself
 point of contact is usually NumPy arrays; feature engineering is performed to extract
numerical representation from the data, which are then fed into the modelling library
 important method for conversion: data.to_numpy() [indexes are stripped away!]
 often, the names need to be converted into the relevant model parameter names
(though some libraries have support for automatically extracting them from Pandas indices)

---

<!-- page:8 source:datsci-07-modeling-and-prediction.pdf -->

## Patsy Library

 a (multivariable) linear model assumes that values of a dependent variable can be predicted
as linear combinations of predictor values plus an intercept: yi = xi1
1 + xi2
2 +    + xtK
K + ϵi
 in matrix notation, this can be written in terms of a design matrix X:
y = X
 + ϵ
 Patsy library (part of the statsmodels package, see below) describes linear models in
string-based formula syntax, e.g. y, X = patsy.dmatrices('y ~ x0 + x1', data)
 data typically is a Pandas dataframe where the variables of the formula are column names
 y and X are DesignMatrix objects which combine an ndarray with additional metadata,
which can be accessed (and retrieved) via e.g. y.design_info.column_names
 in order to perform model ﬁtting, Patsy objects can be passed directly into algorithms like
numpy.linalg.lstsq (NumPy implementation of ordinary least squares regression)
 Patsy formulas can include Python code; function deﬁnitions will be retrieved from the
enclosing scope, but there are inbuilt ones for the most frequent types of transformations
(e.g. standardize(x) for mean and variance 0 or center(x) for subtracting the mean)

---

<!-- page:9 source:datsci-07-modeling-and-prediction.pdf -->

## Patsy: Introductory Example from McKinney (2022)

---

<!-- page:10 source:datsci-07-modeling-and-prediction.pdf -->

## Patsy: Categorical Data Example

 nonnumeric terms in a Patsy formula are converted to dummy variables by default
 in order to have columns for each category value in the design matrix (and not one less),
the intercept needs to be omitted by adding “ + 0 ” to the formula

---

<!-- page:11 source:datsci-07-modeling-and-prediction.pdf -->

## Patsy: Interaction Term Example

 Patsy supports interaction terms with the colon notation ( x1:x2)
 this allows the model to assign a different value to any combination of categorical terms

---

<!-- page:12 source:datsci-07-modeling-and-prediction.pdf -->

## The statsmodels library

 statsmodels is a very straightforward library for ﬁtting many kinds of classic statistical
models, with some integrated support for data exploration and visualisation
 it mainly supports the traditional frequentist statistical methods, including
- linear models (modeling a continuous variable as a linear combination of predictors)
- generalised linear models (GLMs) (modeling a variable as generated by a distribution
from the exponential family, parametrised by a linear combination of predictors)
- logistic regression (GLM with a categorical distribution, allowing to predict
a categorical variable from a linear combination of predictors)
- robust linear models (ﬁtted with loss functions that are less sensitive against outliers)
- linear mixed effects models (sum of linear combinations of ﬁxed and random effects)
- Analysis of Variance (ANOVA) methods (linear models involving interaction terms
ﬁtted under certain assumptions of independence and homoscedasticity)
- generalised methods of moments
- time series processes and state space models

---

<!-- page:13 source:datsci-07-modeling-and-prediction.pdf -->

## Frequentist Statistics: Overview (University of Dundee)

---

<!-- page:14 source:datsci-07-modeling-and-prediction.pdf -->

## Frequentist Statistics: Overview (Brian Y uen, University of Southampton)

---

<!-- page:15 source:datsci-07-modeling-and-prediction.pdf -->

## The statsmodels library: Basic Usage

 installation (recommended): conda install statsmodels
 convention for import: import statsmodels as sm
 functions for statistical tests are in sm.stats
- sm.stats.gof has goodness of ﬁt tests and measures
- sm.stats.multivariate has functions for multivariate samples
- sm.stats.oneway has functions for one-way ANOVAs
- sm.stats.weightstats has basic statistics and tests for means
- sm.stats.tsa has models for time series analysis
- many more submodules!
 different types of models are organised into ﬁrst-order submodules, e.g.:
- sm.genmod implements Generalised Linear Mixed Effects Models
- sm.gmm implements the Generalised Method of Moments
- sm.multivariate has various algorithms from multivariate statistics
 the library is very comprehensive, and the documentation can be a bit technical;
no worries about using other sources in order to ﬁnd examples or more information

---

<!-- page:16 source:datsci-07-modeling-and-prediction.pdf -->

## statsmodels Example: Running a Statistical Test

 assume that we have samples of a normally distributed variable from two populations, and
would like to know whether the populations can be assumed to have different means
y1 = np.random.normal(0, 1, 10) #mean in example run was -0.144
y2 = np.random.normal(0, 1, 10) #mean in example run was 1.121
 the overview charts tell us that an independent samples t-test is what we need here
 searching in the statsmodels documentation, we ﬁnd that this is how we perform the test:
from sm.stats.weightstats import ttest_ind
tstat, pvalue, df = ttest_ind(y1, y2, alternative='two-sided')
 in the example run (results will differ with new random data!)
- the t statistic evaluated to -2.517 at 18 degrees of freedom
- the p-value was 0.022, which means that we reject the null hypothesis of identical means!
 caution: traditional tests always come with strong assumptions which you have to check on
real data (cf. your introduction to statistics, or the documentation of tests you are considering)

---

<!-- page:17 source:datsci-07-modeling-and-prediction.pdf -->

## statsmodels Example: OLS Linear Regression

 linear models are deﬁnable through two main interfaces: array-based (you manipulate the
design matrix directly) and formula-based (as in Patsy); they are imported like this:
 for illustration, we work with a Pandas dataframe of the following shape:
 we perform ordinary least squares regression with a linear model deﬁned through a formula:

---

<!-- page:18 source:datsci-07-modeling-and-prediction.pdf -->

## statsmodels Example: Interpreting the Results

 the result object allows us to retrieve the ﬁtted coefﬁcients (the
 vector) as well as their
t-values ( number of standard deviations by which the coefﬁcient differs from zero)

---

<!-- page:19 source:datsci-07-modeling-and-prediction.pdf -->

## statsmodels Example: Basic Criteria of Regression Model Quality

 results.summary() prints detailed diagnostic output of the model
 this includes standard deviations for all coefﬁcients to quantify the uncertainty
 key measures which allow you to assess the quality of the model:
- R-Squared (R2), also called the coefﬁcient of determination, measures the proportion of
the variation in the dependent variable which is predictable from the predictor variables
(this can be interpreted roughly like a correlation, the best possible result is 1)
- the F statistic measures how much better the current model ﬁts the data than a model
without predictor variables; a low associated p-value suggests the model is a good ﬁt
- the log likelihood approximates the probability of seeing the data given the estimated
parameters; higher is better because likelihood is proportional to probability of parameters
given the data (only useful between models with equal numbers of predictor variables!)
- the Akaike Information Criterion (AIC) 2k   2 ln(^L) balances out number of parameters k
with the maximum likelihood ^L (lower is better, can compare models of different complexity)
- the Bayes Information Criterion (BIC) is derived from the maximum likelihood as well, but
it penalises free parameters more, thus showing a stronger preference for simple models

---

<!-- page:20 source:datsci-07-modeling-and-prediction.pdf -->

## statsmodels Example: Using the Model for Prediction

 the results object also allows you to directly run the model on new data:
 these are the values of the dependent variable which are predicted as the linear combination
of predictor variable values with the ﬁtted coefﬁcients; we can compare them to actual values
 this is useful for more general evaluation of model ﬁt (performance on held-out data,
as is standard in machine learning, e.g. in the shape of cross-validation)

---

<!-- page:21 source:datsci-07-modeling-and-prediction.pdf -->

## The scikit-learn library

 most widely used general-purpose Python machine learning toolkit
(as opposed to specialised toolkits for neural models such as PyT orch)
 broad selection of standard supervised and unsupervised machine learning methods
(almost everything we are going to need for this course, with a uniﬁed interface)
- prediction (i.e. regression models)
- classiﬁcation (Session 08)
- clustering (Session 09)
- dimensionality reduction (Session 10)
 additional tooling for
- model selection and evaluation
- data transformation
- data loading
- model persistence
 installation (recommended): conda install scikit-learn
 available under the module name sklearn

---

<!-- page:22 source:datsci-07-modeling-and-prediction.pdf -->

## scikit-learn: Algorithm Cheat Sheet

---

<!-- page:23 source:datsci-07-modeling-and-prediction.pdf -->

## scikit-learn: Basic Usage

 setting up and training any of the many models available through scikit-learn always
follows the same basic recipe (illustrated here for the case of linear regression)
 ﬁrst, we split our data into training and test data, and transform the relevant values of predictor
variables and the output variables into two NumPy arrays X and y, which we then split into a
training set and a test set: X_train, y_train, X_test, y_test
 we import the class which implements the model:
from sklearn.linear_model import LinearRegression
 we create an instance of the model (with potential hyperparameters as arguments):
model = LinearRegression()
 then, we ﬁt the model to the NumPy arrays specifying training inputs and outputs:
model.fit(X_train, y_train)
 now, we can perform prediction on our test data:
y_predict = model.predict(X_test)
 we analyse the prediction quality of our model by comparing y_predict to y_test

---

<!-- page:24 source:datsci-07-modeling-and-prediction.pdf -->

## Logistic Regression

 logistic regression is a standard technique when the dependent variable is binary
 it works just like linear regression, except that the weighted sum is transformed through the
logit function logit(p) = ln
(
p
1 p
)
, and goodness of ﬁt is measured as negative log-likelihood
 the continuous output is between 0 and 1, which can be interpreted as the predicted
probability of either label, and setting a threshold at 0.5 turns it into a binary predictor
 to avoid overﬁtting, regularisation (penalisation of large coefﬁcient values) is needed; this is
done by adding a penalty term to the cost function, which is weighted by a regularisation
strength parameter  (or its inverse C, smaller values mean stronger regularisation)
 sklearn.linear_model.LogisticRegression implements this
(using exactly the same interface as the example model from the previous slide!)

---

<!-- page:25 source:datsci-07-modeling-and-prediction.pdf -->

## scikit-learn: Cross-Validation

 overﬁtting to the training data is typically avoided by cross-validation, where we reserve
varying parts of the training data as test data in order to simulate out-of-sample prediction
 many scikit-learn models have estimator classes with built-in cross-validation
(recognisable by the sufﬁx CV) in order to optimise model regularisation parameters:
 alternatively, there is a cross_val_score helper function which handles the data splitting:

---

<!-- page:26 source:datsci-07-modeling-and-prediction.pdf -->

## Sources

 good programming-oriented recaps of statistics and probability concepts
are in Grus (2019): “Data Science from Scratch: First Principles with Python”
 much of this presentation was a summary of Chapter 12
in McKinney (2022): “Python for Data Analysis”, enhanced by
further information from the online documentation of statsmodels and scikit-learn

---

<!-- page:27 source:datsci-07-modeling-and-prediction.pdf -->

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

<!-- page:28 source:datsci-07-modeling-and-prediction.pdf -->

## Questions

Questions?
Comments?
Suggestions?

---
