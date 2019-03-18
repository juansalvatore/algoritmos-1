# Ejercicio 2.7. 
# Escribir un programa que imprima por pantalla todas las fichas de dominó, de
# una por línea y sin repetir.
def domino():
    for i in range(0, 7):
        for j in range(0, 7):
            print(i, j)

domino()