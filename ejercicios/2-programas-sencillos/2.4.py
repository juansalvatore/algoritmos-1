# Ejercicio 2.4. 
# Escribir un programa que imprima todos los números pares entre dos números
# que se le pidan al usuario.
from helpers import get_int, es_par

def numeros_pares():
    n1 = get_int('Numero 1: ')
    n2 = get_int('Numero 2: ')

    for i in range(n1, n2+1):
        if es_par(i):
            print(i)

numeros_pares()