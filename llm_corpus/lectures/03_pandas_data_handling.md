---
id: "03"
title: "Pandas and Data Handling"
kind: "lecture"
course: "Data Science for Linguists"
term: "Summer 2026"
instructor: "Johannes Dellert"
source_pdf: "Vorlesungenslides/datsci-03-pandas-data-handling.pdf"
pages: 40
---

# Session 3: Pandas and Data Handling

> Full slide text extracted from `datsci-03-pandas-data-handling.pdf` for LLM use. Every PDF page is included; page markers are HTML comments.

<!-- page:1 source:datsci-03-pandas-data-handling.pdf -->

## Session 3: Pandas and Data Handling

Johannes Dellert
7 May, 2026

---

<!-- page:2 source:datsci-03-pandas-data-handling.pdf -->

## Table of Contents

Introduction to Pandas
Fundamental Data Structures ( pd.Series, pd.DataFrame, pd.Index)
Data Indexing and Selection
Data Loading and Storage
Data Exploration and Summary Statistics
Data Cleaning
Data Preparation

---

<!-- page:3 source:datsci-03-pandas-data-handling.pdf -->

## Pandas: Purpose and Usage

- the pandas package provides the most popular Python implementation of a data frame
(a multidimensional array of heterogeneous types with attached row and column labels)
- pandas.DataFrame objects provide extensive functionality for
- working with missing data
- operations that do not map well to NumPy-style element-wise broadcasting
- efﬁcient data structures for time slices and indexing
- convention for import (this is what we will assume throughout this course):
import pandas as pd

---

<!-- page:4 source:datsci-03-pandas-data-handling.pdf -->

## Pandas: Fundamental Data Structures

- two main workhorse data structures:
- pd.Series for a sequence of values of the same type
- pd.DataFrame for a rectangular table of data composed of one series per column
- Pandas data structures combine NumPy arrays with Index objects which hold
- axis labels (most centrally, column names and labels for rows, i.e. individual data points)
- other metadata (e.g. axis name or names)

---

<!-- page:5 source:datsci-03-pandas-data-handling.pdf -->

## pd.Series as an Indexed Sequence

- a Series combines a sequence of values (a one-dimensional NumPy array) with an explicit
sequence of indices (of type pd.Index) which allows much broader usage
- construction from list literal: data = pd.Series([0.25, 0.5, 0.75, 1.0])
- data.values is the array,data.index is a RangeIndex(start=0, stop=4, step=1)
- data can be accessed by the associated index using slicing notation: data[1:3]
- crucial difference to a NumPy array: explicitly deﬁned index associated with the values,
which gives the Series object additional capabilities:
- index need not be an integer, but can consist of values of any desired type
- for instance, this allows us to make every datapoint accessible under string ids:
data = pd.Series([0.25, 0.5, 0.75], index=['a', 'b', 'c'])
stored_value = data['b']
- data.reindex() allows us to create a new Series with values rearranged
to align with the new index (plus support for ﬁlling with default values or interpolation)

---

<!-- page:6 source:datsci-03-pandas-data-handling.pdf -->

## pd.Series as a Specialized Dictionary

- this capability turns a Pandas Series into a specialised Python dictionary:
- a Python dictionary maps arbitrary keys to a set of arbitrary values
- a Series maps typed keys to a set of typed values (which makes it more efﬁcient!)
- there is a constructor which allows to construct a Series directly from a Python dictionary:
iso_to_lang = {'aa': 'Afar', 'ab': 'Abkhaz', 'ae': 'Avestan',
'af': 'Afrikaans', 'ak': 'Akan', 'am': 'Amharic'}
- the index is ordered, which makes array-style operations such as slicing possible:
In [ ]: iso_to_lang['ae':'ak']
Out[ ]: ae Avestan
af Afrikaans
ak Akan
- the equivalent to del dct[key] is data.drop(list_of_indices)

---

<!-- page:7 source:datsci-03-pandas-data-handling.pdf -->

## Constructing pd.Series Objects

