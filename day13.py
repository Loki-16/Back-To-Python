import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "age": [23, 30, 35, 28, 40, 30],
    "salary": [40000, 50000, 70000, 48000, 90000, 52000],
    "department": ["HR", "IT", "IT", "Finance", "Management", "IT"]
})

print(df)

# task 13.1
print(df.groupby("department")["salary"].mean())

# task 13.2
print(df.groupby("department")["salary"].agg(["mean","max","count"]))

# task 13.3
print(df.groupby("department")["age"].mean())

# task 13.4
print(df.groupby(["department","age"]).count())

# task 13.5.1
print(df.groupby("department",as_index=False)["salary"].mean())

# task 13.5.2
print(df.groupby("department",as_index=False).agg(
    avg_salary =("salary","mean"),
    max_salary = ("salary","max"),
    employee_count = ("salary","count")
))

# task 13.5.3
result = (
    df.groupby(["department","age"])
    .size()
    .to_frame(name="employee_count")
    .reset_index()
)
print(result)