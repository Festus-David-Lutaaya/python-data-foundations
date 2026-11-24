from nb import lesson, exercises

F = "05_NumPy/"
FR = "[NumPy user guide](https://numpy.org/doc/stable/user/index.html)"

lesson(F + "01_Introduction_to_NumPy.ipynb", "Introduction to NumPy",
["explain what NumPy is and why data science depends on it",
 "describe how an array differs from a list",
 "compare the speed of lists and arrays",
 "inspect an array's shape, size, dimensions and data type"],
"""
NumPy (Numerical Python) provides the **ndarray**: a grid of numbers of a single type, stored compactly
in memory, with fast operations that work on the whole grid at once. pandas, Matplotlib, SciPy and
scikit-learn are all built on top of it, so understanding arrays makes everything later easier.
""",
[
'''import numpy as np
np.__version__''',
'''#md
## An array versus a list
''',
'''values = [5.4, 7.8, 6.1, 9.2]
arr = np.array(values)
print(values, type(values))
print(arr, type(arr))''',
'''#md
The key difference shows in arithmetic. A list treats `*` and `+` as list operations; an array does
the maths on every element (*vectorisation*).
''',
'''print(values * 2)          # repeats the list
print(arr * 2)             # doubles every value
print(arr + 1, arr / 18)
try:
    values + 1
except TypeError as e:
    print("TypeError:", e)''',
'''#md
| | list | NumPy array |
|---|---|---|
| item types | anything, mixed | one type for all items |
| maths on all items | needs a loop | one expression |
| memory | each item a separate object | one compact block |
| speed on numbers | slow | fast |
| size | grows easily | fixed when created |

## Speed

Timing the sum of squares of a million numbers both ways:
''',
'''import time

n = 1_000_000
py_list = list(range(n))
np_arr = np.arange(n)

t0 = time.perf_counter()
total_list = sum(x * x for x in py_list)
t_list = time.perf_counter() - t0

t0 = time.perf_counter()
total_arr = int((np_arr.astype(np.int64) ** 2).sum())
t_arr = time.perf_counter() - t0

print(total_list == total_arr)
print(f"list: {t_list * 1000:.1f} ms   array: {t_arr * 1000:.1f} ms   ratio: {t_list / t_arr:.0f}x")''',
'''#md
The exact numbers depend on the computer, but the array version is consistently several times faster, and the gap grows for
heavier calculations, because the loop runs in compiled C code instead of in Python.

## Array attributes
''',
'''m = np.array([[5.4, 7.8, 6.1],
              [6.0, 8.1, 5.9]])
print("ndim :", m.ndim)      # number of dimensions
print("shape:", m.shape)     # (rows, columns)
print("size :", m.size)      # total elements
print("dtype:", m.dtype)     # data type of the elements
print("bytes:", m.nbytes)''',
'''#md
`shape` is the attribute you will check most. `(2, 3)` means 2 rows and 3 columns. A 1-D array of 4
values has shape `(4,)`.

## Data types

All elements share one dtype. Mixing types makes NumPy pick a type that fits all of them.
''',
'''print(np.array([1, 2, 3]).dtype)
print(np.array([1, 2.5, 3]).dtype)        # integers became floats
print(np.array([1, "2", 3]).dtype)        # everything became text
print(np.array([True, False]).dtype)''',
'''a = np.array([1.7, 2.2, 3.9])
print(a.astype(int))                       # truncates, does not round
print(np.round(a).astype(int))
print(np.array(["4.5", "6"]).astype(float))''',
'''#md
Common dtypes: `int64`, `float64`, `bool`, `<U` (text). Integers have limits: `int8` holds −128 to
127, and values outside wrap around silently.
''',
'''small = np.array([120, 125], dtype=np.int8)
print(small + 10)''',
'''#md
That wrap-around is why NumPy defaults to 64-bit types. Use smaller types only when memory matters and
you know the range.
''',
],
[FR, "[NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)",
 "[Data types](https://numpy.org/doc/stable/user/basics.types.html)"],
exercises_note="Exercises for this folder are in `exercises/NumPy_Exercises.ipynb`.")

