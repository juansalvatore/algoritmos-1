# Ejercicio 11.7.
# Agregar a ListaEnlazada un método extend que reciba una ListaEnlazada y
# agregue a la lista actual los elementos que se encuentran en la lista recibida.


class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.len = 0

    def insert(self, dato, i=None):
        if i is None:
            i = self.len
        if i < 0 or i > self.len:
            raise IndexError('El indice no se encuentra')
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
            raise Exception('El indice no existe')
        if self.prim is None:
            raise Exception('Lista vacía')

        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            ant = None
            act = self.prim
            for n in range(1, i):
                ant = act
                act = act.prox
            dato = act.dato
            ant.prox = act.prox
        self.len -= 1
        return dato

    def remove(self, dato):
        if self.len == 0:
            raise ValueError('Lista vacía')
        ant = None
        act = self.prim
        if self.prim.dato == dato:
            self.prim = self.prim.prox
            self.len -= 1
            return dato
        while act:
            if act.dato == dato:
                ant.prox = act.prox
                self.len -= 1
                return dato
            ant = act
            act = act.prox
        raise ValueError('El valor no esta en la lista')

    def extend(self, lista):
        if lista.len == 0:
            return
        act = self.prim
        c_act = lista.prim
        if act is None:
            while c_act:
                act = _Node(c_act.dato)
                act = act.prox
                c_act = c_act.prox
                self.len += 1
        else:
            while act.prox:
                act = act.prox
            while c_act:
                act.prox = _Node(c_act.dato)
                act = act.prox
                c_act = c_act.prox
                self.len += 1

    def __str__(self):
        s = ''
        if self.len == 0:
            return s
        act = self.prim
        while act:
            s += f'{act.dato}, '
            act = act.prox
        return s


class _Node:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
