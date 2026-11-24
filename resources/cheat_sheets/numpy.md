# NumPy cheat sheet

```python
import numpy as np
```

## Creating arrays

```python
np.array([1, 2, 3])
np.array([[1, 2], [3, 4]])
np.zeros(5)   np.ones((2, 3))   np.full((2, 2), 7)   np.eye(3)
np.arange(0, 10, 2)             # stop excluded
np.linspace(0, 1, 5)            # stop included
rng = np.random.default_rng(42)
rng.random(5)  rng.integers(1, 7, 10)  rng.normal(0, 1, 100)  rng.choice(arr, 3)
```

## Inspecting

```python
a.shape   a.ndim   a.size   a.dtype
a.astype(float)
```

## Indexing

```python
a[0]   a[-1]   a[1:4]   a[::2]
m[row, col]   m[0]   m[:, 0]   m[1:3, :2]
a[a > 5]                        # boolean mask
a[(a > 2) & (a < 8)]            # & | ~ with brackets
a[[0, 2, 4]]                    # fancy indexing
np.where(a > 5)                 # positions
np.where(a > 5, "high", "low")  # choose values
```

## Maths and statistics

```python
a + 1   a * b   a ** 2   np.sqrt(a)   np.log10(a)   np.exp(a)   np.round(a, 2)
a.sum()  a.mean()  np.median(a)  a.std(ddof=1)  a.var(ddof=1)  a.min()  a.max()
np.percentile(a, [25, 50, 75])
a.argmin()  a.argmax()  a.cumsum()
np.corrcoef(x, y)
m.mean(axis=0)                  # down rows: one value per column
m.mean(axis=1)                  # across columns: one value per row
z = (a - a.mean()) / a.std(ddof=1)
```

## Missing values

```python
np.nan
np.isnan(a)   np.isfinite(a)
np.nanmean(a)   np.nanmedian(a)   np.nanstd(a, ddof=1)
```

## Shape

```python
a.reshape(3, 4)   a.reshape(-1, 2)   a.flatten()   a.ravel()   m.T
a[:, np.newaxis]
np.concatenate([a, b])   np.vstack([a, b])   np.hstack([a, b])   np.column_stack([a, b])
np.split(a, 3)   np.array_split(a, 3)
np.sort(a)   np.argsort(a)   np.unique(a, return_counts=True)
```

## Broadcasting rule

Shapes are compared from the right; each pair must be equal or one of them 1.
`(6, 4) - (4,)` works; `(6, 4) - (6, 1)` works; `(6, 4) - (6,)` fails.
