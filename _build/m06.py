from nb import lesson, exercises

F = "06_Pandas/"
PG = "[pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)"
NOTE = "Exercises for this folder are in `exercises/Pandas_Exercises.ipynb`."
SETUP = '''import pandas as pd
import numpy as np
RAW = "../datasets/raw/"
PROCESSED = "../datasets/processed/"'''

lesson(F + "01_Introduction_to_Pandas.ipynb", "Introduction to pandas",
["explain what pandas is and the problems it solves",
 "name its two main structures: Series and DataFrame",
 "load a dataset and take a first look",
 "describe a typical pandas workflow"],
"""
pandas is the standard Python library for working with tables: rows of observations and columns of
variables, like a spreadsheet or a statistics data file. It reads data from files and databases,
cleans it, reshapes it, summarises it and hands it to plotting and modelling libraries.
""",
[
'''import pandas as pd
pd.__version__''',
'''#md
## Why pandas?

With only lists and dictionaries, answering "what is the mean age per site?" takes a loop, a dictionary
of lists and a second loop. With pandas it is one line, and it handles missing values, dates and text
along the way.
''',
'''patients = pd.read_csv("../datasets/raw/patients.csv")
patients.groupby("site")["age"].mean().round(1)''',
'''#md
## The two main structures

- a **Series** is one column: values plus an *index* (labels for the rows)
- a **DataFrame** is a table: several Series that share the same index

```
DataFrame
            ┌─────────── columns ──────────┐
 index      patient_id   site    age   ...
   0        P0001        Site A   41
   1        P0002        Site B   83        ← one row = one observation
   2        P0003        Site B   36
                          ↑
                   one column = one Series
```
''',
'''print(type(patients))
print(type(patients["age"]))''',
'''#md
## A first look
''',
'''patients.head()''',
'''print(patients.shape)        # (rows, columns)
print(patients.columns.tolist())''',
'''#md
## What pandas is used for

| task | pandas tools | notebook |
|---|---|---|
| read and write files | `read_csv`, `read_excel`, `to_csv` | 03 |
| look at the data | `head`, `info`, `describe`, `value_counts` | 04 |
| clean it | `isna`, `fillna`, `drop_duplicates`, `astype`, `str` methods | 05 |
| select, filter, compute columns | `loc`, `iloc`, `query`, `assign` | 06 |
| summarise by group | `groupby`, `agg` | 07 |
| combine and reshape | `merge`, `concat`, `pivot_table`, `melt` | 08 |
| plot | `.plot`, then Matplotlib and Seaborn | 07_Matplotlib, 08_Seaborn |

## A typical workflow

1. **import** the raw file, without editing it by hand
2. **explore**: size, types, missing values, odd categories
3. **clean**: fix types, standardise text, handle missing and impossible values, remove duplicates
4. **transform**: new variables, filtering, merging other tables
5. **summarise and visualise**
6. **export** the cleaned data and results

Keeping each step in code means anyone can rerun the analysis from the raw file and get the same answer.

## pandas and NumPy

Each column is stored as a NumPy array, so everything in module 5 applies:
''',
'''ages = patients["age"].to_numpy()
print(type(ages), ages[:5], ages.mean())''',
],
[PG, "[10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)",
 "[Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)"],
exercises_note=NOTE)

lesson(F + "02_Series_and_DataFrames.ipynb", "Series and DataFrames",
["create Series and DataFrames from lists, dictionaries and arrays",
 "understand the index and how operations align on it",
 "access columns, and add and remove them",
 "inspect data types"],
"""
Before loading real files it helps to build small tables by hand, so you can see exactly how pandas
stores rows, columns and the index.
""",
[
SETUP,
'''#md
## Series
''',
'''glucose = pd.Series([5.4, 7.8, 6.1, 9.2])
print(glucose)''',
'''#md
The left column is the **index**. By default it is 0, 1, 2, ... but it can be any labels:
''',
'''glucose = pd.Series([5.4, 7.8, 6.1, 9.2], index=["P01", "P02", "P03", "P04"], name="glucose")
print(glucose)
print(glucose["P03"], glucose.iloc[0])''',
'''#md
A Series has NumPy-style vectorised maths and statistics methods:
''',
'''print((glucose * 18).round(0))
print(glucose.mean(), glucose.max(), glucose.idxmax())
print(glucose[glucose > 7])''',
'''#md
### Alignment on the index

Operations between Series match labels, not positions. Labels missing from either side give NaN.
''',
'''before = pd.Series({"P01": 142, "P02": 128, "P03": 155})
after = pd.Series({"P03": 141, "P01": 131, "P04": 120})
print(after - before)''',
'''#md
P01 and P03 are matched correctly even though they are in a different order; P02 and P04 have no
partner, so their result is missing. This prevents silent mismatches, but means you should check for
unexpected NaN after combining data.

## DataFrames

### From a dictionary of columns
''',
'''df = pd.DataFrame({
    "patient_id": ["P01", "P02", "P03", "P04"],
    "sex": ["F", "M", "F", "M"],
    "age": [34, 51, 47, 62],
    "glucose": [5.4, 7.8, 6.1, 9.2],
})
df''',
'''#md
### From a list of dictionaries (one per row)
''',
'''rows = [
    {"patient_id": "P05", "sex": "F", "age": 29, "glucose": 5.0},
    {"patient_id": "P06", "sex": "M", "age": 44},
]
pd.DataFrame(rows)''',
'''#md
### From a NumPy array
''',
'''rng = np.random.default_rng(0)
pd.DataFrame(rng.normal(10, 2, (3, 4)).round(1), columns=["run1", "run2", "run3", "run4"],
             index=["sample_a", "sample_b", "sample_c"])''',
'''#md
## Anatomy of a DataFrame
''',
'''print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)''',
'''#md
pandas uses `int64` and `float64` for numbers, `str` for text (pandas 3) or `object` (older versions),
`bool`, `datetime64` for dates and `category` for categories.

## Columns

`df["name"]` returns a Series; `df[["a", "b"]]` (a list) returns a DataFrame.
''',
'''print(df["age"])
df[["patient_id", "glucose"]]''',
'''#md
Adding and changing columns:
''',
'''df["glucose_mg_dl"] = (df["glucose"] * 18).round(0)
df["high"] = df["glucose"] >= 7
df["site"] = "Site A"                       # one value for every row
df''',
'''#md
Removing columns and renaming them:
''',
'''df = df.drop(columns=["site"])
df = df.rename(columns={"glucose": "glucose_mmol"})
df.columns.tolist()''',
'''#md
## Setting the index

A column of unique IDs often makes a good index.
''',
'''indexed = df.set_index("patient_id")
print(indexed.loc["P03"])
indexed.reset_index().head(2)''',
'''#md
## Rows

`len(df)` counts rows; `df.iloc[0]` is the first row; `df.loc[label]` selects by index label
(details in notebook 06).
''',
'''print(len(df))
print(df.iloc[0])''',
],
[PG, "[Intro to data structures](https://pandas.pydata.org/docs/user_guide/dsintro.html)"],
exercises_note=NOTE)

