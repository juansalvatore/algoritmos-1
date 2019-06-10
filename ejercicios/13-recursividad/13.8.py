# Ejercicio 13.8. Escribir una funcion recursiva que encuentre el mayor elemento de una lista.


def mayor(lista):
    length = len(lista)
    if length == 1:
        return lista[0]
    elif lista[length - 1] <= lista[length - 2]:
        del lista[length - 1]
    elif lista[length - 1] >= lista[length - 2]:
        del lista[length - 2]
    return mayor(lista)


lista = [1, 10, 3, 4, 5]
print(mayor(lista))
print(lista)
