import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

# task 1 - Load Dataset
df = pd.read_csv('employee_data_day18.csv') #imported cleaned data from day 17

# task 2 - Dataset Overview
print(df.shape)
df.info()
print(df.describe())
print(df.head())

# task 3 - Univariate Analysis
# Histogram
sns.histplot(df["salary"])
plt.show()

# Boxplot
sns.boxplot(x=df["salary"])
plt.show()

# Countplot
sns.countplot(x=df["department"])
plt.show()
"""
1. Salary distribution is right-skewed, with most employees earning lower to mid-range salaries and a few high earners.
2. The salary boxplot shows a median around 88,000 and several high-value outliers, indicating salary inequality.
3. Department counts are imbalanced, with Engineering dominating the dataset and HR having the fewest employees.

"""

# task 4 - Bivariate Analysis
# Scatterplot
sns.scatterplot(x=df["experience"], y=df["salary"])
plt.show()
# Boxplot (category vs numeric)
sns.boxplot(x=df["department"],y=df["salary"])
plt.show()
"""
1. Salary distribution is right-skewed, with most employees earning lower to mid-range salaries and a few high-salary outliers.
2. The scatter plot shows a positive relationship between experience and salary, although there is noticeable variability among employees with similar experience.
3. The Engineering department has the widest salary spread and multiple outliers, while Finance also shows high salaries with slightly less variability.
4. Sales, Marketing, and HR exhibit lower and more compact salary distributions.
5. Salary outliers are present across departments, most notably in Engineering and Finance.


"""
# Heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.show()
