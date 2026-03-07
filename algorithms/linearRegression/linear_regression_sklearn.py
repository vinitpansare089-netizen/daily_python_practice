from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,5,4,5])

model = LinearRegression()
model.fit(X,y)

pred = model.predict(X)

mse = mean_squared_error(y, pred)
rmse = np.sqrt(mse)

print("MSE:", mse)
print("RMSE:", rmse)