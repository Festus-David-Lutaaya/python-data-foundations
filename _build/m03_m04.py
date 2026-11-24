from nb import lesson, exercises

# =====================================================================================
# 03 Data structures  (Module 3)
# =====================================================================================
F = "03_Data_Structures/"

lesson(F + "01_Strings.ipynb", "Strings",
["create strings and use escape characters",
 "index and slice strings",
 "clean and transform text with string methods",
 "split text into parts and join parts into text",
 "work with DNA sequences and identifier codes as strings"],
"""
Strings hold text: names, codes, categories, free-text comments, and sequences such as DNA. A large
share of data cleaning is string work: removing stray spaces, fixing capitalisation, splitting codes
into parts.
""",
[
'''#md
## Creating strings

Single and double quotes are the same. Triple quotes allow text over several lines.
''',
'''site = "Site A"
note = 'sample stored at 4 C'
quote = "the participant said 'no change'"
report = """Line one of the report.
Line two of the report."""
print(site, note, quote, report, sep="\\n")''',
'''#md
Escape characters start with a backslash: `\\n` new line, `\\t` tab, `\\\\` a backslash, `\\'` a quote.
A *raw string* `r"..."` keeps backslashes as typed, which is useful for Windows file paths.
''',
'''print("name\\tage\\nAmina\\t29")
print(r"C:\\data\\new_results.csv")''',
'''#md
## Indexing

Each character has a position, starting at **0**. Negative positions count from the end.

```
 sequence:  A  T  G  C  G  T
 index:     0  1  2  3  4  5
 negative: -6 -5 -4 -3 -2 -1
```
''',
'''sequence = "ATGCGT"
print(sequence[0], sequence[3], sequence[-1], len(sequence))''',
'''#md
## Slicing

`text[start:stop]` takes characters from `start` up to but **not including** `stop`.
Leaving out `start` means "from the beginning"; leaving out `stop` means "to the end".
A third number is the step.
''',
'''code = "LAB-2025-000731"
print(code[:3])       # first three characters
print(code[4:8])      # the year
print(code[-6:])      # last six characters
print(code[::2])      # every second character
print(code[::-1])     # reversed''',
'''#md
Strings cannot be changed in place (they are *immutable*). Methods and slices always create new strings.
''',
'''try:
    sequence[0] = "G"
except TypeError as e:
    print("TypeError:", e)
mutated = "G" + sequence[1:]
print(mutated)''',
'''#md
## Common string methods

| method | does |
|---|---|
| `upper()`, `lower()`, `title()`, `capitalize()` | change case |
| `strip()`, `lstrip()`, `rstrip()` | remove spaces (or given characters) at the ends |
| `replace(old, new)` | substitute text |
| `split(sep)` | break into a list |
| `join(list)` | glue a list into text |
| `startswith()`, `endswith()` | test the beginning or end |
| `find()`, `count()` | position and number of a substring |
| `isdigit()`, `isalpha()`, `isspace()` | test what the characters are |
| `zfill(n)` | pad with leading zeros |
''',
'''raw = "   blood SAMPLE  "
print(repr(raw.strip()))
print(raw.strip().upper(), "|", raw.strip().lower(), "|", raw.strip().title(), "|", raw.strip().capitalize())
print("E. coli".replace("E.", "Escherichia"))
print("--x--".strip("-"), "0042".lstrip("0"), "7".zfill(3))''',
'''#md
## Cleaning inconsistent categories

Data entry often gives the same category several spellings. Chaining methods makes them consistent:
''',
'''entries = ["Blood", "blood ", " BLOOD", "Urine", "urine", "Saliva "]
cleaned = [e.strip().capitalize() for e in entries]
print(cleaned)
print(sorted(set(cleaned)))''',
'''#md
## split and join
''',
'''record = "P0042,F,34,Site B"
fields = record.split(",")
print(fields, fields[2])

print("2025-03-14".split("-"))
print("a  b   c".split())                  # no argument: split on any run of spaces
print("key=value=extra".split("=", 1))     # split only at the first =
print("-".join(["LAB", "2025", "000731"]))''',
'''#md
## Searching
''',
'''dna = "ATGCGATACGCTTGAATGCCGTA"
print(dna.find("GAT"), dna.find("XYZ"))    # -1 means not found
print(dna.count("A"), dna.count("ATG"))
print(dna.startswith("ATG"), dna.endswith("TAA"))
print("ATG" in dna)''',
'''#md
## Working with DNA sequences

A few classic sequence tasks show how much can be done with basic string tools.

**GC content** (the share of G and C bases):
''',
'''gc = (dna.count("G") + dna.count("C")) / len(dna)
print(f"length {len(dna)}, GC content {gc:.1%}")''',
'''#md
**Complement and reverse complement**: `str.maketrans` builds a translation table, and `translate` applies it.
''',
'''table = str.maketrans("ATGC", "TACG")
complement = dna.translate(table)
reverse_complement = complement[::-1]
print(dna)
print(complement)
print(reverse_complement)''',
'''#md
**Codons**: splitting a sequence into groups of three with a slice inside a comprehension.
''',
'''codons = [dna[i:i + 3] for i in range(0, len(dna) - 2, 3)]
print(codons)
stop = {"TAA", "TAG", "TGA"}
print([i for i, c in enumerate(codons) if c in stop])''',
'''#md
Reading sequences from a file (tab-separated: name, sequence):
''',
'''with open("../datasets/raw/sequences.txt") as fh:
    for line in fh:
        name, seq = line.strip().split("\\t")
        gc = (seq.count("G") + seq.count("C")) / len(seq)
        print(f"{name}: {len(seq):3} bases, GC {gc:.0%}")''',
'''#md
## Formatting text with f-strings

Covered in detail in `01_Python_Fundamentals/03_Input_and_Output`. A reminder:
''',
'''name, n, rate = "Site B", 182, 0.2143
print(f"{name}: {n} samples, positivity {rate:.1%}")''',
'''#md
## Checking characters
''',
'''for t in ["123", "12.5", "abc", "abc123", "  "]:
    print(repr(t).ljust(8), "digit:", t.isdigit(), " alpha:", t.isalpha(), " alnum:", t.isalnum(), " space:", t.isspace())''',
'''#md
`"12.5".isdigit()` is False because of the dot. To test whether text is a number, try converting it
(module 4, error handling).
''',
],
["[String methods](https://docs.python.org/3/library/stdtypes.html#string-methods)",
 "[Python tutorial: text](https://docs.python.org/3/tutorial/introduction.html#text)",
 "[Regular expressions HOWTO](https://docs.python.org/3/howto/regex.html), for pattern matching beyond simple methods"],
exercises_note="Exercises for this folder are in `exercises/Data_Structures_Exercises.ipynb`.")

