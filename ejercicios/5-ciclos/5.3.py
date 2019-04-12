# Ejercicio 5.3. Manejo de contraseñas
# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario
# la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
# c) Modificar el programa anterior para que después de cada intento agregue una pausa
# cada vez mayor, utilizando la función sleep del módulo time.
# d) Modificar el programa anterior para que sea una función que devuelva si el usuario
# ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).
from time import sleep


def programa_login():
    password = input('Ingresar contraseña: ')
    counter = 0
    while password != '42':
        counter += 1
        if counter == 3:
            return False
        password = input('Ingresar contraseña: ')
    return True


print(programa_login())
