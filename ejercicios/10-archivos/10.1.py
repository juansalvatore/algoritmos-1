# Ejercicio 10.1. Escribir un programa, llamado head que reciba un archivo y un número N e
# imprima las primeras N líneas del archivo.


def head(arch, n):
    with open(arch) as f:
        for i, line in enumerate(f):
            if i == n:
                return
            line = line.rstrip('\n')
            print(line, i)


head('texto.txt', 2)
