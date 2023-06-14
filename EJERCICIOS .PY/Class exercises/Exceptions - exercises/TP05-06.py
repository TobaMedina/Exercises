import random

numero_secreto = random.randint(1, 500)
intentos = 0

while True:
    intentos += 1
    try:
        numero_usuario = int(input("Adivina el número (entre 1 y 500): "))
        if numero_usuario == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif numero_usuario < numero_secreto:
            print("El número que debes adivinar es mayor.")
        else:
            print("El número que debes adivinar es menor.")
    except ValueError:
        print("Debes ingresar un número válido.")

