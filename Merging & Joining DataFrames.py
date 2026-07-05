import pandas as pd

students = pd.DataFrame({
    "ID": [101,102,103,104],
    "Name": ["Ali","Sara","Ahmed","Hamza"]
})

print(students)
marks = pd.DataFrame({
    "ID":[101,102,104,105],
    "Marks":[85,90,88,95]
})

print(marks)
result = pd.merge(students, marks, on="ID")
print(result)
result = pd.merge(students, marks,
                  on="ID",
                  how="left")

print(result)
result = pd.merge(students, marks,
                  on="ID",
                  how="right")

print(result)
result = pd.merge(students,
                  marks,
                  on="ID",
                  how="outer")

print(result)
import pandas as pd

# ----------------------------
# DataFrame 1
# ----------------------------
students = pd.DataFrame({
    "ID": [101,102,103,104],
    "Name": ["Ali","Sara","Ahmed","Hamza"],
    "City": ["Lahore","Karachi","Multan","Faisalabad"]
})

# ----------------------------
# DataFrame 2
# ----------------------------
marks = pd.DataFrame({
    "ID": [101,102,104,105],
    "Marks": [85,90,88,95]
})

print("Students")
print(students)

print("\nMarks")
print(marks)

# ----------------------------
# INNER MERGE
# ----------------------------
print("\nINNER MERGE")
print(pd.merge(students, marks, on="ID"))

# ----------------------------
# LEFT MERGE
# ----------------------------
print("\nLEFT MERGE")
print(pd.merge(students, marks, on="ID", how="left"))

# ----------------------------
# RIGHT MERGE
# ----------------------------
print("\nRIGHT MERGE")
print(pd.merge(students, marks, on="ID", how="right"))

# ----------------------------
# OUTER MERGE
# ----------------------------
print("\nOUTER MERGE")
print(pd.merge(students, marks, on="ID", how="outer"))

# ----------------------------
# DIFFERENT COLUMN NAMES
# ----------------------------
student2 = pd.DataFrame({
    "StudentID":[1,2],
    "Name":["Ali","Sara"]
})

marks2 = pd.DataFrame({
    "ID":[1,2],
    "Marks":[80,90]
})

print("\nDifferent Column Names")
print(pd.merge(student2,
               marks2,
               left_on="StudentID",
               right_on="ID"))

# ----------------------------
# JOIN
# ----------------------------
student3 = pd.DataFrame({
    "Name":["Ali","Sara","Ahmed"]
})

marks3 = pd.DataFrame({
    "Marks":[81,91,71]
})

print("\nJOIN")
print(student3.join(marks3))

# ----------------------------
# CONCAT VERTICAL
# ----------------------------
df1 = pd.DataFrame({
    "Name":["Ali","Sara"]
})

df2 = pd.DataFrame({
    "Name":["Ahmed","Hamza"]
})

print("\nVERTICAL CONCAT")
print(pd.concat([df1,df2], ignore_index=True))

# ----------------------------
# CONCAT HORIZONTAL
# ----------------------------
df3 = pd.DataFrame({
    "Marks":[85,90]
})

print("\nHORIZONTAL CONCAT")
print(pd.concat([df1,df3], axis=1))