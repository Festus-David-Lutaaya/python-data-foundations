from nb import build

D = "notebooks/"

# ---------------------------------------------------------------- 09
build(D + "09_numpy_arrays.ipynb", [
'''#md
# 09 NumPy arrays

NumPy gives Python fast arrays of numbers. pandas, matplotlib and scikit-learn
are all built on it.

The key difference from a list: operations apply to every element at once,
with no loop, and run in compiled code.
''',
'''import numpy as np

hb_list = [12.1, 10.4, 13.8, 9.7]
hb = np.array(hb_list)

print(hb * 10)            # every element
print(hb_list * 2)        # a list just repeats''',
'''#md
## Making arrays
''',
'''print(np.array([[1, 2, 3], [4, 5, 6]]))
print(np.zeros(4), np.ones((2, 3)))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))
print(np.full(3, 7.5))''',
'''#md
## Shape, size and type

An array has one type for all elements (`dtype`) and a shape.
''',
'''m = np.arange(12).reshape(3, 4)
print(m)
print("shape", m.shape, "ndim", m.ndim, "size", m.size, "dtype", m.dtype)''',
'''#md
## Indexing and slicing

`[row, column]` for 2-D arrays. `:` means "all".
''',
'''print(m[0, 1])
print(m[1])          # row 1
print(m[:, 2])       # column 2
print(m[0:2, 1:3])
print(m[-1, -1])''',
'''#md
Slices are views, not copies: changing a slice changes the original. Use `.copy()` when you need a separate array.
''',
'''a = np.arange(5)
view = a[1:3]
view[0] = 99
print(a)

b = a[1:3].copy()
b[0] = -1
print(a, b)''',
'''#md
## Boolean masks

A comparison gives an array of True/False, which you can use to select.
This is the idea behind filtering in pandas.
''',
'''hb = np.array([12.1, 10.4, 13.8, 9.7, 11.2])
low = hb < 11
print(low)
print(hb[low])
print(hb[(hb > 10) & (hb < 13)])      # & for and, | for or, brackets required
print(low.sum(), "low values")        # True counts as 1''',
'''#md
## Random numbers

Use a generator with a seed so results can be reproduced.
''',
'''rng = np.random.default_rng(42)
print(rng.normal(loc=12.5, scale=1.5, size=5).round(1))
print(rng.integers(1, 7, size=10))
print(rng.choice(["S", "I", "R"], size=8, p=[0.6, 0.1, 0.3]))
print(rng.permutation(5))''',
])

