# Desarrollar  cada  una  de  las  siguientes  funciones  y  escribir  un  programa  que  permita  verificar  su  funcionamiento imprimiendo la lista luego de invocar a cada función:
# a.Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
# b.Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
# c.Eliminar todas las apariciones de un valor en la lista anterior.El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro.
# d.Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].

import random

def cargar(lista):
    lista = []
    a = random.randint(10, 13)
    for i in range(a):
        lista.append(random.randint(1000, 9999))
    return lista

def sumatoria(lista):
    a = sum(lista)
    return a 

def remover(lista, n):
    while lista.count(n)>0:
        lista.remove(n)
    return lista

def capicua(lista2):
    inicio = 0
    fin = len(lista) -1
    
    while inicio < fin:
        if lista2[inicio] != lista[fin]:
            return 0
        inicio +=1
        fin -= 1
    return 1

lista = []
lista2 = lista[:]
carga = cargar(lista)
suma = sumatoria(carga)
print(carga)
print(suma)

n = int(input("Ingrese el numero que desea retirar de la lista: "))
sacar = remover(carga, n)
print(sacar)

capicua = capicua(lista2)
if capicua == 1:
    print("La lista no es capicua")
else:
    print("La lista es capicua")

