import random
import csv
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle


def XD():
    datos = pd.read_csv("datos.csv", sep=",")
    
    prediccion = "victoria"
    
    puntuacion1 = 0
    puntuacion2 = 0
    puntuacion3 = 0

    X = np.array(datos.drop([prediccion], 1))
    y = np.array(datos[prediccion])
    
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.01)
    
    linear = linear_model.LinearRegression()
    linear.fit(X_train, y_train)
    precision = linear.score(X_test, y_test)
    
    
    print(type(X_train))


    elecciones = ["piedra", "papel", "tijeras"]
    eleccion = 0


    
    #eleccion = random.choice(elecciones)
    #eleccion2 = random.choice(elecciones)
    eleccion1 = 0

    victoria = 1

    eleccion2 = input("Piedra papel tijeras? ")
    

    if eleccion2 == "piedra":
        eleccion1 = 1
        e1 = np.array([[1, 1]])
        
        eleccion = linear.predict(e1)

    if eleccion2 == "papel":
        eleccion1 = 2
        e1 = np.array([[2, 1]])
        
        eleccion = linear.predict(e1)

    if eleccion2 == "tijeras":
        eleccion1 = 3
        e1 = np.array([[3, 1]])
        
        eleccion = linear.predict(e1)
        print(eleccion)
        
    eleccion = elecciones[round(int(eleccion))]

    if eleccion == "piedra":
        eleccion4 = 1

    if eleccion == "papel":
        eleccion4 = 2

    if eleccion == "tijeras":
        eleccion4 = 3

    if eleccion2 == eleccion:
        victoria = 2
        print("has empatado")

    if eleccion2 == "piedra" and eleccion == "papel":
        print("El papel repele a la piedra asi que el bot gana")
        victoria = False
        eleccion1 = 1
        eleccion_bot = 2

    if eleccion2 == "papel" and eleccion == "piedra":
        print("El papel repele a la piedra asi que tu ganas")
        victoria = True
        eleccion1 = 2
        eleccion_bot = 1

    if eleccion2 == "piedra" and eleccion == "tijeras":
        print("La piedra aplasta a las tijeras asi que tu ganas")
        victoria = True
        eleccion1 = 1
        eleccion_bot = 3

    if eleccion2 == "tijeras" and eleccion == "piedra":
        print("La piedra aplasta a las tijeras asi que el bot gana")
        victoria = False
        eleccion1 = 3

    if eleccion2 == "papel" and eleccion == "tijeras":
        print("Las tijeras cortan el papel asi que el bot gana")
        victoria = False
        eleccion1 = 2
        eleccion_bot = 3

    if eleccion2 == "tijeras" and eleccion == "papel":
        print("Las tijeras cortan el papel asi que tu ganas")
        victoria = True
        eleccion1 = 3
        eleccion_bot = 2



    if victoria == True:
        with open("datos.csv", "a", newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([eleccion1, 1, eleccion4])
        
    if victoria == False:
        with open("datos.csv", "a", newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([eleccion1, 0, eleccion4])

    if victoria == 2:
        with open("datos.csv", "a", newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([eleccion1, 2, eleccion4])
    
    otra = input("otra?")
    if otra == "si":
        XD()


XD()
