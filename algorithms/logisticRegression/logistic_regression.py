
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

# dataset
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
y = np.array([0,0,0,0,1,1,1,1])

# train model
model = LogisticRegression()
model.fit(X,y)

# predictions
pred = model.predict(X)

# evaluation
accuracy = accuracy_score(y, pred)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:")
print(confusion_matrix(y,pred))

print("\nClassification Report:")
print(classification_report(y,pred))

