# task 8.1
import pandas as pd

# task 8.2
pan1 = pd.Series([10,20,30,40])
print(pan1)

# task 8.3
df = pd.DataFrame({
    "name" : ["A","B","C"],
    "age" : [20,25,30]
})
print(df)

# task 8.4
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.index)
df.info() # df.info() prints itself

# task 8.5
df = pd.read_csv("people.csv")
print(df)
df.info()
print(df.head())