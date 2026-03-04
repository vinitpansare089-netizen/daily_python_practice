from sklearn.linear_model import LinearRegression
import numpy as np

###DataSet

x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,5,4,5])
model = LinearRegression()
model.fit(x, y)

print("Slope: ", model.coef_[0])
print("Intercept:", model.intercept_)

pred = model.predict(x)

mse = np.mean((y - pred)**2)
print("MSE:", mse)