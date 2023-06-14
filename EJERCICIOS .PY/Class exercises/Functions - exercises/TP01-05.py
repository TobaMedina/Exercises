# Desarrollar una función que reciba como parámetros dos números enteros positivosy devuelva el número que resulte de concatenar ambos valores. Por ejemplo, sirecibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades dePython no vistas en clase, ni tampoco concatenar strings mediante la conversión de número a cadena.

def concatenar_numeros(num1, num2):
    digitos_num2 = 0
    temp = num2
    while temp > 0:
        digitos_num2 += 1
        temp //= 10

    num1 *= 10 ** digitos_num2

    resultado = num1 + num2

    return resultado


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultado = concatenar_numeros(numero1, numero2)
print("El número resultante de la concatenación es:", resultado)
