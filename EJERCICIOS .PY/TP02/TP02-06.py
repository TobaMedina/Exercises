# Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

def listaFinal(lista1, lista2):
    listaResultante = []
    for palabra in lista1:
        if palabra not in lista2:
            listaResultante.append(palabra)
    return listaResultante
            
listaOriginal = ["Es", "Chau", "Muy", "Todo", "Mes"]
listaEliminar = ["Chau", "Todo"]

lista = listaFinal(listaOriginal, listaEliminar)

print(listaOriginal)
print(listaEliminar)
print(lista)
