# Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
# a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
# 's,e,p,a,r,a,r'
# b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
# debería devolver 'mi_archivo_de_texto.txt'
# c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
# 'X' debería devolver 'su clave es: XXXX'
# d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
# '255.255.255.0'


def insertar_caracter(str, c):
    str_res = list(str)
    return c.join(str_res)


# print(insertar_caracter('separar', ','))


def reemplazar_por_caracter(str, c):
    return c.join(str.split(' '))


# print(reemplazar_por_caracter('mi archivo de texto.txt', '_'))
def reemplazar_digitos(str, c):
    result = []
    for char in list(str):
        if char.isdigit():
            result.append(c)
        else:
            result.append(char)
    return ''.join(result)


# print(reemplazar_digitos('su clave es: 1540', 'X'))

def char_every_three_digits(str, c):
    for i, char in enumerate(list(str)):
        if i % 3 == 0 and i != 0:
            print(c, end=char)
        else:
            print(char, end='')
    print()


char_every_three_digits('2552552550', '.')
