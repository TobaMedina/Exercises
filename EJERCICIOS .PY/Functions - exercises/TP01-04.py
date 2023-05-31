# Un comercio de electrodomésticos necesita para su línea  de  cajas un programa que  le indique  al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cadadenominación deben ser entregados al cliente como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensajede  error si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es  de  $317 y se  abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.

def calcular_vuelto(total_compra, dinero_recibido):
    denominaciones = [500, 100, 50, 20, 10, 5, 1]
    vuelto = dinero_recibido - total_compra
    billetes_entregados = {}

    if vuelto < 0:
        return "Error: El dinero recibido es insuficiente."

    for denominacion in denominaciones:
        cantidad_billetes = vuelto // denominacion
        if cantidad_billetes > 0:
            billetes_entregados[denominacion] = cantidad_billetes
            vuelto -= cantidad_billetes * denominacion

    return billetes_entregados


total_compra = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))

vuelto = calcular_vuelto(total_compra, dinero_recibido)
if isinstance(vuelto, str):
    print(vuelto)
else:
    print("Cantidad de billetes a entregar como vuelto:")
    for denominacion, cantidad in vuelto.items():
        print(f"{cantidad} billete(s) de ${denominacion}")