lesson(F + "02_Lists.ipynb", "Lists",
["create lists and access items by position",
 "add, remove and change items",
 "sort lists, including by a key",
 "copy lists correctly",
 "compute simple statistics from a list"],
"""
A list is an ordered collection of items. It can grow and shrink, and its items can be changed.
Lists are the general-purpose container in Python: a list of test results, of file names, of patient IDs.
""",
[
'''#md
## Creating lists
''',
'''results = [5.4, 7.8, 6.1, 9.2, 5.0]
sample_ids = ["S01", "S02", "S03"]
empty = []
mixed = ["P01", 34, 61.5, True]          # allowed, but a dictionary or table usually fits mixed data better
numbers = list(range(1, 6))
print(results, sample_ids, empty, mixed, numbers, sep="\\n")''',
'''#md
## Indexing and slicing

Exactly as with strings: positions start at 0, negative positions count from the end, slices exclude
the stop position.
''',
'''print(results[0], results[-1], results[1:4], results[:2], results[::-1])
print(len(results))''',
'''#md
## Changing items

Lists are *mutable*: you can change them in place.
''',
'''results[2] = 6.3
print(results)''',
'''#md
## List methods

| method | effect |
|---|---|
| `append(x)` | add x at the end |
| `extend(other)` | add every item from another list |
| `insert(i, x)` | add x at position i |
| `remove(x)` | delete the first x |
| `pop(i)` | delete and return the item at i (default: the last) |
| `index(x)` | position of the first x |
| `count(x)` | how many times x appears |
| `sort()` | sort in place |
| `reverse()` | reverse in place |
| `clear()` | remove everything |
''',
'''tests = ["Hb", "WBC"]
tests.append("Platelets")
tests.extend(["ALT", "AST"])
tests.insert(0, "Glucose")
print(tests)

tests.remove("AST")
last = tests.pop()
first = tests.pop(0)
print(tests, "| removed:", last, first)
print(tests.index("WBC"), tests.count("Hb"))''',
'''#md
## Sorting

`sorted(list)` returns a **new** sorted list; `list.sort()` sorts the list **in place** and returns `None`.
''',
'''values = [7.8, 5.4, 9.2, 5.0, 6.3]
print(sorted(values), sorted(values, reverse=True))
print(values)                  # unchanged
values.sort()
print(values)                  # now sorted

result = values.sort()
print(result)                  # None: a common mistake is  values = values.sort()''',
'''#md
`key=` gives a function that decides the sort value. Here, sorting text without regard to case, and
sorting records by their second item:
''',
'''names = ["banana", "Apple", "cherry"]
print(sorted(names), sorted(names, key=str.lower))

participants = [("P03", 52), ("P01", 34), ("P02", 47)]
print(sorted(participants, key=lambda p: p[1]))     # by age; lambda is covered in module 4''',
'''#md
## Membership, counting and simple statistics
''',
'''glucose = [5.4, 7.8, 6.1, 9.2, 5.0, 7.1]
print(7.8 in glucose, len(glucose), sum(glucose), min(glucose), max(glucose))

mean = sum(glucose) / len(glucose)
ordered = sorted(glucose)
n = len(ordered)
median = (ordered[n // 2 - 1] + ordered[n // 2]) / 2 if n % 2 == 0 else ordered[n // 2]
print(f"mean {mean:.2f}, median {median:.2f}, range {max(glucose) - min(glucose):.1f}")''',
'''import statistics
print(statistics.mean(glucose), statistics.median(glucose), round(statistics.stdev(glucose), 3))''',
'''#md
## Copying lists

`b = a` does **not** copy a list: both names point to the same list, so changing one changes "both".
''',
'''a = [1, 2, 3]
b = a
b.append(4)
print(a)          # a changed too

c = a.copy()      # a real copy; list(a) and a[:] also work
c.append(5)
print(a, c)''',
'''#md
Lists inside lists need `copy.deepcopy` to copy fully:
''',
'''import copy
grid = [[0, 0], [0, 0]]
shallow = grid.copy()
deep = copy.deepcopy(grid)
grid[0][0] = 99
print(shallow, deep)''',
'''#md
## Lists of lists

A simple way to hold a small table. For real tables, pandas (module 6) is far better.
''',
'''table = [
    ["P01", "F", 34, 5.4],
    ["P02", "M", 51, 7.8],
    ["P03", "F", 47, 6.1],
]
for pid, sex, age, glu in table:
    print(f"{pid} {sex} {age:>3} {glu:>5}")
print("mean age:", sum(row[2] for row in table) / len(table))''',
'''#md
## Unpacking
''',
'''first, *middle, last = [10, 20, 30, 40, 50]
print(first, middle, last)''',
],
["[Python tutorial: lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)",
 "[Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)",
 "[statistics module](https://docs.python.org/3/library/statistics.html)"],
exercises_note="Exercises for this folder are in `exercises/Data_Structures_Exercises.ipynb`.")

