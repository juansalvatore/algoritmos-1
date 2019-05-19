# Ejercicio 11.9. Implementar el método duplicar(elemento) de ListaEnlazada, que recibe un
# elemento y duplica todas las apariciones del mismo. Ejemplo:

# L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
# L.duplicar(8) => L = 1 -> 5 -> 8 -> 8 -> 8 -> 8 -> 2 -> 8 -> 8


class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None


class LE():
    def __init__(self):
        self.prim = None
        self.len = 0

    def insertar(self, dato, i=None):
        if i is None:
            i = self.len
        if i < 0 or i > self.len:
            raise Exception('Indice incorrecto')
        nuevo = _Nodo(dato)
        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            act = self.prim
            for n in range(1, i):
                act = act.prox
            nuevo.prox = act.prox
            act.prox = nuevo
        self.len += 1
