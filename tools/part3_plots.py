from nb import build

D = "notebooks/"

# ---------------------------------------------------------------- 15
build(D + "15_matplotlib.ipynb", [
'''#md
# 15 matplotlib

The plotting library underneath most Python charts, seaborn and pandas included.
Learn the figure / axes model once and everything else makes sense.
''',
'''import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

patients = pd.read_csv("../data/patients.csv", parse_dates=["enrolled"])
visits = pd.read_csv("../data/visits.csv")''',
'''#md
## Figure and axes

`fig` is the whole picture; `ax` is one plot inside it. Draw on `ax`.
''',
'''fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(patients["height_cm"], patients["weight_kg"], alpha=0.6)
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Weight (kg)")
ax.set_title("Weight against height")
plt.show()''',
'''#md
## The main chart types
''',
'''fig, axes = plt.subplots(2, 2, figsize=(10, 7))

axes[0, 0].hist(patients["age"], bins=20, color="steelblue", edgecolor="white")
axes[0, 0].set_title("Histogram: age")

counts = patients["site"].value_counts()
axes[0, 1].bar(counts.index, counts.values, color="darkorange")
axes[0, 1].set_title("Bar: patients per site")

monthly = patients.groupby(patients["enrolled"].dt.month).size()
axes[1, 0].plot(monthly.index, monthly.values, marker="o")
axes[1, 0].set_title("Line: enrolment by month")
axes[1, 0].set_xticks(range(1, 13))

data = [g["age"].values for _, g in patients.groupby("sex")]
axes[1, 1].boxplot(data, tick_labels=["F", "M"])
axes[1, 1].set_title("Box: age by sex")

fig.tight_layout()
plt.show()''',
'''#md
## Colour, size and labels for groups
''',
'''fig, ax = plt.subplots(figsize=(6, 4))
for sex, colour in [("F", "tab:purple"), ("M", "tab:green")]:
    d = patients[patients["sex"] == sex]
    ax.scatter(d["age"], d["weight_kg"], label=sex, color=colour, alpha=0.6, s=25)
ax.legend(title="Sex")
ax.set(xlabel="Age", ylabel="Weight (kg)")
plt.show()''',
'''#md
## Reference lines, annotation and limits
''',
'''first = visits[visits["visit"] == 0]
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(first["hb"], bins=25, color="grey", edgecolor="white")
ax.axvline(11, color="red", linestyle="--", label="Anaemia cut-off")
ax.annotate(f"{(first['hb'] < 11).mean():.0%} below 11",
            xy=(11, 5), xytext=(7.5, 25), arrowprops={"arrowstyle": "->"})
ax.set_xlim(6, 18)
ax.legend()
ax.set_xlabel("Haemoglobin (g/dL)")
plt.show()''',
'''#md
## Error bars
''',
'''s = visits.groupby("visit")["hb"].agg(["mean", "sem"])
fig, ax = plt.subplots(figsize=(6, 4))
ax.errorbar(s.index, s["mean"], yerr=1.96 * s["sem"], marker="o", capsize=4)
ax.set(xlabel="Visit", ylabel="Mean Hb (95% CI)", xticks=s.index)
plt.show()''',
'''#md
## Plotting straight from pandas

`df.plot()` calls matplotlib for you and returns the axes, so you can keep adjusting.
''',
'''ax = patients.groupby("site")["age"].mean().sort_values().plot(kind="barh", color="teal", figsize=(6, 3))
ax.set_xlabel("Mean age")
plt.show()''',
'''#md
## Styles and saving

`plt.style.available` lists built-in styles. Save with `fig.savefig()`;
use `dpi=300` for print and `bbox_inches="tight"` so labels are not cut off.
Saving as `.svg` or `.pdf` keeps the plot sharp at any size.
''',
'''with plt.style.context("ggplot"):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.hist(patients["age"], bins=15)
    ax.set_title("ggplot style")
    fig.savefig("age_hist.png", dpi=300, bbox_inches="tight")
    plt.show()

import os
os.remove("age_hist.png")''',
])

