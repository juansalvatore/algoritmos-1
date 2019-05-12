# Ejercicio 10.7. Persistencia de un diccionario
# a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido
# tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave
# y el segundo como diccionario.
# b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo,
# y guarde el contenido del diccionario en el archivo, con el formato clave, valor.

import csv


def cargar_datos(arch):
    dic = {}
    with open(arch) as a:
        archivo_csv = csv.reader(a)
        encabezado = next(archivo_csv)
        for clave, valor in archivo_csv:
            dic[clave] = valor
    print(dic)


cargar_datos('10.7.txt')


def guardar_datos()
