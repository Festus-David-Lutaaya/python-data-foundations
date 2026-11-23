from nb import build

D = "notebooks/"

# ---------------------------------------------------------------- 01
build(D + "01_python_basics.ipynb", [
'''#md
# 01 Python basics

Values, variables, types, arithmetic, printing and comments.

Python runs code from top to bottom. In a notebook each cell runs when you press
Shift+Enter, and the last line of a cell is shown automatically.
''',
'''#md
## Values and variables

A variable is a name that points at a value. You create it with `=`.
Names are case sensitive, cannot start with a number, and by convention use
lower case with underscores (`sample_count`, not `SampleCount`).
''',
'''sample_id = "S001"
age = 34
weight = 61.5
consented = True

age''',
'''#md
`print()` shows several things at once. Without it, only the last line of a cell is displayed.
''',
'''print(sample_id)
print(age, weight, consented)''',
'''#md
## Types

Every value has a type. The basic ones:

| type | example | used for |
|---|---|---|
| `int` | `34` | whole numbers |
| `float` | `61.5` | decimals |
| `str` | `"S001"` | text |
| `bool` | `True` | yes / no |
| `NoneType` | `None` | "no value" |
''',
'''print(type(age), type(weight), type(sample_id), type(consented), type(None))''',
'''#md
Convert between types with `int()`, `float()`, `str()` and `bool()`.
Data read from files often arrives as text, so this comes up a lot.
''',
'''text_age = "34"
print(int(text_age) + 1)
print(float("12.7"))
print(str(2026) + "-01")
print(int(9.99))        # cuts off, does not round
print(round(9.99))''',
'''#md
## Arithmetic

`+ - * /` work as expected. Also:

- `//` whole-number division
- `%` remainder
- `**` power

`/` always gives a float, even for `10 / 2`.
''',
'''print(10 / 3)
print(10 // 3)
print(10 % 3)
print(2 ** 10)

weight_kg = 70
height_m = 1.75
bmi = weight_kg / height_m ** 2
round(bmi, 1)''',
'''#md
Floats are stored in binary, so some decimals are not exact. Compare floats with
`math.isclose()` or by rounding, never with `==`.
''',
'''import math

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(math.isclose(0.1 + 0.2, 0.3))''',
'''#md
## Updating a variable
''',
'''count = 0
count = count + 1
count += 1          # same thing, shorter
count *= 10
count''',
'''#md
## Comparisons and logic

Comparisons give `True` or `False`: `==  !=  <  >  <=  >=`.
Combine them with `and`, `or`, `not`.
''',
'''hb = 10.4
print(hb < 11)
print(hb >= 11 and hb <= 17)
print(11 <= hb <= 17)          # Python allows chained comparisons
print(not consented)''',
'''#md
## Comments

Anything after `#` on a line is ignored. Use comments to explain *why*, not *what*.
''',
'''# reference range from the lab manual, adults
hb_low = 11.0''',
'''#md
## Getting help

- `help(round)` shows the documentation
- in Jupyter, `round?` does the same
- press Tab after a name to see what is available
''',
'''help(round)''',
])

# ---------------------------------------------------------------- 02
build(D + "02_strings.ipynb", [
'''#md
# 02 Strings

Text in Python is a `str`. Single and double quotes are the same.
Strings cannot be changed in place: every method returns a new string.
''',
'''name = "Escherichia coli"
site = 'Kampala'
long_text = """Triple quotes
span several lines."""
print(long_text)''',
'''#md
## f-strings

The clearest way to build text from values. Put `f` before the quote and
variables in `{}`. After a colon you can give a format.
''',
'''patient = "P0012"
age = 34
hb = 10.456
pct = 0.2564

print(f"{patient} is {age} years old")
print(f"Hb: {hb:.1f} g/dL")
print(f"Resistant: {pct:.1%}")
print(f"{'ID':<8}{'Age':>5}")
print(f"{patient:<8}{age:>5}")
print(f"{1234567:,}")''',
'''#md
## Indexing and slicing

Positions start at 0. Negative numbers count from the end.
A slice `[start:stop]` includes start and excludes stop.
''',
'''code = "ISO-2025-0042"
print(code[0])
print(code[-1])
print(code[0:3])
print(code[4:8])
print(code[-4:])
print(len(code))''',
'''#md
## Useful methods
''',
'''raw = "  Urine  "
print(repr(raw.strip()))
print("BLOOD".lower(), "blood".upper(), "wound swab".title())
print("E. coli".replace("E.", "Escherichia"))
print("ISO-2025-0042".split("-"))
print("-".join(["ISO", "2025", "0042"]))
print("ISO-2025".startswith("ISO"), "report.csv".endswith(".csv"))
print("coli" in "Escherichia coli")
print("Kampala".find("pa"))
print("42".zfill(4))''',
'''#md
Cleaning a messy value usually chains several methods:
''',
'''entry = "  urine "
clean = entry.strip().title()
clean''',
'''#md
## Checking what a string contains
''',
'''print("123".isdigit(), "12.5".isdigit(), "abc".isalpha(), "   ".isspace())''',
'''#md
## Escape characters

`\\n` is a new line, `\\t` a tab. A raw string `r"..."` keeps backslashes as they
are, which is handy for Windows paths and regular expressions.
''',
'''print("line one\\nline two")
print("col1\\tcol2")
print(r"C:\\data\\new")''',
])

