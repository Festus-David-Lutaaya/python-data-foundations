from nb import lesson, exercises

# =====================================================================================
# 00 Introduction  (Module 1, topics 1.1 - 1.6)
# =====================================================================================
F = "00_Introduction/"

lesson(F + "01_Introduction_to_Python.ipynb", "Introduction to Python",
["describe what Python is and where it is used",
 "explain the strengths and limitations of Python for data analysis",
 "name the main parts of the Python ecosystem: interpreter, distributions, packages and libraries",
 "check which Python version and packages you are running"],
"""
Python is a general-purpose programming language created by Guido van Rossum and first released in 1991.
It was designed to be readable: code often looks close to plain English, and indentation (spaces at the
start of a line) is part of the syntax rather than a matter of style.

Today Python is one of the most widely used languages in the world, and the most common one for data
analysis, scientific computing and machine learning.
""",
[
'''#md
## Where Python is used

| field | examples |
|---|---|
| data analysis and statistics | cleaning survey data, summarising clinical trials, financial reports |
| scientific research | genomics, physics simulations, climate models, image analysis |
| machine learning and AI | prediction models, image recognition, language models |
| automation | renaming thousands of files, filling forms, scheduled reports |
| web development | websites and web services (Django, Flask, FastAPI) |
| education | a first language in many universities |

## Strengths

- **readable**: code is easy to write, review and hand over to someone else
- **free and open source**: no licence fees; runs on Windows, macOS and Linux
- **huge ecosystem**: hundreds of thousands of packages for almost any task
- **interactive**: Jupyter notebooks mix code, results, figures and notes in one document
- **community**: abundant tutorials, documentation and answered questions

## Limitations

- **speed**: plain Python loops are slower than compiled languages such as C. For data work this is
  largely solved by libraries like NumPy and pandas, which run their heavy work in compiled code.
- **memory**: Python objects take more memory than raw numbers in some other languages
- **versions and environments**: projects can need different package versions, so environments have
  to be managed (see the next notebook)
- **dynamic typing**: mistakes such as adding text to a number are found when the code runs, not before
''',
'''#md
## The Python ecosystem

| term | meaning |
|---|---|
| **interpreter** | the program that reads and runs Python code. "Python 3.12" means version 3.12 of the interpreter |
| **standard library** | modules that come with Python: `math`, `statistics`, `csv`, `datetime`, `pathlib`... |
| **package / library** | extra code you install, such as NumPy or pandas |
| **pip** | Python's package installer: `pip install pandas` |
| **distribution** | Python bundled with packages and tools. **Anaconda** and **Miniconda** are popular for data work |
| **conda** | Anaconda's package and environment manager |
| **environment** | an isolated set of packages for one project |

The scientific Python stack used in this course:

| library | role |
|---|---|
| NumPy | fast numerical arrays and maths |
| pandas | tables (DataFrames): import, clean, transform, summarise |
| Matplotlib | general plotting |
| Seaborn | statistical plotting built on Matplotlib |
| Jupyter | notebooks for interactive work |

## Checking your setup

The cell below asks the interpreter about itself. Press **Shift+Enter** to run it.
''',
'''import sys
import platform

print("Python version:", sys.version.split()[0])
print("Operating system:", platform.system(), platform.release())
print("Interpreter location:", sys.executable)''',
'''#md
**What the output means**: the first line is the version of Python running this notebook. This course
needs Python 3.10 or newer. The last line shows where the interpreter lives, which tells you which
installation or environment is being used, useful when a package seems to be "missing".

Now check that the course libraries are installed and see their versions:
''',
'''import importlib

for name in ["numpy", "pandas", "matplotlib", "seaborn"]:
    try:
        module = importlib.import_module(name)
        print(f"{name:<11} {module.__version__}")
    except ImportError:
        print(f"{name:<11} NOT INSTALLED: run  pip install {name}")''',
'''#md
## A first look at Python

A few lines show the flavour of the language. Do not worry about the details; each idea has its own
notebook later.
''',
'''# a list of measurements
heights_cm = [162, 175, 158, 181, 169]

# the average, rounded to one decimal place
average = sum(heights_cm) / len(heights_cm)
print(f"Average height: {average:.1f} cm")

# how many are above the average?
above = [h for h in heights_cm if h > average]
print(f"{len(above)} of {len(heights_cm)} people are taller than average: {above}")''',
'''#md
**What happened**: we stored five numbers in a *list*, used the built-in functions `sum` and `len` to
compute the mean, and printed it with a *formatted string*. The last part picked out values above the
mean with a *list comprehension*. All of these are covered in modules 1 to 3.

## The Zen of Python

Python's design principles are built in. They are worth reading once.
''',
'''import this''',
],
["[Python official documentation](https://docs.python.org/3/)",
 "[The Python tutorial](https://docs.python.org/3/tutorial/index.html), the official introduction",
 "[Python Package Index (PyPI)](https://pypi.org/), where packages are published",
 "[Anaconda distribution](https://www.anaconda.com/download)"])

