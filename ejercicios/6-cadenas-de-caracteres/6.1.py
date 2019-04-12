# Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
# a) Imprima los dos primeros caracteres.
# b) Imprima los tres últimos caracteres.
# c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
# d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
# e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
# 'reflejoojelfer'.


def primeros_dos_caracteres(str):
    print(str[1:3])


# primeros_dos_caracteres('hola')


def ultimos_tres_caracteres(str):
    str_len = int(len(str))
    print(str[str_len - 3: str_len])


# ultimos_tres_caracteres('hola')


def de_a_dos_caracteres(str):
    for i in range(0, len(str), 2):
        print(str[i], end='')
    print()


# de_a_dos_caracteres('recta')


def reverse_string(str):
    rev = []
    for i in range(len(str) - 1, -1, -1):
        rev.append(str[i])
    return ''.join(rev)


# print(reverse_string('recta'))


def ambos_sentidos(str):
    print(str + reverse_string(str))


ambos_sentidos('recta')
