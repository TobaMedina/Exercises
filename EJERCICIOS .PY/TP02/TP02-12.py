# Resolver el siguiente problema, diseñando las funciones a utilizar:
# Una  clínica  necesita  un  programa  para  atender  a  sus  pacientes.  Cada  paciente  que  ingresa  se  anuncia  en  la  recepción indicando su número de afiliado (número entero de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita:
# a.Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en el orden que llegaron a la clínica.
# b.Realizar la búsqueda de  un número de  afiliado e  informar cuántas veces  fue  atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado.

def busqueda(lista, lista2):
    while True:
        numero = int(input("Ingrese el numero de afiliado que desea buscar: "))
        
        if numero == -1:
            break
        
        urgencias = lista.count(numero)
        turnos = lista2.count(numero)
        
        print("El paciente con numero de afiliado: ", numero, " ha ingresado por urgencia: ", urgencias, " veces. Y por turno: ", turnos, " veces.")
    


listaAfiliado = []
listaUrgencia = []
listaTurno = []
numeroAfiliado = int(input("Ingrese numero de afiliado: "))
while numeroAfiliado != -1:
    if numeroAfiliado < 1000 or numeroAfiliado > 9999:
        print("El numero ingresado es incorrecto. Ingrese nuevamente")
        numeroAfiliado = int(input("Ingrese numero de afiliado: "))
    else:
        motivo = int(input("Ingrese 0 si tiene una emergencia o 1 si tiene un turno: "))
        if motivo == 0:
            listaUrgencia.append(numeroAfiliado)
            listaAfiliado.append(numeroAfiliado)
        elif motivo == 1:
            listaTurno.append(numeroAfiliado)
            listaAfiliado.append(numeroAfiliado)
        else:
            print("El motivo ingresado no esta dentro de los parametros")
        numeroAfiliado = int(input("Ingrese numero de afiliado: "))

print(listaAfiliado)
print("Los afiliados que visitaron la clinica por una urgencia fueron: ", listaUrgencia)
print("Los afiliados que visitaron la clinica con un turno fueron: ", listaTurno)

listaFinal = busqueda(listaUrgencia, listaTurno)
print(listaFinal)


