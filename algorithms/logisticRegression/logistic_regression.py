
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

# dataset
X = np.array([[1],[5],[3],[10],[5],[3],[7],[2]])
y = np.array([0,0,0,0,1,1,1,1])

# train model
model = LogisticRegression()
model.fit(X,y)


print("Class 0(fail)   class 1(pass)")
print(model.predict_proba(X))

# predictions
pred = model.predict(X)
print(pred)
print(model.coef_)
print(model.intercept_)

# # evaluation

accuracy = accuracy_score(y, pred)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:")
print(confusion_matrix(y,pred))

print("\nClassification Report:")
print(classification_report(y,pred))