lesson(F + "02_Python_Environment.ipynb", "The Python environment",
["choose between Jupyter Notebook, JupyterLab, Google Colab and VS Code",
 "install Python and the course packages, and create an environment",
 "write and run a first program in a notebook and as a script",
 "explain Python syntax: indentation, comments, statements and expressions"],
"""
Before writing analyses you need somewhere to write and run code. This notebook compares the common
tools, shows how to install everything, and introduces the basic rules of Python syntax.
""",
[
'''#md
## Development environments

| tool | what it is | best for |
|---|---|---|
| **Jupyter Notebook** | browser-based notebooks: code cells, output and text together | learning, exploration, reports |
| **JupyterLab** | the newer Jupyter interface: notebooks, files, terminals and editors in tabs | day-to-day data analysis (recommended for this course) |
| **Google Colab** | Jupyter in the cloud, free, nothing to install | trying things quickly; working on a borrowed or shared computer |
| **VS Code** | a full code editor with notebook support, debugging and Git | larger projects, scripts and packages |

All of them run the same Python code. The notebooks in this course work in any of them.

## Installing Python

**Option 1: Anaconda (easiest for beginners).** Download from anaconda.com, install, then open
*Anaconda Navigator* and launch JupyterLab. NumPy, pandas, Matplotlib and Seaborn are already included.

**Option 2: Python from python.org plus pip.** Install Python 3, then in a terminal:

```bash
pip install -r requirements.txt     # installs everything listed in the course requirements file
jupyter lab                         # opens JupyterLab in the browser
```

**Option 3: Google Colab.** Go to colab.research.google.com and upload a notebook. The course packages
are already installed.

## Environments

An *environment* is a separate folder of packages for one project, so that updating a package for one
project does not break another.

With Python's built-in `venv`:

```bash
python -m venv .venv                 # create an environment in a folder called .venv
source .venv/bin/activate            # macOS / Linux
.venv\\Scripts\\activate               # Windows
pip install -r requirements.txt
```

With conda:

```bash
conda create -n pyda python=3.12 numpy pandas matplotlib seaborn jupyterlab
conda activate pyda
```

## Working in a notebook

- a notebook is made of **cells**. *Code cells* run Python; *Markdown cells* hold formatted text like this one
- **Shift+Enter** runs a cell and moves to the next; **Ctrl+Enter** runs it and stays
- the number in `[ ]` beside a cell shows the order cells were run. Cells share variables, so running
  them out of order can confuse you. **Kernel > Restart and Run All** runs everything from the top
- the last expression in a cell is displayed automatically; use `print()` to show several things

## Your first program
''',
'''print("Hello, World!")''',
'''#md
`print` is a *function*: a named piece of code that does a job. Here the job is to display the text in
quotes. Text in quotes is called a *string*.
''',
'''print("Python is ready.")
print("2 + 3 =", 2 + 3)''',
'''#md
**What the output shows**: `print` can take several items separated by commas; it shows them with a
space between them. The `2 + 3` was calculated before printing.

## Running a Python script

Code can also live in a plain text file ending in `.py` and run from a terminal. The cell below writes
a tiny script to a file and runs it, just as you would in a terminal with `python hello.py`.
''',
'''from pathlib import Path
import subprocess
import sys

Path("hello.py").write_text('name = "analyst"\\nprint(f"Hello, {name}! This ran as a script.")\\n')
result = subprocess.run([sys.executable, "hello.py"], capture_output=True, text=True)
print(result.stdout)
Path("hello.py").unlink()        # tidy up''',
'''#md
Notebooks are best for exploring and explaining; scripts are best for code you run repeatedly, such as
a monthly report or a cleaning step in a pipeline.

## Python syntax

### Statements and expressions

- an **expression** produces a value: `2 + 3`, `len("hello")`, `age > 18`
- a **statement** is an instruction: `x = 5` (assignment), `print(x)`, `import math`

In a notebook, if the last line of a cell is an expression, its value is displayed:
''',
'''10 * 4 + 2''',
'''#md
### Comments

Anything after `#` on a line is ignored by Python. Comments explain *why* the code does something.
Good comments make an analysis understandable to someone else, including you in six months.
''',
'''# Body mass index = weight in kg divided by height in metres squared
weight_kg = 68
height_m = 1.72
bmi = weight_kg / height_m ** 2   # ** means "to the power of"
bmi''',
'''#md
### Indentation

Python uses indentation (conventionally **4 spaces**) to group lines into blocks, for example the lines
that belong to an `if`. Other languages use braces `{ }` for this; in Python the spaces *are* the syntax.
''',
'''temperature = 38.4

if temperature >= 38.0:
    print("Fever")                       # indented: runs only when the condition is true
    print("Recommend follow-up")
print("Check complete")                  # not indented: always runs''',
'''#md
Wrong indentation is an error, not a style problem:
''',
'''code = """
if temperature >= 38.0:
print("Fever")
"""
try:
    exec(code)
except IndentationError as e:
    print("IndentationError:", e.msg)''',
'''#md
### Case sensitivity and line length

- `Age`, `age` and `AGE` are three different names
- one statement per line is the norm; long expressions can be wrapped inside brackets
''',
'''age = 30
Age = 40
print(age, Age)

total = (120 + 340 + 210
         + 80 + 95)                # brackets allow the expression to continue on the next line
print(total)''',
'''#md
### Errors are normal

Every programmer sees errors all day. Python tells you the *type* of error and *where* it happened.
Read the **last line first**.
''',
'''try:
    print(undefined_variable)
except NameError as e:
    print(type(e).__name__, "-", e)''',
'''#md
`NameError` means Python does not know that name: usually a typo, or a cell that has not been run yet.
Module 4 covers errors in detail.
''',
],
["[JupyterLab documentation](https://jupyterlab.readthedocs.io/)",
 "[Google Colab](https://colab.research.google.com/)",
 "[VS Code: Python and Jupyter](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)",
 "[Python style guide (PEP 8)](https://peps.python.org/pep-0008/)",
 "[venv documentation](https://docs.python.org/3/library/venv.html)"],
exercises_note="Exercises for this module are in `exercises/Introduction_Exercises.ipynb`.")

exercises(F, "Introduction", "your first programs",
"These exercises check that your environment works and that you can run and write simple cells.",
[
("Print the text `Hello, Python!` and, on a second line, your name.",
 '''print("Hello, Python!")
print("Ada Lovelace")'''),
("Print the Python version you are using.",
 '''import sys
print(sys.version.split()[0])'''),
("Without a calculator, use Python to compute the number of seconds in a 365-day year.",
 '''60 * 60 * 24 * 365''', "31,536,000 seconds."),
("Write a comment explaining what the next line does, then calculate the BMI of a person who weighs 82 kg and is 1.79 m tall.",
 '''# BMI = weight (kg) / height (m) squared
82 / 1.79 ** 2''', "About 25.6."),
("The cell below has an indentation error. Copy it into your answer cell and fix it.\n\n```python\nscore = 72\nif score >= 50:\nprint(\"pass\")\n```",
 '''score = 72
if score >= 50:
    print("pass")'''),
("Write a two-line script to a file called `greet.py` that prints a greeting, then run it from Python with `subprocess` as shown in the notebook. Delete the file afterwards.",
 '''from pathlib import Path
import subprocess, sys
Path("greet.py").write_text('print("Greetings from a script")\\nprint(2 * 21)\\n')
print(subprocess.run([sys.executable, "greet.py"], capture_output=True, text=True).stdout)
Path("greet.py").unlink()'''),
])