lesson(F + "03_Data_Import_and_Export.ipynb", "Importing and exporting data",
["read CSV, TSV and Excel files, including sheets",
 "control column types, missing value codes and dates when reading",
 "read only the columns or rows you need",
 "export results to CSV and Excel in a processed-data folder"],
"""
Most analyses start by reading a file. `read_csv` has many options, and using the right ones while
reading saves a lot of cleaning afterwards. The rule: **never edit raw data by hand**. Read the raw file,
fix it in code, and write the result to a separate processed file.
""",
[
SETUP,
'''#md
## CSV files
''',
'''patients = pd.read_csv(RAW + "patients.csv")
patients.head()''',
'''#md
## Useful read_csv options

| option | does |
|---|---|
| `sep` | separator: `","`, `"\\t"`, `";"` |
| `usecols` | read only some columns |
| `nrows` | read only the first n rows |
| `dtype` | force column types, e.g. `{"patient_id": str}` |
| `na_values` | extra codes that mean missing |
| `parse_dates` | convert columns to dates |
| `index_col` | use a column as the index |
| `skiprows`, `header` | deal with notes above the table |
| `encoding` | for files with special characters (`"utf-8"`, `"latin-1"`) |
''',
'''small = pd.read_csv(RAW + "patients.csv", usecols=["patient_id", "site", "age"], nrows=5)
small''',
'''#md
### Dates

Without `parse_dates`, dates are read as text, so you cannot subtract them or extract the month.
''',
'''print(pd.read_csv(RAW + "patients.csv")["enrolled"].dtype)
patients = pd.read_csv(RAW + "patients.csv", parse_dates=["enrolled"])
print(patients["enrolled"].dtype)
print(patients["enrolled"].min(), "to", patients["enrolled"].max())''',
'''#md
### Missing value codes

The sample register uses codes like `not done` and blanks. Telling pandas about them while reading
turns them into proper missing values (NaN):
''',
'''register = pd.read_csv(RAW + "sample_register_raw.csv", na_values=["not done", ""])
print(register["concentration"].isna().sum(), "missing concentrations")
register.head()''',
'''#md
The concentration column is still text, because it contains values like `<0.5` and `>100`. That is
handled in notebook 05.

## TSV and other separators
''',
'''expr = pd.read_csv(RAW + "gene_expression.tsv", sep="\\t", index_col="sample")
print(expr.shape)
expr.iloc[:5, :6]''',
'''#md
Files without a header row need `header=None` and `names=`:
''',
'''seqs = pd.read_csv(RAW + "sequences.txt", sep="\\t", header=None, names=["name", "sequence"])
seqs["length"] = seqs["sequence"].str.len()
seqs.head()''',
'''#md
## Excel files

`read_excel` needs the `openpyxl` package for `.xlsx` files. `sheet_name` chooses the sheet; `None`
reads every sheet into a dictionary.
''',
'''sites = pd.read_excel(RAW + "sites.xlsx", sheet_name="sites")
sites''',
'''all_sheets = pd.read_excel(RAW + "sites.xlsx", sheet_name=None)
print(list(all_sheets))
all_sheets["staff"].head()''',
'''#md
## Other formats, briefly

| format | read | write |
|---|---|---|
| JSON | `pd.read_json` | `df.to_json` |
| Parquet (fast, keeps types) | `pd.read_parquet` | `df.to_parquet` |
| SQL databases | `pd.read_sql` | `df.to_sql` |
| Stata, SPSS, SAS | `read_stata`, `read_spss`, `read_sas` | `to_stata` |
| clipboard | `pd.read_clipboard` | `df.to_clipboard` |

## Reading from the web

`read_csv` also accepts a URL. Seaborn ships example datasets this way, which we use in later modules:

```python
pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")
```

## Exporting

Results and cleaned data go to `datasets/processed`, never back over the raw file.
''',
'''summary = patients.groupby("site").agg(n=("patient_id", "count"), mean_age=("age", "mean")).round(1)
summary''',
'''from pathlib import Path
Path(PROCESSED).mkdir(exist_ok=True)

summary.to_csv(PROCESSED + "age_by_site.csv")
patients.to_csv(PROCESSED + "patients_copy.csv", index=False)     # index=False: do not write 0, 1, 2 ...
print(pd.read_csv(PROCESSED + "age_by_site.csv"))''',
'''#md
Several tables into one Excel workbook:
''',
'''with pd.ExcelWriter(PROCESSED + "patients_summary.xlsx") as writer:
    summary.to_excel(writer, sheet_name="by_site")
    patients.groupby("group")["age"].describe().round(1).to_excel(writer, sheet_name="by_group")
print(pd.ExcelFile(PROCESSED + "patients_summary.xlsx").sheet_names)''',
'''for f in ["age_by_site.csv", "patients_copy.csv", "patients_summary.xlsx"]:
    Path(PROCESSED + f).unlink()           # tidy up the demo files''',
],
[PG, "[IO tools: reading and writing](https://pandas.pydata.org/docs/user_guide/io.html)",
 "[read_csv reference](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)"],
exercises_note=NOTE)

