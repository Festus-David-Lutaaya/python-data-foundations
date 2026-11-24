# Foundations of Python Programming for Data Analysis

An open course that takes you from no programming experience to importing, cleaning, analysing and
visualising real datasets with Python, NumPy, pandas, Matplotlib and Seaborn.

| | |
|---|---|
| **Level** | Beginner to intermediate |
| **Audience** | Students, researchers, scientists, statisticians and data analysts |
| **Prerequisites** | Basic computer literacy. No programming experience needed |
| **Suggested duration** | 6 weeks (30-36 contact hours) |

## Course objectives

By the end of the course you will be able to:

1. understand Python programming fundamentals and computational thinking
2. write and run Python scripts and Jupyter notebooks
3. work with Python data structures and control flow
4. perform numerical computations with NumPy
5. import, clean, transform and analyse datasets with pandas
6. create publication-quality visualisations with Matplotlib and Seaborn
7. apply Python to real data analysis problems
8. organise and document reproducible analysis projects

## Modules

| folder | module | notebooks |
|---|---|---|
| [00_Introduction](00_Introduction) | Introduction to Python | what Python is; installing and using the environment |
| [01_Python_Fundamentals](01_Python_Fundamentals) | Python fundamentals | variables and data types; operators; input and output |
| [02_Control_Flow](02_Control_Flow) | Control flow | conditional statements; for loops and comprehensions; while loops |
| [03_Data_Structures](03_Data_Structures) | Data structures | strings; lists; tuples and sets; dictionaries and nested data |
| [04_Functions_and_Modules](04_Functions_and_Modules) | Functions and modules | functions; lambda; modules; error handling and files |
| [05_NumPy](05_NumPy) | Numerical computing with NumPy | introduction; creating arrays; indexing; operations and statistics; reshaping |
| [06_Pandas](06_Pandas) | Data analysis with pandas | introduction; Series and DataFrames; import and export; exploration; cleaning; manipulation; grouping; merging and reshaping |
| [07_Matplotlib](07_Matplotlib) | Visualisation with Matplotlib | introduction; basic plots; customising and exporting; subplots |
| [08_Seaborn](08_Seaborn) | Statistical graphics with Seaborn | introduction; distributions; categorical plots; relationships; heatmaps, pair plots, facets and publication figures |
| [09_Capstone_Project](09_Capstone_Project) | Capstone project | exploratory analysis of a clinical study dataset |

Work through the folders in order. Each module builds on the ones before it.

## Learning levels

| level | modules | expected competency |
|---|---|---|
| 1. Python fundamentals | 00-04 | write basic Python programs and work with data structures |
| 2. Scientific computing | 05-06 | perform numerical computations and manipulate structured datasets |
| 3. Data visualisation | 07-08 and capstone | explore, interpret and communicate data with visualisations |

## How each module is organised

Every lesson notebook follows the same layout: title, learning objectives, introduction, concepts with
code demonstrations and their outputs, practical examples, and further reading. The text explains what
each function does, why it is useful, and how to read its output.

Each module also has an `exercises/` folder with two notebooks:

- `*_Exercises.ipynb`: tasks with empty cells for your code
- `*_Solutions.ipynb`: worked solutions, to check yourself after trying

The examples come from public health, laboratory science, biology, statistics and general data
science (sales, restaurant bills, penguins, flights).

## Capstone project

The capstone combines every module: take the raw `clinic_study.csv`, find and fix its problems,
derive new variables, describe the participants and outcomes, make at least five figures and explain
the findings. The brief, stages and deliverables are in
[09_Capstone_Project/README.md](09_Capstone_Project/README.md), with a starter template and a complete
worked example.

## Repository structure

```text
.
├── README.md
├── LICENSE
├── requirements.txt
├── 00_Introduction/ ... 08_Seaborn/      lesson notebooks + exercises/
├── 09_Capstone_Project/
│   ├── README.md                         project brief
│   ├── analysis_template.ipynb           start here
│   ├── analysis.ipynb                    worked example
│   └── figures/
├── datasets/
│   ├── raw/                              original data (never edited)
│   ├── processed/                        cleaned data written by notebooks
│   └── make_datasets.py                  regenerates the raw data
├── resources/
│   ├── python_documentation.md
│   ├── useful_resources.md
│   └── cheat_sheets/
└── _build/                               scripts that generate the notebooks
```

## Setup

1. Install Python 3.10 or newer, either from [python.org](https://www.python.org/downloads/) or with
   [Anaconda](https://www.anaconda.com/download) / [Miniforge](https://github.com/conda-forge/miniforge)
2. Download this repository (green **Code** button, then **Download ZIP**), or clone it:

   ```bash
   git clone <repository URL>
   cd python-data-foundations
   ```

3. Create an environment and install the packages:

   ```bash
   python -m venv .venv
   source .venv/bin/activate          # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. Start JupyterLab and open `00_Introduction/01_Introduction_to_Python.ipynb`:

   ```bash
   jupyter lab
   ```

Module `00_Introduction/02_Python_Environment.ipynb` covers these steps in more detail, including
VS Code and Google Colab.

## Datasets

All course datasets in `datasets/raw/` are **simulated**: they look like real data, including the
errors, but describe no real people. `datasets/make_datasets.py` regenerates them exactly.

| file | contents |
|---|---|
| `patients.csv` | 300 study participants: site, sex, age, weight, height, smoking, group |
| `lab_results.csv` | repeated visits: glucose, haemoglobin, blood pressure |
| `sample_register_raw.csv` | a messy laboratory sample register, used for cleaning |
| `clinic_study.csv` | the capstone dataset: a three-arm study with baseline and six-month outcomes |
| `daily_sales.csv` | two years of daily sales for three shops |
| `sites.xlsx` | site details and staff, in two sheets |
| `gene_expression.tsv` | 24 samples × 20 genes in two conditions |
| `sequences.txt` | short DNA sequences |

Some modules also use Seaborn's public example datasets (`penguins`, `tips`, `titanic`, `flights`,
`fmri`, `mpg`), which download automatically the first time, so an internet connection is needed.

## Regenerating the notebooks

The notebooks are generated from the scripts in `_build/`, then executed so that outputs are saved.
To change a lesson, edit its script and rebuild:

```bash
PYTHONPATH=_build python _build/m06.py
jupyter nbconvert --to notebook --execute --inplace 06_Pandas/*.ipynb
```

## Licence

Course content is released under the Creative Commons Attribution 4.0 licence; see [LICENSE](LICENSE).