- general form of the constructor: pd.Series(data, index=index)
- data can be one of many entities:
- list or NumPy array, in which case index defaults to an integer sequence
- a scalar, which is repeated to ﬁll the speciﬁed index
- a dictionary, in which case index defaults to dictionary keys
- in each case, an index can be explicity set to control the order or subset of keys used
In [ ]: pd.Series({2:'a', 1:'b', 3:'c'}, index=[1, 2])
Out[ ]: 1 b
2 a

---

<!-- page:8 source:datsci-03-pandas-data-handling.pdf -->

## pd.DataFrame as Generalized NumPy Array

- a DataFrame combines a two-dimensional array of values with explict row and column indices
- it can be thought of as a sequence of Series that are aligned (share the same index)
In [ ]: lang = pd.Series(iso_to_lang)
speakers = pd.Series({'aa': 2500000, 'ab': 190000, 'ae': 0,
'af': 17500000, 'ak': 11000000, 'am': 57000000})
data = pd.DataFrame({'lang_name': lang, 'num_speakers': speakers})
data
Out[ ]:
lang_name num_speakers
aa Afar 2500000
ab Abkhaz 190000
ae Avestan 0
af Afrikaans 17500000
ak Akan 11000000
am Amharic 57000000

---

<!-- page:9 source:datsci-03-pandas-data-handling.pdf -->

## pd.DataFrame as Generalised Array and Specialised Dictionary

- like Series, a DataFrame object has an index attribute
- additionally, it has a columns attribute containing an Index object with the column labels:
In [ ]: data.columns
Out[ ]: Index(['lang_name', 'num_speakers'], dtype='object')
- therefore, the DataFrame can be seen as a generalisation of a two-dimensional NumPy array
where both rows and columns have a generalised index for data access
- at the same time, a DataFrame can be seen as a specialised dictionary:
- dictionary maps key to value
- DataFrame maps column name to a Series of column data

---

<!-- page:10 source:datsci-03-pandas-data-handling.pdf -->

## Constructing pd.DataFrame Objects

- DataFrame objects can be constructed in a multitude of ways:
- a single-column DataFrame can be constructed from a single Series
- any list of dictionaries can be turned into a DataFrame
- from a dictionary of Series objects (with column names as keys)
- by adding column and index names to a two-dimensional NumPy array
- this is not an exhaustive list, see Pandas documentation for more!

---

<!-- page:11 source:datsci-03-pandas-data-handling.pdf -->

## pd.Index as Immutable Array

- the Index object which implements the indices in a Series or DataFrame
can be thought of as an immutable array
- an Index object ind in many ways operates like an array:
- ind[1] provides the key stored in the second position of the index
- ind[::2] creates a new index which only contains every second element
- ind.size returns the number of entries in the index
- ind.shape returns the length in both dimensions
- ind.ndim returns the number of index dimensions
- ind.dtype returns the type of the index keys
- the important difference is that the indices are immutable
- no possibility to add a new key for a new position
- no possibility to assign a different key to a position
- no possibility to delete an entry
- immutability decreases the risk of unintended side effects

---

<!-- page:12 source:datsci-03-pandas-data-handling.pdf -->

## pd.Index as Ordered Set

- Pandas is designed to facilitate set operations across datasets
- as we will see, this primarly works through set operations on indices:
- indA.intersection(indB) will contain only those keys which occur in both indA and
indB, with the order depending on indA
- indA.union(indB) will contain keys which occur in indA or indB,
with enough copies to cover all repeated elements, in default order
- indA.symmetric_difference(indB) will contain only those keys
which occur in either indA or indB, but not in both

---

<!-- page:13 source:datsci-03-pandas-data-handling.pdf -->

## Data Selection in Series as Dictionary

- accessing individual entry/row via data[key]
- membership test via key in data
- iteration over rows supports the standard idioms for Python dictionaries:
- for key in data
- data.keys()
- data.items()
- data[key] = value to change or add value under a key

---

<!-- page:14 source:datsci-03-pandas-data-handling.pdf -->

## Data Selection in Series as One-Dimensional Array