# =====================================================================================
# 01 Python fundamentals  (Module 1 topics 1.7-1.10, Module 2 topics 2.1-2.5)
# =====================================================================================
F = "01_Python_Fundamentals/"

lesson(F + "01_Variables_and_Data_Types.ipynb", "Variables and data types",
["create variables and follow Python naming conventions",
 "explain dynamic typing",
 "use the core data types: int, float, str, bool and None",
 "convert between types explicitly, and recognise implicit conversion",
 "avoid common pitfalls with floating-point numbers"],
"""
A program works with values: numbers, text, true/false answers. Variables give those values names so you
can use them later. Every value has a *type*, which decides what you can do with it.
""",
[
'''#md
## Variables

A variable is a name that refers to a value. You create one with `=` (the *assignment operator*).
Read `age = 34` as "age is set to 34", not "age equals 34".
''',
'''patient_id = "P0042"
age = 34
weight_kg = 61.5
is_smoker = False

print(patient_id, age, weight_kg, is_smoker)''',
'''#md
A variable can be given a new value at any time. The old value is forgotten.
''',
'''count = 10
count = count + 5      # take the current value, add 5, store it back
count''',
'''#md
Several variables can be assigned on one line, and two values can be swapped without a temporary variable:
''',
'''x, y, z = 1, 2, 3
x, y = y, x
print(x, y, z)''',
'''#md
## Naming rules and conventions

**Rules** (break these and Python refuses):

- letters, digits and underscores only; cannot start with a digit
- cannot be a keyword such as `if`, `for`, `class`, `True`
- case sensitive: `Weight` and `weight` are different

**Conventions** (from the style guide, PEP 8):

| kind | style | example |
|---|---|---|
| variables and functions | `snake_case` | `mean_age`, `sample_count` |
| constants | `UPPER_CASE` | `MAX_DOSE_MG = 500` |
| classes | `CamelCase` | `DataFrame` |

Choose names that say what the value is: `systolic_bp` is better than `x` or `sbp1`.
''',
'''import keyword
print(keyword.kwlist)''',
'''#md
## Dynamic typing

In Python the *value* has a type, not the name. The same name can point to a number and later to text.
This is convenient, but it means mistakes such as treating text as a number only show up when the code runs.
''',
'''value = 42
print(type(value))
value = "forty-two"
print(type(value))''',
'''#md
## The core data types

| type | examples | used for |
|---|---|---|
| `int` | `0`, `34`, `-7`, `1_000_000` | counts, whole numbers |
| `float` | `61.5`, `0.001`, `1.2e-5` | measurements, anything with decimals |
| `str` | `"P0042"`, `'Blood'` | text, codes, labels |
| `bool` | `True`, `False` | yes/no answers, results of comparisons |
| `NoneType` | `None` | "no value" or "not recorded" |

`type()` tells you the type of any value:
''',
'''examples = [34, 61.5, "P0042", True, None, 3e8]
for v in examples:
    print(repr(v).ljust(8), type(v).__name__)''',
'''#md
**Reading the output**: `3e8` is scientific notation for 3 × 10⁸, and it is a float. `repr` shows strings
with their quotes so you can tell the text `"P0042"` from a variable named P0042.

### Integers

Python integers can be as large as you need.
''',
'''print(2 ** 100)
population = 8_100_000_000     # underscores make big numbers readable; Python ignores them
print(population)''',
'''#md
### Floats and precision

Floats are stored in binary, so most decimal fractions are stored as close approximations. This happens
in every programming language and in spreadsheets.
''',
'''print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)''',
'''#md
The result is 0.30000000000000004, so comparing it with `==` gives `False`. When comparing floats, allow
a small tolerance:
''',
'''import math
print(math.isclose(0.1 + 0.2, 0.3))
print(round(0.1 + 0.2, 2) == 0.3)''',
'''#md
`round` uses *round half to even* ("banker's rounding"), which avoids bias when many numbers are rounded:
''',
'''print(round(2.5), round(3.5), round(4.5))
print(round(2.675, 2))     # 2.675 is really stored as 2.67499999..., so it rounds down''',
'''#md
For money or anything that must be exact in decimal, use the `decimal` module:
''',
'''from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))''',
'''#md
### Strings

Text in single or double quotes. Module 3 covers strings in depth.
''',
'''sample_type = "Blood"
note = 'collected at 08:30'
print(sample_type + " sample " + note)
print(len(sample_type))''',
'''#md
### Booleans

`True` and `False` are the result of comparisons, and they control decisions (module 2).
Internally they behave like 1 and 0, which makes counting easy:
''',
'''results = [True, False, True, True]
print(sum(results), "positive out of", len(results))''',
'''#md
### None

`None` means "no value". It is what you use when a measurement was not taken. Check for it with `is`:
''',
'''hdl = None
print(hdl is None)''',
'''#md
## Type conversion

### Explicit conversion

You convert a value on purpose with `int()`, `float()`, `str()` and `bool()`.
This is essential because data read from files and from user input usually arrives as text.
''',
'''age_text = "34"
age_number = int(age_text)
print(age_number + 1)

print(float("61.5"), str(2026), int(9.99), int("101", 2))''',
'''#md
**Note**: `int(9.99)` gives 9. Converting a float to int cuts off the decimals; it does not round.

Conversion fails if the text is not a valid number:
''',
'''try:
    int("34 years")
except ValueError as e:
    print("ValueError:", e)''',
'''#md
`bool()` turns values into True or False. Zero, empty text and `None` are false; almost everything else is true:
''',
'''for v in [0, 1, -5, 0.0, "", "No", None, []]:
    print(repr(v).ljust(6), bool(v))''',
'''#md
`bool("No")` is `True`: any non-empty text is true. To interpret yes/no answers in data, compare the text,
for example `answer == "Yes"`.

### Implicit conversion

Python converts automatically in a few safe cases, such as mixing int and float in arithmetic:
''',
'''print(3 + 2.5, type(3 + 2.5))
print(True + 2)''',
'''#md
It will **not** silently mix numbers and text, because the meaning would be unclear:
''',
'''try:
    print("Age: " + 34)
except TypeError as e:
    print("TypeError:", e)
print("Age: " + str(34))''',
'''#md
## Example: demographic and biological data in variables
''',
'''participant = "HC-017"
age_years = 52
sex = "Female"
weight_kg = 74.2
height_m = 1.63
systolic_bp = 138
diabetic = False
hba1c = None              # not measured

bmi = weight_kg / height_m ** 2
print(participant, "BMI:", round(bmi, 1))
print("Types:", type(age_years).__name__, type(bmi).__name__, type(diabetic).__name__, type(hba1c).__name__)''',
],
["[Python tutorial: numbers, strings](https://docs.python.org/3/tutorial/introduction.html)",
 "[Built-in types](https://docs.python.org/3/library/stdtypes.html)",
 "[Floating-point arithmetic: issues and limitations](https://docs.python.org/3/tutorial/floatingpoint.html)",
 "[PEP 8 naming conventions](https://peps.python.org/pep-0008/#naming-conventions)"],
exercises_note="Exercises for this folder are in `exercises/Python_Fundamentals_Exercises.ipynb`.")