lesson(F + "04_Data_Exploration.ipynb", "Exploring data",
["inspect a dataset with head, tail, sample, shape and info",
 "summarise numeric and categorical columns with describe",
 "count categories with value_counts",
 "find missing values and unusual values",
 "interpret what each summary tells you"],
"""
Before analysing, get to know the data: how big it is, what each column holds, what is missing, what
looks wrong. A few minutes here prevents conclusions built on errors. This notebook uses the
`clinic_study.csv` dataset, which has several deliberate problems for you to find.
""",
[
SETUP,
'''df = pd.read_csv(RAW + "clinic_study.csv")''',
'''#md
## head, tail and sample
''',
'''df.head()''',
'''df.tail(3)''',
'''df.sample(5, random_state=1)''',
'''#md
`head` shows how the file starts, `tail` whether it ends cleanly (no totals row or notes), and `sample`
shows rows from the middle, where problems often hide.

## Size and structure
''',
'''print(df.shape)
df.info()''',
'''#md
### Reading `info()`

- **RangeIndex**: number of rows
- **Non-Null Count**: values present in each column. Columns with fewer than the row count have missing
  values: here `sbp_6m` and `glucose_6m`, the six-month follow-up
- **Dtype**: `float64` for `age_years` although ages are whole numbers. Integer columns become float
  when they contain missing values, or (as here) when a value has a decimal point
- **memory usage**: useful for large files

## describe: numeric columns
''',
'''df.describe().round(2)''',
'''#md
### Reading `describe()`

| row | meaning | what to look for |
|---|---|---|
| count | non-missing values | differences between columns mean missing data |
| mean, std | average and spread | |
| min, max | extremes | impossible values |
| 25%, 50%, 75% | quartiles; 50% is the median | mean far from median suggests skew |

Problems visible here:

- `age_years` has a minimum below zero and a maximum of 150: impossible ages, probably entry errors
- `height_m` has a maximum far above any human height in metres: some heights were entered in centimetres

## describe: text columns
''',
'''df.describe(exclude="number")''',
'''#md
`unique` is the number of different values and `top` the most common. Five clinic values for what are
three clinics (East, North, West), and five sex values instead of two, mean inconsistent spelling.
`value_counts` shows exactly what is there:

## value_counts
''',
'''df["clinic"].value_counts()''',
'''#md
Two entries look like `West`. Printing the unique values with `repr` reveals a trailing space in one:
''',
'''print([repr(c) for c in df["clinic"].unique()])''',
'''df["sex"].value_counts(dropna=False)''',
'''df["arm"].value_counts(normalize=True).round(3)''',
'''#md
`normalize=True` gives proportions. `dropna=False` includes a count of missing values.

## Missing values
''',
'''missing = pd.DataFrame({"n_missing": df.isna().sum(), "percent": (df.isna().mean() * 100).round(1)})
missing[missing["n_missing"] > 0]''',
'''#md
The follow-up measurements are missing for the same participants (people who did not return), which
matters later: comparing only those who returned may not represent everyone who enrolled.
''',
'''print(((df["sbp_6m"].isna()) == (df["glucose_6m"].isna())).all())''',
'''#md
## Duplicates
''',
'''print(df.duplicated().sum(), "fully duplicated rows")
print(df["participant"].duplicated().sum(), "repeated participant IDs")
df[df["participant"].duplicated(keep=False)].sort_values("participant").head(6)''',
'''#md
## Unusual values
''',
'''print("ages outside 18-100:")
print(df.loc[(df["age_years"] < 18) | (df["age_years"] > 100), ["participant", "age_years"]])
print("\\nheights above 3 m:")
print(df.loc[df["height_m"] > 3, ["participant", "height_m"]])''',
'''#md
## Unique values and ranges
''',
'''print(df["smoking"].unique())
print(df["participant"].nunique(), "unique participants in", len(df), "rows")
print(df["baseline_date"].min(), "to", df["baseline_date"].max())''',
'''#md
## Relationships: a first glance

Correlations between numeric columns and a cross-tabulation of two categories. These are only first
impressions before cleaning.
''',
'''df[["age_years", "weight_kg", "sbp_baseline", "glucose_baseline"]].corr().round(2)''',
'''pd.crosstab(df["arm"], df["smoking"])''',
'''#md
## An exploration checklist

1. how many rows and columns? what is one row?
2. are the types right (numbers as numbers, dates as dates)?
3. which columns have missing values, and is there a pattern?
4. are categories spelled consistently?
5. are there impossible or extreme values?
6. are there duplicate rows or IDs?

The answers become the cleaning plan for notebook 05 and the capstone project.
''',
],
[PG, "[Essential basic functionality](https://pandas.pydata.org/docs/user_guide/basics.html)",
 "[describe reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)"],
exercises_note=NOTE)

