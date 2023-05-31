# Utilizar la técnica de listas por comprensión para construir una lista con todos los números impares comprendidos entre 100 y 200.

def listaNueva():
    lista = []
    for i in range(100, 201):
        lista.append(i)
    return lista

lista = listaNueva()
listaImpares = [numero for numero in lista if numero % 2 == 1]

print(listaImpares)
