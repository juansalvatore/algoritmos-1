from string import ascii_uppercase, ascii_lowercase
from random import randint


def crear_tablero(ancho, alto, placeholder='.'):
    """
        recibe dos integers correspondientes al alto y ancho y un string (placeholder) para llenar cada espacio.
        Devuelve una matriz de alto * ancho con un string placeholder en cada posición.
    """
    return [[' {} '.format(placeholder.strip()[0]) for col in range(ancho)] for row in range(alto)]


def mostrar_tablero(tablero):
    """
        recibe una matriz de n * m e imprime la matriz en forma de tablero rectangular n * m con numeros
        como referencia del eje horizontal y letras ascii_uppercase para el eje vertical.
    """
    print()
    for i in range(len(tablero) + 2):
        row = tablero[i - 2]
        if i > 1:
            print(ascii_uppercase[i - 2] + ' |', end='')
        else:
            print('  ', end='')
        for j, col in enumerate(row):
            if i == 0:
                print('  {}'.format(j), end='')
            elif i == 1:
                number_len = len(str(j))
                print(' ' * (number_len-1) + '  -', end='')
            else:
                number_len = len(str(j))
                if number_len == 2:
                    print(' ' * (number_len-1) + col, end='')
                else:
                    print(col, end='')
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
    nuevo_tablero[x][y] = ' {} '.format(str(elemento).strip()[0])
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
        recibe una matriz de n * m y un numero correspondiente a la cantida de minas para agregar
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
    """
        recibe una cadena de caracteres representando una posición, ej: "a1". También recibe una matriz de n * m y 
        un string correspondiente a la representación de las minas en el tablero. Devuelve un integer correspondiente a 
        cuantas minas se encuentran en un radio de un casillero desde el centro "posicion".
    """
    x, y = parsear_posicion(posicion)
    alto_tablero, ancho_tablero = len(tablero) - 1, len(tablero[0]) - 1
    ancho_rectangulo = 3
    count = 0
    for row in range(ancho_rectangulo):
        for col in range(ancho_rectangulo):
            x1, y1 = (x-1) + row, (y-1) + col
            if (x1 < 0 or y1 < 0) or (x1 > alto_tablero or y1 > ancho_tablero):
                continue
            if str(tablero[x1][y1]).strip() == mina:
                count += 1
    return count


def popular_tablero_con_numeros(tablero, mina):
    """
        recibe una matriz de n * m y un string correspondiente a una mina. Retorna un nuevo tablero reemplazando cada
        espacio vacío por el numero correspondiente a la cantidad de minas que tiene alrededor.
    """
    nuevo_tablero = tablero
    for row in range(len(tablero)):
        for col in range(len(tablero[0])):
            if tablero[row][col].strip() == mina:
                continue
            posicion = '{}{}'.format(ascii_lowercase[row], col)
            nuevo_tablero = agregar_elemento(posicion, nuevo_tablero,
                                             numero_minas_alrededor(posicion, nuevo_tablero, mina))

    return nuevo_tablero


def validar_win(tablero, mina, cantidad_minas, placeholder):
    """
        recibe una matriz de n * m, un string correspondiente a una mina, un integer que representa la cantidad de minas que posee la matriz 
        y un string que representa un espacio vacío. Retorna un valor booleano dependiendo de si el jugador ganó o no.  
    """
    count = 0
    for row in tablero:
        for col in row:
            if col.strip() == placeholder:
                count += 1
            if col.strip() == mina:
                return False
    if count == cantidad_minas:
        return True
    return False


def pedir_posicion(mensaje1, mensaje2, ancho, alto):
    """
        recibe dos strings correspondiente a mensajes para pedir posicion, el ancho y el alto del tablero (matriz). 
        Retorna la posicion cuando tenga el formato, ej: "a3" sin importar mayusculas, y cuando la posicion se encuentre
        en las dimensiones del tablero. 
    """
    counter = 0
    while True:
        if counter == 0:
            posicion = input('\n{}'.format(mensaje1))
        else:
            posicion = input('{}'.format(mensaje2))
        if len(posicion) < 2 or (posicion[0] not in ascii_lowercase) or (not posicion[1].isdigit()) or letra_a_index(posicion[0]) > alto or int(posicion[1:]) > ancho:
            counter += 1
            continue
        return posicion


def refrescar_tablero(tablero):
    """
        recibe el tablero a imprimir. Imprime cien saltos de linea para limpiar el tablero anterior y luego imprime el nuevo tablero.
    """
    print("\n" * 100)
    mostrar_tablero(tablero)
