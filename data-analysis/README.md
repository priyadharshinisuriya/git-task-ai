# HR Employee Attrition Analysis

## Project Overview
Analysis of the IBM HR Analytics Employee Attrition dataset to understand why employees leave.

## Dataset
IBM HR Analytics Employee Attrition & Performance (Kaggle): 1,470 rows, 35 columns, no missing values or duplicates.

## Business Questions
1. Which department has the highest attrition rate?
2. Does overtime affect whether employees leave?
3. How does monthly income compare between leavers and stayers?
4. Which age group or years-at-company band has the most attrition?
5. Does job satisfaction or work-life balance relate to attrition?

## Project Structure
- `data/` - raw CSV file
- `analysis.ipynb` - first data summary and questions

## How to run
1. Install Python 3.10 or newer.
2. Install the libraries: `pip install -r requirements.txt`
3. Open `data-cleaning.ipynb`, then `visualisations.ipynb`, and choose Run All.
4. Charts are saved to `reports/figures/`.
5. Export the report: `python -m jupyter nbconvert --to html visualisations.ipynb`