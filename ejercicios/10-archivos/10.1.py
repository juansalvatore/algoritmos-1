# Ejercicio 10.1. Escribir un programa, llamado head que reciba un archivo y un número N e
# imprima las primeras N líneas del archivo.

<<<<<<< HEAD
def head(archivo, n):
    count = 0
    with open(archivo) as arch:
        for linea in arch:
            if count == n: return
            print(linea.rstrip('\n'))
            count += 1

head('test.txt', 3)

=======

def head(arch, n):
    with open(arch) as f:
        for i, line in enumerate(f):
            if i == n:
                return
            line = line.rstrip('\n')
            print(line, i)


head('texto.txt', 2)
>>>>>>> 11a94b7d5035e4d2a4d9e989307d44c17fc04304
