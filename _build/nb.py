"""Helpers that write the course notebooks.

lesson(): a teaching notebook in the course format
    title, objectives, introduction, body cells, further reading
exercises(): an exercises notebook and a matching solutions notebook
Cells are strings; a string starting with '#md' is markdown (first line dropped).
"""
from pathlib import Path
import nbformat as nbf


def _cells(items):
    out = []
    for c in items:
        c = c.strip("\n")
        if c.startswith("#md"):
            out.append(nbf.v4.new_markdown_cell(c.split("\n", 1)[1].strip()))
        else:
            out.append(nbf.v4.new_code_cell(c))
    return out


def _write(path, cells):
    nb = nbf.v4.new_notebook()
    nb["cells"] = cells
    nb["metadata"]["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    nbf.write(nb, path)


def lesson(path, title, objectives, intro, body, further, exercises_note=None):
    head = [f"#md\n# {title}\n\n## Learning objectives\n\nBy the end of this notebook you will be able to:\n\n"
            + "\n".join(f"- {o}" for o in objectives),
            "#md\n## Introduction\n\n" + intro.strip()]
    tail = ["#md\n## Further reading\n\n" + "\n".join(f"- {f}" for f in further)]
    if exercises_note:
        tail.insert(0, "#md\n## Practise\n\n" + exercises_note)
    _write(path, _cells(head + body + tail))


def exercises(folder, module, title, intro, items):
    """items: list of (task_markdown, solution_code or list of code strings, optional note after)"""
    ex = [f"#md\n# {module} exercises: {title}\n\n{intro}\n\nWrite your answer in the empty cell under each task. "
          "Worked solutions are in the solutions notebook in this folder; try each task first."]
    sol = [f"#md\n# {module} solutions: {title}\n\nWorked solutions to the exercises. "
           "Other correct answers are possible; what matters is that the result is right and the code is readable."]
    for i, item in enumerate(items, 1):
        task, code = item[0], item[1]
        note = item[2] if len(item) > 2 else None
        ex += [f"#md\n## Exercise {i}\n\n{task}", "# your code here\n"]
        sol += [f"#md\n## Exercise {i}\n\n{task}"]
        sol += code if isinstance(code, list) else [code]
        if note:
            sol += [f"#md\n{note}"]
    slug = module.replace(" ", "_")
    _write(Path(folder) / "exercises" / f"{slug}_Exercises.ipynb", _cells(ex))
    _write(Path(folder) / "exercises" / f"{slug}_Solutions.ipynb", _cells(sol))
