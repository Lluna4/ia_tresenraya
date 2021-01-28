import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

#print(data.head())

data = data[["G1", "G2", "G3", "studytime", "failures", "absences", "freetime"]]

prediccion = "G3"

X = np.array(data.drop([prediccion], 1))
y = np.array(data[prediccion])

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

linear = linear_model.LinearRegression()
linear.fit(X_train, y_train)
precision = linear.score(X_test, y_test)


predicciones = linear.predict(X_test)


for X in range(len(predicciones)):
    print(predicciones[X], X_test[X], y_test[X])