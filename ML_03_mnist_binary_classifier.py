from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

digits = load_digits()

X = digits.data
y = (digits.target == 5)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

print("Training Accuracy:", model.score(X_train, y_train) * 100)


print("Testing Accuracy:", model.score(X_test, y_test) * 100)


prediction = model.predict([X_test[0]])



if prediction[0]:
    print("Digit is 5")
else:
    print("Digit is not 5")
