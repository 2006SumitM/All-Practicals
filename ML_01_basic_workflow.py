import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("student.csv")

print("Dataset:")
print(data)

le = LabelEncoder()
data["Result"] = le.fit_transform(data["Result"])

X = data[["Hours", "Attendance"]]
y = data["Result"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = KNeighborsClassifier()
model.fit(X_train, y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("Training Accuracy:", accuracy_score(y_train, train_pred) * 100)
print("Testing Accuracy:", accuracy_score(y_test, test_pred) * 100)
