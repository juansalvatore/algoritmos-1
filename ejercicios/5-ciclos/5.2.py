# Ejercicio 5.2. Escribir una función que reciba un número entero 𝑘 e imprima su descomposición
# en factores primos.


def desc_en_factores_primos(n):
    primos = lista_de_primos(n)
    counter = 1
    result = []
    while n != 1:
        if n % primos[counter] == 0:
            n = n / primos[counter]
            result.append(primos[counter])
        else:
            counter += 1
    return result


def lista_de_primos(n):
    numeros = range(n)
    return list(filter(es_primo, numeros))


def es_primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


print(desc_en_factores_primos(200))
