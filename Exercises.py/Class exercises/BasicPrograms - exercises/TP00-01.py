# Desarrollar un programa que calcule cuántos kilómetros podrá recorrer un auto de acuerdo con la cantidad de litros de combustible ingresados y al tipo de camino indicado (ruta o ciudad). Rendimiento de l vehículo:14.1 km por litro en ruta10.3 km por litro en ciudad

litros = int(input("Ingresar cantidad de litros de combustible: "))
camino = str(input("Ingrese tipo de camino a transitar, siendo las opciones RUTA o CIUDAD: "))

while camino != "ruta" and camino != "ciudad":
    print("Ingrese un camino valido")
    camino = str(input("Ingrese tipo de camino a transitar, siendo las opciones RUTA o CIUDAD: "))
    

if camino == "ruta":
    rendimiento = litros * 14.1
else:
    rendimiento = litros * 10.3
    
print("La cantidad de kilometros que el vehiculo podra recorrer es de: ")
print(rendimiento)
