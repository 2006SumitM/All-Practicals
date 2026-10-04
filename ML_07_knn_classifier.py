import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("studentknn.csv")

le = LabelEncoder()
data["Result"] = le.fit_transform(data["Result"])

X = data[["Hours"]]
y = data["Result"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

new_student = [[6]]
prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Result: Pass")
else:
    print("Result: Fail")
