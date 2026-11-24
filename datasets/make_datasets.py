"""Create the simulated datasets used in the course.

Run from the repository root:

    python datasets/make_datasets.py

Every dataset is simulated. No real people, patients or businesses are described.
Some files contain deliberate problems (duplicates, typos, impossible values,
missing entries) so they can be cleaned in the notebooks.
"""
from pathlib import Path

import numpy as np
import pandas as pd

rng = np.random.default_rng(2026)
raw = Path(__file__).parent / "raw"
raw.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- patients
n = 300
sites = ["Site A", "Site B", "Site C", "Site D"]
patients = pd.DataFrame({
    "patient_id": [f"P{i:04d}" for i in range(1, n + 1)],
    "site": rng.choice(sites, n, p=[0.4, 0.25, 0.2, 0.15]),
    "sex": rng.choice(["F", "M"], n),
    "age": rng.integers(18, 86, n),
    "weight_kg": np.round(rng.normal(70, 13, n).clip(38, 140), 1),
    "height_cm": np.round(rng.normal(166, 10, n).clip(140, 200), 1),
    "smoker": rng.choice(["No", "Yes"], n, p=[0.8, 0.2]),
    "group": rng.choice(["Control", "Treatment"], n),
    "enrolled": (pd.Timestamp("2025-01-01") + pd.to_timedelta(rng.integers(0, 365, n), unit="D")).date,
})
patients.loc[rng.choice(n, 10, replace=False), "weight_kg"] = np.nan
patients.to_csv(raw / "patients.csv", index=False)

# ---------------------------------------------------------------- lab results: repeated visits
rows = []
for pid, grp, enrolled in zip(patients.patient_id, patients.group, pd.to_datetime(patients.enrolled)):
    base_glucose = rng.normal(6.2, 1.0)
    effect = -0.25 if grp == "Treatment" else 0.0
    for visit in range(int(rng.integers(2, 5))):
        rows.append({
            "patient_id": pid,
            "visit": visit,
            "visit_date": (enrolled + pd.Timedelta(days=30 * visit + int(rng.integers(-3, 4)))).date(),
            "glucose_mmol": round(base_glucose + effect * visit + rng.normal(0, 0.4), 1),
            "haemoglobin_g_dl": round(float(rng.normal(13.2, 1.5)), 1),
            "systolic_bp": int(rng.normal(128, 15)),
            "diastolic_bp": int(rng.normal(82, 9)),
        })
pd.DataFrame(rows).to_csv(raw / "lab_results.csv", index=False)

# ---------------------------------------------------------------- messy sample register
m = 420
samples = pd.DataFrame({
    "sample_id": [f"S-{i:04d}" for i in range(1, m + 1)],
    "patient_id": rng.choice(patients.patient_id, m),
    "collected": (pd.Timestamp("2025-01-01") + pd.to_timedelta(rng.integers(0, 365, m), unit="D")).strftime("%d/%m/%Y"),
    "sample_type": rng.choice(["Blood", "blood ", "BLOOD", "Urine", "urine", "Saliva"], m),
    "result": rng.choice(["Positive", "Negative", "positive", "NEG", "neg", ""], m, p=[0.2, 0.5, 0.05, 0.1, 0.1, 0.05]),
    "concentration": rng.choice(["12.5", "8.0", "3.2", "<0.5", ">100", "not done", "15.1", "22.0"], m),
    "temperature_c": np.round(rng.normal(4.0, 1.2, m), 1),
    "technician": rng.choice(["AN", "BK", "CM", "an", None], m, p=[0.3, 0.3, 0.25, 0.1, 0.05]),
})
samples.loc[rng.choice(m, 6, replace=False), "temperature_c"] = 99.0       # impossible fridge temperatures
samples = pd.concat([samples, samples.sample(10, random_state=4)])          # duplicated rows
samples.to_csv(raw / "sample_register_raw.csv", index=False)

# ---------------------------------------------------------------- daily sales (general data)
days = pd.date_range("2024-01-01", "2025-12-31", freq="D")
sales_rows = []
for shop, base in {"North": 120, "Central": 260, "South": 90}.items():
    season = 1 + 0.25 * np.sin(2 * np.pi * (days.dayofyear - 80) / 365.25)
    weekday = np.where(days.dayofweek == 5, 1.35, np.where(days.dayofweek == 6, 0.7, 1.0))
    promo = rng.random(len(days)) < 0.08
    units = rng.poisson(base * season * weekday * np.where(promo, 1.5, 1.0))
    price = np.round(rng.normal(4.5, 0.15, len(days)) * np.where(promo, 0.85, 1.0), 2)
    sales_rows.append(pd.DataFrame({"date": days.date, "shop": shop, "units": units, "price": price, "promo": promo.astype(int)}))
