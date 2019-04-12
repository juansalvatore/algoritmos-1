# Ejercicio 7.1. Escribir una función que reciba una tupla de elementos e indique si se encuentran
# ordenados de menor a mayor o no.


def esta_ordenado(tupla):
    return tupla == tuple(sorted(tupla))


print(esta_ordenado((1, 3, 2, 4)))