# ---------------------------------------------------------------- 10
build(D + "10_numpy_operations.ipynb", [
'''#md
# 10 NumPy operations

Element-wise maths, summaries along an axis, broadcasting, missing values and a little linear algebra.
''',
'''import numpy as np

rng = np.random.default_rng(1)
# 5 patients x 3 tests: hb, wbc, crp
labs = np.column_stack([
    rng.normal(12.5, 1.5, 5),
    rng.normal(7, 2, 5),
    rng.lognormal(1.5, 1, 5),
]).round(1)
labs''',
'''#md
## Element-wise maths
''',
'''print(np.sqrt(labs[:, 2]).round(2))
print(np.log(labs[:, 2]).round(2))
print(np.round(labs * 1.1, 1))''',
'''#md
## Summaries and axes

`axis=0` works down the rows (one result per column).
`axis=1` works across the columns (one result per row).
''',
'''print("column means:", labs.mean(axis=0).round(2))
print("row max:     ", labs.max(axis=1))
print("overall sd:  ", labs.std().round(2))
print(np.percentile(labs[:, 0], [25, 50, 75]).round(2))''',
'''#md
## Broadcasting

When shapes differ, NumPy stretches the smaller one where it can.
Standardising each column (z-scores) is one line:
''',
'''z = (labs - labs.mean(axis=0)) / labs.std(axis=0)
print(z.round(2))
print(z.mean(axis=0).round(10), z.std(axis=0))''',
'''#md
Scaling like this is exactly what `StandardScaler` does in scikit-learn.

## Missing values

`np.nan` marks a missing number. Ordinary functions return `nan` if any value is missing;
the `nan*` versions skip them.
''',
'''x = np.array([12.1, np.nan, 13.8, 9.7])
print(x.mean(), np.nanmean(x))
print(np.isnan(x), np.isnan(x).sum())
print(np.nan == np.nan)      # nan is not equal to itself: always use isnan''',
'''#md
## where, clip, unique, sort
''',
'''hb = np.array([12.1, 10.4, 13.8, 9.7, 11.2])
print(np.where(hb < 11, "Low", "Normal"))
print(np.clip(hb, 10, 13))
print(np.unique(["S", "R", "S", "I", "R"], return_counts=True))
print(np.sort(hb), np.argsort(hb))''',
'''#md
## Combining arrays
''',
'''a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(np.vstack([a, b]))
print(np.hstack([a, a]))
print(np.concatenate([a, b], axis=0))''',
'''#md
## Linear algebra

Machine learning models are mostly matrix maths. A linear model predicts `X @ w + b`.
''',
'''X = np.array([[1.0, 2.0], [2.0, 0.5], [3.0, 1.5]])
w = np.array([0.4, -0.2])
print(X @ w)                         # matrix times vector
print(X.T @ X)                       # transpose times itself

# least squares fit of y = X w, the core of linear regression
y = np.array([1.1, 0.6, 1.0])
w_hat, *_ = np.linalg.lstsq(X, y, rcond=None)
print(w_hat.round(3))''',
'''#md
## Why vectorise

Loops in Python are slow for large data. Compare:
''',
'''big = rng.normal(size=1_000_000)

import time
t = time.perf_counter()
total = 0.0
for v in big:
    total += v * v
loop_time = time.perf_counter() - t

t = time.perf_counter()
total2 = (big * big).sum()
vec_time = time.perf_counter() - t

print(f"loop {loop_time:.3f}s, numpy {vec_time:.4f}s, about {loop_time / vec_time:.0f}x faster")''',
])

# ---------------------------------------------------------------- 11
build(D + "11_pandas_basics.ipynb", [
'''#md
# 11 pandas basics

A DataFrame is a table: named columns, each with its own type, and a row index.
A Series is a single column.
''',
'''import pandas as pd

df = pd.read_csv("../data/patients.csv")
df.head()''',
'''#md
## First look at any new data
''',
'''print(df.shape)
df.info()''',
'''df.describe()''',
'''df.describe(exclude="number")      # the text columns''',
'''print(df["site"].value_counts())
print(df["site"].nunique(), df["site"].unique())''',
'''#md
## Selecting columns
''',
'''df["age"].head()''',
'''df[["patient_id", "age", "site"]].head()''',
'''#md
## Selecting rows: loc and iloc

- `loc` selects by label and condition
- `iloc` selects by position

Always use one of these with a single `[]` pair, `df.loc[rows, columns]`.
''',
'''df.iloc[0:3, 0:4]''',
'''df.loc[df["age"] > 80, ["patient_id", "age", "site"]]''',
'''#md
## Filtering

Combine conditions with `&` (and), `|` (or), `~` (not). Each condition needs brackets.
''',
'''adults_kla = df.loc[(df["age"] >= 18) & (df["site"] == "Kampala")]
len(adults_kla)''',
'''df.loc[df["site"].isin(["Gulu", "Mbale"]) & ~(df["hiv_status"] == "Unknown")].head()''',
'''#md
`query()` reads more like a sentence:
''',
'''df.query("age >= 65 and sex == 'F'").head()''',
'''#md
## New columns
''',
'''df["bmi"] = (df["weight_kg"] / (df["height_cm"] / 100) ** 2).round(1)
df["age_group"] = pd.cut(df["age"], bins=[0, 17, 49, 120], labels=["<18", "18-49", "50+"])
df[["age", "age_group", "bmi"]].head()''',
'''#md
`assign()` does the same and fits in a chain:
''',
'''(
    df
    .assign(height_m=lambda d: d["height_cm"] / 100)
    .loc[:, ["patient_id", "height_cm", "height_m"]]
    .head(3)
)''',
'''#md
## Sorting
''',
'''df.sort_values(["site", "age"], ascending=[True, False]).head()''',
'''df.nlargest(3, "weight_kg")[["patient_id", "weight_kg"]]''',
'''#md
## Summaries of one column
''',
'''print(df["age"].mean(), df["age"].median(), df["age"].std())
print(df["weight_kg"].isna().sum(), "missing weights")''',
'''#md
## Saving
''',
'''df.to_csv("patients_with_bmi.csv", index=False)
# df.to_excel("patients.xlsx", index=False)    # needs openpyxl
# df.to_parquet("patients.parquet")             # fast and keeps types, needs pyarrow

from pathlib import Path
Path("patients_with_bmi.csv").unlink()''',
'''#md
## Copies and SettingWithCopy

Since pandas 3.0, a filtered DataFrame always behaves like a copy (copy-on-write),
so changing it never changes the original. Assign changes with `.loc` on the
DataFrame you mean to change:

```python
df.loc[df["age"] > 120, "age"] = None     # right
df[df["age"] > 120]["age"] = None         # does nothing to df
```
''',
])

