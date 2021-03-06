# Ejercicio 2.1. 
# Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa
# de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula
# a utilizar es:
# 𝐶𝑛 = 𝐶 × (1 + 𝑥/100) 𝑛
# Donde 𝐶 es el capital inicial, 𝑥 es la tasa de interés y 𝑛 es el número de años a calcular.

from helpers import get_int

def calcular_monto(pesos, interes, años):
    return pesos * (1 + interes / 100) * años

def pedir_monto():
    pesos = get_int('Pesos: ')
    interes =  get_int('Tasa de interes: ')
    años = get_int('Años: ')
    return calcular_monto(pesos, interes, años)
    
print('2.1) Ejercicio:', pedir_monto())