# ---------------------------------------------------------------- 03
build(D + "03_lists_tuples.ipynb", [
'''#md
# 03 Lists and tuples

A list holds an ordered collection of values and can be changed.
A tuple is the same but cannot be changed.
''',
'''sites = ["Kampala", "Gulu", "Mbarara"]
ages = [34, 28, 51, 19]
mixed = ["P001", 34, True, None]   # allowed, but usually a sign a dict or table fits better
print(sites, len(sites))''',
'''#md
## Indexing and slicing

Same rules as strings.
''',
'''print(sites[0], sites[-1])
print(ages[1:3])
print(ages[::-1])      # reversed''',
'''#md
## Changing a list
''',
'''sites.append("Mbale")          # add to the end
sites.insert(1, "Jinja")       # add at a position
sites.extend(["Lira", "Arua"]) # add several
print(sites)

sites.remove("Lira")           # remove by value
last = sites.pop()             # remove and return the last item
sites[0] = "Kampala Central"   # replace
print(sites, last)''',
'''#md
## Sorting and searching
''',
'''ages = [34, 28, 51, 19]
print(sorted(ages))                 # new sorted list
print(sorted(ages, reverse=True))
ages.sort()                         # sorts in place, returns None
print(ages)
print(min(ages), max(ages), sum(ages), sum(ages) / len(ages))
print(51 in ages, ages.index(51), ages.count(28))''',
'''#md
## Copying: a common surprise

`b = a` does not copy. Both names point at the same list.
''',
'''a = [1, 2, 3]
b = a
b.append(4)
print(a)          # a changed too

c = a.copy()      # or list(a), or a[:]
c.append(5)
print(a, c)''',
'''#md
## Lists of lists

A simple way to hold rows of data. For anything bigger, use pandas (notebook 11).
''',
'''rows = [
    ["P001", 34, 12.1],
    ["P002", 28, 10.4],
    ["P003", 51, 13.8],
]
print(rows[1])
print(rows[1][2])''',
'''#md
## Tuples

Use a tuple for a fixed group of values, like coordinates or a record that should not change.
Unpacking assigns each item to its own name.
''',
'''location = (0.3476, 32.5825)
lat, lon = location
print(lat, lon)

def min_max(values):
    return min(values), max(values)    # returns a tuple

low, high = min_max([4, 9, 1, 7])
print(low, high)''',
'''#md
## Handy built-ins for sequences
''',
'''ids = ["P001", "P002", "P003"]
hbs = [12.1, 10.4, 13.8]

for i, pid in enumerate(ids):
    print(i, pid)

for pid, hb in zip(ids, hbs):
    print(pid, hb)

print(list(range(5)), list(range(2, 10, 2)))''',
])

