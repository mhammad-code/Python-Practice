import pandas as pd

data = {
    "Name": ["  Ali Khan  ", "SARA", "Ahmed Ali", "hamza"],
    "Email": [
        "Ali@gmail.com",
        "SARA@Yahoo.COM",
        "ahmed123@gmail.com",
        "hamza@gmail.com"
    ],
    "City": ["Lahore", "Karachi", "Islamabad", "Multan"]
}

df = pd.DataFrame(data)

print(df)
df["Name"]=df["Name"].str.strip()
print(df)

df["Name"]=df["Name"].str.lower()
print(df)
df["City"] = df["City"].str.upper()

print(df)
df["Name"] = df["Name"].str.capitalize()

print(df)
df["Name"] = df["Name"].str.title()

print(df)
df["Name"] = df["Name"].str.title()

print(df)
df["First_Name"] = df["Name"].str.split().str[0]
df["Last_Name"] = df["Name"].str.split().str[1]

print(df)
df["Full"] = df["Name"].str.cat(df["City"], sep=" - ")

print(df)