lesson(F + "02_Array_Creation.ipynb", "Creating arrays",
["create arrays from lists and nested lists",
 "use zeros, ones, full, arange, linspace and eye",
 "generate random numbers reproducibly",
 "simulate laboratory measurements from known distributions",
 "load numeric data from a text file"],
"""
Arrays usually come from data files, but you constantly need to create them yourself too: a range of
doses, a grid of zeros to fill in, or simulated measurements to test an analysis on.
""",
[
'''import numpy as np''',
'''#md
## From lists
''',
'''one_d = np.array([12.1, 10.4, 13.8])
two_d = np.array([[1, 2, 3], [4, 5, 6]])
print(one_d.shape, two_d.shape)
print(two_d)''',
'''#md
## Filled arrays
''',
'''print(np.zeros(4))
print(np.ones((2, 3)))
print(np.full((2, 2), 7.5))
print(np.eye(3))                     # identity matrix
print(np.zeros_like(two_d))          # same shape as another array''',
'''#md
## Ranges

- `np.arange(start, stop, step)`: like `range`, stop excluded; works with decimals
- `np.linspace(start, stop, num)`: `num` evenly spaced values, **stop included**
''',
'''print(np.arange(0, 10, 2))
print(np.arange(0, 1, 0.25))
print(np.linspace(0, 1, 5))
doses = np.linspace(0, 100, 11)
print(doses)''',
'''#md
For decimal steps, prefer `linspace`: with `arange`, rounding can make the last value appear or
disappear unexpectedly.

A dilution series uses `geomspace` (equal ratios instead of equal steps):
''',
'''print(np.geomspace(1, 1 / 64, 7))      # two-fold dilutions
print(np.logspace(0, 3, 4))            # 10**0 to 10**3''',
'''#md
## Random numbers

`np.random.default_rng(seed)` creates a random number generator. A fixed **seed** gives the same
numbers every time, so your analysis can be repeated exactly.
''',
'''rng = np.random.default_rng(42)
print(rng.random(3))                       # uniform between 0 and 1
print(rng.integers(1, 7, size=10))         # dice rolls (7 excluded)
print(rng.choice(["A", "B", "C"], size=5))''',
'''#md
### Distributions for simulation

| function | models | parameters |
|---|---|---|
| `rng.normal(mean, sd, n)` | symmetric measurements (height, haemoglobin) | mean, standard deviation |
| `rng.lognormal(mu, sigma, n)` | positive, right-skewed values (concentrations, viral loads) | on the log scale |
| `rng.binomial(n, p, size)` | number of successes out of n trials | trials, probability |
| `rng.poisson(lam, size)` | counts per unit (colonies per plate, cases per week) | mean count |
| `rng.uniform(low, high, n)` | equally likely values in a range | bounds |
''',
'''rng = np.random.default_rng(1)
haemoglobin = rng.normal(loc=13.5, scale=1.6, size=200)
print(haemoglobin[:5].round(1))
print(f"mean {haemoglobin.mean():.2f}, sd {haemoglobin.std(ddof=1):.2f}")''',
'''#md
The sample mean and standard deviation are close to 13.5 and 1.6, but not exact: that is sampling
variation. Larger samples get closer.
''',
'''for n in [10, 100, 10_000]:
    s = rng.normal(13.5, 1.6, n)
    print(f"n={n:>6}: mean {s.mean():.3f}")''',
'''colonies = rng.poisson(lam=35, size=12)              # colonies on 12 plates
positives = rng.binomial(n=50, p=0.12, size=8)       # positives per batch of 50 tests
viral_load = rng.lognormal(mean=8, sigma=1.5, size=6)
print(colonies)
print(positives)
print(viral_load.round(0))''',
'''#md
## A simulated experiment

Three replicate measurements for each of 5 samples, as a 5 × 3 array:
''',
'''rng = np.random.default_rng(7)
true_values = np.array([2.0, 4.0, 6.0, 8.0, 10.0])
replicates = true_values[:, None] + rng.normal(0, 0.3, size=(5, 3))
print(replicates.round(2))
print(replicates.shape)''',
'''#md
`true_values[:, None]` turns the 5 values into a column so they can be added to a 5 × 3 grid; this is
*broadcasting*, explained in notebook 04.

## Loading numbers from a text file

`np.loadtxt` and `np.genfromtxt` read numeric text files. `genfromtxt` copes with missing values.
pandas is usually easier for real tables (module 6).
''',
'''expr = np.genfromtxt("../datasets/raw/gene_expression.tsv", delimiter="\\t", skip_header=1,
                     usecols=range(2, 22))
print(expr.shape, expr.dtype)
print(expr[:3, :5].round(2))''',
'''#md
## Saving and loading arrays
''',
'''np.save("replicates.npy", replicates)
back = np.load("replicates.npy")
print(np.array_equal(back, replicates))

np.savetxt("replicates.csv", replicates, delimiter=",", fmt="%.3f")
print(open("replicates.csv").read())

import os
os.remove("replicates.npy"); os.remove("replicates.csv")''',
],
[FR, "[Array creation](https://numpy.org/doc/stable/user/basics.creation.html)",
 "[Random generator](https://numpy.org/doc/stable/reference/random/generator.html)"],
exercises_note="Exercises for this folder are in `exercises/NumPy_Exercises.ipynb`.")