# ---------------------------------------------------------------- 04
build(D + "04_dicts_sets.ipynb", [
'''#md
# 04 Dictionaries and sets

A dictionary maps keys to values: look a value up by name instead of by position.
A set holds unique values with no order.
''',
'''patient = {
    "id": "P0012",
    "age": 34,
    "sex": "F",
    "tests": ["Hb", "WBC"],
}
print(patient["age"])
print(patient.get("site"))               # None instead of an error
print(patient.get("site", "unknown"))''',
'''#md
## Adding, changing and removing
''',
'''patient["site"] = "Gulu"
patient["age"] = 35
del patient["tests"]
print(patient)
print("site" in patient)''',
'''#md
## Looping over a dictionary
''',
'''for key, value in patient.items():
    print(f"{key:>5}: {value}")

print(list(patient.keys()))
print(list(patient.values()))''',
'''#md
## Dictionaries as look-up tables

A very common use: translate codes into labels, or recode messy values.
''',
'''recode = {"F": "Female", "M": "Male"}
codes = ["F", "M", "M", "F", "U"]
print([recode.get(c, "Unknown") for c in codes])''',
'''#md
## Counting with a dictionary
''',
'''results = ["S", "R", "S", "S", "I", "R", "S"]
counts = {}
for r in results:
    counts[r] = counts.get(r, 0) + 1
print(counts)

from collections import Counter
print(Counter(results))
print(Counter(results).most_common(1))''',
'''#md
## Nested dictionaries

JSON files (notebook 07) read into exactly this shape.
''',
'''lab = {
    "P001": {"hb": 12.1, "wbc": 6.2},
    "P002": {"hb": 10.4, "wbc": 11.9},
}
print(lab["P002"]["wbc"])

for pid, values in lab.items():
    print(pid, values["hb"])''',
'''#md
## Sets

Sets remove duplicates and make "which are in both / only in one" questions easy.
''',
'''enrolled = {"P001", "P002", "P003", "P004"}
sampled = {"P002", "P004", "P005"}

print(enrolled & sampled)      # in both
print(enrolled - sampled)      # enrolled but no sample
print(sampled - enrolled)      # sample but not enrolled: a data problem
print(enrolled | sampled)      # either

print(set(["Urine", "Blood", "Urine"]))''',
])

# ---------------------------------------------------------------- 05
build(D + "05_control_flow.ipynb", [
'''#md
# 05 Control flow

`if` to choose, `for` and `while` to repeat, comprehensions to build lists in one line.

Python uses indentation (4 spaces) to mark which lines belong to a block.
''',
'''#md
## if / elif / else
''',
'''hb = 10.4

if hb < 11:
    status = "Low"
elif hb > 17:
    status = "High"
else:
    status = "Normal"

status''',
'''#md
Empty values count as false: `0`, `""`, `[]`, `{}`, `None`. So `if items:` means "if the list is not empty".
''',
'''notes = ""
if not notes:
    print("No notes recorded")''',
'''#md
Checking for `None` uses `is`:
''',
'''value = None
if value is None:
    print("missing")''',
'''#md
A one-line `if` for simple choices:
''',
'''age = 15
group = "child" if age < 18 else "adult"
group''',
'''#md
## for loops
''',
'''hbs = [12.1, 10.4, 13.8, 9.7]

low = 0
for hb in hbs:
    if hb < 11:
        low += 1
print(f"{low} of {len(hbs)} low")''',
'''#md
`break` stops the loop, `continue` skips to the next item.
''',
'''for hb in hbs:
    if hb is None:
        continue
    if hb < 10:
        print("Critical value found:", hb)
        break''',
'''#md
## while loops

Repeat until a condition is false. Make sure something inside changes the condition.
''',
'''cells = 100
hours = 0
while cells < 10_000:
    cells *= 2
    hours += 4
print(hours, "hours to pass 10,000 cells")''',
'''#md
## Comprehensions

A compact way to build a list from another list. Read it as
"value **for** item **in** list **if** condition".
''',
'''hbs = [12.1, 10.4, 13.8, 9.7]

rounded = [round(h) for h in hbs]
low = [h for h in hbs if h < 11]
flags = ["L" if h < 11 else "N" for h in hbs]
print(rounded, low, flags)

ids = ["P001", "P002"]
lookup = {pid: hb for pid, hb in zip(ids, hbs)}     # dict comprehension
print(lookup)''',
'''#md
Keep comprehensions short. If one needs two lines of thought, write a normal loop.

## Nested loops
''',
'''for site in ["Kampala", "Gulu"]:
    for specimen in ["Urine", "Blood"]:
        print(site, specimen)''',
])

