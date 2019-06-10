# Ejercicio 13.9. Escribir una función recursiva para replicar los elementos de una lista
# una cantidad n de veces. Por ejemplo:
# replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])


def replicar(lista, n):
    arr = []
    if len(lista) == 1:
        return lista * n
    else:
        arr += lista[:1] * n
        del lista[0]
    return arr + replicar(lista, n)


print(replicar([1, 3, 3, 7], 2))
