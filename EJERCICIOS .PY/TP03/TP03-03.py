# Desarrollar  un  programa para  rellenar  una matriz  de  N  x  N  con  números  enteros  al  azar  comprendidos en  el  intervalo [0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla.

import random

def matrizRandom(n):
    numeros = list(range(n*n))
    random.shuffle(numeros)
    matriz = [[0 for j in range(n)] for i in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            matriz[i][j] = numeros[k]
            k += 1
    return matriz


print(matrizRandom(4))
    