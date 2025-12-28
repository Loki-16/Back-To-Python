import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

df = pd.read_csv('employee_data_day18.csv')

# Task 1
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

"""
experience-age is the strongest correlation
the feature is positive
the correlation is suspiciously high, plus the high correlation of 
experience-salary and salary-age suggests redundancy increasing 
multicollinearity risks.
"""

# Task 2
sns.violinplot(x=df["department"],y=df["salary"])
plt.show()

"""
Engineering seems to look most stable/least-spread
Hr has the most wide spread thus high variability 
of salaries between employess
"""

# Task 3
print(df["salary"].skew())
sns.histplot(df["salary"], kde=True)
plt.show()

"""
Salary shows right skewness with a long tail,
suggesting that a log transformation may help stabilize the distribution 
for modeling
"""

# Task 4
sns.scatterplot(
    x=df["experience"],
    y=df["salary"],
    hue=df["department"]
)
plt.show()

"""
At the same experience level, salaries are differing by department.
This implies that department has an independent effect on salary 
and should be included as a feature in the model.
"""