lesson(F + "02_Operators.ipynb", "Operators",
["use arithmetic operators, including floor division, modulus and powers",
 "compare values with comparison operators",
 "combine conditions with and, or and not",
 "update variables with compound assignment",
 "test membership with in and not in, and identity with is",
 "predict the order in which operators are applied"],
"""
Operators are symbols that act on values: `+` adds, `>` compares, `and` combines conditions.
They are the building blocks of every calculation and every decision in a program.
""",
[
'''#md
## Arithmetic operators

| operator | meaning | example | result |
|---|---|---|---|
| `+` | addition | `7 + 2` | 9 |
| `-` | subtraction | `7 - 2` | 5 |
| `*` | multiplication | `7 * 2` | 14 |
| `/` | division (always a float) | `7 / 2` | 3.5 |
| `//` | floor division (rounds down) | `7 // 2` | 3 |
| `%` | modulus (remainder) | `7 % 2` | 1 |
| `**` | exponent (power) | `7 ** 2` | 49 |
''',
'''a, b = 17, 5
print(a + b, a - b, a * b, a / b)
print(a // b, a % b, a ** b)''',
'''#md
Floor division and modulus are a pair: 17 = 5 × 3 + 2. They are useful for splitting units:
''',
'''total_minutes = 135
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{total_minutes} minutes = {hours} h {minutes} min")

print(divmod(135, 60))      # both at once''',
'''#md
`%` also tests divisibility: a number is even when `n % 2 == 0`.

With negative numbers, `//` rounds towards minus infinity, not towards zero:
''',
'''print(-7 // 2, -7 % 2)''',
'''#md
## Percentages and proportions

A common task: turning counts into proportions and percentages.
''',
'''positive = 37
tested = 412
proportion = positive / tested
print(f"proportion {proportion:.4f}, percentage {proportion * 100:.1f}%")
print(f"same thing with a format code: {proportion:.1%}")''',
'''#md
## Operator precedence

Python follows the usual maths order: brackets, then powers, then `* / // %`, then `+ -`.
When in doubt, add brackets: they cost nothing and make intent clear.
''',
'''print(2 + 3 * 4)
print((2 + 3) * 4)
print(-3 ** 2)       # ** happens before the minus sign: -(3 ** 2)
print((-3) ** 2)''',
'''#md
## Comparison operators

| operator | meaning |
|---|---|
| `==` | equal to (two equals signs; one `=` is assignment) |
| `!=` | not equal to |
| `>`, `<` | greater than, less than |
| `>=`, `<=` | greater than or equal, less than or equal |

They always return `True` or `False`.
''',
'''glucose = 7.4
print(glucose > 7.0, glucose == 7.4, glucose != 6.1, glucose <= 5.5)''',
'''#md
Python allows *chained* comparisons, which read like maths:
''',
'''haemoglobin = 12.8
print(12.0 <= haemoglobin <= 15.5)''',
'''#md
Strings are compared alphabetically (by character codes), so uppercase sorts before lowercase:
''',
'''print("apple" < "banana", "Zebra" < "apple", "10" < "9")''',
'''#md
`"10" < "9"` is `True` because text is compared character by character and "1" comes before "9".
Numbers stored as text sort wrongly: convert them first.

## Logical operators

| operator | true when |
|---|---|
| `and` | both conditions are true |
| `or` | at least one is true |
| `not` | reverses true and false |
''',
'''age = 67
smoker = True
sbp = 152

high_risk = age >= 65 and sbp >= 140
any_risk = smoker or sbp >= 140
print(high_risk, any_risk, not smoker)''',
'''#md
Truth table for `and` and `or`:
''',
'''for p in [True, False]:
    for q in [True, False]:
        print(f"{p!s:5} {q!s:5}  and={p and q!s:5}  or={p or q!s:5}")''',
'''#md
`and` and `or` *short-circuit*: Python stops as soon as the answer is known. This lets you guard a
risky check behind a safe one:
''',
'''tested = 0
positives = 0
print(tested > 0 and positives / tested > 0.1)     # the division is never attempted''',
'''#md
## Assignment operators

Compound assignment updates a variable in place.

| operator | same as |
|---|---|
| `x += 3` | `x = x + 3` |
| `x -= 3` | `x = x - 3` |
| `x *= 3` | `x = x * 3` |
| `x /= 3` | `x = x / 3` |
| `x //= 3`, `x %= 3`, `x **= 3` | likewise |
''',
'''stock = 100
stock -= 12      # 12 units used
stock += 50      # delivery arrived
stock *= 2       # doubled by a second warehouse
print(stock)''',
'''#md
## Membership operators

`in` and `not in` test whether a value is inside a collection (a string, list, set or dictionary).
''',
'''valid_types = ["Blood", "Urine", "Saliva"]
print("Urine" in valid_types, "Stool" in valid_types, "Stool" not in valid_types)

sequence = "ATGCGTACGTTAG"
print("GTA" in sequence)          # substring test''',
'''#md
## Identity operators

`is` checks whether two names refer to the *same object*; `==` checks whether values are *equal*.
Use `is` mainly to test for `None`.
''',
'''a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b, a is b, a is c)

result = None
print(result is None)''',
'''#md
## Putting it together: a small risk calculation
''',
'''age, sbp, total_chol, smoker = 58, 146, 6.1, False

points = 0
points += 2 if age >= 55 else 0
points += 2 if sbp >= 140 else 0
points += 1 if total_chol > 5.5 else 0
points += 2 if smoker else 0

print(f"risk points: {points} of 7 ({points / 7:.0%})")
print("refer" if points >= 4 else "routine follow-up")''',
],
["[Python tutorial: using Python as a calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)",
 "[Operator precedence table](https://docs.python.org/3/reference/expressions.html#operator-precedence)",
 "[Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)"],
exercises_note="Exercises for this folder are in `exercises/Python_Fundamentals_Exercises.ipynb`.")

