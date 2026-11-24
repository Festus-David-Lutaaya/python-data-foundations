from nb import lesson, exercises

F = "07_Matplotlib/"
MG = "[Matplotlib user guide](https://matplotlib.org/stable/users/index.html)"
NOTE = "Exercises for this folder are in `exercises/Matplotlib_Exercises.ipynb`."
SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
RAW = "../datasets/raw/"'''

lesson(F + "01_Introduction_to_Matplotlib.ipynb", "Introduction to Matplotlib",
["explain why visualisation matters in data analysis",
 "describe the main principles of a good chart",
 "understand Matplotlib's structure: Figure, Axes and artists",
 "use both the pyplot and the object-oriented interfaces"],
"""
A chart can show in seconds what a table hides: skew, outliers, a trend, a difference between groups.
Matplotlib is Python's foundational plotting library. Seaborn and pandas' own plotting are built on it,
so knowing Matplotlib lets you adjust any Python chart.
""",
[
SETUP,
'''#md
## Why visualise? Anscombe's quartet

Four datasets with almost identical means, variances and correlations, but completely different
patterns. Summary statistics alone would call them the same.
''',
'''x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
ys = {
    "I":   (x,  [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
    "II":  (x,  [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
    "III": (x,  [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
    "IV":  (x4, [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]),
}
for name, (xx, yy) in ys.items():
    yy = np.array(yy)
    print(f"{name:>3}: mean y {yy.mean():.2f}, sd y {yy.std(ddof=1):.2f}, r {np.corrcoef(xx, yy)[0, 1]:.3f}")''',
'''fig, axes = plt.subplots(1, 4, figsize=(12, 3), sharey=True)
for ax, (name, (xx, yy)) in zip(axes, ys.items()):
    ax.scatter(xx, yy, s=30)
    ax.set_title(name)
plt.show()''',
'''#md
## Principles of a good chart

1. **One message.** Decide what the chart should show, then choose the form: distribution (histogram,
   box plot), comparison of groups (bar, box), relationship (scatter), change over time (line).
2. **Honest scales.** Bar charts start at zero, because bar length encodes the value. Never use two
   different y-axes on one chart: readers compare the lines' heights, which then mean nothing. Draw two
   charts instead.
3. **Label everything.** A title that states the point, axis labels with units, a legend when there are
   two or more series.
4. **Colour with a purpose.** Colour for identity (groups) or magnitude (light to dark). Use
   colour-blind-friendly palettes such as `viridis` or `tab10`; avoid rainbow maps such as `jet`.
   Never rely on colour alone: add labels, markers or line styles.
5. **Remove clutter.** Light gridlines, no 3-D effects, no unnecessary borders.

## Matplotlib's structure

```
Figure  (the whole image, can hold several plots)
└── Axes  (one plot: the data area plus its x and y axis)
    ├── lines, markers, bars, text ... (artists)
    ├── XAxis / YAxis  (ticks, tick labels, axis label)
    └── title, legend
```

An **Axes** is a single plot, not the plural of axis. A figure with four panels has four Axes.

## Two interfaces

**pyplot** (`plt.plot`, `plt.title`): quick, works on the "current" plot.
''',
'''plt.plot([1, 2, 3, 4], [10, 12, 9, 14])
plt.title("pyplot style")
plt.xlabel("week")
plt.ylabel("cases")
plt.show()''',
'''#md
**Object-oriented** (`fig, ax = plt.subplots()`, then `ax.plot`): you hold the Figure and Axes
explicitly. This is the recommended style, especially with several plots, and the one this course uses.
''',
'''fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot([1, 2, 3, 4], [10, 12, 9, 14], marker="o")
ax.set_title("object-oriented style")
ax.set_xlabel("week")
ax.set_ylabel("cases")
plt.show()''',
'''#md
The pyplot function `plt.xlabel` corresponds to the method `ax.set_xlabel`; most others follow the
`set_` pattern: `set_title`, `set_xlim`, `set_ylim`, `set_xticks`.

## pandas plotting

pandas has a `.plot` method that calls Matplotlib for you and returns an Axes you can then customise.
''',
'''patients = pd.read_csv(RAW + "patients.csv")
ax = patients["age"].plot.hist(bins=20, edgecolor="white", figsize=(6, 3.5))
ax.set_xlabel("age (years)")
ax.set_title("Age of enrolled patients")
plt.show()''',
'''#md
In notebooks, `plt.show()` is optional but keeps the output clean (no `<Axes ...>` text line). In
scripts, it is what opens the window.
''',
],
[MG, "[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)",
 "[Parts of a figure](https://matplotlib.org/stable/users/explain/quick_start.html#parts-of-a-figure)",
 "[Claus O. Wilke, Fundamentals of Data Visualization](https://clauswilke.com/dataviz/)"],
exercises_note=NOTE)

lesson(F + "02_Basic_Plots.ipynb", "Basic plots",
["draw line, bar, scatter, histogram, box and pie charts",
 "choose the plot type that fits the question",
 "interpret what each plot shows"],
"""
Each basic plot answers a different kind of question. This notebook draws each with real course data
and explains how to read it.

| question | plot |
|---|---|
| how does a value change over time? | line |
| how do groups compare in size or count? | bar |
| are two numeric variables related? | scatter |
| what is the shape of one variable's distribution? | histogram |
| how do distributions compare between groups? | box plot |
| what share of a whole does each part take? | pie (use sparingly) |
""",
[
SETUP,
'''patients = pd.read_csv(RAW + "patients.csv")
labs = pd.read_csv(RAW + "lab_results.csv", parse_dates=["visit_date"])
sales = pd.read_csv(RAW + "daily_sales.csv", parse_dates=["date"])''',
'''#md
## Line plot: change over time
''',
'''monthly = (sales.assign(month=sales["date"].dt.to_period("M").dt.to_timestamp())
           .groupby(["month", "shop"])["units"].sum().unstack())

fig, ax = plt.subplots(figsize=(8, 4))
for shop in monthly.columns:
    ax.plot(monthly.index, monthly[shop], label=shop, linewidth=2)
ax.set_title("Monthly units sold by shop")
ax.set_ylabel("units per month")
ax.legend(title="shop")
plt.show()''',
'''#md
**Reading it:** each line is one shop. Look for the overall trend (here roughly level from 2024 to
2025), repeating patterns (a clear seasonal peak in the middle of each year) and how the shops differ
in level (Central sells about twice as much as North). A line implies continuity, so use it for ordered
x values such as time, not for unrelated categories.

## Bar chart: comparing groups
''',
'''counts = patients["site"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(6, 3.5))
ax.bar(counts.index, counts.values)
ax.set_title("Patients enrolled per site")
ax.set_ylabel("patients")
plt.show()''',
'''#md
Bars must start at zero. For many categories or long names, horizontal bars (`barh`) read better,
sorted by value:
''',
'''mean_age = patients.groupby("site")["age"].mean().sort_values()
fig, ax = plt.subplots(figsize=(6, 3))
ax.barh(mean_age.index, mean_age.values)
ax.set_xlabel("mean age (years)")
plt.show()''',
'''#md
### Grouped bars

Bars for two groups side by side, shifted by half a bar width:
''',
'''tab = pd.crosstab(patients["site"], patients["group"])
x = np.arange(len(tab))
w = 0.4

fig, ax = plt.subplots(figsize=(7, 3.5))
ax.bar(x - w / 2, tab["Control"], width=w, label="Control")
ax.bar(x + w / 2, tab["Treatment"], width=w, label="Treatment")
ax.set_xticks(x, tab.index)
ax.set_ylabel("patients")
ax.legend()
plt.show()''',
'''#md
## Scatter plot: relationships
''',
'''fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(patients["height_cm"], patients["weight_kg"], s=15, alpha=0.6)
ax.set_xlabel("height (cm)")
ax.set_ylabel("weight (kg)")
ax.set_title("Weight against height")
plt.show()''',
'''#md
**Reading it:** look at the direction (do points rise to the right?), the strength (a tight band or a
loose cloud?), its shape (straight or curved) and any points far from the rest. `alpha` makes points
partly transparent so that overlapping points show as darker areas.

## Histogram: one variable's distribution
''',
'''fig, ax = plt.subplots(figsize=(6, 3.5))
ax.hist(labs["glucose_mmol"], bins=30, edgecolor="white")
ax.axvline(7.0, color="black", linestyle="--", linewidth=1)
ax.text(7.1, ax.get_ylim()[1] * 0.9, "7.0 mmol/L", fontsize=9)
ax.set_xlabel("glucose (mmol/L)")
ax.set_ylabel("number of results")
plt.show()''',
'''#md
**Reading it:** the height of each bar is how many values fall in that interval. Look for the centre,
the spread, whether one tail is longer (skew), several peaks (mixed groups) and isolated bars
(outliers). The number of bins changes the picture; try a few:
''',
'''fig, axes = plt.subplots(1, 3, figsize=(12, 3), sharey=False)
for ax, bins in zip(axes, [5, 20, 80]):
    ax.hist(labs["glucose_mmol"], bins=bins, edgecolor="white")
    ax.set_title(f"{bins} bins")
plt.show()''',
'''#md
Too few bins hide the shape; too many make it noisy.

## Box plot: comparing distributions
''',
'''groups = [g["age"].values for _, g in patients.groupby("site")]
labels = sorted(patients["site"].unique())

fig, ax = plt.subplots(figsize=(6, 3.5))
ax.boxplot(groups, tick_labels=labels)
ax.set_ylabel("age (years)")
ax.set_title("Age by site")
plt.show()''',
'''#md
**Reading a box plot:**

```
   o        ← outlier: beyond 1.5 × IQR from the box
   ┬        ← whisker: furthest value within 1.5 × IQR
 ┌───┐      ← 75th percentile (Q3)
 │───│      ← median
 └───┘      ← 25th percentile (Q1)
   ┴
```

The box holds the middle half of the values. Compare medians (the lines) and spreads (box heights)
across groups.

## Pie chart: parts of a whole

People judge angles poorly, so a bar chart is usually clearer. A pie can work for two or three parts.
''',
'''shares = patients["smoker"].value_counts()
fig, ax = plt.subplots(figsize=(4, 4))
ax.pie(shares.values, labels=shares.index, autopct="%1.0f%%", startangle=90,
       wedgeprops={"edgecolor": "white"})
ax.set_title("Smoking status")
plt.show()''',
'''#md
## Error bars: means with uncertainty
''',
'''stats = labs.groupby("visit")["systolic_bp"].agg(["mean", "std", "count"])
stats["se"] = stats["std"] / np.sqrt(stats["count"])

fig, ax = plt.subplots(figsize=(6, 3.5))
ax.errorbar(stats.index, stats["mean"], yerr=1.96 * stats["se"], marker="o", capsize=4)
ax.set_xticks(stats.index)
ax.set_xlabel("visit")
ax.set_ylabel("mean systolic BP (mmHg)")
ax.set_title("Mean systolic BP by visit, with 95% confidence intervals")
plt.show()''',
'''#md
The bars show ±1.96 standard errors, an approximate 95% confidence interval for each mean. Always say
in the caption what error bars represent: standard deviation, standard error and confidence intervals
look alike but mean different things.
''',
],
[MG, "[Plot types gallery](https://matplotlib.org/stable/plot_types/index.html)",
 "[From data to viz: choosing a chart](https://www.data-to-viz.com/)"],
exercises_note=NOTE)

lesson(F + "03_Customising_Plots.ipynb", "Customising plots",
["set titles, axis labels, limits and ticks",
 "add legends and annotations",
 "control colours, markers, line styles and colour maps",
 "apply styles and gridlines",
 "set figure size and resolution, and export to PNG, JPEG, SVG and PDF"],
"""
A default plot shows the data; a customised plot communicates it. This notebook covers the settings
you will use most, then saving figures for reports and publications.
""",
[
SETUP,
'''labs = pd.read_csv(RAW + "lab_results.csv")
patients = pd.read_csv(RAW + "patients.csv")
df = labs.merge(patients[["patient_id", "group", "age"]], on="patient_id")''',
'''#md
## Titles, labels, limits and ticks
''',
'''fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(df["age"], df["systolic_bp"], s=10, alpha=0.5)
r = df["age"].corr(df["systolic_bp"])
ax.set_title(f"Systolic BP shows no trend with age (r = {r:.2f})", fontsize=13, loc="left")
ax.set_xlabel("age (years)")
ax.set_ylabel("systolic BP (mmHg)")
ax.set_xlim(15, 95)
ax.set_xticks(range(20, 100, 10))
ax.tick_params(labelsize=9)
plt.show()''',
'''#md
A title that **states the finding** ("no trend with age") helps more than one that only names the variables.
(The data in this course are simulated; in real populations blood pressure does tend to rise with age.)

## Colours, markers and line styles

Colours can be names (`"steelblue"`), hex codes (`"#1f77b4"`) or the default cycle `"C0"`, `"C1"`, ...

| marker | | line style | |
|---|---|---|---|
| `"o"` | circle | `"-"` | solid |
| `"s"` | square | `"--"` | dashed |
| `"^"` | triangle | `":"` | dotted |
| `"x"` | cross | `"-."` | dash-dot |
''',
'''means = df.groupby(["visit", "group"])["systolic_bp"].mean().unstack()

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(means.index, means["Control"], color="C0", marker="o", linestyle="-", linewidth=2, label="Control")
ax.plot(means.index, means["Treatment"], color="C1", marker="s", linestyle="--", linewidth=2, label="Treatment")
ax.set_xticks(means.index)
ax.set_xlabel("visit")
ax.set_ylabel("mean systolic BP (mmHg)")
plt.show()''',
'''#md
Different markers and line styles as well as colours mean the chart still works in greyscale print and
for readers with colour-vision deficiency.

## Legends
''',
'''fig, ax = plt.subplots(figsize=(6, 4))
for g, marker in [("Control", "o"), ("Treatment", "s")]:
    ax.plot(means.index, means[g], marker=marker, linewidth=2, label=g)
ax.legend(title="group", loc="upper right", frameon=False)
ax.set_xticks(means.index)
plt.show()''',
'''#md
`loc` places the legend (`"best"`, `"upper left"`, `"lower right"`, ...). For a few lines, labelling the
lines directly is often clearer than a legend:
''',
'''fig, ax = plt.subplots(figsize=(6, 4))
for g in ["Control", "Treatment"]:
    ax.plot(means.index, means[g], marker="o", linewidth=2)
    ax.text(means.index[-1] + 0.1, means[g].iloc[-1], g, va="center")
ax.set_xlim(right=means.index[-1] + 0.9)
ax.set_xticks(means.index)
plt.show()''',
'''#md
## Annotations
''',
'''sales = pd.read_csv(RAW + "daily_sales.csv", parse_dates=["date"])
north = sales[sales["shop"] == "North"].set_index("date")["units"].rolling(14).mean()
peak = north.idxmax()

fig, ax = plt.subplots(figsize=(8, 3.5))
ax.plot(north.index, north.values, linewidth=1.5)
ax.annotate(f"peak: {north.max():.0f} units/day", xy=(peak, north.max()),
            xytext=(peak - pd.Timedelta(days=200), north.max() * 0.98),
            arrowprops={"arrowstyle": "->"})
ax.axhline(north.mean(), color="grey", linestyle=":", linewidth=1)
ax.axvspan(pd.Timestamp("2025-01-01"), pd.Timestamp("2025-03-31"), color="grey", alpha=0.15)
ax.set_title("North shop, 14-day rolling mean of units sold")
plt.show()''',
'''#md
- `annotate` draws text with an optional arrow to a point
- `axhline` / `axvline` draw reference lines
- `axhspan` / `axvspan` shade a range (here, the first quarter of 2025)

## Gridlines and spines
''',
'''fig, ax = plt.subplots(figsize=(6, 3.5))
ax.bar(["Site A", "Site B", "Site C", "Site D"], patients["site"].value_counts().sort_index())
ax.grid(axis="y", color="0.9")
ax.set_axisbelow(True)                  # gridlines behind the bars
ax.spines[["top", "right"]].set_visible(False)
plt.show()''',
'''#md
## Styles

A style changes many defaults at once. `plt.style.available` lists them. Use `with plt.style.context`
to try one without changing everything after it.
''',
'''print(plt.style.available[:10])
for style in ["default", "ggplot", "seaborn-v0_8-whitegrid"]:
    with plt.style.context(style):
        fig, ax = plt.subplots(figsize=(4, 2.5))
        ax.hist(labs["haemoglobin_g_dl"], bins=25)
        ax.set_title(style)
        plt.show()''',
'''#md
## Colour maps

A colour map turns numbers into colours. Use **sequential** maps (`viridis`, `Blues`) for values from
low to high, and **diverging** maps (`RdBu`, `coolwarm`) for values either side of a meaningful centre
such as zero. `viridis` is designed to be readable in greyscale and by people with colour-vision
deficiency; avoid `jet` and `rainbow`, which create false boundaries.
''',
'''fig, ax = plt.subplots(figsize=(6, 4))
pts = ax.scatter(df["age"], df["systolic_bp"], c=df["glucose_mmol"], cmap="viridis", s=12)
fig.colorbar(pts, ax=ax, label="glucose (mmol/L)")
ax.set_xlabel("age (years)")
ax.set_ylabel("systolic BP (mmHg)")
plt.show()''',
'''#md
## Figure size and resolution

`figsize=(width, height)` is in inches. `dpi` (dots per inch) sets the resolution: about 100 for screens,
300 or more for print. A figure 6 inches wide saved at 300 dpi is 1800 pixels wide.

## Exporting

| format | type | use for |
|---|---|---|
| PNG | raster (pixels) | slides, web, documents |
| JPEG | raster, lossy | photos; blurs sharp lines, so avoid for charts |
| SVG | vector | web, editing in Inkscape or Illustrator |
| PDF | vector | LaTeX, journals, printing |

Vector formats stay sharp at any size.
''',
'''from pathlib import Path
out = Path("figures_demo")
out.mkdir(exist_ok=True)

fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(labs["glucose_mmol"], bins=30, edgecolor="white")
ax.set_xlabel("glucose (mmol/L)")
ax.set_ylabel("results")

fig.savefig(out / "glucose.png", dpi=300, bbox_inches="tight")
fig.savefig(out / "glucose.jpg", dpi=200, bbox_inches="tight")
fig.savefig(out / "glucose.svg", bbox_inches="tight")
fig.savefig(out / "glucose.pdf", bbox_inches="tight")
plt.close(fig)

for f in sorted(out.iterdir()):
    print(f"{f.name:14} {f.stat().st_size / 1024:7.1f} KB")''',
'''#md
`bbox_inches="tight"` trims empty margins so labels are not cut off. `plt.close(fig)` frees memory and
stops the figure also displaying in the notebook. Call `savefig` before `plt.show()`: after show, the
figure may be empty.
''',
'''import shutil
shutil.rmtree(out)''',
'''#md
## Setting defaults for a whole notebook

`plt.rcParams` holds the defaults. Setting a few at the top of a notebook keeps all its figures
consistent:

```python
plt.rcParams.update({
    "figure.figsize": (7, 4),
    "figure.dpi": 110,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 13,
    "font.size": 10,
})
```
''',
],
[MG, "[Customising Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html)",
 "[Choosing colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html)",
 "[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)",
 "[savefig reference](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)"],
exercises_note=NOTE)

lesson(F + "04_Subplots.ipynb", "Subplots and multi-panel figures",
["create grids of plots with plt.subplots",
 "share axes between panels",
 "loop over panels to plot groups",
 "build uneven layouts with GridSpec and subplot_mosaic",
 "label panels and add a figure title"],
"""
Several related plots side by side let the reader compare them directly: one panel per group, or
different views of the same data. Multi-panel figures are standard in reports and papers.
""",
[
SETUP,
'''labs = pd.read_csv(RAW + "lab_results.csv")
patients = pd.read_csv(RAW + "patients.csv")''',
'''#md
## A grid of plots

`plt.subplots(nrows, ncols)` returns the figure and an array of Axes.
''',
'''fig, axes = plt.subplots(2, 2, figsize=(9, 6))
print(axes.shape)

axes[0, 0].hist(labs["glucose_mmol"], bins=25, edgecolor="white")
axes[0, 0].set_title("Glucose (mmol/L)")
axes[0, 1].hist(labs["haemoglobin_g_dl"], bins=25, edgecolor="white", color="C1")
axes[0, 1].set_title("Haemoglobin (g/dL)")
axes[1, 0].scatter(labs["systolic_bp"], labs["diastolic_bp"], s=8, alpha=0.5, color="C2")
axes[1, 0].set_title("Diastolic against systolic BP")
axes[1, 1].boxplot([labs.loc[labs["visit"] == v, "systolic_bp"] for v in sorted(labs["visit"].unique())])
axes[1, 1].set_title("Systolic BP by visit")
fig.tight_layout()
plt.show()''',
'''#md
`tight_layout()` (or `layout="constrained"` in `plt.subplots`) adjusts spacing so titles and labels do
not overlap.

## Looping over panels

`axes.flat` goes through all panels in order, which pairs well with groups:
''',
'''fig, axes = plt.subplots(1, 4, figsize=(13, 3), sharex=True, sharey=True, layout="constrained")
for ax, (site, g) in zip(axes.flat, patients.groupby("site")):
    ax.hist(g["age"], bins=15, edgecolor="white")
    ax.set_title(f"{site} (n={len(g)})")
    ax.set_xlabel("age")
axes[0].set_ylabel("patients")
fig.suptitle("Age distribution by site")
plt.show()''',
'''#md
`sharex=True, sharey=True` give every panel the same scales, so bar heights can be compared across panels.
Without shared axes each panel scales itself, and a small group can look as large as a big one.

## Small multiples instead of a crowded chart

Ten lines on one plot are hard to follow. One small panel per line, on shared axes, is usually clearer.
''',
'''sample_ids = labs["patient_id"].drop_duplicates().iloc[:8]
fig, axes = plt.subplots(2, 4, figsize=(12, 5), sharex=True, sharey=True, layout="constrained")
for ax, pid in zip(axes.flat, sample_ids):
    d = labs[labs["patient_id"] == pid]
    ax.plot(d["visit"], d["systolic_bp"], marker="o")
    ax.set_title(pid, fontsize=10)
fig.supxlabel("visit")
fig.supylabel("systolic BP (mmHg)")
plt.show()''',
'''#md
## Uneven layouts

`subplot_mosaic` draws a layout from a text picture. Each letter is a panel; repeating a letter makes it span.
''',
'''fig, ax = plt.subplot_mosaic("AAB;CCB", figsize=(10, 5), layout="constrained")
ax["A"].hist(labs["glucose_mmol"], bins=30, edgecolor="white")
ax["A"].set_title("A. Glucose distribution", loc="left")
ax["B"].boxplot([patients.loc[patients["group"] == g, "age"] for g in ["Control", "Treatment"]],
                tick_labels=["Control", "Treatment"])
ax["B"].set_title("B. Age by group", loc="left")
ax["C"].scatter(labs["glucose_mmol"], labs["systolic_bp"], s=6, alpha=0.4)
ax["C"].set_title("C. Systolic BP against glucose", loc="left")
plt.show()''',
'''#md
Panel letters (A, B, C) with `loc="left"` are the usual way to refer to panels in a report's text.

`GridSpec` gives the same control with row and column positions:
''',
'''from matplotlib.gridspec import GridSpec
fig = plt.figure(figsize=(8, 5), layout="constrained")
gs = GridSpec(2, 3, figure=fig)
main = fig.add_subplot(gs[:, :2])
top = fig.add_subplot(gs[0, 2])
bottom = fig.add_subplot(gs[1, 2])
main.scatter(patients["height_cm"], patients["weight_kg"], s=10, alpha=0.6)
main.set_xlabel("height (cm)"); main.set_ylabel("weight (kg)")
top.hist(patients["height_cm"], bins=20, edgecolor="white"); top.set_title("height")
bottom.hist(patients["weight_kg"].dropna(), bins=20, edgecolor="white"); bottom.set_title("weight")
plt.show()''',
'''#md
## Two measures with different units

When two variables have different units, put them in **two panels with a shared x-axis**, not on one
plot with two y-axes:
''',
'''sales = pd.read_csv(RAW + "daily_sales.csv", parse_dates=["date"])
north = sales[sales["shop"] == "North"].set_index("date").resample("W")[["units", "price"]].mean()

fig, (top, bottom) = plt.subplots(2, 1, figsize=(8, 5), sharex=True, layout="constrained")
top.plot(north.index, north["units"])
top.set_ylabel("units per day")
bottom.plot(north.index, north["price"], color="C1")
bottom.set_ylabel("price")
top.set_title("North shop, weekly means")
plt.show()''',
],
[MG, "[Arranging multiple Axes](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)",
 "[subplot_mosaic](https://matplotlib.org/stable/users/explain/axes/mosaic.html)",
 "[Constrained layout](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)"],
exercises_note=NOTE)

exercises(F, "Matplotlib", "Matplotlib",
"Exercises for notebooks 01 to 04 of this folder. Use the object-oriented style (`fig, ax = plt.subplots()`).",
[
("Load `../../datasets/raw/daily_sales.csv` and plot total units sold per week across all shops as a line chart, with a title and axis labels.",
 '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
RAW = "../../datasets/raw/"
sales = pd.read_csv(RAW + "daily_sales.csv", parse_dates=["date"])
weekly = sales.set_index("date")["units"].resample("W").sum()
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.plot(weekly.index, weekly.values)
ax.set_title("Total units sold per week")
ax.set_xlabel("week"); ax.set_ylabel("units")
plt.show()'''),
("Make a horizontal bar chart of the number of patients per site (from `patients.csv`), sorted from largest to smallest, with the largest bar at the top.",
 '''patients = pd.read_csv(RAW + "patients.csv")
c = patients["site"].value_counts().sort_values()
fig, ax = plt.subplots(figsize=(6, 3))
ax.barh(c.index, c.values)
ax.set_xlabel("patients")
plt.show()'''),
("Draw a histogram of haemoglobin from `lab_results.csv` with 25 bins, and add a dashed vertical line at 12 g/dL labelled 'anaemia cut-off'.",
 '''labs = pd.read_csv(RAW + "lab_results.csv")
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.hist(labs["haemoglobin_g_dl"], bins=25, edgecolor="white")
ax.axvline(12, linestyle="--", color="black")
ax.text(12.1, ax.get_ylim()[1] * 0.9, "anaemia cut-off")
ax.set_xlabel("haemoglobin (g/dL)")
plt.show()'''),
("Make a scatter plot of systolic against diastolic BP, coloured by glucose with the `viridis` colour map, and include a colour bar.",
 '''fig, ax = plt.subplots(figsize=(6, 4))
p = ax.scatter(labs["systolic_bp"], labs["diastolic_bp"], c=labs["glucose_mmol"], cmap="viridis", s=10)
fig.colorbar(p, ax=ax, label="glucose (mmol/L)")
ax.set_xlabel("systolic"); ax.set_ylabel("diastolic")
plt.show()'''),
("Compare the age distributions of smokers and non-smokers with a box plot.",
 '''fig, ax = plt.subplots(figsize=(5, 3.5))
ax.boxplot([patients.loc[patients["smoker"] == s, "age"] for s in ["No", "Yes"]], tick_labels=["Non-smoker", "Smoker"])
ax.set_ylabel("age")
plt.show()'''),
("Plot mean units per day for each shop on promotion and non-promotion days as a grouped bar chart.",
 '''m = sales.groupby(["shop", "promo"])["units"].mean().unstack()
x = np.arange(len(m)); w = 0.4
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.bar(x - w / 2, m[0], w, label="no promotion")
ax.bar(x + w / 2, m[1], w, label="promotion")
ax.set_xticks(x, m.index); ax.set_ylabel("mean units per day"); ax.legend()
plt.show()'''),
("Make a 1 × 3 figure with histograms of glucose, haemoglobin and systolic BP, each with its own title, and save it as `lab_panels.png` at 300 dpi. Check the file exists, then delete it.",
 '''from pathlib import Path
fig, axes = plt.subplots(1, 3, figsize=(12, 3), layout="constrained")
for ax, col in zip(axes, ["glucose_mmol", "haemoglobin_g_dl", "systolic_bp"]):
    ax.hist(labs[col], bins=25, edgecolor="white"); ax.set_title(col)
fig.savefig("lab_panels.png", dpi=300, bbox_inches="tight")
plt.show()
print(Path("lab_panels.png").exists()); Path("lab_panels.png").unlink()'''),
("Draw one small panel per shop showing its monthly revenue, with shared y-axes, and a figure title.",
 '''sales["revenue"] = sales["units"] * sales["price"]
fig, axes = plt.subplots(1, 3, figsize=(12, 3), sharey=True, layout="constrained")
for ax, (shop, g) in zip(axes, sales.groupby("shop")):
    mon = g.set_index("date")["revenue"].resample("MS").sum()
    ax.plot(mon.index, mon.values); ax.set_title(shop); ax.tick_params(axis="x", rotation=45)
fig.suptitle("Monthly revenue by shop")
plt.show()'''),
])
print("module 07 written")
