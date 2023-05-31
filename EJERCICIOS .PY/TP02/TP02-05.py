# Crear  una  lista  con  los  cuadrados  de  los  números  entre  1  y  N  (ambos  incluidos),  donde  N  se  ingresa  desde  el  teclado. Luego se solicita imprimir los últimos 10 valores de la lista.

def cuadrado(n):
    lista = []
    for i in range(1, n+1):
        lista.append(i**2)
    return lista

def ultimos(lista):
    ultimosDiez = lista[-10:]
    return ultimosDiez




n = int(input("Numero: "))
lista = cuadrado(n)
print(lista)


ultimos = ultimos(lista)
print(ultimos)