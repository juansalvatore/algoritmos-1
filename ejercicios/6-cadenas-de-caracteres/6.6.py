# Ejercicio 6.6. Escribir funciones que dada una cadena de caracteres:
# a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
# 'logaritmos' debe devolver 'lgrtms'.
# b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
# devolver 'i ooae'.
# c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
# devolver 'vistaerou'.
# d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un
# palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).


def es_consonante(char):
    return char not in ['a', 'e', 'i', 'o', 'u']


def es_vocal(char):
    return char in ['a', 'e', 'i', 'o', 'u']


def consonates(str):
    return ''.join(filter(es_consonante, list(str)))


def vocales(str):
    return ''.join(filter(es_vocal, list(str)))


print(vocales('algoritmos'))


def reverse_string(str):
    word = list(str)
    result = []
    for i in range(len(str) - 1, -1, -1):
        result.append(word[i])
    return ''.join(result)


def es_palindromo(str):
    word = ''.join(str.split(' '))
    return word == reverse_string(word)


print(es_palindromo('anita lava la tina'))
