import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", None, "David", "Eva"],
    "age": [25, None, 30, 35, None],
    "department": ["HR", "IT", "IT", None, "HR"],
    "salary": [50000, 60000, None, 80000, 70000]
})
# task 15.1.1
print(df.isna())
# task 15.1.2
print(df.isna().sum())
# task 15.1.3
df.info()

# task 15.2.1
df_dropna_any = df.dropna()
print(df_dropna_any)
# task 15.2.2
df_dropna_all = df.dropna(how="all")
print(df_dropna_all)
# task 15.2.3
df_dropna_any_col = df.dropna(axis=1)
print(df_dropna_any_col)

# task 15.3.1
avg_age = df["age"].mean()
df_fillna_avg_age = df["age"].fillna(avg_age)
print(df_fillna_avg_age)
# task 15.3.2
median_salary = df["salary"].median()
df_fillna_median_salary = df["salary"].fillna(median_salary)
print(df_fillna_median_salary)
# task 15.3.3
df_fillna_department = df["department"].fillna("Unknown")
print(df_fillna_department)

# task 15.4.1
avg_age = df["age"].mean()
median_salary = df["salary"].median()
df_fillna = df.fillna({
    "age" : avg_age,
    "salary" : median_salary,
    "department" : "Unknown"
})
print(df_fillna)

# task 15.5.1
avg_age = df["age"].mean()
median_salary = df["salary"].median()
df_fillna_all = df.fillna({
    "name" : "Unknown",
    "age" : avg_age,
    "salary" : median_salary,
    "department" : "Unknown"
})
print(df_fillna_all)
# task 15.5.2
avg_age = df["age"].mean()
median_salary = df["salary"].median()
df.fillna({
    "name" : "Unknown",
    "age" : avg_age,
    "salary" : median_salary,
    "department" : "Unknown"
},inplace=True)
print(df)
