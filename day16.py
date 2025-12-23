import pandas as pd

df = pd.DataFrame({
    "Name ": [" Amit", "Riya", "John", "Amit", "riya", "John "],
    "Department": ["IT", "HR ", "IT", "HR", "it", "HR"],
    "Salary": ["60000", "50000", "65000", "52000", "70000", "48000"],
    "Experience": [3, 2, 4, 3, 5, 1]
})
print(df)
df.info()

# task 16.1
df.columns = df.columns.str.lower().str.strip(" ").str.replace(" ","_")
print(df.columns)
# task 16.2
df["name"] = df["name"].str.strip().str.lower()
df["department"] = df["department"].str.strip().str.lower()
print(df)
# task 16.3
df["salary"] = df["salary"].astype("Int64")
df.info()
# task 16.4
duplicate_mask = df.duplicated(subset=["name","department"])
print(duplicate_mask)
duplicate_rows = df[duplicate_mask]
print(duplicate_rows)
df.drop_duplicates(subset=["name","department"],inplace=True)
# task 16.5
print(df)
df.info()