lesson(F + "03_Input_and_Output.ipynb", "Input and output",
["display results with print and control separators and line endings",
 "format numbers and text with f-strings",
 "read input from the user with input() and convert it",
 "build a small interactive program"],
"""
Programs communicate by showing output and, sometimes, asking for input. In data analysis most output
is tables and figures, but clear printed messages remain essential for reporting results and checking
that code did what you expected.
""",
[
'''#md
## print()
''',
'''print("Samples processed:", 248)
print("A", "B", "C", sep=" | ")
print("no new line here", end="... ")
print("continued")
print()                        # an empty line
print("line 1\\nline 2")        # \\n inside text starts a new line
print("col1\\tcol2")             # \\t is a tab''',
'''#md
`sep` sets what goes between items (a space by default); `end` sets what goes at the end (a new line by default).

## f-strings: formatted output

Put `f` before the opening quote and write expressions inside `{ }`. After a colon you can give a
*format specification*.

| format | meaning | `{x:...}` with x = 1234.5678 |
|---|---|---|
| `.2f` | 2 decimal places | `1234.57` |
| `,.1f` | thousands separator, 1 decimal | `1,234.6` |
| `.3e` | scientific notation | `1.235e+03` |
| `10.1f` | width 10, right-aligned | `    1234.6` |
| `<10.1f` | width 10, left-aligned | `1234.6    ` |
| `.1%` | percentage (multiplies by 100) | for 0.256: `25.6%` |
''',
'''x = 1234.5678
p = 0.2564
name = "Site A"
print(f"{x:.2f} | {x:,.1f} | {x:.3e} | {x:10.1f}| {x:<10.1f}| {p:.1%}")
print(f"{name:>10}|{name:<10}|{name:^10}|")
print(f"{x = :.1f}")      # the = sign also prints the expression: handy for checking''',
'''#md
Expressions inside the braces are evaluated:
''',
'''weight, height = 74.2, 1.63
print(f"BMI is {weight / height ** 2:.1f} kg/m²")''',
'''#md
### A neat summary table with f-strings
''',
'''rows = [("Blood", 182, 0.214), ("Urine", 140, 0.093), ("Saliva", 58, 0.172)]
print(f"{'Sample':<8}{'n':>6}{'positive':>10}")
print("-" * 24)
for sample, n, pos in rows:
    print(f"{sample:<8}{n:>6}{pos:>10.1%}")''',
'''#md
## input()

`input(prompt)` shows a prompt, waits for the user to type and press Enter, and returns what was typed
**as a string**. Convert it if you need a number.

```python
name = input("What is your name? ")
age = int(input("How old are you? "))
```

`input()` pauses until someone types, so this notebook simulates the answers to let it run on its own.
In your own notebook, replace the fixed answers with the `input(...)` calls shown in the comments.
''',
'''answers = iter(["Amina", "29"])
def fake_input(prompt):            # stands in for input() so the notebook can run without a person
    reply = next(answers)
    print(prompt + reply)
    return reply

name = fake_input("What is your name? ")            # name = input("What is your name? ")
age = int(fake_input("How old are you? "))          # age = int(input("How old are you? "))
print(f"Hello {name}. In ten years you will be {age + 10}.")''',
'''#md
## Handling bad input

Users type unexpected things. Check before converting, or catch the error (module 4).
''',
'''for typed in ["42", "  7 ", "seven", "3.5"]:
    text = typed.strip()
    if text.isdigit():
        print(f"{typed!r:8} -> {int(text)}")
    else:
        print(f"{typed!r:8} -> not a whole number")''',
'''#md
## Example: an interactive calculator

A program that asks for two numbers and an operation, then prints the result. The answers are
simulated here, as above.
''',
'''def calculator(ask):
    a = float(ask("First number: "))
    op = ask("Operation (+ - * /): ").strip()
    b = float(ask("Second number: "))
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        result = a / b
    else:
        return f"Unknown operation {op!r}"
    return f"{a:g} {op} {b:g} = {result:g}"

answers = iter(["12", "/", "5"])
print(calculator(fake_input))
# to use it for real:  print(calculator(input))''',
'''#md
The `:g` format shows a number in the shortest sensible form (`12` rather than `12.0`).
''',
],
["[f-string format specification](https://docs.python.org/3/library/string.html#format-specification-mini-language)",
 "[print()](https://docs.python.org/3/library/functions.html#print) and [input()](https://docs.python.org/3/library/functions.html#input)",
 "[Python tutorial: input and output](https://docs.python.org/3/tutorial/inputoutput.html)"],
exercises_note="Exercises for this folder are in `exercises/Python_Fundamentals_Exercises.ipynb`.")

