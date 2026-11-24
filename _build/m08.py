from nb import lesson, exercises

F = "08_Seaborn/"
SG = "[Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)"
NOTE = "Exercises for this folder are in `exercises/Seaborn_Exercises.ipynb`."
SETUP = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
RAW = "../datasets/raw/"'''

lesson(F + "01_Introduction_to_Seaborn.ipynb", "Introduction to Seaborn",
["explain what Seaborn adds to Matplotlib",
 "load Seaborn's example datasets",
 "understand figure-level and axes-level functions",
 "set themes, contexts and colour palettes"],
"""
Seaborn is a statistical plotting library built on Matplotlib. It works directly with pandas DataFrames:
you name the columns for x, y and colour, and Seaborn groups the data, computes summaries (means,
confidence intervals, density curves) and adds legends. Charts that take twenty lines in Matplotlib take
one in Seaborn, and because the result is Matplotlib, everything from module 7 still works for fine-tuning.
""",
[
SETUP,
'''sns.__version__''',
'''#md
## Example datasets

Seaborn downloads small, well-known datasets (an internet connection is needed the first time). This
module uses:

| dataset | rows | about |
|---|---|---|
| `penguins` | 344 | body measurements of three penguin species on three islands |
| `tips` | 244 | restaurant bills and tips |
| `fmri` | 1064 | brain signal over time in an imaging experiment |
| `flights` | 144 | monthly airline passengers, 1949-1960 |
| `titanic` | 891 | passengers and survival |
''',
'''penguins = sns.load_dataset("penguins")
print(penguins.shape)
penguins.head()''',
'''penguins.isna().sum()''',
'''#md
## The data-to-plot pattern

Name the DataFrame and the columns. `hue` maps a column to colour and adds a legend automatically.
''',
'''sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.show()''',
'''#md
The same plot in plain Matplotlib needs a loop over species, a colour for each and a legend call.
Seaborn handles all that and drops rows with missing values.

## Two kinds of function

| | axes-level | figure-level |
|---|---|---|
| examples | `scatterplot`, `histplot`, `boxplot`, `heatmap` | `relplot`, `displot`, `catplot`, `lmplot`, `pairplot` |
| draws on | one Matplotlib Axes (`ax=`) | its own figure, possibly many panels |
| size | `figsize` of your figure | `height=` and `aspect=` |
| panels | you arrange them | `col=` and `row=` make small multiples |

Axes-level functions fit into your own `plt.subplots` layout:
''',
'''fig, axes = plt.subplots(1, 2, figsize=(10, 3.5), layout="constrained")
sns.histplot(data=penguins, x="bill_length_mm", ax=axes[0])
sns.boxplot(data=penguins, x="species", y="bill_length_mm", ax=axes[1])
axes[0].set_title("All penguins")
axes[1].set_title("By species")
plt.show()''',
'''#md
Figure-level functions make panels for you:
''',
'''sns.displot(data=penguins, x="bill_length_mm", col="species", height=3, aspect=1.1)
plt.show()''',
'''#md
## Themes

`sns.set_theme()` sets a style for every plot that follows. Styles: `darkgrid` (default), `whitegrid`,
`dark`, `white`, `ticks`.
''',
'''for style in ["darkgrid", "whitegrid", "ticks"]:
    sns.set_theme(style=style)
    g = sns.displot(data=penguins, x="flipper_length_mm", height=2.5, aspect=1.6)
    g.ax.set_title(style)
    plt.show()
sns.set_theme(style="whitegrid")''',
'''#md
`sns.despine()` removes the top and right borders. **Contexts** scale fonts and lines for where the
figure will be seen: `paper`, `notebook` (default), `talk`, `poster`.
''',
'''sns.set_theme(style="ticks", context="talk")
sns.boxplot(data=penguins, x="species", y="body_mass_g")
sns.despine()
plt.show()
sns.set_theme(style="whitegrid", context="notebook")''',
'''#md
## Colour palettes

| type | for | examples |
|---|---|---|
| qualitative | categories with no order | `"colorblind"`, `"deep"`, `"Set2"` |
| sequential | ordered values, low to high | `"viridis"`, `"rocket"`, `"Blues"` |
| diverging | values either side of a centre | `"vlag"`, `"coolwarm"`, `"RdBu"` |

