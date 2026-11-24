# Python basics cheat sheet

## Types and conversion

```python
x = 42            # int
y = 3.14          # float
s = "text"        # str
ok = True         # bool
n = None          # no value

int("7"), float("2.5"), str(10), bool(0)
type(x), isinstance(x, int)
```

## Operators

```python
+  -  *  /       # / always gives a float
//  %  **        # floor division, remainder, power
==  !=  <  <=  >  >=
and  or  not
in   not in      # membership
x += 1           # same as x = x + 1
```

## Strings

```python
s = "  Blood Sample  "
s.strip()  s.lower()  s.upper()  s.title()
s.replace("Blood", "Urine")
"a,b,c".split(",")          # ['a', 'b', 'c']
"-".join(["a", "b"])        # 'a-b'
s[0]  s[-1]  s[2:5]  s[::-1]
len(s)   "lo" in s   s.startswith("  B")
f"{name}: {value:.2f}  {share:.1%}  {n:>5}"
```

## Lists, tuples, sets, dictionaries

```python
lst = [3, 1, 2]
lst.append(4); lst.extend([5, 6]); lst.insert(0, 9)
lst.remove(9); lst.pop(); sorted(lst); lst.sort(reverse=True)
lst[0]  lst[-1]  lst[1:3]  len(lst)  sum(lst)  min(lst)  max(lst)
copy = lst.copy()

t = (1, 2)                  # tuple: cannot be changed
a, b = t                    # unpacking

st = {1, 2, 2, 3}           # set: {1, 2, 3}
st | other   st & other   st - other

d = {"id": "P01", "age": 34}
d["age"]   d.get("weight", 0)   d["sex"] = "F"   d.pop("sex")
d.keys()   d.values()   d.items()   "id" in d
```

## Conditions and loops

```python
if x > 10:
    ...
elif x > 5:
    ...
else:
    ...

for item in items: ...
for i, item in enumerate(items): ...
for a, b in zip(list1, list2): ...
for k, v in d.items(): ...
while condition: ...
break   continue   pass
```

## Comprehensions

```python
[x * 2 for x in values]
[x for x in values if x > 0]
{k: v for k, v in pairs}
{x % 3 for x in values}
```

## Functions

```python
def bmi(weight, height=1.7):
    """Docstring: what it does."""
    return weight / height ** 2

bmi(70)  bmi(70, 1.8)  bmi(height=1.8, weight=70)
square = lambda x: x ** 2
sorted(records, key=lambda r: r["age"])
```

## Errors and files

```python
try:
    value = float(text)
except ValueError:
    value = None
finally:
    ...

raise ValueError("message")

with open("file.txt", encoding="utf-8") as f:
    for line in f: ...
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("text\n")
```

## Modules

```python
import math
from statistics import mean, median
import numpy as np
from pathlib import Path
```
