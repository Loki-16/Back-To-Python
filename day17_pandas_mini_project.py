import pandas as pd

raw_data = {
    " Employee Name ": [" alice ", "Bob", "charlie", "Alice ", None],
    "Department": [" HR", "IT ", "it", "HR", "HR"],
    "Salary ": ["50000", "60000", None, "50000", "50000"],
    "Join Date": ["2021-01-10", "2020-07-15", "2022-03-01", "2021-01-10", "2021-01-10"]
}

df = pd.DataFrame(raw_data)
print("Raw Data:\n",df)

# Inspecting data
print("\nColumns:\n",df.columns)
print("\nData Types of Columns:\n",df.dtypes)
print("\nDataFrame Shape: ",df.shape)
print("\nMissing Data per column:\n",df.isna().sum())

# Cleaning column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ","_")

# value cleaning
df["employee_name"] = df["employee_name"].str.strip().str.title()
df["department"] = df["department"].str.strip().str.upper()

# Fix data types
df["salary"] = pd.to_numeric(df["salary"],errors="coerce")
df["join_date"] = pd.to_datetime(df["join_date"],errors="coerce")
print("\nData Frame info:")
df.info()

# Handling Missing values
df["employee_name"] = df["employee_name"].fillna("Unknown")
salary_median = df["salary"].median()
df["salary"] = df["salary"].fillna(salary_median)

# Detect & Handle Duplicates
duplicate_mask = df.duplicated(subset=["employee_name","department","join_date"])
duplicate_rows = df[duplicate_mask]
print("\nDuplicate Rows:\n",duplicate_rows)
df.drop_duplicates(subset=["employee_name","department","join_date"],keep="first",ignore_index=False,inplace=True)
print("\nFinal Clean Data:\n",df)
df.to_csv('day17_cleaned_data.csv',index=False)

# Insight Extracting
avg_salary_per_department = df.groupby("department")["salary"].mean()
employee_joined_by_year = df.groupby(df["join_date"].dt.year)["employee_name"].count()
max_total_salary_department = df.groupby("department")["salary"].sum().idxmax()
print("\nAverage Salaries per department:\n",avg_salary_per_department)
print("\nEmployees Joined by year:\n",employee_joined_by_year)
print("\nDepartment with Highest Total salary: ",max_total_salary_department,"\n")