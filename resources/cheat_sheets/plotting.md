# Plotting cheat sheet: Matplotlib and Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

## Matplotlib: the pattern

```python
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, marker="o", linestyle="--", color="C0", label="series")
ax.set(title="Title states the finding", xlabel="x (units)", ylabel="y (units)")
ax.legend()
fig.savefig("figure.png", dpi=300, bbox_inches="tight")
plt.show()
```

## Matplotlib: plot types

```python
ax.plot(x, y)                    # line
ax.bar(cats, values)             # bar; ax.barh for horizontal
ax.scatter(x, y, s=10, alpha=0.5, c=z, cmap="viridis")
ax.hist(values, bins=30, edgecolor="white")
ax.boxplot([g1, g2], tick_labels=["A", "B"])
ax.errorbar(x, y, yerr=err, capsize=4)
ax.pie(values, labels=labels, autopct="%1.0f%%")
```

## Matplotlib: customising

```python
ax.set_xlim(0, 10)   ax.set_ylim(bottom=0)   ax.set_xticks([0, 5, 10])
ax.axhline(7, color="grey", linestyle=":")   ax.axvline(...)   ax.axvspan(a, b, alpha=0.2)
ax.annotate("note", xy=(x, y), xytext=(x2, y2), arrowprops={"arrowstyle": "->"})
ax.text(x, y, "label")
ax.grid(axis="y")   ax.spines[["top", "right"]].set_visible(False)
fig.colorbar(points, ax=ax, label="units")
plt.style.use("seaborn-v0_8-whitegrid")
```

## Matplotlib: several panels

```python
fig, axes = plt.subplots(2, 3, figsize=(12, 6), sharex=True, sharey=True, layout="constrained")
for ax, (name, g) in zip(axes.flat, df.groupby("group")): ...
fig, ax = plt.subplot_mosaic("AAB;CCB")
fig.suptitle("Overall title")
```

## Seaborn: the pattern

```python
sns.set_theme(style="whitegrid", context="notebook")    # context: paper, notebook, talk, poster
sns.scatterplot(data=df, x="col1", y="col2", hue="group", style="group", palette="colorblind")
```

## Seaborn: which function

| question | axes-level | figure-level |
|---|---|---|
| distribution | `histplot`, `kdeplot`, `ecdfplot` | `displot` |
| category comparison | `countplot`, `barplot`, `boxplot`, `violinplot`, `stripplot`, `swarmplot`, `pointplot` | `catplot` |
| relationship | `scatterplot`, `lineplot`, `regplot` | `relplot`, `lmplot`, `jointplot` |
| many variables | `heatmap` | `pairplot`, `clustermap` |

Figure-level functions take `col=`, `row=`, `height=` and `aspect=`.

## Seaborn: useful options

```python
hue=  style=  size=                      # map columns to colour, marker, size
order=["a", "b"]  hue_order=[...]        # category order
errorbar=("ci", 95)  "se"  "sd"  None    # error bars
multiple="stack"                         # histplot: layer, stack, dodge, fill
common_norm=False                        # kdeplot: each group scaled separately
sns.heatmap(corr, cmap="vlag", center=0, vmin=-1, vmax=1, annot=True, fmt=".2f")
g = sns.FacetGrid(df, col="a", row="b"); g.map_dataframe(sns.histplot, x="x")
sns.despine()
```

## Choosing colours

- groups: `"colorblind"`, `"tab10"`, `"Set2"`, and add markers or labels as well as colour
- low to high: `"viridis"`, `"rocket"`, `"Blues"`
- either side of zero: `"vlag"`, `"RdBu"`, `"coolwarm"`, with `center=0`
- avoid `"jet"` and `"rainbow"`

## Rules of thumb

- bars start at zero
- never two y-axes on one chart; use two panels with a shared x-axis
- label axes with units; say what error bars show
- export PDF or SVG for print, PNG at 300 dpi or more otherwise
