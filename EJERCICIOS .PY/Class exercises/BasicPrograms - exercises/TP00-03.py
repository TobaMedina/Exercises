# Escribir un programa básico de caja, donde se ingrese el precio total de la compra, luego se ingrese el monto con el cual el cliente abona la compra, y finalmente informe con un mensaje si no es suficiente con lo que abonó o, caso contrario, informe el vuelto que se le debe dar al cliente.

total = int(input("Ingrese el precio total: "))
abono = int(input("Ingrese la totalidad con la que abonara: "))

if total == abono:
    print("No se debe de dar vuelto")
elif total < abono:
    vuelto = abono - total
    print("El vuelto es: ")
    print(vuelto)
else:
    print("El dinero dado no es suficiente para pagar la compra")
    
        