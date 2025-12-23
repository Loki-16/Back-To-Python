import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", None],
    "age": [23, None, 35, 28, 40],
    "salary": [40000, 50000, None, 48000, 90000]
})

# #  task 12.1
# print(df)
# print(df.isna())
# print(df.isna().sum())

# #  task 12.2
# print(df.dropna())
# print(df.dropna(subset=["salary"]))

# #  task 12.3
# mean_age = df["age"].mean()
# filled_age = df["age"].fillna(mean_age)
# filled_df = df.fillna({
#     "salary" : 0,
#     "name" : "Unknown"
# })
# print(filled_age)
# print(filled_df)

#  task 12.4
df_employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"]
})

df_salaries = pd.DataFrame({
    "emp_id": [1, 2, 4],
    "salary": [40000, 50000, 48000]
})
merged_df = pd.merge(df_employees, df_salaries, on="emp_id")
print(merged_df)