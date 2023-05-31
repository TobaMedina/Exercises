# Intercalar  los  elementos  de  una  lista  entre  los  elementos  de  otra.  La  intercalación  deberá  realizarse  exclusivamente mediante la técnica de rebanadas y no se creará una lista nueva,sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].

def intercalar(lista1, lista2):
    n = len(lista1)
    for i in range(1, n+1):
        lista1[2*i-1:2*i-1] = lista2[i-1:i]


lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8]

intercalar(lista1, lista2)
print(lista1)