# ---------------------------------------------------------------- 16
build(D + "16_seaborn.ipynb", [
'''#md
# 16 seaborn

seaborn draws statistical plots straight from a DataFrame in long format.
It handles grouping, colours and legends, and returns matplotlib axes you can adjust.
''',
'''import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid", context="notebook")

patients = pd.read_csv("../data/patients.csv")
visits = pd.read_csv("../data/visits.csv")
df = visits.merge(patients, on="patient_id")
df["bmi"] = df["weight_kg"] / (df["height_cm"] / 100) ** 2''',
'''#md
## Distributions
''',
'''sns.histplot(data=patients, x="age", hue="sex", bins=20, multiple="stack")
plt.show()''',
'''sns.kdeplot(data=df[df["visit"] == 0], x="hb", hue="hiv_status", common_norm=False, fill=True, alpha=0.3)
plt.show()''',
'''#md
## Comparing groups
''',
'''fig, axes = plt.subplots(1, 3, figsize=(13, 4), sharey=True)
sns.boxplot(data=df, x="site", y="hb", ax=axes[0])
sns.violinplot(data=df, x="site", y="hb", ax=axes[1], inner="quart")
sns.stripplot(data=df, x="site", y="hb", ax=axes[2], alpha=0.4, jitter=0.25)
for ax in axes:
    ax.tick_params(axis="x", rotation=30)
fig.tight_layout()
plt.show()''',
'''#md
Bar plots show a mean with a confidence interval by default:
''',
'''sns.barplot(data=df, x="visit", y="hb", hue="sex", errorbar=("ci", 95))
plt.show()''',
'''sns.countplot(data=patients, y="site", hue="hiv_status", order=patients["site"].value_counts().index)
plt.show()''',
'''#md
## Relationships
''',
'''sns.scatterplot(data=patients, x="height_cm", y="weight_kg", hue="sex", size="age", alpha=0.7)
plt.show()''',
'''sns.regplot(data=patients, x="age", y="weight_kg", scatter_kws={"alpha": 0.4}, line_kws={"color": "red"})
plt.show()''',
'''#md
Line plots of repeated measures, with the mean and its interval per visit:
''',
'''sns.lineplot(data=df, x="visit", y="hb", hue="site", marker="o", errorbar=None)
plt.show()''',
'''#md
## Correlation heatmap
''',
'''num = df[["age", "weight_kg", "height_cm", "bmi", "hb", "wbc", "crp"]]
corr = num.corr().round(2)
sns.heatmap(corr, annot=True, cmap="vlag", center=0, square=True, cbar_kws={"shrink": 0.7})
plt.show()''',
'''#md
## Small multiples

The figure-level functions `relplot`, `displot` and `catplot` split a plot into panels with `col` and `row`.
''',
'''g = sns.relplot(data=df, x="visit", y="hb", col="site", col_wrap=3, kind="line",
                units="patient_id", estimator=None, alpha=0.3, height=2.6)
g.set_titles("{col_name}")
plt.show()''',
'''g = sns.displot(data=patients, x="age", col="sex", row="hiv_status", bins=15, height=2.2, aspect=1.4)
plt.show()''',
'''#md
## Pair plot

Every numeric variable against every other: a quick first look before modelling.
''',
'''sns.pairplot(patients[["age", "weight_kg", "height_cm", "sex"]].dropna(), hue="sex",
             corner=True, plot_kws={"alpha": 0.5, "s": 15}, height=2)
plt.show()''',
'''#md
## Adjusting a seaborn plot

Axes-level functions return a matplotlib `ax`; figure-level ones return a grid `g`
with `g.fig` and `g.axes`.
''',
'''ax = sns.boxplot(data=df, x="hiv_status", y="crp", hue="hiv_status", palette="Set2", legend=False)
ax.set_yscale("log")
ax.set(xlabel="", ylabel="CRP (mg/L, log scale)", title="CRP by HIV status")
plt.show()''',
])

