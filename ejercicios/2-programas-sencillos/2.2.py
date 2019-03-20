# Ejercicio 2.2. 
# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
# Celsius. Recordar que la fórmula para la conversión es: 𝐹 = 9/5𝐶 + 32
from helpers import get_int, round_decimal

def fahrenheit_to_celsius():
    temperature = get_int('Temperature: ')
    return round_decimal(((temperature - 32) * 5) / 9) + 'C'

print('2.2) Ejercicio:', fahrenheit_to_celsius())