lesson(F + "05_Data_Cleaning.ipynb", "Cleaning data",
["find and handle missing values: drop, fill or flag",
 "remove duplicate rows",
 "standardise text categories",
 "convert columns to the right types, including dates and numbers stored as text",
 "detect and handle impossible values and outliers",
 "write a cleaned dataset"],
"""
This notebook cleans the laboratory sample register `sample_register_raw.csv`, which has the problems
real registers have: mixed spellings, blanks, results stored as text, an impossible temperature code and
duplicated rows. Every step is code, so the cleaning is documented and repeatable.
""",
[
SETUP,
'''raw = pd.read_csv(RAW + "sample_register_raw.csv")
print(raw.shape)
raw.head(8)''',
'''#md
Work on a copy so the raw data stays available for comparison.
''',
'''df = raw.copy()
df.info()''',
'''#md
## 1. Duplicates
''',
'''print(df.duplicated().sum(), "duplicated rows")
df = df.drop_duplicates()
print(df.shape, "| sample IDs unique now:", df["sample_id"].is_unique)''',
'''#md
`drop_duplicates()` keeps the first copy of rows that are identical in every column. With
`subset=["sample_id"]` it would compare only that column. Check that the remaining IDs are unique, as
here.

## 2. Standardising text
''',
'''print(df["sample_type"].value_counts())''',
'''df["sample_type"] = df["sample_type"].str.strip().str.capitalize()
df["sample_type"].value_counts()''',
'''print(df["result"].value_counts(dropna=False))''',
'''#md
For categories with different words for the same thing, a mapping dictionary is clearest. Anything not
in the map becomes NaN, so unexpected spellings show up instead of slipping through.
''',
'''result_map = {"positive": "Positive", "negative": "Negative", "neg": "Negative"}
df["result"] = df["result"].str.strip().str.lower().map(result_map)
df["result"].value_counts(dropna=False)''',
'''df["technician"] = df["technician"].str.upper()
df["technician"].value_counts(dropna=False)''',
'''#md
## 3. Dates
''',
'''print(df["collected"].head(3).tolist())
df["collected"] = pd.to_datetime(df["collected"], format="%d/%m/%Y")
print(df["collected"].dtype, df["collected"].min().date(), df["collected"].max().date())''',
'''#md
Giving `format=` avoids ambiguity: is `01/05/2025` the 1st of May or the 5th of January? Here the file
uses day/month/year. If some entries do not match, `errors="coerce"` turns them into missing values
(`NaT`) instead of stopping.

## 4. Numbers stored as text

The concentration column mixes numbers with `<0.5` (below the detection limit), `>100` (above the
upper limit) and `not done`.
''',
'''print(df["concentration"].value_counts().head(10))''',
'''#md
A common approach: keep a flag saying whether a value was censored, and store a numeric value for
analysis. Here values below the limit are set to half the limit, a simple convention; values above the
limit are set to the limit itself. Whatever rule you choose, record it.
''',
'''conc = df["concentration"].str.strip()
df["conc_flag"] = np.select([conc.str.startswith("<"), conc.str.startswith(">"), conc == "not done"],
                            ["below_limit", "above_limit", "not_done"], default="measured")
numeric = pd.to_numeric(conc.str.lstrip("<>"), errors="coerce")
df["concentration_num"] = np.where(df["conc_flag"] == "below_limit", numeric / 2, numeric)
df[["concentration", "conc_flag", "concentration_num"]].drop_duplicates().head(8)''',
'''df["conc_flag"].value_counts()''',
'''#md
`pd.to_numeric(..., errors="coerce")` converts what it can and turns the rest (`not done`) into NaN.

## 5. Impossible values
''',
'''df["temperature_c"].describe().round(2)''',
'''print((df["temperature_c"] == 99.0).sum(), "readings of exactly 99.0")
print(df["temperature_c"].sort_values().tail(8).tolist())''',
'''#md
Every other reading is below 7 °C, then there is a jump to exactly 99.0 °C, several times over. That is a
code for "not recorded", not a real storage temperature. The mean and standard deviation above are
badly distorted by it. Replace it with NaN:
''',
'''df["temperature_c"] = df["temperature_c"].replace(99.0, np.nan)
df["temperature_c"].describe().round(2)''',
'''#md
Now flag samples stored outside the acceptable 2-8 °C range:
''',
'''df["temp_ok"] = df["temperature_c"].between(2, 8)
print(df["temp_ok"].value_counts())
df.loc[~df["temp_ok"] & df["temperature_c"].notna(), ["sample_id", "temperature_c"]].head()''',
'''#md
## 6. Outliers

An *outlier* is a value far from the rest. It may be an error or a real extreme; investigate before
removing. A standard rule flags values more than 1.5 × IQR below the first quartile or above the
third quartile (the box-plot rule).
''',
'''def iqr_flags(s, k=1.5):
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    return (s < q1 - k * iqr) | (s > q3 + k * iqr)

measured = df.loc[df["conc_flag"] == "measured", "concentration_num"]
print(measured.describe().round(2))
print(iqr_flags(measured).sum(), "measured concentrations flagged by the IQR rule")''',
'''#md
None are flagged: the measured values all lie between the detection limits, in a fairly narrow range.
On other columns or datasets, look at the flagged rows before deciding whether to correct, keep or
exclude them, and record the decision.
''',
'''#md
## 7. Missing values

Options, and when each fits:

| approach | code | use when |
|---|---|---|
| keep and report | `isna().sum()` | always: know how much is missing |
| drop rows | `dropna(subset=[...])` | few missing, and missingness unrelated to the outcome |
| fill with a value | `fillna(value)` | a meaningful default exists ("Unknown") |
| fill with a statistic | `fillna(s.median())` | quick descriptive work; it understates variability |
| flag | `s.isna()` as a new column | to analyse who is missing |
''',
'''df.isna().sum()''',
'''df["technician"] = df["technician"].fillna("UNKNOWN")
print(df["result"].isna().sum(), "results missing: kept as missing, not guessed")
complete_results = df.dropna(subset=["result"])
print(len(df), "rows;", len(complete_results), "with a result")''',
'''#md
Missing test results are kept as missing: inventing a result would be wrong. Analyses of positivity use
`complete_results` and report how many were excluded.

## 8. Types and tidy columns
''',
'''df["sample_type"] = df["sample_type"].astype("category")
df["result"] = df["result"].astype("category")
df = df.drop(columns=["concentration"]).rename(columns={"concentration_num": "concentration"})
df.dtypes''',
'''#md
## 9. Check and save
''',
'''assert df["sample_id"].is_unique
assert set(df["sample_type"].dropna()) <= {"Blood", "Urine", "Saliva"}
assert df["temperature_c"].dropna().lt(50).all()
print(f"raw {raw.shape} -> clean {df.shape}")

df.to_csv(PROCESSED + "sample_register_clean.csv", index=False)
pd.read_csv(PROCESSED + "sample_register_clean.csv").head()''',
'''#md
The `assert` lines make the cleaning self-checking: if a future version of the raw file has a new
spelling or a new error code, the notebook stops and tells you.

## A summary of the cleaning log

| problem | action |
|---|---|
| duplicated rows | removed |
| sample type in mixed case with spaces | stripped and capitalised |
| result in five spellings | mapped to Positive / Negative; blanks kept missing |
| technician initials in mixed case | upper case; blanks set to UNKNOWN |
| dates as day/month/year text | converted to dates |
| concentration as text with `<`, `>`, `not done` | flag column plus numeric value |
| temperature code 99.0 | set to missing; range flag added |
''',
],
[PG, "[Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)",
 "[Working with text data](https://pandas.pydata.org/docs/user_guide/text.html)",
 "[Hadley Wickham, Tidy data (2014)](https://doi.org/10.18637/jss.v059.i10)"],
exercises_note=NOTE)

