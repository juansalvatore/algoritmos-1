# Ejercicio 10.5. Escribir un programa, llamado grep.py que reciba una expresión y un archivo e
# imprima las líneas del archivo que contienen la expresión recibida.


def grep(exp, arch):
    with open(arch) as f:
        for linea in f:
            linea = linea.rstrip('\n')
            if len(linea.split(exp)) != 1:
                print(linea)


grep('estas', 'wc.txt')
