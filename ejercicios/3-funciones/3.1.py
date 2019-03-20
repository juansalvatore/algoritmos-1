# Ejercicio 3.1. 
# Escribir dos funciones que permitan calcular:
# a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
# b) La duración en horas, minutos y segundos de un intervalo dado en segundos
from helpers import get_int

def a_segundos(h, m , s):
    return h * 3600 + m * 60 + s

def calc_segundos():
    h = get_int('Horas: ')
    m = get_int('Minutos: ')
    s = get_int('Segundos: ')
    return a_segundos(h, m, s)

print('3.1) a) Ejercicio: ', calc_segundos())