The `colorblind` palette is a safe default for groups.
''',
'''for name in ["colorblind", "deep", "viridis", "vlag"]:
    print(name)
    sns.palplot(sns.color_palette(name, 7))
    plt.show()''',
'''sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species",
                style="species", palette="colorblind")
plt.show()''',
'''#md
`style="species"` gives each species its own marker as well as its own colour, so the plot still works
without colour.

A palette can also be a dictionary, fixing each group's colour so it stays the same in every chart of a
report:
''',
'''species_colours = dict(zip(["Adelie", "Chinstrap", "Gentoo"], sns.color_palette("colorblind", 3)))
sns.boxplot(data=penguins, x="species", y="flipper_length_mm", hue="species", palette=species_colours)
plt.show()''',
],
[SG, "[Overview of plotting functions](https://seaborn.pydata.org/tutorial/function_overview.html)",
 "[Controlling figure aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)",
 "[Choosing colour palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)"],
exercises_note=NOTE)

lesson(F + "02_Distribution_Plots.ipynb", "Distribution plots",
["draw histograms and density curves with histplot and kdeplot",
 "compare distributions between groups",
 "use ECDF plots and rug plots",
 "describe a distribution's shape: centre, spread, skew and modes"],
"""
Looking at a variable's distribution is the first step with any numeric data. It shows the typical
value, how much values vary, whether the distribution is symmetric or skewed, and whether there are
several groups hidden inside one variable.
""",
[
SETUP,
'''sns.set_theme(style="whitegrid")
penguins = sns.load_dataset("penguins")
tips = sns.load_dataset("tips")
labs = pd.read_csv(RAW + "lab_results.csv")''',
'''#md
## histplot
''',
'''sns.histplot(data=penguins, x="flipper_length_mm", bins=25)
plt.show()''',
'''#md
**Reading it:** the distribution has two humps (it is *bimodal*). Two humps usually mean two groups
mixed together. Colouring by species shows which:
''',
'''sns.histplot(data=penguins, x="flipper_length_mm", hue="species", bins=25, multiple="layer", alpha=0.5)
plt.show()''',
'''#md
Gentoo penguins form the upper hump; Adelie and Chinstrap overlap in the lower one. `multiple=` can be
`"layer"` (overlapping), `"stack"`, `"dodge"` (side by side) or `"fill"` (proportions).
''',
'''fig, axes = plt.subplots(1, 2, figsize=(11, 3.5), layout="constrained")
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack", ax=axes[0])
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="fill", ax=axes[1])
axes[0].set_title("stack: counts")
axes[1].set_title("fill: proportion in each bin")
plt.show()''',
'''#md
## Skewness

A long right tail means a few large values pull the mean above the median.
''',
'''fig, ax = plt.subplots(figsize=(7, 3.5))
sns.histplot(data=tips, x="total_bill", bins=30, ax=ax)
ax.axvline(tips["total_bill"].mean(), color="black", linestyle="--", label=f"mean {tips['total_bill'].mean():.2f}")
ax.axvline(tips["total_bill"].median(), color="black", linestyle=":", label=f"median {tips['total_bill'].median():.2f}")
ax.legend()
plt.show()
print("skewness:", round(tips["total_bill"].skew(), 2))''',
'''#md
Positive skewness confirms the right skew. For skewed variables, report the median and interquartile
range rather than only the mean and standard deviation.

## kdeplot: smooth density

A kernel density estimate (KDE) draws a smooth curve instead of bars. The area under the curve is 1.
It is good for comparing overlapping groups, but it can suggest values where there are none (below zero,
for example), so check it against a histogram.
''',
'''sns.kdeplot(data=penguins, x="body_mass_g", hue="species", fill=True, alpha=0.3, common_norm=False)
plt.show()''',
'''#md
`common_norm=False` scales each group's curve to area 1 separately, so a small group is not drawn
smaller just because it has fewer members.