- Series can be sliced using both explicit and implicit indices:
- slicing by explicit index: data["a":"c"] (ﬁnal index included!)
- slicing by implicit integer index: data[0:2] (ﬁnal index excluded!)
- masking works just like in NumPy: data[(data > 0.2) & (data < 0.8)]
- note that series and data frames expose two different indices:
- data.loc for indexing and slicing with reference to explicit index
- data.iloc for indexing and slicing with implicit Python-style index
- especially relevant when working with integer indices
(note that by default, data[x] and data[a:b] operate on different indices!)

---

<!-- page:15 source:datsci-03-pandas-data-handling.pdf -->

## Data Selection in Data Frame as Dictionary

- a DataFrame object is a specialised dictionary as well:
- access to individual series via column name indexing: data[num_speakers]
- equivalently, the column names are available as ﬁelds: data.num_speakers
(only for strings, and in the absence of naming conﬂicts with internal names!)
- dictionary-style syntax can also be used to add new columns on the ﬂy:
data["density"] = data["pop"] / data["area"]
(this exploits element-by-element arithmetic between Series objects)

---

<!-- page:16 source:datsci-03-pandas-data-handling.pdf -->

## Data Selection in Data Frame as Two-Dimensional Array

- but a DataFrame object is a generalised two-dimensional array as well:
- underlying raw NumPy array accessible via data.values
- much array-based logic is available for data frames as well (e.g. data.T)
- index semantics is different, array-style indexing works via data.iloc
- data.iloc keeps broadcasting etc. available
- important facts about the behaviour of indices:
- by default, indexing refers to columns, but slicing refers to rows
- direct masking operations are interpreted row-wise rather than column-wise
- applying any NumPy universal function on a Pandas object will return
another Pandas object with the indices preserved

---

<!-- page:17 source:datsci-03-pandas-data-handling.pdf -->

## Data Loading and Storage

- for data loading, there are many functions of shape pd.read_X, including:
- pd.read_csv(filename) (for comma-separated value ﬁles, many options!)
- pd.read_table(filename) (for delimited ﬁles in general)
- pd.read_excel(filename) (for importing from spreadsheets like XLSX and ODS ﬁles)
- pd.read_json(filename) (for converting JSON strings to pandas objects)
- pd.read_html(filename) (for reading HTML tables into DataFrame objects)
- pd.read_xml(filename) (for reading XML documents as speciﬁed by an XPath)
- DataFrame offers equivalent methods for exporting into different formats, including:
- df.to_csv(filename) (for export as comma-separated value ﬁle)
- df.to_excel(filename) (for single table, more complex operations via ExcelWriter)
- df.to_html(filename) (for export as an HTML table)
- df.to_json(filename) (for conversion into a JSON string)
- df.to_latex(filename) (for export into LaT eX table, very useful for publications)

---

<!-- page:18 source:datsci-03-pandas-data-handling.pdf -->

## Data Exploration and Summary Statistics

- data.count() returns the number of non-NA values
- data.sum() returns a Series containing column sums
- data.sum(axis="columns") returns a Series containing row sums
- data.mean() returns the average of the values in each column
- data.median() returns the median of the values in each column
- data.idxmax() returns a Series of index values where the maximum values are attained
- data.pct_change() computes percent changes
- data.corrwith(series) computes pairwise correlations of each column with series
- data.describe() produces multiple summary statistics in one go
- data.unique() produces an array of the unique values in a Series
- data.value_counts() computes a Series containing value frequencies
- data.isin() performs a vectorised set membership check and
returns a boolean mask for ﬁltering, e.g. data[data.isin(["b", "c"])]
- pd.notnull(series) returns a boolean Series of values where the value is NaN
- option level to reduce grouped by level if axis is hierarchically indexed

---

<!-- page:19 source:datsci-03-pandas-data-handling.pdf -->

## Sorting and Ranking

- data.sort_index() returns copy of data with rows sorted by their index
- named parameter ascending=False switches to reverse order
- named parameter inplace=True switches to in-place sorting
- data.sort_values() returns copy of data with rows sorted by their values
- accepts column name or list of column names to sort by as unnamed parameter
- named parameter ascending=False switches to descending order
- named parameter inplace=True switches to in-place sorting
- data.rank() returns Series of ranks (1 through n) for the rows
- in a DataFrame, columns of output will contain ranks for respective column
- by default, equal values are assigned the average of ranks of those values
- named parameter ascending=False switches to descending order
- named parameter axis=1 or axis="columns" provides ranks within rows instead

