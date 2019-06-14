# 3) a) Mostrar paso a paso como funcionarıan los algoritmos de insercion y quicksort sobre
# la siguiente lista de numeros: [9, 12, 1, 4, 2, 8, 15, 21]
# b) ¿Cual de los dos algoritmos es mas eficiente para ordenar una gran cantidad de elementos?


def ord_insercion(lista):
    for i in range(1, len(lista)):
        val_actual = lista[i]
        pos = i
        while pos > 0 and lista[pos - 1] > val_actual:
            lista[pos] = lista[pos - 1]
            pos -= 1
        lista[pos] = val_actual
    return lista


print(ord_insercion([9, 12, 1, 4, 2, 8, 15, 21]))

# VER QUICKSORT