`bw_adjust` controls smoothness, like the bin count of a histogram:
''',
'''fig, ax = plt.subplots(figsize=(7, 3.5))
for bw in [0.3, 1, 3]:
    sns.kdeplot(data=labs, x="glucose_mmol", bw_adjust=bw, label=f"bw_adjust={bw}", ax=ax)
ax.legend()
plt.show()''',
'''#md
## Histogram with a density curve
''',
'''sns.histplot(data=labs, x="haemoglobin_g_dl", kde=True, stat="density", bins=30)
plt.show()''',
'''#md
## displot: panels

The figure-level `displot` draws one panel per group with `col` or `row`:
''',
'''sns.displot(data=tips, x="tip", col="time", row="smoker", bins=15, height=2.6, aspect=1.4)
plt.show()''',
'''#md
## ECDF

An *empirical cumulative distribution function* shows, for each value, the proportion of observations
at or below it. It needs no bins, and medians and percentiles can be read straight off the y-axis.
''',
'''ax = sns.ecdfplot(data=penguins, x="body_mass_g", hue="species")
ax.axhline(0.5, color="grey", linestyle=":")
plt.show()''',
'''#md
Where each curve crosses 0.5 is that species' median. A curve further to the right means heavier
penguins throughout the distribution.

## Rug plot

Tick marks for each observation, useful with small samples:
''',
'''small = penguins.sample(40, random_state=2)
sns.kdeplot(data=small, x="bill_depth_mm")
sns.rugplot(data=small, x="bill_depth_mm", height=0.06)
plt.show()''',
'''#md
## Two variables: bivariate distributions
''',
'''sns.displot(data=penguins, x="bill_length_mm", y="bill_depth_mm", kind="kde", hue="species", height=4)
plt.show()''',
'''#md
The contours are like a map's height lines: each species occupies its own region of bill length and
depth, which is why these two measurements separate the species well.
''',
],
[SG, "[Visualising distributions](https://seaborn.pydata.org/tutorial/distributions.html)",
 "[histplot reference](https://seaborn.pydata.org/generated/seaborn.histplot.html)"],
exercises_note=NOTE)

lesson(F + "03_Categorical_Plots.ipynb", "Categorical plots",
["count categories with countplot",
 "show means and uncertainty with barplot and pointplot",
 "compare distributions across groups with box, violin, strip and swarm plots",
 "use catplot for panels"],
"""
Many questions compare a numeric value across categories: glucose by treatment group, tips by day,
positivity by sample type. Seaborn has a family of plots for this, from simple counts to full
distributions.
""",
[
SETUP,
'''sns.set_theme(style="whitegrid")
tips = sns.load_dataset("tips")
titanic = sns.load_dataset("titanic")
penguins = sns.load_dataset("penguins")''',
'''#md
## countplot: how many in each category
''',
'''sns.countplot(data=titanic, x="class", hue="survived", palette="colorblind")
plt.show()''',
'''#md
Pass `order=` to control the category order and `stat="percent"` for percentages. Horizontal bars,
sorted by count, suit many categories:
''',
'''order = titanic["embark_town"].value_counts().index
sns.countplot(data=titanic, y="embark_town", order=order)
plt.show()''',
'''#md
## barplot: a summary with uncertainty

`barplot` shows the **mean** of y for each category, with an error bar. By default, the error bar is a
95% confidence interval computed by resampling (bootstrapping).
''',
'''sns.barplot(data=titanic, x="class", y="survived", hue="sex", palette="colorblind")
plt.ylabel("proportion survived")
plt.show()''',
'''#md
The mean of a 0/1 column is a proportion, so the bars are survival rates. Women survived far more often
than men in every class, and survival fell from first to third class.

`errorbar=` chooses what the bars show: `("ci", 95)`, `"se"` (standard error), `"sd"` (standard
deviation), or `None`.
''',
'''fig, axes = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True, layout="constrained")
sns.barplot(data=tips, x="day", y="total_bill", errorbar=("ci", 95), ax=axes[0])
sns.barplot(data=tips, x="day", y="total_bill", errorbar="sd", ax=axes[1])
axes[0].set_title("95% confidence interval of the mean")
axes[1].set_title("standard deviation of the values")
plt.show()''',
'''#md
The confidence interval describes the uncertainty in the **mean**; the standard deviation describes the
spread of the **individual values**, and is wider. Always say which one you show.

