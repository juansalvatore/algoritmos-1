# Ejercicio 10.2. Escribir un programa, llamado cp.py, que copie todo el contenido de un archivo
# (sea de texto o binario) a otro, de modo que quede exactamente igual.
# Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.

def copy(archivo, copia):
    with open(archivo) as archivo: 
        with open(copia, 'w') as copia:
            copia.writelines(archivo)

copy('test.txt', 'copia.txt')