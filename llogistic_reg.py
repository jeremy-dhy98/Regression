# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Geting and transforming data
# reshape the data to a 2D matrix with as many rows as possible and 1 col
x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Creating a model and traing it/fitting it with data
model = LogisticRegression(solver="liblinear", C=10.0, random_state=0).fit(x, y)

# Some key attributes of the model
print(f"\nValues of y: {model.classes_}") # 0 and 1 as this is a clasification problem
print(f"\nIntercept(b0): {model.intercept_}")
print(f"\nSlope coef(b1): {model.coef_}")

# Evaluating the model .predict_proba(x)
print(f"\nModel eficiency: {model.predict_proba(x)}")
# Check the actual predictions
print(f"\nPredictions: {model.predict(x)}")
# Check how many observations are predicted correctly
print(f"Model score: {model.score(x,y)}") # correct/total observations

# Use confusion_matrix to check more on the models accuracy
com_matrix = confusion_matrix(y, model.predict(x))
print(f"Confusion_matrix: {com_matrix}")

# Visualizing the confusion_matrix use .imshow() from matplotlib
fig, ax = plt.subplots(figsize=(5, 3))
ax.imshow(com_matrix)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=("Predicted 0s", "Predicted 1s"))
ax.yaxis.set(ticks=(0, 1), ticklabels=("Actual 0s", "Actual 1s"))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, com_matrix[i, j], ha="center", va="center", color="white")
plt.savefig("confusion_matrix.png")
plt.show()

