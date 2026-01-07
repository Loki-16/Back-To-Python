import pandas as pd

# Create raw data
data = {
    "experience_years": [0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10],
    "salary": [25000, 30000, 34000, 38000, 42000, 46000,
               54000, 62000, 70000, 78000, 86000, 94000, 102000]
}

# Create DataFrame explicitly
# task 24.1
df = pd.DataFrame(data)
print(df.head())
print(df.shape)
df.info()

#  task 24.2
X = pd.DataFrame(df["experience_years"])
y = pd.Series(df["salary"])

# task 24.3
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print(len(X_train) + len(X_test) == len(X))
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
# why do we split data before training
"""
we split data into training and test so that we can compare and validate that
the rules and parameters the model has come-up with are accurate on both known
and unseen data to make the model more generalized and avoid misleading performance.
"""

# task 24.4
from sklearn.linear_model import LinearRegression
model = LinearRegression()
print(model)
print(model.get_params(),"\n")
# What does the LinearRegression() object represent before training?
"""
The LinearRegression() object represents an untrained regression algorithm.
At this stage, it only defines the model structure and configuration.
It has not learned any weights or bias yet.
The model needs to be trained using .fit(x_train, y_train) to learn
parameters from the data.

"""

# task 24.5
model.fit(X_train,y_train)
print(model.coef_)
print(model.intercept_)
print(model)
print(model.get_params(),"\n")
# What changed inside the model after calling fit()?
"""
After calling fit(), the model object itself does not change visually
and model.get_params() still shows configuration parameters only.
However, new attributes (coef_ and intercept_) are created,
which store the learned weight(s) and bias from the training data.
"""

# task 24.6
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
print(y_train_pred)
print(y_test_pred)
print(y_train_pred.shape)
print(y_test_pred.shape)
# What does model.predict() return and why?
"""
model.predict() returns a NumPy array of predicted target values.
The predictions are computed using the learned weights and bias
from the training data.
"""

# train 24.7
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
mae = mean_absolute_error(y_test,y_test_pred)
mse = mean_squared_error(y_test,y_test_pred)
r2 = r2_score(y_test,y_test_pred)
print("test data performance")
print(f'MAE = {mae}')
print(f'MSE = {mse}')
print(f'R2 = {r2}')
# Is training performance better than test performance?
# What does this indicate about generalization?
"""
Training performance is expected to be better than test performance
because the model is optimized on training data.
If test performance is close to training performance,
it indicates good generalization.
A large gap would indicate overfitting.
"""