A bar of the mean hides the distribution. When the distribution matters, use the plots below.

## boxplot
''',
'''sns.boxplot(data=tips, x="day", y="total_bill", hue="time", palette="colorblind")
plt.show()''',
'''#md
## violinplot

A violin is a box plot with a density curve on each side, so it also shows the shape (two humps, a long
tail).
''',
'''sns.violinplot(data=penguins, x="species", y="flipper_length_mm", hue="sex", split=True,
               inner="quart", palette="colorblind")
plt.show()''',
'''#md
`split=True` draws the two sexes as halves of one violin; `inner="quart"` adds lines at the quartiles.

## strip and swarm plots: every observation

With small or moderate samples, showing each point is the most honest option.
''',
'''fig, axes = plt.subplots(1, 2, figsize=(11, 3.5), sharey=True, layout="constrained")
sns.stripplot(data=tips, x="day", y="tip", alpha=0.6, jitter=0.25, ax=axes[0])
sns.swarmplot(data=tips, x="day", y="tip", size=3.5, ax=axes[1])
axes[0].set_title("stripplot (jittered)")
axes[1].set_title("swarmplot (no overlap)")
plt.show()''',
'''#md
## Combining layers: box plus points
''',
'''ax = sns.boxplot(data=penguins, x="species", y="body_mass_g", color="white", showfliers=False)
sns.stripplot(data=penguins, x="species", y="body_mass_g", alpha=0.4, ax=ax)
plt.show()''',
'''#md
`showfliers=False` hides the box plot's own outlier points, because the strip plot already shows every
point.

## pointplot: means joined across categories

Good for showing how group means change across an ordered factor, and for interactions:
''',
'''sns.pointplot(data=tips, x="day", y="tip", hue="sex", dodge=0.3, palette="colorblind",
              order=["Thur", "Fri", "Sat", "Sun"])
plt.show()''',
'''#md
## catplot: panels

The figure-level `catplot` gives any of these with `kind=` and panels with `col`/`row`:
''',
'''sns.catplot(data=titanic, x="class", y="age", kind="box", col="sex", height=3.5, aspect=1)
plt.show()''',
'''#md
## Course data: glucose by group and visit
''',
'''labs = pd.read_csv(RAW + "lab_results.csv")
patients = pd.read_csv(RAW + "patients.csv")
df = labs.merge(patients[["patient_id", "group"]], on="patient_id")
sns.boxplot(data=df, x="visit", y="glucose_mmol", hue="group", palette="colorblind")
plt.ylabel("glucose (mmol/L)")
plt.show()''',
],
[SG, "[Visualising categorical data](https://seaborn.pydata.org/tutorial/categorical.html)",
 "[Statistical estimation and error bars](https://seaborn.pydata.org/tutorial/error_bars.html)"],
exercises_note=NOTE)

lesson(F + "04_Relationship_Plots.ipynb", "Relationship plots",
["show the relationship between two numeric variables with scatterplot",
 "add groups with hue, style and size",
 "fit and interpret regression lines with regplot and lmplot",
 "plot trends over time with lineplot, including uncertainty bands",
 "use relplot and jointplot"],
"""
"Is y related to x?" is one of the most common questions in data analysis. Scatter plots show the
relationship; regression lines summarise it; line plots show how a value changes over time or an
ordered variable.
""",
[
SETUP,
'''sns.set_theme(style="whitegrid")
penguins = sns.load_dataset("penguins")
tips = sns.load_dataset("tips")
fmri = sns.load_dataset("fmri")''',
'''#md
## scatterplot
''',
'''sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()''',
'''#md
**Reading it:** tips rise with the bill, roughly in a straight line, and the spread of tips widens as
bills grow (the cloud fans out). That widening matters: a single "average tip rate" fits small bills
better than large ones.

### Encoding more variables

