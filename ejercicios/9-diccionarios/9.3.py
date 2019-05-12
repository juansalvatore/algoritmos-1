# Ejercicio 9.3. Continuación de la agenda.
# Escribir un programa que vaya solicitando al usuario que ingrese nombres.
# a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
# el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# El usuario puede utilizar la cadena ”*”, para salir del programa.

def agenda():
    agenda = {}
    while True:
        nombre = input('ingresar el nombre o "*" para salir del programa: ').lower()
        if nombre == '*':
            return
        if agenda.get(nombre, ''):
            print(agenda[nombre])
            if(input('¿Desea modificar el numero? si/no ').lower() == 'si'):
                agenda[nombre] = input('Ingrese el nuevo numero: ')
        else:
            numero = input('Ingresar un numero: ')
            agenda[nombre] = numero

agenda()
