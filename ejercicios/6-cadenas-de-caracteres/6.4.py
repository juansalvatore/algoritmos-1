# Ejercicio 6.4. Escribir una función que reciba una cadena que contiene un largo número
# entero y devuelva una cadena con el número y las separaciones de miles.
# Por ejemplo, si recibe '1234567890', debe devolver '1.234.567.890'.


def format_number(num):
    numero = list(str(num))
    resultado = []
    for i in range(len(numero)-1, -1, -1):
        if i % 3 == 0 and i != len(numero) - 1:
            resultado.insert(0, '.')
        resultado.insert(0, numero[i])
    return ''.join(resultado)


print(format_number(1234567890))
