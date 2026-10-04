import pandas as pd
from sklearn.datasets import fetch_openml

data = fetch_openml("adult", version=2, as_frame=True)

df = data.frame

print("Income Class Distribution:")
print(df["class"].value_counts())

print("\nGender Distribution:")
print(df["sex"].value_counts())

print("\nIncome by Gender:")
print(pd.crosstab(df["sex"], df["class"]))
