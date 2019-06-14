# Ejercicio 15.2. Mostrar los pasos del ordenamiento de la lista: 6 0 3 2 5 7 4 1 con los métodos
# de inserción y con merge sort. ¿Cuáles son las principales diferencias entre los métodos? ¿Cuál
# usarías en qué casos?


# def ord_insercion(lista):
#     for i in range(1, len(lista)):
#         v_act = lista[i]
#         pos = i
#         while pos > 0 and lista[pos - 1] > v_act:
#             lista[pos] = lista[pos - 1]
#             pos -= 1
#         lista[pos] = v_act


# lista = [6, 0, 3, 2, 5, 7, 4, 1]
# print(lista)
# ord_insercion(lista)
# print(lista)


# def merge_sort(lista):
#     if len(lista) < 2:
#         return lista
#     medio = len(lista) // 2
#     izq = merge_sort(lista[:medio])
#     der = merge_sort(lista[medio:])
#     return merge(izq, der)


# def merge(lista1, lista2):
#     i, j = 0, 0
#     resultado = []

#     while(i < len(lista1) and j < len(lista2)):
#         if (lista1[i] < lista2[j]):
#             resultado.append(lista1[i])
#             i += 1
#         else:
#             resultado.append(lista2[j])
#             j += 1

#     # Agregar lo que falta
#     resultado += lista1[i:]
#     resultado += lista2[j:]

#     return resultado


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    m = len(lista) // 2
    izq = merge_sort(lista[:m])
    der = merge_sort(lista[m:])
    return merge(izq, der)


def merge(lista1, lista2):
    i, j = 0, 0
    nueva_lista = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            nueva_lista.append(lista1[i])
            i += 1
        else:
            nueva_lista.append(lista2[j])
            j += 1
    nueva_lista += lista1[i:]
    nueva_lista += lista1[j:]

    return nueva_lista


lista = [6, 0, 3, 2, 5, 7, 4, 1]

print(lista)
print(merge_sort(lista))
