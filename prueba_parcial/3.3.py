# 3. Escribir una función que reciba una pila de números y elimine de la misma los elementos
# consecutivos que están repetidos. Se pueden usar estructuras auxiliares. La función no devuelve
# nada, simplemente modifica los elementos de la pila que recibe por parámetro.
# Por ejemplo:
# remover duplicados consecutivos(Pila([2, 8, 8, 8, 3, 3, 2, 3, 3, 3, 1, 7]))
# Genera: Pila([2, 8, 3, 2, 3, 1, 7]).


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None


class Pila:
    def __init__(self):
        self.prim = None
        self.len = 0

    def apilar(self, dato):
        nuevo = Nodo(dato)
        if self.len == 0:
            self.prim = nuevo
        else:
            nuevo.prox = self.prim
            self.prim = nuevo
        self.len += 1

    def desapilar(self):
        if self.len == 0:
            raise Exception('Lista vacía')
        dato = self.prim.dato
        self.prim = self.prim.prox
        self.len -= 1
        return dato

    def vacia(self):
        return self.len == 0

    def __str__(self):
        arr = []
        act = self.prim
        while act:
            arr.append(str(act.dato))
            act = act.prox
        return ' - '.join(arr)


def removerDuplicados(pila):
    pila_aux = Pila()
    tope = pila.desapilar()
    pila_aux.apilar(tope)
    while not pila.vacia():
        sig = pila.desapilar()
        if tope != sig:
            pila_aux.apilar(sig)
            tope = sig

    while not pila_aux.vacia():
        pila.apilar(pila_aux.desapilar())