# ---------------------------------------------------------------- 06
build(D + "06_functions.ipynb", [
'''#md
# 06 Functions

A function packages code under a name so you can reuse it and test it.
''',
'''def bmi(weight_kg, height_cm):
    """Body mass index from weight in kg and height in cm."""
    return weight_kg / (height_cm / 100) ** 2

round(bmi(70, 175), 1)''',
'''#md
The text in triple quotes right after `def` is the docstring. `help(bmi)` shows it.

## Arguments

- positional: matched by order
- keyword: matched by name, easier to read
- defaults: used when the argument is left out
''',
'''def classify_hb(hb, low=11.0, high=17.0):
    if hb < low:
        return "Low"
    if hb > high:
        return "High"
    return "Normal"

print(classify_hb(10.4))
print(classify_hb(10.4, low=10))
print(classify_hb(hb=18, high=18.5))''',
'''#md
Do not use a list or dict as a default value: it is created once and shared between calls.
Use `None` and create it inside.
''',
'''def add_result(result, results=None):
    if results is None:
        results = []
    results.append(result)
    return results

print(add_result("S"))
print(add_result("R"))''',
'''#md
## Returning several values
''',
'''def summary(values):
    n = len(values)
    mean = sum(values) / n
    return n, mean, min(values), max(values)

n, mean, lo, hi = summary([12.1, 10.4, 13.8, 9.7])
print(n, round(mean, 2), lo, hi)''',
'''#md
## Any number of arguments

`*args` collects extra positional arguments into a tuple, `**kwargs` collects extra
keyword arguments into a dict. You will see these in library code.
''',
'''def mean_of(*values):
    return sum(values) / len(values)

def describe(**info):
    for k, v in info.items():
        print(k, "=", v)

print(mean_of(1, 2, 3, 4))
describe(site="Gulu", n=40)''',
'''#md
## Scope

Variables created inside a function exist only inside it.
A function can read outside variables, but it is clearer to pass them in.
''',
'''threshold = 11

def is_low(hb):
    return hb < threshold     # reads the outer variable

def make_local():
    temp = 5
    return temp

print(is_low(10))
print(make_local())
# print(temp)  would fail: temp only existed inside make_local''',
'''#md
## lambda

A one-line function without a name. Mostly used as an argument to another function.
''',
'''records = [("P001", 12.1), ("P002", 9.7), ("P003", 13.8)]
print(sorted(records, key=lambda r: r[1]))
print(max(records, key=lambda r: r[1]))''',
'''#md
## Type hints

Optional labels that say what a function expects and returns.
Python does not enforce them, but editors and readers find them useful.
''',
'''def egfr_stage(egfr: float) -> str:
    if egfr >= 90:
        return "G1"
    if egfr >= 60:
        return "G2"
    if egfr >= 30:
        return "G3"
    if egfr >= 15:
        return "G4"
    return "G5"

[egfr_stage(x) for x in [95, 72, 41, 20, 9]]''',
'''#md
## Good habits

- one function, one job
- a name that says what it returns (`classify_hb`, not `do_stuff`)
- return values instead of printing them, so other code can use the result
''',
])

# ---------------------------------------------------------------- 07
build(D + "07_files_errors_modules.ipynb", [
'''#md
# 07 Files, errors and modules

Reading and writing files, handling errors, and using code from other modules.
''',
'''#md
## Paths with pathlib

`pathlib.Path` handles file paths on Windows, Mac and Linux the same way.
''',
'''from pathlib import Path

data_dir = Path("..") / "data"
print(data_dir.resolve())
print(sorted(p.name for p in data_dir.glob("*.csv")))

f = data_dir / "patients.csv"
print(f.exists(), f.suffix, f.stem)''',
'''#md
## Reading and writing text files

`with open(...)` closes the file for you, even if something goes wrong.
`"r"` reads, `"w"` writes (replacing the file), `"a"` appends.
''',
'''out = Path("notes.txt")

with open(out, "w") as fh:
    fh.write("first line\\n")
    fh.write("second line\\n")

with open(out) as fh:
    for line in fh:
        print(line.strip())

out.unlink()       # delete the demo file''',
'''#md
## CSV files with the csv module

For quick jobs. For real analysis use pandas (notebook 11).
''',
'''import csv

with open(data_dir / "patients.csv") as fh:
    reader = csv.DictReader(fh)
    first_rows = [next(reader) for _ in range(3)]

for row in first_rows:
    print(row["patient_id"], row["site"], row["age"])     # note: age is text here''',
'''#md
## JSON

JSON maps directly onto Python dicts and lists.
''',
'''import json

record = {"id": "P0012", "tests": {"hb": 10.4, "wbc": 6.1}, "flags": ["low_hb"]}

text = json.dumps(record, indent=2)
print(text)

back = json.loads(text)
print(back["tests"]["hb"])

# to a file:  json.dump(record, open("x.json", "w"))
# from a file: json.load(open("x.json"))''',
'''#md
## Errors and exceptions

When something goes wrong, Python raises an exception. Read the last line of the
error first: it names the type and the cause.

Common ones: `ValueError`, `TypeError`, `KeyError`, `IndexError`,
`FileNotFoundError`, `ZeroDivisionError`.
''',
'''def to_number(text):
    try:
        return float(text)
    except ValueError:
        return None

print([to_number(x) for x in ["12.5", "n/a", "7", ""]])''',
'''#md
Catch the specific error you expect. A bare `except:` hides real bugs.
`else` runs when nothing failed, `finally` always runs.
''',
'''try:
    with open(data_dir / "missing.csv") as fh:
        content = fh.read()
except FileNotFoundError as e:
    print("Could not open:", e.filename)
else:
    print("read", len(content), "characters")
finally:
    print("done")''',
'''#md
Raise your own errors when input does not make sense:
''',
'''def bmi(weight_kg, height_cm):
    if height_cm <= 0:
        raise ValueError(f"height must be positive, got {height_cm}")
    return weight_kg / (height_cm / 100) ** 2

try:
    bmi(70, 0)
except ValueError as e:
    print(e)''',
'''#md
## Modules and imports

A module is a `.py` file. Import a whole module, a part of it, or give it a short name.
''',
'''import math
from statistics import mean, median
import datetime as dt

print(math.sqrt(16), mean([1, 2, 3]), median([3, 1, 2]))
print(dt.date.today())''',
'''#md
Your own functions can live in a file such as `helpers.py` next to the notebook,
then `from helpers import bmi`.

Install packages from a terminal:

```
pip install pandas seaborn
```

or with conda: `conda install pandas seaborn`.
''',
'''#md
## Dates with datetime
''',
'''from datetime import date, datetime, timedelta

collected = datetime.strptime("14/03/2025", "%d/%m/%Y")
print(collected)
print(collected.strftime("%Y-%m-%d"))
print(collected + timedelta(days=28))
print((date(2025, 12, 31) - collected.date()).days, "days")''',
])