lesson(F + "03_Tuples_and_Sets.ipynb", "Tuples and sets",
["create and unpack tuples, and know when to use them instead of lists",
 "use named tuples for readable records",
 "remove duplicates and test membership with sets",
 "compare collections with union, intersection and difference"],
"""
Tuples are ordered collections that cannot be changed. Sets are unordered collections of unique items.
Each fits particular jobs: tuples for fixed records, sets for "which items are unique, shared or missing".
""",
[
'''#md
## Tuples

Created with round brackets (or just commas). Once made, they cannot be changed.
''',
'''location = (0.3476, 32.5825)            # latitude, longitude
reading = ("P01", "2025-03-14", 7.8)
single = (5,)                           # a one-item tuple needs a trailing comma
print(location[0], reading[-1], len(reading), type(single))

try:
    location[0] = 1.0
except TypeError as e:
    print("TypeError:", e)''',
'''#md
### Why use a tuple?

- the data is a fixed record (coordinates, a date split into parts, a row from a database)
- it signals that the values should not change
- tuples can be dictionary keys and set members; lists cannot
''',
'''distances = {("Site A", "Site B"): 42, ("Site A", "Site C"): 17}
print(distances[("Site A", "Site C")])''',
'''#md
### Unpacking

Assigning a tuple to several names at once. Functions often return tuples this way.
''',
'''lat, lon = location
print(lat, lon)

def min_max(values):
    return min(values), max(values)

low, high = min_max([5.4, 7.8, 6.1, 9.2])
print(low, high)''',
'''#md
### Named tuples

Tuples whose positions also have names, so `r.glucose` reads better than `r[2]`.
''',
'''from collections import namedtuple

Reading = namedtuple("Reading", ["patient", "date", "glucose"])
r = Reading("P01", "2025-03-14", 7.8)
print(r.patient, r.glucose, r)''',
'''#md
## Sets

Created with curly brackets or `set()`. Duplicates are removed automatically and there is no order.
''',
'''ids = ["S01", "S02", "S01", "S03", "S02"]
unique_ids = set(ids)
print(unique_ids, len(ids), "entries,", len(unique_ids), "unique")

empty = set()                # {} makes an empty dictionary, not a set
print(type(empty), type({}))''',
'''#md
Membership tests on sets are very fast, even with millions of items, which makes them good for
"have we seen this ID?" checks.
''',
'''seen = set()
for sid in ["S01", "S02", "S01", "S04", "S02"]:
    if sid in seen:
        print("duplicate:", sid)
    seen.add(sid)
print(seen)''',
'''#md
### Set operations

| operation | operator | method | meaning |
|---|---|---|---|
| union | `a \\| b` | `a.union(b)` | in either |
| intersection | `a & b` | `a.intersection(b)` | in both |
| difference | `a - b` | `a.difference(b)` | in a but not b |
| symmetric difference | `a ^ b` | `a.symmetric_difference(b)` | in one but not both |
''',
'''enrolled = {"P01", "P02", "P03", "P04", "P05"}
sampled = {"P02", "P03", "P05", "P07"}

print("enrolled and sampled:  ", sorted(enrolled & sampled))
print("enrolled, not sampled: ", sorted(enrolled - sampled))
print("sampled, not enrolled: ", sorted(sampled - enrolled))    # a data problem to check
print("anyone:                ", sorted(enrolled | sampled))
print("in exactly one list:   ", sorted(enrolled ^ sampled))''',
'''#md
Subsets and changing sets:
''',
'''required = {"Hb", "WBC"}
done = {"Hb", "WBC", "Platelets"}
print(required.issubset(done), required <= done, {"ALT"}.isdisjoint(done))

done.add("ALT")
done.discard("Platelets")        # discard does nothing if the item is absent; remove() would raise an error
print(done)''',
'''#md
### Unique values in sequences

Sets of characters show the "alphabet" of a sequence:
''',
'''print(set("ATGCGATACGNNTTGA"))''',
'''#md
The `N` reveals unknown bases in the sequence, which may need handling.

To remove duplicates while **keeping the original order**, use a dictionary instead of a set:
''',
'''visits = ["Site B", "Site A", "Site B", "Site C", "Site A"]
print(list(dict.fromkeys(visits)))''',
'''#md
## Which collection?

| need | use |
|---|---|
| ordered, changeable sequence | list |
| fixed record, or a dictionary key | tuple |
| unique items, fast membership, comparing groups | set |
| look up values by a key | dictionary (next notebook) |
''',
],
["[Python tutorial: tuples and sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)",
 "[Python tutorial: sets](https://docs.python.org/3/tutorial/datastructures.html#sets)",
 "[collections.namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)"],
exercises_note="Exercises for this folder are in `exercises/Data_Structures_Exercises.ipynb`.")

lesson(F + "04_Dictionaries.ipynb", "Dictionaries and nested data",
["create dictionaries and look up values by key",
 "add, change and remove entries safely",
 "loop over keys, values and items",
 "count and group with dictionaries",
 "work with nested structures: lists in dictionaries and dictionaries in lists"],
"""
A dictionary maps **keys** to **values**: a patient ID to a record, a code to a label, a test name to a
result. Looking up by key is fast and readable. Nested dictionaries and lists are also the shape of most
data that comes from web services and JSON files.
""",
[
'''#md
## Creating and reading a dictionary
''',
'''patient = {
    "id": "P0042",
    "age": 34,
    "sex": "F",
    "site": "Site B",
}
print(patient["age"])
print(patient)''',
'''#md
A missing key raises `KeyError`. `get` returns `None` (or a default you choose) instead:
''',
'''try:
    patient["weight"]
except KeyError as e:
    print("KeyError:", e)
print(patient.get("weight"), patient.get("weight", "not recorded"))
print("age" in patient, "weight" in patient)''',
'''#md
Keys must be immutable (strings, numbers, tuples). Values can be anything, including lists and other
dictionaries. Since Python 3.7 dictionaries keep the order in which keys were added.

## Adding, changing and removing
''',
'''patient["weight_kg"] = 61.5          # add
patient["age"] = 35                  # change
patient.update({"smoker": False, "site": "Site A"})
print(patient)

removed = patient.pop("smoker")      # remove and return the value
del patient["site"]
print(removed, patient)''',
'''#md
## Looping
''',
'''for key in patient:
    print(key)

for key, value in patient.items():
    print(f"{key:>10}: {value}")

print(list(patient.keys()), list(patient.values()))''',
'''#md
## Dictionaries as look-up tables

Translating codes into labels, or messy spellings into clean ones:
''',
'''labels = {"P": "Positive", "N": "Negative", "I": "Inconclusive"}
codes = ["P", "N", "N", "I", "X", "P"]
print([labels.get(c, "Unknown") for c in codes])

unit_factor = {"mmol/L": 1.0, "mg/dL": 1 / 18}
readings = [(5.6, "mmol/L"), (126, "mg/dL"), (7.1, "mmol/L")]
print([round(v * unit_factor[u], 1) for v, u in readings])''',
'''#md
## Counting

Counting how often each value occurs is one of the most common tasks.
''',
'''results = ["Neg", "Pos", "Neg", "Neg", "Pos", "Inc", "Neg"]
counts = {}
for r in results:
    counts[r] = counts.get(r, 0) + 1
print(counts)

from collections import Counter
c = Counter(results)
print(c, c.most_common(1))''',
'''#md
## Grouping

Collecting values into lists by a key:
''',
'''samples = [("Site A", 5.4), ("Site B", 7.8), ("Site A", 6.1), ("Site C", 9.2), ("Site B", 5.0)]

by_site = {}
for site, value in samples:
    by_site.setdefault(site, []).append(value)
print(by_site)
print({site: round(sum(v) / len(v), 2) for site, v in by_site.items()})''',
'''#md
`setdefault(key, [])` returns the list for that key, creating an empty one the first time.
`collections.defaultdict(list)` does the same automatically.

## Dictionary comprehensions
''',
'''squares = {n: n ** 2 for n in range(1, 6)}
high_only = {pid: g for pid, g in {"P1": 5.4, "P2": 7.8, "P3": 9.2}.items() if g >= 7}
print(squares, high_only)''',
'''#md
## Sorting a dictionary by its values
''',
'''positivity = {"Site A": 0.12, "Site B": 0.31, "Site C": 0.08}
for site in sorted(positivity, key=positivity.get, reverse=True):
    print(site, positivity[site])''',
'''#md
## Nested data structures

### A dictionary containing lists and dictionaries
''',
'''record = {
    "id": "P0042",
    "demographics": {"age": 34, "sex": "F"},
    "visits": [
        {"date": "2025-01-10", "glucose": 7.8, "flags": ["fasting"]},
        {"date": "2025-02-09", "glucose": 6.9, "flags": []},
        {"date": "2025-03-11", "glucose": 6.2, "flags": ["repeat"]},
    ],
}
print(record["demographics"]["age"])
print(record["visits"][0]["glucose"])
print([v["glucose"] for v in record["visits"]])
print(record["visits"][-1]["flags"][0])''',
'''#md
Read a path like `record["visits"][0]["glucose"]` from left to right: the record, its visits list,
the first visit, its glucose value.

### A list of dictionaries: one per record

This is the most common shape for data before it becomes a table.
''',
'''participants = [
    {"id": "P01", "age": 34, "site": "Site A", "glucose": 5.4},
    {"id": "P02", "age": 51, "site": "Site B", "glucose": 7.8},
    {"id": "P03", "age": 47, "site": "Site A", "glucose": 6.1},
    {"id": "P04", "age": 62, "site": "Site C"},                 # glucose missing
]
ages = [p["age"] for p in participants]
high = [p["id"] for p in participants if p.get("glucose", 0) >= 7]
print(ages, high)

site_a = [p for p in participants if p["site"] == "Site A"]
print(len(site_a), "participants at Site A")''',
'''#md
### Extracting safely from nested data

Real nested data often has missing pieces. A small helper avoids long chains of `if` checks:
''',
'''def get_path(data, path, default=None):
    for step in path:
        try:
            data = data[step]
        except (KeyError, IndexError, TypeError):
            return default
    return data

print(get_path(record, ["visits", 2, "flags", 0]))
print(get_path(record, ["visits", 5, "glucose"], "no such visit"))
print(get_path(record, ["demographics", "weight"], "not recorded"))''',
'''#md
### From nested data to a table

pandas turns a list of dictionaries straight into a table (module 6):
''',
'''import pandas as pd
pd.DataFrame(participants)''',
'''#md
## JSON

JSON, the standard format for web data, maps directly onto dictionaries and lists.
''',
'''import json
text = json.dumps(record, indent=2)
print(text[:200])
back = json.loads(text)
print(back["visits"][1]["glucose"])''',
],
["[Python tutorial: dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)",
 "[collections: Counter, defaultdict](https://docs.python.org/3/library/collections.html)",
 "[json module](https://docs.python.org/3/library/json.html)"],
exercises_note="Exercises for this folder are in `exercises/Data_Structures_Exercises.ipynb`.")

