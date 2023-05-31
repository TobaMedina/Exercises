#Escribir funciones para:
# a.Generar una lista de 50 números aleatorios del 1 al 100.
# b.Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no debe modificar la lista.
# c.Recibir  una  lista  como parámetro  y  devolver  una  nueva  lista  con  los  elementos  únicos  de  la  lista  original,  sin importar el orden.

import random

def listaRandom():
    lista = []
    for i in range(50):
        lista.append(random.randint(1, 100))
    return lista

def repetido(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def unico(lista):
    lista2 = []
    for elemento in lista:
        if elemento not in lista2:
            lista2.append(elemento)
    return lista2

lista = listaRandom()
repetir = repetido(lista)
unico = unico(lista)

print(lista)
print(repetir)
print(unico)