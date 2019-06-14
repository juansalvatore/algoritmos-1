# 4) a) ¿Como deberıa ser un arreglo con n umeros del 1 al 10 para obtener la peor performance
# en una implementacion de quicksort que elige siempre como pivote al ultimo elemento de la
# lista en vez del primero? Justifique.
# b) ¿Que metodo de ordenamiento elegirıa para ordenar ascendentemente un arreglo que ya
# esta ordenado pero en forma descendente? ¿Por que?. Asumiendo que fueran muchos elementos,
# ¿elegirıa este metodo de ordenamiento o utilizarıa una funcion para invertirlos in-place (en el
# mismo arreglo)?

# VER COMPARACIONES ENTRE METODOS DE ORDENAMIENTO


# def quick_sort(lista):
#     if len(lista) < 2:
#         return lista
#     menores, medio, mayores = _partition(lista)
#     return quick_sort(menores) + medio + quick_sort(mayores)


# def _partition(lista):
#     pivote = lista[0]
#     menores = []
#     mayores = []
#     for n in range(1, len(lista)):
#         if lista[n] < pivote:
#             menores.append(lista[n])
#         else:
#             mayores.append(lista[n])
#     return menores, [pivote], mayores

# def insertion_sort(lista):
#     for i in range(1, len(lista)):
#         val = lista[i]
#         p = i
#         while p > 0 and lista[p - 1] > val:
#             lista[p] = lista[p - 1]
#             p -= 1
#         lista[p] = val
#     return lista

def merge_sort(lista):
    if len(lista) < 2:
        return lista
    m = len(lista) // 2
    izq = merge_sort(lista[:m])
    der = merge_sort(lista[m:])
    return _merge(izq, der)


def _merge(lista1, lista2):
    lista_ordenada = []
    i, j = 0, 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            lista_ordenada.append(lista1[i])
            i += 1
        else:
            lista_ordenada.append(lista2[j])
            j += 1
    lista_ordenada += lista1[i:]
    lista_ordenada += lista2[j:]
    return lista_ordenada


print(merge_sort([5, -20, 2, 52, 22, 6, 7, 29, 1]))