lesson(F + "03_Array_Indexing_and_Slicing.ipynb", "Indexing and slicing arrays",
["select single elements, rows and columns",
 "slice one- and two-dimensional arrays",
 "filter with boolean indexing and combined conditions",
 "use fancy indexing and np.where",
 "understand views versus copies"],
"""
Selecting parts of an array is the basis of every analysis: one patient's results, all values above a
threshold, the columns for one condition.
""",
[
'''import numpy as np
rng = np.random.default_rng(3)
glucose = rng.normal(6.2, 1.4, 12).round(1)
print(glucose)''',
'''#md
## One dimension

Exactly like lists: positions from 0, negatives from the end, slices exclude the stop.
''',
'''print(glucose[0], glucose[-1])
print(glucose[2:5], glucose[:3], glucose[::3])''',
'''#md
## Two dimensions

`arr[row, column]`. A colon `:` on its own means "all".

A table of 6 participants (rows) by 4 visits (columns):
''',
'''sbp = np.array([
    [142, 138, 135, 131],
    [128, 130, 127, 126],
    [155, 150, 146, 141],
    [118, 121, 119, 117],
    [149, 147, 140, 138],
    [133, 129, 128, 124],
])
print(sbp[2, 0])         # participant 3, visit 1
print(sbp[0])            # participant 1, all visits
print(sbp[:, 0])         # all participants, visit 1
print(sbp[:, -1])        # last visit
print(sbp[1:3, 1:3])     # a block''',
'''#md
Selecting a single column gives a 1-D array. Keep the result 2-D with a slice (`sbp[:, 0:1]`).
''',
'''print(sbp[:, 0].shape, sbp[:, 0:1].shape)''',
'''#md
## Boolean indexing

A comparison gives an array of True/False values (a *mask*). Using the mask as an index keeps the True
positions.
''',
'''mask = glucose >= 7.0
print(mask)
print(glucose[mask])
print(glucose[glucose < 5.6])''',
'''#md
Counting and proportions: True counts as 1.
''',
'''print(mask.sum(), "values at or above 7.0")
print(f"{mask.mean():.0%} of values")''',
'''#md
### Combining conditions

Use `&` (and), `|` (or), `~` (not), with **brackets around each condition**. Python's `and`/`or` do
not work on arrays.
''',
'''print(glucose[(glucose >= 5.6) & (glucose < 7.0)])       # pre-diabetic range
print(glucose[(glucose < 4.0) | (glucose > 8.0)])        # outside a range
print(glucose[~(glucose >= 7.0)])
try:
    glucose[glucose > 5 and glucose < 7]
except ValueError as e:
    print("ValueError:", str(e)[:60], "...")''',
'''#md
### Boolean indexing on a table

Participants whose first visit was 140 or above, and their whole rows:
''',
'''high_at_start = sbp[:, 0] >= 140
print(high_at_start)
print(sbp[high_at_start])
print("change over follow-up:", sbp[high_at_start, -1] - sbp[high_at_start, 0])''',
'''#md
## Fancy indexing

An array or list of positions selects those items, in that order.
''',
'''print(glucose[[0, 3, 7]])
print(sbp[[0, 2, 4], :][:, [0, 3]])     # rows 0, 2, 4; first and last visits
order = np.argsort(glucose)
print(order)
print(glucose[order])                   # sorted values''',
'''#md
`np.argsort` returns the *positions* that would sort the array, which lets you sort one array by
another.

## np.where

`np.where(condition)` gives the positions where a condition is true;
`np.where(condition, a, b)` chooses between two values element by element.
''',
'''print(np.where(glucose >= 7.0))
labels = np.where(glucose >= 7.0, "high", "normal")
print(labels)
capped = np.where(glucose > 8, 8, glucose)
print(capped)''',
'''#md
`np.select` handles more than two categories:
''',
'''category = np.select([glucose < 5.6, glucose < 7.0], ["normal", "borderline"], default="high")
print(list(zip(glucose, category)))''',
'''#md
## Changing values through an index
''',
'''readings = np.array([5.1, -1.0, 6.4, 999.0, 7.2])
readings[(readings < 0) | (readings > 100)] = np.nan      # mark impossible values as missing
print(readings)''',
'''#md
## Views and copies

A **slice** is a *view*: it shares data with the original, so changing it changes the original.
Boolean and fancy indexing return **copies**. Use `.copy()` when you want an independent array.
''',
'''a = np.arange(6)
v = a[1:4]
v[0] = 100
print(a)                 # changed through the view

b = np.arange(6)
c = b[1:4].copy()
c[0] = 100
print(b)                 # unchanged''',
],
[FR, "[Indexing on ndarrays](https://numpy.org/doc/stable/user/basics.indexing.html)",
 "[np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html)"],
exercises_note="Exercises for this folder are in `exercises/NumPy_Exercises.ipynb`.")

