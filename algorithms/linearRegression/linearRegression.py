#step 0:DataSet for linear regression

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

#step 1:Mean calculate

mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y) 

#step 2: compute the variance of X

var_x = sum((xi - mean_x)**2 for xi in x) / len(x)
print("Variance of X:", var_x)

#step 3:compute covariance

cov_xy = sum((x[i] - mean_x)*(y[i] - mean_y) for i in range(len(x))) / len(x)
print("Covariance:", cov_xy)

#step 4: slope m

m = cov_xy / var_x
print("Slope (m):", m)

#step 5: compute intercept

b = mean_y - m * mean_x
print("Intercept (b):", b)

# step 6: make predictions

y_pred = [m*xi + b for xi in x] 
print("Predictions:", y_pred)

# step 7: compute MSE

mse = sum((y[i] - y_pred[i])**2 for i in range(len(y))) / len(y)
print("MSE:", mse)

mean_y = sum(y)/len(y)
y_mean_pred = [mean_y for _ in y]

mse_mean = sum((y[i] - y_mean_pred[i])**2 for i in range(len(y))) / len(y)
print(mse_mean)