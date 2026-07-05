import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Hamza"],
    "Age": [20, None, 22, None],
    "City": ["Lahore", None, "Karachi", "Islamabad"]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

print("\nMissing Values")
print(df.isnull())

print("\nCount Missing")
print(df.isnull().sum())

print("\nTotal Missing")
print(df.isnull().sum().sum())

print("\nFill Age with Mean")
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

print("\nFill City with Unknown")
df["City"] = df["City"].fillna("Unknown")
print(df)

print("\nRemove Missing Rows")
print(df.dropna())

print("\nForward Fill")
print(df.ffill())

print("\nBackward Fill")
print(df.bfill())