pd.concat(sales_rows).to_csv(raw / "daily_sales.csv", index=False)

# ---------------------------------------------------------------- site information, as an Excel workbook
site_info = pd.DataFrame({"site": sites, "region": ["North", "Central", "Central", "South"],
                          "beds": [120, 340, 210, 80], "opened": [1998, 1972, 2005, 2014]})
staff = pd.DataFrame({"site": rng.choice(sites, 25), "role": rng.choice(["Nurse", "Doctor", "Lab"], 25),
                      "years": rng.integers(1, 30, 25)})
with pd.ExcelWriter(raw / "sites.xlsx") as xl:
    site_info.to_excel(xl, sheet_name="sites", index=False)
    staff.to_excel(xl, sheet_name="staff", index=False)

# ---------------------------------------------------------------- small gene expression table (TSV)
genes = [f"GENE{i:02d}" for i in range(1, 21)]
cond = np.repeat(["control", "treated"], 12)
expr = rng.normal(8, 1, (24, 20))
expr[cond == "treated", :5] += 1.5          # five genes respond to treatment
expr[:, 10:13] += expr[:, :3] * 0.5          # some genes move together
ge = pd.DataFrame(np.round(expr, 3), columns=genes)
ge.insert(0, "condition", cond)
ge.insert(0, "sample", [f"S{i:02d}" for i in range(1, 25)])
ge.to_csv(raw / "gene_expression.tsv", sep="\t", index=False)

# ---------------------------------------------------------------- DNA sequences (text)
with open(raw / "sequences.txt", "w") as fh:
    for i in range(1, 11):
        seq = "".join(rng.choice(list("ACGT"), int(rng.integers(60, 120))))
        fh.write(f"seq{i:02d}\t{seq}\n")

# ---------------------------------------------------------------- capstone: clinic study, deliberately untidy
k = 480
cap = pd.DataFrame({
    "participant": [f"HC-{i:03d}" for i in range(1, k + 1)],
    "clinic": rng.choice(["East", "West", "North", "east", "West "], k, p=[0.3, 0.3, 0.3, 0.05, 0.05]),
    "sex": rng.choice(["Female", "Male", "F", "M", "female"], k, p=[0.42, 0.42, 0.06, 0.06, 0.04]),
    "age_years": rng.integers(25, 80, k).astype(float),
    "arm": rng.choice(["Diet", "Diet + exercise", "Usual care"], k),
    "baseline_date": (pd.Timestamp("2024-02-01") + pd.to_timedelta(rng.integers(0, 300, k), unit="D")).strftime("%Y-%m-%d"),
    "weight_kg": np.round(rng.normal(82, 14, k), 1),
    "height_m": np.round(rng.normal(1.67, 0.09, k), 2),
    "sbp_baseline": np.round(rng.normal(142, 14, k)),
    "glucose_baseline": np.round(rng.normal(7.4, 1.6, k), 1),
    "smoking": rng.choice(["never", "former", "current", "unknown"], k, p=[0.55, 0.25, 0.15, 0.05]),
})
drop_sbp = cap["arm"].map({"Diet": 4, "Diet + exercise": 9, "Usual care": 1})
cap["sbp_6m"] = np.round(cap["sbp_baseline"] - drop_sbp + rng.normal(0, 8, k))
drop_glu = cap["arm"].map({"Diet": 0.4, "Diet + exercise": 0.8, "Usual care": 0.05})
cap["glucose_6m"] = np.round(cap["glucose_baseline"] - drop_glu + rng.normal(0, 0.6, k), 1)
cap.loc[rng.choice(k, 35, replace=False), ["sbp_6m", "glucose_6m"]] = np.nan          # lost to follow-up
cap.loc[rng.choice(k, 5, replace=False), "age_years"] = rng.choice([0, 150, -1], 5)    # entry errors
cap.loc[rng.choice(k, 4, replace=False), "height_m"] = cap["height_m"].iloc[:4].values * 100   # cm typed in metres column
cap = pd.concat([cap, cap.sample(6, random_state=9)])                                  # duplicate rows
cap.to_csv(raw / "clinic_study.csv", index=False)

print("wrote:", ", ".join(sorted(p.name for p in raw.iterdir())))
