# What kind of problems does Linear Regression solve?
"""
linear regression solves problems where prediction of a continuous number is
necessary. ex:- house_price, salary etc.
"""
# Why is it supervised?
"""
in linear regression we know both the input(features) and output(label)
"""
# What does the model actually learn?
"""
the model learns parameteres from the data like:
weight(s) -> how strongly each feature affect the output
bias -> baseline value when inputs are zero
"""
# What does training mean?
"""
training refers to the following:
1. guessing using current parameters
2. compare prediction vs actual value
3. compute how wrong the prediction was(error)
4. adjust the parameteres to reduce error
5. repeat
"""
# Why can Linear Regression fail on some datasets?
"""
linear regression can fail when the relationship is non-linear, curved, or
contains strong outliers and leakage.
"""