lesson(F + "04_Array_Operations.ipynb", "Array operations and statistics",
["do element-wise arithmetic and use universal functions",
 "explain and use broadcasting",
 "compute statistics for a whole array and along an axis",
 "standardise data (z-scores) and compute percentiles",
 "handle NaN and infinity correctly"],
"""
Most numerical work is a few operations applied to many numbers: convert units, subtract a baseline,
average replicates, standardise. NumPy does each of these in one line, over whole arrays.
""",
[
'''import numpy as np''',
'''#md
## Element-wise arithmetic

Operations between arrays of the same shape pair up elements by position.
''',
'''before = np.array([142, 128, 155, 118, 149])
after = np.array([131, 126, 141, 117, 138])
change = after - before
print(change)
print((change / before * 100).round(1))''',
'''#md
## Universal functions (ufuncs)

Functions that act on every element.
''',
'''x = np.array([1, 10, 100, 1000])
print(np.sqrt(x), np.log10(x), np.log(x).round(2), np.exp([0, 1]).round(3))
print(np.abs([-2, 3]), np.round([2.456, 3.14159], 2), np.floor([2.7]), np.ceil([2.1]))''',
'''#md
Log transforms are common for skewed lab values such as concentrations or viral loads:
''',
'''viral_load = np.array([150, 2_400, 38_000, 910_000, 12_000_000])
print(np.log10(viral_load).round(2))''',
'''#md
## Broadcasting

When shapes differ, NumPy stretches the smaller array to match, if the shapes are compatible. Shapes are
compared from the right; each pair of sizes must be equal, or one of them must be 1.

| shapes | result |
|---|---|
| (5,) and scalar | (5,) |
| (6, 4) and (4,) | (6, 4): the row is repeated for every row |
| (6, 4) and (6, 1) | (6, 4): the column is repeated for every column |
| (6, 4) and (6,) | error: compares 4 with 6 |
''',
'''sbp = np.array([
    [142, 138, 135, 131],
    [128, 130, 127, 126],
    [155, 150, 146, 141],
    [118, 121, 119, 117],
    [149, 147, 140, 138],
    [133, 129, 128, 124],
])
baseline = sbp[:, 0:1]            # shape (6, 1)
print(sbp - baseline)             # change from each participant's own baseline''',
'''visit_means = sbp.mean(axis=0)   # shape (4,)
print(visit_means.round(1))
print((sbp - visit_means).round(1))   # deviation from each visit's mean''',
'''try:
    sbp - np.arange(6)
except ValueError as e:
    print("ValueError:", e)''',
'''#md
## Statistical functions

| function | |
|---|---|
| `sum`, `mean`, `median` | totals and centre |
| `min`, `max`, `ptp` | extremes and range |
| `std`, `var` | spread (`ddof=1` for the sample version) |
| `percentile`, `quantile` | cut points |
| `argmin`, `argmax` | position of the extreme |
| `cumsum` | running total |
| `corrcoef` | correlation |
''',
'''rng = np.random.default_rng(5)
hb = rng.normal(13.5, 1.6, 300)
print(f"mean {hb.mean():.2f}  median {np.median(hb):.2f}")
print(f"sd {hb.std(ddof=1):.2f}  variance {hb.var(ddof=1):.2f}")
print(f"min {hb.min():.1f}  max {hb.max():.1f}  range {np.ptp(hb):.1f}")
print("quartiles", np.percentile(hb, [25, 50, 75]).round(2))''',
'''#md
`ddof=1` divides by n − 1, giving the **sample** standard deviation, which is what statistics software
reports. NumPy's default (`ddof=0`) divides by n. With large n they barely differ; with small n they do.
''',
'''small = np.array([4.0, 6.0, 8.0])
print(small.std(), small.std(ddof=1))''',
'''#md
## Statistics along an axis

`axis=0` works **down the rows** (one result per column); `axis=1` works **across the columns** (one
result per row).

```
        axis=1 →
axis=0  [[142 138 135 131]
  ↓      [128 130 127 126] ...
```
''',
'''print("mean per visit      :", sbp.mean(axis=0).round(1))
print("mean per participant:", sbp.mean(axis=1).round(1))
print("highest per visit   :", sbp.max(axis=0))
print("visit of each participant's peak:", sbp.argmax(axis=1))''',
'''#md
Reading this: blood pressure falls on average from the first to the last visit, and every participant's
highest reading is at the first visit except participants 2 and 4, whose second visits were highest.

## Standardisation: z-scores

A z-score says how many standard deviations a value lies from the mean. It puts measurements on
different scales onto a common one.
''',
'''z = (hb - hb.mean()) / hb.std(ddof=1)
print(z[:5].round(2))
print(f"mean of z {z.mean():.3f}, sd of z {z.std(ddof=1):.3f}")
print(f"values more than 2 sd from the mean: {(np.abs(z) > 2).sum()} of {len(z)}")''',
'''#md
For normally distributed data, about 5% of values lie more than 2 standard deviations from the mean, so
roughly 15 of 300 is expected.

## Correlation
''',
'''weight = rng.normal(70, 12, 100)
height = 1.2 + weight / 100 + rng.normal(0, 0.06, 100)
r = np.corrcoef(weight, height)
print(r.round(3))
print(f"r = {r[0, 1]:.2f}")''',
'''#md
`corrcoef` returns a matrix: the diagonal is each variable with itself (1), the off-diagonal value is
the correlation between the two.

## Missing values: NaN

`np.nan` (Not a Number) marks a missing value. Any calculation involving NaN gives NaN, so ordinary
functions return NaN when a single value is missing. The `nan`-functions ignore missing values.
''',
'''results = np.array([5.4, np.nan, 6.1, 7.8, np.nan, 6.6])
print(results.mean(), np.nanmean(results).round(2), np.nanmedian(results), np.nanstd(results, ddof=1).round(3))
print("missing:", np.isnan(results).sum())
print("complete values:", results[~np.isnan(results)])''',
'''#md
NaN is not equal to anything, not even itself, so `results == np.nan` never finds it. Always use `np.isnan`.
''',
'''print(np.nan == np.nan, (results == np.nan).sum(), np.isnan(results).sum())''',
'''#md
Replacing missing values (only after deciding that this is appropriate for the analysis):
''',
'''filled = np.where(np.isnan(results), np.nanmedian(results), results)
print(filled)''',
'''#md
## Infinity

Dividing a non-zero number by zero gives `inf`; zero by zero gives `nan`. NumPy warns instead of
stopping. Log of zero is `-inf`.
''',
'''with np.errstate(divide="ignore", invalid="ignore"):
    ratio = np.array([4.0, 3.0, 0.0]) / np.array([2.0, 0.0, 0.0])
    logs = np.log10(np.array([100.0, 0.0]))
print(ratio, logs)
print(np.isinf(ratio), np.isfinite(ratio))
print(ratio[np.isfinite(ratio)])''',
'''#md
`np.errstate` silences the warnings for that block only, because here we expect them. In real work,
the warnings are useful: they point at zeros you may not have known about.
''',
],
[FR, "[Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)",
 "[Statistics routines](https://numpy.org/doc/stable/reference/routines.statistics.html)",
 "[Universal functions](https://numpy.org/doc/stable/reference/ufuncs.html)"],
exercises_note="Exercises for this folder are in `exercises/NumPy_Exercises.ipynb`.")

