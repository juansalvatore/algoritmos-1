# Ejercicio 10.4. Escribir un programa, llamado wc.py que reciba un archivo, lo procese e imprima
# por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.


def wc(arch):
    with open(arch) as f:
        lineas = [linea.rstrip('\n') for linea in f]
        palabras_suma = 0
        letras_suma = 0
        for linea in lineas:
            palabras = linea.split(' ')
            palabras_suma += len(palabras)
            for palabra in palabras:
                letras_suma += len(palabra)
        print(
            f'lineas: {len(lineas)}, palabras: {palabras_suma}, caracteres: {letras_suma}')


wc('wc.txt')
