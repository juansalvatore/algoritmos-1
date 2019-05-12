# Ejercicio 10.1. Escribir un programa, llamado head que reciba un archivo y un número N e
# imprima las primeras N líneas del archivo.

def head(archivo, n):
    count = 0
    with open(archivo) as arch:
        for linea in arch:
            if count == n: return
            print(linea.rstrip('\n'))
            count += 1

head('test.txt', 3)