lesson(F + "05_Array_Manipulation.ipynb", "Reshaping and combining arrays",
["change an array's shape with reshape, flatten and ravel",
 "transpose arrays and add dimensions",
 "join arrays with concatenate and stack",
 "split arrays into parts",
 "sort arrays and find unique values"],
"""
Data rarely arrives in the shape an analysis needs. Plate readers give 96 numbers in a line that belong
in an 8 × 12 grid; replicate runs come as separate arrays that need joining. This notebook covers
changing shape and combining arrays.
""",
[
'''import numpy as np''',
'''#md
## reshape

`reshape(rows, cols)` rearranges the same values into a new shape. The total size must stay the same.
`-1` means "work this dimension out for me".
''',
'''a = np.arange(12)
print(a.reshape(3, 4))
print(a.reshape(4, -1))
try:
    a.reshape(5, 3)
except ValueError as e:
    print("ValueError:", e)''',
'''#md
### A 96-well plate

A plate reader exports 96 absorbance values in row order (A1, A2, ... A12, B1, ...). Reshaping gives the
plate layout:
''',
'''rng = np.random.default_rng(11)
readings = rng.uniform(0.05, 1.2, 96).round(3)
plate = readings.reshape(8, 12)
rows = "ABCDEFGH"
print(plate.shape)
print("well C5:", plate[rows.index("C"), 5 - 1])
print("row means:", plate.mean(axis=1).round(3))''',
'''#md
## flatten and ravel

Both turn any array into 1-D. `flatten` always returns a copy; `ravel` returns a view when it can.
''',
'''print(plate[:2, :3].flatten())
print(plate.ravel().shape)''',
'''#md
## Transpose

`.T` swaps rows and columns.
''',
'''m = np.array([[1, 2, 3], [4, 5, 6]])
print(m.T, m.T.shape)''',
'''#md
## Adding a dimension

Useful for broadcasting: turning a row of values into a column.
''',
'''v = np.array([10, 20, 30])
print(v.shape, v[:, np.newaxis].shape, v[np.newaxis, :].shape, np.expand_dims(v, 1).shape)''',
'''#md
## Joining arrays

- `np.concatenate` joins along an existing axis
- `np.vstack` stacks rows (one array on top of another)
- `np.hstack` places arrays side by side
- `np.column_stack` turns 1-D arrays into the columns of a table
- `np.stack` creates a new axis
''',
'''run1 = np.array([[5.1, 5.3], [6.0, 6.2]])
run2 = np.array([[5.0, 5.4], [6.1, 5.9]])
print(np.concatenate([run1, run2]))            # axis=0: more rows
print(np.concatenate([run1, run2], axis=1))    # more columns
print(np.vstack([run1, run2]).shape, np.hstack([run1, run2]).shape)
print(np.stack([run1, run2]).shape)            # (2 runs, 2, 2)''',
'''age = np.array([34, 51, 47])
glucose = np.array([5.4, 7.8, 6.1])
table = np.column_stack([age, glucose])
print(table)''',
'''#md
Shapes must match along the joined edge:
''',
'''try:
    np.vstack([np.ones((2, 3)), np.ones((2, 4))])
except ValueError as e:
    print("ValueError:", e)''',
'''#md
## Splitting arrays
''',
'''data = np.arange(10)
print(np.split(data, 2))
print(np.split(data, [3, 7]))             # cut at positions 3 and 7
print(np.array_split(data, 3))            # unequal parts allowed

left, right = np.hsplit(plate, 2)         # two halves of the plate
print(left.shape, right.shape)''',
'''#md
A train/test split, the first step in model evaluation, is just shuffling and splitting:
''',
'''rng = np.random.default_rng(0)
idx = rng.permutation(20)
train_idx, test_idx = idx[:15], idx[15:]
print(sorted(train_idx.tolist()), sorted(test_idx.tolist()))''',
'''#md
## Sorting and unique values
''',
'''values = np.array([3, 1, 2, 3, 3, 1])
print(np.sort(values))
print(np.sort(values)[::-1])               # descending
print(np.unique(values))
u, counts = np.unique(values, return_counts=True)
print(dict(zip(u.tolist(), counts.tolist())))''',
'''results = np.array(["Neg", "Pos", "Neg", "Inc", "Neg", "Pos"])
print(np.unique(results, return_counts=True))''',
'''#md
## Putting it together: replicate analysis

Three runs of 8 samples, measured in triplicate within each run. Stack the runs into a
3 × 8 × 3 array, then average over replicates and runs.
''',
'''rng = np.random.default_rng(21)
true = np.linspace(1, 8, 8)
runs = [true[:, None] + rng.normal(0, 0.25, (8, 3)) + shift for shift in (0.0, 0.2, -0.1)]
cube = np.stack(runs)                    # (run, sample, replicate)
print(cube.shape)

per_run = cube.mean(axis=2)              # (3, 8): replicate means
print(per_run.round(2))
print("run effect:", (per_run.mean(axis=1) - per_run.mean()).round(2))
print("within-run CV %:", (cube.std(axis=2, ddof=1) / cube.mean(axis=2) * 100).mean().round(1))''',
'''#md
Run 2 reads highest and run 3 lowest, matching the shifts built into the simulation (+0.2 and −0.1
relative to run 1); random noise moves the estimates a little. The coefficient of variation (CV) summarises replicate precision as a percentage of the
mean.
''',
],
[FR, "[Array manipulation routines](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)",
 "[Sorting, searching and counting](https://numpy.org/doc/stable/reference/routines.sort.html)"],
exercises_note="Exercises for this folder are in `exercises/NumPy_Exercises.ipynb`.")

