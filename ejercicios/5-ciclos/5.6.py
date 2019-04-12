# Ejercicio 5.6. Potencias de dos.
# a) Escribir una función es_potencia_de_dos que reciba como parámetro un número natural,
# y devuelva True si el número es una potencia de 2, y False en caso contrario.
# b) Escribir una función que, dados dos números naturales pasados como parámetros,
# devuelva la suma de todas las potencias de 2 que hay en el rango formado por
# esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función
# es_potencia_de_dos, descripta en el punto anterior.


def es_potencia_de_dos(num):
    return num != 0 and ((num & (num - 1)) == 0)


print(es_potencia_de_dos(4))


def suma_potencias_de_dos(n1, n2):
    suma = 0
    for i in range(n1, n2 + 1):
        if es_potencia_de_dos(i):
            print(i)
            suma += i
    return suma


print(suma_potencias_de_dos(1, 8))
