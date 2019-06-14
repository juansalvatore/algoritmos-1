# Ejercicio 15.1. Escribir una función merge_sort_3 que funcione igual que el merge sort pero
# en lugar de dividir los valores en dos partes iguales, los divida en tres (asumir que se cuenta
# con la función merge(lista_1, lista_2, lista_3)). ¿Cómo te parece que se va a comportar
# este método con respecto al merge sort original?

# VER


def merge_sort_3(lista):
    if len(lista) <= 1:
        return lista
    m1 = len(lista) // 3
    m2 = m1 * 2
    izq = merge_sort_3(lista[:m1])
    med = merge_sort_3(lista[m1:m2])
    der = merge_sort_3(lista[m2:])
    return merge(izq, med, der)


def merge(lista1, lista2, lista3):
    i, j, k = 0, 0, 0
    nueva_lista = []

    while i < len(lista1) and j < len(lista2) and k < len(lista3):
        if lista1[i] < lista2[j] and lista1[i] < lista3[k]:
            nueva_lista.append(lista1[i])
            i += 1
        elif lista2[j] < lista1[i] and lista2[j] < lista3[k]:
            nueva_lista.append(lista2[j])
            j += 1
        elif lista3[k] < lista1[i] and lista3[k] < lista2[j]:
            nueva_lista.append(lista3[k])
            k += 1
        else:

    nueva_lista += lista1[i:]
    nueva_lista += lista2[j:]
    nueva_lista += lista3[k:]
    return nueva_lista


lista = [6, 2, 88, 4, 12, -4, -11, 3, 44]
print(merge_sort_3(lista))
