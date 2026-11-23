# Python data foundations

Notebooks that take you from your first line of Python to cleaning, summarising
and plotting real-looking data with NumPy, pandas, matplotlib and seaborn.

This is part 1 of a two-part path. Part 2, the machine learning guide,
assumes everything covered here.

## Notebooks

| # | Notebook | Covers |
|---|----------|--------|
| **Python** | | |
| 01 | `01_python_basics` | variables, types, arithmetic, comparisons, getting help |
| 02 | `02_strings` | f-strings, slicing, string methods |
| 03 | `03_lists_tuples` | lists, copying, sorting, tuples, `enumerate`, `zip` |
| 04 | `04_dicts_sets` | dictionaries, look-ups, counting, sets |
| 05 | `05_control_flow` | `if`, `for`, `while`, comprehensions |
| 06 | `06_functions` | arguments, defaults, return values, scope, `lambda`, type hints |
| 07 | `07_files_errors_modules` | `pathlib`, text, CSV and JSON files, exceptions, imports, dates |
| 08 | `08_classes_objects` | classes, methods, dataclasses, and why this matters for libraries |
| **NumPy** | | |
| 09 | `09_numpy_arrays` | arrays, shape, indexing, views, boolean masks, random numbers |
| 10 | `10_numpy_operations` | axes, broadcasting, missing values, linear algebra, vectorising |
| **pandas** | | |
| 11 | `11_pandas_basics` | reading data, `loc`/`iloc`, filtering, new columns, sorting |
| 12 | `12_pandas_cleaning` | duplicates, text, categories, dates, numbers stored as text, outliers, missing values |
| 13 | `13_pandas_groupby` | `groupby`, `agg`, `crosstab`, `transform`, time groups |
| 14 | `14_pandas_merge_reshape` | `merge` with `validate`, `concat`, `pivot`, `melt`, change from baseline |
| **Plotting** | | |
| 15 | `15_matplotlib` | figure and axes, the main chart types, annotation, saving |
| 16 | `16_seaborn` | distributions, group comparisons, relationships, heatmaps, small multiples |
| **Putting it together** | | |
| 17 | `17_case_study_eda` | a full exploratory analysis of antimicrobial resistance data |

Each notebook is notes and worked code. The outputs are saved, so you can read
them on GitHub without running anything.

## Data

All datasets in `data/` are simulated:

| file | contents |
|---|---|
| `patients.csv` | 300 patients: site, sex, age, weight, height, HIV status |
| `visits.csv` | repeated lab results (Hb, WBC, CRP) per patient |
| `isolates_raw.csv` | microbiology results with deliberate data-entry problems |
| `isolates_clean.csv` | the same after notebook 12 |

Recreate them with `python data/make_data.py`.

## Setup

```
pip install -r requirements.txt
jupyter lab
```

Then open `notebooks/01_python_basics.ipynb` and work through in order.
With Anaconda, everything needed is already installed.

The notebooks were run with Python 3.13, NumPy 2.x and pandas 3.0, and the code
also works with pandas 2.x.
