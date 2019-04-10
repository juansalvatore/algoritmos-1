# Ejercicio 4.1. Escribir dos funciones que resuelvan los siguientes problemas:
# a) Dado un número entero 𝑛, indicar si es par o no.
# b) Dado un número entero 𝑛, indicar si es primo o no

def es_par(n):
    return n % 2 == 0

def es_primo(n):
    if(n < 1):
        return False

    for i in range(2, n):
        if(n % i == 0):
            return False

    return True

print(es_primo(-2))