`hue` (colour), `style` (marker) and `size` add up to three more variables. More than two usually
makes a plot hard to read.
''',
'''sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="time", size="size",
                sizes=(20, 200), alpha=0.7, palette="colorblind")
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
plt.show()''',
'''#md
## Regression lines: regplot and lmplot

`regplot` fits a straight line (least squares) and shades a 95% confidence band for the line.
''',
'''ax = sns.regplot(data=tips, x="total_bill", y="tip", scatter_kws={"alpha": 0.5})
plt.show()
slope, intercept = np.polyfit(tips["total_bill"], tips["tip"], 1)
r = tips["total_bill"].corr(tips["tip"])
print(f"tip = {intercept:.2f} + {slope:.3f} x total_bill   (r = {r:.2f}, r squared = {r ** 2:.2f})")''',
'''#md
**Interpreting it:**

- the **slope** (about 0.105): each extra unit on the bill goes with about 0.105 more in tip, a tip rate
  of roughly 10.5% at the margin
- the **intercept** (about 0.92) is the line's value at a bill of zero, which is outside the data and
  has no real meaning here
- **r** (about 0.68) measures how tightly points follow the line; **r squared** (about 0.46) means the
  bill explains about 46% of the variation in tips
- the **shaded band** shows the uncertainty in the line's position, not where individual tips will fall

Correlation is not causation, and a line describes these data only, within the range observed.

### lmplot: separate lines per group
''',
'''sns.lmplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species",
           palette="colorblind", height=4, aspect=1.3)
plt.show()''',
'''#md
### Simpson's paradox

Fitting one line to all penguins tells the opposite story:
''',
'''fig, ax = plt.subplots(figsize=(6, 4))
sns.regplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", scatter_kws={"alpha": 0.4}, ax=ax)
print("overall r:", round(penguins["bill_length_mm"].corr(penguins["bill_depth_mm"]), 2))
print(penguins.groupby("species")[["bill_length_mm", "bill_depth_mm"]].corr().xs("bill_length_mm", level=1)["bill_depth_mm"].round(2))
plt.show()''',
'''#md
Across all penguins, longer bills go with shallower bills (negative r). Within each species, longer
bills go with *deeper* bills (positive r). The overall line is misleading because species differ in both
measurements. Always check whether a grouping variable changes the relationship.

### Non-linear patterns

`order=2` fits a curve; `lowess=True` fits a smooth line without assuming a shape (it needs the
statsmodels package).
''',
'''mpg = sns.load_dataset("mpg")
fig, axes = plt.subplots(1, 2, figsize=(11, 3.5), sharey=True, layout="constrained")
sns.regplot(data=mpg, x="horsepower", y="mpg", ax=axes[0], scatter_kws={"alpha": 0.3})
sns.regplot(data=mpg, x="horsepower", y="mpg", order=2, ax=axes[1], scatter_kws={"alpha": 0.3})
axes[0].set_title("straight line")
axes[1].set_title("quadratic (order=2)")
plt.show()''',
'''#md
The straight line misses the curve: it predicts too low at both ends and too high in the middle. The
quadratic fits the pattern much better.

## lineplot: trends with uncertainty

When there are several observations per x value, `lineplot` draws the mean with a 95% confidence band.
''',
'''sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event", style="region", palette="colorblind")
plt.show()''',
'''#md
The signal peaks around timepoints 5-6 and is stronger for the "stim" event, with the parietal region
higher than the frontal region. The bands show the uncertainty in each mean across subjects.

### Time series
''',
'''flights = sns.load_dataset("flights")
sns.lineplot(data=flights, x="year", y="passengers", hue="month", palette="viridis", legend=False)
plt.title("Monthly passengers by year: each line is one month")
plt.show()''',
'''#md
A sequential palette (viridis) suits months because they are ordered.

Course data, with individual patient lines in light grey behind the group means:
''',
'''labs = pd.read_csv(RAW + "lab_results.csv")
fig, ax = plt.subplots(figsize=(7, 4))
sns.lineplot(data=labs, x="visit", y="systolic_bp", units="patient_id", estimator=None,
             color="0.85", linewidth=0.5, ax=ax)
