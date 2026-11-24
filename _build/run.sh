#!/bin/bash
# execute notebooks given as arguments, in their own folder; report failures and warnings
for f in "$@"; do
  if jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=900 "$f" >/tmp/nbrun.log 2>&1; then
    echo "ok   $f"
  else
    echo "FAIL $f"; grep -E "Error" /tmp/nbrun.log | tail -3
  fi
done
python3 - "$@" <<'PY'
import sys, nbformat
for f in sys.argv[1:]:
    nb = nbformat.read(f, 4)
    for c in nb.cells:
        for o in c.get("outputs", []):
            t = o.get("text", "")
            if "Warning" in t: print("WARN", f, t[:200].replace("\n", " "))
PY
