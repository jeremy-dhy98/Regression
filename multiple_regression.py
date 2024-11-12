import  numpy as np
from sklearn.linear_model import LinearRegression

# In multiple regression x is a 2D array with at least 2 cols and y is a 1D array
x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

# Creating and fitting a model
model = LinearRegression().fit(x, y)

#Getting results and interpreting
res = model.score(x, y)
print(f"Model score: {res}")
print(f"\n Intercept(b0): {model.intercept_}")
print(f"Slope(b1): {model.coef_}")

# Making predictions
y_predicts = model.predict(x)
print(f"Y_predicts: {y_predicts}")

# Predict newdata
x_new = np.arange(10).reshape((-1, 2))# One row 2 cols
# print(x_new)
y_new = model.predict(x_new)
print(f"\nNew y_predict: {y_new}")