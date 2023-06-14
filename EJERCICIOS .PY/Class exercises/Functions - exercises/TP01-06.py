# Escribir  una  función  diaSiguiente(...)  que  reciba  como  parámetro  una  fecha  cualquiera  expresada  por  tres  enteros (correspondientes al día, mes y año) y calcule y devuelva tres enteros correspondientes el día siguiente al dado. Utilizando esta función, desarrollar programas que permitan:
# A.Sumar N días a una fecha.
# B.Calcular la cantidad de días existentes entre dos fechas cualesquiera.

def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def obtener_dias_mes(mes, anio):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and es_bisiesto(anio):
        return 29
    return dias_mes[mes - 1]

def diaSiguiente(dia, mes, anio):
    if dia < obtener_dias_mes(mes, anio):
        return dia + 1, mes, anio
    elif mes < 12:
        return 1, mes + 1, anio
    else:
        return 1, 1, anio + 1

def sumar_dias(dia, mes, anio, n):
    for _ in range(n):
        dia, mes, anio = diaSiguiente(dia, mes, anio)
    return dia, mes, anio

def calcular_diferencia(dia1, mes1, anio1, dia2, mes2, anio2):
    diferencia = 0
    while dia1 != dia2 or mes1 != mes2 or anio1 != anio2:
        dia1, mes1, anio1 = diaSiguiente(dia1, mes1, anio1)
        diferencia += 1
    return diferencia

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
n = int(input("Ingrese la cantidad de días a sumar: "))

nuevo_dia, nuevo_mes, nuevo_anio = sumar_dias(dia, mes, anio, n)
print("La fecha resultante es:", nuevo_dia, nuevo_mes, nuevo_anio)

dia1 = int(input("Ingrese el primer día: "))
mes1 = int(input("Ingrese el primer mes: "))
anio1 = int(input("Ingrese el primer año: "))
dia2 = int(input("Ingrese el segundo día: "))
mes2 = int(input("Ingrese el segundo mes: "))
anio2 = int(input("Ingrese el segundo año: "))

diferencia = calcular_diferencia(dia1, mes1, anio1, dia2, mes2, anio2)
print("La cantidad de días entre las dos fechas es:", diferencia)
