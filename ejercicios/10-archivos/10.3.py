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