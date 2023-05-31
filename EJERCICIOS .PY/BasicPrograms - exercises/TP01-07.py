# Escribir un programa que, ingresado el precio de lista de un producto, muestre cuanto le costará al cliente según todas las  opciones  de  pago disponibles  (si  es  en  cuotas  además  del  precio  final  debe  mostrar  el  valor  de  cada  cuota).  Los descuentos o recargos según las formas de pago son los siguientes:
# En efectivo aplicar 10% de descuento
# Tarjeta 1 pago mantener el precio de lista
# Tarjeta 3 pagos recargar 5%
# Tarjeta 6 pagos recargar 10%
# Tarjeta 12 pagos recargar 15%
# Una vez mostrados los valores, el algoritmo debe esperar un nuevo ingreso, y sólo debe finalizar si se ingresa un precio de 0 pesos (en dicho caso debe terminar sin calcular nada). Se pide usar un tipo de bucle que evite tener que escribir el input dos veces.

precio = int(input("Ingrese el precio: "))

while precio != 0:
    efectivo = precio - (precio * 0.1)
    tarjeta3 = precio * 1.05
    tarjeta6 = precio * 1.1
    tarjeta12 = precio * 1.15
    cuotas3 = tarjeta3 / 3
    cuotas6 = tarjeta6 / 6
    cuotas12 = tarjeta12 / 12
    
    print("El pago en efectivo tendria un valor de: ", efectivo)
    print("El pago en 1 cuota tendria un valor de: ", precio)
    print("El pago en 3 cuotas tendria un valor de: ", tarjeta3, ". Cada cuota tendria un valor de: ", cuotas3)
    print("El pago en 6 cuotas tendria un valor de: ", tarjeta6, ". Cada cuota tendria un valor de: ", cuotas6)
    print("El pago en 12 cuotas tendria un valor de: ", tarjeta12, ". Cada cuota tendria un valor de: ", cuotas12)
    precio = int(input("Ingrese el precio: "))


