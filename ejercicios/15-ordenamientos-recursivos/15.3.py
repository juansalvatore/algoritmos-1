# Ejercicio 15.3. Ordenar la lista 6 0 3 2 5 7 4 1 usando el método quicksort. Mostrar el árbol
# de recursividad explicando las llamadas que se hacen en cada paso, y el orden en el que se
# realizan.


def quick_sort(lista):
    if len(lista) < 2:
        return lista
    menores, medio, mayores = _partition(lista)
    return quick_sort(menores) + medio + quick_sort(mayores)


def _partition(lista):
    pivote = lista[0]
    menores = []
    mayores = []
    for n in range(1, len(lista)):
        if lista[n] < pivote:
            menores.append(lista[n])
        else:
            mayores.append(lista[n])
    return menores, [pivote], mayores


print(quick_sort([6, 0, 3, 2, 5, 7, -4, 1]))
