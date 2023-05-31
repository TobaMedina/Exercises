# Escribir una función que reciba un número de mes y devuelva una cadena con el nombre del mes. Probar la función desde un programa principal con un input para la entrada del número de mes, luego la llamada a la función con dicho número como argumento, y finalmente un print de lo que la función devuelve.

def meses(a):
    if a == 1:
        mes = "Enero"
        return mes
    elif a == 2:
        mes = "Febrero"
        return mes
    elif a == 3:
        mes = "Marzo"
        return mes
    elif a == 4:
        mes = "Abril"
        return mes
    elif a == 5:
        mes = "Mayo"
        return mes
    elif a == 6:
        mes = "Junio"
        return mes
    elif a == 7:
        mes = "Julio"
        return mes
    elif a == 8:
        mes = "Agosto"
        return mes
    elif a == 9:
        mes = "Septiembre"
        return mes
    elif a == 10:
        mes = "Octubre"
        return mes
    elif a == 11:
        mes = "Noviembre"
        return mes
    elif a == 12:
        mes = "Diciembre"
        return mes
    else:
        return "El numero ingresado no corresponde a ningun mes"
        
num = int(input("Ingrese el numero de mes: "))
mes = meses(num)
print(mes)