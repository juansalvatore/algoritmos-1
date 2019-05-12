# Ejercicio 9.1. 
# Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
# en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
# segundos.

# Por ejemplo:
# >>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
# >>> print(tuplas_a_diccionario(l))
# { 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }

def tuplas_a_diccionario(l):
    dic = {}
    for tupla in l:
        if dic.get(tupla[0], ''):
            dic[tupla[0]] = [*dic[tupla[0]], tupla[1]]
        else:
            dic[tupla[0]] = [tupla[1]]
    return dic

print(tuplas_a_diccionario([ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]))