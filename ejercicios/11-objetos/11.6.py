# Ejercicio 11.6.
# Implementar el método __str__ de ListaEnlazada, para que se genere una
# salida legible de lo que contiene la lista, similar a las listas de python.


class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.len = 0

    def __str__(self):
        act = self.prim
        new_str = ''
        while act:
            if act.prox is not None:
                new_str += f'{act.dato}, '
            else:
                new_str += f'{act.dato}'
            act = act.prox
        return f'[{new_str}]'

    def insert(self, dato, i=None):
        if i is None:
            i = self.len

        if i < 0 or i > self.len:
            raise IndexError('Posición invalida')
        nuevo = _Nodo(dato)

        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            n_ant = self.prim
            for n in range(1, i):
                n_ant = n_ant.prox
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.len += 1

    def pop(self, i=None):
        if i is None:
            i = self.len - 1

        if i < 0 or i > self.len:
            raise IndexError('Posición invalida')

        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for n in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            dato = n_act.dato
            n_ant.prox = n_act.prox
        self.len -= 1
        return dato

    def remove(self, dato):
        if self.len == 0:
            raise ValueError('Lista vacía')

        if self.prim.dato == dato:
            self.prim = self.prim.prox

        else:
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != dato:
                n_ant = n_act
                n_act = n_ant.prox

            if n_act == None:
                raise ValueError('El valor no está en la lista')

            n_ant.prox = n_act.prox
        self.len -= 1


class _Nodo:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