---

<!-- page:20 source:datsci-03-pandas-data-handling.pdf -->

Table of Contents
Introduction to Pandas
Data Cleaning
Handling Missing Data
Duplicate Removal, Value Replacement, and Renaming
Outlier Detection and Removal
Data Preparation

---

<!-- page:21 source:datsci-03-pandas-data-handling.pdf -->

## Data Cleaning and Preparation

- in data science, data preparation (cleaning, transforming, and rearranging of real-world data)
often comprises the majority of the work; a common ﬁgure is about 80% of an analyst’s time
- ad hoc processing of data using a variety of tools (plain Python, Perl, R, Java, sed, awk)
is still very common in science, but this approach has many disadvantages
- using Pandas in a Jupyter notebook for these tasks has the advantages of
- a high-level, ﬂexible, and fast set of tools that is very accessible to other researchers
- full documentation of the steps taken to derive the research data from the raw inputs
(crucial for transparency and reproducibility!)

---

<!-- page:22 source:datsci-03-pandas-data-handling.pdf -->

## NaN and None in Pandas

- due to their underlying implementation in NumPy, Pandas series represent missing values by
means of different sentinel values, the choice of which depends on the datatype:
- for data with dtype float64, Pandas uses the ﬂoating-point value NaN (Not a Number)
which is deﬁned by the ISO standard (accessible via np.nan)
- for general Python objects (including variable-length strings), it uses the special value None
from standard Python (which is very slow to compute with!)
- because these two options are the only ones available, series of integer datatypes are
silently converted into ﬂoating point numbers as soon as missing values are inserted
- one of the goals of Pandas is to make working with missing data efﬁcient and smooth
- there is well-deﬁned default behaviour for any functions executed on Pandas series with
missing values; such values will never cause Pandas to throw an exception, though the
default behaviour might not be extremely useful in some cases
- many methods (such as the ones for descriptive statistics) are implemented to silently
exclude missing data per default
- it also provides a range of methods which abstract over the somewhat inconsistent
underlying implementation of null values

---

<!-- page:23 source:datsci-03-pandas-data-handling.pdf -->

## Pandas Nullable Dtypes

- to add support for true integer arrays with missing data, Pandas provides nullable dtypes like
pd.Int32 (distinguished from the default dtypes like pd.int32 by capitalisation)
- the null value in series of these types is represented by pd.NA
- the other null values will be normalised without triggering implicit typecasting:
In [ ]: pd.Series([1, np.nan, 2, None, pd.NA], dtype='Int32')
Out[ ]: 0 1
1 <NA>
2 2
3 <NA>
4 <NA>
dtype: Int32
- for more efﬁcient handling of large amounts of string data, there is the specialised extension
type pd.StringDtype()

---

<!-- page:24 source:datsci-03-pandas-data-handling.pdf -->

## Detecting Null Values

- null values of any kind can be detected using the method data.isnull(), which returns a
Boolean mask over the data, with True in all positions where there is a null value
- data.notnull() returns a Boolean mask as well, but the opposite of the result of the
previous method ( False in all positions where there is a null value)
- data.isna() and data.notna() are aliases of data.isnull() and data.notnull(),
both sentinel values are matched by both methods (unlike in the underlying implementation)
In [ ]: data = pd.Series([1, np.nan, 'hello', None])
In [ ]: data.isnull()
Out[ ]: 0 False
1 True
2 False
3 True
dtype: bool

---

<!-- page:25 source:datsci-03-pandas-data-handling.pdf -->

## Dropping Null Values with dropna()

- data.dropna() is a convenience method which combines ﬁltering for and then dropping the
null values, i.e. a shorthand for data[data.notna()]
- if data is a Series, the result will simply be a shorter series
- if data is a DataFrame, we can only drop entire rows or columns
- by default, data.dropna() will drop all rows which contain any null value
- to drop columns instead, we can provide the argument axis=1 or axis="columns"
- argument how="all" to only drop rows/columns which consist entirely of null values
- for more ﬁne-grained control (e.g. only weeding out the most gappy records),
we can also provide an argument thresh= k to specify that any row/column with at least k
non-null values will be kept

