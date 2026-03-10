from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.metrics import accuracy_score

x = np.array([[2],[3],[6],[7]])
y = np.array([0,0,1,1])

# print(x)

model = DecisionTreeClassifier()

model.fit(x, y)

pred = model.predict([[1.4]])

print(pred)