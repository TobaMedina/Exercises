"""
-----------------------------------------------------------------------------------------------
Título: Primer parcial programacion 1
Fecha: 08/05/2023
Autor: Tobias Medina Viegas
Descripción:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# MÓDULOS BBDD
#----------------------------------------------------------------------------------------------
baseDeNombres = ["ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ANDRES" , "JUAN" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ANDRES" , "JUAN" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ANDRES" , "JUAN" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ROBERTO" , "MARIA" , "JORGE" , "JORGE" , "JORGE" , "MARIA" , "MARIA" , "ROBERTO" , "ROBERTO", "MARIA" , "ROBERTO"]
baseDeCuotas = [15000 , 10000 , 18000 , 18000 , 15000 , 10000 , 15000 , 10000 , 18000 , 18000 , 15000 , 10000 , 18000 , 18000 , 15000 , 10000 , 15000 , 10000 , 18000 , 18000 , 15000 , 10000 , 18000 , 18000 , 15000 , 10000 , 15000 , 10000 , 18000 , 18000 , 15000 , 10000 , 18000 , 18000 , 18000 , 10000 , 10000 , 15000 , 15000 , 10000 , 15000 ]
baseDeCarrocerias = ["SEDAN" , "FAMILIAR" , "COUPE" , "COUPE" , "SEDAN" , "FAMILIAR" , "SEDAN" , "FAMILIAR" , "COUPE" , "COUPE" , "SEDAN" , "FAMILIAR" , "COUPE" , "COUPE" , "SEDAN" , "FAMILIAR" , "SEDAN" , "FAMILIAR" , "COUPE" , "COUPE" , "SEDAN" , "FAMILIAR" , "COUPE" , "COUPE" , "SEDAN" , "FAMILIAR" , "SEDAN" , "FAMILIAR" , "COUPE" , "COUPE" , "SEDAN" , "FAMILIAR" , "COUPE" , "COUPE" , "COUPE" , "FAMILIAR" , "FAMILIAR" , "SEDAN" , "SEDAN", "FAMILIAR" , "SEDAN"]
autosEntregados = ['Se ha entregado un auto SEDAN al cliente SUSANA, valor de cuota $ 15000']

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def cargarNuevoPagoCuota(_baseDeNombres, _baseDeCuotas, _baseDeCarrocerias):
    tipoDeCliente = input("Deseas cargar un nuevo cliente? [S|N]: ").upper()
    
    # Cliente nuevo
    if tipoDeCliente == "S":
        clienteNuevo = input("Dime el nombre del cliente: ").upper()
        while True:
            carroceriaNueva = input("Qué Carrocería? [SEDAN|COUPE|FAMILIAR]: ").upper()
            if carroceriaNueva in _baseDeCarrocerias:
                break
            print("Carrocería inexistente, vuelve a intentar!")

        # Registro el pago de la cuota
        _baseDeNombres.append(clienteNuevo)
        _baseDeCarrocerias.append(carroceriaNueva)
        if carroceriaNueva == "SEDAN":
            _baseDeCuotas.append(15000)
        elif carroceriaNueva == "FAMILIAR":
            _baseDeCuotas.append(10000)
        elif carroceriaNueva == "COUPE":
            _baseDeCuotas.append(18000)
    
    # Cliente existente
    else:
        while True:
            clienteExistente = input("Dime el nombre del cliente: ").upper()
            if clienteExistente in _baseDeNombres:
                break
            print("El cliente no existe o fue mal ingresado, vuelve a intentar!")
        
        # Obtengo posición del cliente para recuperar cuota y carrocería de la misma posición de las otras listas
        posicionClienteExistente = _baseDeNombres.index(clienteExistente)
        
        # Registro el pago de la cuota
        _baseDeNombres.append(clienteExistente)
        _baseDeCuotas.append(_baseDeCuotas[posicionClienteExistente])
        _baseDeCarrocerias.append(_baseDeCarrocerias[posicionClienteExistente])
    
    print()
    print("Cuota almacenada con éxito!")
    return _baseDeNombres, _baseDeCuotas, _baseDeCarrocerias


def SortearAuto(_baseDeNombres, _baseDeCuotas, _baseDeCarrocerias, _autosEntregados):
    # Sorteo un ganador, pero que sea un cliente con al menos 6 cuotas pagadas
    while True:
        posicionSorteo = random.randint(0,len(_baseDeNombres)-1)
        nombreEliminar = _baseDeNombres[posicionSorteo]
        if _baseDeNombres.count(nombreEliminar) >= 6:
            break
    
    # Muestro mensaje de ganador y registro su adjudicación
    print("El cliente sorteado es: ", baseDeNombres[posicionSorteo])
    _autosEntregados.append(f"Se ha entregado un auto {_baseDeCarrocerias[posicionSorteo]} al cliente {_baseDeNombres[posicionSorteo]} valor de cuota $ {_baseDeCuotas[posicionSorteo]}") 
    
    # Borro todas las entradas del cliente ganador
    while nombreEliminar in _baseDeNombres:
         indice = _baseDeNombres.index(nombreEliminar)
         del _baseDeNombres[indice]
         del _baseDeCuotas[indice]
         del _baseDeCarrocerias[indice]

    return _baseDeNombres, _baseDeCuotas, _baseDeCarrocerias, _autosEntregados


def ingresoPorCarroceria(_baseDeCuotas, _baseDeCarrocerias):
    ingresoCarroceria = 0

    while True:
        carroceriaIngreso = input("De qué carrocería quieres revisar los ingresos?: [SEDAN|COUPE|FAMILIAR]: ").upper()
        if carroceriaIngreso in _baseDeCarrocerias:
            break
        print("Carrocería inexistente, vuelve a intentar!")

    # Sumo todas las cuotas del cliente
    for indice, carroceria in enumerate(_baseDeCarrocerias):
        if carroceria == carroceriaIngreso:
            ingresoCarroceria = ingresoCarroceria + _baseDeCuotas[indice]

    return ingresoCarroceria
    

def consultaAutosEntregados(_autosEntregados):
    print("Listado de autos entregados:")
    
    for autoEntregado in _autosEntregados:
        print(autoEntregado)

    return


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
#----------------------------------------------------------------------------------------------
...

# Bloque de menú
#----------------------------------------------------------------------------------------------
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Cargar nuevo pago de cuota")
        print("[2] Sortear auto!")
        print("[3] Ingresos por carrocería")
        print("[4] Autos entregados este año")
        print("[0] Salir del programa")
        print()
        opcion = int(input("Seleccione una opción: "))
        if opcion in range(0,5): # Sólo continua si se elije una opcion de menú válida
            break
        
    if opcion == 0: # Opción salir del programa
        exit()

    elif opcion == 1:   # Cargar nuevo pago de cuota
       baseDeNombres, baseDeCuotas, baseDeCarrocerias = cargarNuevoPagoCuota(baseDeNombres, baseDeCuotas, baseDeCarrocerias)
        
    elif opcion == 2:   # Sortear auto!
        baseDeNombres, baseDeCuotas, baseDeCarrocerias, autosEntregados = SortearAuto(baseDeNombres, baseDeCuotas, baseDeCarrocerias, autosEntregados)
        
    elif opcion == 3:   # Ingresos por carrocería
        ingreso = ingresoPorCarroceria(baseDeCuotas, baseDeCarrocerias)
        print(f"El importe total para esta carroceria es de ${ingreso}")
        
    elif opcion == 4:   # Autos entregados este año
        consultaAutosEntregados(autosEntregados)
        

    print()
    input("Presione ENTER para continuar.")


