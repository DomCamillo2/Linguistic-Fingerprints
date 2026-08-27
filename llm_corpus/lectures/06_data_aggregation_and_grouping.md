---
id: "06"
title: "Data Aggregation and Grouping"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-06-data-aggregation-and-grouping.pdf"
pages: 29
---

# Session 6: Data Aggregation and Grouping

> Full slide text extracted from `datsci-06-data-aggregation-and-grouping.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Session 6: Data Aggregation and Grouping

Johannes Dellert
18 June, 2026

---

<!-- page:2 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Table of Contents

Data Aggregation and Grouping: Overview
Grouping
Data Aggregation
Apply
Pivot T ables and Cross-T abulation

---

<!-- page:3 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Data Aggregation and Grouping: Overview

- data analysis workﬂows often involve spliting a dataset into categories and applying a function
to each group (e.g. computation of group statistics, comparison of groups, visualisation)
- Python and Pandas provide an interface for quite complex group operations
involving arbitrary manipulations through custom functions
- this session introduces some central capabilities in this area:
- splitting Pandas objects into pieces using one or more keys of various types
- calculating group summary statistics like count, mean, or standard deviation
- applying within-group transformations (normalisation, ranking, subset selection)
- computing pivot tables and cross-tabulations
- quantile analysis and other statistical group analyses

---

<!-- page:4 source:datsci-06-data-aggregation-and-grouping.pdf -->

Table of Contents
Data Aggregation and Grouping: Overview
Grouping
Data Aggregation
Apply
Pivot T ables and Cross-T abulation

---

<!-- page:5 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Group Operations: Motivation

- group operations can be described in terms of a split-apply-combine sequence
- data contained in a pandas object is split into groups along one axis
(rows or columns) based on one or more keys we provide
- some function is applied to each group, producing a new value
- the results of those function applications are combined into a result object,
the form of which will depend on what we have been doing to the data
- grouping keys can take many forms, and do not have to be all of the same type:
- list or array of values of the same length as the axis being grouped
- value indicating a column name in a DataFrame
- dictionary or Series deﬁning a correspondence between the values
on the axis being grouped, and the names of the resulting groups
- function to be invoked on the axis index or individual labels in it

---

<!-- page:6 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Group Operations: Illustration

---

<!-- page:7 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Group Operations: Splitting into Groups

- data.groupby(keys) expects an array providing the group indices of each row, and returns
a GroupBy object which summarises all the information needed to apply some operation
(e.g. mean, sum, size, count) to each of the groups it represents
- example on a database of languages (continuing our previous running example):
grouped = df["num_speakers"].groupby(df["family"])
grouped.mean()
(computes and prints the average number of speakers for each family)
- passing a list of arrays leaves us with a hierarchical index over the result Series:
df["num_speakers"].groupby([df["family"],df["subfamily"]]).mean()
- if the grouping information is found in the same dataframe, this can be shortened by only
passing the column names:
df["num_speakers"].groupby(["family", "subfamily"]]).mean()
- if we call groupby on a dataframe, columns to which the function
cannot be applied will be treated as nuisance columns, i.e. excluded from the result
- the same is true for missing values in a group key (such rows will be discarded)

---

<!-- page:8 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Group Operations: Iterating over Groups

- GroupBy objects support iteration, generating a sequence of 2-tuples
consisting of the group name and the chunk of data the name refers to
- in case of multiple keys, the ﬁrst element will be a tuple of key values
(in our example, pairs of shape (family, subfamily) )
- it often makes sense to store the data pieces in a dictionary with the group names as keys:
pieces = {name: group for name, group in df.groupby("key1")}

---

<!-- page:9 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Group Operations: Selection by Columns

- by default, groupby groups on axis="index", but we can group on any axis
- using the axis parameter, we can group columns instead of rows:
df.groupby({"col1": "a", "col2": "a", "col2": "b"}, axis="columns")
- GroupBy objects can be indexed by a column name or array of column names:
df.groupby("key1")["data"] is the same as df["data"].groupby(df["key1"])
- to only aggregate a few columns (e.g. to save computation time on a large dataset),
we can index the GroupBy object with an array of column names:
df.groupby(["key1", "key2"])[["data1", "data2"]].mean()
- the type of the object returned depends on how we performed column selection:
- if we only pass a single column name, the result is a grouped Series
- if we pass an array of column names, the result is a grouped DataFrame

---

<!-- page:10 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Grouping with Dictionaries and Series

- instead of lists of column names, we can also create a mapping from column names
to group ids, and use it as the ﬁrst argument to groupby together with the axis speciﬁcation:
df.groupby(mapping, axis="columns")
- the mapping can be implemented
- as a Python dictionary, e.g. {"col1": "g1", "col2": "g2", "col3": "g3"}
- as a Series, which (as we did before) can be viewed as a ﬁxed-size mapping as well
col1 g1
col2 g2
col3 g1
dtype: object

---

<!-- page:11 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Grouping with Functions

- a function passed as a group key will be called once per index value,
and the return values will be used as the group names
- as a simple example, assume a dataframe which uses words as index values
- we can pass the len function as the group key
- the data will be aggregated per word length
- functions can be freely mixed with arrays, dictionaries, or Series as group keys
(all options will be converted into arrays internally)
- we could use an additional series which classiﬁes words by their etymology
(Germanic or Romance), and get our data grouped by both:
In [ ]: df.groupby([len, etymology]).sum()
Out[ ]:
freq
2 Germanic 453
3 Germanic 2458
3 Romance 120
4 Germanic 5678
4 Romance 2345

---

<!-- page:12 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Grouping by Index Levels

- ﬁnally,groupby allows us to aggregate using one of the levels of an axis index
by passing a level number or name using the level keyword
- in our hierarchical indexing example from Session 5, we could have avoided the trouble of
swapping levels by calling data.groupby() on an inner level:
>>> data
subject GL CL
gender m f m f
level year
BA 1 41 68 77 67
2 60 26 28 16
3 15 30 49 34
MA 1 68 75 50 58
2 30 47 51 63
>>> data.groupby(level="year").sum()
subject GL CL
gender m f m f
year
1 109 143 127 125
2 90 73 79 79
3 15 30 49 34

---

<!-- page:13 source:datsci-06-data-aggregation-and-grouping.pdf -->

Table of Contents
Data Aggregation and Grouping: Overview
Grouping
Data Aggregation
Apply
Pivot T ables and Cross-T abulation

---

<!-- page:14 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Data Aggregation: Optimised GroupBy Methods

- an aggregation is the term for any data transformation which produces
scalar values from arrays (such as the usual summary statistics)
- the implementations of many aggregations are optimised for use with GroupBy objects:
all True if all non-NA values are “truthy”
any True if one or more values are “truthy”
count number of non-NA values
mean mean of non-NA values
median arithmetic median of non-NA values
min minimum of non-NA values
max maximum of non-NA values
nth value that would appear at position n with data in sorted order
quantile computes sample quantile, i.e. rank divided by size
rank ordinal ranks of non-NA values
size computes group sizes, returning result as a Series
sum sum of non-NA values
std computes sample standard deviation
var computes sample variance

---

<!-- page:15 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Data Aggregation: Custom Functions

- beyond these highly optimised standard functions, any method which is deﬁned on the object
being grouped can be used as custom aggregation
- Example: grouped.nsmallest(2) will slice up the Series into pieces,
apply piece.nsmallest(2) on each piece, and then assemble the results
- describe works as well (though not technically an aggregation)
- to execute a custom aggregation function, we can pass any function that aggregates an array
to the aggregate methods (or its alias agg of the GroupBy object)
- Example:
In [ ]: def peak_to_peak(arr):
...: return arr.max() - arr.min()
In [ ]: grouped.agg(peak_to_peak)
- both options are generally much slower than the optimised methods because of
the extra overhead involved in constructing intermediate group data chunks

---

<!-- page:16 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Data Aggregation: Column-Wise and Multiple Function Application

- agg also supports aggregation by functions which differ per column
- Example: grouped.agg(["similarity": np.max, "size": "sum"])
- result will have maximum in-group similarities in the similarity column,
and group totals in the size column
- ﬁnally, we can aggregate by multiple functions at once:
- Example: grouped.agg(["mean", "std", peak_to_peak])
- result will be a DataFrame with function names as column names
- if grouped deﬁned more than one group of columns,
this will be reﬂected by a hierarchical column index in the resulting DataFrame

---

<!-- page:17 source:datsci-06-data-aggregation-and-grouping.pdf -->

Table of Contents
Data Aggregation and Grouping: Overview
Grouping
Data Aggregation
Apply
Pivot T ables and Cross-T abulation

---

<!-- page:18 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Apply: Basic Split-Apply-Combine Pattern

- apply is the most general-purpose GroupBy method
- splits the object being manipulated into pieces
- invokes the passed function on each piece
- then attempts to concatenate the pieces
- function must either return a Pandas object or a scalar value
- if the function passed takes other arguments or keywords,
they can be passed to apply after the function

---

<!-- page:19 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Example: Quantile and Bucket Analysis (McKinney 2022, p. 338f)

- creating a dataframe with 1000 observations of two normally distributed variables:
- creating the quartiles ( pd.cut would have created buckets):

---

<!-- page:20 source:datsci-06-data-aggregation-and-grouping.pdf -->

Example: Quantile and Bucket Analysis (McKinney 2022, p. 338f)
- function for extracting desired group statistics:
- grouping by the quartiles and extracting statistics per group:

---

<!-- page:21 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Example: Group Weighted Average and Correlation (McKinney 2022, p. 344f)

- generating a toy dataset of normally distributed data along with random weights
(these could be conﬁdence values or sizes of contributions to a mixture):
- deﬁning the weighted average function and applying it to the two groups:

---

<!-- page:22 source:datsci-06-data-aggregation-and-grouping.pdf -->

Table of Contents
Data Aggregation and Grouping: Overview
Grouping
Data Aggregation
Apply
Pivot T ables and Cross-T abulation

---

<!-- page:23 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Pivot Tables

- a pivot table
- aggregates a table of data by one or more keys
- arranges data in rectangle with some keys along the rows and some along the columns
- they are possible in Pandas through groupby in combination with the reshape operations
based on hierarchical indexing we introduced in Session 6
- convenience method df.pivot_table can add partial totals ( margins)
- basic usage: df.pivot_table(index=["col1", "col3"]) creates hierarchical index,
and by default provides the group means for the remaining columns
- main arguments of df.pivot_table:
- values: column name(s) to aggregate; all numeric columns by default
- index: column names or group keys to group on rows of resulting pivot table
- columns: column names or group keys to group on columns of resulting pivot table

---

<!-- page:24 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Pivot Tables: Example from McKinney (2022), p. 352f

- remember the tips dataset we used in the introduction to Seaborn:
- example of a simple pivot table (averages by day and smoker status)

---

<!-- page:25 source:datsci-06-data-aggregation-and-grouping.pdf -->

Pivot Tables: Example from McKinney (2022), p. 352f
- example of a more complex pivot table which groups by time, but only two values:

---

<!-- page:26 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Pivot Tables: Options

- the pivot_table method is very ﬂexible thanks to a range of additional options:
- aggfunc allows to override the default aggregation function ( mean) with any aggregation
function valid in a groupby context (see above for options and example)
- dropna=True prevents inclusion of columns whose entries are all null values
- fill_value speciﬁes how to replace missing values in the result table (mean 0?)
- margins=True adds rows and columns with the subtotals for the outermost levels
- margins_name allows to specify the names for the margin columns/rows (default All)
- observed_keys=True hides the unobserved category values in the keys

---

<!-- page:27 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Cross-Tabulation

- a cross-tabulation is a special case of a pivot table that computes group frequencies
- pd.crosstab takes two (lists of) Series with a shared index as arguments:
- the ﬁrst will form the (hierarchical) row index
- the second the (hierarchical) column index
- Example from McKinney (2022) expanding on the pivot table examples:

---

<!-- page:28 source:datsci-06-data-aggregation-and-grouping.pdf -->

## Cross-Tabulation: Example from McKinney (2022), p. 354f

- small toy dataframe with the following structure (5 of 10 entries shown):
- let’s cross-tabulate nationality with handedness, and marginalise as well:

---

<!-- page:29 source:datsci-06-data-aggregation-and-grouping.pdf -->

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
