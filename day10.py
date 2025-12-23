import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [23, 30, 35, 28, 40],
    "salary": [40000, 50000, 70000, 48000, 90000],
    "department": ["HR", "IT", "IT", "Finance", "Management"]
})

print(df)

# task 10.1
df["salary_in_lakhs"] = df["salary"] / 100000
df["age_plus_5"] = df["age"] + 5
print(df)

# task 10.2
df["salary"] = df["salary"] * 1.1
print(df)

# task 10.3
def senior(age):
    if age >= 35:
        return "Senior"
    elif 28 <= age < 35:
        return "Mid"
    else:
        return "Junior"

df["seniority"] = df["age"].apply(senior)

# task 10.4
print(df.sort_values("salary",ascending= False))
print(df.sort_values("age"))

# task 10.5
print(df["salary"].mean())
print(df["age"].max())
print(df["salary"].sum())

# task 10.6
print(df.groupby("department")["salary"].mean())