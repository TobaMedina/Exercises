import math
def funcion1(numero):
    try:
        if numero < 0:
            raise ValueError("No se puede calcular la raiz cuadrada del numero ingresado")
        raizCuadrada = math.sqrt(numero)
        return print(f"La raiz cuadrada del numero ingresado es {raizCuadrada}")
    except ValueError as error:
        print("Error: ", error)


numero = float(input("Ingrese el numero del que desea conocer su raiz cuadrada: "))
print(funcion1(numero))