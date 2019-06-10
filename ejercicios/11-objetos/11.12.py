# Ejercicio 11.12. Una lista circular es una lista cuyo último nodo está ligado al primero, de modo

# que es posible recorrerla infinitamente. Escribir la clase ListaCircular, incluyendo los méto-
# dos insert, append, remove y pop.


class _Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.prox = None


class LE:
    def __init__(self):
        self.prim = None
        self.len = 0

    def insert(self, dato, i=None):
        if i is None:
            i = self.len
        nuevo = _Nodo(dato)
        if i < 0 or i > self.len:
            raise Exception('Indice no encontrado')
        if i == 0:
            self.prim = nuevo
            nuevo.prox = self.prim
        else:
            act = self.prim
            for pos in range(1, i):
                act = act.prox
            if i == self.len:
                nuevo.prox = self.prim
                act.prox = nuevo
            else:
                nuevo.prox = act
                act.prox = nuevo
        self.len += 1

    def pop(self, i=None):
        if i is None:
            i = self.len - 1
        if i == 0:
            i = self.len
        if i < 0 and i > self.len:
            raise Exception('Indice no encontrado')
        act = self.prim
        sig = act.prox
        for pos in range(i):
            act = sig
            sig = sig.prox
        if i == self.len:
            self.prim = sig
            act.prox = self.prim
        else:
            act.prox = sig.prox
        self.len -= 1

    def append(self, dato):
        nuevo = _Nodo(dato)
        act = self.prim
        for pos in range(1, self.len):
            act = act.prox
        if self.len == 0:
            self.prim = nuevo
            nuevo.prox = self.prim
        else:
            nuevo.prox = self.prim
            act.prox = nuevo
        self.len += 1

    def __repr__(self):
        arr = []
        act = self.prim
        for pos in range(self.len):
            arr.append(str(act.dato))
            act = act.prox
        return ' - '.join(arr)

    def remove(self, dato):
        if self.len == 0:
            raise Exception('Element not found')
        act = self.prim
        sig = act.prox
        for pos in range(1, self.len):
            if act.dato == dato:
                act.prox = sig.prox
                if pos == self.len:
                    self.prim = sig
                break
            act = sig
            sig = sig.prox
        self.len -= 1


def main():
    l = LE()
    l.append(1)
    l.append(2)
    l.append(3)
    print(l)
    l.remove(1)
    print(l)
    # print(l.prim.dato)
    # print(l.prim.prox.dato)
    # print(l.prim.prox.prox.dato)
    # print(l.prim.prox.prox.prox.dato)
    # print(l.prim.prox.prox.prox.prox.dato)
    # print(l.prim.prox.prox.prox.prox.prox.dato)
    # print(l.prim.prox.prox.prox.prox.prox.prox.dato)
    # print(l)
    # l.pop(0)
    # print(l)
    # l.append('test')
    # print(l)
    # print(l.prim.dato)


main()
