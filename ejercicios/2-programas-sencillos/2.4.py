# Ejercicio 2.4. 
# Escribir un programa que imprima todos los números pares entre dos números
# que se le pidan al usuario.
from helpers import get_int
from helpers import esPar

def numerosPares():
    n1 = get_int('Numero 1: ')
    n2 = get_int('Numero 2: ')

    for i in range(n1, n2+1):
        if esPar(i):
            print(i)

numerosPares()