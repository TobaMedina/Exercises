# Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que dicho  medio  de  transporte  utiliza  un  esquema  de  tarifas  decrecientes  (detalladas  en  la  tabla de  abajo)  se  solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.
# Cantidad de viajes: 1 a 20; 21 a 30; 31 a 40; 41 o más
# Valor del pasaje: Averiguar valor actualizado; 20% de descuento sobre tarifa máxima; 30% de descuento sobre tarifa máxima; 40% de descuento sobre tarifa máxima

def calcular_total_gastado(cantidad_viajes):
    tarifa_maxima = 10.0  
    total_gastado = 0.0

    if cantidad_viajes >= 1 and cantidad_viajes <= 20:
        total_gastado = cantidad_viajes * tarifa_maxima
    elif cantidad_viajes >= 21 and cantidad_viajes <= 30:
        total_gastado = cantidad_viajes * tarifa_maxima * 0.8
    elif cantidad_viajes >= 31 and cantidad_viajes <= 40:
        total_gastado = cantidad_viajes * tarifa_maxima * 0.7
    elif cantidad_viajes >= 41:
        total_gastado = cantidad_viajes * tarifa_maxima * 0.6

    return total_gastado


cantidad_viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))

total_gastado = calcular_total_gastado(cantidad_viajes)
print(f"Total gastado en viajes: ${total_gastado:.2f}")
