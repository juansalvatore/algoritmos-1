# Ejercicio 14.1.Implementar una función que reciba una lista y devuelva otra
# lista con los mismos elementos que la primera, ordenados de mayor a menor mediante
#  el método de inserción.

#        i  i+1 = p
# lista = [3, 2, 10, 44, 1, 7]


# def ordenar_por_insercion(lista):
#     for i in range(len(lista) - 1):
#         if lista[i] > lista[i + 1]:
#             reubicar(lista, i + 1)
#         continue


# def reubicar(lista, p):
#     v = lista[p]
#     j = p
#     while j > 0 and lista[p - 1] > v:
#         lista[j] = lista[j - 1]
#         j -= 1
#     lista[j] = v


# ordenar_por_insercion(lista)
# print('GUIA', lista)

# # CORRECTO


# def ordenamientoPorInsercion(lista):
#     for indice in range(1, len(lista)):
#         valor_actual = lista[indice]
#         pos = indice

#         while pos > 0 and lista[pos-1] > valor_actual:
#             lista[pos] = lista[pos-1]
#             pos -= 1

#         lista[pos] = valor_actual


# # unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# unaLista = [3, 2, 10, 44, 1, 7]

# ordenamientoPorInsercion(unaLista)
# print('SEG VERSION', unaLista)

# El ordenamiento por inserción, aunque sigue siendo O(n2),
# funciona de una manera ligeramente diferente. Siempre mantiene
# una sublista ordenada en las posiciones inferiores de la lista.
# Cada ítem nuevo se “inserta” de vuelta en la sublista previa de
# manera que la sublista ordenada sea un ítem más larga.


def ord_insercion(lista):
    for i in range(1, len(lista)):
        val_act = lista[i]
        pos = i

        while pos > 0 and lista[pos - 1] > val_act:
            lista[pos] = lista[pos - 1]
            pos -= 1

        lista[pos] = val_act


lista = [22, 1, 4, 3, 124, 5, 0, -123, -2]
print(lista)
ord_insercion(lista)
print(lista)
