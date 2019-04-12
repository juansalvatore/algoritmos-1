# Ejercicio 6.8. Escribir una función que reciba una cadena de unos y ceros (es decir, un número
# en representación binaria) y devuelva el valor decimal correspondiente


def binary_to_decimal(str):
    binary = list(str)
    count = 0
    result = 0
    for i in range(len(binary) - 1, -1, -1):
        if binary[i] == '1':
            result += 2**count
        count += 1
    return result


print(binary_to_decimal('11001'))
