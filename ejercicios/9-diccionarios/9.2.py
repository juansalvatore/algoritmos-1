# Ejercicio 9.2. Diccionarios usados para contar.
# a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
# de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
# hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.

# b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una ca-
# dena de texto, y los devuelva en un diccionario.

# c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
# realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
# dados.
# Nota: utilizar el módulo random para obtener tiradas aleatorias.

def cantidad_de_palabras(str):
    dic = {}
    palabras =  str.lower().split(' ')
    for palabra in palabras:
        if dic.get(palabra, ''):
            dic[palabra] = dic[palabra] + 1
        else:
            dic[palabra] = 1
    return dic

# print(cantidad_de_palabras("Que lindo día que hace hoy hoy hoy"))

def cantidad_caracter(str):
    dic = {}
    letras = ''.join(str.lower().split(' '))
    for letra in letras:
        if dic.get(letra, ''):
            dic[letra] = dic[letra] + 1
        else:
            dic[letra] = 1
    return dic

# print(cantidad_caracter("ho hoy hoy"))

import random

def tirar_dados(iteraciones):
    dic = {}
    for i in range(iteraciones):
        suma = random.randint(1, 6) + random.randint(1, 6)
        if dic.get(suma, ''):
            dic[suma] = dic[suma] + 1
        else:
            dic[suma] = 1
    return dic

print(tirar_dados(6))