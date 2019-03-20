from helpers import ejercicio, get_int
# Ejercicio 1.1 
# a) Preguntar nombre, y luego lo salude
def hola(nombre):
    return 'Hola ' + nombre

def saludar():
    nombre = input('Ingrese su nombre: ')
    return hola(nombre)

ejercicio('1.1) a) Saludar:', saludar())

# B) Dos numeros y luego muestre el producto
def producto():
    n1 = get_int('Numero 1: ')
    n2 = get_int('Numero 2: ')
    return n1 * n2

ejercicio('1.1) b) Rroducto de dos numeros:', producto())
