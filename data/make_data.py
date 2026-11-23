"""Create the practice datasets used in the notebooks.

Run from the repository root:  python data/make_data.py
All data are simulated.
"""
from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(2026)
here = Path(__file__).parent

# ---- patients: one row per person ----
n = 300
sites = ["Kampala", "Gulu", "Mbarara", "Mbale", "Jinja"]
patients = pd.DataFrame({
    "patient_id": [f"P{i:04d}" for i in range(1, n + 1)],
    "site": rng.choice(sites, n, p=[0.35, 0.15, 0.2, 0.15, 0.15]),
    "sex": rng.choice(["F", "M"], n),
    "age": rng.integers(1, 85, n),
    "weight_kg": np.round(rng.normal(62, 14, n).clip(8, 130), 1),
    "height_cm": np.round(rng.normal(162, 12, n).clip(70, 200), 1),
    "hiv_status": rng.choice(["Negative", "Positive", "Unknown"], n, p=[0.8, 0.12, 0.08]),
    "enrolled": pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 365, n), unit="D"),
})
patients.loc[rng.choice(n, 12, replace=False), "weight_kg"] = np.nan
patients.to_csv(here / "patients.csv", index=False)

# ---- visits: several lab results per person (long format) ----
rows = []
for pid, enrolled in zip(patients.patient_id, patients.enrolled):
    base_hb = rng.normal(12.5, 1.8)
    for v in range(rng.integers(1, 5)):
        rows.append({
            "patient_id": pid,
            "visit": v,
            "visit_date": enrolled + pd.Timedelta(days=28 * v + int(rng.integers(-3, 4))),
            "hb": round(base_hb + rng.normal(0.3 * v, 0.6), 1),
            "wbc": round(float(rng.lognormal(1.9, 0.3)), 1),
            "crp": round(float(rng.lognormal(1.5, 1.0)), 1),
        })
visits = pd.DataFrame(rows)
visits.to_csv(here / "visits.csv", index=False)

# ---- isolates: microbiology results, with typical data-entry problems ----
m = 400
organisms = ["E. coli", "K. pneumoniae", "S. aureus", "P. aeruginosa"]
iso = pd.DataFrame({
    "isolate_id": [f"ISO-{i:04d}" for i in range(1, m + 1)],
    "patient_id": rng.choice(patients.patient_id, m),
    "collected": (pd.to_datetime("2025-01-01")
                  + pd.to_timedelta(rng.integers(0, 365, m), unit="D")).strftime("%d/%m/%Y"),
    "specimen": rng.choice(["Urine", "urine ", "Blood", "BLOOD", "Wound swab", "Stool"], m),
    "organism": rng.choice(organisms, m, p=[0.4, 0.25, 0.2, 0.15]),
    "ciprofloxacin": rng.choice(["S", "R", "I", "s", "r", ""], m, p=[0.45, 0.35, 0.05, 0.05, 0.05, 0.05]),
    "ceftriaxone": rng.choice(["S", "R", "I", "n/a"], m, p=[0.45, 0.4, 0.05, 0.10]),
    "mic_cipro": rng.choice(["0.25", "0.5", "1", "2", ">4", "<=0.06", "not done"], m),
    "temp_c": np.round(rng.normal(37.6, 0.9, m), 1),
})
iso.loc[rng.choice(m, 6, replace=False), "temp_c"] = 999      # impossible values
iso = pd.concat([iso, iso.sample(8, random_state=1)])         # duplicated rows
iso.to_csv(here / "isolates_raw.csv", index=False)

print("wrote", ", ".join(p.name for p in here.glob("*.csv")))
