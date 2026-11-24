# Capstone project: exploratory analysis of a clinical study dataset

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
