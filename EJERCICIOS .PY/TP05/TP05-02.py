def obtenerMes(numero_mes):
    try:
        nombresMeses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        nombresMeses = nombresMeses[numero_mes -1]
        return nombresMeses
    except IndexError:
        return ""
    
nombre = obtenerMes(6)
print(nombre)
