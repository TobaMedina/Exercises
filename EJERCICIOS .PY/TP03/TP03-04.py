# Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas en cada una de sus plantas durante una semana. De este modo, cada columna representa el día de la semana (Lunes columna 0, Martes columna 1, etc.)y cada fila representa a una de sus fábricas
# A. Crear una matriz con datos generados al azar de N fábricas durante una semana, considerando que la capacidad máxima de fabricación es de 150 unidades por día y puede suceder que en ciertos días no se fabrique ninguna. Mostrar la matriz por pantalla.
# B. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
# C. Mostrar cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
# D. Mostrar cuál es el día más productivo, considerando todas las fábricas combinadas.
# E. Crear una lista por comprensión que contenga la menor cantidad fabricada por cada fábrica. Mostrarla.

import random

def cargarMatriz():
    fabricas = int(input("Dame el numero de fabricas: "))
    matriz = [[0 for j in range(7)] for i in range(fabricas)]
    for i in range(fabricas):
        for j in range(7):
            matriz[i][j] = random.randint(0, 150)
    return matriz

def total(matriz):
    suma = []
    for fila in matriz:
        sumaFila = sum(fila)
        suma.append(sumaFila)
    return suma





matriz = cargarMatriz()
print(matriz)
print(total(matriz))