exercises(F, "Data Structures", "strings, lists, tuples, sets and dictionaries",
"Exercises for notebooks 01 to 04 of this folder.",
[
("For the sequence `\"ATGCGCGATTACAGGCTTAA\"`, print its length, GC content as a percentage, and its reverse complement.",
 '''s = "ATGCGCGATTACAGGCTTAA"
gc = (s.count("G") + s.count("C")) / len(s)
rc = s.translate(str.maketrans("ATGC", "TACG"))[::-1]
print(len(s), f"{gc:.0%}", rc)''', "20 bases, 45% GC."),
("Clean `[\" urine\", \"URINE\", \"Blood \", \"blood\", \"Saliva\"]` so that each entry has no spaces and only a capital first letter, then print the unique categories in alphabetical order.",
 '''raw = [" urine", "URINE", "Blood ", "blood", "Saliva"]
clean = [r.strip().capitalize() for r in raw]
print(sorted(set(clean)))'''),
("Split the code `\"LAB-KLA-2025-0042\"` into its parts and print the site (`KLA`) and the number as an integer.",
 '''parts = "LAB-KLA-2025-0042".split("-")
print(parts[1], int(parts[3]))'''),
("Create a list of test results `[12.1, 10.4, 13.8, 9.7, 11.2]`. Add `14.0`, remove `9.7`, sort the list, and print the mean, median and range.",
 '''r = [12.1, 10.4, 13.8, 9.7, 11.2]
r.append(14.0); r.remove(9.7); r.sort()
import statistics as st
print(r, round(st.mean(r), 2), st.median(r), round(max(r) - min(r), 1))'''),
("Explain the output of this code, then change it so `a` is not affected:\n\n```python\na = [1, 2]\nb = a\nb.append(3)\nprint(a)\n```",
 '''a = [1, 2]
b = a.copy()
b.append(3)
print(a, b)''', "`b = a` makes both names point to the same list, so appending through `b` changes `a`. `a.copy()` makes a separate list."),
("Two lists of sample IDs come from the freezer and the database: `freezer = [\"S1\", \"S2\", \"S3\", \"S5\"]`, `database = [\"S2\", \"S3\", \"S4\", \"S5\", \"S6\"]`. Print the IDs in both, only in the freezer, and only in the database.",
 '''freezer = {"S1", "S2", "S3", "S5"}; database = {"S2", "S3", "S4", "S5", "S6"}
print(sorted(freezer & database), sorted(freezer - database), sorted(database - freezer))'''),
("Store a patient as a dictionary with keys id, age, sex and tests, where tests is a dictionary `{\"Hb\": 11.2, \"WBC\": 6.4}`. Print the haemoglobin value, add a platelet count of 250, and print all tests.",
 '''patient = {"id": "P07", "age": 41, "sex": "M", "tests": {"Hb": 11.2, "WBC": 6.4}}
print(patient["tests"]["Hb"])
patient["tests"]["Platelets"] = 250
print(patient["tests"])'''),
("Count each result in `[\"Pos\", \"Neg\", \"Neg\", \"Pos\", \"Neg\", \"Inc\"]` with a dictionary, without using Counter.",
 '''counts = {}
for r in ["Pos", "Neg", "Neg", "Pos", "Neg", "Inc"]:
    counts[r] = counts.get(r, 0) + 1
print(counts)'''),
("From the list of dictionaries below, print the IDs of participants older than 40 and the mean glucose of those with a glucose value.\n\n```python\npeople = [{\"id\": \"A\", \"age\": 34, \"glucose\": 5.4}, {\"id\": \"B\", \"age\": 51, \"glucose\": 7.8},\n          {\"id\": \"C\", \"age\": 47}, {\"id\": \"D\", \"age\": 62, \"glucose\": 6.6}]\n```",
 '''people = [{"id": "A", "age": 34, "glucose": 5.4}, {"id": "B", "age": 51, "glucose": 7.8},
          {"id": "C", "age": 47}, {"id": "D", "age": 62, "glucose": 6.6}]
print([p["id"] for p in people if p["age"] > 40])
g = [p["glucose"] for p in people if "glucose" in p]
print(round(sum(g) / len(g), 2))''', "B, C, D; mean glucose 6.6."),
("Group these readings by site into a dictionary of lists, then print the mean for each site: `[(\"North\", 4), (\"South\", 7), (\"North\", 6), (\"South\", 9), (\"East\", 5)]`.",
 '''groups = {}
for site, v in [("North", 4), ("South", 7), ("North", 6), ("South", 9), ("East", 5)]:
    groups.setdefault(site, []).append(v)
print({s: sum(v) / len(v) for s, v in groups.items()})'''),
])

