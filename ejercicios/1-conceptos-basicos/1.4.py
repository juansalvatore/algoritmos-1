from helpers import ejercicio

# Ejercicio 1.4. 
# Implementar un algoritmo que, dado un número entero 𝑛, permita calcular su factorial.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i 
    return result

ejercicio('1.4) Factorial:', factorial(8))
