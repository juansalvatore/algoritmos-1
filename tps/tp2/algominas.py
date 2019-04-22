from helpers import crear_tablero, mostrar_tablero, letra_a_index, parsear_posicion, agregar_elemento, get_elemento, popular_tablero_con_minas, numero_minas_alrededor, popular_tablero_con_numeros, validar_win, pedir_posicion, refrescar_tablero

# ancho x alto
DIMENSIONES_TABLERO = [8, 8]
MINA = '*'
PLACEHOLDER = '.'
BANDERA = 'P'
EXPLOSION = 'X'
CANTIDAD_MINAS = 10


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

    # Limpia terminal
    refrescar_tablero(tablero)

    while True:
        bandera_o_descubrir = input(
            '\nElegir:\n1- Descubir celda\n2- Poner o quitar bandera\n(Ingrese el numero 1 o 2) ').strip()
        if not bandera_o_descubrir.isdigit() or (int(bandera_o_descubrir) != 1 and int(bandera_o_descubrir) != 2):
            refrescar_tablero(tablero)
            continue

        posicion_elegida = pedir_posicion(
            'Ingrese fila y columna (ejemplo: C3): ', 'Fila o columna incorrecta, intente de nuevo (ejemplo: C3): ', DIMENSIONES_TABLERO[0], DIMENSIONES_TABLERO[1])
        elemento = get_elemento(posicion_elegida, tablero).strip()

        if elemento.isdigit():
            # Limplia terminal
            refrescar_tablero(tablero)
            print('\nCelda ya descubierta.')
            continue

        # descubrir celda
        if int(bandera_o_descubrir) == 1:
            if elemento != BANDERA:
                elemento_escondido = get_elemento(
                    posicion_elegida, tablero_escondido)
                agregar_elemento(posicion_elegida, tablero, elemento_escondido)
                # validar
                if validar_win(tablero, MINA, CANTIDAD_MINAS, PLACEHOLDER):
                    refrescar_tablero(tablero)
                    return print('\nGanaste!')
                if elemento_escondido.strip() == MINA.strip():
                    agregar_elemento(posicion_elegida,
                                     tablero_escondido, EXPLOSION)
                    refrescar_tablero(tablero_escondido)
                    return print('\nGame Over')
            refrescar_tablero(tablero)
            continue

        # poner / sacar bandera
        else:
            if elemento == BANDERA:
                agregar_elemento(posicion_elegida, tablero, PLACEHOLDER)
            else:
                agregar_elemento(posicion_elegida, tablero, BANDERA)
            refrescar_tablero(tablero)
            continue


algominas()
