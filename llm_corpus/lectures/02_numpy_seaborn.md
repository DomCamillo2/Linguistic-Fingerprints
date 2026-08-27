---
id: "02"
title: "NumPy and Seaborn"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-02-numpy-seaborn.pdf"
pages: 27
---

# Session 2: NumPy and Seaborn

> Full slide text extracted from `datsci-02-numpy-seaborn.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-02-numpy-seaborn.pdf -->

## Session 2: Introduction to NumPy and Seaborn

Johannes Dellert
30 April, 2026

---

<!-- page:2 source:datsci-02-numpy-seaborn.pdf -->

## Table of Contents

NumPy
Purpose and Basic Usage
The Multidimensional Array
Universal Functions and Array-Oriented Programming
Pseudorandom Number Generation
File Input and Output with Arrays
NumPy for Linear Algebra
Seaborn

---

<!-- page:3 source:datsci-02-numpy-seaborn.pdf -->

## NumPy: Purpose and Basic Usage

- main uses of NumPy for data analyis:
- fast array-based operations for data munging and cleaning, subsetting and ﬁltering
- common array algorithms like sorting, unique, set operations
- efﬁcient descriptive statistics and data aggregation/summarisation
- data alignment and relational data manipulations for merging heterogeneous datasets
- conditional logic as array expressions instead of loops with if-then-else branches
- group-wise data manipulations (aggregation, transformation, function application)
- backbone of most other packages we are going to see in this course
- basic usage:
- convention for import (this is what we will assume throughout this course):
import numpy as np

---

<!-- page:4 source:datsci-02-numpy-seaborn.pdf -->

## NumPy Arrays: Creation

- the NumPy array object is much quicker and less memory-consuming than nested lists in core
Python because it places the values next to each other in memory, allowing the underlying
computations without to occur without type checking and other types of overhead
- np.arrays(data) is the main constructor, it infers the database from the structure of data
- onedimensional arrays (= row vectors) can be constructed directly from any sequence:
vec = np.array([1.5, -0.1, 3, 0, -3, 6.5])
- twodimensional arrays can be created directly from nested lists of numbers (of same length):
arr = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])
- important sources of basic information: data.ndim, data.shape, data.dtype
- np.zeros(10) and np.zeros((3, 6)), np.empty() returns uninitialized memory
(saves time if all will be ﬁlled anyway, but no guarantee of any default value)
- np.arange(15) is the numpy equivalent of range(15)
- np.ones(), np.full() with ﬁll value, np.zeros_like() [copy of same dimensions with
zeros in every entry], np.identity() for identity matrices

---

<!-- page:5 source:datsci-02-numpy-seaborn.pdf -->

## NumPy Arrays: Data Types

- possibility to specify the exact datatype,
e.g. np.float32 or np.bool for lower precision or binary matrix
- casting between types using arr.astype(np.float64),
e.g. string to ﬂoat [creates new array, i.e. potentially memory-intensive!]
- ﬁxed-length stringtype numpy.str_ (or non-Unicode numpy.string_ in older versions)
- for storing textual data of predictable length (alphanumeric IDs, standardised codes,...)
- truncation properties (assigning a longer string will lead to loss without warning)
- length of the longest strings determines default data type when creating an array from
strings, e.g. arr = np.array([”hello”, ”world”])
- variable-length strings are very inefﬁcient and must be imported explicitly:
from numpy.dtypes import StringDType
data = [”this is a longer string”, ”short string”]
arr = np.array(data, dtype=StringDType())

---

<!-- page:6 source:datsci-02-numpy-seaborn.pdf -->

## NumPy Arrays: Vectorisation and Broadcasting

- vectorisation for element-wise application (can be done between equal-sized arrays):
arr + arr, (arr * arr)
- propagating a scalar argument to each element in an array, e.g. arr * 10, (1 / arr)
- more general broadcasting (evaluating operations between differently sized arrays) is
complicated, but powerful; the elementary rules governing behaviour are as follows:
- if two arrays differ in the number of dimensions,
the shape of the one with fewer dimensions is padded with ones on its leading (left) side
- if in any dimension the shape of the two arrays does not match,
the array with shape equal to one is stretched to map the other shape
- if in any dimension the sizes disagree and neither is equal to 1,
the operation is not possible, and an error is raised instead

---

<!-- page:7 source:datsci-02-numpy-seaborn.pdf -->

## NumPy Arrays: Indexing and Slicing

- slicing as view on the original array (unlike Python, were slicing means copying;
arr[x:y].copy() for the original Python behaviour)
- broadcast when assigning scalar value to a slice (instead of T ypeError)
- comma-separated list of indices to select individual elements in multidimensional array
(arr[x, y] instead of arr[x][y] for nested lists)
- subarray extraction like arr3d[3] or arr3d[1, 0]
(again, views of the original array; not possible using nested list representation)
- slicing along axes, e.g. arr2d[:2] “select ﬁrst two rows”
- multiple slices can be performed simultaneously: arr2d[:2, 1:]
- with an index, we receive a lowerdimensional slice arr2d[1,:2]
- arr[:,:1] for slicing the ﬁrst column (but keeping the dimension)
- note the difference between shapes (2,) and (1,2),
e.g. difference between arr[1,:2] and arr[1:2,:2]

---

<!-- page:8 source:datsci-02-numpy-seaborn.pdf -->

## NumPy Arrays: Boolean Indexing and Filtering

- comparison between arrays ( arr2 > arr ) yields Boolean arrays
- assume we have a vector names of names for each row in data
- Boolean indexing: names == ”Bob”, data[names == ”Bob”],!= or ~( == ) [~for
inverting a Boolean array], &, | [NOT the usual python operators and and or]
- example of combination with broadcasting:
data[data < 0] = 0 to set all negative values to 0
- fancy indexing: indexing using integer arrays, e.g. arr[[4, 3, 0, 6]]
- multiple index array for selection corresponding to each tuple of indices; for instance,
arr[[1, 0], [5, 2]] will result in array containing arr[1, 5] and arr[0, 2]
- arr[l1][:,l2] for selecting subset of rows and columns instead

---

<!-- page:9 source:datsci-02-numpy-seaborn.pdf -->

## NumPy Arrays: Sorting and Searching

- arr.sort() sorts in place
- arr.sort(axis=0) sorts values within each column
- arr.sort(axis=1) sorts values across each row
- arr.argsort() returns the indices that would sort an array
(important for sorting by a certain column, can be called twice to receive ranks)
- np.sort(arr) returns sorted copy of the array (like built-in sorted())
- np.unique(arr) returns (by default) a sorted array with the unique elements
- np.in1d(values, arr) returns Boolean vector whether each value is in arr
- np.intersect1d(x, y): sorted, common elements
- np.union1d(x, y): sorted union of elements

---

<!-- page:10 source:datsci-02-numpy-seaborn.pdf -->

## Vectorisation and Universal Functions

- NumPy arrays make array expressions available for many kinds of data processing tasks
which would otherwise require loops; this is called vectorisation
- universal functions or ufuncs are the NumPy term for fast element-wise array functions
- examples of useful unary universal functions:
- np.sqrt(arr)
- np.exp(arr)
- np.log(arr)
- np.cos(arr)
- examples of useful binary universal functions:
- np.add(arr1, arr2)
- np.multiply(arr1, arr2)
- np.greater(arr1, arr2)
- np.maximum(arr1, arr2)

---

<!-- page:11 source:datsci-02-numpy-seaborn.pdf -->

## Array-Oriented Programming

- evaluate function across regular grid of values, ﬁnd minimum (grid search)
- points = np.arange(-5, 5, 0.01)
- xs, ys, zs = np.meshgrid(points, points, points)
- vals = np.sqrt(xs ** 2 + ys ** 2 + zs ** 2)
- min = np.argmin(vals, keepdims=True)
- np.where(cond, xarr, yarr) is a vectorised version of x if condition else y
- xarr and yarr can also be scalars
- typical usecase: np.where(arr > 0, 2, -2) creates a copy of arr
where all positive values are replaced by 2 and all negative values by -2
- for the equivalent of a condition without an else clause, we can just put the original array
into the third argument, for example np.where(arr > 0, 2, arr)

---

<!-- page:12 source:datsci-02-numpy-seaborn.pdf -->

## Pseudorandom Numbers with np.random

- more efﬁcient generation of whole arrays of sample values from many kinds of distributions:
- np.random.uniform() for uniform sampling from an interval
- np.random.integers() for uniformly sampled integers from some range
- np.random.binomial(), np.random.normal(), np.random.beta()
- all of these are vectorised, e.g. np.random.standard_normal(size=(4,4))
- fast implementations of probabilistic utility functions:
- np.random.permutation() for generating permuted copies
- np.random.shuffle() for in-place permutation
- a pseudorandom number generator with a seed will always generate the same sequence of
numbers (good practice for reproducibility!)
- rng = np.random.default_rng(seed=12345)
- rng.standard_normal() etc.

---

<!-- page:13 source:datsci-02-numpy-seaborn.pdf -->

## Linear Algebra

- efﬁcient implementations of standard operations from linear algebra are available out of the
box (though of course, deep learning libraries with GPU support are even faster):
- Matrix multiplication is written x.dot(y) or np.dot(x,y) or x @ y
- transpose mtx.T (swaps axes)
- inverse np.linalg.inv(mtx) (implements reverse of the linear transformation)
- QR decomposition np.linalg.qr(mtx) (orthonormal times upper triangular matrix)
- trace np.linalg.trace(mtx) (sum of diagonal elements)
- determinant np.linalg.det(mtx) (“volume compression factor” of transformation)
- eigenvalues and eigenvectors np.linalg.eig(mtx) (“invariants” of transformation)
- np.linalg.solve(amtx, bvect) for solving set Ax = b of linear equations
- there are further subpackages for other often-needed types of mathematics:
- np.polynomials for polynomials
- np.fft for basic functionality around Fourier transform

---

<!-- page:14 source:datsci-02-numpy-seaborn.pdf -->

Table of Contents
NumPy
Seaborn
Role and Basic Usage
Histograms and Joint Distributions
Categorical Plots

---

<!-- page:15 source:datsci-02-numpy-seaborn.pdf -->

## Matplotlib and the Role of Seaborn

- Matplotlib (standard library for scientiﬁc visualisation in Python, you have probably used it),
while extremely popular and feature-rich, is taken to have a range of undesirable properties:
- API is quite low-level; all kinds of sophisticated visualisations are possible, but simple
standard visualisations often require large amounts of boilerplate code
- color and style defaults look dated (though this has been improved in recent versions)
- Seaborn (which we will explore for visualisation) solves these issues:
- API on top of Matplotlib which offers more modern default choices for plot styles and colours
- simple high-level functions for common statistical plot types (which we will cover today)
- Matplotlib proper is adapting, and might regain its status as the tool of choice in the future
- Seaborn is primarily intended for effortless plotting of standard datatypes during data
exploration; for full customisability and publication-quality visualisations, dropping down into
the underlying Matplotlib functionality for ﬁne-grained tweaking is necessary
- NOTE: a major advantage of Seaborn is its integration with Pandas, which we have not
introduced yet; the examples you will see on the next slides will use this functionality in minor
ways; but Seaborn can be used on Numpy arrays as well

---

<!-- page:16 source:datsci-02-numpy-seaborn.pdf -->

## Seaborn: Installation Basic Usage

- installation should work in the usual fashion (assuming you work from Jupyter):
In []!pip install seaborn
- switch to matplotlib mode for inline visualisations, and conventions for imports:
In [] %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
- Seaborn should be initialised with a chart style, this is the default Matplotlib reconﬁguration:
In [] sns.set()
- outside matplotlib mode, visualisations need to be opened explicitly (separate window!):
In [] plt.show()

---

<!-- page:17 source:datsci-02-numpy-seaborn.pdf -->

## Matplotlib: Histogram Example

---

<!-- page:18 source:datsci-02-numpy-seaborn.pdf -->

## Seaborn: Smooth Density Estimates

- Seaborn one-liner for smooth estimate based on kernel density estimation (Session 12)

---

<!-- page:19 source:datsci-02-numpy-seaborn.pdf -->

## Seaborn: Two-Dimensional Smoothed Joint Density

- by passing column names as dimensions, we get a 2D visualisation of joint density:

---

<!-- page:20 source:datsci-02-numpy-seaborn.pdf -->

## Categorical Plots: Factor Plot

- a factor plot shows the distribution of a parameter within bins deﬁned by some other parameter

---

<!-- page:21 source:datsci-02-numpy-seaborn.pdf -->

## Categorical Plots: Joint Distributions

- joint distribution along with associated marginal distributions are shown by jointplot:
sns.jointplot(x=”total_bill”, y=”tip”, data=tips, kind=kind)
kind=’hex’ yields hexes for joint density:
 kind=’reg’ yields KDEs and regression:

---

<!-- page:22 source:datsci-02-numpy-seaborn.pdf -->

## Categorical Plots: Bar Plots

- to illustrate more general bar plots, we use the Planets dataset, which contains data about
known exoplanets along with the year and the method of their discovery

---

<!-- page:23 source:datsci-02-numpy-seaborn.pdf -->

Categorical Plots: Bar Plots
- we create a bar plot of the number of planets discovered each year, classiﬁed by the methods
of discovery (keyword hue with column ID, because bars are distinguished by their colour)

---

<!-- page:24 source:datsci-02-numpy-seaborn.pdf -->

## Categorical Plots: Swarm and Violin Plots

sns.catplot(data=tips, kind=kind, x=”day”, y=”total_bill”, hue=”smoker”)
with kind=”swarm”:
 with kind=”violin”:
 with kind=”bar”:

---

<!-- page:25 source:datsci-02-numpy-seaborn.pdf -->

## Categorical Plots: Scatter Plots

---

<!-- page:26 source:datsci-02-numpy-seaborn.pdf -->

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

<!-- page:27 source:datsci-02-numpy-seaborn.pdf -->

## Questions

Questions?
Comments?
Suggestions?

---
