# 5. Escribir una funci´on reducir que reciba por par´ametro una cola y una funci´on f de dos
# par´ametros, y aplique sucesivamente la funci´on f a los dos primeros elementos de la cola (luego
# de desencolarlos) y encole el resultado, hasta que solo quede un elemento. La funci´on reducir
# debe devolver el ´unico elemento restante en la cola


class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None


class Cola:
    def __init__(self):
        self.prim = None
        self.ultimo = None
        self.len = 0

    def encolar(self, dato):
        nuevo = _Nodo(dato)
        if self.len == 0:
            self.prim = nuevo
            self.ultimo = self.prim
        else:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        self.len += 1

    def desencolar(self):
        if self.len == 0:
            dato = self.prim.dato
            self.prim = None
            self.ultimo = self.prim
        else:
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
