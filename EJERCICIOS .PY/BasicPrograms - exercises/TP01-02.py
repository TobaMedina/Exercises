# Realizar  un  programa  que  permita  ingresar  la  cantidad  de  inscriptos  a  una  conferencia  y  la  cantidad  de  asientos disponibles en el auditorio. Se debe indicar si alcanzan los asientos. Si los asientos no alcanzan, indicar cuantos faltan para que todos los inscriptos puedan sentarse. 

inscriptos = int(input("Ingrese la cantidad de inscriptos: "))
asientos = int(input("Ingrese la cantidad de asientos: "))

if asientos < inscriptos:
    faltante = inscriptos - asientos
    print("Los asientos disponibles no son suficientes, hay un faltante de: ")
    print(faltante)
else:
    print("Los asientos disponibles son suficientes")