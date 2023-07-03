# Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.

def ordenar_palabras(frase):
    palabras = frase.split()
    palabras_unicas = set(palabras)
    palabras_ordenadas = sorted(palabras_unicas, key=len)
    return palabras_ordenadas

frase = input("Ingrese una frase: ")

palabras_ordenadas = ordenar_palabras(frase)

for palabra in palabras_ordenadas:
    print(palabra)
