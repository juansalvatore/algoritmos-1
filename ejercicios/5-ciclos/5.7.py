# Ejercicio 5.7. Números perfectos y números amigos
# a) Escribir una función que devuelva la suma de todos los divisores de un número 𝑛, sin
# incluirlo.
# b) Usando la función anterior, escribir una función que imprima los primeros 𝑚 números
# tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros 𝑚 números
# perfectos).
# c) Usando la primera función, escribir una función que imprima las primeras 𝑚 parejas
# de números (𝑎, 𝑏), tales que la suma de los divisores de 𝑎 es igual a 𝑏 y la suma de los
# divisores de 𝑏 es igual a 𝑎 (es decir las primeras 𝑚 parejas de números amigos).
# d) Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecución.


def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma


# print(suma_divisores(10))


def numeros_perfectos(m):
    numeros = []
    for i in range(1, m):
        if suma_divisores(i) == i:
            numeros.append(i)
    return numeros


# print(numeros_perfectos(10000))

def numeros_amigos(m):
    parejas = []
    for a in range(1, m):
        for b in range(1, m):
            if suma_divisores(a) == suma_divisores(b):
                parejas.append((a, b))

    return parejas


print(numeros_amigos(10))
