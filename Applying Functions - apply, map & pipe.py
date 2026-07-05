import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed", "Hamza"],
    "Math": [80, 90, 70, 85],
    "English": [75, 88, 95, 80]
})

print("Original DataFrame")
print(df)

# -----------------------------
# APPLY
# -----------------------------
df["Math"] = df["Math"].apply(lambda x: x + 5)

# -----------------------------
# MAP
# -----------------------------
df["Name"] = df["Name"].map(str.upper)

# -----------------------------
# Custom Function
# -----------------------------
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    return "Fail"

df["Grade"] = df["Math"].apply(grade)

# -----------------------------
# Row-wise Apply
# -----------------------------
df["Total"] = df.apply(
    lambda row: row["Math"] + row["English"],
    axis=1
)

# -----------------------------
# Pipe Function
# -----------------------------
def add_bonus(data):
    data["English"] += 2
    return data

df = df.pipe(add_bonus)

# -----------------------------
# Method Chaining
# -----------------------------
result = (
    df
    .sort_values("Total", ascending=False)
    .reset_index(drop=True)
)

print("\nFinal DataFrame")
print(result)