sns.lineplot(data=labs, x="visit", y="systolic_bp", color="C0", linewidth=3, ax=ax)
ax.set_xticks(sorted(labs["visit"].unique()))
ax.set_ylabel("systolic BP (mmHg)")
plt.show()''',
'''#md
`units=` and `estimator=None` draw one line per patient instead of a mean, which shows how much
individuals vary around the average.

## relplot: panels
''',
'''sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker", palette="colorblind",
            height=3.5, aspect=1)
plt.show()''',
'''#md
## jointplot: relationship plus each variable's distribution
''',
'''sns.jointplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species", height=5)
plt.show()''',
],
[SG, "[Visualising statistical relationships](https://seaborn.pydata.org/tutorial/relational.html)",
 "[Estimating regression fits](https://seaborn.pydata.org/tutorial/regression.html)"],
exercises_note=NOTE)

lesson(F + "05_Heatmaps_and_Pairplots.ipynb", "Heatmaps, pair plots, facets and publication figures",
["draw and interpret heatmaps of tables and correlation matrices",
 "explore many variables at once with pairplot",
 "build custom small multiples with FacetGrid",
 "prepare figures to a publication standard"],
"""
This notebook covers plots that show many values or variables at once, and finishes with a checklist
and template for figures good enough for a report or journal.
""",
[
SETUP,
'''sns.set_theme(style="whitegrid")
penguins = sns.load_dataset("penguins").dropna()
flights = sns.load_dataset("flights")''',
'''#md
## Heatmap of a table

A heatmap colours each cell of a table by its value. Wide data (rows × columns) goes straight in:
''',
'''table = flights.pivot(index="month", columns="year", values="passengers")
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(table, cmap="rocket_r", annot=True, fmt="d", annot_kws={"size": 7},
            cbar_kws={"label": "passengers (thousands)"}, ax=ax)
ax.set_title("Monthly airline passengers")
plt.show()''',
'''#md
**Reading it:** darker is more. Passengers rise from left to right (growth over the years) and the
darkest cells each year are July and August (summer peaks). Both patterns are visible at a glance, which
is hard from 144 numbers in a table.

## Correlation heatmap

A correlation matrix uses a **diverging** palette centred on zero, so positive and negative
correlations get different colours and zero is neutral.
''',
'''num = penguins.select_dtypes("number")
corr = num.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))      # hide the repeated upper triangle

fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(corr, mask=mask, cmap="vlag", vmin=-1, vmax=1, center=0, annot=True, fmt=".2f",
            square=True, linewidths=0.5, ax=ax)
ax.set_title("Correlation between penguin measurements")
plt.show()''',
'''#md
Flipper length and body mass are strongly positively correlated (0.87); bill depth is negatively
correlated with the others across species, an effect of the species differences seen in notebook 04.

## Gene expression heatmap

Expression matrices are usually standardised per gene (z-scores), so that genes with different overall
levels can be compared on one colour scale. `clustermap` also reorders rows and columns so similar
ones sit together.
''',
'''expr = pd.read_csv(RAW + "gene_expression.tsv", sep="\\t", index_col="sample")
condition = expr.pop("condition")
z = (expr - expr.mean()) / expr.std()

colours = condition.map({"control": "#999999", "treated": "#0072B2"})
g = sns.clustermap(z.T, cmap="vlag", center=0, col_colors=colours, figsize=(9, 7),
                   cbar_kws={"label": "z-score"})
plt.show()''',
'''#md
Each column is a sample (the top bar marks its condition), each row a gene. If treatment changes some
genes, those rows show colour that differs between treated and control samples. Here the treatment
effect is modest, so the clustering only partly separates the conditions: most control samples group
together, but some treated and control samples mix. That is common with real expression data, and a
reason not to over-read a heatmap: it is a picture for exploring, not a test.

## pairplot

Every pair of numeric variables as a scatter plot, with each variable's distribution on the diagonal.
A quick first look at a new dataset.
''',
'''sns.pairplot(penguins, hue="species", palette="colorblind", corner=True, height=2,
             plot_kws={"alpha": 0.6, "s": 15})
plt.show()''',
'''#md
`corner=True` drops the repeated upper half. Look for pairs where the species separate cleanly, and
for curved or unusual patterns worth a closer look.

