---
id: "05"
title: "Data Wrangling"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-05-data-wrangling.pdf"
pages: 30
---

# Session 5: Data Wrangling

> Full slide text extracted from `datsci-05-data-wrangling.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-05-data-wrangling.pdf -->

## Session 5: Data Wrangling – Join, Combine, Reshape

Johannes Dellert
11 June, 2026

---

<!-- page:2 source:datsci-05-data-wrangling.pdf -->

## Table of Contents

Data Wrangling: Overview
Hierarchical Indexing
Combining and Merging Datasets
Reshaping and Pivoting

---

<!-- page:3 source:datsci-05-data-wrangling.pdf -->

## Data Wrangling: Overview

- data is often spread across a number of ﬁles or databases, or is arranged in forms
that make them inconvenient to analyse (e.g. datapoints in columns rather than rows)
- Pandas provides many tools which help to combine, join, or rearrange data:
- hierarchical indexing (i.e. indexes with several levels on one axis) makes
higher-dimensional data tractable within a two-dimensional dataframe
- pandas.concat allows to stack objects together along an axis
- combine_first allows to splice together overlapping data
by ﬁlling in missing values in one object by values from another
- pandas.merge impements database join operations,
allowing to connect rows in DataFrames based on one or more keys
- data.stack, data.pivot and pandas.melt for reshaping data
in order to balance out columns and rows as desired

---

<!-- page:4 source:datsci-05-data-wrangling.pdf -->

Table of Contents
Data Wrangling: Overview
Hierarchical Indexing
Combining and Merging Datasets
Reshaping and Pivoting

---

<!-- page:5 source:datsci-05-data-wrangling.pdf -->

## Hierarchical Indexing: Basic Example

- hierarchical indexing allows us to have multiple index levels (equivalent to additional
dimensions) on an index; it allows us to work higher-dimensional data in a lower-dimensional
form (i.e. as a two-dimensional dataframe)
- simple example: a Series with a list of lists as the index
>>> series = pd.Series(np.random.randint(5, high=80, size=5),
index=[["BA", "BA", "BA", "MA", "MA"], [1, 2, 3, 1, 2]])
>>> series
BA 1 22
2 33
3 72
MA 1 18
2 10
dtype: int64
- data.index.nlevels is the number of levels in the row index

---

<!-- page:6 source:datsci-05-data-wrangling.pdf -->

## Hierarchical Indexing: Both Axes

- either axis in a DataFrame can have a hierarchical index, e.g.
>>> data = pd.DataFrame(np.random.randint(5, high=80, size=(5,4)),
index=[["BA", "BA", "BA", "MA", "MA"], [1, 2, 3, 1, 2]],
columns=[["GL", "GL", "CL", "CL"], ["m", "f", "m", "f"]])
>>> data
GL CL
m f m f
BA 1 41 49 43 36
2 40 14 54 38
3 45 19 36 50
MA 1 45 32 43 76
2 66 77 31 74

---

<!-- page:7 source:datsci-05-data-wrangling.pdf -->

## Hierarchical Indexing: Naming Levels

- frame.index.names and frame.columns.names allow to assign names to hierarchical
levels (one value per level, typically strings); in our example case, we could do
>>> data.index.names = ["level", "year"]
>>> data.columns.names = ["subject", "gender"]
>>> data
subject GL CL
gender m f m f
level year
BA 1 41 49 43 36
2 40 14 54 38
3 45 19 36 50
MA 1 45 32 43 76
2 66 77 31 74
- note the layout (level names should not be confused with index values)

---

<!-- page:8 source:datsci-05-data-wrangling.pdf -->

## Hierarchical Indexing: Partial Indexing

- partial indexing from a hierarchically indexed object makes it very straightforward to select
subsets of the data, e.g. only the rows with the counts of master students:
>>> data.loc["MA"]
subject GL CL
gender m f m f
year
1 45 32 43 76
2 66 77 31 74
- partial column indexing provides convenient access to groups of columns:
>>> data.loc["MA"]["GL"]
gender m f
year
1 45 32
2 66 77

---

<!-- page:9 source:datsci-05-data-wrangling.pdf -->

## Hierarchical Indexing: Cross-Sectioning

- underlyingly, multi-indices are implemented via tuples of indices (lists are multiple selection!)
- selection from an inner level (i.e. lower in the hierarchy) is possible as well, but things get
complicated very quickly (see Pandas documentation about slice(None) and similar)
- a very handy shortcut to selecting from an inner level (i.e. lower in the hierarchy) is the
cross-section method, which we can use to e.g. get the second-year students in BA or MA:
>>> data.xs(2, level="year")
subject GL CL
gender m f m f
level
BA 40 14 54 38
MA 66 77 31 74

---

<!-- page:10 source:datsci-05-data-wrangling.pdf -->

## Hierarchical Indexing: unstack and stack

- hierarchical indexing plays an important role in reshaping and group-based operations
- the unstack() method unpacks the highest-level row index into additional columns
a series with a two-level index therefore becomes a Dataframe, as in our example;
>>> series.unstack()
1 2 3
BA 22.0 33.0 72.0
MA 18.0 10.0 NaN
- stack() is the opposite of unstack(): the lowest-level column index is converted
into a new lowest-level row index (and it therefore only applies to dataframes)
- in essence, the two transformations help to conveniently motivate between more
column-heavy and more row-heavy formats in representing multidimensional data
- these operations will be central to reshaping and pivoting (later in this session)

---

<!-- page:11 source:datsci-05-data-wrangling.pdf -->

## Hierarchical Indexing: Reordering and Sorting Levels

- sometimes we may need to rearrange the order of the levels on an axis
(e.g. when a complex selection is easiest to express in a different order)
- the swaplevel method takes two level numbers or names and returns a new object with the
levels interchanged (numbers have changed due to reinitialisation without ﬁxed random seed):
>>> data.swaplevel("subject", "gender", axis=1)
gender m f m f
subject GL GL CL CL
level year
BA 1 44 40 15 17
2 10 72 57 33
3 62 42 65 24
MA 1 69 56 24 9
2 32 75 13 16

---

<!-- page:12 source:datsci-05-data-wrangling.pdf -->

Hierarchical Indexing: Reordering and Sorting Levels
- the sort_index method allows us to sort the data by values in one speciﬁc level instead of
the default lexicographic ordering based on all the levels according to their hierarchy
>>> data.sort_index(level="year")
subject GL CL
gender m f m f
level year
BA 1 44 40 15 17
MA 1 69 56 24 9
BA 2 10 72 57 33
MA 2 32 75 13 16
BA 3 62 42 65 24

---

<!-- page:13 source:datsci-05-data-wrangling.pdf -->

## Hierarchical Indexing: Indexing with a DataFrame’s columns

- quite often, we would like to use a combination of columns from a DataFrame as the row
index, and hierarchical indexing implements this in a very well-integrated way
- data.set_index() creates a new DataFrame using one or more of the speciﬁed columns
as the index, which could be useful e.g. for a language database with family speciﬁcation;
by default, columns used as index are removed ( drop=False changes that)
- data.reset_index() instead creates a new DataFrame where all hierarchical index levels
are moved into the columns, and the index is replaced by a default enumeration index
- both are very useful tools in exploring large real-world datasets

---

<!-- page:14 source:datsci-05-data-wrangling.pdf -->

Table of Contents
Data Wrangling: Overview
Hierarchical Indexing
Combining and Merging Datasets
Reshaping and Pivoting

---

<!-- page:15 source:datsci-05-data-wrangling.pdf -->

## Combining Datasets: Overview

- in order to arrive at a useful dataset for a given task, we often need to combine information
contained in different sources in a systematic way
- Pandas provides various capabilities for combining data contained in different objects
- concatenation or stacking, as implemented by pd.concat(), allows to “chain together”
objects along an axis
- combine_first() allows to splice together overlapping data, ﬁlling in missing values in
one object with values from another
- pandas.merge implements database join operations as they occur in relational
databases (i.e. equivalent to certain contructs in relational algebra and SQL)

---

<!-- page:16 source:datsci-05-data-wrangling.pdf -->

## Combining Datasets: Concatenation

- in addition to specifying the axis along which two arrays should be joined (the only parameter
we need for np.concatenate), labeled axes lead to additional concerns:
- if the objects are indexed differently on other axes,
should the distinct elements be combined, or only the shared values be used?
- do concatenated chunks need to remain identiﬁable in the result?
- does the concatenation axis contain data that needs to be preserved?
in most cases, default integer labels should be discarded
- pd.concat provides ways to address each of these questions:
- by default ( axis="index", calling it on a list of Series without index overlaps will simply
glue together the values and indexes (result is again a Series)
- with axis="columns", we instead receive a DataFrame over the concatenated index
(with all values but one in each row missing, an outer join in database terminology)
- by providing a keys list of the same length as the number of concatenated objects, they will
become a hierarchical index level (in the case of dataframes) or column names (in the case
of series), helping to keep blocks identiﬁable

---

<!-- page:17 source:datsci-05-data-wrangling.pdf -->

## Combining Datasets: Further Options of pd.concat

- pd.concat supports a range of additional options:
- in axis="columns" mode, join="inner" allows to perform an inner join instead of the
default outer join (only complete rows, makes sense if some index values are shared)
- keys can also be speciﬁed by using a dictionary instead of a list for the ﬁrst argument
(e.g. pd.concat({"key1": series1, "key2": series2}) )
- the names argument allows to specify names for the hierarchical levels created when keys
is passed; forinstance, this can be used to create an upper level for keeping the original
dataframes apart, lower level for the columns names coming from the original dataframes:
pd.concat([d1,d2], axis=1, keys=["HD","TÜ"], names=["uni","sbjct"])
- ignore_index=True discards the indexes from each DataFrame and concatenates the
data in identially-named columns only, then builds a new default index which simply
enumerates the rows
- by default, duplicates along the new axis are allowed;
with verify_integrity=True, an exception will be raised instead

---

<!-- page:18 source:datsci-05-data-wrangling.pdf -->

## Combining Datasets: a.combine_first(b)

- can be seen as a column-wise if-else which lines up values by index
- for two Series objects a and b, a.combine_first(b) will select values from b for all indices
where the value in a is null, while keeping all non-null values from a
(“patching in” missing data in the Series a with data from the Series b)
- with DataFrame objects, the same logic is applied column by column
- the output will have the union of all the column names
- columns which only exist in a will have their entire data from a (including null values)
- columns which do not exist in a will have their entire data from b (including null values)
- for all shared column names, the Series logic applies (from a if non-null, otherwise from b)

---

<!-- page:19 source:datsci-05-data-wrangling.pdf -->

## Merging Datasets: Database-Style DataFrame Joins

- merge (Pandas talk) or join (database talk) operations combine datasets by grouping
information into longer rows on the basis of shared keys (values of certain columns)
- example: if we have a database of language coordinates (as the one from Assignment 3) and
a database of numbers of speakers, these might be merged using the ISO codes as key;
each row would then combine coordinates and a number of speakers for some language
- there are several different join types which differ in which key combinations will be processed
- an inner join only uses the key combinations found in both tables (intersection)
- an outer join uses all key combinations found in either table (union)
- a left join uses all key combinations found in the ﬁrst table
- a right join uses all key combinations found in the second table
- put differently, an inner join will discard records which do not match, an outer join will preserve
all the information (but lead to incomplete records), and the directional joins will prioritise
preserving information from either side (treating the other table as supplementary data source)

---

<!-- page:20 source:datsci-05-data-wrangling.pdf -->

## Merging Datasets: Functionality of pd.merge

- a simple call pd.merge(df1, df2) implements an inner join
(keys in result are intersection of the values found in key columns of both tables)
- other types of joins can be selected using the named argument how:
options are how="inner", how="outer", how="left", how="right"
- by default, pd.merge uses the overlapping column names as keys, but it is always better to
specify explicitly using the on argument which column(s) should be used
- if the key columns are named differently in both arguments, left_on and right_on
arguments can be used to bridge the naming difference (no prior renaming necessary!)
- in non-inner joins, rows from the left or right arguments which do not match on keys in the
other argument will appear with NA values in the resulting dataframe
- overlapping non-key column names require special treatment; one option is to specify through
the named suffixes how column names from either side should be systematically extended

---

<!-- page:21 source:datsci-05-data-wrangling.pdf -->

## Merging Datasets: Merging on Index

- to indicate that an index (rather than a column) should be used as the merge key,
we can set left_index=True and/or right_index=True as arguments to pd.merge
- for hierarchically-indexed data, joining on index is equivalent to a multiple-key merge,
and the other side must have an equivalent number of levels/keys (for instance,
there could be the combination left_on=["key1", "key2"], right_index=True )
- in order to simplify merging by index, DataFrame has a join method which merges its ﬁrst
argument into the DataFrame by its index
- example syntax: df1.join(df2, how="outer")
- the on keyword makes it possible to join by a column in the calling dataframe
(whereas in the argument dataframe, the index will continue to serve as the key):
df1.join(df2, on="column_in_df1")

---

<!-- page:22 source:datsci-05-data-wrangling.pdf -->

Table of Contents
Data Wrangling: Overview
Hierarchical Indexing
Combining and Merging Datasets
Reshaping and Pivoting

---

<!-- page:23 source:datsci-05-data-wrangling.pdf -->

## Reshaping and Pivoting: Overview

- in many situations, we will want to rearrange complex tabular data in order to simply
computations, or make patterns more apparent; such transformations are called reshaping
- the two elementary reshaping actions involving hierarchical indexing which involve moving
indexing layers from columns to rows, and vice versa:
- stacking pivots (“rotates”) from the columns in the data to the rows
- unstacking pivots from the rows into the columns
- wihout indexing, these can be seen as repackaging the contents of columns
- pivoting transforms one column into many, moving towards a wider format
- melting merges multiple columns into one, moving towards a longer format

---

<!-- page:24 source:datsci-05-data-wrangling.pdf -->

## Long Format

- in a long format, each row represents a single observation, with several categorical
“identifying columns” and a single “value column”
- for our earlier example dataset, a long format (just BA students) would look like this:
subject year gender count
0 CL 1 f 55
1 CL 1 m 20
2 CL 2 f 23
3 CL 2 m 26
4 CL 3 f 48
5 CL 3 m 14
6 GL 1 f 50
7 GL 1 m 18
8 GL 2 f 25
9 GL 2 m 16
10 GL 3 f 29
11 GL 3 m 67

---

<!-- page:25 source:datsci-05-data-wrangling.pdf -->

## Pivoting from Long to Wide Format

- pd.pivot() implements a very frequent use case where a long format is turned
into a wide format where the values of an ID column become separate columns
- the columns argument speciﬁes which column should turn into the new frame’s columns
- the index argument speciﬁes the column(s) to use to make the new frame’s index
(must be unique!); if not speciﬁed, the existing index is used
- this is equivalent to creating a hierarchical index with the two levels speciﬁed via the index
and columns arguments, and then unstacking on the level of the columns argument
- the optional values argument speciﬁes which colum(s) to use for populating the new frame’s
values; by default, all remaining columns are used, and result is a hierarchical column index

---

<!-- page:26 source:datsci-05-data-wrangling.pdf -->

Pivoting from Long to Wide Format
- pivot() can only handle unique rows speciﬁed by index and columns; in case of duplicate
rows, a solution is to aggregate numeric data, which can be done using pivot_table()
- pd.pivot_table(data, index=["year","gender"], columns=["subject"]):
count
subject CL GL
year gender
1 f 55 50
m 20 18
2 f 23 25
m 26 16
3 f 48 29
m 14 67
- we are going to call this example pivoted_table

---

<!-- page:27 source:datsci-05-data-wrangling.pdf -->

## pd.pivot_table: Further Examples

- by default, aggregation happens through averaging over unspeciﬁed columns:
pd.pivot_table(long_format, columns=["year"], index=["gender"],
values="count")
year 1 2 3
gender
f 52.5 24.0 38.5
m 19.0 21.0 40.5
- other functions can be speciﬁed, e.g. pd.pivot_table(long_format,
columns=["subject"], index=["gender"], values="count",
aggfunc=["sum"])
sum
subject CL GL
gender
f 126 104
m 60 101

---

<!-- page:28 source:datsci-05-data-wrangling.pdf -->

## Pivoting from Wide to Long Format

- pd.melt() implements the inverse operation to pd.pivot(),
merging multiple columns into one through an identiﬁer variable column
- the id_vars arguments states which columns should not be melted
- the resulting dataframe is of course longer than the input
- pivoted_table.reset_index().melt(id_vars=["year","gender"])
year gender NaN subject value
0 1 f count CL 55
1 1 m count CL 20
2 2 f count CL 23
3 2 m count CL 26
4 3 f count CL 48
5 3 m count CL 14
6 1 f count GL 50
7 1 m count GL 18
8 2 f count GL 25
9 2 m count GL 16
10 3 f count GL 29
11 3 m count GL 67

---

<!-- page:29 source:datsci-05-data-wrangling.pdf -->

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

<!-- page:30 source:datsci-05-data-wrangling.pdf -->

## Questions

Questions?
Comments?
Suggestions?

---
