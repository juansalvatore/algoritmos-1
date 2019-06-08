# Ejercicio 13.4. Escribir una funcion recursiva que reciba como parámetros dos cadenas a y b, y
# devuelva una lista con las posiciones en donde se encuentra b dentro de a.
# Ejemplo:
# posiciones_de("Un tete a tete con Tete", "te") -> [3, 5, 10, 12, 21]

posiciones_lista = [] 
indice = 0
def posiciones(a, b):
    global posiciones_lista
    global indice
    if len(a) == 0:
        return posiciones_lista
    elif a[:len(b)] == b:
        posiciones_lista.append(indice)
    indice += 1
    return posiciones(a[1:], b)

print(posiciones("Un tete a tete con Tete", "te"))