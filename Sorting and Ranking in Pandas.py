import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Hamza", "Ayesha"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print(df)
print(df.sort_values("Marks"))
print(df.sort_values("Marks", ascending=False))
print(df.sort_values(by=["Age", "Marks"]))
print(df.sort_values(
    by=["Department", "Marks"],
    ascending=[True, False]
))
df["Rank"] = df["Marks"].rank()

print(df)
df["Rank"] = df["Marks"].rank(ascending=False)

print(df)
import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Hamza", "Ayesha"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

# Sort by Marks
print("\nSort by Marks")
print(df.sort_values("Marks"))

# Sort by Age then Marks
print("\nSort by Age and Marks")
print(df.sort_values(by=["Age", "Marks"]))

# Sort by Index
print("\nSort by Index Descending")
print(df.sort_index(ascending=False))

# Overall Ranking
df["Rank"] = df["Marks"].rank(ascending=False)

print("\nOverall Ranking")
print(df)

# Department Ranking
df["Department Rank"] = df.groupby("Department")["Marks"].rank(ascending=False)

print("\nRanking Within Department")
print(df)