# ---------------------------------------------------------------- 08
build(D + "08_classes_objects.ipynb", [
'''#md
# 08 Classes and objects

You do not need to write many classes for data analysis, but every library you use
is built from them. Knowing the basics makes pandas, scikit-learn and matplotlib
easier to understand: `df.mean()` is a method of a DataFrame object,
`model.fit()` is a method of a model object.
''',
'''#md
## A simple class

A class is a template. An object is one thing made from it.
`__init__` runs when the object is created; `self` is the object itself.
''',
'''class Sample:
    def __init__(self, sample_id, specimen, volume_ml=0.0):
        self.sample_id = sample_id      # attributes: data stored on the object
        self.specimen = specimen
        self.volume_ml = volume_ml
        self.results = {}

    def add_result(self, test, value):  # methods: functions that belong to it
        self.results[test] = value

    def is_complete(self, required=("hb", "wbc")):
        return all(t in self.results for t in required)

s = Sample("S001", "Blood", 5)
s.add_result("hb", 12.1)
print(s.sample_id, s.results, s.is_complete())
s.add_result("wbc", 6.0)
print(s.is_complete())''',
'''#md
## How it should print

`__repr__` controls what you see when the object is displayed.
''',
'''class Sample:
    def __init__(self, sample_id, specimen):
        self.sample_id = sample_id
        self.specimen = specimen

    def __repr__(self):
        return f"Sample({self.sample_id!r}, {self.specimen!r})"

[Sample("S001", "Blood"), Sample("S002", "Urine")]''',
'''#md
## dataclasses

For classes that mostly hold data, `@dataclass` writes `__init__` and `__repr__` for you.
''',
'''from dataclasses import dataclass, field

@dataclass
class Isolate:
    isolate_id: str
    organism: str
    results: dict = field(default_factory=dict)

    def resistant_to(self):
        return [ab for ab, r in self.results.items() if r == "R"]

iso = Isolate("ISO-0001", "E. coli", {"ciprofloxacin": "R", "ceftriaxone": "S"})
print(iso)
print(iso.resistant_to())''',
'''#md
## Inheritance

A class can build on another one and change or add behaviour.
''',
'''class Test:
    def __init__(self, value):
        self.value = value
    def flag(self):
        return "N"

class Haemoglobin(Test):
    def flag(self):
        return "L" if self.value < 11 else "N"

print(Test(5).flag(), Haemoglobin(9.8).flag())''',
'''#md
## Why this matters for the rest of the course

The same pattern appears in every library:

```python
df = pd.read_csv("x.csv")    # create an object
df.head()                    # call a method
df.shape                     # read an attribute (no brackets)

model = RandomForestClassifier(n_estimators=200)   # create with settings
model.fit(X, y)                                    # method that changes the object
model.feature_importances_                         # attribute set by fit()
```

`dir(obj)` lists everything an object has.
''',
'''print([name for name in dir(iso) if not name.startswith("_")])''',
])
print("part 1 written")
