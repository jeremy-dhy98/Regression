import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Providing data
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([15, 11, 2, 8, 25, 32])

transformer = PolynomialFeatures(degree=2, include_bias=False)
transformer.fit(x) # fit the transformer obj with the data
x_transformed = transformer.transform(x)# transform the data

#creating a model and fitting it
model = LinearRegression().fit(x_transformed, y)

# Getting results to evaluate the model
print(f"Model score(R*2): {model.score(x_transformed,y)}")
print(f"\n Intercept(b0): {model.intercept_}")
print(f"\n Scope(b1): {model.coef_}")

# Predict response
y_predict = model.predict(x_transformed)
print(f"Y_predict: \n{y_predict}")