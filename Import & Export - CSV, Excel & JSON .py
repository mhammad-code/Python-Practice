import pandas as pd

df = pd.read_csv("currency.csv")

print(df)


df = pd.read_csv("currency.csv")

print(df.head())

df = pd.read_csv("currency.csv")

print(df.to_string())
print(df.info())

import pandas as pd

# ==============================
# 1. Read CSV File
# ==============================
df = pd.read_csv("currency.csv")

print("=" * 60)
print("Original Data")
print("=" * 60)
print(df)

# ==============================
# 2. First & Last Rows
# ==============================
print("\nFirst 5 Rows")
print(df.head())

print("\nFirst 10 Rows")
print(df.head(10))

print("\nLast 5 Rows")
print(df.tail())

print("\nLast 10 Rows")
print(df.tail(10))

# ==============================
# 3. Shape
# ==============================
print("\nShape of Dataset")
print(df.shape)

print("\nNumber of Rows")
print(df.shape[0])

print("\nNumber of Columns")
print(df.shape[1])

# ==============================
# 4. Column Names
# ==============================
print("\nColumn Names")
print(df.columns)

# ==============================
# 5. Data Types
# ==============================
print("\nData Types")
print(df.dtypes)

# ==============================
# 6. Dataset Information
# ==============================
print("\nInformation")
print(df.info())

# ==============================
# 7. Statistical Summary
# ==============================
print("\nStatistics")
print(df.describe())

# ==============================
# 8. Missing Values
# ==============================
print("\nMissing Values")
print(df.isnull())

print("\nMissing Values Count")
print(df.isnull().sum())

# ==============================
# 9. Duplicate Values
# ==============================
print("\nDuplicate Rows")
print(df.duplicated())

print("\nNumber of Duplicate Rows")
print(df.duplicated().sum())

# ==============================
# 10. Display Complete Data
# ==============================
print("\nComplete Dataset")
print(df.to_string())

# ==============================
# 11. Access Columns
# Replace with your actual column names
# ==============================
# print(df["Currency"])
# print(df["Country"])
# print(df["Rate"])

# Multiple Columns
# print(df[["Currency","Rate"]])

# ==============================
# 12. Access Rows
# ==============================
print("\nFirst Row")
print(df.iloc[0])

print("\nSecond Row")
print(df.iloc[1])

print("\nRows 0 to 4")
print(df.iloc[0:5])

# ==============================
# 13. Sorting
# Replace "Rate" with a numeric column
# ==============================
# print(df.sort_values(by="Rate"))
# print(df.sort_values(by="Rate", ascending=False))

# ==============================
# 14. Filtering
# Replace according to your dataset
# ==============================
# print(df[df["Rate"] > 100])

# ==============================
# 15. Unique Values
# ==============================
# print(df["Country"].unique())

# ==============================
# 16. Number of Unique Values
# ==============================
# print(df["Country"].nunique())

# ==============================
# 17. Value Counts
# ==============================
# print(df["Country"].value_counts())

# ==============================
# 18. Rename Columns
# ==============================
# df.rename(columns={"Rate":"Exchange Rate"}, inplace=True)

# ==============================
# 19. Add New Column
# ==============================
df["Serial No"] = range(1, len(df)+1)

print("\nDataset with New Column")
print(df.head())

# ==============================
# 20. Delete Column
# ==============================
# df.drop("Serial No", axis=1, inplace=True)

# ==============================
# 21. Fill Missing Values
# ==============================
# df.fillna(0, inplace=True)

# ==============================
# 22. Drop Missing Values
# ==============================
# df.dropna(inplace=True)

# ==============================
# 23. Save CSV
# ==============================
df.to_csv("currency_new.csv", index=False)

print("\nNew CSV File Saved Successfully!")

# ==============================
# 24. Save Excel
# ==============================
df.to_excel("currency.xlsx", index=False)

print("Excel File Saved Successfully!")

# ==============================
# 25. Save JSON
# ==============================
df.to_json("currency.json",
           orient="records",
           indent=4)

print("JSON File Saved Successfully!")

# ==============================
# 26. Read Excel
# ==============================
excel_df = pd.read_excel("currency.xlsx")

print("\nReading Excel")
print(excel_df.head())

# ==============================
# 27. Read JSON
# ==============================
json_df = pd.read_json("currency.json")

print("\nReading JSON")
print(json_df.head())