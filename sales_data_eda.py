import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("04_sales_data.csv")

# 1. Basic inspection
print("First 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

# 2. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 4. Invalid values
print("\nInvalid Values:")

print("Negative Units Sold:")
print((df["units_sold"] < 0).sum())

print("Negative Price:")
print((df["price_per_unit"] < 0).sum())

print("Invalid Discount Percentage:")
print(((df["discount_percent"] < 0) | (df["discount_percent"] > 100)).sum())

# 5. Revenue outliers
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["revenue"])
plt.title("Revenue Outliers")
plt.show()

# 6. Units sold distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["units_sold"], kde=True)
plt.title("Units Sold Distribution")
plt.xlabel("Units Sold")
plt.ylabel("Count")
plt.show()

# 7. Revenue distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["revenue"], kde=True)
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Count")
plt.show()

# 8. Advertising Spend vs Revenue
plt.figure(figsize=(8, 5))
sns.scatterplot(x="advertising_spend", y="revenue", data=df)
plt.title("Advertising Spend vs Revenue")
plt.xlabel("Advertising Spend")
plt.ylabel("Revenue")
plt.show()

# 9. Discount vs Revenue
plt.figure(figsize=(8, 5))
sns.scatterplot(x="discount_percent", y="revenue", data=df)
plt.title("Discount Percentage vs Revenue")
plt.xlabel("Discount Percentage")
plt.ylabel("Revenue")
plt.show()

# 10. Units Sold vs Revenue
plt.figure(figsize=(8, 5))
sns.scatterplot(x="units_sold", y="revenue", data=df)
plt.title("Units Sold vs Revenue")
plt.xlabel("Units Sold")
plt.ylabel("Revenue")
plt.show()

# 11. Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 12. Data Cleaning

# Remove duplicates
df = df.drop_duplicates()

# Replace invalid values with NaN
df.loc[df["units_sold"] < 0, "units_sold"] = np.nan
df.loc[df["price_per_unit"] < 0, "price_per_unit"] = np.nan

df.loc[
    (df["discount_percent"] < 0) |
    (df["discount_percent"] > 100),
    "discount_percent"
] = np.nan

# Fill missing values with median
for column in ["units_sold", "price_per_unit",
               "discount_percent", "advertising_spend"]:
    df[column] = df[column].fillna(df[column].median())

# 13. Feature Engineering

df["gross_sales"] = df["units_sold"] * df["price_per_unit"]

df["discount_amount"] = (
    df["gross_sales"] * df["discount_percent"] / 100
)

# 14. Final dataset check
print("\nAfter Cleaning:")
print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFinal Shape:")
print(df.shape)

# 15. Separate X and y
X = df.drop("revenue", axis=1)
y = df["revenue"]

print("\nX Shape:")
print(X.shape)

print("\ny Shape:")
print(y.shape)

# 16. Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned sales dataset saved successfully!")