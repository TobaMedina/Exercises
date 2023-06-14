"""
-----------------------------------------------------------------------------------------------
Título: Mock Exam
Fecha:
Autor: Tobias Medina Viegas
Descripción:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def agregarAmigosAlSorteo():
    nombre = input("Ingresar nombre: ")
    apellido = input("Ingresar apellido: ")
    dni = validarEntero("Ingrese DNI: ", "El DNI ingresado no es un numero entero. ")
    nro1 = validarEntero("Ingrese el numero elegido: ", "El numero ingresado no es un entero! ")
    nro2 = validarEntero("Ingrese el numero elegido: ", "El numero ingresado no es un entero! ")
    nro3 = validarEntero("Ingrese el numero elegido: ", "El numero ingresado no es un entero! ")
    nro4 = validarEntero("Ingrese el numero elegido: ", "El numero ingresado no es un entero! ")
    nro5 = validarEntero("Ingrese el numero elegido: ", "El numero ingresado no es un entero! ")
    nro6 = validarEntero("Ingrese el numero elegido: ", "El numero ingresado no es un entero! ")
    cadenaCaracteres = f"{nombre};{apellido};{dni};{nro1};{nro2};{nro3};{nro4};{nro5};{nro6}\n"
    
    f = open(path, "a", encoding="utf-8")
    f.write(cadenaCaracteres)
    
    
    

def validarEntero(_mensajePedido, _mensajeError):
    while True:
        try:
            dato = int(input(_mensajePedido))
            return dato
        except ValueError:
            print(_mensajeError)


def realizarSorteo():
    _numerosSorteados = sortearNumeros()
    _listaGanadores = []
    f = open(path, "r", encoding="utf-8")
    lineas = f.readlines()
    for linea in lineas:
        datos = linea.strip().split(";")
        numerosApostados = []
        aciertos = 0
        for i in range(3, len(datos)):
            numerosApostados.append(int(datos[i]))
        for numero in numerosApostados:
            if numero in _numerosSorteados:
                aciertos += 1
        if aciertos >= 2:
            ganador = f"{datos[0]} {datos[1]}"
            _listaGanadores.append(ganador)
        
    return _numerosSorteados, _listaGanadores
        
        
    

def sortearNumeros():
    _numerosSorteados = []
    while len(_numerosSorteados) < 6:
        numero = random.randint(1, 90)
        if numero not in _numerosSorteados:
            _numerosSorteados.append(numero)
    return _numerosSorteados


def repartirPozo(_listaGanadores):
    mensajePedido = "ingrese un monto total de apuestas válido: "
    mensajeError = "El monto no es un número, intente denuevo"
    monto = validarEntero(mensajePedido, mensajeError)
    ganadores = len(_listaGanadores)
    try:
        montoGanador = monto / ganadores
    except ZeroDivisionError:
        print("Pozo vacante!")
    for ganador in _listaGanadores:
        print(f"{ganador} gano: ${montoGanador}")
    

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
#----------------------------------------------------------------------------------------------
numerosSorteados = []
path = "D:\sorteados.txt"  # IMPORTANTE!!!!! usa esta variable string para el path completo del archivo sorteados.txt

# Bloque de menú
#----------------------------------------------------------------------------------------------while True:
while True:
    while True:
        try:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Cargar Amigos al sorteo")
            print("[2] Sortear!")
            print("[3] Mostrar ganadores!")
            print("[0] Salir del programa")
            print()
            opcion = int(input("Seleccione una opción: "))
            if opcion in range(0,4): # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para continuar.")
        except ValueError:
            input("Opción inválida. Presione ENTER para continuar.")
            continue

    if opcion == 0: # Opción salir del programa
        exit()

    elif opcion == 1:   # Opción Cargar Amigos al sorteo
        agregarAmigosAlSorteo()
        
    elif opcion == 2:   # Sortear!
        numerosSorteados, listaGanadores = realizarSorteo()
        print('Números sorteados: ', numerosSorteados)
        print('Ganadores: ', listaGanadores)

    elif opcion == 3:   # Vaciar lista de amigos
        if len(numerosSorteados) > 0:
            repartirPozo(listaGanadores)
        else:
            print("Primero realice el sorteo!")

    print()
    input("Presione ENTER para continuar.")

