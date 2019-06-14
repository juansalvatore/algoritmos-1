# 12) Escribir una funcion recursiva en Python que cuente la cantidad de apariciones de un
# elemento en una lista recibidos por parametro.


def cantidad(cadena, c):
    total = 0
    if len(cadena) == 0:
        return 0
    if cadena[0] == c:
        total += 1
    return total + cantidad(cadena[1:], c)


print(cantidad("cadenacac", 'c'))