# ---------------------------------------------------------------- 12
build(D + "12_pandas_cleaning.ipynb", [
'''#md
# 12 Cleaning data with pandas

Real data arrive with duplicates, typos, mixed case, impossible values and text
where numbers should be. This notebook cleans `isolates_raw.csv` step by step.
''',
'''import pandas as pd
import numpy as np

raw = pd.read_csv("../data/isolates_raw.csv")
print(raw.shape)
raw.head()''',
'''raw.info()''',
'''#md
## 1. Duplicates
''',
'''print(raw.duplicated().sum(), "fully duplicated rows")
print(raw["isolate_id"].duplicated().sum(), "repeated isolate IDs")

iso = raw.drop_duplicates().copy()
print(iso.shape)''',
'''#md
## 2. Text: spaces and case
''',
'''print(iso["specimen"].value_counts())''',
'''iso["specimen"] = iso["specimen"].str.strip().str.capitalize()
iso["specimen"].value_counts()''',
'''#md
The `.str` accessor gives every string method from notebook 02, applied to the whole column.

## 3. Consistent categories
''',
'''for col in ["ciprofloxacin", "ceftriaxone"]:
    print(col, iso[col].value_counts(dropna=False).to_dict())''',
'''for col in ["ciprofloxacin", "ceftriaxone"]:
    iso[col] = (
        iso[col]
        .str.strip()
        .str.upper()
        .replace({"N/A": np.nan, "": np.nan})
    )
    iso[col] = pd.Categorical(iso[col], categories=["S", "I", "R"], ordered=True)

iso["ciprofloxacin"].value_counts(dropna=False)''',
'''#md
## 4. Dates

Dates were typed as day/month/year. Tell pandas the format rather than letting it guess.
''',
'''iso["collected"] = pd.to_datetime(iso["collected"], format="%d/%m/%Y")
iso["month"] = iso["collected"].dt.to_period("M")
iso["weekday"] = iso["collected"].dt.day_name()
iso[["collected", "month", "weekday"]].head()''',
'''#md
## 5. Numbers stored as text

MIC values contain `>4`, `<=0.06` and `not done`. Keep the sign in its own column
and turn the rest into a number.
''',
'''mic = iso["mic_cipro"].str.strip()
iso["mic_sign"] = mic.str.extract(r"^([<>]=?)", expand=False)
iso["mic_value"] = pd.to_numeric(mic.str.replace(r"^[<>]=?", "", regex=True), errors="coerce")
iso[["mic_cipro", "mic_sign", "mic_value"]].drop_duplicates().sort_values("mic_value")''',
'''#md
`errors="coerce"` turns anything that is not a number into `NaN` instead of failing.

## 6. Impossible values
''',
'''print(iso["temp_c"].describe())
print((iso["temp_c"] > 45).sum(), "temperatures above 45")''',
'''iso.loc[~iso["temp_c"].between(30, 45), "temp_c"] = np.nan
iso["temp_c"].describe()''',
'''#md
## 7. Missing values
''',
'''iso.isna().sum()''',
'''#md
Options, depending on why the value is missing:

- leave it missing and report it (often the honest choice)
- drop rows: `dropna(subset=[...])`
- fill: `fillna(value)`, or with the median of a group

Filling is a modelling decision; in the machine learning guide it is done inside a pipeline.
''',
'''print(len(iso.dropna(subset=["ciprofloxacin"])))
iso["temp_filled"] = iso["temp_c"].fillna(iso.groupby("organism")["temp_c"].transform("median"))
iso[["temp_c", "temp_filled"]].isna().sum()''',
'''#md
## 8. Rename and choose types
''',
'''clean = (
    iso
    .rename(columns={"ciprofloxacin": "cip", "ceftriaxone": "cro"})
    .astype({"organism": "category", "specimen": "category"})
    .drop(columns=["temp_filled"])
)
clean.info()''',
'''#md
## Write the clean file and keep the steps as code

Never clean by hand in Excel: keep every step in code so it can be rerun when new data arrive.
''',
'''clean.to_csv("../data/isolates_clean.csv", index=False)
clean.head()''',
])

