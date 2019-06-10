# Del tercer parcialito del primer cuatrimestre de 2012
# 1. Escribir una función reemplazar que tome una Pila, un valor nuevo y un valor viejo y
# reemplace en la Pila todas las ocurrencias de valor viejo por valor nuevo. Considerar que la
# Pila tiene las primitivas apilar(dato), desapilar() y esta vacia().


class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None


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
            raise Exception('Lista vacía!')
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
        return '|\n'.join(arr)


def reemplazar(pila, nuevo, viejo):
    if pila.vacia():
        raise Exception('La pila esta vacia')

    pila_aux = Pila()

    while not pila.vacia():
        tope = pila.desapilar()
        if tope == viejo:
            pila_aux.apilar(nuevo)
        else:
            pila_aux.apilar(tope)
    while not pila_aux.vacia():
        tope = pila_aux.desapilar()
        pila.apilar(tope)
