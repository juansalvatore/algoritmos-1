<<<<<<< HEAD
# Ejercicio 10.3. 
# Escribir un programa, llamado cut.py, que dado un archivo de texto, un delimi-
# tador, y una lista de campos, imprima solamente esos campos, separados por ese delimitador.

def cut(archivo, delimitador, campos):
    with open(archivo) as archivo:
        for line in archivo:
            line = line.rstrip('\n').split(delimitador)
            test = campos.index(line)
            print(test)

cut('test.txt', ',', ['titulo', 'rate'])
=======
# Ejercicio 10.3.
#
# Escribir un programa, llamado cut.py, que dado un archivo de texto, un delimi-
# tador, y una lista de campos, imprima solamente esos campos, separados por ese delimitador.


def cut(arch, delimitador, campos):
    with open(arch) as f:
        primera_linea = f.readline().rstrip('\n').split(delimitador)
        indices = [primera_linea.index(campo) for campo in campos]
        for linea in f:
            linea_filtrada = [linea.rstrip('\n').split(
                delimitador)[indice] for indice in indices]
            print(delimitador.join(linea_filtrada))


cut('texto.txt', ',', ['nombre', 'apellido'])
>>>>>>> 11a94b7d5035e4d2a4d9e989307d44c17fc04304
