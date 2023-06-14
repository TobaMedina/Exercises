# Escribir un programa con un menú que invoque a cada una de ellas y muestre por pantalla la matriz obtenida. El tamaño de las matrices debeestablecerse como N x Nsolicitando el valor por teclado, y las funciones deben servirpara cualquier valor ingresado.Antes de volver al menú detener el programa y continuar con ENTER.

def cargarMatriz():
    filas = int(input("Dame el numero de filas: "))
    columnas = int(input("Dame el numero de columnas: "))
    matriz = []
    for i in range(filas):
        fila = [0] * columnas
        matriz.append(fila)
    return matriz

def valoresDecreciente(matriz):
    numFilas = len(matriz)
    numColumnas = len(matriz[0])
    numero = int(input("Dame el valor inicial: "))
    for i in range(numFilas):
        for j in range(numColumnas):
            if i >= j:
                matriz[i][j] += numero
                if i == j:
                    numero -= 1
    print(matriz)
    
matriz = cargarMatriz()
valoresDecreciente(matriz)