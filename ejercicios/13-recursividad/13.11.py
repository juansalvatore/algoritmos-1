# Ejercicio 13.11. El triángulo de Pascal es un arreglo triangular de números que se define de la
# siguiente manera: Las filas se enumeran desde 𝑛 = 0, de arriba hacia abajo. Los valores de cada
# fila se enumeran desde 𝑘 = 0 (de izquierda a derecha). Los valores que se encuentran en los
# bordes del triángulo son 1. Cualquier otro valor se calcula sumando los dos valores contiguos
# de la fila de arriba.
# 𝑛 = 0        1
# 𝑛 = 1       1 1
# 𝑛 = 2      1 2 1
# 𝑛 = 3     1 3 3 1
# 𝑛 = 4    1 4 6 4 1
# 𝑛 = 5   1 5 10 10 5 1
# 𝑛 = 6  1 6 15 20 15 6 1
# Escribir la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n
# y la columna k. Ejemplo: pascal(5, 2) -> 10


def pascal(n, k):
    arr = []
    if n == k:
        arr += [1]


print(pascal(5, 2))
