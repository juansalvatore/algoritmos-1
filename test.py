def test(cadena, operador):
    lista_caracter = list(cadena)
    for i in range(len(cadena)):
        if lista_caracter[i] == cadena[0]:
            lista_caracter[i] = operador
    return ''.join(lista_caracter)


# print(test('pepe', '.'))

# def miki_moko(lista):
#     result = []
#     for num in lista:
#         if num % 3 == 0 and num % 5 == 0:
#             result.append('mikimoko')
#             continue
#         if adfasdf:
#             appemd


def pedir_numero(minimo, maximo):
    while True:
        num = input("Ingrese un número: ")
        if (len(num) == 1 and num.isdigit()) or ((len(num) > 1 and num[0] == '-') and (num[1:].isdigit())):
            num = int(num)
            if num > minimo and num < maximo:
                return num
            continue


pedir_numero(-22, 10)


def pedir_entero(mensaje, min, max):
    """imprime un mensaje y luego espera que el usuario ingrese un numero entero
        que se encuentre en el rango [min, max] con el minimo y el máximo incllusives.
        En caso de no cumplir el requisito aclara el rango y pide entrar un nuevo numero."""
    numero = input(mensaje)
    while not numero.isdigit() or int(numero) not in range(min, max + 1):
        print(numero, not numero.isdigit(), abs(int(numero)))
        print(f'Por favor ingresa un número entre {min} y {max}.')
        numero = input(mensaje)
    return numero