## FacetGrid: custom small multiples

`FacetGrid` sets up panels by `row` and `col`, then `map` or `map_dataframe` draws any function in each.
''',
'''tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="time", row="smoker", height=2.8, aspect=1.3, margin_titles=True)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip", alpha=0.6)
g.map_dataframe(sns.regplot, x="total_bill", y="tip", scatter=False, color="black", ci=None)
g.set_axis_labels("total bill", "tip")
plt.show()''',
'''#md
`col_wrap` wraps a long row of panels:
''',
'''labs = pd.read_csv(RAW + "lab_results.csv")
patients = pd.read_csv(RAW + "patients.csv")
df = labs.merge(patients[["patient_id", "site"]], on="patient_id")
g = sns.FacetGrid(df, col="site", col_wrap=2, height=2.6, aspect=1.4, sharex=True, sharey=True)
g.map_dataframe(sns.histplot, x="glucose_mmol", bins=20)
g.set_titles("{col_name}")
plt.show()''',
'''#md
## Publication-quality figures

A checklist:

1. **size for the destination**: a journal single column is about 3.5 inches (89 mm) wide, a double
   column about 7 inches (180 mm). Draw at the final size, so text is not shrunk
2. **readable text**: 7-9 pt at final size; `sns.set_theme(context="paper")` helps
3. **labels with units** on every axis; no internal variable names such as `glucose_mmol`
4. **colour-blind-safe palette**, plus markers or labels so nothing depends on colour alone
5. **consistent colours** for the same group across all figures
6. **say what error bars show** (SD, SE or CI) in the caption
7. **vector format** (PDF, SVG) or PNG/TIFF at 300 dpi or more
8. **panel letters** (A, B, C) for multi-panel figures

A template that puts these together:
''',
'''sns.set_theme(style="ticks", context="paper", font_scale=1.0)
palette = dict(zip(["Adelie", "Chinstrap", "Gentoo"], sns.color_palette("colorblind", 3)))

fig, axes = plt.subplots(1, 2, figsize=(7, 2.8), layout="constrained")

sns.boxplot(data=penguins, x="species", y="body_mass_g", hue="species", palette=palette,
            showfliers=False, width=0.6, ax=axes[0])
sns.stripplot(data=penguins, x="species", y="body_mass_g", color="0.25", size=2, alpha=0.5, ax=axes[0])
axes[0].set(xlabel="", ylabel="Body mass (g)")
axes[0].set_title("A", loc="left", fontweight="bold")

sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species", style="species",
                palette=palette, s=14, ax=axes[1])
axes[1].set(xlabel="Flipper length (mm)", ylabel="Body mass (g)")
axes[1].set_title("B", loc="left", fontweight="bold")
axes[1].legend(title=None, frameon=False, fontsize=7)