exercises(F, "Python Fundamentals", "variables, types, operators, input and output",
"Exercises for notebooks 01 to 03 of this folder.",
[
("Create variables for a participant: an ID `\"HC-101\"`, age 45, weight 88.5 kg, height 1.80 m, and whether they smoke (`True`). Print each with its type.",
 '''pid, age, weight, height, smoker = "HC-101", 45, 88.5, 1.80, True
for v in [pid, age, weight, height, smoker]:
    print(repr(v), type(v).__name__)'''),
("Calculate the participant's BMI and print it with one decimal place.",
 '''bmi = weight / height ** 2
print(f"BMI: {bmi:.1f}")''', "27.3."),
("A file stored ages as text: `ages = [\"34\", \"28\", \"51\", \"19\"]`. Convert them to integers and print their sum and mean.",
 '''ages = ["34", "28", "51", "19"]
nums = [int(a) for a in ages]
print(sum(nums), sum(nums) / len(nums))'''),
("Of 1,250 people screened, 87 tested positive. Print the proportion to 4 decimal places and the percentage to 1 decimal place.",
 '''pos, n = 87, 1250
print(f"{pos / n:.4f}  {pos / n:.1%}")''', "0.0696 and 7.0%."),
("Convert 200 minutes into hours and minutes using `//` and `%`.",
 '''print(200 // 60, "h", 200 % 60, "min")'''),
("A haemoglobin result is 10.9 g/dL. Using comparison and logical operators, print whether it is within the range 12.0 to 15.5 and whether it is below 11.0.",
 '''hb = 10.9
print("in range:", 12.0 <= hb <= 15.5)
print("below 11:", hb < 11.0)'''),
("Check whether `\"TATA\"` occurs in the DNA sequence `\"GGCTATAAAAGGCT\"` and whether `\"Plasma\"` is one of `[\"Blood\", \"Urine\", \"Saliva\"]`.",
 '''print("TATA" in "GGCTATAAAAGGCT", "Plasma" in ["Blood", "Urine", "Saliva"])'''),
("Explain why `0.1 * 3 == 0.3` is False, and write a comparison that correctly checks they are equal.",
 '''import math
print(0.1 * 3, math.isclose(0.1 * 3, 0.3))''', "Decimal fractions are stored in binary as approximations, so 0.1 * 3 is 0.30000000000000004. Compare with a tolerance."),
("Print a three-row table of countries and populations (in millions) with names left-aligned in 12 characters and populations right-aligned with one decimal place: Nigeria 223.8, Ethiopia 126.5, Egypt 112.7.",
 '''rows = [("Nigeria", 223.8), ("Ethiopia", 126.5), ("Egypt", 112.7)]
for c, p in rows:
    print(f"{c:<12}{p:>8.1f}")'''),
("Write a temperature converter that asks for a temperature in Celsius (simulate the answer `\"37.5\"`) and prints it in Fahrenheit (F = C × 9/5 + 32).",
 '''typed = "37.5"            # in your notebook: typed = input("Temperature in C: ")
c = float(typed)
print(f"{c} C = {c * 9 / 5 + 32:.1f} F")''', "99.5 F."),
])

# =====================================================================================
# 02 Control flow  (Module 2, topics 2.6 - 2.11)
# =====================================================================================
F = "02_Control_Flow/"

lesson(F + "01_Conditional_Statements.ipynb", "Conditional statements",
["make decisions with if, elif and else",
 "nest conditions and know when to flatten them",
 "write one-line conditional expressions",
 "use pass as a placeholder",
 "classify measurements into categories"],
"""
Most analyses need decisions: is this value in range, which category does a participant fall into,
should a record be flagged? `if` statements run code only when a condition is true.
""",
[
'''#md
## if

The indented block runs only when the condition is `True`.
''',
'''temperature = 38.6
if temperature >= 38.0:
    print("Fever")''',
'''#md
## if ... else
''',
'''glucose = 5.4
if glucose >= 7.0:
    print("Above the diabetes threshold")
else:
    print("Below the threshold")''',
'''#md
## if ... elif ... else

`elif` ("else if") checks further conditions. Python tests them **in order** and runs only the first
block whose condition is true, so order matters.
''',
'''def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

for value in [17.2, 22.0, 25.0, 29.9, 34.1]:
    print(value, bmi_category(value))''',
'''#md
**Why order matters**: a BMI of 22 also satisfies `bmi < 30`, but it never gets there, because
`bmi < 25` was true first. If the conditions were written largest-first with `<`, every value below
30 would be labelled "Overweight".

## Classifying laboratory measurements

Blood pressure categories need two values, so conditions combine with `or`:
''',
'''def bp_category(systolic, diastolic):
    if systolic >= 180 or diastolic >= 120:
        return "Crisis"
    elif systolic >= 140 or diastolic >= 90:
        return "Stage 2 hypertension"
    elif systolic >= 130 or diastolic >= 80:
        return "Stage 1 hypertension"
    elif systolic >= 120:
        return "Elevated"
    else:
        return "Normal"

readings = [(118, 76), (124, 78), (134, 82), (150, 94), (185, 100)]
for s, d in readings:
    print(f"{s}/{d}: {bp_category(s, d)}")''',
'''#md
## Nested conditions

An `if` inside another `if`. Useful when the second question only makes sense after the first.
''',
'''def anaemia(hb, sex):
    if sex == "F":
        if hb < 12.0:
            return "anaemic"
        else:
            return "normal"
    elif sex == "M":
        if hb < 13.0:
            return "anaemic"
        else:
            return "normal"
    else:
        return "sex not recorded"

print(anaemia(11.4, "F"), anaemia(12.6, "M"), anaemia(13.5, "M"), anaemia(12.0, None))''',
'''#md
Deep nesting gets hard to read. The same logic, flattened with a dictionary of thresholds:
''',
'''THRESHOLD = {"F": 12.0, "M": 13.0}

def anaemia_flat(hb, sex):
    if sex not in THRESHOLD:
        return "sex not recorded"
    return "anaemic" if hb < THRESHOLD[sex] else "normal"

print(anaemia_flat(11.4, "F"), anaemia_flat(12.6, "M"), anaemia_flat(12.0, None))''',
'''#md
## Conditional expressions

For a simple two-way choice, a one-line form:  `value_if_true if condition else value_if_false`
''',
'''score = 64
result = "pass" if score >= 50 else "fail"
print(result)''',
'''#md
## Conditions on missing values

Check for `None` before comparing: comparing `None` with a number is an error.
''',
'''def classify_glucose(value):
    if value is None:
        return "not measured"
    if value >= 7.0:
        return "high"
    return "normal"

print([classify_glucose(v) for v in [5.1, None, 8.3]])
try:
    None > 7
except TypeError as e:
    print("TypeError:", e)''',
'''#md
## Truthiness in conditions

Empty values count as false, so `if items:` means "if the list is not empty".
''',
'''flags = []
if not flags:
    print("No flags raised")

notes = "patient fasted"
if notes:
    print("Note:", notes)''',
'''#md
## pass

A block cannot be empty. `pass` does nothing and holds the place while you write the rest of the code.
''',
'''status = "pending"
if status == "pending":
    pass          # handling of pending samples to be written
else:
    print("processed")
print("done")''',
'''#md
## match (Python 3.10+)

`match` compares one value against several patterns. It can be clearer than a long `elif` chain.
''',
'''def describe(code):
    match code:
        case "P":
            return "positive"
        case "N":
            return "negative"
        case "I" | "E":
            return "inconclusive"
        case _:
            return "unknown code"

print([describe(c) for c in ["P", "N", "E", "X"]])''',
],
["[Python tutorial: if statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)",
 "[Conditional expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)",
 "[The match statement](https://docs.python.org/3/tutorial/controlflow.html#match-statements)"],
exercises_note="Exercises for this folder are in `exercises/Control_Flow_Exercises.ipynb`.")

