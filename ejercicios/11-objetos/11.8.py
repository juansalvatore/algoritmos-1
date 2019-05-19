# Ejercicio 11.8.
# Implementar el método remover_todos(elemento) de ListaEnlazada, que re-
# cibe un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad
# de elementos removidos. La lista debe ser recorrida una sola vez.


class _Node:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None


class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.len = 0

    def insert(self, dato, i=None):
        if i is None:
            i = self.len
        if i < 0 or i > self.len:
            raise Exception('Indice incorrecto')
        nuevo = _Node(dato)
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

    def pop(self, i=None):
        if i is None:
            i = self.len - 1
        if i < 0 or i > self.len:
            raise Exception('Indice incorrecto')
        if self.prim is None:
            raise Exception('Lista vacía')
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            ant = None
            act = self.prim
            while act:
                ant = act
                act = act.prox
            dato = act.dato
            ant.prox = act.prox
        self.len -= 1
        return dato

    def remove(self, dato):
        if self.len == 0:
            raise Exception('Lista vacia')
        if self.prim.dato == dato:
            self.prim = self.prim.prox
            self.len -= 1
            return
        ant = None
        act = self.prim
        while act:
            if act.dato == dato:
                ant.prox = act.prox
                self.len -= 1
                return
            ant = act
            act = act.prox

    def __repr__(self):
        s = ''
        act = self.prim
        if self.len == 0:
            return ''
        while act:
            s += str(act.dato) + ', '
            act = act.prox
        return s

    def remover_todos(self, dato):
        if self.len == 0:
            return
        act = self.prim
        sig = act.prox
        while self.prim and self.prim.dato == dato:
            self.prim = self.prim.prox
            self.len -= 1
        while sig:
            if sig.dato == dato:
                act.prox = sig.prox
                sig = sig.prox
                self.len -= 1
                continue
            act = sig
            sig = act.prox
        if act.dato == dato:
            act.prox = sig
