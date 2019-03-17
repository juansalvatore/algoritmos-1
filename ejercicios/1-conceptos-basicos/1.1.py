# Ejercicio 1.1. Escribir un programa que pregunte al usuario:
# a) Su nombre, y luego lo salude


def hola(nombre):
    return 'Hola ' + nombre


def saludar():
    nombre = input('Ingrese su nombre: ')
    saludo = hola(nombre)
    print(saludo)


print('Ejercicio 1-A')
saludar()

# B) Dos numeros y luego muestre el producto


def producto():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    print(n1 * n2)


print('\nEjercicio 1-B')
producto()
