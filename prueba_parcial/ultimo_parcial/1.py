# 2) Escribir una funcion recursiva que reciba una lista y un parametro n, y devuelva otra
# lista con los elementos de la lista replicados esa cantidad n de veces.
# Por ejemplo, replicar ([1, 3, 3, 7], 2) debe devolver ([1, 1, 3, 3, 3, 3, 7, 7]) .


def replicar(lista, n):
    nueva_lista = []
    if len(lista) == 0:
        return lista
    else:
        nueva_lista += lista[:1] * n
    return nueva_lista + replicar(lista[1:], n)


lista = [1, 3, 3, 7]
print(replicar(lista, 2))
print(lista)
