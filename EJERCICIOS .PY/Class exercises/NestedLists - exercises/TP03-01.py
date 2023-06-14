# 1.Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado.
# 2.Ordenar en forma ascendente cada una de las filas de la matriz.
# 3.Intercambiar dos filas, cuyos números se reciben como parámetro.
# 4.Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
# 5.Trasponer la matriz sobre símisma. (intercambiar cada elemento Aij por Aji)
# 6.Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
# 7.Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
# 8.Determinar si la matriz es simétrica con respecto a su diagonal principal.
# 9.Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
# 0.Salir del programa usandoexit()

# FUNCIONES
def generar(matriz):
    filas = int(input("Dame el numero de filas: "))
    columnas = int(input("Dame el numero de columnas: "))
    matriz = []
    for i in range(filas):
        fila = [0] * columnas
        matriz.append(fila)
        
    while True:
        relleno = int(input("Dame el numero que desees posicionar en las proximas coordenadas. Si ingresas -1 se termina la carga: "))
        if relleno == -1:
            break
        rellenoFila = int(input("Dame el numero de fila donde deseas ingresar un numero, teniendo en cuenta que inicia en 0: "))
        rellenoColumna = int(input("Dame el numero de columna donde deseas ingresar un numero, teniendo en cuenta que inicia en 0: "))
        matriz[rellenoFila][rellenoColumna] = relleno
    return matriz

def ascendente(matriz):
    matrizOrdenada = sorted(matriz)
    print(matrizOrdenada)

def intercambiarFilas(matriz):
    primeraFila = int(input("Dame el index de la primera fila: "))
    segundaFila = int(input("Dame el index de la segunda fila: "))
    matriz[primeraFila], matriz[segundaFila] = matriz[segundaFila], matriz[primeraFila]
    print(matriz)
    
def intercambiarColumnas(matriz):
    primeraColumna = int(input("Dame el index de la primera columna: "))
    segundaColumna = int(input("Dame el index de la segunda columna: "))
    for fila in matriz:
        fila[primeraColumna], fila[segundaColumna] = fila[segundaColumna], fila[primeraColumna]
    print(matriz)
    
def transponerMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transponer = [[0 for j in range(filas)] for i in range (columnas)] 
    for i in range(filas):
        for j in range(columnas):
            transponer[j][i] = matriz[i][j]
    print(transponer)

def promedio(matriz):
    fila = int(input("Dame el index de la fila: "))
    promedioFila = sum(matriz[fila])
    print(promedioFila)
    
def imparesColumna(matriz):
    numColumna = int(input("Dame el indice de la columna: "))
    numFila = len(matriz)
    impares = 0
    for i in range(numFila):
        if matriz[i][numColumna] % 2 != 0:
            impares +=1
    porcentaje = (impares / numFila) * 100
    print(porcentaje)

def diagonalPrincipal(matriz):
    numFilas = len(matriz)
    numColumnas = len(matriz[0])
    if numFilas != numColumnas:
        return False
    for i in range(numFilas):
        for j in range(i+1, numColumnas):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def diagonalSecundaria(matriz):
    transpuesta = []
    for j in range(len(matriz[0])):
        fila = []
        for i in range(len(matriz)):
            fila.append(matriz[i][j])
        transpuesta.append(fila)
    validar = transpuesta == matriz
    if validar == True:
        print("La diagonal secundaria de la matriz es simetrica")
    else:
        print("La diagonal secundaria de la matriz no es simetrica")
    
# CUERPO
matriz = []
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("1 - Generar matriz")
        print("2 - Ordenar matriz")
        print("3 - Intercambiar dos filas")
        print("4 - Intercambiar dos columnas")
        print("5 - Transponer matriz")
        print("6 - Promedio de fila")
        print("7 - Porcentaje de impares de columna")
        print("8 - Verificación de simetría diagonal principal.")
        print("9 - Verificación de simetría diagonal secundaria.")
        print("0 - Salir del programa")
        print()
        opcion = int(input("Seleccione una opción: "))
        if opcion in range(0,10): 
            break

    if opcion == 0: # Opción salir del programa
        exit()
    elif opcion == 1:   # Opción generar matriz
        matriz = generar(matriz)
        print(matriz)
    elif opcion == 2:   # Opción ordenar en forma ascendente las filas
        ascendente(matriz)
    elif opcion == 3:   # Opción intercambiar 2 filas
        intercambiarFilas(matriz)
    elif opcion == 4:   # Opcion intercambiar 2 columnas
        intercambiarColumnas(matriz)
    elif opcion == 5:   # Opcion transponer matriz
        transponerMatriz(matriz)
    elif opcion == 6:   # Opcion promedio de fila
        promedio(matriz)
    elif opcion == 7:   # Opcion promedio de impares en columna
        imparesColumna(matriz)
    elif opcion == 8:   # Opcion diagonal principal simetrica
        diagonalPrincipal(matriz)
    elif opcion == 9:   # Opcion diagonal secundaria simetrica
        diagonalSecundaria(matriz)
    
    print()
    input("Presione ENTER para continuar.")