lesson(F + "06_Data_Manipulation.ipynb", "Selecting, filtering and transforming",
["select columns, and rows by label with loc and by position with iloc",
 "filter rows with conditions, isin, between and query",
 "sort by one or more columns",
 "create columns with vectorised maths, np.where, cut, map and apply",
 "work with dates: extract parts, compute intervals, resample"],
"""
Most analysis code selects some rows and columns, adds a calculated variable, sorts the result and
looks at it. This notebook covers those everyday operations, using the patients and lab results tables
and a simulated two-year sales series.
""",
[
SETUP,
'''patients = pd.read_csv(RAW + "patients.csv", parse_dates=["enrolled"])
labs = pd.read_csv(RAW + "lab_results.csv", parse_dates=["visit_date"])
patients.head()''',
'''#md
## Selecting columns
''',
'''patients[["patient_id", "age", "sex"]].head(3)''',
'''patients.filter(like="_").head(3)          # columns whose name contains "_"''',
'''patients.select_dtypes("number").head(3)''',
'''#md
## loc and iloc

- `df.loc[rows, columns]` selects by **label** (index labels and column names); slices **include** the end
- `df.iloc[rows, columns]` selects by **position**; slices exclude the end, like Python
''',
'''print(patients.iloc[0, 3])                  # first row, fourth column
patients.iloc[:3, :4]''',
'''patients.loc[0:2, ["patient_id", "age"]]   # labels 0, 1 and 2''',
'''p = patients.set_index("patient_id")
p.loc[["P0003", "P0010"], ["site", "age", "group"]]''',
'''#md
## Filtering rows

A condition gives a True/False Series; using it inside `[]` or `.loc[]` keeps the True rows. As with
NumPy, combine with `&`, `|`, `~` and brackets.
''',
'''older = patients[patients["age"] >= 65]
print(len(older), "patients aged 65 or more")
patients[(patients["sex"] == "F") & (patients["smoker"] == "Yes")].head()''',
'''patients[patients["site"].isin(["Site A", "Site C"])].shape''',
'''patients[patients["age"].between(30, 39)].shape''',
'''#md
`query` writes the same conditions as a string, which is easier to read for long filters. `@` refers
to a Python variable:
''',
'''min_age = 60
patients.query("group == 'Treatment' and age >= @min_age and smoker == 'No'").head()''',
'''#md
Filtering and assigning at once uses `loc` with a condition and a column:
''',
'''p2 = patients.copy()
p2.loc[p2["weight_kg"].isna(), "weight_flag"] = "missing"
p2["weight_flag"].value_counts(dropna=False)''',
'''#md
## Sorting
''',
'''patients.sort_values("age", ascending=False).head(3)''',
'''patients.sort_values(["site", "age"], ascending=[True, False]).head(4)''',
'''patients.nlargest(3, "weight_kg")[["patient_id", "weight_kg"]]''',
'''#md
## Creating new columns

### Vectorised arithmetic

The fastest and clearest way: operate on whole columns.
''',
'''patients["height_m"] = patients["height_cm"] / 100
patients["bmi"] = (patients["weight_kg"] / patients["height_m"] ** 2).round(1)
patients[["weight_kg", "height_cm", "bmi"]].head()''',
'''#md
`assign` creates columns and returns a new DataFrame, which chains well:
''',
'''(patients
 .assign(age_decade=lambda d: d["age"] // 10 * 10,
         is_smoker=lambda d: d["smoker"] == "Yes")
 [["patient_id", "age", "age_decade", "is_smoker"]]
 .head())''',
'''#md
### Conditions: np.where and np.select
''',
'''patients["older"] = np.where(patients["age"] >= 65, "65+", "under 65")
patients["bmi_class"] = np.select(
    [patients["bmi"] < 18.5, patients["bmi"] < 25, patients["bmi"] < 30, patients["bmi"] >= 30],
    ["Underweight", "Normal", "Overweight", "Obese"], default="Unknown")
patients["bmi_class"].value_counts()''',
'''#md
`default="Unknown"` catches the rows where BMI is missing, because NaN fails every comparison.

### Binning: cut
''',
'''patients["age_group"] = pd.cut(patients["age"], bins=[17, 34, 49, 64, 120],
                               labels=["18-34", "35-49", "50-64", "65+"])
patients["age_group"].value_counts().sort_index()''',
'''#md
`bins` are edges; each bin includes its right edge, so 34 falls in 18-34. `pd.qcut` makes bins with
equal numbers of rows instead (quartiles, deciles).

### map: translate values
''',
'''patients["sex_label"] = patients["sex"].map({"F": "Female", "M": "Male"})
patients["sex_label"].value_counts()''',
'''#md
### apply: any function

`apply` runs a Python function on each value (Series) or each row (`axis=1`). It is flexible but slow
on large data; prefer vectorised operations when one exists.
''',
'''def risk_label(row):
    if row["age"] >= 65 and row["smoker"] == "Yes":
        return "high"
    if row["age"] >= 65 or row["smoker"] == "Yes":
        return "moderate"
    return "low"

patients["risk"] = patients.apply(risk_label, axis=1)
patients["risk"].value_counts()''',
'''#md
The same result, vectorised. The two methods agree:
''',
'''n_flags = (patients["age"] >= 65).astype(int) + (patients["smoker"] == "Yes").astype(int)
vectorised = n_flags.map({0: "low", 1: "moderate", 2: "high"})
print((vectorised == patients["risk"]).all())''',
'''#md
## String columns

The `.str` accessor applies string methods to every value:
''',
'''print(patients["patient_id"].str[1:].astype(int).head(3).tolist())
print(patients["site"].str.replace("Site ", "").head(3).tolist())
print(patients["site"].str.contains("A").sum())''',
'''#md
## Dates

The `.dt` accessor gives parts of dates.
''',
'''labs["year"] = labs["visit_date"].dt.year
labs["month"] = labs["visit_date"].dt.month_name()
labs["weekday"] = labs["visit_date"].dt.day_name()
labs[["visit_date", "year", "month", "weekday"]].head()''',
'''#md
Differences between dates are `Timedelta` values; `.dt.days` turns them into numbers:
''',
'''first_visit = labs.groupby("patient_id")["visit_date"].transform("min")
labs["days_since_first"] = (labs["visit_date"] - first_visit).dt.days
labs[["patient_id", "visit", "visit_date", "days_since_first"]].head(6)''',
'''#md
### Time series: resampling

The sales data have one row per shop per day. `resample` regroups by time period; it needs the dates
as the index.
''',
'''sales = pd.read_csv(RAW + "daily_sales.csv", parse_dates=["date"])
sales["revenue"] = sales["units"] * sales["price"]
north = sales[sales["shop"] == "North"].set_index("date")
monthly = north["revenue"].resample("MS").sum().round(0)
monthly.head()''',
'''#md
`"MS"` means month start. Others: `"D"` day, `"W"` week, `"QS"` quarter, `"YS"` year. A rolling mean
smooths day-to-day noise:
''',
'''north["units_7day"] = north["units"].rolling(7).mean()
north[["units", "units_7day"]].iloc[5:10]''',
'''#md
The first six rows of a 7-day rolling mean are NaN because there are not yet seven days to average.

## Method chaining

Several steps written as one readable pipeline:
''',
'''(patients
 .query("smoker == 'Yes'")
 .assign(bmi_rounded=lambda d: d["bmi"].round())
 .sort_values("bmi", ascending=False)
 [["patient_id", "site", "age", "bmi"]]
 .head(5))''',
],
[PG, "[Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html)",
 "[Time series and date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html)",
 "[Copy-on-write in pandas](https://pandas.pydata.org/docs/user_guide/copy_on_write.html)"],
exercises_note=NOTE)

