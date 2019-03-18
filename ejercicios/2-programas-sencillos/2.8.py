# Ejercicio 2.8.
# Modificar el programa anterior para que pueda generar fichas de un juego que
# puede tener números de 0 a 𝑛.
def domino(n):
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            print(i, j)

domino(7)