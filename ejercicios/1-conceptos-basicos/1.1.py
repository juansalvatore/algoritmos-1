from helpers import ejercicio
# Ejercicio 1.1 
# a) Preguntar nombre, y luego lo salude
def hola(nombre):
    return 'Hola ' + nombre

def saludar():
    nombre = input('Ingrese su nombre: ')
    saludo = hola(nombre)
    return saludo

ejercicio('1.1) a) Saludar:', saludar())

# B) Dos numeros y luego muestre el producto
def producto():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    return n1 * n2

ejercicio('1.1) b) Rroducto de dos numeros:', producto())
