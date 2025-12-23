import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [23,30,35,28,40],
    "salary": [40000,50000,70000,48000,90000],
    "department": ["HR", "IT", "IT", "Finance", "Management"]
})
print(df)

# task 9.1
print(df["age"])
print(df["salary"])
print(df[["name","department"]])

# task 9.2
print(df.head(2))
print(df.tail(1))
print(df[1:4])

# task 9.3
print(df[df["age"]>30])
print(df[df["salary"]>=50000])
print(df[df["department"]=="IT"])

# task 9.4
it_salary_more_than_60000 = df[(df["department"]=="IT") & (df["salary"]>60000)]
print(it_salary_more_than_60000)
Hr_or_Finance = df[(df["department"]=="HR") | (df["department"]=="Finance")]
print(Hr_or_Finance)

# task 9.5
df2 = df[["name","salary"]]
more_than_45000_salary = df2[df2["salary"]>45000]
print(more_than_45000_salary)