# Ejercicio 13.7. Escribir una función que calcule recursivamente cuántos elementos hay en una
# pila, suponiendo que la pila sólo tiene los métodos apilar y desapilar, y no altere el contenido
# de la pila.

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
        if self.prim is None:
            self.prim = nuevo
        else:
            nuevo.prox = self.prim 
            self.prim = nuevo
        self.len += 1

    def desapilar(self):
        if self.prim is None:
            raise Exception('Lista vacía')
        dato = self.prim.dato
        self.prim = self.prim.prox
        self.len -= 1
        return dato

    def __str__(self):
        arr = []
        act = self.prim
        while act: 
            arr.append(str(act.dato))
            act = act.prox 
        return ' - '.join(arr)
    
def cant_elementos(pila):
    p = pila
    try:
        p.desapilar()
    except:
        return 0
    return 1 + cant_elementos(p)

def main():
    p = Pila()
    p.apilar(1)
    p.apilar(2)
    p.apilar(3)
    print(p)
    print(cant_elementos(p)) # Modifica la pila actual
    print(p)

main()