# Ejercicio 5.4. Utilizando la función randrange del módulo random, escribir un programa que
# obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
# si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
# correcto.
from random import randrange


def get_number():
    return int(input('Ingrese un numero: '))


def app():
    random_num = randrange(0, 10)
    guess = get_number()
    while guess != random_num:
        if guess > random_num:
            print('Number is lower')
        else:
            print('Number is higher')
        guess = get_number()
    print('You found the number!', random_num)


app()
