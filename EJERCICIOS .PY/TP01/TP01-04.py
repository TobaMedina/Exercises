# Un banco necesita establecer los nuevos límites de crédito de sus tarjetas. Las de tipo 1 aumentarán un 25%; las de tipo 2 aumentarán un 35%; las de tipo 3 aumentarán un 40%, y las de cualquier otro tipo aumentarán un 50%. Desarrollar un algoritmo para calcular el nuevo límite según el límite actual y el tipo de tarjeta del cliente.

limite = int(input("Ingrese limite actual de su tarjeta: "))
tipo = int(input("Ingrese su tipo de tarjeta: "))

if tipo == 1:
    limiteNuevo = limite * 1.25
elif tipo == 2:
    limiteNuevo = limite * 1.35
elif tipo == 3:
    limiteNuevo = limite * 1.40
else:
    limiteNuevo = limite * 1.50
    
print("El nuevo limite de tarjeta es de: ")
print(limiteNuevo)

