from helpers import crear_tablero, mostrar_tablero, letra_a_index, parsear_posicion, agregar_elemento, get_elemento, popular_tablero_con_minas, numero_minas_alrededor, popular_tablero_con_numeros, validar_win, pedir_posicion, refrescar_tablero

# ancho x alto (El alto no puede ser mayor a 26)
DIMENSIONES_TABLERO = [8, 8]
MINA = '*'
PLACEHOLDER = '.'
BANDERA = 'P'
EXPLOSION = 'X'
CANTIDAD_MINAS = 30


def algominas():
    """
        recibe como variables globales un array correspondiente a las dimensiones del tablero, un string representando una mina,
        otro representando un espacio vacío (placeholder), otro string representando la bandera, otro representando la explosión y 
        un integer representando la cantida de minas a agregar al tablero. Crea dos tableros, uno escondido (populado con minas y 
        numero de minas alrededor) y otro que se imprime en consola. Permite agregar/quitar banderas al tablero y "descubrir" celdas, 
        esto corresponde a buscar la misma posicion en el tablero escondido y agregandola al tablero visible. Retorna "ganaste" si todas 
        las celdas fueron descubiertas sin encontrar minas, y retorna "Game Over" si se descubre un espacio con minas.
    """
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
        # preguntar si agregar/quitar bandera o descubrir celda
        bandera_o_descubrir = input(
            '\nElegir:\n1- Descubir celda\n2- Poner o quitar bandera\n(Ingrese el numero 1 o 2) ').strip()
        if not bandera_o_descubrir.isdigit() or (int(bandera_o_descubrir) != 1 and int(bandera_o_descubrir) != 2):
            refrescar_tablero(tablero)
            continue

        # pedir posición para agregar/quitar bandera o descubrir celda
        posicion_elegida = pedir_posicion(
            'Ingrese fila y columna (ejemplo: C3): ', 'Fila o columna incorrecta, intente de nuevo (ejemplo: C3): ', DIMENSIONES_TABLERO[0], DIMENSIONES_TABLERO[1])

        # chequea si el elemento presente en la posición elegida es digito
        elemento = get_elemento(posicion_elegida, tablero).strip()
        if elemento.isdigit():
            # Limplia terminal
            refrescar_tablero(tablero)
            print('\nCelda ya descubierta.')
            continue

        # descubrir celda
        if int(bandera_o_descubrir) == 1:
            if elemento != BANDERA:
                # busca el elemento escondido en la posición elegida y lo agrega al tablero visible
                elemento_escondido = get_elemento(
                    posicion_elegida, tablero_escondido)
                agregar_elemento(posicion_elegida, tablero, elemento_escondido)

                # validar si ganó o perdió
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

        # poner/quitar bandera
        else:
            if elemento == BANDERA:
                agregar_elemento(posicion_elegida, tablero, PLACEHOLDER)
            else:
                agregar_elemento(posicion_elegida, tablero, BANDERA)
            refrescar_tablero(tablero)
            continue


algominas()