# ---------------------------------------------------------------- 17
build(D + "17_case_study_eda.ipynb", [
'''#md
# 17 Case study: exploring a dataset from start to finish

Everything from the previous notebooks applied to one question:

*Which organisms and specimens show the most ciprofloxacin resistance, and has it changed over the year?*

This is the kind of exploration done before any modelling.
''',
'''import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")''',
'''#md
## 1. Load

Start from the raw file and repeat the cleaning from notebook 12 as one function,
so the analysis never depends on a file someone edited by hand.
''',
'''def load_isolates(path):
    d = pd.read_csv(path).drop_duplicates()
    d["specimen"] = d["specimen"].str.strip().str.capitalize()
    for col in ["ciprofloxacin", "ceftriaxone"]:
        d[col] = d[col].str.strip().str.upper().replace({"N/A": np.nan, "": np.nan})
    d["collected"] = pd.to_datetime(d["collected"], format="%d/%m/%Y")
    d.loc[~d["temp_c"].between(30, 45), "temp_c"] = np.nan
    return d

iso = load_isolates("../data/isolates_raw.csv")
patients = pd.read_csv("../data/patients.csv")
iso = iso.merge(patients[["patient_id", "site", "sex", "age"]], on="patient_id",
                how="left", validate="many_to_one")
print(iso.shape)
iso.head()''',
'''#md
## 2. Check the data
''',
'''print(iso.isna().sum()[lambda s: s > 0])
print(iso["isolate_id"].is_unique)''',
'''#md
## 3. Describe
''',
'''print(iso["organism"].value_counts())
print(iso["specimen"].value_counts())''',
'''tested = iso.dropna(subset=["ciprofloxacin"]).assign(resistant=lambda d: d["ciprofloxacin"] == "R")
print(f"{len(tested)} isolates tested, {tested['resistant'].mean():.1%} resistant to ciprofloxacin")''',
'''#md
## 4. Resistance by organism and specimen
''',
'''table = (
    tested
    .groupby(["organism", "specimen"])
    .agg(n=("resistant", "size"), pct_r=("resistant", "mean"))
    .reset_index()
)
heat = table.pivot(index="organism", columns="specimen", values="pct_r")
n = table.pivot(index="organism", columns="specimen", values="n")

labels = (heat * 100).round(0).astype("Int64").astype(str) + "%\\n(n=" + n.astype(str) + ")"
fig, ax = plt.subplots(figsize=(8, 4))
sns.heatmap(heat, annot=labels, fmt="", cmap="Reds", vmin=0, vmax=1, ax=ax,
            cbar_kws={"label": "% resistant"})
ax.set(xlabel="", ylabel="", title="Ciprofloxacin resistance")
plt.show()''',
'''#md
Small cells (low n) give unstable percentages. Look at the counts before reading the colours.

## 5. Change over time
''',
'''monthly = (
    tested
    .groupby([tested["collected"].dt.to_period("Q").astype(str), "organism"])["resistant"]
    .agg(["mean", "size"])
    .reset_index()
    .rename(columns={"collected": "quarter"})
)
ax = sns.lineplot(data=monthly, x="quarter", y="mean", hue="organism", marker="o")
ax.set(ylabel="% resistant", xlabel="", ylim=(0, 1))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
plt.show()''',
'''#md
## 6. Does resistance relate to patient characteristics?
''',
'''fig, axes = plt.subplots(1, 2, figsize=(11, 4))
sns.barplot(data=tested, x="site", y="resistant", ax=axes[0], color="steelblue")
axes[0].set(ylabel="% resistant", xlabel="")
sns.boxplot(data=tested, x="ciprofloxacin", y="age", order=["S", "I", "R"], ax=axes[1])
fig.tight_layout()
plt.show()''',
'''#md
## 7. Co-resistance

Are isolates resistant to ciprofloxacin also resistant to ceftriaxone?
''',
'''pd.crosstab(tested["ciprofloxacin"], tested["ceftriaxone"], margins=True)''',
'''#md
## 8. Write down what you found

- the overall resistance rate and which organism / specimen groups are highest
- whether there is a visible time trend, and how many isolates each point rests on
- data problems found and fixed: duplicates, inconsistent case, impossible temperatures, MICs stored as text

These are simulated data, so the patterns are made up. The steps are the ones you would use on real data,
and the cleaned table is the starting point for the machine learning guide.
''',
])
print("part 3 written")
