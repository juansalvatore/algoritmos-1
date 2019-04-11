# Ejercicio 5.1. Escribir un programa que permita al usuario ingresar 
# un conjunto de notas, preguntando a cada paso si desea ingresar más notas, 
# e imprimiendo el promedio correspondiente.
from functools import reduce

def sumar(x1, x2): return x1 + x2
def promedio_notas():
    notas = []
    finalizar = 'si'
    while finalizar == 'si':
        nota = int(input('Ingrese una nota: '))
        notas.append(nota)
        print(reduce(sumar, notas) / len(notas))
        finalizar = input('Desea ingresar una nota mas? si/no ')

promedio_notas()