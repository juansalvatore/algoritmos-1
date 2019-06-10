# Ejercicio 10.2. Escribir un programa, llamado cp.py, que copie todo el contenido de un archivo
# (sea de texto o binario) a otro, de modo que quede exactamente igual.
# Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.


def cp(original, copia, maximo=1200):
    with open(original, 'rb') as o:
        test = o.read(maximo)
        print(test)
    with open(copia, 'wb') as c:
        c.write(test)


cp('texto.txt', 'texto2.txt')