lesson(F + "07_Grouping_and_Aggregation.ipynb", "Grouping and aggregation",
["explain split-apply-combine",
 "summarise by one or more groups with groupby",
 "compute several statistics at once with agg and named aggregation",
 "add group statistics to every row with transform",
 "build frequency and summary tables with crosstab and pivot_table"],
"""
"What is the mean glucose by group?", "How many positives per site and month?" Group summaries answer
most descriptive questions. pandas handles them with `groupby`: **split** the rows into groups,
**apply** a calculation to each, **combine** the results into a table.
""",
[
SETUP,
'''patients = pd.read_csv(RAW + "patients.csv")
labs = pd.read_csv(RAW + "lab_results.csv")
clean = pd.read_csv(PROCESSED + "sample_register_clean.csv", parse_dates=["collected"])''',
'''#md
`sample_register_clean.csv` is written by notebook 05. Run that notebook first if this cell fails.

## One group, one statistic
''',
'''patients.groupby("site")["age"].mean().round(1)''',
'''patients.groupby("site").size()          # rows per group''',
'''#md
## Several groups
''',
'''patients.groupby(["site", "sex"])["age"].mean().round(1)''',
'''#md
The result has a two-level index. `unstack` spreads the inner level into columns, which is often
easier to read:
''',
'''patients.groupby(["site", "sex"])["age"].mean().round(1).unstack()''',
'''#md
## Several statistics: agg
''',
'''patients.groupby("group")["age"].agg(["count", "mean", "median", "std", "min", "max"]).round(1)''',
'''#md
**Named aggregation** chooses the column, the function and the output name together. This is the
clearest way to build a summary table:
''',
'''summary = patients.groupby("site").agg(
    n=("patient_id", "count"),
    mean_age=("age", "mean"),
    sd_age=("age", "std"),
    pct_female=("sex", lambda s: (s == "F").mean() * 100),
    weight_missing=("weight_kg", lambda s: s.isna().sum()),
).round(1)
summary''',
'''#md
Reading the table: one row per site, with the number of patients, their mean and standard deviation of
age, the percentage who are female, and how many weights are missing. Compare sites on these before
comparing outcomes, because differences in who attends a site can explain differences in results.

## Positivity by group

The mean of a True/False column is the proportion of True values:
''',
'''tested = clean.dropna(subset=["result"])
by_type = tested.groupby("sample_type", observed=True).agg(
    tests=("result", "size"),
    positives=("result", lambda r: (r == "Positive").sum()),
)
by_type["positivity_pct"] = (by_type["positives"] / by_type["tests"] * 100).round(1)
by_type''',
'''#md
`observed=True` limits the result to categories that occur, which is the recommended setting for
categorical columns.

## Grouping by time
''',
'''monthly = (tested
           .groupby(tested["collected"].dt.to_period("M"))
           .agg(tests=("result", "size"), positive_pct=("result", lambda r: (r == "Positive").mean() * 100))
           .round(1))
monthly.head(6)''',
'''#md
## transform: group values on every row

`agg` gives one row per group. `transform` returns a value **for every original row**, which is how you
compare each row to its group.
''',
'''labs["patient_mean_glucose"] = labs.groupby("patient_id")["glucose_mmol"].transform("mean")
labs["diff_from_own_mean"] = (labs["glucose_mmol"] - labs["patient_mean_glucose"]).round(2)
labs[["patient_id", "visit", "glucose_mmol", "patient_mean_glucose", "diff_from_own_mean"]].head(6).round(2)''',
'''#md
Standardising within groups (z-scores per site) is a typical use:
''',
'''p = patients.copy()
g = p.groupby("site")["age"]
p["age_z_within_site"] = ((p["age"] - g.transform("mean")) / g.transform("std")).round(2)
p[["site", "age", "age_z_within_site"]].head()''',
'''#md
## filter: keep whole groups

Keep only patients with three or more lab visits:
''',
'''three_plus = labs.groupby("patient_id").filter(lambda g: len(g) >= 3)
print(labs["patient_id"].nunique(), "patients;", three_plus["patient_id"].nunique(), "with 3+ visits")''',
'''#md
## First, last and change per group
''',
'''bp = (labs.sort_values(["patient_id", "visit"])
      .groupby("patient_id")["systolic_bp"]
      .agg(first="first", last="last", n="size"))
bp["change"] = bp["last"] - bp["first"]
bp[bp["n"] > 1]["change"].describe().round(1)''',
'''#md
## crosstab: frequency tables
''',
'''pd.crosstab(patients["site"], patients["smoker"], margins=True)''',
'''pd.crosstab(patients["site"], patients["smoker"], normalize="index").round(3) * 100''',
'''#md
`normalize="index"` gives row percentages: within each site, the percentage of smokers and non-smokers.

## pivot_table: summaries in a grid
''',
'''merged = labs.merge(patients[["patient_id", "group"]], on="patient_id")
pd.pivot_table(merged, values="systolic_bp", index="visit", columns="group", aggfunc="mean").round(1)''',
'''#md
`merge` joins the two tables (next notebook). The table shows mean systolic blood pressure at each visit
for each study group, a typical way to present follow-up data.
''',
],
[PG, "[Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html)",
 "[Reshaping and pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html)"],
exercises_note=NOTE)

