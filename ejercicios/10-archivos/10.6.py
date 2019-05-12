# Ejercicio 10.6. Escribir un programa, llamado rot13.py que reciba un archivo de texto de origen
# y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada
# en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter com-
# prendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo
# caracter.
from string import ascii_lowercase


def cifrado(line):
    new_line = ''
    for palabra in line:
        for letra in palabra:
            try:
                new_line += ascii_lowercase[(
                    ascii_lowercase.index(letra) + 13) % 26]
            except Exception:
                new_line += letra
    return new_line


def rot(origen, destino):
    with open(destino, 'w') as d:
        with open(origen) as o:
            for line in o:
                line = line.rstrip('\n')
                new_line = cifrado(line)
                d.write(new_line + '\n')


rot('wc.txt', 'cifrado.txt')
