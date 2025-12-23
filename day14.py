import pandas as pd

employees_df = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Amit", "Neha", "Ravi", "Sara"]
})

departments_df = pd.DataFrame({
    "emp_id": [2, 3, 5],
    "department": ["HR", "IT", "Finance"]
})
print(employees_df)
print(departments_df)
# task 14.2.2
merge_inner = pd.merge(employees_df,departments_df,on="emp_id")
print("Inner\n",merge_inner)
# task 14.2.3
merge_left = pd.merge(employees_df,departments_df,on="emp_id",how="left")
print("Left\n",merge_left)
# task 14.2.4
merge_right = pd.merge(employees_df,departments_df,on="emp_id",how="right")
print("Right\n",merge_right)
# task 14.2.5
merge_outer = pd.merge(employees_df,departments_df,on="emp_id",how="outer")
print("Outer\n",merge_outer)
# Mandatory Safety Check
print(merge_inner.shape)
print(merge_inner.isna().sum())

print(merge_left.shape)
print(merge_left.isna().sum())

print(merge_right.shape)
print(merge_right.isna().sum())

print(merge_outer.shape)
print(merge_outer.isna().sum())

# task 14.3.1
import pandas as pd

jan_df = pd.DataFrame({
    "emp_id": [1, 2],
    "sales": [200, 300]
})

feb_df = pd.DataFrame({
    "emp_id": [3, 4],
    "sales": [250, 400]
})
print(jan_df)
print(feb_df)

# task 14.3.2
sales_q1 = pd.concat([jan_df,feb_df])
print(sales_q1)
# task 14.3.3
sales_q1_reset = pd.concat([jan_df,feb_df],ignore_index=True)
print(sales_q1_reset)
# task 14.3.4
bonus_df = pd.DataFrame({
    "bonus": [50, 60]
})
combined_cols = pd.concat(
    [jan_df,bonus_df],
    axis=1
)
print(combined_cols)

import pandas as pd

employees_df = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "name": ["Amit", "Neha", "Ravi"]
})

salaries_df = pd.DataFrame({
    "emp_id": [1, 2, 4],
    "salary": [50000, 60000, 70000]
})
# task 14.4.1
emp_full_df = pd.merge(employees_df,salaries_df,on="emp_id",how="left")

# task 14.4.2 
mar_df = pd.DataFrame({
    "emp_id": [1, 2],
    "sales": [300, 450]
})

apr_df = pd.DataFrame({
    "emp_id": [3, 4],
    "sales": [500, 350]
})
sales_df = pd.concat(
    [mar_df,apr_df],
    ignore_index=True
)
print(sales_df)