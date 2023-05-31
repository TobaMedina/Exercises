# Escribir un programa con un menú que invoque a cada una de ellas y muestre por pantalla la matriz obtenida. El tamaño de las matrices debeestablecerse como N x Nsolicitando el valor por teclado, y las funciones deben servirpara cualquier valor ingresado.Antes de volver al menú detener el programa y continuar con ENTER.

def cargarMatriz():
    filas = int(input("Dame el numero de filas: "))
    columnas = int(input("Dame el numero de columnas: "))
    matriz = []
    for i in range(filas):
        fila = [0] * columnas
        matriz.append(fila)
    return matriz


def matrizCaracol(matriz):
    numFilas = len(matriz)
    numColumnas = len(matriz[0])
    
    matriz_salida = [[0 for x in range(numColumnas)] for y in range(numFilas)]
    
    fila = 0
    columna = 0
    incremento = 1
    
    for i in range(numFilas * numColumnas):
        matriz_salida[fila][columna] = i + 1
        if columna + incremento == numColumnas or fila - incremento < 0 or matriz_salida[fila-incremento][columna+incremento] != 0:
            incremento = -incremento
        fila -= incremento
        columna += incremento
    
    return matriz_salida



matriz = cargarMatriz()
print(matrizCaracol(matriz))