# Desarrollar  una  función  que  reciba tres  números enteros  positivos  y  verifique  si  corresponden  a  una  fecha  válida  (día, mes,  año).  Devolver  True  o  False  según  la  fecha  sea  correcta  o  no.  Realizar  también  un  programa  para  verificar  el comportamiento de la función.

def es_fecha_valida(dia, mes, anio):
    if not isinstance(dia, int) or not isinstance(mes, int) or not isinstance(anio, int):
        return False

    if dia <= 0 or mes <= 0 or anio <= 0:
        return False

    if mes > 12:
        return False

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
        dias_por_mes[1] = 29

    if dia > dias_por_mes[mes - 1]:
        return False

    return True



dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if es_fecha_valida(dia, mes, anio):
    print("La fecha es válida.")
else:
    print("La fecha no es válida.")