# ---------------------------------------------------------------- 13
build(D + "13_pandas_groupby.ipynb", [
'''#md
# 13 Grouping and summarising

Split the data into groups, apply a calculation, combine the results.
''',
'''import pandas as pd

patients = pd.read_csv("../data/patients.csv", parse_dates=["enrolled"])
patients.groupby("site")["age"].mean().round(1)''',
'''#md
## Several statistics

`agg()` with named results gives tidy column names.
''',
'''summary = (
    patients
    .groupby("site")
    .agg(
        n=("patient_id", "count"),
        mean_age=("age", "mean"),
        median_weight=("weight_kg", "median"),
        missing_weight=("weight_kg", lambda s: s.isna().sum()),
        pct_female=("sex", lambda s: (s == "F").mean() * 100),
    )
    .round(1)
    .sort_values("n", ascending=False)
)
summary''',
'''#md
## Grouping by more than one column
''',
'''patients.groupby(["site", "sex"])["age"].agg(["count", "mean"]).round(1).head(6)''',
'''#md
`reset_index()` turns the group labels back into ordinary columns, which is easier to plot or save:
''',
'''patients.groupby(["site", "sex"], as_index=False)["age"].mean().head()''',
'''#md
## Counts and cross tables
''',
'''pd.crosstab(patients["site"], patients["hiv_status"], margins=True)''',
'''pd.crosstab(patients["site"], patients["hiv_status"], normalize="index").round(3) * 100''',
'''#md
## transform: a group value on every row

`agg` gives one row per group. `transform` gives a value for every original row,
for example each patient's age relative to their site's mean.
''',
'''patients["site_mean_age"] = patients.groupby("site")["age"].transform("mean").round(1)
patients["age_vs_site"] = patients["age"] - patients["site_mean_age"]
patients[["patient_id", "site", "age", "site_mean_age", "age_vs_site"]].head()''',
'''#md
## Time-based groups
''',
'''by_month = (
    patients
    .groupby(patients["enrolled"].dt.to_period("M"))
    .size()
    .rename("enrolled")
)
by_month.head()''',
'''patients.set_index("enrolled").resample("QE")["patient_id"].count()''',
'''#md
## filter: keep whole groups
''',
'''big_sites = patients.groupby("site").filter(lambda g: len(g) >= 50)
big_sites["site"].unique()''',
'''#md
## Ranking within groups
''',
'''patients["age_rank_in_site"] = patients.groupby("site")["age"].rank(ascending=False, method="first")
patients.loc[patients["age_rank_in_site"] <= 2, ["site", "patient_id", "age"]].sort_values(["site", "age"])''',
])