---

<!-- page:26 source:datsci-03-pandas-data-handling.pdf -->

## Filling Null Values with fillna()

- data.fillna(x) is a convenience method which combines ﬁltering for and then overwriting
the null values with a default value x, i.e. a shorthand for data[data.isna()] = x
- x can be a dictionary providing different ﬁll values by column index
- data.fillna(method="ffill") speciﬁes a forward ﬁll, i.e. empty values will be replaced
by the previous non-null value (which therefore gets propagated forward)
- example: a series with data [1 <NA> 2 <NA> <NA> 3] will become [1 1 2 2 2 3]
- data.fillna(method="bfill") speciﬁes a backward ﬁll, i.e. empty values will be
replaced by the subsequent non-null value (which therefore gets propagated backward)
- example: a series with data [1 <NA> 2 <NA> <NA> 3] will become [1 2 2 3 3 3]
- if no previous or subseqent value is available, fﬁll and bﬁll leave null values at the fringes!
- for a DataFrame, we can again switch to propagation through columns by specifying axis=1

---

<!-- page:27 source:datsci-03-pandas-data-handling.pdf -->

## Removing Duplicates

- data.duplicated() returns a Boolean Series indicating whether each row is a duplicate
(all values equal to some previous row) or not
- data.drop_duplicates() returns a Series or DataFrame consisting of only those rows
in data where data.duplicated() was False
- the subset argument allows to provide a list of column indices to specify which columns are
relevant for duplicate detection (other columns are allowed to have different values)
- if the subset argument is used, the ﬁrst variant of each duplicate will be used for the values in
the irrelevant columns, keep="last" changes this

---

<!-- page:28 source:datsci-03-pandas-data-handling.pdf -->

## Replacing Values

- data.replace(oldvals, newvals) substitutes a set of values by replacements
- data.replace(-1, 0) sets all cells with value -1 to 0
- data.replace([-2, -1], 0) sets all cells with value -2 or -1 to 0
- data.replace([-2, -1], [-1, 0]) sets cells with value -2 or -1, and all with -1 to 0
- data.replace(dictionary) replaces each occurrence of a key with its value
- more complex element-wise transformation can be implemented as a function
(e.g. transform_value(x)), and then executed on every cell by a call to
data.map(transform_value); this works with anonymous functions ( lambda) as well

---

<!-- page:29 source:datsci-03-pandas-data-handling.pdf -->

## Renaming Axis Indexes

- the axes can be modiﬁed in place by executing the map method of their indices:
- data.columns = data.columns.map(str.title)
- data.index = data.index.map(lambda x: x[:4].upper())
- data.rename() allows to create a transformed version of a dataset without modifying the
original (simple example: data.rename(index=str.title, columns=str.upper) )

---

<!-- page:30 source:datsci-03-pandas-data-handling.pdf -->

## Detecting and Filtering Outliers

- outlier detection and ﬁltering is typically performed by combinations of simple array operations
- for a normally distributed Series of data, we might deﬁne our outliers as all rows where the
value exceeds 3 in absolute value: data[data.abs() > 3]
- in a DataFrame full of normally distributed values, we might be interested in rows where any
of the columns has such a value: data[(data.abs() > 3).any(axis="columns")]
(Boolean DataFrame generated by the comparison, on which we apply the any() method)
- to remove the outliers by capping values to the range [-3, 3], we can just do
data[data.abs() > 3] = np.sign(data) * 3

---

<!-- page:31 source:datsci-03-pandas-data-handling.pdf -->

Table of Contents
Introduction to Pandas
Data Cleaning
Data Preparation
Discretisation and Binning
Permutation and Random Sampling
Vectorised String Operations
Categorical Data

---

<!-- page:32 source:datsci-03-pandas-data-handling.pdf -->

## Discretisation and Binning

