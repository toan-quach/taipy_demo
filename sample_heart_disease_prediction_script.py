import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

heart_disease_df = pd.read_csv("data/heart-disease-dataset.csv")

x = heart_disease_df.drop("target" , axis = 1)
y = heart_disease_df[['target']]

np.random.seed(0)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
x_validate, x_test, y_validate, y_test = train_test_split(x_test, y_test, test_size = 0.5)

model = RandomForestClassifier()

model.fit(x_train, y_train["target"])

model_accuracy_test = model.score(x_test, y_test["target"])

print("Model Accuracy Test:" , model_accuracy_test * 100 , "%")
