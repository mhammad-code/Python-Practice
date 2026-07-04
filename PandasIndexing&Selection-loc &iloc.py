import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Hamza", "Ayesha"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}
df=pd.DataFrame(data)
print(df)
i=df.loc[1:2,['Name','Marks']]
print(i)

j=df.iloc[0:2,0:3]
print(j)

import pandas as pd

df = pd.read_csv("currency.csv")

print("Complete Data")
print(df)

print("\nloc - First Row")
print(df.loc[0])

print("\nloc - Country and Rate")
print(df.loc[:, ["Country", "Rate"]])

print("\niloc - First Row")
print(df.iloc[0])

print("\niloc - First Two Columns")
print(df.iloc[:, 0:2])

print("\nSpecific Value")
print(df.loc[2, "Currency"])

print("\nSpecific Value using iloc")
print(df.iloc[2, 1])

print("\nCountries with Rate > 1")
print(df[df["Rate"] > 1])