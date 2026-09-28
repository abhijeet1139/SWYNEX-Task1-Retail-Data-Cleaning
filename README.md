# Retail Store Sales — Data Cleaning and Preparation

## SWYNEX Technologies Internship — Task 1

### Objective
Clean and prepare a public retail sales dataset by identifying missing values, duplicate records, incorrect data types, and inconsistent values.

## Dataset
- **Dataset:** Retail Store Sales — Dirty for Data Cleaning
- **Raw records:** 12,575
- **Raw columns:** 11
- **Tool:** Python / Pandas
- **Source:** Kaggle — Retail Store Sales: Dirty for Data Cleaning
- **Source link:** https://www.kaggle.com/datasets/ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning

## Issues Identified

### Missing Values
- `Item`: 1,213
- `Price Per Unit`: 609
- `Quantity`: 604
- `Total Spent`: 604
- `Discount Applied`: 4,199

### Duplicate Records
The raw dataset contains **0 exact duplicate rows**. No artificial duplicates were created.

### Incorrect Data Types
- `Price Per Unit`, `Quantity`, and `Total Spent` were converted to numeric.
- `Transaction Date` was converted to datetime.

### Inconsistent Values
- Leading/trailing whitespace was removed from text values.
- `Discount Applied` was standardized to `Yes`, `No`, or `Unknown`.
- Missing `Item` values were labeled `Unknown`.

## Cleaning Performed
1. Preserved the original raw dataset.
2. Checked missing values and exact duplicates.
3. Standardized text whitespace.
4. Converted numeric columns to numeric types.
5. Reconstructed missing numeric values only when mathematically determinable:
   - `Total Spent = Price Per Unit × Quantity`
   - `Price Per Unit = Total Spent ÷ Quantity`
   - `Quantity = Total Spent ÷ Price Per Unit`
6. Filled missing `Item` values with `Unknown`.
7. Filled missing `Discount Applied` values with `Unknown`.
8. Standardized discount values.
9. Converted `Transaction Date` to datetime.
10. Removed rows where both `Quantity` and `Total Spent` were missing because those values could not be reliably reconstructed.
11. Removed exact duplicate records if present.
12. Performed final validation.

## Final Dataset
- **Final records:** 11,971
- **Final columns:** 11
- **Rows removed as unrecoverable:** 604
- **Remaining missing values:** 0
- **Remaining exact duplicates:** 0

## Project Structure
```text
SWYNEX_Task1_Retail_Data_Cleaning/
├── data/
│   ├── raw/
│   │   └── retail_store_sales_raw.csv
│   └── cleaned/
│       └── retail_store_sales_cleaned.csv
├── notebook/
│   └── data_cleaning.ipynb
├── data_cleaning.py
├── requirements.txt
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
python data_cleaning.py
```

Or open `notebook/data_cleaning.ipynb` in Jupyter Notebook.

## Validation
The cleaned dataset was checked for remaining missing values, exact duplicates, correct numeric types, correct date type, and the transaction calculation relationship.

## Author
**Abhijeet Pawar**

Data Analyst Internship Project — 2026