# =====================================================================================
# 04 Functions and modules  (Module 4)
# =====================================================================================
F = "04_Functions_and_Modules/"

lesson(F + "01_Functions.ipynb", "Functions",
["explain why functions matter for analysis code",
 "define functions with parameters and return values",
 "use positional, keyword and default arguments",
 "understand local and global scope",
 "use the most important built-in functions",
 "document functions with docstrings"],
"""
A function is a named, reusable piece of code. Instead of copying the same calculation into ten places,
you write it once, give it a clear name, test it, and call it wherever it is needed. Functions make
analyses shorter, easier to read, and much easier to correct.
""",
[
'''#md
## Why functions?

- **reuse**: write a BMI calculation once and use it everywhere
- **readability**: `classify_bp(sbp, dbp)` says what it does; twelve lines of conditions do not
- **one place to fix**: correct a mistake once, and every use is corrected
- **testing**: a function can be checked on known inputs

## Defining and calling a function
''',
'''def greet():
    print("Hello from a function")

greet()
greet()''',
'''#md
`def` starts the definition, then the name, brackets and a colon. The indented block is the *body*.
Nothing runs until the function is **called** with `greet()`.

## Parameters and return values

Parameters are the inputs. `return` sends a result back to whoever called the function.
''',
'''def bmi(weight_kg, height_m):
    """Body mass index: weight in kg divided by height in metres squared."""
    return weight_kg / height_m ** 2

value = bmi(70, 1.75)
print(round(value, 1))
print(round(bmi(55, 1.60), 1))''',
'''#md
`print` shows a value; `return` hands it back so it can be stored and used again. A function without
`return` gives back `None`:
''',
'''def show_bmi(w, h):
    print(round(w / h ** 2, 1))

result = show_bmi(70, 1.75)
print("returned:", result)''',
'''#md
## Docstrings

The text in triple quotes right after `def` documents the function. `help()` displays it.
''',
'''def mean_median_range(values):
    """Return the mean, median and range of a list of numbers.

    Parameters
    ----------
    values : list of numbers

    Returns
    -------
    tuple (mean, median, range)
    """
    ordered = sorted(values)
    n = len(ordered)
    mean = sum(ordered) / n
    mid = n // 2
    median = ordered[mid] if n % 2 else (ordered[mid - 1] + ordered[mid]) / 2
    return mean, median, ordered[-1] - ordered[0]

help(mean_median_range)
m, med, rng = mean_median_range([5.4, 7.8, 6.1, 9.2, 5.0, 7.1])
print(round(m, 2), med, round(rng, 1))''',
'''#md
## Positional and keyword arguments

Arguments can be matched by **position** or by **name**. Named arguments are clearer and can be given in any order.
''',
'''def dose(weight_kg, mg_per_kg, max_mg):
    return min(weight_kg * mg_per_kg, max_mg)

print(dose(20, 15, 500))                                # positional
print(dose(mg_per_kg=15, max_mg=500, weight_kg=40))     # keyword
print(dose(80, mg_per_kg=15, max_mg=500))               # mixed: positional first''',
'''#md
## Default arguments

A parameter with a default can be left out.
''',
'''def classify_hb(hb, low=12.0, high=17.0):
    if hb < low:
        return "low"
    if hb > high:
        return "high"
    return "normal"

print(classify_hb(11.4), classify_hb(11.4, low=11.0), classify_hb(18.0, high=18.5))''',
'''#md
Never use a list or dictionary as a default value: it is created once and shared between calls.
Use `None` and create a new one inside.
''',
'''def add_flag(flag, flags=None):
    if flags is None:
        flags = []
    flags.append(flag)
    return flags

print(add_flag("repeat"), add_flag("haemolysed"))''',
'''#md
## Variable scope

Variables created inside a function are **local**: they exist only while the function runs. Variables
defined at the top level of a notebook or script are **global**.
''',
'''threshold = 7.0                 # global

def is_high(glucose):
    margin = glucose - threshold  # local; reads the global threshold
    return margin >= 0

print(is_high(7.8))
try:
    print(margin)
except NameError as e:
    print("NameError:", e)''',
'''#md
A function can *read* a global variable, but relying on globals makes code fragile: the result changes
if someone changes `threshold` elsewhere. Pass values in as parameters instead.
''',
'''def is_high(glucose, threshold=7.0):
    return glucose >= threshold

print(is_high(7.8), is_high(7.8, threshold=8.0))''',
'''#md
## Functions calling functions
''',
'''def bmi_category(b):
    return "underweight" if b < 18.5 else "normal" if b < 25 else "overweight" if b < 30 else "obese"

def describe(person):
    b = bmi(person["weight"], person["height"])
    return f"{person['id']}: BMI {b:.1f} ({bmi_category(b)})"

for p in [{"id": "P1", "weight": 52, "height": 1.70}, {"id": "P2", "weight": 95, "height": 1.75}]:
    print(describe(p))''',
'''#md
## Reusable functions for laboratory calculations
''',
'''def c1v1(c1, c2, v2):
    """Volume of stock (c1) needed to make v2 of concentration c2."""
    return c2 * v2 / c1

def mg_dl_to_mmol(glucose_mg_dl):
    return glucose_mg_dl / 18.0

def percent_change(before, after):
    return (after - before) / before * 100

print(f"{c1v1(c1=10, c2=0.5, v2=200):.1f} mL of stock")
print(f"{mg_dl_to_mmol(126):.1f} mmol/L")
print(f"{percent_change(142, 131):.1f}% change")''',
'''#md
## Important built-in functions

| function | does | example |
|---|---|---|
| `len(x)` | number of items | `len([1, 2, 3])` → 3 |
| `sum(x)` | total | `sum([1, 2, 3])` → 6 |
| `min(x)`, `max(x)` | smallest, largest | `max([4, 9, 2])` → 9 |
| `range()` | sequence of integers | `range(3)` → 0, 1, 2 |
| `sorted(x)` | new sorted list | |
| `round(x, n)` | round to n places | |
| `abs(x)` | absolute value | `abs(-3)` → 3 |
| `enumerate`, `zip` | loop helpers | module 2 |
| `any(x)`, `all(x)` | is any / every item true? | |
| `type`, `isinstance` | type checks | |
''',
'''v = [3, -8, 5, 0, 12]
print(len(v), sum(v), min(v), max(v), sorted(v), abs(-8))
print(any(x < 0 for x in v), all(x < 20 for x in v), isinstance(v, list))
print(max(["Site B", "Site A"], key=len), min(v, key=abs))''',
'''#md
## Checking functions with assert

`assert condition` does nothing when the condition is true and raises an error when it is false.
A few asserts on known answers catch mistakes early.
''',
'''assert round(bmi(70, 1.75), 1) == 22.9
assert classify_hb(11.0) == "low"
assert mean_median_range([1, 2, 3, 4])[1] == 2.5
print("all checks passed")''',
],
["[Python tutorial: defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)",
 "[Built-in functions](https://docs.python.org/3/library/functions.html)",
 "[Docstring conventions (PEP 257)](https://peps.python.org/pep-0257/)"],
exercises_note="Exercises for this folder are in `exercises/Functions_and_Modules_Exercises.ipynb`.")

