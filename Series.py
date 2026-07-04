import pandas as pd
s = pd.Series([10,20,30,40])

print(s)
s = pd.Series([10,20,30], index=["A","B","C"])

print(s)
student = {
    "Ali":85,
    "Ahmed":90,
    "Sara":95
}

s = pd.Series(student)

print(s)


marks = pd.Series(
    [85, 90, 78, 92, 88],
    index=["Ali", "Sara", "Ahmed", "Ayesha", "Hamza"]
)

print("Series:")
print(marks)

print("\nMaximum:", marks.max())
print("Minimum:", marks.min())
print("Average:", marks.mean())
print("Sum:", marks.sum())
print("Total Students:", marks.size)

print("\nSorted:")
print(marks.sort_values())

print("\nUnique Values:")
print(marks.unique())

print("\nStatistical Summary:")
print(marks.describe())

print("\nStudents scoring above 85:")
print(marks[marks > 85])