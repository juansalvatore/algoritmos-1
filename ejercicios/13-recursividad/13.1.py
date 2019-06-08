# Ejercicio 13.1. Escribir una función recursiva que reciba un número positivo 𝑛 y devuelva la
# cantidad de dígitos que tiene.


def digitos(n):
    if n/10 < 1: 
        return 1
    return 1 + digitos(n/10)

print(digitos(1654))