lesson(F + "08_Merging_and_Reshaping.ipynb", "Merging and reshaping",
["join tables with merge, and choose the right join type",
 "check merges for unexpected row counts",
 "stack tables with concat",
 "reshape between wide and long formats with melt, pivot and pivot_table"],
"""
Data usually comes in several tables: participants in one, lab results in another, site details in a
third. Merging links them through a shared key. Reshaping changes the layout: one row per participant
with a column per visit (*wide*), or one row per participant-visit (*long*). Plotting and grouping
usually want long data; reports often want wide.
""",
[
SETUP,
'''patients = pd.read_csv(RAW + "patients.csv")
labs = pd.read_csv(RAW + "lab_results.csv")
sites = pd.read_excel(RAW + "sites.xlsx", sheet_name="sites")
print(patients.shape, labs.shape, sites.shape)''',
'''#md
## merge

`pd.merge(left, right, on="key", how=...)` matches rows that share a key value.

| how | keeps |
|---|---|
| `"inner"` (default) | only keys found in both tables |
| `"left"` | every row of the left table; NaN where the right has no match |
| `"right"` | every row of the right table |
| `"outer"` | every key from either table |

A small example makes the differences visible:
''',
'''a = pd.DataFrame({"id": ["P1", "P2", "P3"], "age": [34, 51, 47]})
b = pd.DataFrame({"id": ["P2", "P3", "P4"], "glucose": [7.8, 6.1, 5.2]})
for how in ["inner", "left", "right", "outer"]:
    print(how)
    print(pd.merge(a, b, on="id", how=how), "\\n")''',
'''#md
## One-to-many: patients and their visits

Each patient has several lab rows, so the patient details repeat on each visit row:
''',
'''full = labs.merge(patients, on="patient_id", how="left", validate="many_to_one")
print(labs.shape, "->", full.shape)
full.head(4)''',
'''#md
`validate="many_to_one"` makes pandas check that each patient appears only once in `patients`; if not,
it raises an error instead of silently multiplying rows. Also check the row count: after a left join on
a unique key, it should equal the left table's row count.

## Adding site information
''',
'''full = full.merge(sites, on="site", how="left")
full[["patient_id", "visit", "site", "region", "beds"]].head()''',
'''#md
## Different key names, and the indicator column
''',
'''register = pd.read_csv(RAW + "sample_register_raw.csv").drop_duplicates()
check = register[["sample_id", "patient_id"]].merge(
    patients[["patient_id", "site"]].rename(columns={"patient_id": "pid"}),
    left_on="patient_id", right_on="pid", how="left", indicator=True)
check["_merge"].value_counts()''',
'''#md
`indicator=True` adds `_merge`, saying whether each row matched (`both`) or not (`left_only`). It is the
quickest way to find IDs that do not link, a common data-quality check.

## concat: stacking tables

`concat` puts tables on top of each other (same columns) or side by side.
''',
'''batch1 = pd.DataFrame({"sample": ["S1", "S2"], "value": [5.1, 6.3]})
batch2 = pd.DataFrame({"sample": ["S3", "S4"], "value": [4.8, 7.0]})
pd.concat([batch1, batch2], ignore_index=True)''',
'''pd.concat([batch1.assign(batch=1), batch2.assign(batch=2)], ignore_index=True)''',
'''#md
Reading many files with the same layout and stacking them is a common pattern:

```python
from pathlib import Path
frames = [pd.read_csv(f).assign(source=f.name) for f in Path("data").glob("run_*.csv")]
combined = pd.concat(frames, ignore_index=True)
```

## Wide and long data
''',
'''wide = labs.pivot(index="patient_id", columns="visit", values="systolic_bp")
wide.columns = [f"sbp_visit{v}" for v in wide.columns]
wide.head()''',
'''#md
That is **wide**: one row per patient, one column per visit. `pivot` requires each (index, column) pair
to be unique; when it is not, use `pivot_table` with an `aggfunc`.

`melt` turns wide back into **long**:
''',
'''long = wide.reset_index().melt(id_vars="patient_id", var_name="visit", value_name="systolic_bp")
long = long.dropna().sort_values(["patient_id", "visit"])
long.head(6)''',
'''#md
## Several measurements: long format for plotting

Lab results have three measurements per visit. Melting them into one column lets you group or plot all
of them in one step:
''',
'''measures = labs.melt(id_vars=["patient_id", "visit"],
                     value_vars=["glucose_mmol", "haemoglobin_g_dl", "systolic_bp"],
                     var_name="test", value_name="value")
print(measures.shape)
measures.groupby("test")["value"].describe().round(2)''',
'''#md
## Gene expression: from a matrix to tidy data

Expression data come as a matrix (samples × genes). Melting gives one row per sample-gene, which makes
per-gene comparisons a simple groupby:
''',
'''expr = pd.read_csv(RAW + "gene_expression.tsv", sep="\\t")
tidy = expr.melt(id_vars=["sample", "condition"], var_name="gene", value_name="expression")
print(expr.shape, "->", tidy.shape)

by_gene = tidy.pivot_table(index="gene", columns="condition", values="expression", aggfunc="mean")
by_gene["difference"] = by_gene["treated"] - by_gene["control"]
by_gene.sort_values("difference", key=abs, ascending=False).head(5).round(2)''',
'''#md
The genes with the largest mean differences between conditions are candidates for a closer look. A
difference in means is not yet evidence: it needs the spread and the number of samples (a statistical
test), which is beyond this course.

## stack and unstack

These move levels between the index and the columns, and are the index-based relatives of melt and pivot:
''',
'''two_level = patients.groupby(["site", "group"])["age"].mean().round(1)
print(two_level.unstack())
print(two_level.unstack().stack().head(4))''',
],
[PG, "[Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html)",
 "[Reshaping and pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html)"],
exercises_note=NOTE)

