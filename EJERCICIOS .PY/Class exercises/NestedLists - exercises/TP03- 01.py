"""
TP03-01
FUNCIONES CON MATRICES Y MENÚ

Desarrollar un programa que presente el siguiente menú de opciones:
Cada opción llamará a una función a desarrollar según las siguientes funcionalidades:
1. Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado.
2. Ordenar en forma ascendente cada una de las filas de la matriz.
3. Intercambiar dos filas, cuyos números se reciben como parámetro.
4. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
5. Trasponer la matriz sobre sí misma. (intercambiar cada elemento Aij por Aji)
6. Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
7. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
8. Determinar si la matriz es simétrica con respecto a su diagonal principal.
9. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
0. Salir del programa usando exit()
Para operar el programa siempre primero se elegirá la opción 1 para generar la matriz de trabajo.
La matriz de trabajo deberá quedar en el ámbito global del programa y nunca deberá ser modificada por ninguna de
las demás funciones. Al elegir la opción 1 se debe mostrar la matriz generada por pantalla.
Luego, al elegir cualquiera de las demás opciones del menú, se solicitarán datos de ser necesario,
y luego se llamará a la correspondiente función, para finalmente presentar la matriz original
junto al resultado de la función invocada.
Se deberá esperar a presionar ENTER para que vuelva a aparecer le menú de opciones codificando
para esto input("Presione ENTER para continuar.")
NOTA: No incluir instrucciones “input” ni “print” dentro de las funciones."""

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
        print("6 - Promedio de filas")
        print("7 - Porcentaje de impares de columna")
        print("8 - Verificación de simetría diagonal principal")
        print("9 - Verificación de simetría diagonal secundaria")
        print("0 - Salir del programa")
        print()
        print("Seleccione una opción: ")
        opcion = int(input())
        if opcion in range(0,10): # Sólo continua si se elije una opcion de menú válida
            break
        
    matriz = []

    if opcion == 0: # Opción salir del programa
        exit()  # Cierro la aplicación

    elif opcion == 1:   
        generarMatriz(matriz)
        input("Presione ENTER para continuar.")
        
    elif opcion == 2:   
        ordenarMatriz(matriz)
        input("Presione ENTER para continuar.")
    
    elif opcion == 3:
        intercambiarDosFilas(matriz)
        input("Presione ENTER para continuar.")
           
    elif opcion == 4:
        intercambiarDosColumnas(matriz)
        input("Presione ENTER para continuar.")
        
    elif opcion == 5:
        transponerMatriz(matriz)
        input("Presione ENTER para continuar.")
        
    elif opcion == 6:
        
        input("Presione ENTER para continuar.")
        
    elif opcion == 7:
        
        input("Presione ENTER para continuar.")
        
    elif opcion == 8:
        
        input("Presione ENTER para continuar.")
        
    elif opcion == 9:
        
        input("Presione ENTER para continuar.")
    

        

