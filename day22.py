# Q: Why do we split data into train and test?
"""
we split data so we can compare & validate learning accuracy between the two
to see how the model works for data it has already seen(with label)
vs unseen data(real-life data)
"""
# Q: What is overfitting? Give a real-life analogy.
"""
overfitting is the case in which a model has very high accuracy for training,
but has low accuracy for test. an example would be if someone solves an already
memorized puzzle but can't perform on a new puzzle.
"""
# Q: Why is test accuracy more important than training accuracy?
"""
In a model, test accuracy is the more likely representative of real life data
thus it's more important, example would be a Final exam to a student to a
mock exam.
"""

# Q: What does “generalization” mean in ML?
"""
Generalization is the model's ability to apply learned patterns
from training data to unseen data,
resulting in similar performance on both sets
"""