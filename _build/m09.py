from pathlib import Path
from nb import lesson

F = "09_Capstone_Project/"

Path(F + "README.md").write_text("""# Capstone project: exploratory analysis of a clinical study dataset

The capstone brings together everything in modules 1 to 8. You take a raw dataset with realistic
problems, clean it, describe it, visualise it and explain what you found, with every step in code.

## The dataset

`datasets/raw/clinic_study.csv` is a simulated study of 480 adults attending three clinics (East,
North, West). Each was assigned to one of three arms (*Usual care*, *Diet*, *Diet + exercise*) and had
blood pressure and fasting glucose measured at baseline and again after six months.

| column | description |
|---|---|
| participant | participant ID (HC-001 ...) |
| clinic | clinic attended |
| sex | sex |
| age_years | age at baseline |
| arm | study arm |
| baseline_date | date of the baseline visit |
| weight_kg | weight at baseline (kg) |
| height_m | height (m) |
| sbp_baseline, sbp_6m | systolic blood pressure (mmHg) at baseline and six months |
| glucose_baseline, glucose_6m | fasting glucose (mmol/L) at baseline and six months |
| smoking | never, former, current or unknown |

The file contains deliberate problems of the kind found in real data. Finding them is part of the task.

## Questions to answer

1. Who are the participants? Describe them by clinic, sex, age, BMI and smoking.
2. Are the three arms similar at baseline?
3. How did blood pressure and glucose change over six months, and does the change differ by arm?
4. How many participants have no six-month measurement, and do they differ from those who returned?
5. How are age, BMI, blood pressure and glucose related to each other?

## Stages

| stage | what to do | modules |
|---|---|---|
| 1. Understand the data | read the column descriptions; state what one row is | 6 |
| 2. Import | read the raw file with suitable options; never edit it by hand | 6 |
| 3. Explore | size, types, missing values, categories, ranges, duplicates | 6 |
| 4. Clean | fix categories, impossible values, unit errors, duplicates; record each decision | 3, 4, 6 |
| 5. Derive | BMI, six-month changes, age groups, a completer flag | 5, 6 |
| 6. Describe | summary tables overall, by arm and by completion | 6 |
| 7. Visualise | at least five clear, labelled figures | 7, 8 |
| 8. Interpret | answer the questions in plain language; state limitations | all |
| 9. Export | write the cleaned dataset and figures | 6, 7 |

## Deliverables

1. **A documented Jupyter notebook** that runs from top to bottom without errors, with markdown
   explaining each step and each decision
2. **A cleaned dataset** saved to `datasets/processed/clinic_study_clean.csv`
3. **Descriptive statistics tables** (participant characteristics; outcomes by arm)
4. **At least five visualisations**, saved to `09_Capstone_Project/figures/`
5. **Interpretation of findings**: a short written summary answering the questions, with limitations
6. **A README** for your project: what it is, the data, how to run it and the main findings

## Worked example

`analysis.ipynb` is a complete worked solution. Try the project yourself first, using
`analysis_template.ipynb` as a starting point, then compare. There is more than one reasonable way to
make most cleaning decisions; what matters is that each is sensible, documented and applied in code.

## Scope

The capstone is descriptive. Formal hypothesis testing, regression modelling and machine learning are
outside this course; where a comparison suggests a difference, say that it would need a statistical
test to confirm.
""")

# ---------------------------------------------------------------- template
lesson(F + "analysis_template.ipynb", "Capstone project: your analysis",
["complete a full exploratory analysis from raw data to written findings"],
"""
Replace each *to do* with your own code and markdown. The brief is in `README.md`. Paths assume this
notebook is in `09_Capstone_Project/`.
""",
[
'''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

RAW = Path("../datasets/raw")
PROCESSED = Path("../datasets/processed")
FIGURES = Path("figures")
FIGURES.mkdir(exist_ok=True)''',
"#md\n## 1. Understand the data\n\n*to do: what is one row? what are the questions?*",
"#md\n## 2. Import",
"# to do",
"#md\n## 3. Explore\n\n*to do: shape, info, describe, value counts, missing values, duplicates*",
"# to do",
"#md\n## 4. Clean\n\n*to do: list each problem and the decision you made*",
"# to do",
"#md\n## 5. Derive new variables",
"# to do",
"#md\n## 6. Descriptive statistics",
"# to do",
"#md\n## 7. Visualisations (at least five)",
"# to do",
"#md\n## 8. Findings and limitations\n\n*to do*",
"#md\n## 9. Export",
"# to do",
],
["The brief: `README.md` in this folder"])

