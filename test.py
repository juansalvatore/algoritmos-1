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
