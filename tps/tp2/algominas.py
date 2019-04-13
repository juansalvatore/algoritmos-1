from helpers import crear_tablero, mostrar_tablero, letra_a_index, parsear_posicion, agregar_elemento, get_elemento, popular_tablero_con_minas, numero_minas_alrededor, popular_tablero_con_numeros

DIMENSIONES_TABLERO = [8, 8]
MINA = '*'
PLACEHOLDER = '.'
CANTIDAD_MINAS = 2


def algominas():
    # Inicializa tablero con minas y numeros
    tablero_escondido = crear_tablero(
        DIMENSIONES_TABLERO[0], DIMENSIONES_TABLERO[1], PLACEHOLDER)
    tablero_escondido = popular_tablero_con_minas(
        tablero_escondido, CANTIDAD_MINAS, MINA)
    tablero_escondido = popular_tablero_con_numeros(tablero_escondido, MINA)

    # Inicializa tablero visible para el usuario
    tablero = crear_tablero(
        DIMENSIONES_TABLERO[0], DIMENSIONES_TABLERO[1], PLACEHOLDER)
    print("\n" * 100)
    mostrar_tablero(tablero)

    while True:
        posicion_elegida = input('\nElegir posición: ')
        elemento = get_elemento(posicion_elegida, tablero_escondido)
        agregar_elemento(posicion_elegida, tablero, elemento)
        print("\n" * 100)
        mostrar_tablero(tablero)
        if elemento.strip() == MINA.strip():
            return print('game over')


algominas()