- continuous data is often discretised or otherwise separated into bins for analyis
- pd.cut(data, k) returns a Categorical object which describes the k equal-length bins
computed on the basis of the minimum and maximum values within the data
- pd.cut(data, cutoffs) returns a Categorical object which describes the bins
computed from the data based on the speciﬁed cutoff values between the bins
- pd.qcut(data, k) bins the data into k quantiles (equally sized bins)
- pd.qcut(data, quantiles) bins the data into the provided quantiles (between 0 and 1)
- the argument labels=group_names allows to override the default bin names
- a Categorical object cats has the following key applications:
- cats.codes returns an array containing the bin index for each datapoint
- cats.categories shows an IntervalIndex object representing the bins
- pd.value_counts(cats) renders the counts of datapoints in each bin
- these functions will have central importance in Session 7 (aggregation and grouping)

---

<!-- page:33 source:datsci-03-pandas-data-handling.pdf -->

## Permutation and Random Sampling

- permutations are sampled using smp = np.random.permutation(k)
- data.take(smp) (= iloc-based indexing) is then a random permutation of the ﬁrst k lines
- data.sample(n=k) selects a random subset of k rows without replacement
- data.sample(n=k, replace=True) samples k rows with replacement

---

<!-- page:34 source:datsci-03-pandas-data-handling.pdf -->

## Vectorised String Operations: Equivalents of Basic Methods

- cleaning up a messy dataset often requires a lot of string manipulation, but simple
element-wise application using data.map() will fail on the null values
- the Pandas Series offers array-oriented and null-aware string operations which are
accessible via the str attribute; here is a small sample:
- data.str.count to count occurrences of a pattern
- data.str.contains(s) returns a Boolean mask with the result of calls to
s in value on each cell value, mixed with NaN values wherever a value was missing
- data.str.len to compute the length of each string
- data.str.strip to trim whitespace (including newlines) from both sides

---

<!-- page:35 source:datsci-03-pandas-data-handling.pdf -->

## Vectorised String Operations: Regular Expressions

- there are also vectorised and null-aware versions of the regex capabilities:
- matches = data.str.findall(r"somePattern")
- first_matches = matches.str.get(1)
- data.str.extract(pattern) returns the captured groups of the regular expression as a
new DataFrame
- this is difﬁcult to practise in class using a minimal example,
but you will get to explore this option in the new assignment!

---

<!-- page:36 source:datsci-03-pandas-data-handling.pdf -->

## Vectorised String Operations: Miscellaneous Methods

- several methods emulate the capabilities of Python string operations:
- data.str.cat for element-wise concatenation (with optional delimiter)
- data.str.get to index each string
- data.str.repeat to repeat each string
- data.str.slice for extracting slices from each string
- data.str.get and data.str.slice are also available through the normal indexing
syntax (data.str[i] and data.str[i:j])

---

<!-- page:37 source:datsci-03-pandas-data-handling.pdf -->

## Categorical Data: Background and Motivation

- if a column contains repeated instances of a smaller set of distinct values (e.g. macroareas in
the previous assignment), storage and computations can be somewhat efﬁcient
- in a categorical representation, we store the primary observations only as integer keys
(called codes) which refer to a dimension table that contains the actual distinct values
- if we simply use a pandas Series as the dimension table dim, we can use
dim.take(values) in order to restore the original Series of strings
- categorical representation is a popular data compression technique which can lead to
signiﬁcantly less memory use and faster performance, especially on string data

---

<!-- page:38 source:datsci-03-pandas-data-handling.pdf -->

## Categorical Extension Type

- pandas has a special Categorical extension type which provides a convenient way of
handling integer-based categorical encoding
- an existing column (like macroarea) can be converted to categorical by calling
data["macroarea"].astype('category')
- this returns a Series that we can reassign to data["macroarea"];
values are of type pd.Categorical, which we can access via the.array attribute
- important features of a Categorical object c:
- c.categories to access the dimension table (as an Index)
- c.codes to access the encoded primary observations
- much better performance of groupby and binning functions
- special accessor attribute c.cats provides access to categorical methods
- c.cat.remove_categories (removed values become null)
- c.cat.remove_unused_categories
- pd.get_dummies() to generate one-hot encoding is very quick on categorical Series

---

<!-- page:39 source:datsci-03-pandas-data-handling.pdf -->

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

<!-- page:40 source:datsci-03-pandas-data-handling.pdf -->

## Questions

Questions?
Comments?
Suggestions?

---
