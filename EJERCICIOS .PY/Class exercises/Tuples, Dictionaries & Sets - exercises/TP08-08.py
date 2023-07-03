# Escribir una función que reciba un número entero N y devuelva un diccionario con la tabla de multiplicar de N del 1 al 12. Escribir también un programa para probar la función.

def tabla_multiplicar(N):
    tabla = {}
    for i in range(1, 13):
        tabla[i] = N * i
    return tabla

# Programa de prueba
numero = int(input("Ingrese un número entero: "))
tabla_de_multiplicar = tabla_multiplicar(numero)
for key, value in tabla_de_multiplicar.items():
    print(f"{numero} x {key} = {value}")