exercises(F, "NumPy", "NumPy",
"Exercises for notebooks 01 to 05 of this folder.",
[
("Create an array from the list `[12.1, 10.4, 13.8, 9.7, 11.2]`. Print its shape, dtype, and the values converted from g/dL to g/L (multiply by 10).",
 '''import numpy as np
hb = np.array([12.1, 10.4, 13.8, 9.7, 11.2])
print(hb.shape, hb.dtype, hb * 10)'''),
("Time summing the squares of numbers 0 to 999,999 with a list comprehension and with NumPy. Which is faster, and by roughly how much on your computer?",
 '''import time
t = time.perf_counter(); sum([x * x for x in range(1_000_000)]); t_list = time.perf_counter() - t
a = np.arange(1_000_000, dtype=np.int64)
t = time.perf_counter(); (a ** 2).sum(); t_np = time.perf_counter() - t
print(f"list {t_list*1000:.1f} ms, numpy {t_np*1000:.1f} ms, about {t_list / t_np:.0f}x")'''),
("Simulate 500 haemoglobin measurements with mean 13.2 and standard deviation 1.5, using seed 2025. Print the mean, median, sample standard deviation, minimum and maximum, each rounded to 2 places.",
 '''rng = np.random.default_rng(2025)
hb = rng.normal(13.2, 1.5, 500)
print(hb.mean().round(2), np.median(hb).round(2), hb.std(ddof=1).round(2), hb.min().round(2), hb.max().round(2))'''),
("Using the simulated values, what proportion lie below 12.0 (a common anaemia cut-off)? Print the values between 12 and 12.5.",
 '''print(f"{(hb < 12).mean():.1%}")
print(hb[(hb >= 12) & (hb <= 12.5)].round(2))'''),
("Simulate colony counts on 20 plates with a Poisson mean of 40. Print the counts, their mean and variance. For a Poisson distribution, how should the two compare?",
 '''counts = rng.poisson(40, 20)
print(counts, counts.mean(), counts.var(ddof=1).round(1))''', "For Poisson data the variance is about equal to the mean."),
("Make a 4 × 5 array of the numbers 1 to 20. Select the second row, the last column, and the block of rows 2-3, columns 3-4 (counting from 1).",
 '''m = np.arange(1, 21).reshape(4, 5)
print(m[1], m[:, -1], m[1:3, 2:4], sep="\\n")'''),
("Replace impossible values (below 0 or above 50) in `np.array([4.2, -1, 6.8, 99, 5.5])` with NaN, then compute the mean of the remaining values.",
 '''x = np.array([4.2, -1, 6.8, 99, 5.5])
x[(x < 0) | (x > 50)] = np.nan
print(x, np.nanmean(x).round(2))'''),
("For the blood pressure table below, compute each participant's change from their first to last visit and the mean of each visit.\n\n```python\nsbp = np.array([[142, 138, 131], [128, 130, 126], [155, 150, 141]])\n```",
 '''sbp = np.array([[142, 138, 131], [128, 130, 126], [155, 150, 141]])
print(sbp[:, -1] - sbp[:, 0], sbp.mean(axis=0).round(1))'''),
("Convert `np.array([4.1, 5.6, 7.2, 6.0, 8.9])` to z-scores and label each value `\"high\"` if z > 1, otherwise `\"typical\"`.",
 '''v = np.array([4.1, 5.6, 7.2, 6.0, 8.9])
z = (v - v.mean()) / v.std(ddof=1)
print(z.round(2), np.where(z > 1, "high", "typical"))'''),
("Reshape 24 random values into a 4 × 6 'plate', compute each row's mean, then split the plate into left and right halves.",
 '''p = np.random.default_rng(0).uniform(0, 1, 24).reshape(4, 6)
print(p.mean(axis=1).round(3))
left, right = np.hsplit(p, 2)
print(left.shape, right.shape)'''),
("Count each result in `np.array([\"Pos\", \"Neg\", \"Neg\", \"Pos\", \"Neg\", \"Inc\", \"Neg\"])` with `np.unique`.",
 '''r = np.array(["Pos", "Neg", "Neg", "Pos", "Neg", "Inc", "Neg"])
print(np.unique(r, return_counts=True))'''),
])
print("module 05 written")
