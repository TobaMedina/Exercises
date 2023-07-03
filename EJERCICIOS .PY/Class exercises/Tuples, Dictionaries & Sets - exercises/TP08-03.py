# Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve Trueo False. Escribir también un programa para verificar su comportamiento.

def fichas_encajan(ficha1, ficha2):
    if ficha1[0] == ficha2[0] or ficha1[1] == ficha2[1]:
        return True
    else:
        return False

ficha1 = (3, 4)
ficha2 = (5, 4)
encajan = fichas_encajan(ficha1, ficha2)
print(encajan)
