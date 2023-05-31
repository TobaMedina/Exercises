def suma_numeros_reales(cadena1, cadena2):
    try:
        numero1 = float(cadena1)
        numero2 = float(cadena2)
        resultado = numero1 + numero2
        return resultado
    except ValueError:
        return -1

resultado = suma_numeros_reales("23123", "ABABABABA")
print(resultado)