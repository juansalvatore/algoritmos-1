# Ejercicio 5.9. Escribir una función que reciba dos números como parámetros,
# y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.
# a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que
# sea mayor que el segundo. ??????????????????
# c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?
????????????


def multiplos(a, b):
    count = 0
    for i in range(a, b):
        if i % a == 0:
            count += 1
    return count


print(multiplos(2, 20))


def multiplos_while(a, b):
    count = 0
    while a < b:
        count += 1
        a *= a
    return count


print(multiplos_while(2, 20))
