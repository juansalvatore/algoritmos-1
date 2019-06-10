# 4. Para una lista simplemente enlazada de números (que solo mantiene una referencia al
# primer nodo) implementar la primitiva suma acumulativa() que devuelva una nueva lista (del
# mismo largo) tal que el nodo i de la nueva lista contenga la suma acumulativa de los elementos
# de la lista origina hasta el nodo i.


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

    def acumulativa(self):
        l = ListaEnlazada()
        suma = 0
        act = self.prim
        l_act = l.prim
        while act:
            suma += act.dato
            nuevo = _Nodo(suma)
            if l_act:
                l_act.prox = nuevo
            else:
                l_act = nuevo
            l_act = l_act.prox
            act = act.prox
        return l
