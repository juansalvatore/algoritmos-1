
# 2. Escribir un método que invierta una ListaEnlazada utilizando una Pila como estructura
# auxiliar y considerando que lista solo tiene una referencia al primer nodo.


class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None


class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.len = 0

    def insertar(self, dato, i=None):
        if i == None:
            i = self.len
        if i < 0 or i > self.len:
            raise Exception('Indice fuera de la lista')
        nuevo = _Nodo(dato)
        if i == 0:
            self.prim = nuevo
        else:
            act = self.prim
            for _ in range(1, i):
                act = act.prox
            nuevo.prox = act.prox
            act.prox = nuevo
        self.len += 1

    def __str__(self):
        arr = []
        act = self.prim
        while act:
            arr.append(str(act.dato))
            act = act.prox
        return ' - '.join(arr)


class Pila:
    def __init__(self):
        self.prim = None
        self.len = 0

    def apilar(self, dato):
        nuevo = _Nodo(dato)
        if self.len == 0:
            self.prim = nuevo
        else:
            nuevo.prox = self.prim
            self.prim = nuevo
        self.len += 1

    def desapilar(self):
        if self.len == 0:
            raise Exception('Lista vacia')
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


def invertirLista(lista):
    pila = Pila()
    act = lista.prim
    while act:
        pila.apilar(act.dato)
        act = act.prox
    act = lista.prim
    while not pila.vacia():
        act.dato = pila.desapilar()
        act = act.prox
