# Ejercicio 5.10. Escribir una función que reciba un número natural e imprima todos los números
# primos que hay hasta ese número.


def es_primo(n):
    i = n - 1
    while i >= 2:
        if n % i == 0:
            return False
        i -= 1
    return True


def listar_primos(n):
    return list(filter(es_primo, list(range(1, n))))


print(listar_primos(20000))
