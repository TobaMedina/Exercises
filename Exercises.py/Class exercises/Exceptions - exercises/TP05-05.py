lista_numeros = []
errores = 0

while True:
    numero = int(input("Ingresa un número entero (-1 para terminar): "))
    if numero == -1:
        break
    lista_numeros.append(numero)

while errores < 3:
    try:
        elemento = int(input("Ingresa un elemento para buscar su posición: "))
        posicion = lista_numeros.index(elemento)
        print(f"El elemento {elemento} se encuentra en la posición {posicion}.")
    except ValueError:
        errores += 1
        print("El elemento no pertenece a la lista. Inténtalo nuevamente.")
        if errores == 3:
            print("Se han producido 3 errores. Abortando el proceso.")
            break
