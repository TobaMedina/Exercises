# Realizar  un  programa  que  solicite  la  carga  de  las  temperaturas  de  todos  los  días  de  enero  y  al  finalizar  devuelva  la temperatura promedio, máxima y mínima del mes.

acum = 0
cont = 0
maxima = 0
minima = 9999999
for i in range(31):
    grados = float(input("Ingrese la temperatura del dia: "))
    cont += 1
    acum = acum + grados
    if grados > maxima:
        maxima = grados
    if grados < minima:
        minima = grados
        
promedio = acum / cont    
print("La temperatura promedio de Enero fue de: ", promedio)
print("La temperatura maxima del mes de enero fue de: ", maxima, " y la minima fue de: ", minima)
