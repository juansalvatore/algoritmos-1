# Ejercicio 2.6.
# Escribir un programa que tome una cantidad 𝑚 de valores ingresados por el usuario,
# a cada uno le calcule el factorial e imprima el resultado junto con el número 
# de orden correspondiente.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calcular_factoriales(*args):
    for i, elem in enumerate(args):
        print(i,'-', factorial(elem))

calcular_factoriales(2,4,5)