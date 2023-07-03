# Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12,10,17) devuelve "12 de octubre de 2017". Escribir también un programa para verificar su comportamiento.

def fecha_extendida(fecha):
    meses = {
        1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
        5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
        9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }

    dia, mes, año = fecha
    fecha_extendida = f"{dia} de {meses[mes]} de {año}"
    return fecha_extendida

fecha = (12, 10, 2017)
fecha_en_formato_extendido = fecha_extendida(fecha)
print(fecha_en_formato_extendido)
