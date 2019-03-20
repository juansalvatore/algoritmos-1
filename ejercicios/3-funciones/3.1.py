# Ejercicio 3.1. 
# Escribir dos funciones que permitan calcular:
# a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
from helpers import get_int, round_decimal

def a_segundos(h, m , s):
    return h * 3600 + m * 60 + s

def calc_segundos():
    h = get_int('Horas: ')
    m = get_int('Minutos: ')
    s = get_int('Segundos: ')
    return a_segundos(h, m, s)

# b) La duración en horas, minutos y segundos de un intervalo dado en segundos
def de_segundos(s):
    h = round_decimal(s / 3600)
    m = round_decimal((s - (h * 3600))/60)
    sec = round_decimal(s - (h * 3600) - (m * 60))
    return h, m, sec

print('\n3.1) b) Ejercicio: ', de_segundos(1432)) # Result: 00:23:52.

