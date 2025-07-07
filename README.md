# Machine Learning Project: Predicting Student Writing Scores

---

**Course:** Optimization and Machine Learning M  
**Instructor:** Prof. Andrea Lodi  
**Date:** 3rd-10th of July 2025

This repository contains a Jupyter notebook (`test_scores.ipynb`) that walks through a complete machine learning workflow. We are using the “StudentsPerformance” dataset to predict students’ writing exam scores.

---

## 🔍 Project Overview

**Objective:**  
Build and evaluate a regression model to predict a student’s writing score based on demographic and academic features.

**Five‐Task Workflow:**

1. **Data Exploration & Preprocessing**
   - Load dataset
   - Handle missing values & outliers
   - Visualize distributions (histograms, boxplots, scatter plots, heatmaps)
2. **Feature Selection & Engineering**
   - Identify relevant predictors
   - Create ordinal mappings and derived features (e.g., skill differences)
   - Encode categorical variables
3. **Model Development & Evaluation**
   - Split into train/test sets
   - Compare Linear Regression, Decision Tree, Random Forest, XGBoost, Neutral Network via 5-fold CV
   - Hyperparameter tuning with `GridSearchCV`
4. **Prediction & Interpretation**
   - Generate final predictions
   - Report RMSE, MAE, R²
   - Plot Actual vs. Predicted & Residuals
   - Examine feature coefficients / importances
5. **Conclusion & Recommendations**
   - Summarize key findings
   - Suggest areas for improvement (e.g., SHAP analysis, additional data)

---

## 📂 Repository Structure

```bash
├── data/
│ └── StudentsPerformance.csv
├── autogluon_models/   # The models from autogluon gets stored here
│ └──ag_yyyymmdd_hhmmss
│ └──...
├── test_scores.ipynb   # Main analysis notebook
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ⚙️ Environment Setup

1. **Python Version**

   - Tested on **Python 3.12**

2. **Create & Activate Virtual Environment**
   From the root of the project:

   ```bash
   # Make virtual environment
   python3.12 -m venv .venv

   # Activate enviroment:
   # 1. MacOS / Linux
   source venv/bin/activate

   # 2. Windows (PowerShell)
   ./venv/Scripts/Activate.ps1

   # 3. Windows (CMD)
   venv/Scripts/Activate.bat
   ```

3. **Install dependencies**
   - python.exe -m pip install --upgrade pip
   - pip install -r requirements.txt

---

## 📊 Results & Interpretation

Best Model: Linear Regression achieved the lowest Test RMSE (~3.87) and highest R² (~0.94).

Key Predictors: Reading score had the strongest positive coefficient, demographic features had smaller effects.

Residual Analysis: Errors are evenly distributed around zero with a few outliers, indicating good model fit without major bias.

---

Made by:
Åke Sjursen Hauge & Andreas Omholt Olsen
