import pandas as pd
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("studentmarks.csv")

X = data[['Hours']]
y = data['Marks']

model = DecisionTreeRegressor(max_depth=3, random_state=1)

model.fit(X, y)

new_student = pd.DataFrame([[7.5]], columns=['Hours'])
prediction = model.predict(new_student)

print("Predicted Marks for 7.5 Hours:", round(prediction[0], 2))
