# Sales Data Analysis & EDA

## 📌 Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on a sales dataset using Python.

The main goal is to understand the dataset, identify missing and invalid values, detect duplicate records and outliers, explore relationships between variables, and prepare a clean dataset for further analysis or machine learning.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 📂 Dataset

The dataset contains sales-related information such as:

- Units Sold
- Price Per Unit
- Discount Percentage
- Advertising Spend
- Revenue

## 🔍 EDA Performed

The following analysis was performed:

1. Dataset inspection
2. Shape and structure analysis
3. Statistical summary
4. Missing value detection
5. Duplicate row detection
6. Invalid value detection
7. Outlier detection using boxplot
8. Units Sold distribution analysis
9. Revenue distribution analysis
10. Advertising Spend vs Revenue analysis
11. Discount Percentage vs Revenue analysis
12. Units Sold vs Revenue analysis
13. Correlation heatmap

## 🧹 Data Cleaning

The dataset was cleaned by:

- Removing duplicate rows
- Handling missing values using median imputation
- Identifying and handling negative units sold
- Identifying and handling negative prices
- Handling invalid discount percentages
- Creating new features for analysis

## ⚙️ Feature Engineering

Two new features were created:

- `gross_sales` = Units Sold × Price Per Unit
- `discount_amount` = Gross Sales × Discount Percentage / 100

## 📊 Visualizations

The project includes visualizations for:

- Revenue outliers
- Units Sold distribution
- Revenue distribution
- Advertising Spend vs Revenue
- Discount Percentage vs Revenue
- Units Sold vs Revenue
- Correlation between numerical features

## 📁 Project Structure

```text
thiru/
│
├── 04_sales_data.csv
├── sales_data_eda.py
├── cleaned_sales_data.csv
└── README.md