sns.despine(fig)
fig.savefig("figure1.pdf")
fig.savefig("figure1.png", dpi=300)
plt.show()''',
'''#md
Caption: *Figure 1. (A) Body mass by species; boxes show the median and interquartile range, points
show individual birds. (B) Body mass against flipper length.*
''',
'''import os
for f in ["figure1.pdf", "figure1.png"]:
    print(f, os.path.getsize(f) // 1024, "KB")
    os.remove(f)
sns.set_theme()''',
],
[SG, "[heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) and [clustermap](https://seaborn.pydata.org/generated/seaborn.clustermap.html)",
 "[Building structured multi-plot grids](https://seaborn.pydata.org/tutorial/axis_grids.html)",
 "[Ten simple rules for better figures (Rougier et al., 2014)](https://doi.org/10.1371/journal.pcbi.1003833)"],
exercises_note=NOTE)

exercises(F, "Seaborn", "Seaborn",
"Exercises for notebooks 01 to 05 of this folder. Several use Seaborn's example datasets, which need an internet connection the first time.",
[
("Load the `penguins` dataset. Draw a histogram of `bill_depth_mm` coloured by species, and describe what you see.",
 '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")
penguins = sns.load_dataset("penguins")
sns.histplot(data=penguins, x="bill_depth_mm", hue="species", bins=25, alpha=0.5)
plt.show()''', "Gentoo penguins have clearly shallower bills; Adelie and Chinstrap overlap."),
("Compare the distribution of `body_mass_g` by species and sex with a violin plot, using `split=True`.",
 '''sns.violinplot(data=penguins, x="species", y="body_mass_g", hue="sex", split=True, inner="quart", palette="colorblind")
plt.show()'''),
("From `tips`, make a bar plot of the mean tip by day, with error bars showing the standard error. Order the days Thur, Fri, Sat, Sun.",
 '''tips = sns.load_dataset("tips")
sns.barplot(data=tips, x="day", y="tip", errorbar="se", order=["Thur", "Fri", "Sat", "Sun"])
plt.show()'''),
("Draw a box plot of `total_bill` by day with the individual bills shown as a strip plot on top.",
 '''ax = sns.boxplot(data=tips, x="day", y="total_bill", color="white", showfliers=False)
sns.stripplot(data=tips, x="day", y="total_bill", alpha=0.5, ax=ax)
plt.show()'''),
("Fit a regression line of `tip` on `total_bill` separately for lunch and dinner with `lmplot`. Do the slopes look different?",
 '''sns.lmplot(data=tips, x="total_bill", y="tip", col="time", height=3.5)
plt.show()
for t, g in tips.groupby("time", observed=True):
    print(t, round(np.polyfit(g["total_bill"], g["tip"], 1)[0], 3))'''),
("Load `../../datasets/raw/lab_results.csv` and plot mean glucose by visit as a line with its 95% confidence band.",
 '''labs = pd.read_csv("../../datasets/raw/lab_results.csv")
sns.lineplot(data=labs, x="visit", y="glucose_mmol", marker="o")
plt.show()'''),
("Make a correlation heatmap of the four numeric lab columns (glucose, haemoglobin, systolic and diastolic BP) with a diverging palette centred at zero and annotated values.",
 '''c = labs[["glucose_mmol", "haemoglobin_g_dl", "systolic_bp", "diastolic_bp"]].corr()
sns.heatmap(c, cmap="vlag", center=0, vmin=-1, vmax=1, annot=True, fmt=".2f", square=True)
plt.show()'''),
("Draw a `pairplot` of the penguins' four measurements coloured by species, using `corner=True`. Which pair of measurements separates the three species best?",
 '''sns.pairplot(penguins.dropna(), hue="species", corner=True, height=1.8, plot_kws={"s": 10})
plt.show()''', "Bill length against bill depth (or bill length against flipper length) separates all three species fairly cleanly."),
("Use `FacetGrid` to draw a histogram of `tip` for every combination of `sex` (columns) and `smoker` (rows).",
 '''g = sns.FacetGrid(tips, col="sex", row="smoker", height=2.5, margin_titles=True)
g.map_dataframe(sns.histplot, x="tip", bins=12)
plt.show()'''),
("Make a two-panel figure 7 inches wide, in the `paper` context, suitable for a report: panel A, a box plot of flipper length by species; panel B, a scatter of flipper length against body mass. Label the panels A and B, give units, and save it as a 300 dpi PNG (then delete the file).",
 '''import os
sns.set_theme(style="ticks", context="paper")
p = penguins.dropna()
fig, axes = plt.subplots(1, 2, figsize=(7, 2.8), layout="constrained")
sns.boxplot(data=p, x="species", y="flipper_length_mm", hue="species", palette="colorblind", ax=axes[0])
axes[0].set(xlabel="", ylabel="Flipper length (mm)"); axes[0].set_title("A", loc="left", fontweight="bold")
sns.scatterplot(data=p, x="flipper_length_mm", y="body_mass_g", hue="species", style="species", palette="colorblind", s=12, ax=axes[1])
axes[1].set(xlabel="Flipper length (mm)", ylabel="Body mass (g)"); axes[1].set_title("B", loc="left", fontweight="bold")
sns.despine(fig)
fig.savefig("exercise_figure.png", dpi=300)
plt.show()
os.remove("exercise_figure.png")
sns.set_theme()'''),
])
print("module 08 written")
