import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [23, 30, 35, 28, 40],
    "salary": [40000, 50000, 70000, 48000, 90000],
    "department": ["HR", "IT", "IT", "Finance", "Management"]
})
# # task 11.1
# df.loc[df["department"] == "IT"]
# df.loc[df["department"] == "IT",["name","salary"]]
# df["salary"] = df["salary"].astype(float)
# df.loc[df["age"]>35,"salary"] *= 1.1

# # task 11.2
# df.iloc[0:3]
# df.iloc[[-2,-1]]
# df.iloc[1:4,0:3]

# task 11.3
"""
My answer: 
1. df.loc[1:3] will return the rows: 1,2, and 3 included because .loc[] in 
inclusive 
2. df.iloc[1:3] will return the rows: 1 and 2 because .loc[] in 
exclusive it wont count the 3rd row 
3. because .loc[] is inclusive but .iloc is exclusive 
4. in selecting from a dataframe for a task you could
either include 1 unnecessary row or remove 1 necessary row 
which can cause problems in either output or simply crash the program 
depending on the execution.
Model answer:
1. df.loc[1:3] returns rows with labels 1,2, and 3 because .loc[] uses 
label-based inclusive slicing.
2. df.iloc[1:3] returns rows at positions 1 and 2 because .iloc[] follows 
Python-style exclusive slicing.
3. This difference exists because .loc[] is label-oriented, while .iloc[] is 
position-oriented.
4. This can cause off-by-one bugs where an extra row is included or an 
important row is skipped, leading to incorrect analysis or downstream errors.
"""

# task 11.4
df.loc[df["department"] == "Finance","salary"] = 60000
