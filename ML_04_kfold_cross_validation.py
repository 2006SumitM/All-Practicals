from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = KNeighborsClassifier()

scores = cross_val_score(model, X, y, cv=5)

print("Accuracy scores for each fold:")
print(scores)

print("Average Accuracy:", round(scores.mean() * 100, 2), "%")