# ---------------------------------------------------------------- 14
build(D + "14_pandas_merge_reshape.ipynb", [
'''#md
# 14 Combining and reshaping

Joining tables on a key, stacking tables, and moving between long and wide shapes.
''',
'''import pandas as pd

patients = pd.read_csv("../data/patients.csv")
visits = pd.read_csv("../data/visits.csv", parse_dates=["visit_date"])
print(patients.shape, visits.shape)
visits.head()''',
'''#md
## merge

`how` decides which rows are kept:

| how | keeps |
|---|---|
| `inner` | keys in both tables |
| `left` | every row of the left table |
| `right` | every row of the right table |
| `outer` | every key from either |
''',
'''merged = visits.merge(patients[["patient_id", "site", "sex", "age"]], on="patient_id", how="left")
merged.head()''',
'''#md
`validate` checks the relationship you expect, and `indicator` shows where each row came from.
Use them: a wrong join is one of the most common silent errors in analysis.
''',
'''check = patients.merge(visits, on="patient_id", how="outer",
                       validate="one_to_many", indicator=True)
check["_merge"].value_counts()''',
'''#md
Different key names in each table:
''',
'''codes = pd.DataFrame({"site_name": ["Kampala", "Gulu", "Mbarara", "Mbale", "Jinja"],
                      "region": ["Central", "Northern", "Western", "Eastern", "Eastern"]})
patients.merge(codes, left_on="site", right_on="site_name", how="left")[["patient_id", "site", "region"]].head()''',
'''#md
## concat: stacking

Same columns, more rows (or `axis=1` for side by side).
''',
'''batch1 = patients.iloc[:3]
batch2 = patients.iloc[3:5]
pd.concat([batch1, batch2], ignore_index=True)''',
'''pd.concat([batch1.assign(batch=1), batch2.assign(batch=2)])[["patient_id", "batch"]]''',
'''#md
## Long and wide

- long: one row per measurement (patient, visit, value). Best for groupby and seaborn.
- wide: one row per patient, a column per visit. Best for some tables and for ML features.
''',
'''wide = visits.pivot(index="patient_id", columns="visit", values="hb")
wide.columns = [f"hb_v{c}" for c in wide.columns]
wide.head()''',
'''#md
`pivot_table` also summarises when a combination appears more than once:
''',
'''merged.pivot_table(index="site", columns="sex", values="hb", aggfunc="mean").round(2)''',
'''#md
## melt: wide back to long
''',
'''long_again = wide.reset_index().melt(id_vars="patient_id", var_name="visit", value_name="hb")
long_again = long_again.dropna()
long_again["visit"] = long_again["visit"].str.replace("hb_v", "").astype(int)
long_again.sort_values(["patient_id", "visit"]).head()''',
'''#md
Several measures at once:
''',
'''labs_long = visits.melt(id_vars=["patient_id", "visit"], value_vars=["hb", "wbc", "crp"],
                        var_name="test", value_name="value")
labs_long.head()''',
'''#md
## Change from baseline

A common clinical calculation that combines grouping and shifting.
''',
'''visits = visits.sort_values(["patient_id", "visit"])
visits["hb_baseline"] = visits.groupby("patient_id")["hb"].transform("first")
visits["hb_change"] = (visits["hb"] - visits["hb_baseline"]).round(1)
visits["hb_previous"] = visits.groupby("patient_id")["hb"].shift(1)
visits.head(8)''',
])
print("part 2 written")
