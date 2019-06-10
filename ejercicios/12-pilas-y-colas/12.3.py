# Ejercicio 12.3. En la parada del colectivo 130 pueden ocurrir dos eventos diferentes:
# • Llega una persona
# • Llega un colectivo con n asientos libres, y se suben al mismo todas las personas que están
# esperando, en orden de llegada, hasta que no quedan asientos libres.
# Cada evento se representa con una tupla que incluye:
# • El instante de tiempo (cantidad de segundos desde el inicio del día)
# • El tipo de evento, que puede ser 'p' (persona) o 'c' (colectivo).
# • En el caso de un evento de tipo 'c' hay un tercer elemento que es la cantidad de asientos
# libres.

# Escribir una función que recibe una lista de eventos, ordenados cronológicamente, y devuel-
# va el promedio de tiempo de espera de los pasajeros en la parada.

# Ejemplo:
# promedio_espera([(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)])
# -> 62.6667 (calculado como (45+99+44) / 3)


class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None


class _Cola:
    def __init__(self):
        self.prim = None
        self.ultimo = None
        self.len = 0

    def encolar(self, dato):
        nuevo = _Nodo(dato)
        if self.len != 0:
            self.ultimo.prox = nuevo
            self.ultimo = self.ultimo.prox
        else:
            self.prim = nuevo
            self.ultimo = self.prim
        self.len += 1

    def desencolar(self):
        if self.len == 0:
            raise ValueError('Cola vacia')
        dato = self.prim.dato
        self.prim = self.prim.prox
        self.len -= 1
        return dato

    def esta_vacia(self):
        return self.len == 0


def promedio_espera(eventos):
    suma = 0
    cola = _Cola()
    personas = 0
    for evento in eventos:
        # llega colectivo
        if evento[1] == 'c':
            tiempo, _, asientos = evento
            while not cola.esta_vacia() and asientos > 0:
                suma += tiempo - cola.desencolar()
                asientos -= 1
        # personas
        else:
            cola.encolar(evento[0])
            personas += 1
    if not personas:
        return 'No hay personas'
    return suma / personas
