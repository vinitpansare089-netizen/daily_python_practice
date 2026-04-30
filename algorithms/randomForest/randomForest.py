from sklearn.ensemble import RandomForestClassifier
import numpy as np

x = np.array([[2],[3],[6],[7]])
y = np.array([0,0,1,1])

model = RandomForestClassifier(n_estimators=10, max_depth=5)

model.fit(x, y)

pred = model.predict([[5]])

print(pred)

