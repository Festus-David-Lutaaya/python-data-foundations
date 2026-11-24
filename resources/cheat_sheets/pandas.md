# pandas cheat sheet

```python
import pandas as pd
```

## Reading and writing

```python
df = pd.read_csv("file.csv", parse_dates=["date"], na_values=["NA", "not done"])
pd.read_csv("file.tsv", sep="\t")
pd.read_excel("file.xlsx", sheet_name="Sheet1")
df.to_csv("out.csv", index=False)
df.to_excel("out.xlsx", index=False)
```

## Looking at data

```python
df.head()  df.tail()  df.sample(5)
df.shape  df.columns  df.dtypes  df.info()
df.describe()  df.describe(exclude="number")
df["col"].value_counts(dropna=False)  df["col"].unique()  df["col"].nunique()
df.isna().sum()  df.duplicated().sum()
```

## Selecting

```python
df["col"]                       # a Series
df[["a", "b"]]                  # a DataFrame
df.loc[rows, cols]              # by label; slices include the end
df.iloc[0:5, 0:3]               # by position
df[df["age"] > 60]
df[(df["sex"] == "F") & (df["age"] < 40)]
df[df["site"].isin(["A", "B"])]
df[df["x"].between(1, 5)]
df.query("age > 60 and group == 'Treatment'")
```

## Cleaning

```python
df.drop_duplicates()
df.dropna(subset=["col"])
df["col"].fillna(value)
df["col"].str.strip().str.lower()
df["col"].map({"m": "Male", "f": "Female"})
df["col"].replace(99, np.nan)
pd.to_numeric(df["col"], errors="coerce")
pd.to_datetime(df["date"], format="%d/%m/%Y")
df["col"].astype("category")
df.rename(columns={"old": "new"})
df.drop(columns=["col"])
```

## New columns

```python
df["bmi"] = df["weight"] / df["height"] ** 2
df = df.assign(older=lambda d: d["age"] >= 65)
df["flag"] = np.where(df["x"] > 7, "high", "normal")
df["group"] = pd.cut(df["age"], bins=[0, 35, 65, 120], labels=["<35", "35-64", "65+"])
df["out"] = df.apply(my_function, axis=1)     # slower; prefer vectorised
df["date"].dt.year  df["date"].dt.month_name()  (df["d2"] - df["d1"]).dt.days
```

## Sorting

```python
df.sort_values("age", ascending=False)
df.sort_values(["site", "age"])
df.nlargest(5, "x")
```

## Grouping

```python
df.groupby("site")["age"].mean()
df.groupby(["site", "sex"])["age"].mean().unstack()
df.groupby("site").agg(n=("id", "count"), mean_age=("age", "mean"))
df.groupby("id")["x"].transform("mean")       # a value for every row
df.groupby("cat_col", observed=True)          # for categorical columns
pd.crosstab(df["a"], df["b"], normalize="index")
pd.pivot_table(df, values="x", index="a", columns="b", aggfunc="mean")
```

## Combining and reshaping

```python
pd.merge(left, right, on="id", how="left", validate="many_to_one")
pd.concat([df1, df2], ignore_index=True)
df.pivot(index="id", columns="visit", values="x")         # long to wide
wide.melt(id_vars="id", var_name="visit", value_name="x")  # wide to long
```

## Time series

```python
s = df.set_index("date")["x"]
s.resample("MS").sum()     # "D", "W", "MS", "QS", "YS"
s.rolling(7).mean()
```