lesson(F + "02_For_Loops.ipynb", "For loops and list comprehensions",
["repeat work over sequences with for loops",
 "generate sequences with range()",
 "loop with enumerate() and zip()",
 "accumulate totals, counts and running values",
 "build lists with list comprehensions"],
"""
A `for` loop repeats a block of code once for every item in a sequence: every patient, every file,
every row. Combined with conditions, loops let you process data of any size with a few lines.
""",
[
'''#md
## Looping over a sequence
''',
'''sample_types = ["Blood", "Urine", "Saliva"]
for s in sample_types:
    print("Processing", s)''',
'''#md
The variable `s` takes each value in turn. Any name works; choose one that reads well.

Strings are sequences of characters:
''',
'''for base in "ATGC":
    print(base, end=" ")''',
'''#md
## range()

`range(stop)`, `range(start, stop)` and `range(start, stop, step)` produce whole numbers.
The stop value is **not** included.
''',
'''print(list(range(5)))
print(list(range(1, 6)))
print(list(range(0, 50, 10)))
print(list(range(10, 0, -2)))''',
'''for dose in range(10, 60, 10):
    print(f"dose {dose} mg")''',
'''#md
## Accumulating results

A common pattern: start with an empty total, update it inside the loop.
''',
'''glucose = [5.4, 7.8, 6.1, 9.2, 5.0, 7.1]

total = 0
high = 0
for g in glucose:
    total += g
    if g >= 7.0:
        high += 1

mean = total / len(glucose)
print(f"mean {mean:.2f}, {high} of {len(glucose)} high ({high / len(glucose):.0%})")''',
'''#md
Finding a maximum by hand shows the logic that `max()` uses:
''',
'''largest = glucose[0]
for g in glucose[1:]:
    if g > largest:
        largest = g
print(largest, max(glucose))''',
'''#md
## enumerate(): position and value together
''',
'''for i, g in enumerate(glucose, start=1):
    flag = " <-- high" if g >= 7.0 else ""
    print(f"reading {i}: {g}{flag}")''',
'''#md
## zip(): several sequences in step
''',
'''ids = ["P01", "P02", "P03"]
weights = [61.0, 82.4, 70.3]
heights = [1.62, 1.80, 1.71]

for pid, w, h in zip(ids, weights, heights):
    print(f"{pid}: BMI {w / h ** 2:.1f}")''',
'''#md
`zip` stops at the shortest sequence. Add `strict=True` to raise an error if the lengths differ, which
catches misaligned data:
''',
'''try:
    list(zip(ids, [61.0, 82.4], strict=True))
except ValueError as e:
    print("ValueError:", e)''',
'''#md
## Generating sequences

Loops can build sequences step by step, for example compound growth or a dilution series:
''',
'''concentration = 100.0
series = []
for step in range(6):
    series.append(concentration)
    concentration /= 2          # two-fold dilution
print(series)

population = 1000
for year in range(1, 6):
    population = round(population * 1.03)
    print(year, population)''',
'''#md
## Nested loops
''',
'''for site in ["Site A", "Site B"]:
    for sample in ["Blood", "Urine"]:
        print(site, sample)''',
'''#md
A multiplication table, building one row at a time:
''',
'''for i in range(1, 5):
    row = ""
    for j in range(1, 5):
        row += f"{i * j:4}"
    print(row)''',
'''#md
## List comprehensions

A compact way to build a list from another sequence:

```python
[expression for item in sequence]
[expression for item in sequence if condition]
```
''',
'''squares = [n ** 2 for n in range(1, 6)]
high = [g for g in glucose if g >= 7.0]
in_mg_dl = [round(g * 18) for g in glucose]          # convert mmol/L to mg/dL
labels = ["high" if g >= 7.0 else "normal" for g in glucose]
print(squares, high, in_mg_dl, labels, sep="\\n")''',
'''#md
The equivalent loop for `high`, to show what the comprehension does:
''',
'''high_loop = []
for g in glucose:
    if g >= 7.0:
        high_loop.append(g)
print(high_loop == high)''',
'''#md
Comprehensions also build dictionaries and sets (module 3):
''',
'''bmi = {pid: round(w / h ** 2, 1) for pid, w, h in zip(ids, weights, heights)}
unique_lengths = {len(s) for s in sample_types}
print(bmi, unique_lengths)''',
'''#md
Keep comprehensions short. If one needs a second line of thought, a normal loop is clearer.

## Built-ins that replace loops

Python's built-in functions often do in one call what would otherwise need a loop:
''',
'''print(sum(glucose), min(glucose), max(glucose), len(glucose))
print(sorted(glucose), any(g > 9 for g in glucose), all(g > 4 for g in glucose))''',
],
["[Python tutorial: for statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)",
 "[range()](https://docs.python.org/3/library/stdtypes.html#range)",
 "[List comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)"],
exercises_note="Exercises for this folder are in `exercises/Control_Flow_Exercises.ipynb`.")

