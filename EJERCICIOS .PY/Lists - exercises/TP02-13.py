# Resolver el siguiente problema, utilizando funciones: Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga.
# Se solicita:
# a.Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola vez en el informe).
# b.Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los registros de entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron.

def registro():
    lista = []
    numero = int(input("Ingrese el numero de socio: "))
    while True:
        if numero == 0:
            break
        if numero < 10000 or numero > 99999:
            print("El numero de socio ingresado no es valido, por favor ingrese uno correcto.")
            numero = int(input("Ingrese el numero de socio: "))
        else: 
            lista.append(numero)
            numero = int(input("Ingrese el numero de socio: "))
    return lista
    
def contador(lista):
    socios = []
    for socio in lista:
        if socio not in socios:
            socios.append(socio)
            ingresos = lista.count(socio)
            print(f"El socio {socio} ingresó {ingresos} veces al club.")
            
def eliminar(socios):
    baja = int(input("Ingrese el numero de socio que desea dar de baja: "))
    antes = len(socios)
    socios = [socio for socio in socios if socio != baja]
    despues = len(socios)
    print(f"El socio {baja} ha sido eliminado.")
    print(f"Antes de la eliminacion del socio {baja}, los registros de entrada eran de: {antes}")
    print(f"Los registros de entrada luego de la eliminacion del socio {baja} son de: {despues}")
    

lista = registro()
ingresos = contador(lista)
eliminado = eliminar(lista)

