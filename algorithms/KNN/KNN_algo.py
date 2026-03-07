from sklearn.neighbors import KNeighborsClassifier
import numpy as np

x = np.array([[1],[2],[3],[6],[7],[8]])
y = np.array([0,0,0,1,0,1])


model = KNeighborsClassifier(n_neighbors=3)

model.fit(x, y)

pred = model.predict([[5]])

print("prediction: ", pred)