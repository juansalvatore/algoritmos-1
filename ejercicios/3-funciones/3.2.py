# Ejercicio 3.2.
# Usando las funciones del ejercicio anterior, escribir un programa que pida 
# al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, 
# y muestre por pantalla la duración total en horas, minutos y segundos.
from helpers import get_int, round_decimal

def a_segundos(h, m , s):
    return h * 3600 + m * 60 + s

def calc_segundos():
    h = get_int('Horas: ')
    m = get_int('Minutos: ')
    s = get_int('Segundos: ')
    return a_segundos(h, m, s)

def de_segundos(s):
    h = round_decimal(s / 3600)
    m = round_decimal((s - (h * 3600))/60)
    sec = round_decimal(s - (h * 3600) - (m * 60))
    return h, m, sec

def tiempo_total():
    return de_segundos(calc_segundos() + calc_segundos())

print(tiempo_total())