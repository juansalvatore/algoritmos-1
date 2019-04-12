# Ejercicio 7.2. Dominó.
# a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
# recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
# b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
# recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las
# cadenas.


def encajan(t1, t2):
    return t1[0] == t2[0] or t1[0] == t2[1] or t2[0] == t1[1] or t2[1] == t1[1]


print(encajan((3, 4), (5, 5)))