lesson(F + "03_While_Loops.ipynb", "While loops and loop control",
["repeat code while a condition holds",
 "avoid infinite loops",
 "control loops with break, continue and pass",
 "use the for ... else pattern for searches"],
"""
A `while` loop repeats as long as its condition stays true. It suits situations where you do not know
in advance how many repetitions are needed: until a target is reached, until valid input arrives,
until a search succeeds.
""",
[
'''#md
## while
''',
'''count = 1
while count <= 5:
    print("count is", count)
    count += 1''',
'''#md
The condition is checked **before** each repetition. Something inside the loop must eventually make it
false, otherwise the loop never ends (an *infinite loop*). In Jupyter, stop one with **Kernel > Interrupt**.

## Repeating until a target is reached
''',
'''balance = 1000.0
years = 0
while balance < 2000:
    balance *= 1.07         # 7% growth per year
    years += 1
print(f"Doubles after {years} years ({balance:.2f})")''',
'''bacteria = 100
minutes = 0
while bacteria < 1_000_000:
    bacteria *= 2           # doubles every 20 minutes
    minutes += 20
print(f"{bacteria:,} cells after {minutes} minutes ({minutes / 60:.1f} hours)")''',
'''#md
## Halving until below a limit

A drug concentration halves every half-life. How long until it drops below a threshold?
''',
'''concentration = 80.0      # mg/L
half_life_h = 6
hours = 0
while concentration >= 5:
    concentration /= 2
    hours += half_life_h
print(f"below 5 mg/L after {hours} hours ({concentration:.2f} mg/L)")''',
'''#md
## break: leave the loop early
''',
'''readings = [5.2, 6.1, 4.9, 11.3, 5.5, 6.0]
for i, r in enumerate(readings):
    if r > 10:
        print(f"Critical value {r} at position {i}: stopping")
        break
    print("ok", r)''',
'''#md
## continue: skip to the next item
''',
'''raw = ["12.1", "", "9.8", "n/a", "14.0"]
values = []
for item in raw:
    if not item.replace(".", "", 1).isdigit():
        continue            # skip anything that is not a number
    values.append(float(item))
print(values)''',
'''#md
## pass: do nothing

`pass` is a placeholder where Python needs a statement but you have nothing to do yet. Unlike
`continue`, it does not skip the rest of the loop body.
''',
'''for code in ["A", "B", "C"]:
    if code == "B":
        pass                 # nothing special for B, yet
    print("handled", code)''',
'''#md
## for ... else: searching

A loop's `else` block runs only if the loop finished **without** `break`. It expresses
"search, and report if nothing was found" neatly.
''',
'''def find_first_positive(results):
    for i, r in enumerate(results):
        if r == "Positive":
            print("first positive at index", i)
            break
    else:
        print("no positives")

find_first_positive(["Negative", "Negative", "Positive", "Negative"])
find_first_positive(["Negative", "Negative"])''',
'''#md
## Input validation with while

Ask again until the input is valid. The answers are simulated here; in your own notebook use `input()`.
''',
'''typed_answers = iter(["abc", "-5", "42"])

while True:
    typed = next(typed_answers)          # typed = input("Enter age: ")
    print("entered:", typed)
    if typed.isdigit() and 0 < int(typed) < 120:
        age = int(typed)
        break
    print("  please enter a whole number between 1 and 119")
print("Age accepted:", age)''',
'''#md
`while True` with a `break` inside is the usual way to write "repeat until done".

## for or while?

| use | when |
|---|---|
| `for` | you are going through a known collection or a fixed number of steps |
| `while` | you repeat until a condition changes and do not know how many times |
''',
],
["[Python tutorial: break, continue and else on loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)",
 "[The while statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)",
 "[pass statements](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)"],
exercises_note="Exercises for this folder are in `exercises/Control_Flow_Exercises.ipynb`.")

exercises(F, "Control Flow", "decisions and loops",
"Exercises for notebooks 01 to 03 of this folder.",
[
("Write a function `glucose_status(g)` that returns `\"low\"` below 3.9, `\"normal\"` from 3.9 up to 5.5, `\"prediabetes\"` from 5.6 up to 6.9, and `\"diabetes\"` at 7.0 or above. Test it on `[3.5, 5.0, 6.2, 7.0, 11.4]`.",
 '''def glucose_status(g):
    if g < 3.9:
        return "low"
    elif g <= 5.5:
        return "normal"
    elif g < 7.0:
        return "prediabetes"
    return "diabetes"

print([glucose_status(g) for g in [3.5, 5.0, 6.2, 7.0, 11.4]])'''),
("Given `temps = [36.8, 38.2, 37.1, 39.0, 36.5, 38.0]`, count how many are fevers (38.0 or above) and print the percentage.",
 '''temps = [36.8, 38.2, 37.1, 39.0, 36.5, 38.0]
fevers = sum(1 for t in temps if t >= 38.0)
print(fevers, f"{fevers / len(temps):.0%}")''', "3 of 6, 50%."),
("Using `range`, print the even numbers from 2 to 20 and the multiples of 7 below 100.",
 '''print(list(range(2, 21, 2)))
print(list(range(7, 100, 7)))'''),
("Write a loop that prints a ten-fold dilution series starting at 1000 units until the value drops below 0.01.",
 '''c = 1000.0
while c >= 0.01:
    print(c)
    c /= 10'''),
("Given `ids = [\"A1\", \"A2\", \"A3\"]` and `scores = [67, 45, 88]`, use `zip` to print each ID with `pass` or `fail` (pass is 50 or more).",
 '''ids = ["A1", "A2", "A3"]; scores = [67, 45, 88]
for i, s in zip(ids, scores):
    print(i, "pass" if s >= 50 else "fail")'''),
("Use a list comprehension to convert `[5.4, 7.8, 6.1]` from mmol/L to mg/dL (multiply by 18.0), and another to keep only values above 6.",
 '''g = [5.4, 7.8, 6.1]
print([round(x * 18.0, 1) for x in g], [x for x in g if x > 6])'''),
("Find the first value above 100 in `[12, 45, 88, 130, 7, 150]` with a loop and `break`, and print its position. Use `for ... else` to print a message if there is none.",
 '''for i, v in enumerate([12, 45, 88, 130, 7, 150]):
    if v > 100:
        print("found", v, "at", i)
        break
else:
    print("none above 100")'''),
("Clean the list `[\"7.2\", \"\", \"6.8\", \"error\", \"5.9\"]` into floats, skipping anything that is not a number, using `continue`.",
 '''clean = []
for x in ["7.2", "", "6.8", "error", "5.9"]:
    try:
        clean.append(float(x))
    except ValueError:
        continue
print(clean)'''),
("A population of 5,000 grows by 2.5% a year. With a `while` loop, find how many years until it exceeds 10,000.",
 '''pop, years = 5000, 0
while pop <= 10000:
    pop *= 1.025
    years += 1
print(years, round(pop))''', "29 years."),
("Print a 5 x 5 multiplication table using nested loops, with each number right-aligned in 4 characters.",
 '''for i in range(1, 6):
    print("".join(f"{i * j:4}" for j in range(1, 6)))'''),
])
print("modules 00-02 written")
