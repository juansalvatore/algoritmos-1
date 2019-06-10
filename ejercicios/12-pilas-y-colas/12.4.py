# Ejercicio 12.4.
# Juego de Cartas
# a) Crear una clase Carta que contenga un palo y un valor.
# b) Crear una clase Solitario que permita apilar las cartas una arriba de otra, pero sólo
# permita apilar una carta si es de un número inmediatamente inferior y de distinto palo
# a la carta que está en el tope. Si se intenta apilar una carta incorrecta, debe lanzar una
# excepción.


class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None


class _Pila:
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
            raise Exception('Pila vacía')
        dato = self.prim.dato
        self.prim = self.prim.prox
        self.len -= 1
        return dato

    def esta_vacia(self):
        return self.len == 0


class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor


class Solitario:
    def __init__(self):
        self.pila = _Pila()

    def apilar(self, carta):
        pila = self.pila
        if pila.esta_vacia():
            pila.apilar(carta)
        else:
            carta_tope = pila.desapilar()
            palo = carta_tope.palo
            valor = carta_tope.valor
            if carta.valor < valor and carta.palo != palo:
                pila.apilar(carta_tope)
                pila.apilar(carta)
            else:
                raise Exception('Error!!')