# ---------------------------------------------------------------- worked analysis
lesson(F + "analysis.ipynb", "Capstone worked example: exploratory analysis of a clinical study",
["clean a raw clinical dataset and document each decision",
 "derive analysis variables",
 "describe participants and outcomes with summary tables",
 "communicate findings with clear figures",
 "interpret results and state limitations"],
"""
A complete worked solution to the capstone brief in `README.md`. It follows the stages in order:
understand, import, explore, clean, derive, describe, visualise, interpret, export.

The data are simulated for teaching. The patterns found here describe these data only.
""",
[
'''#md
## Setup
''',
'''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

RAW = Path("../datasets/raw")
PROCESSED = Path("../datasets/processed")
FIGURES = Path("figures")
PROCESSED.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid", context="notebook")
ARM_ORDER = ["Usual care", "Diet", "Diet + exercise"]
ARM_COLOURS = dict(zip(ARM_ORDER, sns.color_palette("colorblind", 3)))

def save(fig, name):
    """Save a figure as PNG (300 dpi) in the figures folder."""
    fig.savefig(FIGURES / f"{name}.png", dpi=300, bbox_inches="tight")''',
'''#md
`ARM_COLOURS` fixes one colour per arm, used in every figure so readers can follow the arms throughout.

## 1. Understanding the data

Each row should be **one participant**: baseline characteristics, baseline measurements and six-month
measurements. The questions are in the README: who the participants are, whether the arms are
comparable at baseline, how blood pressure and glucose changed by arm, who was lost to follow-up, and
how the variables relate.

## 2. Import
''',
'''raw = pd.read_csv(RAW / "clinic_study.csv", parse_dates=["baseline_date"])
print(raw.shape)
raw.head()''',
'''#md
## 3. Exploration
''',
'''raw.info()''',
'''raw.describe().round(2)''',
'''for col in ["clinic", "sex", "arm", "smoking"]:
    print(col, raw[col].map(repr).value_counts().to_dict(), "\\n")''',
'''#md
`map(repr)` shows each value in quotes, so stray spaces are visible.
''',
'''print("fully duplicated rows:", raw.duplicated().sum())
print("repeated IDs:", raw["participant"].duplicated().sum())
print("ages outside 18-100:", raw.loc[~raw["age_years"].between(18, 100), "age_years"].tolist())
print("heights above 3 m:", raw.loc[raw["height_m"] > 3, "height_m"].tolist())
print("missing values:", raw.isna().sum()[raw.isna().sum() > 0].to_dict())''',
'''#md
### Problems found

| # | problem | evidence |
|---|---|---|
| 1 | duplicated rows | 6 rows repeat another row exactly |
| 2 | clinic spelled inconsistently | `east`, and `West ` with a trailing space |
| 3 | sex coded five ways | Male, Female, M, F, female |
| 4 | impossible ages | 0, −1 and 150 |
| 5 | some heights in centimetres | values of 154 to 185 in a column of metres |
| 6 | no six-month values for some participants | 35 missing in both `sbp_6m` and `glucose_6m` |

The arm and smoking columns are consistent. `unknown` is a real smoking category, recorded as such,
not a missing value to fill.

## 4. Cleaning

Each step changes a copy and is checked straight away.
''',
'''df = raw.copy()

# 1. duplicates
df = df.drop_duplicates()
assert df["participant"].is_unique

# 2. clinic
df["clinic"] = df["clinic"].str.strip().str.title()

# 3. sex
df["sex"] = df["sex"].str.strip().str.lower().map({"male": "Male", "m": "Male", "female": "Female", "f": "Female"})
assert df["sex"].notna().all()

print(len(raw), "->", len(df), "rows")
print(df["clinic"].value_counts().to_dict(), df["sex"].value_counts().to_dict())''',
'''#md
**Ages (problem 4).** Ages of 0, −1 and 150 cannot be corrected from the data (the true age is
unknown), so they are set to missing. The participants stay in the dataset, because their other
measurements are valid.
''',
'''bad_age = ~df["age_years"].between(18, 100)
print(df.loc[bad_age, ["participant", "age_years"]])
df.loc[bad_age, "age_years"] = np.nan''',
'''#md
**Heights (problem 5).** Values above 3 can only be centimetres (all are 1.5-1.9 m once divided by
100), so they are converted rather than discarded.
''',
'''cm = df["height_m"] > 3
print(df.loc[cm, ["participant", "height_m"]])
df.loc[cm, "height_m"] = df.loc[cm, "height_m"] / 100
assert df["height_m"].between(1.3, 2.2).all()''',
'''#md
**Six-month values (problem 6).** Missing follow-up is not an error to fix: these participants did not
return. They are kept, and flagged so they can be compared with those who did.

**Types.** Text columns with a fixed set of values become ordered categories so that tables and
figures follow a sensible order.
''',
'''df["arm"] = pd.Categorical(df["arm"], categories=ARM_ORDER, ordered=True)
df["smoking"] = pd.Categorical(df["smoking"], categories=["never", "former", "current", "unknown"], ordered=True)
df.dtypes''',
'''#md
### Cleaning log

| problem | decision | rows affected |
|---|---|---|
| duplicated rows | removed | 6 |
| clinic spelling | stripped spaces, title case | 39 |
| sex codes | mapped to Male / Female | 81 |
| impossible ages | set to missing | 5 |
| heights in cm | divided by 100 | 4 |
| no six-month values | kept; flagged as not completed | 35 |
''',
'''print("clinic changed:", (raw.drop_duplicates()["clinic"] != df["clinic"]).sum())
print("sex changed:   ", (raw.drop_duplicates()["sex"] != df["sex"]).sum())''',
'''#md
## 5. Derived variables
''',
'''df["bmi"] = (df["weight_kg"] / df["height_m"] ** 2).round(1)
df["bmi_class"] = pd.cut(df["bmi"], [0, 18.5, 25, 30, 100], right=False,
                         labels=["Underweight", "Normal", "Overweight", "Obese"])
df["age_group"] = pd.cut(df["age_years"], [18, 35, 50, 65, 101], right=False,
                         labels=["18-34", "35-49", "50-64", "65+"])
df["completed"] = df["sbp_6m"].notna() & df["glucose_6m"].notna()
df["sbp_change"] = df["sbp_6m"] - df["sbp_baseline"]
df["glucose_change"] = (df["glucose_6m"] - df["glucose_baseline"]).round(2)
df["hypertensive_baseline"] = df["sbp_baseline"] >= 140

df[["participant", "bmi", "bmi_class", "age_group", "completed", "sbp_change", "glucose_change"]].head()''',
'''#md
## 6. Descriptive statistics

### Table 1: participant characteristics by arm

A "Table 1" describes who is in each group. With random allocation the arms should look similar;
large differences would complicate any comparison of outcomes.
''',
'''def mean_sd(s):
    return f"{s.mean():.1f} ({s.std():.1f})"

def n_pct(s, value):
    return f"{(s == value).sum()} ({(s == value).mean() * 100:.0f}%)"

def describe_group(g):
    return pd.Series({
        "N": f"{len(g)}",
        "Age, years: mean (SD)": mean_sd(g["age_years"]),
        "Female: n (%)": n_pct(g["sex"], "Female"),
        "BMI: mean (SD)": mean_sd(g["bmi"]),
        "Current smoker: n (%)": n_pct(g["smoking"], "current"),
        "SBP, mmHg: mean (SD)": mean_sd(g["sbp_baseline"]),
        "SBP ≥ 140: n (%)": n_pct(g["hypertensive_baseline"], True),
        "Glucose, mmol/L: mean (SD)": mean_sd(g["glucose_baseline"]),
    })

table1 = pd.concat({arm: describe_group(g) for arm, g in df.groupby("arm", observed=True)}, axis=1)
table1["All"] = describe_group(df)
table1''',
'''#md
The arms are similar in size and in age, sex, BMI, smoking and baseline measurements, as expected from
random allocation. Mean baseline systolic blood pressure is around 142 mmHg, and more than half of the
participants start at or above 140.

### Table 2: outcomes in participants who completed follow-up
''',
'''completers = df[df["completed"]]
table2 = completers.groupby("arm", observed=True).agg(
    n=("participant", "size"),
    sbp_baseline=("sbp_baseline", "mean"),
    sbp_6m=("sbp_6m", "mean"),
    sbp_change=("sbp_change", "mean"),
    sbp_change_sd=("sbp_change", "std"),
    glucose_baseline=("glucose_baseline", "mean"),
    glucose_6m=("glucose_6m", "mean"),
    glucose_change=("glucose_change", "mean"),
    glucose_change_sd=("glucose_change", "std"),
).round(2)
table2''',
'''#md
A rough 95% confidence interval for each mean change (mean ± 1.96 × SD / √n) gives a sense of
precision:
''',
'''ci = completers.groupby("arm", observed=True)[["sbp_change", "glucose_change"]].agg(["mean", "sem"])
for col in ["sbp_change", "glucose_change"]:
    ci[(col, "low")] = ci[(col, "mean")] - 1.96 * ci[(col, "sem")]
    ci[(col, "high")] = ci[(col, "mean")] + 1.96 * ci[(col, "sem")]
ci.round(2)''',
'''#md
### Table 3: who completed follow-up?
''',
'''follow = df.groupby("completed").agg(
    n=("participant", "size"),
    age=("age_years", "mean"),
    pct_female=("sex", lambda s: (s == "Female").mean() * 100),
    bmi=("bmi", "mean"),
    sbp_baseline=("sbp_baseline", "mean"),
    glucose_baseline=("glucose_baseline", "mean"),
).round(1)
follow.index = follow.index.map({True: "completed", False: "not completed"})
print(pd.crosstab(df["arm"], df["completed"], margins=True))
follow''',
'''#md
## 7. Visualisations

### Figure 1: who are the participants?
''',
'''fig, axes = plt.subplots(1, 3, figsize=(13, 3.8), layout="constrained")
sns.histplot(data=df, x="age_years", bins=20, ax=axes[0])
axes[0].set(xlabel="Age (years)", ylabel="Participants", title="A. Age")
sns.histplot(data=df, x="bmi", bins=20, ax=axes[1])
for cut in (25, 30):
    axes[1].axvline(cut, color="0.3", linestyle=":", linewidth=1)
axes[1].set(xlabel="BMI (kg/m²)", ylabel="", title="B. BMI (lines at 25 and 30)")
sns.countplot(data=df, y="clinic", hue="sex", palette="colorblind", ax=axes[2])
axes[2].set(xlabel="Participants", ylabel="", title="C. Clinic and sex")
for ax in axes:
    ax.set_title(ax.get_title(), loc="left")
save(fig, "fig1_participants")
plt.show()''',
'''#md
### Figure 2: baseline comparison of the arms
''',
'''fig, axes = plt.subplots(1, 2, figsize=(11, 4), layout="constrained")
for ax, col, label in [(axes[0], "sbp_baseline", "Systolic BP at baseline (mmHg)"),
                       (axes[1], "glucose_baseline", "Fasting glucose at baseline (mmol/L)")]:
    sns.boxplot(data=df, x="arm", y=col, hue="arm", palette=ARM_COLOURS, showfliers=False, width=0.55, ax=ax)
    sns.stripplot(data=df, x="arm", y=col, color="0.3", size=2.5, alpha=0.4, ax=ax)
    ax.set(xlabel="", ylabel=label)
axes[0].set_title("A. Systolic blood pressure", loc="left")
axes[1].set_title("B. Fasting glucose", loc="left")
save(fig, "fig2_baseline_by_arm")
plt.show()''',
'''#md
### Figure 3: change over six months by arm
''',
'''fig, axes = plt.subplots(1, 2, figsize=(11, 4), layout="constrained")
for ax, col, label in [(axes[0], "sbp_change", "Change in systolic BP (mmHg)"),
                       (axes[1], "glucose_change", "Change in glucose (mmol/L)")]:
    sns.pointplot(data=completers, x="arm", y=col, hue="arm", palette=ARM_COLOURS,
                  errorbar=("ci", 95), capsize=0.15, markersize=8, ax=ax)
    ax.axhline(0, color="0.4", linewidth=1)
    ax.set(xlabel="", ylabel=label)
axes[0].set_title("A. Systolic BP", loc="left")
axes[1].set_title("B. Glucose", loc="left")
fig.suptitle("Mean change from baseline to six months, with 95% confidence intervals (completers)")
save(fig, "fig3_change_by_arm")
plt.show()''',
'''#md
### Figure 4: individual changes in blood pressure

Means hide how much individuals vary. Each line is one participant, from baseline to six months; the
thick line is the arm mean.
''',
'''long = completers.melt(id_vars=["participant", "arm"], value_vars=["sbp_baseline", "sbp_6m"],
                       var_name="time", value_name="sbp")
long["time"] = long["time"].map({"sbp_baseline": "Baseline", "sbp_6m": "6 months"})

g = sns.FacetGrid(long, col="arm", col_order=ARM_ORDER, height=3.6, aspect=0.9, sharey=True)
g.map_dataframe(sns.lineplot, x="time", y="sbp", units="participant", estimator=None,
                color="0.8", linewidth=0.5)
for ax, arm in zip(g.axes.flat, ARM_ORDER):
    m = long[long["arm"] == arm].groupby("time", sort=False)["sbp"].mean()
    ax.plot(m.index, m.values, color=ARM_COLOURS[arm], linewidth=3, marker="o")
g.set_titles("{col_name}")
g.set_axis_labels("", "Systolic BP (mmHg)")
save(g.figure, "fig4_individual_sbp")
plt.show()''',
'''#md
### Figure 5: relationships between variables
''',
'''cols = {"age_years": "Age", "bmi": "BMI", "sbp_baseline": "SBP", "glucose_baseline": "Glucose",
        "sbp_change": "SBP change", "glucose_change": "Glucose change"}
corr = df[list(cols)].rename(columns=cols).corr()
mask = np.triu(np.ones_like(corr, dtype=bool))

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), layout="constrained")
sns.heatmap(corr, mask=mask, cmap="vlag", center=0, vmin=-1, vmax=1, annot=True, fmt=".2f",
            square=True, linewidths=0.5, cbar_kws={"shrink": 0.8}, ax=axes[0])
axes[0].set_title("A. Correlations (Pearson r)", loc="left")
axes[0].grid(False)
sns.scatterplot(data=completers, x="sbp_change", y="glucose_change", hue="arm", style="arm",
                palette=ARM_COLOURS, hue_order=ARM_ORDER, s=18, alpha=0.7, ax=axes[1])
axes[1].set(xlabel="Change in systolic BP (mmHg)", ylabel="Change in glucose (mmol/L)")
axes[1].set_title("B. Change in glucose against change in SBP", loc="left")
axes[1].legend(title=None, frameon=False)
save(fig, "fig5_relationships")
plt.show()''',
'''#md
### Figure 6: loss to follow-up
''',
'''fig, axes = plt.subplots(1, 2, figsize=(11, 3.8), layout="constrained")
rate = (1 - df.groupby("arm", observed=True)["completed"].mean()) * 100
axes[0].bar(rate.index, rate.values, color=[ARM_COLOURS[a] for a in rate.index])
axes[0].set(ylabel="Not followed up (%)", title="A. Loss to follow-up by arm")
sns.kdeplot(data=df, x="sbp_baseline", hue=df["completed"].map({True: "completed", False: "not completed"}),
            common_norm=False, fill=True, alpha=0.3, palette="colorblind", ax=axes[1])
axes[1].set(xlabel="Systolic BP at baseline (mmHg)", title="B. Baseline SBP by follow-up status")
axes[1].get_legend().set_title(None)
for ax in axes:
    ax.set_title(ax.get_title(), loc="left")
save(fig, "fig6_follow_up")
plt.show()''',
'''sorted(p.name for p in FIGURES.glob("*.png"))''',
'''#md
## 8. Findings
''',
'''n = len(df); n_comp = int(df["completed"].sum())
chg = completers.groupby("arm", observed=True)[["sbp_change", "glucose_change"]].mean()
r_changes = completers["sbp_change"].corr(completers["glucose_change"])
r_within = completers.groupby("arm", observed=True)[["sbp_change", "glucose_change"]].corr().xs("sbp_change", level=1)["glucose_change"]
print(f"{n} participants; {n_comp} ({n_comp / n:.0%}) completed follow-up")
print(chg.round(2))
print(f"SBP change vs glucose change: r = {r_changes:.2f} overall; within arms:", r_within.round(2).to_dict())''',
'''#md
**1. Participants.** After removing six duplicate rows, the study has 480 participants across three
clinics, with a broad adult age range and roughly equal numbers of men and women. Average BMI is in the
overweight range, and baseline systolic blood pressure averages about 142 mmHg (Table 1, Figure 1).

**2. Baseline comparability.** The three arms are similar in age, sex, BMI, smoking, blood pressure
and glucose at baseline (Table 1, Figure 2), so differences at six months are unlikely to come from
differences in who was in each arm.

**3. Change over six months.** Among completers, systolic blood pressure barely changed under *Usual
care* (mean −0.5 mmHg; the 95% confidence interval includes zero), fell by about 3 mmHg in the *Diet*
arm and by about 9 mmHg in the *Diet + exercise* arm (Table 2, Figure 3A). Glucose followed the same
order: essentially no change under usual care, a fall of about 0.4 mmol/L with diet, and about
0.8 mmol/L with diet and exercise (Figure 3B). None of the three arms' confidence intervals overlap for
either outcome. Figure 4 shows that individual changes still vary widely within every arm: some
participants' blood pressure rose even in the arm with the largest average fall.

**4. Follow-up.** 35 participants (7%) have no six-month measurements. Fewer were lost from the
*Diet + exercise* arm (7 of 167, 4%) than from the other two (8-10%) (Figure 6A). Those who did not
return look similar to completers at baseline (Table 3, Figure 6B), which makes serious bias from loss
to follow-up less likely, though it cannot be ruled out.

**5. Relationships.** The baseline variables are almost unrelated to each other in these data: all
their correlations are close to zero (Figure 5A). The one clear correlation is between the two
*changes* (r about 0.2): participants whose blood pressure fell more also tended to have larger falls in
glucose. But within each arm this correlation disappears (r close to 0). It arises only because both
outcomes fall most in the *Diet + exercise* arm and least under usual care, so the arms form three
clusters (Figure 5B). This is the same lesson as Simpson's paradox in module 8: always check whether a
grouping variable explains an overall correlation.

### Limitations

- the data are **simulated** for teaching; real studies are messier and effects smaller
- the analysis is **descriptive**: the differences between arms would need a formal statistical test
  (for example, a regression of six-month SBP on arm, adjusted for baseline) before drawing conclusions
- outcome comparisons use **completers only**; methods for missing data are beyond this course
- five implausible ages were set to missing and four heights converted from centimetres; other errors
  that look plausible cannot be detected
- six months is a short follow-up; whether changes last is unknown

## 9. Export
''',
'''export_cols = ["participant", "clinic", "sex", "age_years", "age_group", "arm", "baseline_date",
               "weight_kg", "height_m", "bmi", "bmi_class", "smoking",
               "sbp_baseline", "sbp_6m", "sbp_change", "glucose_baseline", "glucose_6m", "glucose_change",
               "hypertensive_baseline", "completed"]
df[export_cols].to_csv(PROCESSED / "clinic_study_clean.csv", index=False)
table1.to_csv(PROCESSED / "clinic_study_table1.csv")
table2.to_csv(PROCESSED / "clinic_study_table2.csv")

check = pd.read_csv(PROCESSED / "clinic_study_clean.csv")
print(check.shape)
check.head(3)''',
'''#md
The cleaned dataset, the two summary tables and six figures are now saved. Rerunning this notebook
from the raw file reproduces all of them exactly.
''',
],
["The brief: `README.md` in this folder",
 "[STROBE checklist for reporting observational studies](https://www.strobe-statement.org/)",
 "[Seaborn: visualising statistical relationships](https://seaborn.pydata.org/tutorial/relational.html)"])
print("capstone written")