lesson(F + "02_Lambda_Functions.ipynb", "Lambda functions",
["write short anonymous functions with lambda",
 "use lambda as a key for sorting, min and max",
 "apply functions to sequences with map and filter",
 "know when a normal function or a comprehension is clearer"],
"""
A lambda is a small function written in one line without a name. Its main use is passing a short
piece of logic to another function, for example telling `sorted` what to sort by.
""",
[
'''#md
## Syntax

`lambda parameters: expression`. The expression's value is returned automatically.
''',
'''square = lambda x: x ** 2
bmi = lambda w, h: w / h ** 2
print(square(6), round(bmi(70, 1.75), 1))

def square_def(x):          # the same as square, written normally
    return x ** 2''',
'''#md
Assigning a lambda to a name, as above, is legal but discouraged: if it deserves a name, use `def`.
Lambdas shine as arguments.

## Sorting with a key
''',
'''participants = [("P03", 52, 7.8), ("P01", 34, 5.4), ("P02", 47, 9.2), ("P04", 29, 6.1)]

print(sorted(participants, key=lambda p: p[1]))                  # by age
print(sorted(participants, key=lambda p: p[2], reverse=True))    # by glucose, highest first
print(max(participants, key=lambda p: p[2]))                     # highest glucose''',
'''records = [{"id": "A", "score": 71}, {"id": "B", "score": 88}, {"id": "C", "score": 64}]
print(sorted(records, key=lambda r: r["score"]))
print(min(records, key=lambda r: r["score"])["id"])''',
'''#md
Sorting by more than one thing: return a tuple. Here by site, then by age within site:
''',
'''people = [("Site B", 51), ("Site A", 34), ("Site B", 29), ("Site A", 62)]
print(sorted(people, key=lambda p: (p[0], p[1])))
print(sorted(people, key=lambda p: (p[0], -p[1])))     # age descending within site''',
'''#md
## map and filter

`map(f, items)` applies `f` to each item; `filter(f, items)` keeps items for which `f` is true.
Both return lazy objects, so wrap them in `list()` to see the result.
''',
'''glucose_mg = [99, 126, 140, 88]
print(list(map(lambda g: round(g / 18, 1), glucose_mg)))
print(list(filter(lambda g: g >= 126, glucose_mg)))''',
'''#md
The same with list comprehensions, which most Python programmers find clearer:
''',
'''print([round(g / 18, 1) for g in glucose_mg])
print([g for g in glucose_mg if g >= 126])''',
'''#md
`map` with a named function is neat when the function already exists:
''',
'''print(list(map(str.strip, ["  a", "b  ", " c "])))
print(list(map(int, ["3", "14", "15"])))''',
'''#md
## Lambdas in pandas

You will meet lambdas often in pandas, for example to compute a column from others (module 6):
''',
'''import pandas as pd
df = pd.DataFrame({"weight": [70, 55, 95], "height": [1.75, 1.60, 1.80]})
df = df.assign(bmi=lambda d: (d["weight"] / d["height"] ** 2).round(1))
df["category"] = df["bmi"].apply(lambda b: "high" if b >= 25 else "normal")
df''',
'''#md
## When not to use lambda

- if the logic needs more than one simple expression, write a `def` function
- if a comprehension says the same thing, prefer the comprehension
- if you need to reuse it, give it a name with `def` and a docstring
''',
],
["[Lambda expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)",
 "[Sorting HOW TO: key functions](https://docs.python.org/3/howto/sorting.html#key-functions)",
 "[map](https://docs.python.org/3/library/functions.html#map) and [filter](https://docs.python.org/3/library/functions.html#filter)"],
exercises_note="Exercises for this folder are in `exercises/Functions_and_Modules_Exercises.ipynb`.")

lesson(F + "03_Modules.ipynb", "Modules and packages",
["import modules in the different ways Python allows",
 "use key modules from the standard library",
 "install and import third-party packages",
 "write and import your own module"],
"""
A module is a file of Python code you can reuse. Python ships with a large *standard library* of modules,
and thousands more are available to install. NumPy, pandas and Matplotlib are all packages of modules.
""",
[
'''#md
## Ways to import
''',
'''import math                          # the whole module; use as math.sqrt
print(math.sqrt(16), math.pi)

from statistics import mean, median  # only some names
print(mean([1, 2, 3]), median([3, 1, 2]))

import datetime as dt                # a short alias
print(dt.date.today().year >= 2025)''',
'''#md
The data science community uses standard aliases. Always use these so others can read your code:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

Avoid `from module import *`: it fills your namespace with unknown names and hides where things come from.

## Useful standard library modules

| module | for |
|---|---|
| `math` | square roots, logs, rounding, constants |
| `statistics` | mean, median, standard deviation |
| `random` | random numbers and sampling |
| `datetime` | dates and times |
| `pathlib`, `os` | files and folders |
| `csv`, `json` | reading and writing those formats |
| `collections` | Counter, defaultdict, namedtuple |
''',
'''import math
print(math.log(100, 10), math.exp(1), math.floor(2.7), math.ceil(2.1), math.isclose(0.1 + 0.2, 0.3))''',
'''import statistics as st
data = [2.1, 3.4, 3.4, 5.0, 7.9]
print(st.mean(data), st.median(data), st.mode(data), round(st.stdev(data), 3), st.quantiles(data, n=4))''',
'''import random
random.seed(42)              # a seed makes "random" results repeatable
print(random.random(), random.randint(1, 6), random.choice(["A", "B", "C"]))
print(random.sample(range(1, 50), 6))''',
'''from datetime import date, datetime, timedelta
collected = datetime.strptime("14/03/2025", "%d/%m/%Y")
print(collected.date(), collected.strftime("%A %d %B %Y"))
print(collected + timedelta(days=28))
print((date(2025, 12, 31) - collected.date()).days, "days to the end of the year")''',
'''#md
Common date format codes: `%Y` four-digit year, `%m` month, `%d` day, `%H` hour, `%M` minute,
`%b`/`%B` month name, `%A` weekday name.
''',
'''from pathlib import Path
raw = Path("..") / "datasets" / "raw"
print(sorted(p.name for p in raw.glob("*.csv")))
print((raw / "patients.csv").exists(), (raw / "patients.csv").suffix)''',
'''#md
## Installing packages

Third-party packages are installed from a terminal (not inside Python):

```bash
pip install pandas
pip install -r requirements.txt
conda install pandas            # with Anaconda
```

In a notebook you can run `%pip install package_name` in a cell. Check what is installed:
''',
'''import importlib.metadata as md
for pkg in ["numpy", "pandas", "matplotlib", "seaborn"]:
    print(pkg, md.version(pkg))''',
'''#md
## Writing your own module

Any `.py` file is a module. Put functions you use in several notebooks into one file, then import it.
The cell below writes a small module file and imports it.
''',
'''code = """\\"\\"\\"Helper functions for laboratory calculations.\\"\\"\\"

def bmi(weight_kg, height_m):
    return weight_kg / height_m ** 2

def mg_dl_to_mmol(value):
    return value / 18.0

LAB_NAME = "Course lab"
"""
Path("labtools.py").write_text(code)

import labtools
print(labtools.__doc__)
print(round(labtools.bmi(70, 1.75), 1), labtools.mg_dl_to_mmol(126), labtools.LAB_NAME)''',
'''#md
Python looks for modules in the folder you are working in first, then in installed packages. If you
change the module file, restart the kernel (or use `importlib.reload`) to load the new version.

A folder of modules with an `__init__.py` file is a **package**. A typical project:

```text
project/
├── analysis.ipynb
└── mytools/
    ├── __init__.py
    ├── cleaning.py
    └── stats.py
```

Then: `from mytools.cleaning import standardise_names`.

### Code that runs only as a script

Code under `if __name__ == "__main__":` runs when the file is executed directly (`python labtools.py`)
but not when it is imported.

```python
if __name__ == "__main__":
    print(bmi(70, 1.75))
```
''',
'''Path("labtools.py").unlink()        # tidy up the demo file''',
],
["[Python tutorial: modules](https://docs.python.org/3/tutorial/modules.html)",
 "[The Python standard library](https://docs.python.org/3/library/index.html)",
 "[Installing packages with pip](https://packaging.python.org/en/latest/tutorials/installing-packages/)"],
exercises_note="Exercises for this folder are in `exercises/Functions_and_Modules_Exercises.ipynb`.")

