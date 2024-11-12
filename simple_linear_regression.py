# importing vital pkgs
import numpy as np
from sklearn.linear_model import  LinearRegression

# Providinp data and transforming it
# Inputs(Regressors, x) and Outputs(responses, y)
x = np. array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
print(x ,"\nShape: ", x.shape)
y = np.array([5, 20, 14, 32, 22, 38])
print(y.shape)

# Creating a model to fit the regression
model = LinearRegression().fit(x, y)

#  Getting results to see if model was suitable
# call .score(x,y ) on the model
result = model.score(x,y)
print(f'Coeffient of det: {result}.')
print(f'b0 == {model.intercept_}')
print(f'Slope: b1 == {model.coef_}') # y = 0.54x + 5.63

# Making predictions with the model
# Can be using existing or new data
# call the .predict(x) on the model
y_predicts = model.predict(x)
print(f'Predicted response: \n{y_predicts}')

# Predicting newdata
x_new = np.arange(5).reshape((-1, 1))
y_new_predicts = model.predict(x_new)
print(f"New y predicts: \n{y_new_predicts}")


