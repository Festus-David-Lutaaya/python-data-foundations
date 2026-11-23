"""Tiny helper to write notebooks from a list of cells.

A cell is a string. Strings starting with '#md' are markdown (the first
line is dropped); everything else is code.
"""
import nbformat as nbf
from pathlib import Path


def build(path, cells):
    nb = nbf.v4.new_notebook()
    out = []
    for c in cells:
        c = c.strip("\n")
        if c.startswith("#md"):
            out.append(nbf.v4.new_markdown_cell(c.split("\n", 1)[1].strip()))
        else:
            out.append(nbf.v4.new_code_cell(c))
    nb["cells"] = out
    nb["metadata"]["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    nbf.write(nb, path)
