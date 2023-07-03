# Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto luego de  cada eliminación. Finalizar el proceso al ingresar -1. Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.

conjunto = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

while True:
    try:
        valor = int(input("Ingrese un valor a eliminar (-1 para salir): "))
        if valor == -1:
            break
        conjunto.remove(valor)
        print("Contenido del conjunto:", conjunto)
    except KeyError:
        print("El valor ingresado no existe en el conjunto.")

print("Final del programa.")