lesson(F + "04_Error_Handling.ipynb", "Error handling and file handling",
["read error messages and recognise common error types",
 "handle errors with try, except, else and finally",
 "raise errors for invalid input",
 "read and write text files safely with with open()",
 "read and write CSV files with the csv module",
 "handle missing files and invalid values"],
"""
Errors are part of programming: a file is missing, a value is text instead of a number, a list is empty.
Good analysis code expects these situations and handles them clearly instead of crashing halfway or,
worse, carrying on with wrong values. This notebook also covers reading and writing files, where many
errors happen.
""",
[
'''#md
## Reading an error message

Python prints a *traceback*. Read the **last line first**: it names the error type and gives a message.
The lines above show where it happened.

| error | typical cause |
|---|---|
| `NameError` | a name that does not exist (typo, or cell not run) |
| `TypeError` | an operation on the wrong type, e.g. `"5" + 3` |
| `ValueError` | right type, impossible value, e.g. `int("five")` |
| `KeyError` | a dictionary key that does not exist |
| `IndexError` | a list position that does not exist |
| `ZeroDivisionError` | dividing by zero |
| `FileNotFoundError` | a file path that does not exist |
| `IndentationError`, `SyntaxError` | code Python cannot read |
''',
'''for code in ['int("five")', '"5" + 3', '[1, 2][5]', '{"a": 1}["b"]', '1 / 0']:
    try:
        eval(code)
    except Exception as e:
        print(f"{code:16} -> {type(e).__name__}: {e}")''',
'''#md
## try and except

Put code that might fail in `try`. If an error of the named type happens, the `except` block runs
instead of the program stopping.
''',
'''def to_number(text):
    try:
        return float(text)
    except ValueError:
        return None

values = ["12.5", "n/a", "7", "", "3.2e1"]
print([to_number(v) for v in values])''',
'''#md
Catch the **specific** error you expect. A bare `except:` also catches typos and other bugs, hiding them.
Several types can share one block:
''',
'''def safe_ratio(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float("nan")
    except TypeError:
        return None

print(safe_ratio(10, 4), safe_ratio(10, 0), safe_ratio("10", 4))''',
'''#md
## else and finally

- `else` runs only if the `try` block succeeded
- `finally` always runs, error or not, which is where clean-up goes
''',
'''def parse_age(text):
    try:
        age = int(text)
    except ValueError:
        print(f"  {text!r} is not a whole number")
        return None
    else:
        print(f"  parsed {age}")
        return age
    finally:
        print("  (finished checking", repr(text) + ")")

parse_age("42")
parse_age("forty")''',
'''#md
## Raising errors

When input does not make sense, stop with a clear message rather than returning a wrong answer.
''',
'''def bmi(weight_kg, height_m):
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError(f"weight and height must be positive, got {weight_kg} and {height_m}")
    if height_m > 3:
        raise ValueError(f"height {height_m} looks like centimetres; give metres")
    return weight_kg / height_m ** 2

for w, h in [(70, 1.75), (70, 175), (70, 0)]:
    try:
        print(round(bmi(w, h), 1))
    except ValueError as e:
        print("ValueError:", e)''',
'''#md
## File handling

### Opening files with with

`with open(...) as f:` opens a file and closes it automatically when the block ends, even if an error
happens.

| mode | meaning |
|---|---|
| `"r"` | read (the default) |
| `"w"` | write, replacing the file if it exists |
| `"a"` | append to the end |
| `"x"` | create; fail if the file exists |

Always give `encoding="utf-8"` for text files so special characters work on every computer.
''',
'''from pathlib import Path
work = Path("scratch")
work.mkdir(exist_ok=True)

notes = work / "notes.txt"
with open(notes, "w", encoding="utf-8") as f:
    f.write("Run 1: 48 samples processed\\n")
    f.write("Run 2: 52 samples processed\\n")

with open(notes, "a", encoding="utf-8") as f:
    f.write("Run 3: 47 samples processed\\n")

with open(notes, encoding="utf-8") as f:
    content = f.read()
print(content)''',
'''#md
Reading line by line uses little memory, even for huge files:
''',
'''total = 0
with open(notes, encoding="utf-8") as f:
    for line in f:
        number = int(line.split(":")[1].split()[0])
        total += number
print("total samples:", total)''',
'''#md
`pathlib` has shortcuts for small files:
''',
'''print(notes.read_text(encoding="utf-8").splitlines())''',
'''#md
### Reading CSV files with the csv module

CSV (comma-separated values) is the most common data file format. `csv.DictReader` reads each row as a
dictionary keyed by the column names. Note that **every value arrives as text**.
''',
'''import csv

with open("../datasets/raw/patients.csv", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(len(rows), "rows; columns:", list(rows[0].keys()))
print(rows[0])
print(type(rows[0]["age"]))''',
'''ages = [int(r["age"]) for r in rows]
weights = [float(r["weight_kg"]) for r in rows if r["weight_kg"] != ""]
print(f"mean age {sum(ages) / len(ages):.1f}; mean weight {sum(weights) / len(weights):.1f} "
      f"({len(rows) - len(weights)} weights missing)")''',
'''#md
### Writing CSV files
''',
'''summary = {}
for r in rows:
    summary.setdefault(r["site"], []).append(int(r["age"]))

out = work / "age_by_site.csv"
with open(out, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["site", "n", "mean_age"])
    for site, a in sorted(summary.items()):
        writer.writerow([site, len(a), round(sum(a) / len(a), 1)])

print(out.read_text())''',
'''#md
`newline=""` is required by the `csv` module on all platforms to avoid blank lines on Windows.

In practice, pandas reads and writes CSV files in one line (module 6), but the `csv` module is useful
for small scripts and for files that are not quite tables.

### Handling missing files
''',
'''def load_lines(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"File not found: {path}. Check the name and the folder you are working in.")
        return []

print(load_lines(notes)[:1])
print(load_lines(work / "missing.txt"))''',
'''#md
### Handling invalid values while reading

A robust reader keeps going past bad rows and reports them:
''',
'''bad_file = work / "readings.csv"
bad_file.write_text("id,value\\nA,5.4\\nB,n/a\\nC,7.1\\nD,\\nE,6.8\\n")

good, problems = [], []
with open(bad_file, encoding="utf-8", newline="") as f:
    for line_no, row in enumerate(csv.DictReader(f), start=2):
        try:
            good.append((row["id"], float(row["value"])))
        except ValueError:
            problems.append((line_no, row["id"], row["value"]))

print("valid:", good)
print("problems (line, id, value):", problems)''',
'''import shutil
shutil.rmtree(work)          # remove the demo folder''',
],
["[Python tutorial: errors and exceptions](https://docs.python.org/3/tutorial/errors.html)",
 "[Built-in exceptions](https://docs.python.org/3/library/exceptions.html)",
 "[Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)",
 "[csv module](https://docs.python.org/3/library/csv.html)",
 "[pathlib](https://docs.python.org/3/library/pathlib.html)"],
exercises_note="Exercises for this folder are in `exercises/Functions_and_Modules_Exercises.ipynb`.")

