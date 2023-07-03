# Generar una lista  con números al azar entre 1 y 100 y crear una nueva lista con los elementos de  la primera que  sean impares. El proceso deberá realizarse utilizando listas por comprensión. Imprimir las dos listas por pantalla.

import random

def listaRandom():
    lista = []
    for i in range(random.randint(1, 20)):
        lista.append(random.randint(1, 100))
        
    return lista

lista = listaRandom()
print(lista)

listaImpares = [numero for numero in lista if numero % 2 == 1]
print(listaImpares)

