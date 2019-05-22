# Ejercicio 11.10. Implementar el método filter(f) de ListaEnlazada, que recibe una función

# y devuelve una nueva lista enlazada con los elementos para los cuales la aplicación de f de-
# vuelve True. La nueva lista debe ser construida recorriendo los nodos una sola vez (es decir,

# no se puede llamar a append). Ejemplo:
# L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
# L.filter(es_primo) -> L2 = 5 -> 2


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

    def pop(self, i=None):
        if i is None:
            i = self.len - 1
        if i < 0 or i > self.len:
            raise Exception('Posicion invalida')
        else:
            index = 0
            ant = None
            act = self.prim
            while act and index < i:
                ant = act
                act = act.prox
                index += 1
            if ant is None:
                dato = self.prim.dato
                self.prim = act.prox
            else:
                dato = act.dato
                ant.prox = act.prox
        self.len -= 1
        return dato

    def remove(self, dato):
        if dato is None:
            raise Exception('Dato necesario')
        if self.prim == dato:
            self.prim = self.prim.prox
        else:
            ant = None
            act = self.prim
            while act and act.dato != dato:
                ant = act
                act = act.prox
            if act is not None and act.dato == dato:
                self.prim = self.prim.prox
            else:
                if act.dato != dato:
                    raise Exception('Dato not found')
                ant.prox = act.prox
        self.len -= 1

    def __repr__(self):
        res = []
        act = self.prim
        while act:
            res.append(str(act.dato))
            act = act.prox
        return ' - '.join(res)

    def filter(self, f):
        ant = None
        act = self.prim
        while act:
            if not f(act.dato):
                if ant is None:
                    self.prim = self.prim.prox
                else:
                    ant.prox = act.prox
                self.len -= 1
            ant = act
            act = act.prox


def esPar(n):
    return int(n) % 2 == 0