exercises(F, "Pandas", "pandas",
"""Exercises for notebooks 01 to 08 of this folder. Most use `../../datasets/raw/patients.csv`,
`lab_results.csv` and `daily_sales.csv`, plus two Seaborn example datasets downloaded from the
internet (`tips` and `penguins`).""",
[
("Load `patients.csv`. Print the number of rows and columns, the column types, and the first five rows.",
 '''import pandas as pd
import numpy as np
RAW = "../../datasets/raw/"
patients = pd.read_csv(RAW + "patients.csv", parse_dates=["enrolled"])
print(patients.shape)
print(patients.dtypes)
patients.head()'''),
("Create a DataFrame by hand with columns `sample`, `type` and `value` for four samples, then add a column `value_x10`.",
 '''d = pd.DataFrame({"sample": ["S1", "S2", "S3", "S4"], "type": ["Blood", "Urine", "Blood", "Saliva"],
                  "value": [5.1, 2.3, 6.8, 1.9]})
d["value_x10"] = d["value"] * 10
d'''),
("Use `describe` on the patients' numeric columns. Which column has missing values, and how many?",
 '''print(patients.describe().round(1))
print(patients.isna().sum()[patients.isna().sum() > 0])''', "weight_kg has 10 missing values (count 290 out of 300)."),
("How many patients are there in each site, and what percentage are smokers overall?",
 '''print(patients["site"].value_counts())
print(f"{(patients['smoker'] == 'Yes').mean():.1%}")'''),
("Select female patients over 60 from Site B, showing only patient_id, age and group, sorted by age (oldest first).",
 '''(patients.query("sex == 'F' and age > 60 and site == 'Site B'")
 [["patient_id", "age", "group"]].sort_values("age", ascending=False))'''),
("Add a BMI column (height is in cm) and a column `bmi_class` with Underweight / Normal / Overweight / Obese. How many patients fall in each class?",
 '''patients["bmi"] = patients["weight_kg"] / (patients["height_cm"] / 100) ** 2
patients["bmi_class"] = pd.cut(patients["bmi"], [0, 18.5, 25, 30, 100],
                               labels=["Underweight", "Normal", "Overweight", "Obese"], right=False)
patients["bmi_class"].value_counts(dropna=False)''', "`right=False` makes each bin include its left edge, so BMI 25.0 is Overweight, as in the standard definition."),
("Fill missing weights with the median weight of the same sex, and confirm no weights are missing afterwards.",
 '''filled = patients.copy()
filled["weight_kg"] = filled["weight_kg"].fillna(filled.groupby("sex")["weight_kg"].transform("median"))
print(filled["weight_kg"].isna().sum())'''),
("Load `lab_results.csv`. Compute the mean glucose, haemoglobin and systolic BP at each visit number.",
 '''labs = pd.read_csv(RAW + "lab_results.csv", parse_dates=["visit_date"])
labs.groupby("visit")[["glucose_mmol", "haemoglobin_g_dl", "systolic_bp"]].mean().round(2)'''),
("Merge the lab results with the patients' group and compute, per group, the number of visits, the mean glucose and the proportion of visits with glucose of 7.0 or more.",
 '''m = labs.merge(patients[["patient_id", "group"]], on="patient_id", how="left", validate="many_to_one")
m.groupby("group").agg(visits=("visit", "size"), mean_glucose=("glucose_mmol", "mean"),
                       prop_high=("glucose_mmol", lambda g: (g >= 7).mean())).round(3)'''),
("Reshape the systolic BP into wide format (one row per patient, one column per visit), then back to long format.",
 '''wide = labs.pivot(index="patient_id", columns="visit", values="systolic_bp")
print(wide.head())
long = wide.reset_index().melt(id_vars="patient_id", value_name="systolic_bp").dropna()
long.head()'''),
("From `daily_sales.csv`, compute total revenue (units × price) per shop per year, as a table with shops as rows and years as columns.",
 '''sales = pd.read_csv(RAW + "daily_sales.csv", parse_dates=["date"])
sales["revenue"] = sales["units"] * sales["price"]
sales.pivot_table(index="shop", columns=sales["date"].dt.year, values="revenue", aggfunc="sum").round(0)'''),
("In the sales data, compare the mean units sold on promotion days and other days, for each shop.",
 '''sales.groupby(["shop", "promo"])["units"].mean().unstack().round(1)'''),
("Load the Seaborn `tips` dataset with `pd.read_csv(\"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv\")`. Add a `tip_pct` column (tip as a percentage of total_bill) and find the mean tip percentage by day and time.",
 '''tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100
tips.pivot_table(index="day", columns="time", values="tip_pct", aggfunc="mean", observed=True).round(1)'''),
("Load the Seaborn `penguins` dataset in the same way (`penguins.csv`). How many rows have any missing value? Drop them, then give the mean body mass per species and sex.",
 '''peng = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")
print(peng.isna().any(axis=1).sum(), "rows with a missing value")
peng = peng.dropna()
peng.groupby(["species", "sex"])["body_mass_g"].mean().unstack().round(0)'''),
])
print("module 06 written")
