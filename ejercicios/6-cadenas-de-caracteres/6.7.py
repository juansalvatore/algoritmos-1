# Ejercicio 6.7. Escribir funciones que dadas dos cadenas de caracteres:
# a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
# es una subcadena de 'subcadena'.
# b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
# debe devolver 'gnome'.


def es_subcadena(str1, str2):
    return str1.split(str2) != [str1]


# print(es_subcadena('subcadena', 'cadena'))


def orden(str1, str2):
    if str1 < str2:
        return str1
    return str2


print(orden('kde', 'gnome'))
