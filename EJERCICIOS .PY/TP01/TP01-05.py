# En un mercado los clientes pueden comprar sólo una unidad de cada producto. Realizar un programaque pida uno por uno los precios de los productos comprados por el cliente, y que al ingresar un precio igual a cero muestre el total que debe abonar por la compra y la cantidad de productos comprados.

precio = int(input("Ingrese el precio del producto: "))
total = 0
while precio != 0:
    total = total + precio
    precio = int(input("Ingrese el precio del producto: "))

print("El total a abonar es de: ")
print(total)