exercises(F, "Functions and Modules", "functions, lambda, modules, errors and files",
"Exercises for notebooks 01 to 04 of this folder. File paths assume this notebook is in the `exercises` folder.",
[
("Write a function `summary(values)` that returns the mean, median and range of a list. Test it on `[4, 8, 15, 16, 23, 42]`.",
 '''def summary(values):
    s = sorted(values); n = len(s); mid = n // 2
    median = s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2
    return sum(s) / n, median, s[-1] - s[0]

print(summary([4, 8, 15, 16, 23, 42]))''', "Mean 18.0, median 15.5, range 38."),
("Write `c1v1(c1, c2, v2)` that returns the stock volume needed (v1 = c2 × v2 / c1). How much 10 mM stock makes 50 mL of 0.2 mM solution?",
 '''def c1v1(c1, c2, v2):
    return c2 * v2 / c1
print(c1v1(10, 0.2, 50), "mL")''', "1.0 mL."),
("Write `classify_bp(sbp, dbp=None)` that returns `\"high\"` if sbp is 140 or more, or dbp (if given) is 90 or more, otherwise `\"normal\"`. Call it with and without dbp.",
 '''def classify_bp(sbp, dbp=None):
    if sbp >= 140 or (dbp is not None and dbp >= 90):
        return "high"
    return "normal"
print(classify_bp(132), classify_bp(132, 94), classify_bp(150))'''),
("Sort `[(\"Site C\", 0.08), (\"Site A\", 0.12), (\"Site B\", 0.31)]` by the second value, highest first, using a lambda.",
 '''print(sorted([("Site C", 0.08), ("Site A", 0.12), ("Site B", 0.31)], key=lambda x: x[1], reverse=True))'''),
("Use the `statistics` module to compute the mean, standard deviation and quartiles of `[2.3, 4.1, 3.8, 5.6, 4.4, 3.9, 6.2]`.",
 '''import statistics as st
d = [2.3, 4.1, 3.8, 5.6, 4.4, 3.9, 6.2]
print(round(st.mean(d), 3), round(st.stdev(d), 3), st.quantiles(d, n=4))'''),
("Use `datetime` to work out how many days lie between 2025-03-14 and 2025-11-30, and what weekday 2025-11-30 is.",
 '''from datetime import date
print((date(2025, 11, 30) - date(2025, 3, 14)).days, date(2025, 11, 30).strftime("%A"))''', "261 days; a Sunday."),
("Write `safe_float(text)` that returns a float, or `None` if the text cannot be converted. Apply it to `[\"3.5\", \"abc\", \"\", \"1e2\"]`.",
 '''def safe_float(text):
    try:
        return float(text)
    except ValueError:
        return None
print([safe_float(t) for t in ["3.5", "abc", "", "1e2"]])'''),
("Write `percent(part, whole)` that raises a `ValueError` with a clear message if `whole` is 0 or negative. Show it working and failing.",
 '''def percent(part, whole):
    if whole <= 0:
        raise ValueError("whole must be a positive number")
    return part / whole * 100
print(percent(37, 412))
try:
    percent(3, 0)
except ValueError as e:
    print("error:", e)'''),
("Read `../../datasets/raw/patients.csv` with the `csv` module and count how many patients are smokers.",
 '''import csv
with open("../../datasets/raw/patients.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
print(sum(r["smoker"] == "Yes" for r in rows), "of", len(rows))'''),
("Write a CSV file `group_counts.csv` with the number of patients in each group (Control, Treatment), read it back and print it, then delete it.",
 '''import csv
from pathlib import Path
counts = {}
for r in rows:
    counts[r["group"]] = counts.get(r["group"], 0) + 1
with open("group_counts.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(["group", "n"]); w.writerows(sorted(counts.items()))
print(Path("group_counts.csv").read_text())
Path("group_counts.csv").unlink()'''),
("Make the file reader below robust: it should print a friendly message if the file does not exist instead of crashing.\n\n```python\nwith open(\"results_2019.csv\") as f:\n    print(f.read())\n```",
 '''try:
    with open("results_2019.csv") as f:
        print(f.read())
except FileNotFoundError:
    print("results_2019.csv was not found; check the file name and folder")'''),
])
print("modules 03-04 written")
