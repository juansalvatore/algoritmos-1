# Ejercicio 5.8. Escribir un programa que le pida al usuario que ingrese una sucesión de números
# naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de
# salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total
# de los valores y el promedio.
from statistics import mean


def app():
    numero = int(input('Ingrese un numero: '))
    numeros = []
    while numero != -1:
        if numero > 0:
            numeros.append(numero)
        numero = int(input('Ingrese un numero: '))

    return len(numeros), sum(numeros), mean(numeros)


print('cantidad: {}, suma: {}, promedio: {}'.format(*app()))
