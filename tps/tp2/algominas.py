from string import ascii_uppercase, ascii_lowercase
from random import randint

DIMENSIONES_TABLERO = [8, 8]
MINA = '*'
PLACEHOLDER = '.'
CANTIDAD_MINAS = 10


def crear_tablero(ancho, alto, placeholder='.'):
    """
        recibe dos integers correspondientes al alto y ancho y un string (placeholder) para llenar cada espacio.
        Devuelve una matriz de alto * ancho con un string placeholder en cada posición.
    """
    return [[' {} '.format(placeholder.strip()[0]) for col in range(ancho)] for row in range(alto)]


def mostrar_tablero(tablero):
    """
        recibe una matriz de n * n e imprime la matriz en forma de tablero rectangular n * n con numeros
        como referencia del eje horizontal y letras ascii_uppercase para el eje vertical.
    """
    print()
    for i in range(len(tablero) + 1):
        row = tablero[i - 1]
        if i != 0:
            print(ascii_uppercase[i - 1], end=' ')
        else:
            print('  ', end='')
        for j, col in enumerate(row):
            if i == 0:
                print(' {} '.format(j), end='')
            else:
                number_len = len(str(j))
                if number_len == 2:
                    print(' ' * (number_len-1) + col, end='')
                else:
                    print(col, end='')
        print()
    for row in tablero:
        for col in row:
            print(col, end="")
        print()


def letra_a_index(letra):
    """
        recibe una letra y devuelve su indice en relación a su posición en la lista ascii_lowercase
    """
    return int(ascii_lowercase.index(letra.lower()))


def parsear_posicion(posicion):
    """
        recibe un string (conformada por una letra en el indice 0 y un integer en el indice 1)
        y devuelve dos posiciones.
    """
    return letra_a_index(posicion[0]), int(posicion[1])


def agregar_elemento(posicion, tablero, elemento):
    """
        recibe un string con un char en el indice 0 y un numero en el indice 1, una matriz de n*n
        y un string para representar las minas. Devuelve una nueva matriz igual a la primera pero
        con una mina en la posicion correspondiente a la posicion del char en el abecedario y el numero.
    """
    x, y = parsear_posicion(posicion)
    nuevo_tablero = tablero
    nuevo_tablero[x][y] = ' {} '.format(elemento.strip()[0])
    return nuevo_tablero


def get_elemento(posicion, tablero):
    """
        recibe un string con un char en el indice 0 y un numero en el indice 1, una matriz de n*n.
        Devuelve el elemento correspondiente a la posicion
    """
    x, y = parsear_posicion(posicion)
    return tablero[x][y]


def popular_tablero_con_minas(tablero, cantidad, mina='*'):
    """
        recibe una matriz de n * n y un numero correspondiente a la cantida de minas para agregar
        al tablero. Como parametro opcional se puede pasar un tipo de mina distinta
    """
    alto, ancho = len(tablero), len(tablero[1])
    nuevo_tablero = tablero
    while cantidad > 0:
        posicion_alto = ascii_lowercase[randint(0, alto - 1)]
        posicion_ancho = randint(0, ancho - 1)
        nuevo_tablero = agregar_elemento('{}{}'.format(
            posicion_alto, posicion_ancho), tablero, mina)
        cantidad -= 1
    return nuevo_tablero


def numero_minas_alrededor(posicion, tablero, mina):
    x, y = parsear_posicion(posicion)
    alto_tablero, ancho_tablero = len(tablero) - 1, len(tablero[0]) - 1
    ancho_rectangulo = 3
    count = 0
    for row in range(ancho_rectangulo):
        for col in range(ancho_rectangulo):
            x1, y1 = (x-1) + row, (y-1) + col
            if (x1 < 0 or y1 < 0) or (x1 > alto_tablero or y1 > ancho_tablero):
                continue
            if tablero[x1][y1].strip() == mina:
                count += 1
            # print(tablero[x1][y1], end='')
    return count


def popular_tablero_con_numeros(tablero):


TABLERO = crear_tablero(
    DIMENSIONES_TABLERO[0], DIMENSIONES_TABLERO[1], PLACEHOLDER)
TABLERO = popular_tablero_con_minas(TABLERO, CANTIDAD_MINAS, MINA)

mostrar_tablero(TABLERO)
# print(get_elemento('a1', TABLERO))
print(numero_minas_alrededor('h7', TABLERO, MINA))
